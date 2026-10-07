---
name: find-leads
description: Sourcing agent. Builds a new list of independent residential HVAC shops for a region, screens them against the Boltline ICP, and writes a CSV the outbound engine can score and queue. Use when Yerian says "find leads", "build a list for <city/region>", "more shops", or the call queue is running dry.
---

# Find leads (sourcing agent)

Replaces TryGTM's "find people matching your ICP". Quality over volume: a few hundred real local owners beat a 700M-contact database.

## Input
Region and cities (e.g. "Lower Mainland: Surrey, Langley, Burnaby"), target count (default 50), and any existing lead files to de-duplicate against (always include every file in `outbound/config.json` → `lead_files`).

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

## Output
1. `13 — Outbound/HVAC_Leads_<REGION>_<YYYY-MM-DD>.csv`, using the **same columns as the existing lead CSV** (open it and copy the header). Status = `Not called`.
2. `..._report.md` (counts, top 10, things to check before calling) and `..._excluded_log.md` (company, reason, source).
3. Add the new CSV path to `lead_files` in `outbound/config.json`.
4. Run `python3 outbound/engine.py score` and report the HOT/WARM/COLD split.

## Rules
- Business phone numbers and owner names only from public business sources. No people-search sites, no personal cell numbers, no data brokers.
- Collect an email only if the business itself publishes it (on its site or Google listing). Note where. Never guess email patterns. Cold email is switched off anyway until Gate 2.
- If your search budget runs out, save progress to `13 — Outbound/.leadbuilder_progress.json` and say which cities are left.
