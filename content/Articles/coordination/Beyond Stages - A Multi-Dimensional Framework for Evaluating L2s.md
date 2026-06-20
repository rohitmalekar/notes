---
title: Beyond Stages - A Multi-Dimensional Framework for Evaluating L2s
tags:
  - Web3
type:
  - Article
permalink: beyond-stages
date: 2026-02-11
description: The current L2 evaluation landscape relies on a single-axis Stages framework that fails to capture the diversity of what Layer 2s actually offer. By distinguishing between convex and concave evaluation dispositions, a multi-dimensional approach can assess security inheritance, differentiated value, interoperability depth, and vibes-substance alignment. This essay proposes how L2Beat could expand its evaluation infrastructure to help users find the L2 that matches their needs rather than simply ranking chains on a single leaderboard.
---

Two recent posts in early February 2026( [here](https://x.com/VitalikButerin/status/2018711006394843585) and [here](https://x.com/VitalikButerin/status/2019341766407725170?s=20)) by Vitalik reframe what L2s are supposed to be. The short version: **L2s are no longer "branded shards" of Ethereum, and we should stop pretending they are.**

L1 is scaling directly. Many L2s cannot or will not reach Stage 2. And "yet another EVM chain with an optimistic bridge" is to infrastructure what forking Compound was to governance. Comfortable repetition. 

L2Beat has built a serious evaluation infrastructure over the years: the Stages framework, Risk Analysis, ZK Catalog, and the recent project recategorization. This article proposes how L2Beat should expand from a single-axis into a multi-dimensional evaluation. And the key to doing this well is understanding which evaluation axes demand convex dispositions (expert-driven, top-down, decisive) and which necessitate concave dispositions (pluralistic, bottom-up, compromise-seeking).

## What L2Beat Has Already Built
Before we get to what's next, it's worth pausing on what already exists. L2Beat has established the following  evaluation tools: 
- The [Stages framework](https://forum.l2beat.com/t/the-stages-framework/291) which classifies rollups by maturity from operator-controlled (Stage 0) to fully code-governed (Stage 2)
- A detailed [Risk Analysis](https://forum.l2beat.com/t/the-risk-rosette-framework/292) assessing factors like state validation, data availability, exit windows, and failure scenarios 
- The [ZK Catalog](https://forum.l2beat.com/t/the-trusted-setups-framework-for-zk-catalog/381), which standardizes verification of ZK proof systems onchain 
- [Recategorization](https://forum.l2beat.com/t/the-recategorization/377) of projects with inadequate proof systems or data availability into an "Others" category
- The [Interop Risk Framework](https://www.youtube.com/watch?v=zPiCzXRyQNw) was introduced last year during DevCon Bogota

## What Needs to Change
Vitalik’s posts highlight gaps in the current L2 evaluation framework: it doesn’t capture the diversity of L2s’ value propositions, their honesty in marketing, variations in their connection to Ethereum, or the real depth of interoperability. Both technical specs and qualitative factors matter, but require different evaluation approaches.

Some aspects demand clear, expert-driven (convex) judgment, while others benefit from a pluralistic, community-informed (concave) perspective. Getting these dispositions right for each axis is crucial for useful, trustworthy evaluations. (See [this](https://vitalik.eth.limo/general/2020/11/08/concave.html)article for more details on Convex and Concave Dispositions)

With a multi-dimensional evaluation, the question moves from "which L2 has the highest stage?" to "which L2 matches your needs?". Here are four new axes that could help guide the next phase of L2 evaluation.

## Axis 1: Security Inheritance

**Disposition: Convex. No compromise.**

This is where L2Beat's existing Stages framework and Risk Analysis live. And they should stay exactly where they are: expert-driven, binary, top-down. Security properties are not a matter of opinion. Either the proof system exists, or it doesn't. Either users can exit without operator coordination, or they can't.

**What could be added:**
- A new tier for **native rollup precompile** readiness, tracking which L2s can adopt Ethereum's [enshrined ZK-EVM verification](https://vitalik.eth.limo/general/2025/01/23/l1l2future.html) once it ships. Readiness depends on EVM equivalence, existing proof system compatibility, and whether custom modifications are modular enough to "bring your own prover" only for the delta. 
- Clearer gradation across the full spectrum: full faith & credit > Stage 2 > Stage 1 > bridged L1 > merkle root anchor

**Example:** Linea, currently Stage 0, has validity proofs (good), but three separate risk factors compound against it. First, there is no exit window: contracts are instantly upgradable, so users have no protection period against unwanted upgrades. Second, if the sequencer goes down or censors transactions, there is no mechanism to force inclusion. Third, if the proposer fails, users cannot independently withdraw. L2Beat does note a fallback: after 6 months of no finalized blocks, the Operator role becomes public, theoretically allowing anyone to post data and propose state. But a 6-month freeze on withdrawals is not a safety net most users would consider acceptable. The current framework flags this as high-risk across multiple dimensions.

## Axis 2: Differentiated Value

**Disposition: Concave. Let the ecosystem speak.**

"What new thing does this L2 bring to the table?" is a question best answered by the builders, users, researchers, and developers who interact with these systems every day.

**What already exists:**
- L2Beat tags some projects by type: "Exchange," "NFT," "Payments," "Privacy" (as seen on ZKsync Lite, Loopring, Aztec v1)
- The "Appchain" designation exists for application-specific rollups

**What could be added:**
- A structured **differentiation taxonomy** covering privacy, app-specific efficiency, extreme scaling, non-financial applications (social, identity, AI), ultra-low latency, specialized sequencing, built-in oracles, non-EVM VMs, algorithmic transparency for institutions
- **Community-sourced assessment** of whether the claimed differentiation is real based on aggregated builder and user perspectives

**Example:** Consider Lighter, an application-specific ZK rollup for exchange operations, currently at Stage 0. Under the existing framework, the conversation starts and ends with "Stage 0, not mature." But over a billion dollars in total value secured and thousands of user operations per second might tell a different story. The throughput is not incidental. Lighter built a [custom proving engine](https://docs.lighter.xyz/about-lighter/technical-architecture-lighter-core) from scratch for exchange-specific workloads: every order placement, match, cancellation, and liquidation is a discrete user operation verified by ZK proofs, with hundreds of thousands of execution proofs aggregated into single batch proofs before settlement on Ethereum. This is architecturally distinct from running exchange logic on a general-purpose EVM rollup. Under a concave differentiation assessment, market makers and builders could weigh in on whether this purpose-built design genuinely provides efficiency gains that justify the tradeoff of a narrower execution environment. 

## Axis 3: Interoperability Depth

**Disposition: Mixed. Convex for the "what," concave for the "is it enough?"**

Interoperability splits into two distinct questions. What mechanisms exist? And are they adequate for what this L2 is trying to be?

**What already exists:**
- L2Beat tracks bridge mechanisms as part of Risk Analysis
- Data Availability assessment captures onchain vs. offchain
- Exit Window captures withdrawal delays

**What could be added:**
- A classification of interoperability *type*: synchronous composability (real-time proving) > asynchronous trustless (ZK message passing) > asynchronous trust-dependent (optimistic bridge with delay) > minimal (bridge as afterthought) > none (merkle roots only)
- Assessment of whether the interoperability posture matches the L2's stated identity

**Example:** Unichain and Zora are both OP Stack optimistic rollups using the same bridge infrastructure. Same technical grade. Unichain is Uniswap's DeFi-focused L2, where traders and liquidity providers need fast, seamless access to L1 liquidity. The optimistic bridge's multi-day withdrawal delay is real friction for that use case. Zora is a creator and NFT chain where content is minted onchain and collectors bridge in and out occasionally. The same withdrawal delay is a non-issue. A convex evaluation gives both the same interoperability score. A concave evaluation, one that incorporates builder and user feedback, correctly notes that Unichain's interop is capital inefficient for latency-sensitive DeFi while Zora's is fit for use.

## Axis 4: Vibes-Substance Alignment

**Disposition: Concave. Emphatically.**

"Does the L2's public image reflect the reality of its connection to Ethereum?" This is where bottom-up assessment matters most.

**What already exists:**
- L2Beat already performs a version of this, implicitly. The "Others" recategorization was essentially saying: "You call yourself a rollup, but you don't have a proof system, so you're not one." The [December 2024 blog](https://medium.com/l2beat/framework-update-l2-projects-recategorization-5d43b0d1fe50) explicitly called out projects where "users deposit funds assuming they inherit Ethereum's security, when, most of the time, this is not the case."

**What could be added:**
- A systematic comparison of claimed identity (from websites, docs, marketing) versus verified technical reality (from L2Beat's own analysis)
- Community-contributed evidence that captures the gap between marketing language and lived builder/user experience

**How it could work in practice:** L2Beat constructs a claim inventory for each project by cataloging identity statements from its website, docs, and public communications (e.g., "scaling Ethereum," "fully decentralized," "trustless bridge"). Each claim is then matched against L2Beat's existing Risk Rosette and Stages data to produce a factual gap analysis. Finally, a time-boxed community attestation window opens where builders, users, and researchers submit structured evidence (integration friction, sequencer downtime experiences, bridge usability, actual vs. marketed decentralization) that is aggregated alongside the factual gap analysis into a vibes-substance score. L2Beat already has the technical data; the addition is a repeatable process for surfacing what that data means in context.

**Example:** Consider an L2 that markets itself as "scaling Ethereum" and emphasizes Ethereum alignment, but which Vitalik would describe as having "put 1-2 devs to get it to Stage 1 so the L2Beat people will put a green checkmark on it." The current framework shows: Stage 1, green checkmark. Done. But a concave honesty assessment might reveal something different: builders report the team actively discourages L1 interop patterns; the primary go-to-market is enterprise customers who want regulatory control (a valid use case, but not "scaling Ethereum"); the bridge is technically functional but practically unused; the token economics incentivize staying within the L2 rather than composing with L1. 

Now flip it. An institutional L2 that honestly says "we post merkle roots to Ethereum for algorithmic transparency, we're not trustless, the operator retains control, but we bring verifiable transparency to government operations"? That chain would score *well* on the honesty axis. Not because it's decentralized (it isn't), but because its vibes match its substance. 

## Risks and Caveats
The concave axes introduce challenges that pure onchain analysis does not face.
- **Governance capture:** if community attestations drive scores, L2 teams can astroturf their own evaluations, and deciding which voices count becomes a design problem in itself. 
- **Scope creep:** L2Beat's credibility rests on narrow, verifiable, reproducible claims and expanding into subjective territory risks diluting exactly the trust that makes the platform valuable. 
- **Incentive misalignment:** L2Beat operates within the Ethereum ecosystem and receives funding from it, which complicates neutrality when evaluating the "vibes" of politically connected projects. None of these are reasons to avoid the expansion, but they are reasons to design the concave processes carefully with transparent contributor selection, clear separation between factual analysis and community input, and explicit disclosure of funding relationships.

## The Bigger Picture
L2Beat earned its credibility by being rigorous, reproducible, and honest about what it found onchain. The new paradigm asks it to extend that approach into territory where pure quantitative rigor isn't enough.

The result would be useful in a way that a single leaderboard can't be: not a scorecard that tells you which L2 is "best," but a decision matrix that helps each user understand which L2 is best for them, and whether that L2 is being honest about what it actually is.