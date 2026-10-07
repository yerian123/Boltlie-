---
name: refresh-signals
description: Signal agent. Re-checks buying signals (Google/LSA ads, Meta ads, hiring, evening hours, review counts) on existing leads and updates their Heat score so the hottest shops get called first. Use weekly, before a calling block, or when Yerian says "refresh the list", "who's hot", "check signals".
---

# Refresh signals (the "heat" agent)

This is TryGTM's "watches buying signals and scores intent", run on our own list.

## Steps
1. Run `python3 outbound/engine.py score` to see the current split.
2. Pick what to check, in this order: leads not yet called, then leads with a callback or retry due this week. Skip `Do not call`, `MTG`, `NI` and `NF`. Default batch is 25.
3. For each lead, check and update with `python3 outbound/engine.py set "<Company>" "<Column>" "<value>"`:
   - **Hiring?:** search Indeed for a tech, installer, CSR or dispatcher posting from the last 60 days. Value: `Y - '<title>' posted <date> (Indeed <url>)` or `None found (<date>)`.
   - **Running ads? (Meta…):** search the Meta Ad Library tool for the company/page name. Value: `Meta - <n> active ads as of <date>: '<headline>'` or `None found (<date>)`.
   - **Google Ads / LSA:** Ads Transparency Center if reachable, otherwise `Unknown`.
   - **Closed weekday evenings:** from their Google hours, if visible.
   - **Review count / rating:** only if a fresh source shows them. Say where it came from.
4. Run `python3 outbound/engine.py score` again. Report which leads **moved up**, with the new signal and its source, and which went quiet.

## Rules
- Every value carries a date and a source. "Not found" stays "not found", not "no".
- New *companies* spotted while checking go into a "next run" list for `/find-leads`. Don't add them to the CSV without the full ICP screen.
- If a tool rate-limits you, stop and list what wasn't checked. Don't retry in a loop.
