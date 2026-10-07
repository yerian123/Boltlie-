#!/usr/bin/env python3
"""Boltline outbound engine: heat scoring, daily call queue, call logging, gate stats.

The research and writing (finding shops, checking signals, writing openers) is done by
the Claude skills in .claude/skills/. This script does the deterministic bookkeeping so
the numbers stay honest.

Usage (run from the repo root):
  python3 outbound/engine.py score                         # recompute Heat for every lead
  python3 outbound/engine.py queue [--n 15] [--date YYYY-MM-DD]
  python3 outbound/engine.py log "Company" CODE [--note ..] [--objection ..] [--cb YYYY-MM-DD]
  python3 outbound/engine.py set "Company" "Column" "Value"
  python3 outbound/engine.py afterhours "Company" VM|NA|ANSWERED
  python3 outbound/engine.py stats

Call codes: NA no answer, VM voicemail, GK gatekeeper, NI not interested, CB callback,
NF not a fit, MTG meeting booked, CONV owner conversation with no decision yet.
"""
import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outbound"
CONFIG = json.loads((OUT / "config.json").read_text())
CALL_LOG = OUT / "call_log.csv"
SHEETS = OUT / "sheets"

CODES = {"NA", "VM", "GK", "NI", "CB", "NF", "MTG", "CONV"}
CONVERSATION_CODES = {"NI", "CB", "NF", "MTG", "CONV"}
CLOSED_CODES = {"NI", "NF", "MTG"}

EXTRA_COLUMNS = [
    "Heat", "Heat level", "Heat reasons", "Google Ads / LSA (Y/N/Unknown + source)",
    "Closed weekday evenings (Y/N/Unknown)", "After-hours result", "Next call date",
    "Objections (word for word)",
]


# ---------- CSV storage ----------

def load_leads():
    """Return list of (path, fieldnames, rows) for every configured lead file."""
    files = []
    for rel in CONFIG["lead_files"]:
        path = ROOT / rel
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fields = list(reader.fieldnames)
            rows = list(reader)
        for col in EXTRA_COLUMNS:
            if col not in fields:
                fields.append(col)
        for row in rows:
            for col in fields:
                row.setdefault(col, "")
                if row[col] is None:
                    row[col] = ""
        files.append((path, fields, rows))
    return files


def save_leads(files):
    for path, fields, rows in files:
        tmp = path.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        tmp.replace(path)


def find_lead(files, name):
    needle = name.lower().strip()
    exact = [(f, r) for f in files for r in f[2] if r["Company"].lower() == needle]
    if exact:
        return exact[0]
    hits = [(f, r) for f in files for r in f[2] if needle in r["Company"].lower()]
    if not hits:
        sys.exit(f"No lead matches '{name}'.")
    if len(hits) > 1:
        names = "\n  ".join(r["Company"] for _, r in hits)
        sys.exit(f"'{name}' matches more than one lead:\n  {names}\nUse more of the name.")
    return hits[0]


# ---------- Heat scoring ----------

def first_number(text, as_float=False):
    m = re.search(r"\d[\d,]*(\.\d+)?", text or "")
    if not m:
        return None
    value = m.group(0).replace(",", "")
    return float(value) if as_float else int(float(value))


def is_yes(text):
    return (text or "").strip().upper().startswith("Y")


def heat(row):
    """Score how 'ready to buy' a shop looks right now, using the Goldilocks signals."""
    w = CONFIG["heat"]
    score, reasons = 0, []

    ads = row.get("Running ads? (Meta/Google/None/Unknown + source)", "")
    if is_yes(row.get("Google Ads / LSA (Y/N/Unknown + source)")) or re.match(r"\s*(Google|LSA)", ads):
        score += w["google_ads"]
        reasons.append(f"buys Google/LSA leads +{w['google_ads']}")
    if ads.strip().startswith("Meta"):
        reasons.append("running Meta ads +0 (check if agency-run; HOLD 90 days if heavy)")

    if is_yes(row.get("Hiring? (Y/N + source)")):
        score += w["hiring"]
        reasons.append(f"hiring now +{w['hiring']}")

    if is_yes(row.get("Closed weekday evenings (Y/N/Unknown)")):
        score += w["closed_evenings"]
        reasons.append(f"closed weekday evenings +{w['closed_evenings']}")

    if row.get("After-hours result", "").upper().startswith(("VM", "NA")):
        score += w["after_hours_unanswered"]
        reasons.append(f"after-hours call unanswered +{w['after_hours_unanswered']}")

    reviews = first_number(row.get("Google review count"))
    rating = first_number(row.get("Google rating"), as_float=True)
    if reviews is not None:
        if reviews > 1000:
            score += w["reviews_too_many"]
            reasons.append(f"{reviews} reviews, may be too big {w['reviews_too_many']}")
        elif 50 <= reviews <= 600 and (rating or 0) >= 4.0:
            score += w["reviews_sweet_spot"]
            reasons.append(f"{reviews} reviews at {rating} +{w['reviews_sweet_spot']}")
        elif reviews < 20:
            score += w["reviews_too_few"]
            reasons.append(f"only {reviews} reviews {w['reviews_too_few']}")
        else:
            score += w["reviews_ok"]
            reasons.append(f"{reviews} reviews +{w['reviews_ok']}")

    if row.get("Owner confidence (High/Medium/Low/None)", "").strip() == "High":
        score += w["owner_high_confidence"]
        reasons.append(f"owner name confirmed +{w['owner_high_confidence']}")

    level = "HOT" if score >= w["hot"] else "WARM" if score >= w["warm"] else "COLD"
    return score, level, "; ".join(reasons)


def rescore(files):
    for _, _, rows in files:
        for row in rows:
            row["Heat"], row["Heat level"], row["Heat reasons"] = (str(x) for x in heat(row))


# ---------- Queue ----------

def parse_date(text):
    try:
        return dt.date.fromisoformat((text or "").strip())
    except ValueError:
        return None


def attempts(row):
    return first_number(row.get("Call attempts")) or 0


def callable_today(row, today):
    if is_yes(row.get("Do not call")):
        return False
    if row.get("Outcome", "").strip().upper() in CLOSED_CODES:
        return False
    if attempts(row) >= CONFIG["max_attempts"]:
        return False
    due = parse_date(row.get("Next call date"))
    return due is None or due <= today


def windows_for(row, day):
    """Your call windows converted to the lead's local time, checked against CRTC hours."""
    mine = ZoneInfo(CONFIG["your_timezone"])
    tz_name = CONFIG["province_timezones"].get(row.get("Province", "").strip().upper())
    if not tz_name:
        return "unknown province: check their local time before dialing"
    theirs = ZoneInfo(tz_name)
    weekend = day.weekday() >= 5
    lo, hi = (dt.time.fromisoformat(t) for t in CONFIG["crtc_hours"]["weekend" if weekend else "weekday"])
    parts = []
    for start, end in CONFIG["your_call_windows"]:
        a = dt.datetime.combine(day, dt.time.fromisoformat(start), mine).astimezone(theirs)
        b = dt.datetime.combine(day, dt.time.fromisoformat(end), mine).astimezone(theirs)
        ok = lo <= a.time() and b.time() <= hi
        parts.append(f"{start}-{end} yours = {a:%H:%M}-{b:%H:%M} theirs {'OK' if ok else 'OUTSIDE CRTC HOURS'}")
    return " | ".join(parts)


def queue(files, n, today):
    leads = [r for _, _, rows in files for r in rows if callable_today(r, today)]

    def key(r):
        callback_due = r.get("Outcome", "").upper() == "CB"
        return (not callback_due, -int(r.get("Heat") or 0), attempts(r), -(first_number(r.get("Fit score")) or 0))

    return sorted(leads, key=key)[:n]


def write_sheet(picked, today):
    SHEETS.mkdir(exist_ok=True)
    path = SHEETS / f"call-sheet-{today.isoformat()}.md"
    lines = [f"# Call sheet: {today:%a %b %d, %Y}", "",
             f"{len(picked)} leads. Callbacks due come first, then hottest. Log each dial with "
             "`python3 outbound/engine.py log \"Company\" CODE`.", ""]
    for i, r in enumerate(picked, 1):
        attempt = attempts(r) + 1
        vm = "LEAVE A VOICEMAIL if no answer" if attempt == CONFIG["voicemail_on_attempt"] else "No voicemail"
        lines += [
            f"## {i}. {r['Company']} ({r['City']}, {r['Province']})",
            f"- **Phone:** {r['Main phone']}  |  **Ask for:** {r['Owner name'] or 'the owner'} "
            f"({r.get('Owner confidence (High/Medium/Low/None)', '')} confidence)",
            f"- **Heat:** {r['Heat']} {r['Heat level']} ({r['Heat reasons'] or 'no signals yet'})",
            f"- **Attempt {attempt} of {CONFIG['max_attempts']}.** {vm}.",
            f"- **When:** {windows_for(r, today)}",
            f"- **Hook:** {r.get('Call hook', '')} ({r.get('Hook source URL', '')})",
            f"- **Last outcome:** {r.get('Outcome') or 'never called'} {r.get('Last call date', '')}".rstrip(),
            "- **Opener:** _(written by /call-prep)_",
            "",
        ]
    path.write_text("\n".join(lines))
    return path


# ---------- Logging and stats ----------

def append_log(entry):
    new = not CALL_LOG.exists()
    with CALL_LOG.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "company", "code", "attempt", "note", "objection"])
        if new:
            writer.writeheader()
        writer.writerow(entry)


def log_call(files, args, today):
    code = args.code.upper()
    if code not in CODES:
        sys.exit(f"Unknown code {code}. Use one of: {', '.join(sorted(CODES))}")
    _, row = find_lead(files, args.company)
    n = attempts(row) + 1
    row["Call attempts"] = str(n)
    row["Last call date"] = today.isoformat()
    row["Outcome"] = code
    row["Status"] = {"MTG": "Meeting booked", "NI": "Not interested", "NF": "Not a fit",
                     "CB": "Callback"}.get(code, "In progress")
    if code == "CB":
        row["Next call date"] = args.cb or (today + dt.timedelta(days=7)).isoformat()
    elif code in CONFIG["retry_days"]:
        row["Next call date"] = (today + dt.timedelta(days=CONFIG["retry_days"][code])).isoformat()
    else:
        row["Next call date"] = ""
    if args.objection:
        prev = row.get("Objections (word for word)", "")
        row["Objections (word for word)"] = f"{prev} | {today}: \"{args.objection}\"".strip(" |")
    if args.note:
        row["Notes"] = f"{row.get('Notes', '')} [{today} {code}: {args.note}]".strip()
    if n >= CONFIG["max_attempts"] and code not in CLOSED_CODES | {"CB"}:
        row["Status"] = "Max attempts reached"
    append_log({"date": today.isoformat(), "company": row["Company"], "code": code, "attempt": n,
                "note": args.note or "", "objection": args.objection or ""})
    print(f"Logged {code} for {row['Company']} (attempt {n}). Next call: {row['Next call date'] or 'none'}.")


def stats(today):
    if not CALL_LOG.exists():
        print("No calls logged yet. Dials: 0.")
        return
    rows = list(csv.DictReader(CALL_LOG.open(encoding="utf-8")))
    week_start = today - dt.timedelta(days=today.weekday())

    def count(rs):
        return (len(rs), sum(r["code"] in CONVERSATION_CODES for r in rs), sum(r["code"] == "MTG" for r in rs))

    total = count(rows)
    week = count([r for r in rows if parse_date(r["date"]) and parse_date(r["date"]) >= week_start])
    g = CONFIG["gates"]["validation"]
    print(f"This week:  {week[0]} dials, {week[1]} owner conversations, {week[2]} meetings "
          "(targets: 75+ / 5+ / 1+)")
    print(f"All time:   {total[0]} dials, {total[1]} conversations, {total[2]} meetings")
    print(f"Validation: dials {total[0]}/{g['dials']}, conversations {total[1]}/{g['conversations']}, "
          f"meetings {total[2]}/{g['meetings']}, clients: track by hand")
    if total[0]:
        print(f"Rates:      {total[1] / total[0]:.0%} of dials reach an owner, "
              f"{(total[2] / total[1]) if total[1] else 0:.0%} of conversations book")
    if total[0] >= CONFIG["gates"]["kill_switch_dials"] and total[2] == 0:
        print("KILL SWITCH: 300+ dials and 0 meetings. Stop dialing; fix the opener or the list first.")
    objections = [r["objection"] for r in rows if r["objection"]]
    if objections:
        print(f"\nObjections logged ({len(objections)}):")
        for o in objections[-10:]:
            print(f"  - \"{o}\"")


# ---------- CLI ----------

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--date", help="pretend today is this date (YYYY-MM-DD)")
    sub = p.add_subparsers(dest="cmd", required=True)
    add = lambda name: sub.add_parser(name, parents=[common])
    add("score")
    q = add("queue")
    q.add_argument("--n", type=int, default=CONFIG["daily_dials"])
    lg = add("log")
    lg.add_argument("company")
    lg.add_argument("code")
    lg.add_argument("--note")
    lg.add_argument("--objection")
    lg.add_argument("--cb", help="callback date YYYY-MM-DD")
    st = add("set")
    st.add_argument("company")
    st.add_argument("column")
    st.add_argument("value")
    ah = add("afterhours")
    ah.add_argument("company")
    ah.add_argument("result", choices=["VM", "NA", "ANSWERED"])
    add("stats")
    args = p.parse_args()

    today = parse_date(args.date) or dt.date.today()
    if args.cmd == "stats":
        stats(today)
        return

    files = load_leads()
    if args.cmd == "queue":
        rescore(files)
        picked = queue(files, args.n, today)
        save_leads(files)
        print(f"Wrote {write_sheet(picked, today).relative_to(ROOT)} ({len(picked)} leads)")
        return
    if args.cmd == "log":
        log_call(files, args, today)
    elif args.cmd == "set":
        f, row = find_lead(files, args.company)
        if args.column not in f[1]:
            sys.exit(f"No column '{args.column}'. Columns: {', '.join(f[1])}")
        row[args.column] = args.value
        print(f"{row['Company']}: {args.column} = {args.value}")
    elif args.cmd == "afterhours":
        _, row = find_lead(files, args.company)
        row["After-hours result"] = f"{args.result} {today.isoformat()}"
        print(f"{row['Company']}: after-hours {args.result}")
    rescore(files)
    save_leads(files)
    if args.cmd == "score":
        hot = sum(r["Heat level"] == "HOT" for _, _, rows in files for r in rows)
        warm = sum(r["Heat level"] == "WARM" for _, _, rows in files for r in rows)
        total = sum(len(rows) for _, _, rows in files)
        print(f"Scored {total} leads: {hot} HOT, {warm} WARM, {total - hot - warm} COLD")


if __name__ == "__main__":
    main()
