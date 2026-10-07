---
name: log-calls
description: Logs a calling session from Yerian's quick notes (e.g. "Spurr VM, Ashton talked - booked till Feb, call back Nov 3, Smith NI"), updates every lead's status and next call date, records objections word for word, and reports progress against the validation gates and kill switch. Use after any calling block, or when Yerian pastes call notes.
---

# Log calls

## Steps
1. Turn each note into one engine command. The codes are:
   NA no answer · VM voicemail · GK gatekeeper · NI not interested · CB callback · NF not a fit · MTG meeting booked · CONV talked to the owner, no decision yet.
   ```
   python3 outbound/engine.py log "<Company>" <CODE> [--note "<short note>"] [--objection "<their exact words>"] [--cb YYYY-MM-DD]
   ```
   - If the note gives a call date, use `--cb`. If someone says "don't call again", also run `set "<Company>" "Do not call" "Y"`.
   - If an owner name or number was wrong, fix it with `set`.
   - For an after-hours check (calls at night), use `afterhours "<Company>" VM|NA|ANSWERED` instead of `log`.
2. If a note is ambiguous (which company, which outcome), ask. Don't guess.
3. Run `python3 outbound/engine.py stats` and report: this week vs targets (75 dials / 5 conversations / 1 meeting), validation progress, and any objection that came up twice or more.
4. If the **kill switch** prints (300+ dials, 0 meetings), say so plainly and suggest what to fix (opener, list or timing), using the logged objections as evidence.
5. For every MTG: draft the follow-up confirmation with `/draft-message`, and suggest running the `boltline-sales-conversations` skill for meeting prep.
