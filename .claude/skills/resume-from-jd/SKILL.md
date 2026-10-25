---
name: resume-from-jd
description: Build a tailored resume for Rohit from a job description (or a recruiter message, role brief, or similar text) and deliver it as a Google Doc in his Drive, styled from template.html (Arial, navy section rules, grey dates). Sources every claim from content/cv.md and content/Portfolio/ in this repo (the same content as rohitmalekar.in/cv and rohitmalekar.in/portfolio). Use when Rohit pastes a JD and asks for a resume, says "tailor my resume to this", "make a CV for this role", or invokes /resume-from-jd.
---

# Resume from JD

Input: a JD or similar text. Output: one Google Doc link, plus a short list of gaps in chat.

## Sources

All paths relative to the quartz repo root (the working directory).

| Path | Use |
|---|---|
| `content/cv.md` | Chronology, titles, dates, education, contact. Source of truth for facts. |
| `content/Portfolio/index.md` | Projects, tools, writing, talks with years and links. Pool for selected-work bullets. |
| `content/Portfolio/*.md` (case studies) | Detail and numbers for the projects they cover. |
| `ai-work.md` (in this skill dir) | AI agent and Claude Code build work not on the public site. Use for AI-specific roles. |

Read all of these in full every run. If the files are missing or look older than the live site, fetch https://rohitmalekar.in/cv and https://rohitmalekar.in/portfolio/ instead.

## Hard rules

- **No fabrication.** Every title, date, employer, number, client, and tool must appear in the sources. Rewording is fine; inventing scope, metrics, or skills is not. If the JD wants something the sources don't support, leave it out and report it as a gap.
- **JD vocabulary only where true.** Mirror the JD's terms (for ATS matching) when they describe something Rohit actually did.
- **Two pages maximum.** One page if the role is junior to mid-level or the JD is short.
- **Styling comes from `template.html` only.** No emojis, icons, tables, columns, images, or wikilinks, and no colours or sizes beyond those in the template. Links only on contact items and on project or publication names.
- **Writing.** Load the `writing-whip` skill before drafting, and follow the user's CLAUDE.md writing rules. British spelling (organisation, analyse, centred). Bullets start with a verb or a bold `Client, Role:` lead, past tense for past roles, no "responsible for", no adjectives that the source doesn't back with evidence.

## Procedure

**1. Parse the JD.** Extract: role title, company, seniority, must-have requirements, nice-to-haves, domain keywords, and the one or two problems the role exists to solve. Keep this in your head, not in the output.

**2. Choose the angle.** Rohit's history supports several framings (institutional finance research, ecosystem analytics and funding design, consulting practice leadership, CX and enterprise delivery, product management). Pick the one the JD's core problem matches and order everything around it.

AI-specific roles (applied AI, AI product, forward deployed, agent or LLM tooling, AI-native operations) take an AI-builder angle: replace the one-line Monsoon Ledger bullet under the 2026 role with the expanded entry from `ai-work.md`, put it first in that role, and add a `GrantsScope and Alfred, Builder:` bullet under the Jun 2023 practice for the LLM tools in the portfolio. The tagline and profile name the agent pipeline. For non-AI roles, keep the one-line Monsoon Ledger bullet from `cv.md`.

**3. Select and rewrite.**
- Tagline: one or two bold sentences under the contact line naming the identity and years that match the role.
- Profile: two short paragraphs in first person, written for this role.
- Experience: keep every role in `cv.md` so the chronology has no gaps. Role line is `Organisation, Location · Title` in bold, then dates in grey as `Mon YYYY to Mon YYYY` (or `to present`). Independent roles take a one-line description under the role line, and their bullets open with a bold `Client, Role:` lead. Spend 3 to 5 bullets on roles that match the JD; give the rest one or two plain bullets.
- Selected work and Skills: off by default. Add one only when the JD's must-haves need evidence the experience bullets can't carry, placed after Experience with the same heading style.
- Education: both degrees, as in the template.

**4. Build the HTML.** Copy `template.html` (in this skill dir) to the scratchpad as `resume.html` and fill it. Repeat the role-line, description and `ul` blocks for each role; drop the description `p` for roles without one. Keep every inline `style` exactly as the template has it, since Drive's HTML import reads only inline styles. Put no blank lines between elements, or Drive adds empty paragraphs.

**5. Create the Google Doc.** Call the Google Drive `create_file` tool (load it via ToolSearch, query `create_file drive`) with:
- `title`: `Rohit Malekar - Resume - <Company> <Role>`
- `textContent`: the HTML
- `contentMimeType`: `text/html`

Drive converts it to a Google Doc and keeps fonts, sizes, colours and bold, but not heading rules or heading margins. Never add a CSS `border` to the HTML: Drive turns it into a separate horizontal rule, which shows as a second line under the heading. Add the rules in one `update_doc` call:

1. `read_doc` the new doc (the result is large and saved to a file; use `jq` on it) and collect `startIndex`/`endIndex` of every paragraph whose `namedStyleType` is `HEADING_2`.
2. For each, send `updateParagraphStyle` with `fields: "borderBottom,spaceAbove,spaceBelow,keepWithNext"` and `paragraphStyle`: `borderBottom` colour rgb 0.749/0.749/0.749, width 0.75 PT, padding 2 PT, `dashStyle` SOLID; `spaceAbove` 14 PT; `spaceBelow` 6 PT; `keepWithNext` true.
3. Check the same `read_doc` output for `horizontalRule` elements. There should be none; delete any found, highest index first.

Apply no other styling unless Rohit asks.

**6. Report.** Reply with the doc link, then a short list of JD requirements the sources could not support (if any), so Rohit can decide whether to add real material to `cv.md`. Nothing else.

## Revisions

When Rohit asks for changes to a resume already created, edit the existing doc (`read_doc`, then `update_doc` with `replaceAllText` or index-based edits) rather than creating a new file, unless he asks for a new version.
