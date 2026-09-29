# HVAC Lead List — Ontario GTA — 2026-09-29

**File:** `HVAC_Leads_ON-GTA_2026-09-29.csv` (64 rows)
**Status: stopped early at 64 of the 150 target.** The research tool hit its session cap of 200 web searches during the second sweep. All 11 cities got a first pass. The region still has companies nobody has looked at yet (listed at the bottom). A new session can pick up from `.leadbuilder_progress.json`.

## Read this first: how this run was limited

1. **I couldn't open websites directly.** This environment's network policy blocked direct page loads: company sites, Google Maps, BBB, HomeStars and Yelp were all refused. Everything comes from **web-search result summaries**, plus the **Meta Ad Library** and **Indeed** tools, which did work. As a result:
   - **"Website loads" could not be tested for any row.** Each row's website is the one search results point to. Rows with no website found at all (8) were taken out of the CSV and are listed below.
   - **Google rating and review counts are mostly Birdeye or NSO.ca aggregates**, and are labelled that way in the CSV. Birdeye mostly mirrors Google but isn't identical. Rows labelled "(Google, per search summary)" came from a search summary quoting Google. Check the real Google listing before quoting a number on a call.
   - Owner sources are the pages the search summaries cited (BBB, company About pages, LinkedIn, HomeStars reviews). Where the only source was a data aggregator (ZoomInfo or RocketReach), confidence is set to Low.
2. **The Meta ad check is keyword-based.** Meta Ad Library search matches ad text, not page names. It confirmed **2 companies running Meta ads right now** (Special Gas Services and Spurr Heating). For everyone else, "Unknown" means *not found*, not *not running*.
3. **Hiring:** the Indeed searches turned up only one qualifying posting from the last 60 days (Spring Home, Sep 22). Dynamic Heating's posting is from Oct 2025, outside the window.
4. **Scores are low on purpose.** Unknown = 1, as the rules say, so rows with unverified ratings, no hiring info and no response-gap evidence land in B/C. Only **1 lead scores A (16+)**. Many B-tier companies could move up to A once someone checks Google reviews or the Ad Library by hand.
5. **The zip you attached arrived empty (0 bytes), and the repo was empty.** So there were no EXISTING_LISTS to de-duplicate against. The only known earlier list, `BC_HVAC_Prospects_Batch1.csv`, covers BC, so overlap is unlikely, but it wasn't checked.

## Counts

| | Count |
|---|---|
| Candidates reviewed | 149 |
| Included in CSV | 64 |
| Held back (fit, but no website found) | 8 |
| Excluded | 77 |

**Included by tier:** A = 1, B = 54, C = 9

**Owner found, by confidence:** High = 12, Medium = 24, Low = 16, None = 12

**Included by city:** Barrie 4, Brampton 9, Burlington 5, Hamilton 11, Markham 6, Mississauga 12, Oakville 5, Oshawa 3, Richmond Hill 3, Vaughan 3, Whitby 3

**Excluded by reason (77):**

| Reason | Count | Examples |
|---|---|---|
| Multi-location brand / brand network | 17 | Aire One (Peel, Markham, East, Barrie), HVAC Trust, Green Heating & Air (5 locations), Constant Home Comfort, AirTemp HVAC, LG Home Comfort, Superior Plumbing & Heating, 3 ClimateCare members* |
| One-truck operator / thin history | 14 | Olympic Heating (owner does all the work), Beyond HVAC, Doug Scott, Elmridge, Just Air |
| Large operator (50+ staff / huge volume) | 11 | Applewood, A1 Air, AtlasCare, Shipton's, Martino HVAC, Superior HVAC Service (85+ techs), Lancaster Group, A-Plus Air, Dr HVAC (6 offices) |
| Not residential HVAC / not a contractor | 11 | Red Line Mechanical, Consult Mechanical, MGT Mechanical, Airway Systems, Home Trade Standards, EMCO, Metalworks |
| Franchise / national brand / PE-owned | 9 | Reliance, Enercare (incl. Abbey Air), Service Experts (incl. **Peel Heating** and **Limcan Certified**, both Service Experts-owned), Aire Serv, Climate Air (bought by Right Time / Gryphon PE) |
| Out of region / outside listed cities | 9 | Toronto: Laird & Son, Culzac, Megacity, Imperial, Ace Air, Metropolitan. Milton: Free Air. Uxbridge: Marx Mechanical |
| Insufficient info / unverifiable | 4 | ZK Mechanical, Direct Heating & Cooling, Mersey Heating (virtual office), Bay Tech (NY phone number) |
| Rental / financing model | 1 | Ontario Efficiency Group ("$59.99/month" ads). LG Home Comfort counted under multi-location |
| Reputation | 1 | High Life Heating & AC (3.8 on ~197 reviews) |

\*ClimateCare members (Woodbridge GTA ClimateCare, Advantage Airtech, Custom Comfort) are locally owned but trade under a shared co-op brand. I excluded them to be safe. **Your call:** if co-op members count as independents, they're good targets.

## 10 best leads

Only one lead reaches A. The other nine are the highest-scoring B-tier leads.

| Tier | Score | Company | City | Phone | Owner (confidence) | Hook |
|---|---|---|---|---|---|---|
| A | 17 | Dynamic Heating and Cooling | Hamilton | (289) 962-4811 | Shawn Mount (High) | Grew from a 2019 start to 600+ five-star Google reviews and 2,000+ projects |
| B | 15 | Ashton Heating & Cooling Inc. | Oshawa (Courtice) | (905) 240-6055 | Bill Ashton (Medium) | 4.9 stars from 515 Google reviews; a reviewer describes Bill personally installing a furnace over the holidays |
| B | 15 | Creature Comforts HVAC Inc. | Burlington | (289) 983-1383 | Grant Gray; Dale Gray (High) | Voted Burlington's Best Heating & Cooling Contractor and Family Business 2013-2026; 5.0 stars on ~1,035 reviews |
| B | 15 | Smith Heating & Cooling Inc. | Hamilton (Dundas) | (905) 379-4248 | Nathan Smith (High) | 5.0 stars from ~104 reviews; reviewers name Nathan for punctuality and communication |
| B | 15 | Spring Home Heating & Cooling Systems Inc. | Markham | (416) 272-8898 | George Li (Medium) | Hiring an HVAC installation technician on Indeed (posted Sep 22) |
| B | 15 | Spurr Heating & Air Conditioning Inc. | Hamilton | (905) 526-4875 | Chad Spurr (Medium) | Running a $99.99 furnace check ad on Facebook right now (started Sep 25) |
| B | 15 | Taunton Trades Ltd. | Whitby | (905) 493-4227 | Sean Lemery (High) | 4.9 stars from ~169 reviews; owner Sean Lemery has 25+ years in the trade |
| B | 14 | Air Flow Heating & Cooling Ltd. | Mississauga | (905) 507-2665 | Hossein Ovisi; Rod Sedaghat (Medium) | 4.9 stars from ~133 reviews; customers name Rod for fast arrival |
| B | 14 | Cozy World Inc. | Richmond Hill | (416) 855-3651 | Boris Sherman (Medium) | In business since 1991; 4.9 stars from ~252 reviews |
| B | 14 | Econoair Heating & Cooling Inc. | Richmond Hill | (905) 763-2400 | Eiden Patros (co-founder with Dani) (Medium) | 4.9 stars from ~430 reviews; offers same-day appointments and 24/7 emergency repair |

Two confirmed ad spenders are worth calling early: **Spurr Heating & Air Conditioning** (Hamilton) is running a $99.99 furnace-check ad on Facebook right now. **Special Gas Services** (Brampton) has had a "Your Local HVAC Company in Brampton" ad running since about Sep 8.

## Check before calling

- **Call block timing.** Every row uses "Lunch 12:00–12:45 PT", as the prompt specifies for Ontario. But 12:00 PT is **3:00 pm in Ontario**, not lunchtime there. If the goal is to catch Ontario owners at their own lunch, the window is **9:00–9:45 am PT**. Please confirm which one you meant.
- **Size could be over the limit (confirm under ~50 staff):** Creature Comforts (~1,035 reviews), Husky (~1,105), Maple Air (~1,314), Spurr (~1,100 Google), Furnace King (~907), HAMCO (632, serves 7+ towns), Dynamic (746).
- **Owner sources disagree:** Husky (BBB says Alex Fedontchouk, another source says Justin James). HAMCO (Thomas E. vs John Vasilak). Econoair (Eiden Patros on the site, but one review calls "Bruce" the owner). Convertible (three Amodeo family names).
- **Phone numbers disagree:** Tenacity HVAC (289-962-7918 vs 289-253-8036). Anything Gas Master Mechanical (705-720-2842 vs 705-305-3654). D.A.D. HVAC and Convertible only turned up toll-free numbers.
- **Possible affiliation:** HVAC Zack (Oshawa) has the same street address as an Oshawa listing for Superior HVAC Service, a large operator. Check whether they're linked.
- **Check for multiple locations/brands:** Ontario Heating Ltd has a "Locations" page. Furnace & AC Experts lists both a Mississauga and a Brampton address, and sources give different founding dates (2015 vs "28+ years").
- **Water-heater rental risk:** Uniworth and a few others install water heaters. Before calling, skim recent reviews for rental-contract complaints (the CBC pattern). None turned up in search summaries.
- **Response-gap hooks need a gentle touch:** HVAC Mechanical Systems (reviews about late arrivals) and Air Solutions Heating & Cooling (reviews about unanswered warranty calls). Use these as discovery questions, not openers.
- **First-name-only owners (Low):** Evam ("Ed"), MH Heating ("Hadi"), Delta T ("Lomesh"), Admore ("Yama"), Castlemore ("Raj"), 905 HVAC ("Omar"), Markham Heating ("Vijay"), TopCare ("Muhaib"). Ask for them by first name, or ask who handles marketing.

## Held back: fit the profile but no website found

These failed the "website loads" QA check, so they're not in the CSV. The phones come from their listings, so you can still call them if you want.

| Company | City | Phone | Owner | Why held |
|---|---|---|---|---|
| Seasonal Home Comfort Heating & A/C Inc. | Mississauga | (416) 937-5620 | Larry Sadowski | No website found |
| Airmax Heating and Cooling | Brampton | (647) 779-9710 | Sunny (surname unknown) | No website found |
| City's Choice Comfort Air | Brampton | (647) 999-0828 | Andre Dyer | No website found |
| Ringers HVAC Services Inc. | Hamilton (Stoney Creek) | (905) 745-9215 | Alan Ringer | No website found |
| The Ontario HVAC Group | Richmond Hill | (437) 385-1339 | — | No website found |
| Barrie Heating & Air Conditioning | Barrie | (705) 734-0054 | Todd (surname unknown) | No website found |
| Air Solutions Heating & Cooling Inc. | Barrie | (705) 719-4777 | — | No website found |
| Burrr Heating & Air (Burrr-lington Heating) | Barrie (Minesing) | (705) 737-7021 | Dan Burlington; Dan Murphy | No website found |

## Untapped companies for the next run

Names found but never researched, because the search budget ran out:
- **Mississauga:** Ontario Energy Care HVAC Services (195 reviews; check for a rental model first), MWS HVAC (35), Custom Contracting, Weston Plumbing & Mechanical, Ekam, AN Heating Cooling Support, NR HVAC Solutions (22).
- **Brampton:** GM Heating & Cooling (86 reviews, 24/7), Mr. HVAC Services.
- **Hamilton:** AirPro Heating & Cooling (137 reviews, 5.0), Ashland Heating & AC (28).
- **Vaughan:** RS Mechanical (Woodbridge), PC Mechanical Services, North Wind HVAC.
- **Oakville:** Quickfast.
- **Oshawa:** True North Home Comfort.
- **Barrie:** Bros Home Services (35).
- **Whitby:** Plumbing & Heating Heroes (plumbing-led, low priority).

Where the region still has the most room:
- **Hamilton and Brampton** have the most independents per search.
- **Oakville and Richmond Hill** are the thinnest (dominated by large or multi-location brands).
- **Toronto proper**, **Milton/Georgetown/Halton Hills** and **Durham outside Oshawa/Whitby** (Ajax, Pickering, Bowmanville, Uxbridge) are the obvious next regions. Several Toronto and Milton fits are already in the excluded list above.

## QA summary

- Phone format: all 64 CSV numbers normalised to (XXX) XXX-XXXX; no invalid numbers.
- Duplicates: none by phone or website domain.
- No franchise or excluded brand names in the CSV. Cozy World was first logged as Toronto, then included under its Richmond Hill office; its exclusion entry was removed.
- Every named owner has a source URL. Every hook has a source URL.
- Rows with no website were moved to the held-back table (8). No row's website could be load-tested, because of the network block.
- Two rows (Ontario Heating, Sentral HVAC) were downgraded to Low owner confidence: their only source was a data aggregator.
- No owner direct lines were recorded. None were published by the businesses in the sources seen. No people-search or data-broker phone numbers were used.

---

## Update, Sep 29 2026: ads and hiring rechecked

This was a follow-up pass on the same 64 leads, using the two tools that still work in this session: the Meta Ad Library and Indeed. No new companies were added. A new browser-based run (Google Maps, Facebook, LinkedIn) couldn't happen here because this session has no Chrome or computer tools, and the network blocks those sites.

**Running Meta ads now (confirmed on Sep 29):**
- **Spurr Heating & Air Conditioning** (Hamilton): 5 active "$99.99 Check" furnace tune-up ads, started Sep 25.
- **Special Gas Services** (Brampton): 5 active ads. The newest started Sep 14 ("Serving Brampton and surrounding areas").
- **Burlington Heating & Air Conditioning** (Burlington): *new find*. Two active ads: "Instant Rebates Up to $1,250 on Trane Systems" (started Sep 23) and "Rebates Up to $1,250 on HVAC Systems" (started Sep 28).
- **Central Heating** (Barrie): *new find, likely match*. The page "Central Heating and Air conditioning Barrie" is running "Get $1,500 OFF Your Heating & AC System" (started Sep 16) and "Heating & AC for $116/Month" (started Sep 2). Confirm it's the same company. The $116/month offer is financing; check it isn't a rental contract.

**Hiring now (posted in the last 60 days, from Indeed):**
- **Maple Air** (Vaughan): HVAC Service Technician (Sep 19) and HVAC Lead Dispatcher (Sep 3). **Now A-tier (16).**
- **Central Heating Inc.** (Barrie): Dispatcher (Sep 24). Score is now 15.
- **Precision HVAC Mechanics** (Oakville): part-time HVAC Administrative Assistant (Sep 21). Hiring office help is a good response-gap discovery angle. Score is now 14.
- **Spring Home Heating & Cooling** (Markham): the Sep 22 installer posting didn't come back in a name search today. It may have closed, or the search just missed it. Kept as Y.

**Tier changes:** A is now 2 (Dynamic Heating & Cooling, Maple Air), B is 53, C is 9. Burlington Heating went from 11 to 12.

**New flag:** **Tenacity HVAC**'s only Indeed posting ("Join the Tenacity HVAC Family", March 2026) was listed under the employer **Veracity Electric Inc**. That could mean a shared owner or a multi-company group. Check before calling.

**How reliable these checks are:**
- Both tools search by keyword, so both miss things. The Meta name search didn't surface Special Gas Services' ads (they were only found by Page ID). The Indeed name search didn't return Spring Home's known posting.
- So "None found" in the CSV means *not found*, not *confirmed none*. Scores for those rows stay at 1 (unknown).
- **Not checked on Indeed** (the tool started rate-limiting, so I stopped rather than retry): Delta T, Evam, Anything Gas, HVAC Zack, The Heatman, Admore, Gas Fitter Complete, MY HVAC guy, Markham Heating, TopCare, AOBUTEC, Castlemore, First Choice, HVAC-Group, Heat Flow, MH Heating, Peatson's, Tropic Air.

**New companies seen hiring on Indeed.** None of these are in the CSV. They're candidates for the next run and need the full screen first:
- **JP Home Comfort** (Brampton): heat pump and ductless installer, Sep 26.
- **Absolute Comfort Heating & Air Conditioning** (Mississauga): lead service/install tech, Sep 16.
- **Guest Plumbing and HVAC** (Hamilton): lead HVAC tech, Sep 8.
- **Ideal Heating and Air Conditioning** (Vaughan): G3 technician, Sep 14.
- **Comfort Air Solutions** (Concord): dispatcher, Sep 8.
- **Green Life HVAC** (Concord): installer, Sep 15.
- **Air Source Home Comfort** (Barrie): service tech, Sep 21.
- **Enterprise Mechanical** (Barrie): G2 tech, Sep 1.
- **Pinewood Heating & A/C** (Pickering): installer, Sep 23.
- **Climate Experts Heating & Cooling** (Pickering): residential service tech, Sep 11.
- **Marx Mechanical** (Uxbridge): residential tech, Sep 25. Already logged as outside the listed cities.
- **Screen carefully first:** Go Lime Inc. (GTA, several postings; may be multi-location) and Peak Home Comfort (Toronto).
