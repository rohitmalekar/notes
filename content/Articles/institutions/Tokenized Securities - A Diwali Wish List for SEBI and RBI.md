---
title: "Tokenized Securities: A Diwali Wish List for SEBI and RBI"
tags:
  - Web3
type:
  - Article
permalink: tokenized-securities-diwali-wish-list
date: 2026-10-07
description: "The SEC and SEBI agree that a tokenized security should be fungible with its conventional twin: same identifier, same rights, convertible without loss. The US has written that principle down filing by filing and now runs it in production. India's Demat 2.0 pilot reaches the same principle inside a sandbox that leaves the basic legal questions open. A ten-point wish list for India's regulators, with stop-losses built into the design."
---

SEC and SEBI both agree, in principle, that tokenized securities ought to be fungible. In other words, a tokenized share or bond is the same instrument as its conventional twin: it has the same identifier and the same rights, and it can move between the two forms without loss. But there is a vast difference in how those principles transition into practice.

## The US, one filing at a time

In the US, the principle has been written down, one filing at a time, and is now running in production.

### Guidance and definitions

In January 2026, staff from three SEC divisions [said](https://www.cooley.com/news/insight/2026/2026-02-04-statement-on-tokenized-securities) the format of a security doesn't change how the securities laws apply. They sorted tokenized securities into three kinds: issued by the issuer, custodial and synthetic. In March, the SEC and CFTC [jointly defined](https://www.winston.com/en/blogs-and-podcasts/capital-markets-and-securities-law-watch/sec-clarifies-the-application-of-federal-securities-laws-to-crypto-assets) a "digital security" as a security whose record of ownership is kept, in whole or in part, on a crypto network.

### Trading in the same order book

Also in March, the SEC [approved Nasdaq's rule](https://www.dechert.com/knowledge/onpoint/2026/3/sec-issues-landmark-interpretation-on-the-application-of-federal.html) to trade tokenized Russell 1000 stocks and major-index ETFs in the same order book as ordinary shares. The tokens use the same CUSIP and ticker and carry the same rights. Settlement stays at T+1 through DTC.

### Settlement in production

Under its December 2025 no-action letter, DTC [ran live production trades](https://finance.yahoo.com/markets/crypto/articles/dtcc-executes-first-live-trades-175751804.html) on 15 July with more than 30 firms. The trades ran on Hyperledger Besu and Canton and covered equity and Treasury delivery-versus-payment, repo, securities lending and collateral pledges. DTC says a tokenized position converts back to the traditional form at will. The [full service](https://www.dtcc.com/news/2026/may/04/dtcc-advances-development-of-new-tokenization-service) is due this month.

### The innovation exemption

On 17 September, the SEC [issued a five-year "innovation exemption"](https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment) for trading tokenized NMS stocks on-chain. Venues can run permissioned automated market makers on public, permissionless chains, provided the token carries the same economic and voting rights as the share. The [order has its own stop-losses](https://www.sidley.com/en/insights/newsupdates/2026/09/sec-issues-innovation-exemption-for-onchain-trading-of-tokenized-us-listed-stocks):

- For the largest stocks, a venue can list at most 75 symbols and trade at most 0.25% of each stock's daily volume.
- No leverage is allowed.
- Trading halts whenever the underlying stock halts.
- Every trading participant is screened.
- A venue must give the issuer 30 days' notice before trading a third party's token of its stock.
- Trade data is published within ten minutes.

Two days ago, OKXICE, a joint venture of ICE and OKX, [became the first to file](https://finance.yahoo.com/markets/crypto/articles/nyse-parent-just-filed-tokenize-025259404.html) under the exemption, for 63 stocks.

### Shareholder records on public chains

Registered transfer agents already keep the official shareholder record on public chains. [Franklin Templeton](https://sec.gov/Archives/edgar/data/1786958/000174177323002447/c497k.htm) has done it for its money market fund since 2021, and [Galaxy](https://www.galaxy.com/newsroom/galaxy-superstate-launch-glxy-tokenized-public-shares) has done it for its Nasdaq-listed shares since 2025.

## India's Demat 2.0 pilot

In India, the most advanced step is Demat 2.0, which SEBI and RBI [launched last month](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2026/successful-launch-of-demat-2-0-pilot-project-for-tokenised-corporate-bonds_104418.html). REC, L&T and IIFL issued ₹1,025 crore of tokenized bonds, settled in wholesale CBDC. SEBI's [FAQ](https://www.sebi.gov.in/sebi_data/faqfiles/sep-2026/1789049630065.pdf) says "the token is the corporate bond". So the principle is the same.

The way India got there is different. The depositories own the ledger, they hold investors' private keys, and they remain the legal record. Per the same FAQ, that design leaves the Depositories Act, 1996 untouched. The pilot runs inside SEBI's regulatory sandbox, with relaxations for a fixed scope and period.

## Questions the sandbox leaves open

Remove any one of those supports and the basic legal questions have no answer:

- Can a token on a ledger the depositories don't own be legal evidence of ownership? No provision says so.
- Is a tokenized bond a virtual digital asset under India's tax law, attracting 30% tax and 1% TDS on every transfer? The VDA definition is wide enough to catch it, and I have yet to see a notification that carves it out.
- Who collects stamp duty when a transfer settles on a ledger rather than through an exchange or depository?
- Can a foreign investor hold an Indian tokenized security outside a demat account? No FEMA rule addresses it.
- When is a transfer on a ledger legally final, and which record wins if the ledger and the depository disagree?
- RBI's tokenized certificates of deposit on the [Unified Markets Interface](https://www.rbi.org.in/Scripts/BS_SpeechesView.aspx?Id=1525) are [live](https://www.rbi.org.in/Scripts/AnnualReportPublications.aspx?Id=1466), and RBI has yet to say whether the token is the legal record or a mirror of one.

## A Diwali wish list for India's regulators

I know Christmas ain't close, but hey, Diwali is. Here's my wish list for regulatory stance in India to adopt distributed ledgers for tokenized securities, with stop-loss baked in the design.

1. Write the token into law. Amend the Depositories Act, or SEBI's regulations under it, so that a record on an approved distributed ledger can be the register of ownership, kept by a depository or a licensed token registrar.
2. Make fungibility a right. A tokenized security should keep the same ISIN and convert to and from ordinary demat form at par, on demand, within a day. This is the first stop-loss: if a ledger fails, the investor walks back to demat with nothing lost.
3. Keep a golden record. Reconcile the ledger against the depository daily, and state in the rules which record prevails in a dispute.
4. Carve tokenized securities out of the VDA definition, and tax the instrument rather than the wrapper.
5. Let public chains in with the controls Hong Kong and Singapore already require: whitelisted wallets, and the power for the issuer or depository to freeze and force-transfer.
6. Cap tokenized issuance and trading, as the SEC's innovation exemption does with symbol and volume limits for US stocks. Raise the cap only after each period of clean reconciliation and settlement data, and pause new issuance automatically if a reconciliation break crosses a set threshold.
7. Publish the sandbox's graduation criteria up front, so issuers know what data moves a pilot into a standing framework and what ends it.
8. Give approved ledgers settlement finality in statute, and collect stamp duty by smart contract at the point of transfer.
9. Open a FEMA route, starting at GIFT City, for foreign investors to hold Indian tokenized securities.
10. Publish the numbers from Demat 2.0 and UMI: settlement times, costs and investor counts.

I publish weekly at [The Monsoon Ledger](https://themonsoonledger.com/) on how banks, market infrastructure and regulators across India, Singapore and Hong Kong could use Ethereum for tokenization, settlement and verification.
