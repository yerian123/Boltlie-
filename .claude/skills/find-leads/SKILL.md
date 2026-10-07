---
name: find-leads
description: Sourcing agent. Builds a new list of independent residential HVAC shops for a region, screens them against the Boltline ICP, and drops them into the Boltline Outbound app for Yerian to add with one click. Use when Yerian says "find leads", "build a list for <city/region>", "more shops", or the call queue is running dry.
---

# Find leads (sourcing agent)

Replaces TryGTM's "find people matching your ICP". Quality over volume: a few hundred real local owners beat a 700M-contact database.

## Input
Region and cities (e.g. "Lower Mainland: Surrey, Langley, Burnaby"), target count (default 50), and any existing lead files to de-duplicate against (always check the app's `leads` collection).

## ICP (screen every company)
**Include:** independent, owner-run, **residential** HVAC (furnace, heat pump, AC installs) in Canada outside Quebec. About 3–15 technicians and roughly $1M–$5M revenue.

**Exclude, logging the reason and a source:**
- Franchises and national brands: Reliance, Enercare, Service Experts, One Hour, Aire Serv, and any shop they own
- Private-equity groups and multi-location brands
- More than about 1,000 Google reviews or 50+ staff (too big)
- One-truck operators or under about 20 reviews (too small)
- Commercial-only shops, suppliers, rental/financing-model companies
- Under 4.0 stars

## Signals to capture (these drive the Heat score)
For each included shop, fill what you can find and **cite a source URL for every fact**:
- Google rating and review count (say where the number came from)
- `Google Ads / LSA (Y/N/Unknown + source)`: check the Google Ads Transparency Center, or note "Unknown"
- `Closed weekday evenings (Y/N/Unknown)`: from their Google hours
- `Hiring? (Y/N + source)`: a tech, installer, CSR or dispatcher posting from the last 60 days (Indeed tool)
- `Running ads? (Meta/Google/None/Unknown + source)`: Meta Ad Library tool
- Owner name, title and confidence (High = named on their own site, BBB or LinkedIn; Low = only data aggregators)
- `Call hook`: one specific, true, sourced fact about this shop that an owner would be glad someone noticed

"Not found" means unknown, never "no". Never invent a number, a name or a hook.

## Output (goes straight into the Boltline Outbound app)
1. Read the existing leads first so you don't duplicate: `ArtifactData` action `list` on https://claude.ai/artifact/K4KwGv5bJSwBrWUoFcoJfW, collection `leads` (page with `query.cursor`). Match on company name and phone.
2. Write ALL new shops as ONE document in the `imports` collection (doc id like `surrey-2026-10-07`):
   `{"source": "<region> agent run <date>", "createdAt": "<ISO time>", "status": "pending", "rows": [ ...leads ]}`
   Each row uses the app's field names: `company, city, province, phone, owner, ownerConf, email, website, facebook, rating, reviews, hiring, ads, googleAds, closedEvenings, hook, hookUrl, angle, notes, tier, source, attempts: 0, stage: "new"`. Put source links and dates inside the field text (e.g. `"Y - 'Installer' posted Oct 2 (Indeed <url>)"`).
3. Yerian presses **Add them** on the Today tab to bring them in. Tell him how many you found, the HOT/WARM split by the app's heat rules, and the top 10 with their hooks.
4. Keep an exclusion log (company, reason, source) in your reply or in `13 — Outbound/` if he asks for a file.

## Rules
- Business phone numbers and owner names only from public business sources. No people-search sites, no personal cell numbers, no data brokers.
- Collect an email only if the business itself publishes it (on its site or Google listing). Note where. Never guess email patterns. Cold email is switched off anyway until Gate 2.
- If your search budget runs out, save progress to `13 — Outbound/.leadbuilder_progress.json` and say which cities are left.
