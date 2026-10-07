---
name: call-prep
description: Call-prep agent. Builds today's call sheet (callbacks due first, then hottest leads), does 2-minute pre-call research on each shop, and writes a personalised opener in Yerian's voice and script framework. Use when Yerian says "prep my calls", "who do I call today", "call sheet", "calling block".
---

# Call prep

TryGTM writes "evidence-grounded copy" for email. We write it for the phone, which is the main channel until Gate 2.

## Steps
1. Run `python3 outbound/engine.py queue` (add `--n <number>` if Yerian gives one; the default is 15). It writes `outbound/sheets/call-sheet-<date>.md`.
2. Read `outbound/voice.md` before writing anything.
3. For each lead on the sheet, do the 2-minute research: Google profile and hours, the hook source, any ad or hiring signal. Confirm the hook is still true; if you can't, swap in a question instead of a claim.
4. Replace each `**Opener:** _(written by /call-prep)_` line with:
   - **Opener (say this):** 2–3 spoken sentences. "Hey <first name>, Yerian with Boltline Growth. I'll be quick." Then the reason for the call, tied to *their* hook. End with "Got a sec?"
   - **Problem question:** one question built on their signal. Hiring: "Sounds like you're busy. Who catches the calls when the techs are out?" Closed evenings: "What happens to calls after 5?" Ads: "How are those furnace check ads doing for you?"
   - **If they bite:** the book-it line with two specific slots inside Yerian's call windows.
   - **Watch out for:** anything from the sheet's checks (size, owner name disputes, wrong number risk).
5. Give Yerian a short summary in chat: how many leads, how many HOT, the best 3 to call first and why.

## Rules
- Never claim something about the shop you didn't verify. A question is always safe.
- Never quote industry stats to owners as fact ("34% of calls go unanswered"). Those are PATTERN-level evidence only.
- Never promise leads, jobs or revenue. Pricing and age answers come from `outbound/voice.md`; tell the truth on age.
- Respect the sheet's "When" line. Never schedule a dial marked OUTSIDE CRTC HOURS.
