# corpus/

A retrieval layer over the garden, so a decade of notes stays reachable instead of just published.

## Why

`content/` is organised for readers. This directory is organised for recall — for the moment you're scoping an
engagement, drafting a proposal, or starting an essay and want to know what you already worked out.

## Files

| File | What it is |
|---|---|
| `build_index.py` | Regenerates everything below from `content/`. Run after adding notes. |
| `index.txt` | Every note as two lines — metadata + thesis. ~24k tokens, small enough to load whole. |
| `links.txt` | Wikilink graph, `Title -> linked; titles`. Grepped, not loaded. |
| `index.jsonl` | Same records plus public `rohitmalekar.in` URLs, for machine use. |

## Refresh

```bash
python3 corpus/build_index.py
```

## How it's used

The `prior-thinking` Claude skill loads `index.txt` in full and selects on *meaning* rather than keywords —
which matters, because vocabulary shifts across nine years and the most useful note for a funding question is
often filed under Well-Being with no words in common. It then reads the shortlisted files, follows one hop
through `links.txt`, and returns a brief: positions already taken (quoted verbatim), material reusable as-is,
tensions between old and new selves, and the honest gaps.

## Design notes

- **Thesis** comes from frontmatter `description:` when present, else the first real paragraph with editorial
  preambles, images, and blockquotes stripped.
- **URLs** mirror Quartz's slugifier: lowercase the file path, `&` → `and`, whitespace → `-`, keep other
  punctuation. Verified against the built site (297/302 exact; the rest are titles containing `?` or `%`,
  which are encoded differently on disk).
- **Excluded**: `Attachments/`, `Drafts/`, `.obsidian/`, and section `index.md` files.
