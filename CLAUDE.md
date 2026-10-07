# Boltline Growth: working notes for Claude

Boltline helps independent residential HVAC shops (3–15 techs, Canada outside Quebec) get more install jobs: Meta ads in the shop's own ad account plus instant text-back on leads and missed calls.

## Outbound agent
See `outbound/README.md`. Skills: `/find-leads`, `/refresh-signals`, `/call-prep`, `/log-calls`, `/draft-message`. Bookkeeping goes through `python3 outbound/engine.py`; don't hand-edit lead CSV statuses.

## Hard rules
- Main channel is cold calls. Cold email is locked (`outbound/config.json` → `channels.cold_email`) until Gate 2 and a mailing address exist. No LinkedIn.
- Drafts only: Yerian approves and sends every written message himself.
- Every fact about a shop needs a source URL and date. "Not found" means unknown.
- Never promise leads, jobs or revenue. Never quote industry stats to owners as fact.
- This repo is public: don't commit personal details about Yerian or his family, or private strategy docs.
