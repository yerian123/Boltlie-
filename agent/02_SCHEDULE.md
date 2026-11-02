# 02 — Schedule

All times America/Vancouver.

## Daily, 07:30 — sweep and draft

1. Pull posts from the last 7 days across the five target subs.
2. Apply the filter in `03_RULEBOOK.md`.
3. Rank survivors. Draft the top 2–3.
4. Write `reddit_queue.md`.
5. Send the daily report (see `05_REPORT.md`).

## Daily, on reply — post approved comments

Triggered by the operator's reply to the report, not by the clock.

Post only the comments they named, exactly as approved or with the edits they gave.
Then log each to `reddit_log.csv`. If no reply arrives, post nothing.

## Daily, 18:00 — check for responses

Check every thread in `reddit_log.csv` from the last 14 days for new replies to our
comments. If an ICP-shaped owner replied, or anyone asked what we do, send an alert
immediately rather than waiting for tomorrow's report. Those are the conversations the
channel exists for and they go cold in hours.

## Weekly, Monday 08:00 — standing check

- Re-read the rules pages of all five subs. Note any change.
- Confirm our recent comments are still visible when logged out. Silent removal is the
  main failure mode and it does not announce itself.
- Report upvote and reply counts for everything posted in the last 7 days.

## Monthly, first Monday — review

- Which subs and which topics produced replies and DMs?
- Re-measure members, posts/day and median comments for the five subs.
- Adjust the ranking weights toward whatever actually worked.
- Report what changed and what is being dropped.

## Pacing limits

- Maximum 3 comments drafted per day, and never more than 1 per subreddit per day.
- Minimum 4 hours between posts.
- Never post 3 comments inside one hour. That is the pattern that trips spam filters
  regardless of content quality.
