# 05 — Daily Report

## Delivery

One channel, swappable. Configured in `agent/config.json` as `notify_channel`.

| Channel | Status |
|---|---|
| `email` | **Working today.** Gmail MCP is connected. Default |
| `whatsapp` | Needs setup. No WhatsApp MCP is connected in this environment. See README |

The report goes out once a day after the morning sweep. Alerts (section below) go out
immediately, any time.

## Daily report format

Keep it short enough to read on a phone. The drafts are the body; everything else is one
line each.

```
Reddit — <date>

SCANNED  <n> threads across 5 subs
PASSED   <n> filter
DRAFTED  <n>

--- DRAFTS (reply with the numbers to post) ---

[1] r/<sub> — "<thread title>"
    <age>, <n> comments
    <url>

    <the draft comment>

    VERIFY: <factual claims to check, or "nothing">

[2] ...

--- INBOUND FLAGS ---
<thread where an ICP-shaped owner describes a problem we solve, with url and one line
on why. "None" if none.>

--- YESTERDAY ---
<each comment posted yesterday: upvotes, replies>

--- NEEDS YOU ---
<anything from Rulebook section F. "Nothing" if nothing.>
```

Reply format the operator can use: `post 1 and 3`, `post 2 with: <edited text>`,
`skip all`, or no reply at all, which posts nothing.

## Immediate alerts, not held for the daily

Send straight away:

- A reply to one of our comments from someone who looks like the ICP.
- Anyone asking what we do, or any buying signal.
- A comment removed, or the account restricted.
- Reddit access broken.

These go cold in hours, which is the whole argument of our own offer. Do not sit on them.

## Weekly report, Monday

```
Reddit — week to <date>

POSTED      <n> comments
ENGAGEMENT  <n> drew replies, <n> drew none
VISIBILITY  <confirmed visible logged out: yes/no per sub>
RULES       <any change on the five rules pages>
CONVERSATIONS <any ongoing exchange with an ICP owner>
```

## Monthly review, first Monday

Report: which subs and topics produced replies and DMs; re-measured members, posts/day
and median comments for the five subs; what the ranking is being changed to; what is
being dropped and why.

## Logging

Every posted comment appends to `reddit_log.csv`:

```
date,subreddit,thread_url,thread_title,upvotes,replies,dm_received,notes
```

Refresh upvotes and replies at the Monday check for anything posted in the last 14 days.
