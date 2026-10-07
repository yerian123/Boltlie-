# Boltline Growth: working notes for Claude

Boltline helps independent residential HVAC shops (3–15 techs, Canada outside Quebec) get more install jobs: Meta ads in the shop's own ad account plus instant text-back on leads and missed calls.

## Boltline Outbound (the CRM)
The source of truth for leads, calls, messages and the playbook is the **Boltline Outbound app**: https://claude.ai/artifact/K4KwGv5bJSwBrWUoFcoJfW (source code: `app/outbound.html`).
- Data lives in the app's private database. Read and write it with the `ArtifactData` tool on that URL. Collections: `leads`, `touches` (every call/message/note), `imports` (agent-found leads waiting for Yerian to press "Add them"), `settings/main` (playbook, voice, mailing address).
- New leads from agents go into ONE `imports` document (`status: "pending"`, `rows: [...]`), never straight into `leads`.
- Pin every write to the version you read (`if_version`).
- Skills: `/find-leads`, `/refresh-signals`. The older `outbound/engine.py` and the call-prep, log-calls and draft-message skills are the offline fallback; the app replaces them day to day.

## Hard rules
- Main channel is cold calls. Cold email is locked (app Playbook tab: needs a mailing address and the unlock switch; Yerian's plan says after Gate 2). No LinkedIn.
- Drafts only: Yerian approves and sends every written message himself.
- Every fact about a shop needs a source URL and date. "Not found" means unknown.
- Never promise leads, jobs or revenue. Never quote industry stats to owners as fact.
- This repo is public: don't commit personal details about Yerian or his family, or private strategy docs.
