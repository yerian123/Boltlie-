---
name: draft-message
description: Drafts written messages in Yerian's voice for the channels Boltline allows right now - meeting confirmations after a call, follow-ups to owners who asked for info, warm-referral follow-ups, and replies to Facebook group members who replied or asked. Cold email stays locked until Gate 2. Use when Yerian says "write a follow-up", "text Mike", "reply to this guy", "send him the info".
---

# Draft message

## Gate check (do this first)
Read `channels` in `outbound/config.json`.
- **Allowed now:** a reply to someone who contacted Yerian or asked for info on a call; a meeting confirmation; a follow-up to a warm referral; a DM to someone who replied in a Facebook group or asked.
- **Locked:** cold email to someone who never engaged (`cold_email: false` until Gate 2 and a mailing address exist) and anything on LinkedIn. If asked, explain why and offer a call opener instead. Only Yerian changes the config.

## Steps
1. Read `outbound/voice.md`. Match it: short, spoken, plain, no hype.
2. Use only true, sourced facts about the recipient (the lead CSV, call notes). No invented familiarity ("loved your post!"), no made-up results.
3. Write one message: who Yerian is → why he's writing (the call, their question, the referral) → one useful thing → one easy next step with an easy no.
4. Email drafts include Yerian's name, "Boltline Growth", how to reach him, and a line saying they can reply "stop" and he won't follow up. Add the mailing address once one exists.
5. Run the `humanizer` skill over the draft to strip AI-sounding phrasing.
6. **Save it as a draft, never send.** If the Gmail connector is available, create a Gmail draft; otherwise show the text. Yerian reads and sends every message himself.
7. Follow-up limit: one follow-up after silence, then stop. Stop immediately on "no", "stop" or "wrong person", and mark `Do not call` / do-not-contact in the CSV.
