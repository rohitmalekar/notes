---
name: notes-add-frontmatter
description: Add YAML frontmatter to a draft markdown file that already exists on disk, classifying it as Article, Reflection, or Reference and deriving all required fields. Use when the user has a draft file without frontmatter and wants it prepared for publishing.
---

# /add-frontmatter — Add YAML frontmatter to a draft markdown file

Read the draft file at the path given in args (or ask for it if omitted). Analyze the content and prepend the appropriate YAML frontmatter block.

## Step 1 — Read the file

Read the file. If it already has a frontmatter block (starts with `---`), show the user what exists and ask whether to replace it before proceeding.

## Step 2 — Determine content type

Classify the file as one of three types based on the content:

- **Article** — a structured essay with a thesis, sections, and developed argument. Usually 500+ words.
- **Reflection** — a short atomic note, personal observation, or idea fragment. Usually under 300 words, no formal structure.
- **Reference** — a note about a specific book, paper, talk, or external source. Often includes quotes or summary of that source.

## Step 3 — Derive each frontmatter field

**`title`** (required, all types)
- Use the H1 heading if present.
- Otherwise derive a clean title from the filename (remove hyphens/underscores, title-case).
- Do not include the file extension.

**`type`** (required, all types)
- Set to `Article`, `Reflection`, or `Reference` based on Step 2.
- For Articles: use YAML list syntax → `type:\n  - Article`
- For Reflections and References: use scalar syntax → `type: Reflection` or `type: Reference`

**`tags`** (required, all types)
- Choose 1–3 tags from this exact list only — do not invent new tags:
  `Well-Being`, `Web3`, `Product`, `Leadership`, `Careers`, `AI`, `Culture`, `Decentralization`, `Recruiting`, `Parenthood`, `Fitness`, `Data-Analysis`, `Startup-Finance`, `Consulting`, `Learning`, `Design`, `DAO`, `Climate`, `Regen`, `Fiction`, `Miscellaneous`
- Use YAML list syntax.

**`date`** (required, all types)
- Use today's date in `YYYY-MM-DD` format.

**`description`** (Articles only)
- Write 1–3 sentences that capture the central argument, context, and why it matters.
- Target 40–80 words. Write in third person or essay-abstract style (not "In this article...").
- Omit for Reflections and References.

**`permalink`** (Articles only)
- A short, memorable, lowercase kebab-case slug (2–5 words).
- Should reflect the core topic, not be a verbatim copy of the title.
- Omit for Reflections and References.

**`Reference`** (Reference notes only)
- The name of the source being referenced (book title, author, talk name, URL, etc.).
- Omit for Articles and Reflections.

## Step 4 — Write the frontmatter

Prepend the frontmatter block to the file, preserving all existing body content exactly. The block must be the very first thing in the file:

```
---
title: <title>
tags:
  - <tag>
type:
  - Article        # or scalar for Reflection/Reference
permalink: <slug>  # Articles only
date: <YYYY-MM-DD>
description: "<description>"  # Articles only; wrap in double quotes
---

<existing content unchanged>
```

For Reflections:
```
---
title: <title>
tags:
  - <tag>
type: Reflection
date: <YYYY-MM-DD>
---

<existing content unchanged>
```

For References:
```
---
title: <title>
tags:
  - <tag>
type: Reference
Reference: <source name>
date: <YYYY-MM-DD>
---

<existing content unchanged>
```

## Step 5 — Confirm before writing

Show the user the proposed frontmatter block and ask for confirmation or edits before writing it to the file. After approval, write the file.
