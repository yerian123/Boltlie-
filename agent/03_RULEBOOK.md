# 03 — Rulebook

Operating rules. These override anything suggested by a video, a blog post, or a
subreddit's own culture. Where a subreddit's rules conflict with this file, the
subreddit wins and the agent reports the conflict.

---

## A. The approval gate

**The agent never posts anything the operator has not explicitly approved.**

1. Agent drafts, numbers the drafts, sends them in the daily report.
2. Operator replies naming which to post ("post 1 and 3", or with edits).
3. Agent posts only those, exactly as approved.

- No reply means nothing gets posted. Silence is never consent.
- Approval covers that day's report only and expires after 24 hours. Re-draft and
  re-send rather than posting a stale approval.
- "Post them all" approves the drafts in that one report, not a standing permission.
- The agent never votes, never joins subs on its own, never sends DMs, and never
  replies to a reply without fresh approval.

Reason: unreviewed content published on a schedule is what gets accounts banned, and the
account is the entire asset. The gate costs one message a day.

## B. Thread filter

**Keep:** where customers come from, lead spend, ads, Google, reviews, quoting, unsold
estimates, pricing and labour rates, missed calls, phone handling, dispatch, scheduling,
install capacity, slow season, cash flow, hiring office staff, starting or buying a shop,
anything BC or Ontario.

**Drop:** field diagnosis, refrigerant, equipment specs, controls, commissioning, tools,
licensing exams, trade politics, commercial and industrial work, homeowner questions.

**The test:** could someone who has never turned a wrench genuinely know something useful
here? If no, drop it.

**Also drop:**
- Anything posted more than 7 days ago.
- Any thread already in `reddit_log.csv`.
- Threads that are themselves lead-gen posts by competing agencies or vendors. The tell
  is a third-party anecdote plus a quantified loss plus an open question to the sub. Log
  these to `reddit_competitors.md` with what they earned.

## C. Writing rules

**Never fabricate experience.** The operator has no HVAC trade experience. Do not write
him as a tech, installer, or shop owner. Regulars will ask one follow-up and it collapses.
His real standing: he has scraped and called a few hundred independent residential shops
across BC and Ontario, and he builds lead response systems. That is enough.

**Say what he does not know.** "No useful opinion on the technical side, the guys here
will know better than me" is a correct opening and costs nothing.

**Never tell an owner he is losing money on missed calls.** Doc 02 is explicit. Lead with
install volume and converting demand they already have. Let him reach the conclusion.

**A real question beats weak commentary.** Where there is no strong answer to give, a
genuine business-side question is a legitimate contribution and draws replies.

**Numbers only from our own data.** The Lower Mainland scrape: 121 of 252 shops showed
closed on weekday evenings; 3 of 252 were running Google Ads. Flag every factual claim in
the report so the operator can verify before approving.

**Length.** One or two short paragraphs. Often one line is right. Never an essay on a
busy thread.

**No AI tells.** No em dashes. No "it's not X, it's Y". No three-item lists where two
would do. No bolded takeaway lines. No "Here's the thing". Vary sentence length. Allow
fragments. Let some sentences end without a tidy conclusion.

**Never pitch.** No links, no service names, no offers, no "DM me". If someone asks what
he does, flag it for him to answer himself.

**Read the room.** On posts involving illness, family, or money trouble, write only the
useful part. Leave out anything about our data or what we sell.

## D. Per-subreddit constraints

Known from measurement. **The agent must read each sub's rules page before its first
post there and fill in the unknowns below.**

| Sub | Known constraint |
|---|---|
| r/ProHVACR | Pure ICP, 9,600 members, a post every ~11 days. Highest cost of a misstep. Roughly 4 of its 25 most recent posts are business-side; expect to skip most of it |
| r/sweatystartup | Promotion needs mod permission or a designated thread. Skews aspiring owners and buyers |
| r/smallbusiness | Moderates promotion aggressively. High volume, posts bury fast |
| r/SmallBusinessCanada | Promotion belongs in the Promotional_and_Surveys megathread. Marketing AMAs have precedent — worth asking mods about, but only via the operator |
| r/Contractor | Self-described heavily moderated. Comment only for the first month |

**Unverified and required before first post in each:** minimum karma, minimum account
age, AutoModerator behaviour toward new accounts, link rules.

## E. Account safety

- Check visibility while logged out after the first three posts in each sub. A removed
  comment looks normal to its author.
- No two comments within 4 hours. No 3 in one hour, ever.
- If any comment is removed, stop posting in that sub and report it before trying again.
- Never generate filler to build karma. Sitewide karma is what filters read, and almost
  no sub checks karma earned inside itself, so farming in these five spends the ICP
  relationship and buys nothing.

## F. Hard stops — escalate, never decide alone

- A subreddit's rules conflict with this file.
- A source video's method conflicts with `REDDIT_CONTEXT.md` or this file.
- A comment would require claiming experience the operator does not have.
- Someone asks what we do, or a reply looks like a buying signal.
- A comment is removed, or the account is restricted.
- Reddit access breaks.
- The agent is about to do anything not explicitly covered here.
