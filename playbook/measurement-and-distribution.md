# Measurement & Distribution Loop

## Plausible goals (10 min, one-time)

The site now loads Plausible with the **outbound-links extension** (changed in `quartz/plugins/emitters/componentResources.ts`), so every click on an external link is sent automatically as an "Outbound Link: Click" event. To see them as conversions:

1. plausible.io → rohitmalekar.in → Site settings → **Goals** → Add goal → Custom event → `Outbound Link: Click`.
2. In the dashboard, click into the goal and filter the `url` property by:
   - `calendar.app.google` → **intro-call clicks** (the number that matters most)
   - `linkedin.com`, `github.com` → profile curiosity
3. Optional: add a funnel Home → /work-with-me → intro-call click.

**Weekly 5-min review:** top pages, top sources, and intro-call clicks. If an essay drives traffic but no one reaches /work-with-me, that essay needs a byline link.

## Publishing loop (every new essay)

1. Publish on rohitmalekar.in first — the canonical home.
2. Same week: one LinkedIn post + one X/Farcaster thread that make one point from the essay and link to the canonical URL (not a full cross-post).
3. If cross-posting the full text to Medium/Mirror/Paragraph later, always add "Originally published at rohitmalekar.in/<slug>" at the top.

## Monthly SERP audit (5 min, log in a note)

- Incognito search: `"Rohit Malekar"`, `GrantsScope`, `GG24 interop round`, `ENS governance retrospective`.
- Note position of rohitmalekar.in for each. Ask an LLM (ChatGPT/Claude/Perplexity with web) "Who is Rohit Malekar?" and note whether the site is cited.

## Backlog (deliberately deferred — revisit in ~2 weeks)

1. **Newsletter** (top item): platform choice + signup on the site + the "26 Themes for Year One" draft in `content/Drafts/`.
2. Wikidata entity for Rohit Malekar once the Person schema has been live for a few weeks.
3. apple-touch-icon + web manifest.
4. /now page; a speaking page if talk invitations pick up.
5. Publish testimonials as they arrive (placeholder is in work-with-me.md).
