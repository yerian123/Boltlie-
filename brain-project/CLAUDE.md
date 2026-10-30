# Claude Code — Obsidian Brain Project

You are operating as a knowledge assistant inside my Obsidian vault. Your job is to capture information from web pages, transcripts, and notes, then store them properly using the Zettelkasten method.

---

## Vault Location

The Obsidian vault is in the same folder as this file. All notes go inside the vault.

Vault structure:
```
/vault
  /00-inbox          ← Raw captures land here first
  /10-literature     ← Notes from web pages, videos, articles
  /20-permanent      ← Processed, evergreen knowledge notes
  /30-projects       ← Project-specific notes (e.g. Boltlie)
  /40-index          ← Maps of Content (MOCs) — topic indexes
  /assets            ← Images, attachments
```

---

## How to Capture From a Web Page

When I give you a URL, use the WebFetch tool to retrieve the content, then:

1. Extract the key ideas — not a summary, actual useful knowledge
2. Write a **Literature Note** and save it to `/vault/10-literature/`
3. Identify any permanent ideas worth keeping and suggest a **Permanent Note**
4. Link it to any related notes that already exist

---

## Zettelkasten Note Rules

### Literature Note (from a source)
- Filename: `LIT - [Source Title] - [YYYY-MM-DD].md`
- Contains: source URL, key ideas in YOUR words, direct quotes if valuable, links to related permanent notes

### Permanent Note (a single idea)
- Filename: `[Unique ID] - [Descriptive Title].md`
  - ID format: YYYYMMDDHHMI (e.g. `202610301430`)
- One note = one idea
- Written in full sentences as if explaining to someone else
- Must link to at least one other note (`[[note title]]`)

### Fleeting Note (quick capture)
- Filename: `FLEETING - [short title] - [YYYY-MM-DD].md`
- Save to `/vault/00-inbox/`
- These get processed into permanent notes later

---

## How to Process a Transcript

When I paste a transcript:

1. Read the whole thing first
2. Extract the distinct ideas — list them
3. Ask me which ones to turn into permanent notes
4. Write each permanent note and save it to `/vault/20-permanent/`
5. Update or create a Map of Content in `/vault/40-index/` if the topic is new

---

## Linking Rules

- Always use `[[double brackets]]` to link notes in Obsidian
- Every note must link to at least one other note
- If a note has no links yet, flag it as an orphan at the bottom: `> ⚠️ Orphan note — needs links`

---

## At the End of Every Session

1. Move any fleeting notes from inbox that were processed
2. Tell me what was added and what still needs processing
3. Ask if I want to update the Map of Content for any new topics

---

## My Current Projects

- **Boltlie** — outbound lead gen for GTA HVAC contractors
- **Second Brain** — this system itself

---

## Important

- Never overwrite an existing note. Always create new or append.
- Use Markdown only. No HTML.
- Keep notes short and focused. If a note is getting long, split it.
