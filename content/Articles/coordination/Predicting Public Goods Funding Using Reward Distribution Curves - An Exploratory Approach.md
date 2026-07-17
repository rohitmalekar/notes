---
title: Predicting Public Goods Funding Using Reward Distribution Curves - An Exploratory Approach
tags:
  - Web3
  - AI
  - Data-Analysis
date: 2025-01-15
description: "An exploratory approach to predicting public goods funding: can power-law patterns in reward distribution curves — an 'invariable' across Gitcoin, Optimism, and Open Collective grant rounds — predict how much a project would receive without relying on noisy data?"
type:
  - Article
---
_This post is inspired by the ongoing mini-contest from_ [deepfunding.org](http://deepfunding.org)_, a special New Year’s initiative to replicate judgments from real-world funding decisions. By drawing on data from past grant rounds—across platforms like Open Collective, Gitcoin, and Optimism—participants aim to develop mechanisms that predict the funding a project would have received. By tackling this challenge, participants contribute to shaping fairer funding ecosystems for Ethereum-related projects and beyond. See the contest details [here](https://cryptopond.xyz/modelFactory/detail/306250?tab=0)_
tl;dr
- Understanding the patterns in the allocation of public goods funding can help design predictive models for fund distribution without relying on unavailable or noisy data.
- This post explores the potential of leveraging "invariables" across grants ecosystems such as the power law in reward distribution curves to predict individual project funding and relative weights between any two projects.

There is a healthy non-zero chance this route may not yield respectable results for the contest. Proceed with caution!
#### Key Insights and Motivation
Understanding the broader patterns in public goods funding can provide valuable insights into designing predictive models. Below are key observations that highlight why focusing on reward distribution curves is both practical and promising.
- **Power Law Distribution as an Invariable:** Across grant rounds, the reward distribution curve consistently exhibits power law characteristics:
    - The top 20% of projects often capture 60% or more of the total funding.
    - This pattern holds true across Quadratic Funding in Gitcoin and Retro Funding in Optimism, albeit with variations in scale and steepness.
    ![[QF and Retro Funding.jpeg]]
    
- **Dataset Observations:**
    - 95% of the dataset for the mini-contest is derived from Open Collective, which follows even an extreme version of the power law compared to Gitcoin and Optimism. Top-ranked projects receive disproportionately higher allocations compared to lower-ranked ones, as shown here in quarterly sampling of the funding data.
    ![[Open Collective.png]]

#### Leveraging the Reward Distribution Curve
Reward distribution curves offer a simple yet powerful framework to understand and predict funding allocations. By focusing on the shape of these curves and the relative positions of projects, this approach aims to provide accurate and scalable predictions for public goods funding.
1. **Predict the Shape of the Curve:**    
    - Use historical data to model the power law distribution for a given ecosystem.
    - Derive parameters that define the curve's shape for different ecosystems.
2. **Rank Projects on the Distribution Curve**
    - Predict the percentile position of a project (or pair of projects) based on their characteristics.
    - Use this position to estimate:
        - The share of funds a project might receive.
        - Relative weights for comparing any two projects.

#### Potential Benefits of This Approach (Remains to be tested with data)
- **Generalizability:** By focusing on distribution patterns rather than specific data points, the model becomes more robust to variations in datasets and funding ecosystems.
- **Efficiency:** Eliminates the need for heavy feature engineering and reliance on noisy or unavailable data at prediction time.

#### Early Hypothesis for Building Data Sets for Feature Analysis
To accurately predict the percentile positions of a project on the reward distribution curve, constructing comprehensive datasets is essential that capture the essence of a project’s visibility, impact, and ecosystem relationships. Agnostic of technical feasibility, the features could include:
- **Project Popularity Metrics:** Quantitative indicators such as GitHub stars, forks, and contributor activity that signify a project’s popularity within the developer community.
- **Development Activity Metrics:** Additional metrics like the team size, number of commits, pull requests merged, issues closed can be valuable inputs to predicting relative impact.
- **Historical Funding Data:** Information about a project’s past grant participation and funding amounts, reflecting its financial trajectory.
- **Community Engagement:** Metrics like social media mentions, active discussions in community forums, and broader participation metrics to gauge community support.
- **Dependency Networks:** Connections with other projects, such as dependencies or collaborations, to highlight interdependencies within the ecosystem.

Once these datasets are curated, the following steps can enhance their utility:
1. **Derived Features:** Develop additional features such as funding growth rates, trends in activity, and network centrality scores, which provide deeper insights into a project’s dynamics.
2. **Correlation Analysis:** Use exploratory data analysis (EDA) to identify relationships between these features and funding outcomes.
3. **Feature Selection:** Apply techniques like recursive feature elimination (RFE) to isolate the most impactful predictors, ensuring the model’s focus on meaningful and actionable insights.