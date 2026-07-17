---
title: "Case Study: ENS DAO Governance Research Platform"
description: "How a reproducible analytics stack — Dagster, dbt, and DuckDB across 7 onchain and forum data sources — became the evidence base for Metagov's independent governance retrospective of ENS DAO, informing decisions over a $400M+ treasury."
tags:
  - Web3
  - Data-Analysis
type:
  - Portfolio
permalink: ens-governance-analytics
date: 2026-07-17
---

**Client:** [Metagov](https://metagov.org), for the ENS DAO community · **Role:** Data & analytics lead · **Year:** 2025–26

## The problem

ENS DAO governs a treasury of over $400M, but the evidence for how well its governance actually works was scattered across onchain votes, delegate activity, forum threads, and working-group records. Metagov's independent retrospective needed a defensible, reproducible evidence base — not a one-off spreadsheet — so that findings could be verified, challenged, and kept alive after the report shipped.

## What I built

A reproducible research data platform that turns raw governance activity into analysis-ready data:

- **Pipeline:** Dagster for orchestration, dbt for transformation, DuckDB for storage — a lightweight, fully open stack anyone can run locally.
- **Coverage:** 7 data sources spanning onchain governance (votes, delegations, treasury flows) and offchain signals (forum discussions and related records).
- **Outputs:** the datasets and analytics behind the retrospective's findings, published as a live research platform rather than static charts.

## The outcome

- The retrospective and its data platform are public: findings can be reproduced from source, not taken on faith.
- The [live dashboard](https://ensretro.metagov.org) is cited in active ENS DAO governance discussions — the analysis outlived the report.
- The stack is a template for any DAO that wants governance research grounded in verifiable data.

<!-- TODO (Rohit): add 1-2 concrete examples of governance decisions/threads that cited the platform, and a testimonial from the Metagov team. -->

## Artifacts

- [Live research platform](https://ensretro.metagov.org)
- [Open-source data stack](https://github.com/metagov/ENS-Retro-Data)
- [Draft final report on the ENS forum](https://discuss.ens.domains/t/ens-retro-draft-final-report/22067)

---

*Need a defensible evidence base for governance or funding decisions? [[work-with-me|Here's how I work with teams →]]*
