---
name: refresh-signals
description: Signal agent. Re-checks buying signals (Google/LSA ads, Meta ads, hiring, evening hours, review counts) on existing leads and updates their Heat score so the hottest shops get called first. Use weekly, before a calling block, or when Yerian says "refresh the list", "who's hot", "check signals".
---

# Refresh signals (the "heat" agent)

This is TryGTM's "watches buying signals and scores intent", run on our own list.

## Steps
1. Read leads from the Boltline Outbound app: `ArtifactData` action `list` on https://claude.ai/artifact/K4KwGv5bJSwBrWUoFcoJfW, collection `leads` (page through with `query.cursor`). Note each document's `version`.
2. Pick what to check: leads in stage `new` or `contacted` with the highest heat (signals: googleAds +3, hiring +2, closedEvenings +2, afterHours VM/NA +2, 50–600 reviews at 4.0+ +2), plus anyone whose `nextCall` is this week. Skip `dnc: true`. Default batch 30.
3. For each lead, check: Indeed (hiring a tech, installer, CSR or dispatcher in the last 60 days), Meta Ad Library (active ads), Google hours (closed weekday evenings), Google rating and review count, Google Ads Transparency if reachable.
4. Write back only changed fields with `ArtifactData` action `batch` (op `update`, `if_version` = the version you read). Values carry a date and source, e.g. `hiring: "Y - 'HVAC Installer' posted Oct 3 (Indeed <url>)"`, `ads: "Meta - 2 active ads as of Oct 7: '<headline>'"`.
5. Report which leads moved up and why, which went quiet, and new companies spotted (those go to `/find-leads`, not straight into the app).

## Rules
- Every value carries a date and a source. "Not found" stays "not found", not "no".
- New *companies* spotted while checking go into a "next run" list for `/find-leads`. Don't add them to the app without the full ICP screen.
- If a tool rate-limits you, stop and list what wasn't checked. Don't retry in a loop.
