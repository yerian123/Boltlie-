# Reddit Channel Agent

Five files. Load all of them into the agent's instructions, in order.

| File | What it is |
|---|---|
| `01_GOAL.md` | What the agent is for, what success and failure look like |
| `02_SCHEDULE.md` | When it works and what it does on each run |
| `03_RULEBOOK.md` | How it operates. The approval gate, the thread filter, writing rules, per-sub constraints, hard stops |
| `04_PLAYBOOK.md` | The business. ICP, offer, our data, the evidence against us, what never to claim |
| `05_REPORT.md` | Report formats, alert triggers, logging |
| `config.json` | Settings: subs, pacing limits, notification channel |

Also give it read access to `REDDIT_CONTEXT.md`, `02_ICP_and_Market.md`,
`02a_Owner_Quote_Bank.md`, and `02b_Reddit_Subreddit_Targets.md`.

---

## Setup

### 1. Reddit access

Use the official API, not browser automation. Reddit blocks datacenter IPs on normal page
loads but the API works fine from anywhere, and it does not break when they change their
HTML.

Create a **script** app at `reddit.com/prefs/apps`. Store the client ID and secret as
environment variables (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`) wherever the agent
runs. Never in a file in this repo.

Read-only scope covers the sweep. Posting needs the `submit` scope and an authorised
account.

### 2. Notifications

**Email works now.** The Gmail MCP is connected. `notify_channel: "email"` in
`config.json` and nothing else to do.

**WhatsApp needs wiring.** There is no WhatsApp MCP in this environment. Two routes:

- **WhatsApp Business Cloud API** (Meta). Create an app, get a phone number ID and a
  permanent access token, then have the agent POST to the messages endpoint. Note that
  Meta only allows free-form messages inside a 24-hour window after the user messages
  you; outside it you need an approved template. For a daily report you will want a
  template.
- **Twilio's WhatsApp sender.** Simpler to start, and their sandbox works immediately for
  a number you have opted in. Account SID, auth token, and the `whatsapp:` prefixed
  from/to numbers.

Either way, set `notify_channel: "whatsapp"` and `notify_whatsapp` to the destination
number, and keep credentials in environment variables.

The report content does not change between channels. Only the send step does.

### 3. Scheduling

Four jobs, from `02_SCHEDULE.md`: daily sweep at 07:30, response check at 18:00, weekly
check Monday 08:00, monthly review first Monday. All America/Vancouver.

The approval run is not scheduled. It fires when you reply to the report.

### 4. Before the first post

The agent must read all five subreddits' rules pages and record minimum karma, minimum
account age, AutoModerator behaviour toward new accounts, and link rules. This is a known
gap in the research and it decides whether a post survives at all.

The account is at 1 karma. If any sub filters new accounts, the agent should report that
and post nothing there until the threshold is met elsewhere.

---

## How a day runs

1. 07:30, agent sweeps, filters, drafts 2–3, sends you the report.
2. You read it on your phone and reply `post 1 and 3`.
3. Agent posts those two, four hours apart, and logs them.
4. 18:00, agent checks for replies on everything from the last 14 days.
5. Anything that looks like a buying signal reaches you immediately, not tomorrow.

Your part is one message a day.

## What the agent will not do

It will not post anything you have not named in that day's report, vote, join subs on its
own, send DMs, reply to a reply without fresh approval, generate filler to build karma,
or claim trade experience the operator does not have. Those are in `03_RULEBOOK.md`
sections A, C and E, with the reasoning.
