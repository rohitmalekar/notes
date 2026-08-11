---
name: notes-prior-thinking
description: Surface Rohit's own prior writing from the quartz digital garden (302 notes, 2017–2026) when scoping a client engagement, drafting a proposal or talk, answering a question in his domain, or starting a new essay. Use whenever he asks "what have I written about X", "have I thought about this before", "pull my prior thinking on X", or is about to write something where a decade of his own notes should inform it.
---

# Prior Thinking

Retrieve Rohit's own decade of writing so he stops rediscovering what he already worked out.

The corpus is his quartz digital garden: ~302 notes, 2017–2026, split between long-form essays (`content/Articles/`) and atomic notes (`content/Notes/`), plus portfolio case studies. It is indexed at `corpus/index.txt` in the quartz repo.

**The job is not search. The job is to come back with the specific paragraphs he can reuse, the positions he's committed to, and the honest gaps.** A list of vaguely related titles is a failure.

## Locating things

The quartz repo is the working directory. Use Read/Glob for files, and bash for scripts.

Key paths, all relative to the repo root:

- `corpus/index.txt` — the whole corpus, 2 lines per note (title ~ type ~ date ~ tags ~ words ~ path, then thesis). ~24k tokens. Load it whole.
- `corpus/links.txt` — wikilink graph, `Title -> linked; titles`. Grep it, don't load it.
- `corpus/index.jsonl` — same records with public `url` fields. Look up URLs here for shortlisted notes only.
- `corpus/build_index.py` — regenerates all three.

## Procedure

**1. Refresh if stale.** Compare the `generated` date on line 1 of `corpus/index.txt` against recent edits in `content/`. If content is newer, run `python3 corpus/build_index.py` first. Cheap, takes a second.

**2. Load `corpus/index.txt` in full.** Do not grep it. Keyword matching is exactly what fails here — his vocabulary shifts across nine years, and the most useful note for a funding question is often filed under Well-Being with no shared terms. Read all 302 theses and select on meaning.

**3. Shortlist 8–15 notes.** Bias toward:

- Notes whose *argument* transfers, even when the subject differs. A note on hiring signal applies to grantee evaluation. A note on attention applies to governance participation.
- His atomic notes (`Notes/self`, `Notes/reference`) — short, dense, and where his distinctive framings live. They are easy to overlook next to the essays; don't.
- Both the recent and the old. A 2019 position that still holds is more persuasive than a 2026 one.

**4. Expand one hop.** Grep `corpus/links.txt` for the shortlisted titles. Notes he explicitly linked are notes he considered related — follow the ones that look load-bearing.

**5. Read the shortlisted files in full.** The thesis line is for selection only. Never quote from the index; quote from the file.

**6. Look up public URLs** in `corpus/index.jsonl` for whatever ends up in the brief.

## The brief

Write it as working material, not a report. No preamble, no restating the question.

**Your position** — 2–5 claims he has already committed to in writing, each stated as a usable sentence, each with the verbatim line worth lifting, the note title, date, and URL. Quote him exactly. Do not smooth his phrasing into generic consultant prose — the specificity and the voice are the entire asset.

**Reusable material** — concrete things that can go straight into the proposal, deck, or draft: a framework he named, a case with numbers, an analogy that landed, a story. Point to the exact passage.

**Tensions and revisions** — where notes disagree with each other, or where an older position predates something that has since changed. Flag anything Web3-tagged older than ~18 months as needing a freshness check before it goes in front of a client. This section prevents him quoting a stale self.

**Gaps** — what this problem requires that he has genuinely not written about. Be direct. This is often the most valuable section: it marks where new thinking is needed, and it's usually the seed of the next essay.

## Rules

- Every claim traces to a file. Never synthesize a position he hasn't taken and attribute it to him.
- If the corpus is thin on the topic, say so plainly in one line and keep the brief short. A padded brief that stretches three loosely-related notes into a false position is worse than "you haven't written about this."
- Prefer quoting over summarizing throughout.
- Distinguish what he *argued* from what he *reported*. A recap of a grants round is evidence; a thesis about capital allocation is a position.
