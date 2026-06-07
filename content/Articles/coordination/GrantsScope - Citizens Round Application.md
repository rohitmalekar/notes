---
title: GrantsScope - Citizens Round Application
tags:
  - Web3
type:
  - Article
permalink: grantsscope-citizens-round
date: 2023-06-01
description:
---
Note: This grant application is entirely for retroactive funding for existing AI utilities.

As Gitcoin Grants scale, it becomes important to improve the discoverability of projects for the effective distribution of public goods funding. With the advent of LLMs (Large Language Models), we can reduce information asymmetry for donors to make an informed choice. 
## What?
GrantsScope is an AI-based conversational experience for Gitcoin Grants donors to discover value and impact-aligned grantees.
## Why?
An experience that matches the user’s style and pace to discover content is more effective than relying solely on pre-defined information hierarchies. By surfacing relevant content programmatically, projects without a strong marketing muscle can have a level playing field with others.
## Proof of Impact

### Product #1: Citizens Round I

![[Screenshot 2023-09-26 at 3.39.23 PM.png]]

- **Live application link:** https://gitcoin-citizens-round.streamlit.app/

- **Description:** Focused on the grantees in the inaugural Gitcoin Citizens Round, you can inquire about a grantee's impact, search for projects on a topic you care about, or even get a song written about your favorite public greats!

- **Sample output:**

![[Screenshot 2023-09-26 at 3.42.05 PM.png]]

![[Screenshot 2023-09-26 at 3.49.23 PM.png]]

![[Screenshot 2023-09-26 at 3.44.04 PM 1.png]]

- **Usage**:

![[Screenshot 2023-09-26 at 3.53.13 PM.png]]
### Product #2: GG18 Climate Round

![[Screenshot 2023-09-26 at 3.55.55 PM.png]]

- **Live application link:** https://gg18-llm.streamlit.app/

- **Description:** A ChatGPT-like experience to explore grantees in the climate round of GG18. New features added:
	- Conversational memory to facilitate conversations like ChatGPT
	- User feedback capture (using 👍 and 👎) 
	- Improved response quality by porting codebase to Langchain for granular control
	- Improved performance by using vector database instead of flat files

- **Sample Output:**

![[Screenshot 2023-09-26 at 4.11.14 PM.png]]

![[Screenshot 2023-09-26 at 4.11.29 PM.png]]

![[Screenshot 2023-09-26 at 4.11.38 PM.png]]

![[Screenshot 2023-09-26 at 4.11.47 PM.png]]

- **Usage**:

![[Screenshot 2023-09-26 at 4.44.53 PM.png]]

## Roadmap
- Expand scope to include all core rounds for GG19
- Improve ability to filter projects based on specific attributes
- Utilize logging to understand patterns in user queries and gain any insights for improving donor communications as part of the Gitcoin MMM workstream

## The Moonshot
Decentralized communities at times have the same information silos as centralized orgs, not as a result of access but difficulty of discovery. Persistent information asymmetry leads to long term damage in building a sustainable culture. 

> **Information silos create cultural silos.** 

The lessons learnt from this project can be fed to solve the larger problems in discovery of actionable content in decentralized communities, such as contributor onboarding and analysis paralysis in governance.