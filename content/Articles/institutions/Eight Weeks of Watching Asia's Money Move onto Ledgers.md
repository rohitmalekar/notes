---
title: "Eight Weeks of Watching Asia's Money Move onto Ledgers"
tags:
  - Web3
type:
  - Article
permalink: monsoon-ledger-eight-weeks
date: 2026-10-31
description: "A monthly step back from The Monsoon Ledger: what changed in Asian onchain finance in September and October 2026, which of my calls are holding, and what India would need to change to join in."
draft: true
---

I started [The Monsoon Ledger](https://themonsoonledger.com/) on 7 September. Every Monday since, I have read the circulars, consultation papers, bank releases and Ethereum core developer calls that touch regulated finance in India, Singapore and Hong Kong, and written them up as plainly as I can. Eight [Weekly Briefs](https://themonsoonledger.com/brief/), 43 entries on the [Pilot Scorecard](https://themonsoonledger.com/pilots/) and 26 items on the [Regulatory Wire](https://themonsoonledger.com/wire/) later, I have noticed a problem with my own method.

Weekly writing rewards the event. A licence is granted or a testnet forks, and it gets its paragraph and its source link. The week does not show drift, the slow change in what people are arguing about. In traditional finance that drift takes a year or more. Here it took about a month, because regulation and Ethereum's own roadmap are moving in the same weeks and reacting to each other.

So I am trying a monthly step back, in my own voice. The Ledger sticks to what a document says and labels my opinion as opinion. Here I get to think out loud.

## The argument moved from the asset to the money

In early September I thought the story was tokenisation: which bonds, funds and deposits would go on a ledger. By the end of October the asset had become the easy part. The question regulators now answer in public is which money settles it.

The answers split within a few weeks of each other. Hong Kong's fourth digital green bond, priced on 28 September, let investors in the Hong Kong dollar tranche pay in tokenised bank deposits for the first time ([Weekly Brief No. 5](https://themonsoonledger.com/brief/5-hk-green-bond-tokenised-deposits/)). India's [Demat 2.0](https://themonsoonledger.com/pilots/in-sebi-demat-2-tokenised-corporate-bonds/) settles tokenised corporate bonds only in the RBI's wholesale CBDC, so commercial bank credit never enters settlement. Singapore issued two tokenised MAS Bills settled in wholesale CBDC, and on 9 October MAS's Chia Der Jiun said of stablecoins: "There may be limits to their suitability for settling large wholesale transactions" ([Weekly Brief No. 6](https://themonsoonledger.com/brief/6-glamsterdam-sepolia-gas-limit/)). Hong Kong's Policy Address pointed retail the other way, toward licensed stablecoins settling tokenised money market funds ([Weekly Brief No. 3](https://themonsoonledger.com/brief/3-hkdap-business-payments-policy-address/)).

I find this a more honest debate than the stablecoin-versus-CBDC one it replaced. Each central bank is deciding how much private credit it will allow into the plumbing, and each answer follows its own history. India trusts the infrastructure it owns. Hong Kong lets banks and licensed issuers compete. Singapore wants a stablecoin to earn its place. If you only read one explainer from the Ledger, make it [why a tokenised deposit and a stablecoin are different claims](https://themonsoonledger.com/under-the-hood/2026-09-tokenised-deposits-and-stablecoins/).

## Public chain, closed door

I expected a long fight between public and private ledgers. What I saw instead is a token on Ethereum mainnet whose contract decides who may hold it.

[HKDAP](https://themonsoonledger.com/pilots/hk-anchorpoint-hkdap-stablecoin/), Hong Kong's licensed dollar stablecoin, runs on Ethereum mainnet, and every holder's wallet is whitelisted by a distributor. In September it paid its first real invoices, for logistics and staff hotel bookings. Singapore's draft stablecoin law would require issuers to trace, freeze and burn tokens onchain, and left open whether to restrict wallets as well ([Weekly Brief No. 1](https://themonsoonledger.com/brief/1-singapore-stablecoin-law-freeze-powers/)). On 19 October J.P. Morgan took its JPMD deposit token to Ethereum mainnet, while every bank deposit token I track in Singapore and Hong Kong still runs on a private ledger ([Weekly Brief No. 8](https://themonsoonledger.com/brief/8-jpmd-ethereum-mainnet/)).

The moment that changed my thinking was the Financial Stability Board's note to the G20 on 12 October. The FSB says it cannot tell where stablecoin holders are, because public chains are pseudonymous. HKDAP's whitelist, built to satisfy an anti-money laundering rule, gives the issuer exactly that data ([Weekly Brief No. 7](https://themonsoonledger.com/brief/7-fsb-stablecoins-untested-cross-border/)). The compliance officer and the financial stability regulator want the same record, and the token contract is the one place that can hold it.

The next problem is privacy. A whitelisted token on a public chain shows every holding to anyone who looks. On 23 October EthSystems published a proof of concept for confidential money market fund shares on Ethereum, and the same day a token standard with Ant Group authors, which approves transfers through zero-knowledge proofs, moved to Review. I wrote up [where the EthSystems design fits among the ways Asian funds keep their registers](https://themonsoonledger.com/under-the-hood/2026-10-tokenised-fund-registers/). My guess is that privacy, more than throughput, will decide whether the next Asian issuers pick a public chain.

## Ethereum's upgrade calendar is now a bank's problem

Ethereum's next upgrade, Glamsterdam, raises the gas cost of writing new state. Writing to an empty storage slot goes from 20,000 to 97,920 gas. On 22 October the Ethereum Foundation postponed the upgrade on the Hoodi testnet to study how that repricing interacts with contracts already on mainnet. Five pilots on the Scorecard in Singapore and Hong Kong run contracts on Ethereum mainnet, and none of their issuers has said whether their code uses the patterns at risk ([Weekly Brief No. 8](https://themonsoonledger.com/brief/8-jpmd-ethereum-mainnet/)).

In [Weekly Brief No. 4](https://themonsoonledger.com/brief/4-glamsterdam-testnet-asia-issuers/) I wrote that Glamsterdam strengthens the case for Ethereum mainnet. I still think so. What I underweighted is that a bank on a public chain inherits a change process it does not control, decided on open calls by developers who may not know its contract exists. That is what MAS's caps and the HKMA's "extra caution" are pricing ([Under the Hood on whitelisted tokens](https://themonsoonledger.com/under-the-hood/2026-09-whitelist-on-a-public-chain/)). I would like to see an Asian issuer, or its tokenisation agent, speak up on an All Core Devs call before mainnet.

Hoodi, the testnet that slipped, is named after a metro station on Bengaluru's Purple Line.

## Calls I made and how they are holding

- Singapore should stop at trace, freeze and burn, and not restrict holders' wallets ([No. 1](https://themonsoonledger.com/brief/1-singapore-stablecoin-law-freeze-powers/)). The consultation closed on 16 October. MAS has not responded. Open.
- Swift's blockchain ledger is the shortest route for Singapore's tokenised deposits to settle against assets on public chains ([No. 2](https://themonsoonledger.com/brief/2-swift-ledger-demat-permissioned/)). Swift has still not named the chain, and no such transaction has happened. Open, and I am less sure of it.
- Hong Kong will split settlement by investor: licensed stablecoins for retail, tokenised deposits and CBDC for institutions ([No. 3](https://themonsoonledger.com/brief/3-hkdap-business-payments-policy-address/)). HSBC launched RedCoin to 3.3 million PayMe users on 23 October and plans to let customers buy a tokenised money market fund class with it. Holding.
- Glamsterdam makes Ethereum mainnet an easier place for issuers to stay ([No. 4](https://themonsoonledger.com/brief/4-glamsterdam-testnet-asia-issuers/)). The Hoodi delay complicates it. Holding, with the caveat above.

## India, in the week Devcon comes to Mumbai

India is good at building rails. UPI carried about 86 per cent of India's retail payment transactions in 2025-26 ([Under the Hood](https://themonsoonledger.com/under-the-hood/2026-10-retail-e-rupee-and-upi/)). Demat 2.0 issued Rs 1,025 crore of tokenised bonds in its first week and settles them against central bank money at the same moment ([Under the Hood](https://themonsoonledger.com/under-the-hood/2026-09-demat-2-tokenised-bonds/)). The RBI built its own Unified Markets Interface to tokenise assets and settle them in wholesale CBDC.

Then look at India's row in the [State of Play](https://themonsoonledger.com/state-of-play/). On [public chains](https://themonsoonledger.com/state-of-play/public-chains/), [stablecoins](https://themonsoonledger.com/state-of-play/stablecoin-rules/) and [bank crypto exposure](https://themonsoonledger.com/state-of-play/bank-crypto-exposure/), the status is "none". [Licensing](https://themonsoonledger.com/state-of-play/licensing/) is AML registration with FIU-IND and nothing more. Crypto policy arrives through tax, 30 per cent on gains and 1 per cent deducted on transfers, and through enforcement, such as the FIU's notices to 15 offshore platforms in September ([Regulatory Wire](https://themonsoonledger.com/wire/2026-09-09-in-fiu-notices-15-vda-service-providers/)). Retail e-rupee in circulation fell last year.

India is building a state-run version of the onchain stack: its own ledgers, its own settlement asset, its own market interface. At home that is coherent, and the engineering is impressive. The cost shows at the border. The arrangements forming in Asia this autumn connect regulators to each other. Bank Negara Malaysia and the Bank of Thailand joined MAS's BLOOM on 23 October ([Regulatory Wire](https://themonsoonledger.com/wire/2026-10-23-sg-mas-bloom-bnm-bot-cross-border/)), and the HKMA and Bank Negara agreed a joint workstream on cross-border stablecoin use on 6 October. Each assumes a settlement asset or a network that more than one jurisdiction can reach. A rupee that exists only on RBI infrastructure cannot join without a bridge the RBI has not described, even though the RBI itself names cross-border use as a reason to keep building the e-rupee.

What I think would need to change:

- A sandbox route to a public chain. SEBI's sandbox already hosts Demat 2.0. One issuance on a public chain, under the controls Singapore named in April (whitelisted wallets, issuer freeze and correction, a documented point of finality, audited contracts), would teach Indian regulators more than another year of private-ledger pilots.
- A capital rule for bank exposure to tokenised assets. Hong Kong has applied the Basel cryptoasset standard since January 2026 and Singapore has an interim treatment. Without one, no Indian bank can price holding a token on a public chain, so none will.
- A government position on stablecoins, separate from the RBI's. A licence limited to fully reserved, rupee-referenced coins would meet the RBI's concern about monetary control and give Indian firms a regulated instrument. The Parliamentary Standing Committee on Finance's study of virtual digital assets is the obvious place for it to start.
- A first corridor for the wholesale e-rupee with a central bank that is already in one of these regional networks.
- A tax that does not charge every transfer. A 1 per cent deduction on each movement makes onchain settlement of anything classed as a virtual digital asset uneconomic for frequent use.
- Rules for transfers to self-hosted wallets under the travel rule, which India's guidelines do not yet cover ([Under the Hood](https://themonsoonledger.com/under-the-hood/2026-10-travel-rule-in-practice/)).

## Watching in November

New Hoodi and mainnet dates for Glamsterdam. MAS's response to its stablecoin consultation. CMU OmniClear's digital asset platform and CBDC settlement on EnsembleTX in Hong Kong, both promised by year-end. How JPMD admits holders on Ethereum, and whether it names a client in Asia.

If you are at Devcon in Mumbai and work on any of this, especially from the Indian side, I would like to compare notes. The Monsoon Ledger publishes every Monday at [themonsoonledger.com](https://themonsoonledger.com/), with the sources behind everything above.
