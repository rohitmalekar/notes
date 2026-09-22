---
title: Ethereum's Privacy Stack and the Gap in the Middle
tags:
  - Web3
  - Decentralization
type:
  - Article
permalink: ethereum-privacy-stack
date: 2026-09-22
description: Ethereum is building privacy by separating neutral mechanisms at the base layer from policy set by wallets, pools, rollups and institutional systems. The teams at both ends are well funded. The applied cryptography research in the middle, which PSE used to maintain, lost its home in the 2026 Ethereum Foundation restructuring.
---

### TL;DR

If Ethereum is going to live up to its name as a "world computer," it has to carry a user's shielded transfer and a bank's confidential bond on the same chain, along with everything in between.

The approach that has emerged separates mechanism from policy. The base layer provides neutral mechanisms, so private transactions get included and metadata does not leak. Everything built on top, including wallets, shielded pools, rollups and institutional systems, sets its own policy on who sees what.

Both ends of that stack now have committed teams and money. Core developers and Ethereum Foundation researchers own the mechanism. Companies, several of them spun out of the Foundation in 2026, increasingly set the policy. What lost its home in the [June 2026 restructuring](https://www.techtimes.com/articles/318949/20260623/ethereum-foundation-cuts-54-jobs-shuts-zk-research-lab-slashes-budget-40.htm) is the shared applied cryptography in the middle: [MACI](https://maci.pse.dev/), [Semaphore](https://semaphore.pse.dev/), and the unglamorous work of making zero-knowledge proofs run on an ordinary phone.

### A public ledger is a privacy problem by design

Every transaction on Ethereum is published to everyone, forever. That is the property that makes the chain verifiable without a trusted operator: anyone can re-run the whole history and check that the rules were followed. It is also the property that makes it unusable for most of what money is actually used for.

A salary paid onchain reveals the salary. A treasury moving funds reveals its position before the trade settles. A person who receives one payment from a known address has their entire financial history linked to their name from that moment on, backwards and forwards. Addresses are pseudonyms, and pseudonyms leak. Chain analysis firms have spent a decade building the tooling to de-anonymise them, and they are good at it.

The exposure is not limited to the ledger. Before a transaction is included in a block it sits in the public mempool, where anyone can read it. Specialised actors watch that queue and profit by reordering around what they see, which is how sandwich attacks and other forms of [MEV](https://ethereum.org/en/developers/docs/mev/) work. Even the act of reading the chain leaks: most wallets query a handful of large data providers, so those providers learn which addresses you care about and when.

So "put it on a public blockchain" and "keep it private" are in direct tension. Resolving that tension is the entire subject below.

### Two different things get called privacy

The word covers two requirements that sound similar and need different machinery.

A bank settling a bond wants **confidentiality**. It has a defined set of counterparties, auditors and supervisors, each entitled to see a different slice of the transaction. The bank is content for all of them to see their slice. What it will not accept is the public seeing any of it, because position sizes and counterparty relationships are commercially sensitive. Confidentiality is about controlling the audience, and the bank knows exactly who is in it.

A person sending money wants **user privacy**. There is no defined audience. The requirement is that a transfer cannot be linked back to them by anyone, including parties they have never heard of and cannot negotiate with. This is closer to anonymity, and it is harder, because it is a claim about what an unbounded set of observers can infer.

The two pull in opposite directions when regulation enters. Regulators are broadly comfortable with confidentiality, since someone accountable still holds the keys to disclosure. They are legislating against pure anonymity. The EU's Anti-Money Laundering Regulation, [Regulation (EU) 2024/1624](https://eur-lex.europa.eu/eli/reg/2024/1624/oj), prohibits regulated firms from keeping anonymous accounts or handling anonymity-enhancing coins [from 10 July 2027](https://cointelegraph.com/news/eu-crypto-ban-anonymous-privacy-tokens-2027).

That deadline shapes almost every design decision in the sections that follow. The teams building for individuals are not building anonymity and hoping regulators look away. They are building anonymity with a disclosure mechanism attached, so a user can prove something about their funds without revealing which funds they are.

### Mechanism at the base, policy above it

The design principle Ethereum has settled on is to keep the base layer neutral.

The protocol does not decide who deserves privacy or under what conditions. It provides mechanisms: a guarantee that a transaction will be included even if block builders would rather drop it, a way for many users to share one sending account, a queue that does not reveal contents before ordering. These are useful to a shielded pool, a bank and a regular wallet alike, and they do not encode a view about any of them.

Policy sits above. A shielded pool decides what proof of clean provenance it demands at withdrawal. A bank's rollup decides which regulator holds which viewing key. A wallet decides what it exposes to its RPC provider. Each of those is a contestable judgement that will change as law and norms change, which is exactly why none of them belongs in a hard fork that takes years to alter.

This split is also, as it happens, the fault line along which the Ethereum Foundation has reorganised itself.

### Who is building what

What follows is not exhaustive, and the boundaries are porous. It is a map of who owns which layer as of late 2026.

#### Protocol: the mechanism layer

Changes here ship through hard forks, are built by core developers and Ethereum Foundation researchers, and take years. They are worth tracking because they are the only part of the stack that no individual company can withdraw.

- [Account abstraction](https://eips.ethereum.org/EIPS/eip-8141) plus [FOCIL (EIP-7805)](https://eips.ethereum.org/EIPS/eip-7805): Today, a small number of large block builders decide which transactions make it into a block. A transaction they dislike, or that their compliance counsel dislikes, can simply never be included, and nothing in the protocol objects. FOCIL puts a small, randomly selected committee of validators in charge of publishing a list of transactions the next block is obliged to include. Paired with account abstraction through [frame transactions (EIP-8141)](https://eips.ethereum.org/EIPS/eip-8141), which lets a smart contract account define its own rules for validating and paying for a transaction, private transactions get inclusion guarantees written into the protocol itself. **So what:** without this, every other privacy tool on this list sits on top of a chokepoint. A shielded withdrawal that no builder will include is not private, it is just stuck.
- [Keyed nonces (EIP-8250)](https://eips.ethereum.org/EIPS/eip-8250): A nonce is the counter that orders transactions from a single account, and today it is strictly sequential, so two transactions from one sender cannot be processed independently. That forces privacy systems into a bad choice. Either every user gets their own sending account, which creates a distinct onchain fingerprint, or they share an account and queue behind each other. Keyed nonces give one account multiple independent counters, so many users can send through the same address without serialising. **So what:** the strength of any privacy system is the size of its anonymity set, meaning how many other people you could plausibly be. This change lets a crowd share one front door without tripping over each other, which keeps the crowd large. It and the main account abstraction changes are slated for the Hegota fork, currently being scoped, with timelines drifting toward 2027.
- Encrypted mempool, [EIP-8105](https://eips.ethereum.org/EIPS/eip-8105) and [LUCID (EIP-8184)](https://eips.ethereum.org/EIPS/eip-8184): Both proposals let a user submit a sealed transaction that is ordered while still encrypted and only revealed once its position in the block is fixed. LUCID was [drafted](https://ethereum-magicians.org/t/eip-8184-lucid-encrypted-mempool/28017) by the Foundation's [Robust Incentives Group](https://rig.ethereum.org/) and deliberately avoids enshrining any one encryption scheme. An [Encrypt the Mempool](https://encryptedmempool.org/) coalition, which includes [Shutter](https://blog.shutter.network/shutter-joins-the-encrypt-the-mempool-coalition/), [Fairblock](https://www.fairblock.network/) and [Nillion](https://nillion.com/), is pushing for inclusion in the I\* fork. **So what:** read the mechanism carefully, because it is narrower than it sounds. Transactions are revealed eventually. This protects against being front-run and sandwiched in the moments before inclusion. It does not give you confidentiality, and anyone who sells it as privacy is overselling it.

#### Wallet and access layer

Protocol guarantees are worthless if using them requires a cryptography degree. This layer is about getting privacy into the software people already have open, and most of it is Ethereum Foundation work.

- [Kohaku](https://github.com/ethereum/kohaku): An open-source SDK, [released in May 2026](https://cryptobriefing.com/kohaku-sdk-wallet-privacy-integration/), that lets any wallet integrate shielded pools through plugins rather than building the integration itself. Plugins for [Railgun](https://railgun.org/), [Privacy Pools](https://privacypools.com/) and [Tornado Cash](https://en.wikipedia.org/wiki/Tornado_Cash) are all still alpha. **So what:** a two-person wallet team can now offer privacy features that previously needed a dedicated cryptography department. Privacy that lives in a specialist app is used by specialists. Privacy that ships as a checkbox in the wallet someone already has is used by everyone else.
- Private reads: When your wallet displays a balance, it asks an RPC provider about your addresses, and that provider learns which addresses belong to one person even when the chain does not say so. Private read techniques let a wallet fetch the data it needs without revealing which records it asked for. **So what:** you can hold a perfectly shielded balance and still be deanonymised by the act of checking it. This closes a side channel that most users do not know exists.
- [Shutter](https://shutter.network/) and [Primev](https://docs.primev.xyz/): Both run encrypted transaction ordering outside the protocol, reachable today by pointing a wallet at a custom RPC endpoint. **So what:** the protocol version of this is years out. These give users the protection now, and give the EIP authors real operating data about what breaks at scale.

#### Shielded pools on L1: user privacy with compliance built in

These are the systems an individual actually uses to break the link between where funds came from and where they go. All are built by independent teams, and all have converged on roughly the same answer to the regulatory problem.

The shared mechanism is worth stating once, plainly. You deposit into a pool along with many others. Later you withdraw to a fresh address and, instead of revealing which deposit was yours, you submit a zero-knowledge proof: a cryptographic argument that your deposit belongs to some set of acceptable deposits, which convinces the verifier without disclosing which member it is. The privacy comes from the size of the set. The compliance comes from how the set is chosen.

- [Privacy Pools](https://privacypools.com/), by [0xbow](https://0xbow.io/), builds on a [2023 paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4563364) co-authored by Vitalik Buterin, Jacob Illum, Matthias Nadler and Fabian Schär. At withdrawal you prove membership in an association set curated to exclude funds tied to illicit activity. **So what:** this inverts the usual argument about mixers. Rather than the honest user being tarred by association with whoever else used the pool, they get to cryptographically separate themselves from the bad deposits while still hiding among the good ones. It is the strongest available answer to "privacy tools only exist to launder money."
- [Railgun](https://railgun.org/) runs its own screening system, [Private Proofs of Innocence](https://docs.railgun.org/wiki/assurance/private-proofs-of-innocence), applied as funds enter rather than at withdrawal. **So what:** same principle, different point of enforcement, and a useful demonstration that the compliance policy is genuinely a choice at this layer rather than something the chain imposes.
- [Tornado Cash](https://en.wikipedia.org/wiki/Tornado_Cash) is the original design, without a screening layer, and the reason the entire category now ships with one. Its sanctioning by OFAC in 2022, [delisted in March 2025](https://home.treasury.gov/news/press-releases/sb0057) after the Fifth Circuit found the agency had exceeded its authority, and the prosecutions of its developers that followed anyway, is the lived history that every team above is designing around. **So what:** the compliance features in these products are not decoration. They are the difference between shipping and being charged.

#### L2s and confidential execution

Layer 2s are separate chains that inherit Ethereum's security by posting proofs back to it. Because they control their own execution environment, they can do things mainnet cannot, including running computation over data that is never revealed in the clear. This is where confidentiality and user privacy are being served by the same infrastructure, and it is mostly venture-funded companies.

- [Aztec](https://aztec.network/) is an L2 built around private computation from the ground up rather than bolted on, with selective disclosure to regulators as a design goal. It [reached Stage 2 on L2BEAT](https://l2beat.com/scaling/projects/aztecnetwork) after onchain governance revoked ownership of the rollup contract. **So what:** Stage 2 is the top of L2BEAT's maturity ladder and means no administrator can override the protocol or seize funds. A privacy chain with an admin key is a privacy promise. A privacy chain without one is a privacy guarantee, and Aztec is currently the only decentralised L2 with privacy native to the protocol.
- [ZKsync Prividium](https://www.zksync.io/prividium) targets banks and corporates whose privacy requirement comes from regulation rather than preference, giving each institution control over who can query its data. A [consortium of five US regional banks](https://thedefiant.io/news/tradfi-and-fintech/cari-zksync-prividium-tokenized-deposits-e07mwc) with over $600 billion in combined deposits is building a tokenized deposit platform on it. **So what:** this is the clearest evidence that institutional demand is real rather than theoretical, and that the constraint on adoption was confidentiality rather than throughput.
- [Zama](https://www.zama.org/) takes a different cryptographic route, using fully homomorphic encryption, which allows computation to be performed directly on encrypted data without decrypting it first. In March 2026, GSR [completed the first confidential OTC trade](https://www.gsr.io/insights/gsr-and-zama-complete-landmark-first-confidential-otc-trade-on-ethereum) using it on mainnet, with the traded quantity staying encrypted between two fully identified counterparties. **So what:** zero-knowledge proofs let you prove a fact about hidden data. FHE lets a contract compute on hidden data. That difference opens up applications, such as confidential order matching, that proofs alone cannot reach, at a performance cost that is still falling.

#### Institutional integration: confidentiality for regulated players

The layer above the chains, where an institution's actual requirements get translated into a deployment. This is commercial consulting work, and it is where the Foundation's own people went.

- [EthSystems](https://ethsystems.org/) is the for-profit successor to the Ethereum Foundation's Institutional Privacy Task Force, [spun out in July 2026](https://www.theblock.co/post/408331/ethereum-foundation-privacy-team-spins-out-as-for-profit-ethsystems-to-serve-institutions-with-lubin-bitmine-backing) with backing from Bitmine, Sharplink and Joe Lubin. It builds systems where each party sees only what it is entitled to, with selective disclosure kept in for compliance, and it arrived with a year of open-source work already published: private bonds, confidential stablecoin transfers, private cross-chain settlement, and an [Ethereum Privacy Map](https://github.com/ethsystems/map) cataloguing institutional requirements across the ecosystem. **So what:** the task force spent its Foundation years in hundreds of conversations with central banks, regulators and financial institutions. That accumulated knowledge of what supervisors will actually accept is now sold as bespoke consulting rather than published as a public good.
- Two other Foundation spin-outs complete the picture. [Ethlabs](https://ethlabs.org/) is a non-profit R&D lab founded by five former senior EF researchers, focused on settlement speed, mainnet capacity and institutional infrastructure. [Ethereum Institutional](https://www.coindesk.com/tech/2026/07/01/ethereum-gets-a-new-nonprofit-focused-on-institutional-adoption) is a non-profit offering banks and asset managers a neutral point of contact as they evaluate the chain. **So what:** three organisations, the same funders, and a clear pattern. Work that serves institutions found money quickly.

### The gap

The restructuring follows the mechanism and policy line almost exactly.

Core developers and the Foundation own the mechanism, and that work is funded and progressing. Companies set the policy, especially for institutions, and that work is funded and progressing faster. The Foundation consolidated its research under a mandate called CROPS, covering censorship resistance, resilience, openness, privacy and security, and [assembled a distributed privacy cluster](https://www.coindesk.com/tech/2025/10/09/ethereum-foundation-expands-privacy-push-with-dedicated-research-cluster) under the [Privacy Stewards of Ethereum](https://pse.dev/) banner.

What did not survive the [40% budget cut and 54 job losses in June 2026](https://www.techtimes.com/articles/318949/20260623/ethereum-foundation-cuts-54-jobs-shuts-zk-research-lab-slashes-budget-40.htm) was PSE as an engineering organisation. PSE was the lab that turned zero-knowledge research into shipped code. It maintained [MACI](https://maci.pse.dev/), which enables voting where no one can prove how they voted and therefore no one can buy the vote, and [Semaphore](https://semaphore.pse.dev/), which lets someone prove they belong to a group without revealing which member they are. It also did the deeply unglamorous work of shrinking proof generation until it runs on a mid-range phone rather than a server.

None of that has an obvious commercial owner. Anonymous voting infrastructure does not have a customer with a procurement budget. Proof performance on cheap hardware benefits everyone downstream and is billable to no one. These are shared inputs that every project on the map above consumes and none has an incentive to fund alone, which is the textbook shape of a public good and the textbook reason it gets underprovided when the organisation that was carrying it stops.

The mandate still lists privacy. The lab that executed on it is gone.

### It is going to take a village

There are real grounds for optimism here, and they are worth stating before the caveat.

Five years ago, "privacy on Ethereum" meant one mixing contract and a lot of arguing. Today there is a coherent division of labour across five layers, with credible teams at each. Inclusion guarantees are being written into the protocol. Wallets are getting privacy as a dependency rather than a project. Shielded pools have found a compliance story that survives contact with a regulator. Institutions are deploying real money on confidential rails. That is not a roadmap, it is shipped or shipping work.

The caveat is that the shape of the funding now tilts toward whoever can pay. Institutional privacy has customers and will be fine. Protocol mechanisms have the Foundation and the core developer process and will be fine. The shared cryptographic substrate in between has neither, and it is the part that everything else quietly depends on.

That gap is fillable, and the mechanisms to fill it already exist in this ecosystem. Retroactive funding, protocol guild style ongoing support for maintainers, L2 sequencer revenue directed at upstream dependencies, and the grants programmes that have funded exactly this kind of work for years. What it needs is for the projects that consume MACI, Semaphore and fast client-side proving to treat them as infrastructure they are jointly responsible for, rather than as free inputs that someone else will keep maintaining.

No single organisation is going to carry applied cryptography for Ethereum again. The Foundation just demonstrated that it cannot, and no company has a reason to. Which leaves the village.
