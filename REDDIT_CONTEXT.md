# Reddit Channel — Context

Last updated: Nov 2, 2026.
Source docs: `02_ICP_and_Market.md`, `02a_Owner_Quote_Bank.md`, `02b_Reddit_Subreddit_Targets.md`.

---

## 1. The ICP

From `02_ICP_and_Market.md`:

- Independent **residential** HVAC company in Canada, outside Quebec. BC Lower Mainland
  first, then Alberta and Ontario, then the US by email later.
- 3–15 technicians, roughly $1M–$5M revenue, owner-run, owner answers or is easy to reach.
- Able to fund about $1,500/month in ad spend.
- **Not:** franchises (Reliance, Enercare, Service Experts, One Hour, Aire Serv),
  private-equity-owned groups, brands with 1,000+ Google reviews, suppliers,
  commercial-only shops.

Highest-priority signals: already paying for Google Ads or Local Services Ads; shows
"Closed" on weekday evenings; hiring a tech, installer, CSR or dispatcher now; 50–600
Google reviews at 4.0+; owner reachable on the main line.

Hard disqualifier: a shop that is booked solid. Five owners in the quote bank say some
version of "I'm turning away half my work."

Market size: 16,621 plumbing/HVAC firms with employees in Canada (6,428 with 5–49 staff).
BC 2,885. Ontario 6,523. Lower Mainland qualified call list: 252 independents.

Seasons: October–March furnace and heat pump. April–September AC.

---

## 2. Status

**Done:** subreddit targeting research, measured live and committed. Six comments drafted.

**Not done:** nothing has been posted. The Reddit account is at 1 karma. Subreddit rules
text is unverified for all five targets.

**Never happened:** the training video was not watched. `www.youtube.com` and
`reddit.com` are both denied by this environment's network policy. Nothing in these docs
comes from the video.

---

## 3. The five target subreddits

Measured Oct 23–24, 2026.

| # | Subreddit | Members | Posts/day | Median comments |
|---|---|---|---|---|
| 1 | r/ProHVACR | 9,600 | 0.09 | 13 |
| 2 | r/sweatystartup | 212,000 | 1.0 | 31 |
| 3 | r/smallbusiness | 2,600,000 | 68.5 | 7 |
| 4 | r/SmallBusinessCanada | 37,000 | 1.4 | 5 |
| 5 | r/Contractor | 65,000 | 10.2 | 9 |

What each is:

- **r/ProHVACR** — the only living HVAC-owner subreddit. Charter is "For HVAC/R business
  owners and operators." One post appears every ~11 days, so a post stays at the top of
  the sub for over a week. Roughly 4 or 5 of its 25 most recent posts are business-side;
  the rest are technical.
- **r/sweatystartup** — highest engagement on the list. Skews aspiring owners and people
  buying a shop rather than established 3–15 tech shops.
- **r/smallbusiness** — largest pool of home-service owner-operators. High volume, so
  posts are buried quickly.
- **r/SmallBusinessCanada** — Canadian, posts tagged by province ([BC], [ON], [AB]). Has a
  promotional megathread and a precedent for marketing AMAs.
- **r/Contractor** — adjacent trade, owner-level business discussion. Self-described
  heavily moderated.

Second tier:

| Subreddit | Members | Posts/day | Median comments |
|---|---|---|---|
| r/canadasmallbusiness | 26,000 | 8.1 | 1 |
| r/businessowners | 39,000 | 12.4 | 5 |
| r/fieldservice | 3,800 | 1.3 | 7 |

---

## 4. Research findings

**All HVAC-owner subreddits except r/ProHVACR are dead.** r/HVACBUSINESS has 10 members.
r/HVAC_SALES has 3. r/hvacleads last post Sep 2025. r/hvactechs last post 2022.
r/HVACprofessionals last post Feb 2024. r/HomeServices last post ~2020.

**Geo subreddits contain no shop owners.** "HVAC" in r/vancouver returns 0 hits in a year.
In r/britishcolumbia, 16 hits, all apprenticeship or career questions.

**Homeowner subs are not the ICP.** r/hvacadvice (298,000 members, 139 posts/day) and
r/askHVAC (8,100) are homeowners asking diagnosis questions.

**r/HVAC is technicians.** 246,000 members. Sidebar states non-trade members should post
elsewhere. Recent posts are flaired Meme/Shitpost, Rant, Field Question.

**Marketing subreddits are competitors, not customers.** r/PPC, r/GoogleAds,
r/FacebookAds, r/marketing, r/digital_marketing, r/SEO, r/localseo, r/agency.

**Offer posts measured at 1–4 comments. Value-first posts at 30–90.** Competitors already
posting the same offer in r/businessowners: "Building an AI lead response system for
HVAC/plumbing companies" got 1 comment. "Built a lead gen and CRM tool for home service
businesses" got 3 and 4.

**A competitor is already running this play in r/canadasmallbusiness.** "Why HVAC
businesses in Ontario should not rely only on Lead Ads on Facebook?" got 3 comments.
"Call tracking gap silently starving an HVAC campaign's bidding data" got 1.

**An HVAC owner raised the missed-call problem unprompted in r/smallbusiness**, 82
comments: "Ran an HVAC shop in Tampa for years... every missed call was probably a
customer calling the next guy." Top reply, 15 points: "You basically need to find a way
to hire someone. It's losing you far more money than it would cost to hire a
receptionist." This closes the gap in doc 02 that said no owner had ever raised
text-back or missed calls in their own words.

---

## 5. How the data was gathered

52 subreddits tested, 47 returned data, r/HVACR does not exist. Member counts, posting
rates and comment medians read from Reddit listing data on Oct 23–24, 2026 by driving
headless Chromium through a public Redlib mirror, because Reddit's own endpoints are
blocked by this environment and Reddit returns 403 to datacenter IPs.

`posts/day` is the 25 newest posts divided by the time they span. `median comments` is
the median across those same 25 posts.

Subreddit rules pages could not be read, because the mirror truncates sidebars.
