---
title: Open Collective As a Decentralized Global Public Good
tags:
  - Web3
  - Startup-Finance
type:
  - Article
permalink: open-collective-publicgood
date: 2022-02-01
description: The following is a thought experiment to explore how Open Collective can [Exit to Community](https://www.colorado.edu/lab/medlab/2020/08/31/exit-community-community-primer). The goal here is to "transition from a privately owned company to a structure that allows us to share power and revenue" with its community comprising of employees, Fiscal Hosts, Collectives, funders, investors, and individual contributors.
---

The following is a thought experiment to explore how Open Collective can [Exit to Community](https://www.colorado.edu/lab/medlab/2020/08/31/exit-community-community-primer). The goal here is to "transition from a privately owned company to a structure that allows us to share power and revenue" with its community comprising of employees, Fiscal Hosts, Collectives, funders, investors, and individual contributors. 

You can read about Open Collective and its pursuit to exit to the community [here](https://opencollective.com/e2c).

This proposal is based on how [Commons Stack](https://commonsstack.org/) has approached realigning incentives around public goods. The incremental changes take the company from a privately held start-up to a self-governing and continuously funded community.

In summary, the article proposes for the platform to be treated as a public good. The  result is a continuous organization<sup>1</sup> powered by a self-sustaining funding mechanism to preserve it as a public good. The setup relies on a token bonding curve to align incentives to produce socially-beneficial behaviors and outcomes.<sup>2</sup>

#### Open Collective as a Public Good Powered by Curve Bonded Crowdfunding

One of the key questions raised in the article, [Early musings on "Exit to Community" for Open Collective](https://blog.opencollective.com/exit-to-community/), is as follows:

> **How can we future-proof Open Collective Inc. for the thousands of communities around the world that rely on it?**

The article proposes achieving this by treating the Open Collective platform as a global public good. The platform is already non-excludable, allowing all kinds of groups to raise, manage, and spend money transparently. It also meets the criteria for being non-rivalrous where use by one person neither prevents access of other people nor does it reduce availability to others.

While the limitations of the capitalistic markets to create and preserve public goods is well established, there is growing research to support public goods using crypto-economic incentive design<sup>3</sup>. Specifically, the next order question is: 

> **Can we define the socially and financially desirable outcomes for Open Collective and work backward to codify rules that incentivize a vested community towards those outcomes?**

Here is a set of outcomes to start this exercise with:
1. Enable community governance inclusive of a variety of stakeholders across the globe
2. Preserve the core purpose by granting control to those who care about it the most
3. Build self-sustaining liquidity to allow existing investors to exit and fund future operations
4. Incentivize long-term contributors who can help meet future needs of the community

Here’s a conceptual view of the building blocks to achieve these outcomes.

![[Screenshot 2022-02-06 at 1.20.12 AM.png]]

The focus of this article will be on mechanism design. It is a sub-discipline of economics that deals with designing protocols that incentivize rational actors to behave in socially desirable ways<sup>3</sup>. The [Augmented Bonding Curve](https://medium.com/commonsstack/the-augmented-bonding-curve-part-1-a-web3-way-to-fund-public-goods-7c9d1a871ae2) as a mechanism design provides continuous funding to establish and maintain a shared public good. It incentivizes group behavior around the collection and prudent use of shared community resources.

For brevity, the rest of the article does not delve into the technical design<sup>1</sup> of the bonding curves to codify these incentives. Also, the design allows optionality for the specific types of governance to apply on top of the mechanism design. This enables the community in essence to BYOG or "Bring Your Own Governance"<sup>2</sup> and is not a topic that is addressed at this time.
	
Each of the subsequent phases outlines the desired outcome, exit criteria, and assumptions that progressively take Open Collective closer to its goal to exit to community using Augmented Bonding Curve. For a technical description of how Augmented Bonding Curves work, see [this](https://medium.com/commonsstack/deep-dive-augmented-bonding-curves-b5ca4fad4436) article.

1. **Seed Phase:** Identify trusted community members using a reputation system who earn the right for future governance and ownership. This is accomplished pending a precise definition of associated economic gains. This is by design.
2. **Hatch Phase:** This is an invitation for the seed members to bootstrap the community with a pre-determined goal of funds. In return, the member tokens offer a stake in ownership and control. The outcome is a system for funding "labor" i.e. actions that have a positive impact on the community.
3. **Open Phase:** This phase extends the capital contributions to investors who may not be directly associated with the commons. In exchange, the investor members receive a stake that enables financial returns but not control.

#### Seed Phase: Setting the Foundations for Self Governance

**OBJECTIVE:** Identify the initial group of value-aligned seed members in the community. They will become eligible for the economic stake and control rights in the next phase. This is based on their proof of participation i.e. qualifying contributions in the community.

**WHY:** The rest of the article remains bullish on the ability of judiciously coded contracts to build a community. Yet, the proposal also recognizes the limitations of relying only on "economic incentives as institutional glue".<sup>5</sup> 

> **How can a community exploit the possibilities of self-governance without entirely relying on economic incentives?**  

It is important to seed the effort with value-aligned members to be the vanguards in this journey.

![[Seed Phase.png]]

**HOW:** Establish processes and systems that recognize members based on their qualifying contributions. These members earn the right to take part in the Hatch Phase.

For example, invite proposals from the community to improve the platform during the seed phase. Authors of the qualified proposals get recognized and gain their standing. Additionally, members who participate with valuable inputs for these proposals also get recognized. An exercise like this sets in motion the cultural foundations needed to pivot to community-led governance.

**EXIT CRITERIA:** This phase identifies a diverse set of trusted community members with representation across the different stakeholders of Open Collective. 

**ASSUMPTION:** Different stakeholders of Open Collective may have varying levels of interest in actively owning and governing the new decentralized entity. 

These stakeholders include employees, Fiscal Hosts, Collectives, funders, investors, and individual contributors. The Seed Phase allows each constituent to make an informed choice for the role they seek to play in Open Collective's future. These roles may vary between control-and-ownership (outlined in the Hatch Phase), ownership-only (outlined in the Open Phase), or neutral (no change to the current state).

#### Hatch Phase: Bootstrapping the Community

**OBJECTIVE:** Bootstrap the community by funding an initial goal from the qualified community members from the Seed phase. In return, the community members receive tokens locked in a vesting period. However, the tokens can be used to drive governance and fund operations. These initial funds are placed in two separate pools - a Reserve Pool and a Funding Pool. This is the point of transfer of active governance to the token holders from the Hatch Phase.

**WHY:** The two pools work together to create a self-sustaining funding mechanism. The distribution of tokens to qualified community members pairs incentives with intrinsic motivation. The vesting period prevents any actions to drive speculative returns. There are now opportunities to assess governance mechanisms to fund initiatives and resources.

![[Hatch Phase.png]]

**HOW:** From a conceptual standpoint, a bonding curve is an interface between the internal economy of the community and the outside world. It creates liquidity to provide incentive-aligned funding for what matters most to the community while putting multiple safeguards for manipulation and speculative activities. 
- The capital in the Reserve Pool is bonded to the curve
- The newly minted tokens are locked in a vesting period to allow Reserve Pool to be stable
- The capital in the Funding Pool remains un-bonded as a floating source of capital
- The tokens are slowly unlocked in correlation to how much capital has been allocated to fund “labor” within the community
- With the vesting process and introduction of a governance model, the token holders are economically incentivized to allocate funding to curated proposals

**EXIT CRITERIA:** Initial funds are raised and distributed between the Reserve Pool and Funding Pool.

**ASSUMPTION:** Community members are familiar with managing crypto wallets to receive tokens and use them to participate in active governance. While this may be a challenge today, with an ever-growing interest in enabling community tooling for crypto-enabled governance, user-friendly solutions will soon be on the horizon for adoption at scale.

#### Open Phase: Decentralization at Scale

**OBJECTIVE:** Attract new investors and qualifying members that see the impact of the community and want to be a part of the movement so that the Funding Pool can grow. The investor tokens enable financial returns but investors cannot participate in the governance.

**WHY:** The system reserves control for the most direct value creators. Thus, the qualifying members keep long-term control of the organization. The liquidity by attracting investors makes the organization more resilient.

![[Open Phase.png]]

**HOW:** Interested new investors can mint tokens by contributing funds into the curve in return for "investor tokens". New qualifying members identified by the reputation system can also buy member tokens. Both contributions go into the Reserve Pool. <sup>6</sup>

Hatch phase members can liquidate their tokens based on:
- a predetermined vesting period, and
- the extent to which funds from the Funding Pool are allocated to projects based on a governance structure

With this vesting process and the introduction of a governance model, members are economically incentivized to allocate funding to curated projects that have the most beneficial impact.

Lastly, whenever members liquidate their tokens, a small percentage of their returns go into the Funding Pool as "Exit Tax". This activates funding of the commons while members are earning returns.

#### Open Collective as a Continuous Organization

So what do we have so far? Let's revisit the outcomes we started with:

1. Enable community governance inclusive of a variety of stakeholders across the globe
	- The Seed Phase identifies value-aligned community members to bootstrap the funding
	- Friction-less stake in ownership and control for qualified members at a global scale
	- The tokens in themselves don't enforce any particular type of governance. This enables the community to design governance processes appropriate to what's at stake

2. Preserve the core purpose by granting control to those who care about it the most
	- New non-member investors are prohibited from participation by design in the Seed and the Hatch Phase
	- Open Phase investors only receive a stake in ownership but do not have governance rights
	- The qualifying members from the Hatch and Open Phase keep long-term control of the organization

3. Build self-sustaining liquidity to allow existing investors to exit and fund future operations
	- The Augmented Bonding Curve offers a continuously open primary market
	- If the demand exceeds supply, tokens are minted providing ongoing funding
	- Enables investors to sell at market price and at a pace they want

4. Incentivize long-term contributors who can help meet future needs of the community
	- Community members get a share of the value if the organization is successful
	- This enables the same long-term financial benefits as employees
	- The liquidity enables the community to be less distracted and focus more on the execution

#### Other Considerations

**How can the existing investors exit as part of this transformation?**
Existing investors could choose between the following alternatives:
- The community can  use the initial funds from the Reserve Pool to pay investors who want to exit
- Investors could choose to receive investor tokens during the open phase and sell at the market price at the pace they want

**How can the structure be inclusive to respond to the needs of various types of stakeholders for Open Collective?**
This will require outreach and education in the Seed Phase. The intent is to encourage all types of stakeholders to participate in qualifying activities to be eligible to receive member tokens. If the diversity of the members is inadequate in the Hatch Phase, the process will need a manual reset or intervention before adequate representation is reached.

**How are profits treated in the model?**
Surplus cash flow and donations can be distributed as follows:
- A fraction could be used to mint new tokens and distribute them to current (investor and member) token holders
- The rest could be directed to the Funding Pool to invest in projects and resources deemed beneficial to the group

#### No Silver Bullets
To see the world's first [Augmented Bonding Curve in action](https://medium.com/commonsstack/the-augmented-bonding-curve-part-1-a-web3-way-to-fund-public-goods-7c9d1a871ae2), check out [Token Engineering Commons](https://tecommons.org/) building token engineering public goods without donation. Bonding curves are helpful in low-liquidity environments and an efficient primary market maker. 

> **At the same time, tokens alone don't build communities - a sense of belonging rooted in a shared value-driven purpose does.**

As we apply the construct of bonding curves to Open Collective, it would be shortsighted to ignore potential challenges in enabling governance using cryptoeconomics in the context of Open Collective's roots, culture, and aspirations. Here's is a preliminary list of topics that need further exploration to avoid narrow incentives overpowering the common good<sup>7</sup>.

**1. Personhood of Participants**
Implementing a reputation system to identify qualifying contributors and their proof of participation is a high-cost activity and increases friction for new members for Open Collective. The investor members in the Open Phase do not have governance rights similar to the current investors in Open Collective. However, with obscured identity, there is a risk of a single actor masquerading as many users. 

**2. Holistic Representation of Community Interests**
The reputation system is intended to avoid voter apathy and bring the most committed members into the fold for making decisions that matter. However, it also implies only a subset of the globally diverse Open Collective community can get involved in token ownership. How can the governance structure be designed so as to respond to the needs of:
- the community members not included in the economic relationship?
- future members who did not have a chance to participate in the initial design?

**3. Technical Complexities of Bifurcating Ownership and Control**
Tokens belonging to qualified community members identified by their proof of participation have a stake in ownership as well as control in decision making. Investor tokens only offer ownership. The implementation details to mint and burn the dual-natured tokens on the same bonding curve need to be assessed for feasibility.

#### Wrap up
Coin voting governance is still in its infancy and the current forms of coin voting are far from being "safe defaults"<sup>8</sup>. At the same time, the mechanism design proposed in the form of Augmented Bonding Curves is not hard-wired to specific forms of governance. This offers an opportunity to further study if the incentive alignment and funding enabled by the bonding curve can be paired with a tailored governance setup for Open Collective's aspirations.

**ABOUT:**

[Open Collective](https://opencollective.com/) is a platform where communities can collect and disburse money transparently, to sustain and grow their projects. The platform provides tools for legal entities to fiscally sponsor Collectives under their umbrella, empowering people to create associations without friction. It's like an API between the legacy world of banks and taxes and the emerging future of digitally powered distributed collaborations.

[Commons Stack](https://commonsstack.org/) is building commons-based microeconomies to sustain public goods through incentive alignment, continuous funding, and community governance. The library of open-source, interoperable web3 components will put effective new tools in the hands of communities, enabling them to raise and allocate shared funds, make transparent decisions, and monitor their progress in supporting the Commons.

[Exit to Community (E2C)](https://e2c.how/) is a project of [MEDLab](https://www.colorado.edu/lab/medlab/) at the University of Colorado Boulder and [Zebras Unite](http://zebrasunite.com/). It's a different kind of story, one that connects the founders, workers, users, investors, activists, and friends who have been trying to feel their way toward a better kind of startup. Its endgame is to be a long-term asset for its community, co-owned and co-governed by those who give it life.

**ADDITIONAL REFERENCES:**

<sup>1</sup> Michael Zargham, Jamsheed Shorish, and Krzysztof Paruch, 2019, [From Curved Bonding to Configuration Spaces](https://epub.wu.ac.at/7385/1/zargham_shorish_paruch.pdf) 
<sup>2</sup> Thibauld Favre, 2018, [Introducing Continuous Organizations](https://hackernoon.com/introducing-continuous-organizations-22ad9d1f63b7), HackerNoon
<sup>3</sup> Jeff Emmett, 2018, [Rewriting the Story of Human Collaboration](https://blog.goodaudience.com/rewriting-the-story-of-human-collaboration-c33a8a4cd5b8), Good Audience (Medium)
<sup>4</sup> Laina Emmanuel, 2018, [Crypto-economic incentive design for public goods](https://medium.com/@lainaemmanuel/crypto-economic-incentive-design-for-public-goods-2bd26668d505), Medium
<sup>5</sup> Nathan Schneider, 2021, [Beyond Cryptoeconomics: Platform Cooperativism and the Future of Blockchain Governance](https://thereboot.com/beyond-cryptoeconomics-platform-cooperativism-and-the-future-of-blockchain-governance/), The Reboot
<sup>6</sup> Nathan Schneider, 2022, [Policy Proposals for Crypto Protocols to Make Them Less Dystopic and More Inclusive](https://hackernoon.com/policy-proposals-for-crypto-protocols-to-make-them-less-dystopic-and-more-inclusive), HackerNoon
<sup>7</sup> Nathan Schneider, 2022, [Cryptoeconomics as a Limitation on Governance](https://osf.io/dzasq/?view_only=a10581ae9a804aa197ac39ebbba05766) (DRAFT v.20220121)
<sup>8</sup> Vitalik Buterin, 2021, [Moving beyond coin voting governance](https://vitalik.ca/general/2021/08/16/voting3.html)

