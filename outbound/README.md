# Boltline outbound agent

A do-it-yourself version of tools like TryGTM ($297/mo), pointed at the channels Boltline uses now: **cold calls first**, with written messages only to people who've engaged. It runs inside Claude Code, so there's no extra monthly cost.

| TryGTM does | Here | How |
|---|---|---|
| Finds people matching your ICP | `/find-leads` | Screens independent residential HVAC shops and writes a sourced CSV |
| Watches buying signals | `/refresh-signals` | Re-checks Google/LSA ads, Meta ads, hiring, evening hours and reviews |
| Intent "heat" score | `engine.py score` | Goldilocks signals → Heat score, HOT ≥ 5, WARM ≥ 3 |
| Writes in your voice | `/call-prep`, `/draft-message` | Openers and messages from `voice.md` plus each shop's sourced hook |
| Sends, paced | You | You dial; written drafts land in Gmail and you send them |
| Tracks replies, books calls | `/log-calls`, `engine.py stats` | Statuses, retries, callbacks, objections, gates, kill switch |

## Daily loop (about 5 minutes of setup)
1. `/call-prep`: today's sheet in `outbound/sheets/`, hottest leads first, each with an opener.
2. Call during your windows. The sheet shows each lead's local time and flags anything outside CRTC hours.
3. `/log-calls` and paste your notes ("Spurr VM, Ashton talked - booked till Feb, Smith NI").
4. Weekly: `/refresh-signals`. Whenever the queue runs low: `/find-leads`.

## Engine commands
```
python3 outbound/engine.py score
python3 outbound/engine.py queue --n 15
python3 outbound/engine.py log "Spurr" VM
python3 outbound/engine.py log "Ashton" CONV --objection "We're booked till February"
python3 outbound/engine.py log "Taunton" CB --cb 2026-10-14
python3 outbound/engine.py afterhours "Smith Heating" VM
python3 outbound/engine.py set "Maple Air" "Closed weekday evenings (Y/N/Unknown)" "Y (Google hours, Oct 7)"
python3 outbound/engine.py stats
```
Codes: NA, VM, GK, NI, CB, NF, MTG, CONV. Every dial is appended to `outbound/call_log.csv`.

## Rules built in
- Max 5 attempts per shop; voicemail on attempt 3 only; NA/VM retried after 3 days, gatekeeper after 2.
- `channels.cold_email` is `false` until Gate 2 and a mailing address exist (CASL). Only you flip it.
- Lead files are listed in `config.json` → `lead_files`. Add each new list there.

## Privacy note
This repo is **public**. Lead CSVs with owner names and your call notes are visible to anyone. Consider making the repo private on GitHub (Settings → General → Danger Zone → Change visibility) before logging real calls.
