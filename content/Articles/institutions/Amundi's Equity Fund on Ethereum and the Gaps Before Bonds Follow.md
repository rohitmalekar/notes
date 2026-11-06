---
title: "Amundi's equity fund on Ethereum, and the gaps before bonds follow"
tags:
  - DLT
type:
  - Article
permalink: amundi-ethereum-bond-gaps
date: 2026-11-06
description: "Amundi has put a tokenized share class of its STOXX Europe 600 index fund on public Ethereum. Funds can already be issued and held there. Bonds still need Basel to move, a path to central bank money, and onchain privacy that keeps positions confidential."
draft: false
---

Europe's biggest fund house has [put a tokenized share class of its flagship STOXX Europe 600 index fund on public Ethereum](https://www.marketsmedia.com/amundi-unveils-tokenised-access-to-a-flagship-index-fund/). Taking stock (no pun!), here is what this means for Ethereum, and what it doesn't.

## Names stay offchain, balances are public

How does Amundi handle privacy on a public chain? Short answer: names stay offchain, balances are public. Amundi hasn't published the full design, but regulated fund tokens usually work like this: wallets are whitelisted, the transfer agent holds the KYC and the mapping between address and investor, and Ethereum records which address holds how many units.

![[amundi-fund-token-subscription.webp]]

Who keeps the register matters more than it looks. I compared [the ways Asian funds keep their register](https://themonsoonledger.com/under-the-hood/2026-10-tokenised-fund-registers/), and each choice changes who can see the holders.

## So why Ethereum?

A private ledger can pull this too. But private DLTs can become silos. Many institutions have run permissioned chain pilots over the last few years, and many of those never connected to anything else. The ones that did needed a bridge, a re-issue or a new interoperability layer.

On Ethereum, a fund unit can be paid for in the same transaction that delivers it, and euro cash is starting to arrive as stablecoins. [EURXT, issued by CACEIS](https://www.caceis.com/press-releases/credit-agricole-launches-eurxt-its-euro-denominated-stablecoin), settled a subscription into Amundi's tokenized money market fund in July. The whole euro stablecoin market is still only about €800m.

Wallets and custodians already support the token standards, and an issuer can keep its whitelist, freezes and forced transfers inside the contract. That pattern of [a whitelist on a public chain](https://themonsoonledger.com/under-the-hood/2026-09-whitelist-on-a-public-chain/) is already live in Asia, in products like [DBS's tokenized structured notes](https://themonsoonledger.com/pilots/sg-dbs-tokenised-structured-notes/). [Singapore and Hong Kong both allow it](https://themonsoonledger.com/state-of-play/public-chains/), with controls.

Moving past funds is where the work is cut out for Ethereum.

## Bank capital is the biggest hurdle for bonds

For bonds, bank capital rules are the biggest hurdle, because banks underwrite, make markets in and repo them. Under Basel's crypto rules, a tokenized bond gets normal capital treatment only in Group 1. Anything outside it can mean holding capital equal to its full value. Basel doesn't qualify public chains for Group 1 yet, though it has had [a targeted review](https://www.bis.org/press/p260520.htm) open since November 2025.

Basel only binds banks once a local regulator adopts it, so this varies across geographies. The US has proposed no implementation. The UK and EU are behind. [Asia is split too](https://themonsoonledger.com/state-of-play/bank-crypto-exposure/). Singapore's MAS has [proposed letting public-chain tokens into Group 1 within caps](https://themonsoonledger.com/wire/2026-04-17-sg-mas-permissionless-cryptoassets-prudential/), and its conditions include [a documented point of finality](https://themonsoonledger.com/under-the-hood/2026-09-when-a-tokenised-transfer-becomes-final/). Worth watching how it shapes up. Until Basel moves, banks under these rules won't hold Ethereum-based bonds at scale.

## Settlement cash is the next gap

Stablecoins work for fund subscriptions, but large bond issues and repo want central bank money. The [ECB's Pontes](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260921_1~5a011ecbea.en.html) went live in September and links DLT platforms to T2.

![[amundi-bond-central-bank-settlement.webp]]

India went the same way that month. Its [first tokenized corporate bonds](https://themonsoonledger.com/wire/2026-09-10-in-sebi-rbi-demat-2-tokenised-bonds/), ₹1,025 crore from REC, L&T and IIFL, settled in wholesale CBDC on [a private, depository-owned ledger](https://themonsoonledger.com/under-the-hood/2026-09-demat-2-tokenised-bonds/).

Hong Kong is explicit about it. HKMA's [Project Ensemble Interoperability Standard](https://www.hkma.gov.hk/media/eng/doc/key-functions/ifc/fintech/cbdc/Project-Ensemble-Interoperability-Standard.pdf) calls central bank money "the settlement asset of choice for wholesale financial transactions", and [EnsembleTX has now moved to 24/7 real-value transactions](https://themonsoonledger.com/wire/2026-11-02-hk-hkma-ensembletx-24-7-tokenised-efbs/). I track how [the three markets compare on settlement](https://themonsoonledger.com/state-of-play/settlement-projects/).

That cash sits off Ethereum, so the same-transaction payment that works for funds doesn't carry over to bonds yet.

## Ethereum+ needs privacy ready

And then there's what Ethereum+ needs to get right. Ethereum+ for me is everything that sits on top of the protocol to keep balances confidential onchain while still letting the right parties read them. A bond desk won't want its positions readable by anyone with a block explorer.

A few years ago, the loudest thing in privacy on Ethereum was Tornado Cash (and the arguing over sanctions). Today teams are building for regulated assets, but it's early. Zama's confidential tokens are live on mainnet, and [EthSystems has proofs of concept](https://themonsoonledger.com/brief/8-jpmd-ethereum-mainnet/) for private money market funds and bonds.

## Where this leaves things

Funds will keep coming onto Ethereum. Bonds need Basel to move and a path to central bank money. By then Ethereum+ needs to be privacy ready.

![[amundi-ethereum-by-asset.webp]]

---

*I write [The Monsoon Ledger](https://themonsoonledger.com/), a weekly publication on Ethereum and Asian finance.*
