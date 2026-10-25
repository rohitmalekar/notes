# AI work (not on the public site)

Source material for AI-specific roles. Same no-fabrication rule as `cv.md`: reword freely, add nothing.

## The Monsoon Ledger (themonsoonledger.com)

Designed and built, with Claude Code, a weekly publication on Ethereum and Asian finance that runs on an AI agent pipeline.

- Wrote the spec, phased build plan and model instructions (CLAUDE.md, house style), then shipped the Astro site in four weeks with Claude co-authoring 73 of 74 commits.
- Built four scheduled Claude Code agents in GitHub Actions. They monitor Asian regulators, track 24 pilot programmes and draft analysis, and each run opens a sourced pull request for human review.
- Wrote CI guardrails aimed at common agent mistakes (duplicate filings, stale dates, broken links). A required check blocks a merge until the editorial judgment is added by hand.
