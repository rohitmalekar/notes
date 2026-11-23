---
title: "Asia Has Opened the Venue to Ethereum but Not Yet Settlement"
tags:
  - DLT
  - Decentralization
type:
  - Article
permalink: ethereum-in-asia
canonical: https://themonsoonledger.com/essays/asia-opened-venue-not-settlement/
date: 2026-11-17
description: "Read side by side, the stablecoin, tokenisation and settlement rules of India, Singapore, Hong Kong, Japan and South Korea show regulators accepting Ethereum as an issuance venue for permissioned tokens, while central banks keep settlement on their own ledgers. The open questions cluster at the self-hosted wallet, bank capital rules and cross-border recognition. Those decide whether regulated assets ever meet open Ethereum."
draft: false
---

Since September, I have tracked a handful of narrow questions across India, Singapore, Hong Kong, Japan and South Korea for [The Monsoon Ledger](https://themonsoonledger.com/). Who may issue a stablecoin. Whether a tokenised bond is still a bond. Which money settles a tokenised trade. Whether a bank may touch a public blockchain at all. Each [State of Play](https://themonsoonledger.com/state-of-play/) entry answers one of these, market by market, with a source for every line.

Last week I added Japan and South Korea to every entry and read them all together for the first time. The five regulators agree on more than their press releases suggest, and the questions they have left open cluster in the same few places. If you work on Ethereum, or at a bank deciding whether to use it, those clusters tell you where the next two years will be decided.

### 1. Every Market Agrees on the Law and Disagrees on the Ledger

All five markets treat a [tokenised security](https://themonsoonledger.com/state-of-play/tokenised-securities-rules/) as the same security under existing law. India's Demat 2.0 bonds carry the same rating, trustee and disclosure rules as any other bond. South Korea's January 2026 amendments keep a security token under the same rules as any other security. Japan has done this since May 2020, and Hong Kong calls it a traditional security with a tokenisation wrapper.

They part ways on the ledger. India's tokenised bonds sit on a ledger the depositories own. South Korea's draft rules require one shared by at least two account managers and the Korea Securities Depository. Japan's digital bonds run on consortium chains such as ibet and Canton. Singapore and Hong Kong let regulated funds issue on Ethereum, under conditions.

![Which ledger regulated finance uses, by market and instrument](ethereum-asia-ledger-map.svg)
*Figure 1. Which ledger regulated finance uses in each market, as of 16 November 2026.*

> In Asia, the argument has moved on from whether tokenisation is legal to who owns the ledger it runs on.

### 2. Central Banks Are Keeping Settlement for Themselves

None of the five central banks [settles on a public chain](https://themonsoonledger.com/state-of-play/settlement-projects/), and none has said it will. Each has picked its own settlement asset. India uses a wholesale e-rupee on the RBI's Unified Markets Interface. Singapore issued its first tokenised MAS Bills in September and October 2026, settled in wholesale CBDC. Hong Kong's EnsembleTX settles tokenised deposits between banks in central bank money, around the clock, still as a pilot. South Korea's Project Hangang runs on a ledger where only participant banks run nodes. Japan has no wholesale settlement asset at all, and its banks are testing tokenised deposits and stablecoins instead.

Public chains connect only at the edge, through bank money and licensed stablecoins. Even there, I read the HKMA's interoperability standard as keeping the interbank leg in central bank money, with stablecoins allowed in only as an asset.

> Settlement is the last thing a central bank will hand to a network it does not run.

### 3. A Housing Society on a Public Road

Singapore and Hong Kong reached the same answer separately. A regulated institution may issue on a [public, permissionless chain](https://themonsoonledger.com/state-of-play/public-chains/) if the controls sit inside the token: a holder whitelist, an issuer power to freeze and an issuer power to correct. MAS's April 2026 capital proposal lists them, along with audited contracts and a documented point of finality. The SFC's tokenisation circular and the HKMA's custody guidance give a permissioned token as the example. HKDAP, UBS's money market fund, DBS's structured notes, OCBC's GOLDX and Hang Seng's gold ETF class all run this way on Ethereum mainnet.

If you live in Bangalore, you know the apartment society with a gate and a guard. It sits on public roads, draws city water and power, and relies on the city police. Yet the guard decides who walks in. The association can clamp a car parked in the wrong spot. The society keeps its own register of who owns which flat, and what goes on inside rarely spills into the street market outside.

A permissioned token on Ethereum works much the same way. Mainnet supplies the road: uptime, shared security and a ledger no single party can rewrite. The whitelist is the guard. The freeze and correction powers are the clamp. In Hong Kong's tokenised fund classes, the trustee keeps the legal register offchain, just as the society keeps its own records. And the tokens rarely wander into DeFi or self-custody.

For the city, the catch is that it carries the traffic without getting the trade. Ether itself, which has no issuer, stays out of the lighter treatment in both markets.

> Regulators have accepted Ethereum as a venue by moving trust from the chain into the token contract.

### 4. Stablecoins Are Being Built to Look Like Banks

Asia's [stablecoin rules](https://themonsoonledger.com/state-of-play/stablecoin-rules/) are producing a narrow payment instrument that does not compete with bank deposits. Japan limits issuance to banks, funds transfer service providers and trust companies. South Korea's government draft centres issuance on banks with a stake of 50% plus one. HSBC is one of Hong Kong's first two licensees. Hong Kong bars interest to holders, Singapore has proposed banning it, and Japan's FSA says holders are not expected to earn income. India rejects private stablecoins outright and points to its CBDC.

Compare that with how stablecoins grew on Ethereum: issued by non-banks, held in self-custody and used as the cash leg of DeFi. The Asian versions keep the peg and the programmability and drop most of the rest. Singapore's draft adds a duty to trace, freeze and burn tokens used for illicit activity. In practice that changes little, since the large fiat-backed contracts on Ethereum already carry freeze functions.

> Asia is licensing the stablecoin as a payment instrument and leaving the yield and the open access behind.

### 5. The Fight Is at the Wallet

Every market applies the [travel rule](https://themonsoonledger.com/state-of-play/travel-rule/) to transfers between service providers. They differ at the moment value leaves a regulated firm for a wallet the user controls. Hong Kong asks the customer to prove ownership, for example by signing a message. Japan's regulator and police asked exchanges in August 2026 to register, screen and hold new withdrawal destinations. South Korea's draft foreign exchange decree would make each transfer to a personal wallet reportable. Singapore is weighing limits on unhosted wallets for MAS-regulated stablecoins. India's January 2026 guidelines say nothing on the subject, which leaves each exchange to decide.

Self-hosted wallets are how most people use Ethereum directly. If Singapore adds wallet limits, its regulated stablecoins will be shut out of self-custody and DeFi by rule.

> The self-hosted wallet is the line regulators are still drawing, and it decides whether regulated assets ever meet open Ethereum.

### 6. Japan Ran It the Other Way Round

Look again at Figure 1. In Singapore and Hong Kong, tokenised funds reached public chains before regulated money did. Bosera's ETF classes went onto HashKey Chain, an Ethereum layer 2, in April 2025, more than a year before HKDAP opened to institutions in August 2026. Singapore has no licensed stablecoin yet. Japan did the reverse. JPYC, a registered funds transfer service provider, has issued yen on Ethereum mainnet with open access since October 2025, while every Japanese security token I track sits on a consortium chain.

Japan's rulebooks are silent on the ledger. The stablecoin rules govern the issuer, the reserve and where assets are held. No securities rule sets public-chain conditions either. So the choice fell to the industry, and the industry split. A payments firm went for reach. Securities houses and megabanks stayed on platforms they control: the megabanks' July 2026 stablecoin test ran on a blockchain built for SMBC.

> When a regulator stays silent on the ledger, each industry picks the ledger that suits its own risks.

### 7. The EVM Is Spreading Faster Than Ethereum

Even where public chains lose, Ethereum's software tends to win. Japan's DCJPY network plans to run on Hyperledger Besu, an Ethereum client run as a consortium chain. DBS Token Services and mBridge run EVM-compatible ledgers. South Korea's draft rule could be met by a permissioned deployment of an EVM client.

That is good news for Ethereum's developers, auditors and tooling vendors. It is weaker news for mainnet. A bank that runs the EVM privately adopts the standard without joining the network, its fee market or its neutrality.

> Asia is adopting Ethereum's software as an industry standard while keeping its network at arm's length.

### 8. Capital Rules Decide How Big Any of This Gets

Securities law has largely made room for tokenisation. [Bank capital](https://themonsoonledger.com/state-of-play/bank-crypto-exposure/) has not. Under the Basel cryptoasset standard, a token on a permissionless chain lands in Group 2, with a risk weight of up to 1,250%. Hong Kong has applied the standard since January 2026. Singapore deferred it to 2027 or later and proposed a Group 1 route for bank tokens on permissionless chains with issuer controls, capped at 2% of Tier 1 capital. India has not implemented the standard, and Japan and South Korea have not started.

That cap keeps bank issuance on public chains at pilot scale. The Basel Committee's targeted review, due later in 2026, may matter more to Ethereum in Asia than any securities rule this year.

> The binding constraint on banks using Ethereum is a capital ratio, and it is set in Basel.

### The Shape That Is Forming

Put the entries together and a structure appears. Central bank ledgers form the settlement core. Tokenised deposits and licensed stablecoins act as bridges. Public chains become a distribution layer for regulated assets with controls in the token. Self-custody and open DeFi sit beyond a gate of travel rules, wallet checks and whitelists.

![The structure forming across five Asian markets](ethereum-asia-structure.svg)
*Figure 2. The structure forming across the five markets.*

The risk in this structure is five national stacks that cannot talk to each other. Cross-border recognition is where that gets settled: whether Singapore's route for foreign-regulated stablecoins covers Hong Kong's licensees, which foreign regimes Japan deems equivalent, and how far BLOOM goes now that the central banks of Malaysia and Thailand have joined. A public chain no single country runs is an obvious meeting point for regulated assets from different jurisdictions. Whether regulators accept it as one is still open.

Several dated tests fall in the next five months.

![Dated tests between November 2026 and March 2027](ethereum-asia-timeline.svg)
*Figure 3. Dated and pending decisions, November 2026 to March 2027.*

### What It Means for Ethereum

| Role | Where Ethereum stands | Evidence |
|---|---|---|
| Issuance venue | Winning, on conditions | HKDAP, UBS, DBS, OCBC, Hang Seng and JPYC on mainnet |
| Software standard | Winning | Besu for DCJPY; EVM ledgers at DBS Token Services and mBridge |
| Settlement layer | Losing, for now | No central bank settles on a public chain |
| Open DeFi and self-custody | Contested | Whitelists, freeze powers and wallet rules |

The uncomfortable question for the Ethereum community is whether mainnet can host regulated finance without being hollowed out by it. A permissioned token borrows the network's security and gives back little of what makes the network valuable: composability, open access and neutral settlement. These tokens could bring institutions onto mainnet and loosen their controls as supervisors gain comfort (best case). Or mainnet becomes a cheaper host for walled gardens while the EVM moves into private deployments anyway (worst case).

The rulebooks themselves point to what would shift the balance:

- A change of default for permissionless chains in the Basel Committee's targeted review.
- Layer 2 safeguards, which MAS already cites as an advance since the Basel standard was written.
- A finality law that treats a finalised Ethereum checkpoint as final against insolvency law. Today an issuer can name the checkpoint in its documents, as MAS asks, but a contract that points to it may not bind a liquidator.
- A published point of finality for each layer 2, so an issuer knows which of the sequencer's confirmation, the batch on mainnet or the end of a challenge window counts.
- Allowlists built on attestations a holder carries across issuers, in place of one whitelist per contract.
- Privacy that still lets an issuer and a supervisor see what they must.

The last three are engineering problems, and the Ethereum community can start on them now. MAS and the HKMA have already written down what they need to see.

If you build on Ethereum, which side of the gate is your work on?

PS: Every fact here links back to a [State of Play](https://themonsoonledger.com/state-of-play/) entry on The Monsoon Ledger, which I update as the rules change.
