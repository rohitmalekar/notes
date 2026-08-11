---
name: notes-add-note
description: Create a new Reflection or Reference atomic note from raw content the user pastes or describes — a personal reflection, or a quote/excerpt from something they read. Use when the user wants to capture a thought or quote as a new note in content/Notes/self/ or content/Notes/reference/.
---

# /add-note — Create a new Reflection or Reference note from raw content

Take a piece of raw content the user pastes or describes — a personal reflection, or a quote/excerpt from something they read — and create a properly formatted atomic note file directly in `content/Notes/self/` or `content/Notes/reference/`.

This is the sibling of `/add-frontmatter`: that skill adds frontmatter to a draft file that already exists on disk. This skill starts from nothing — the content usually only exists in the chat message — and creates the file itself, including deciding its title, folder, and filename.

## Step 1 — Get the raw content

If the user pasted content or gave args, use that. Otherwise ask what they want to capture. It's fine if it arrives as a rough quote, a stream-of-consciousness thought, or a two-line description of an idea — your job is to shape it into a note, not to demand it arrive pre-formatted.

If it's a reference note, try to get the source (article/book title, author, and ideally a URL) from what they pasted. If the source isn't obvious, ask for it rather than guessing — a Reference note with a wrong or invented citation is worse than asking one follow-up question.

## Step 2 — Classify: Reflection or Reference (or neither)

- **Reflection** — the user's own thought, observation, or idea. No external source being cited. Goes in `content/Notes/self/`.
- **Reference** — someone else's idea, captured via a quote or close paraphrase, with a source. Goes in `content/Notes/reference/`.
- **Neither — this is actually an Article** — if the content has a developed thesis or argument (multiple supporting points, a structured case being made), even if it's short, it doesn't belong here. Atomic notes are meant to be a single idea, not an argument. Stop and tell the user this looks like it wants to be a full Article in `content/Articles/` instead, and ask how they'd like to proceed rather than forcing it into a Reflection.

When it's genuinely ambiguous between Reflection and Reference (e.g. the user's own take that was sparked by something they read), ask which one they mean rather than guessing — it changes both the folder and the frontmatter shape.

## Step 3 — Derive the title

The title is a short, evocative phrase that names the core idea — not a truncation of the first sentence. Look at existing notes in the target folder for tone (e.g. `Aging Like a Ship Leaving Harbour`, `Marginal Cost Doctrine`, `Nationalism vs Plurality`) — they read like concept names, not headlines.

Title-Case it. This exact string becomes both the `title` frontmatter field and the filename (`<title>.md`), so keep it filesystem-safe — no `/`, `:`, or other characters that break filenames.

Before finalizing, check whether a file with that name already exists in the target folder. If so, ask the user how to disambiguate (a different phrasing, or confirm overwrite) rather than silently clobbering it.

## Step 4 — Derive the tags

Choose 1–3 tags from this exact list only — do not invent new tags:
`Well-Being`, `Web3`, `Product`, `Leadership`, `Careers`, `AI`, `Culture`, `Decentralization`, `Recruiting`, `Parenthood`, `Fitness`, `Data-Analysis`, `Startup-Finance`, `Consulting`, `Learning`, `Design`, `DAO`, `Climate`, `Regen`, `Fiction`, `Miscellaneous`

If nothing fits well, use `Miscellaneous` rather than inventing a new tag.

## Step 5 — Assemble the frontmatter

**Reflection:**
```
---
title: <title>
tags:
- <tag>
type: Reflection
date: <YYYY-MM-DD>
---
```

**Reference:**
```
---
title: <title>
tags:
- <tag>
type: Reference
Reference: <source title>, <author>
date: <YYYY-MM-DD>
---
```

Notes on each field:
- `date` — today's date, unless the user specifies otherwise.
- `Reference` — free text, usually `"<Article/Book Title>, <Author Name>"`. A bare URL or handle is fine too if that's all the user has (existing notes do this, e.g. `Andrej Karpathy https://x.com/karpathy/status/...`).
- Both types use scalar `type:` (not a YAML list) — that's only for Articles.

## Step 6 — Write the body

Reference notes: the quote or excerpt, close to verbatim, no blockquote markdown (`>`), no added commentary. A single-sentence lead-in is fine if it helps the excerpt make sense out of context (e.g. "The Brihadaranyaka Upanishad (IV.4.5) states,"). If the idea connects to an existing atomic note you're aware of, a `[[wikilink]]` inline is welcome but not required.

Reflection notes: the user's own words, lightly cleaned up (fix typos, tighten grammar) but don't rewrite their voice or add structure/headings they didn't ask for. These run anywhere from one line to a few short paragraphs — resist the urge to pad it out.

## Step 7 — Confirm, then write

Show the user the full file (frontmatter + body) exactly as you're about to write it, and the destination path. Once they confirm (or after light edits), write the file with the Write tool. No manual index update is needed — Quartz lists both folders automatically.
