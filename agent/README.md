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

**Do not plan around the Reddit API.** Reddit announced on Sep 30, 2026 that it is closing
public API access:

| Date | What happens |
|---|---|
| Oct 31, 2026 | New public API access requests no longer accepted |
| Nov 13, 2026 | RSS feed support ends |
| Jan 12, 2027 | Unregistered apps begin losing access |
| March 2027 | Public Data API access ends for everything remaining |

New access is already closed, and the free tier was non-commercial only in any case. This
use is commercial. Reported commercial pricing is roughly $12,000/month. Verify the dates
against Reddit's own developer documentation before acting on them, but do not build on
the Data API.

**What to do instead.** The API was never needed at this volume. The agent reads five
subreddits once a day and drafts at most three comments. Its value is the filtering and
the drafting, and neither requires API access, only the thread text.

Two workable arrangements:

- **Operator gathers, agent drafts.** The operator skims the five subs and pastes anything
  interesting. The agent applies the filter in `03_RULEBOOK.md`, drafts, and reports. No
  API, no cost, no rate limits, nothing to break in March 2027. This is the default.
- **Browser session on the operator's own machine.** A logged-in Chrome session is not API
  access and is unaffected by the shutdown dates. More fragile, and automating it at volume
  conflicts with Reddit's terms, so keep it to the pacing limits in `02_SCHEDULE.md`.

Either way the agent never holds Reddit credentials, and posting stays manual under the
approval gate in `03_RULEBOOK.md` section A.

### 2. Notifications

**WhatsApp: Kapso is the better fit, Bird is the catalog option.**

**Kapso** gives the agent its own WhatsApp number through WhatsApp's API. Free plan: 2,000
messages/month, $2 in credits, one number, no credit card, and its MCP server is included
on the free plan. Pro is $25/month for 100,000 messages; Platform $299/month for 1,000,000.
At one daily report plus occasional alerts, roughly 100 messages a month, the free plan is
ample.

Three things the plan allowance does not cover:
- Meta's own per-message fees are billed separately from Kapso's allowance.
- Meta provides 1,000 free delivered service messages per number per month, no rollover.
- Since Oct 1, 2026 non-template messages on connected production numbers are billable, and
  free-form business messages are only permitted within 24 hours of the user messaging the
  business. A 07:30 report falls outside that window most days, so expect to need an
  approved template, or to message the agent first each morning.

**Kapso is not in the claude.ai connector catalog** — a registry search returns Bird but
not Kapso. It publishes a WhatsApp MCP server, so it is added as a custom MCP server rather
than enabled from connector settings. That requires a host that supports custom servers.

**Bird** is the catalog alternative. It covers email, SMS, WhatsApp, voice and an
agent inbox. The inbox is the reason to pick it: the approval loop needs the operator's
reply to reach the agent, not just the report to reach the operator. It is not installed
yet — connect it in claude.ai connector settings, then set `notify_channel: "whatsapp"`
and `notify_whatsapp` to the destination number in `config.json`.

Alternatives, for the record:

- **Sent** — SMS, WhatsApp and RCS, 25 tools rather than Bird's 337. Fine if one-way
  reports are enough and approvals come back some other way.
- **Twilio** — there is a Twilio connector and it needs no auth, but its only tools are
  `twilio__search` and `twilio__retrieve`, which search Twilio's documentation. It cannot
  send messages. Do not pick it for this.

**Email works right now** with no setup, via the connected Gmail MCP. Keep
`notify_channel: "email"` until Bird is connected, and as the fallback if WhatsApp
delivery fails.

A note on WhatsApp generally: Meta only permits free-form business messages inside a
24-hour window after the user messages the business. Outside that window an approved
template is required. A daily report at 07:30 will land outside the window most days, so
expect to need a template, or to message the agent first each morning. Bird handles the
sending; the template approval is still Meta's process.

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
