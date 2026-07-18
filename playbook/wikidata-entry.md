# Wikidata Entry — Statement-by-Statement

One sitting, ~30 min, at https://www.wikidata.org → create account → "Create a new item" (left menu).
Property/item IDs below are hints — Wikidata's autocomplete resolves labels as you type, so type the **label** and confirm the ID matches. For every statement, add a reference (expand "add reference" under the statement): `reference URL (P854)` = the URL given, plus `retrieved (P813)` = today's date.

## Item basics

| Field | Value |
|---|---|
| **Label** (English) | Rohit Malekar |
| **Description** (English) | Indian researcher and builder working on funding systems and data tools for open source ecosystems |
| **Aliases** | (none needed) |

## Statements

| # | Property | Value | Reference URL |
|---|---|---|---|
| 1 | `instance of` (P31) | human (Q5) | *(no reference needed)* |
| 2 | `occupation` (P106) | researcher (Q1650915) | https://discuss.ens.domains/t/ens-retro-draft-final-report/22067 |
| 3 | `occupation` (P106) — second value | data analyst *(or data scientist; pick from autocomplete)* | https://ensretro.metagov.org |
| 4 | `official website` (P856) | https://rohitmalekar.in | https://hackernoon.com/u/rohitmalekar *(third-party page listing the site)* |
| 5 | `country of citizenship` (P27) | India (Q668) | https://rohitmalekar.in/about |
| 6 | `residence` (P551) | Bengaluru (Q1355) | https://rohitmalekar.in/about |
| 7 | `languages spoken, written or signed` (P1412) | English (Q1860) *(add Kannada/Hindi/Marathi as applicable)* | *(optional, self-evident from published work)* |

## External identifiers (the highest-value section — entity resolvers join on these)

| # | Property | Value | Reference |
|---|---|---|---|
| 8 | `X username` (P2002) | RohitMalekar | *(auto-verifiable — no reference needed)* |
| 9 | `GitHub username` (P2037) | rohitmalekar | — |
| 10 | `LinkedIn personal profile ID` (P6634) | rohitmalekar | — |
| 11 | `Medium username` (P3899) | rohitmalekar | — |
| 12 | Farcaster username — type "Farcaster" in the property picker; add if the property exists | rohitmalekar.eth | — |

## Notes on strategy

- **Do NOT add:** `employer` (independent work doesn't source cleanly and invites challenge), `award received` (the Noonies runner-up has no Wikidata item for the award itself — use it as a *reference*, not a statement), date of birth or family details (privacy; also unsourced statements about living people get flagged).
- **Best third-party references if an editor ever challenges notability:** the Noonies award page (https://noonies.hackernoon.com/2022/web3/2022-hackernoon-contributor-of-the-year-dao), the ENS retrospective report (discuss.ens.domains link above), the Gitcoin governance forum posts under your name (e.g. https://gov.gitcoin.co/t/gg24-interop-round-retrospective/24936), and the OSO blog (https://docs.opensource.observer/blog/octant-2024-grant-analytics).
- **After saving:** note the item's Q-number (top of the page, e.g. Q123456789). Send it to Claude — we'll add `https://www.wikidata.org/wiki/Q…` to the Person schema's `sameAs` in Head.tsx, closing the loop: your site points to Wikidata, Wikidata points to your site.
- Give it 2–4 weeks, then check Google for a Knowledge Panel and re-run the "Who is Rohit Malekar?" LLM test from the measurement playbook.
