---
title: "Tokenizing Bharat: rules, rails and rollouts"
tags:
  - DLT
type:
  - Article
permalink: tokenizing-bharat
date: 2026-11-11
description: "Notes from the Devcon 8 Mumbai panel with Pramod Rao, Sanmesh Kalyanpur and Pramod Mishra on how India can bring in tokenization: how a regulator reads a new instrument, the rails India already runs, and what pilots in grain warehousing and bonds need to show before they scale."
draft: false
---
![](https://www.youtube.com/watch?v=S1J_lg-Anac)

*Notes from the panel I moderated at Devcon 8 Mumbai for ETHIndia, with Pramod Rao (ex Exec Director, SEBI), Sanmesh Kalyanpur (Director of Programs, Finternet Labs) and Pramod Mishra (Director, PwC).*

India has trillions of rupees locked in gold, unpaid invoices, warehouse grain, buildings and highways. These assets are hard to split, slow to move and hard to trade.

Tokenization puts them on a shared ledger where they can be divided and transferred quickly. Speed works in both directions, though. A bad position that a regulator could once stop in time can now spread before anyone steps in.

So I opened the panel with one question for the stage: how does India bring in tokenization without breaking what already works? With a former regulator, an infrastructure builder and someone running live deployments on the panel, I organized my questions around rules, rails and rollouts.

## The panel

- Pramod Rao has sat on every side of this table: lawyer, startup founder and regulator. He was inside SEBI when REITs and InvITs took root, and has served on the board of IFSCA.
- Sanmesh Kalyanpur works on Finternet, the tokenization effort from the team that built Aadhaar, UPI and Account Aggregator.
- Pramod Mishra has spent more than 12 years building blockchain systems with institutions, including policy design for India's carbon credit market with the Ministry of Power and four years on a Swift steering committee.

## Rules: how a regulator reads a new instrument

**My question to Pramod Rao:** builders, and I include myself, often see the regulator as the one saying no. When a new economic instrument lands on a regulator's desk, how do they evaluate it?

He pushed back on "move fast and break things." His alternative was to build deliberately, so that new instruments become lasting institutions instead of things that make confidence evaporate or carry risks nobody imagined.

> "You are in a jungle if you are working in the arena without regulation. What regulation seeks to do is create a playground. People who come into the playground know that there is a rule, there is a referee, there is somebody who will call out if there is unfair play." (Pramod Rao)

I asked him to explain [IFSCA](https://www.ifsca.gov.in) for the room. He called it India's offshore-onshore regulator. It sits in [GIFT City](https://giftgujarat.in), Gujarat, and combines the powers of the RBI, SEBI, the insurance regulator and the pension regulator for that zone. It has published a discussion paper on real-world asset tokenization and runs an active sandbox. His view is that GIFT City is a sandbox for the whole country: anything that works there and isn't tied to foreign currency could be deployed across India.

## Rails: Finternet and what India already runs

**My question to Sanmesh Kalyanpur:** I read the [Finternet white paper](https://www.bis.org/publications/working-paper-1178-finternet-financial-system-future) once, then four more times, because the idea was so new. What is Finternet, and what is the vision?

He said he got worried when he heard "four times." :) Then he laid out the problem Finternet is built around. Money moves easily inside India thanks to UPI, but not from America to Singapore or Namibia. Stocks, money and even marksheets each live on separate ledgers with their own rules. And people still have to go back to their bank for records that are already theirs, for something as routine as a visa application.

> "There are more than 100 types of assets. If we try to solve everything, it'll take us hundreds of years." (Sanmesh Kalyanpur)

Tokenization is the instrument he sees: a way to standardize different assets so they can move together, with regulators setting the rules, in five to ten years.

**My question to Pramod Mishra:** you've written about India as the world's tokenization factory. Can you rub some of that optimism on the rest of us?

He answered with live deployments:

- He said India's carbon credit registry, which [Grid India operates](https://www.mondaq.com/india/renewables/1767018/carbon-credits-enter-the-market-indias-first-regulatory-framework-for-exchange-traded-carbon-credit-certificate), runs on Hyperledger Besu, an Ethereum client, and he expected it to go live nationally within two months.
- For cross-border payments, he described a CBDC rail on one side, [Swift's blockchain-based shared ledger](https://www.finextra.com/the-long-read/1468/what-swifts-blockchain-ledger-means-for-stablecoin-innovation) carrying ISO 20022 data in the middle, and regulated stablecoins on the other.
- Broadridge's Distributed Ledger Repo (DLR) settles [close to $8 trillion of repo a month](https://thefintechtimes.com/broadridge-dlr-hits-8trn-monthly-repo-volume-with-28-yoy-growth/), and [Broadridge's India team worked on it](https://935thelloyd.com/?p=790821). In September 2026 Broadridge launched [DLX](https://www.broadridge.com/press-release/2026/broadridge-launches-dlx), a wider tokenization platform built on DLR.
- The RBI's Unified Markets Interface began with tokenized certificates of deposit settled in wholesale CBDC, and the RBI has said it [plans to add more asset classes](https://www.deccanchronicle.com/business/economics/rbi-considering-gold-tokenisation-says-rbi-exec-director-at-gff-1986165), such as commercial paper and corporate bonds.

> "You need to know the left side of the story, the as-is, and the right side, which is the innovation, and then you need to see where things actually collide and where they work together." (Pramod Mishra)

## Rules: India has fractionalized assets before

**My question to Pramod Rao:** tokenization is a buzzword now, but REITs and InvITs already let small investors own a slice of a building or a highway. What should we carry over from that regulatory experience?

He described a glide path of more than ten years. Access started with investors who understood the instrument and could afford a loss. The minimum ticket for a REIT began around ₹10 lakh, came down in steps, and today you can buy a single unit on the exchange. Online bond platforms followed the same logic. Bonds are an institutional product almost everywhere, so SEBI built a regime to open them up, and there are now 30 to 35 such platforms.

Then he gave the example I'd point every builder to. When digital gold took off, the regulator responded with electronic gold receipts, after several rounds of consultation. Some digital gold players didn't see their business model in the final rules and stayed outside. He called that a fatal flaw, while also saying regulators should keep a listening ear.

The numbers he shared make the case. Electronic gold receipts have done about ₹100 to 200 crore in cumulative sales since launch. Digital gold now averages at least ₹2,000 to 3,000 crore a month.

> "It takes two to tango. I would genuinely hope the entrepreneurs in that space and the regulators come together to see what is the bridge. And maybe that might be the very first real-world asset that can easily get tokenized and distributed." (Pramod Rao)

## Rails: one token across many chains

**My question to Sanmesh Kalyanpur:** there's the GIFT City sandbox, NPCI's DLT work, the Unified Markets Interface, Finternet, and your pilots on other chains. If you had a whiteboard, how would you draw the way these fit together for India?

He described Finternet as a highway that stays neutral about the chains joining it. His example was a tokenized warehouse receipt. A farmer could use it to borrow from several banks, and those banks may want a permissioned chain or an RBI chain. The same token could also go into DeFi pools through an SPV on Ethereum or Solana, and be lent onward in countries where that is allowed. Finternet's job is to set the token standards each route requires.

He is running four or five pilots and expects one in five to stick.

> "Theoretically everything looks good. When you hit the ground, you get to know that it's really different than what is being told on stage." (Sanmesh Kalyanpur)

**My question to Pramod Mishra:** you've argued for separating regulated tokens from everything in the wild west. Why does that matter, and what would it make possible?

He started with the vague way people talk about "tokenizing land." Who holds the legal ownership, and who holds the economic ownership? He split tokens into two kinds. A digital twin carries only the economic right while the legal right stays with today's registries, such as the depositories under SEBI. A token that carries both rights brings its own risks and governance questions, which makes it far harder to regulate.

He also listed what sits around any token: AI on one side, quantum on the other, smart contracts that can be exploited and private keys that can be lost. His answer is to build on the identity and payment rails India has already scaled. He had a lighter moment too: millennials will wait out T+2 settlement, but Gen Z won't.

> "India has so much diversity. If one move goes wrong, it will actually impact the last-mile person in the country." (Pramod Mishra)

## Rules: what a regulator checks before scaling

**My question to Pramod Rao:** SEBI's pilot has tokenized more than ₹1,000 crore of bonds. Say it's running well a year from now. What signals would a regulator look for before opening access or moving to the next asset?

He was clear that he's stepped away from SEBI and was hypothesizing. This was his lens:

1. The token must keep what the regulator wanted from the original instrument. If a bond can only be sold at ₹1 lakh face value, the token has to represent that ₹1 lakh. Fractionalization itself isn't the problem: some bonds already go down to ₹10,000 and ₹1,000 when they meet certain norms.
2. Instant settlement changes how the market clears. India is already on T+1, with T+0 proposed. Atomic delivery-versus-payment means every trade settles gross instead of being netted at the exchange. Does gross settlement raise risk across the system? Does it disrupt clearing?
3. Ownership has to stay traceable. About 99% of Indian securities are held in demat form in the beneficial owner's own name, unlike street-name holdings in the US. Can a wallet give the regulator that same confidence? Two depositories have run this since 1996, and the market has grown on top of them.

> "For those who are building around bonds, what is it you're trading off versus what you're trading up for?" (Pramod Rao)

The netting point is the one I hear least in tokenization pitches, and it's the one I'd want answered first.

## Rollouts: grain warehouses and pilot red flags

**My question to Sanmesh Kalyanpur:** I've spent more than my share of time at sub-registrar offices fighting paperwork. For your pilot you picked grain and warehousing. Why?

He sorts pilots on two axes, impact and hurdle, and looks for high impact with a low hurdle. On high-hurdle projects his line was: "I'm 36, I'll take 60 to do it." Among the 2030 use cases they explored, warehouse financing was one of only one or two that fit.

Field visits to Sangli, Nanded, Panvel and around Lonavala changed his picture. Only about 10% of India's warehouses are regulated. Some have limited bank credit lines, some are just storage with no financing, and corporate warehouses run their own capital financing. Each type has different problems.

The pilot's goal is to cut information asymmetry, so a bank can approve or reject a loan with confidence. The token carries more than 200 data fields into a bank's loan origination system. These include the farmer's verifiable credentials, an independent sampler's assessment, a dynamic rating, the warehouse's vintage and whether the stock is insured against rodent damage.

> "Imagine a personal loan is a derivative of your CIBIL score. Can we make a warehouse loan a derivative of that token?" (Sanmesh Kalyanpur)

It's an 18-month project, now in design. He expects a research paper on what worked and what didn't in six to nine months, and credited both Pramods as advisors on the pilot.

**My question to Pramod Mishra:** you've seen pilots across industries. What are the early red flags that tell you a pilot won't have an impact?

The biggest one, he said, is emotional attachment to the technology, which leads teams to present the technology as the solution. His method starts with a problem. Validate it with peers, map how the existing process copes today, then build a proof of concept. With AI, he said, a POC takes about two days. His own early example is a [blockchain birth certificate system](https://www.business-standard.com/article/pti-stories/civic-body-using-blockchain-tech-to-prepare-tamper-proof-birth-118122000595_1.html) for New Town Kolkata Development Authority, live since December 2018.

> "You need to align that with the people, with the ecosystem, and then place technology, rather than the other way around." (Pramod Mishra)

## Lightning round: one asset each

**My question to all three:** assume the regulations, safeguards and technology all work as expected. Which one asset would you tokenize first in India?

- Pramod Mishra: stocks.
- Sanmesh Kalyanpur: anything for MSMEs and farmers, so the assets of India Two and India Three get liquidity.
- Pramod Rao: MSME trade receivables, and deep-tier supply chain finance in particular.

> "The creamy layer actually manages to get the credit. But the deep tier, the minute you are minus three, minus four from the key supply chain partners, they struggle a lot." (Pramod Rao)

Two of the three went to MSME credit. On stage I cited roughly ₹25 lakh crore as the MSME credit gap. SIDBI's latest estimate puts it closer to [₹30 lakh crore](https://www.sidbi.in/blog/the-msme-credit-gap-in-india-what-does-the-data-say), so that's where I'd watch for the first pilots that matter.

The morning had opened with the point that the barrier to building keeps falling, which makes the choice of what to build matter more. This panel gave me a sharper list of what to build and what has to hold while we build it.

My thanks to Pramod Rao, Sanmesh Kalyanpur and Pramod Mishra. The full recording is on the Ethereum Foundation's YouTube channel: [Tokenizing Bharat](https://www.youtube.com/watch?v=S1J_lg-Anac).

*I write about institutional finance and DLT in Asia at [The Monsoon Ledger](https://themonsoonledger.com).*
