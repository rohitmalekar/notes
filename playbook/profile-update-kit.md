# Profile Update Kit — Entity Consolidation

Search engines and LLMs currently see conflicting versions of you: Medium says "Building products @ Deloitte Studios," your old Obsidian Publish site is still linked around, and two other Rohit Malekars (a VFX artist, a Java engineer) compete for the name. This kit makes every profile tell the same story and point to the same home. Do it in one sitting (~45 min); consistency is the point.

## The canonical set (copy-paste)

**One-liner (bios, social):**
> Funding systems, data tools, and coordination for open source ecosystems. Gitcoin · Metagov · Open Source Observer · Scroll. Writes at rohitmalekar.in

**50-word and 100-word bios:** on the site at https://rohitmalekar.in/about ("Bios for organizers" section) — always link people there instead of emailing bios around.

**The one link:** `https://rohitmalekar.in` — every profile's website field gets this, nothing else.

## Per-platform checklist

| Platform | Action |
|---|---|
| **Medium** (medium.com/@rohitmalekar) | Settings → replace the Deloitte-era bio with the one-liner; set website to rohitmalekar.in; **remove** the Linktree and publish.obsidian.md links. |
| **Old Obsidian Publish site** (publish.obsidian.md/rohitmalekar) | If your Publish subscription is still active: either take the site down, or replace the home note with one line — "This site has moved → rohitmalekar.in". It still outranks your own domain for some queries. |
| **Linktree** (linktr.ee/rohit.malekar) | Either retire it, or make rohitmalekar.in the first/primary link. |
| **LinkedIn** | Contact info → Website → rohitmalekar.in. Align the headline with the one-liner (keep "Researcher & Builder" if you like it — just make sure "open source ecosystems / funding systems" appears). Add featured links: /about and the two case studies. |
| **GitHub** (github.com/rohitmalekar) | Profile bio → one-liner; website field → rohitmalekar.in. Consider a profile README linking the site, GrantsScope, and metagov/ENS-Retro-Data. |
| **X/Twitter** (@RohitMalekar) | Bio → one-liner; website field → rohitmalekar.in. |
| **Farcaster** (rohitmalekar.eth) | Same: bio + link. |
| **HackerNoon** | If you can still edit your author profile, set the website link to rohitmalekar.in. Then send me the profile URL — I'll add it to the Person schema's `sameAs` list in `quartz/components/Head.tsx`. |
| **Gitcoin blog author page** | Already in the schema. If Gitcoin lets you edit the author bio, add the site link. |

## Tool footer credits (high-authority backlinks)

Add "Built by [Rohit Malekar](https://rohitmalekar.in)" to the footer/about of every tool you control:

- **grantsscope.xyz** — site footer
- **gg24-analysis.fly.dev** — dashboard footer
- **Streamlit apps** (stylus-sprint, gg23-retro-analysis) — `st.caption()` at the bottom
- **ensretro.metagov.org** — ask the Metagov team for a credit line linking rohitmalekar.in ("Data platform by Rohit Malekar"). This is the single most authoritative backlink available to you right now.

## Testimonials (do this week while the work is fresh)

Ask one person each at Gitcoin, Metagov, and Scroll for 1-2 sentences on working with you. Suggested ask: *"I'm adding a short 'what it's like to work with me' section to my site — could you give me one or two sentences on the [X project]? Happy to draft something for you to edit."* They go into the placeholder in `content/work-with-me.md`.

## Verify (a week later)

Search your name in incognito. The goal state: rohitmalekar.in first, then LinkedIn/GitHub/X — all showing the same one-liner, no Deloitte-era bios, no orphaned Obsidian Publish results.
