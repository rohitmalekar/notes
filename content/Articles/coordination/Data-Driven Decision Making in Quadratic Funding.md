---
title: Data-Driven Decision Making in Quadratic Funding
permalink: data-driven-qf
type:
  - Article
date: 2024-12-01
tags:
  - Product
  - Web3
  - Data-Analysis
description: In quadratic funding rounds with hundreds of grantees, the loudest voices tend to win—not the most impactful projects. The fix isn't more curation; it's giving donors the analytical tools to move from subjective narratives to objective, customizable evaluation of what grantees actually built. This study presents a live data-driven tool deployed during Gitcoin Grants 22 that lets donors define their own metrics and composite scores to discover and fund projects that match their priorities.
---
## Pivoting From Subjective Narratives to Objective Insights

#product #Web3 #Data-Analysis 

*Last Updated: Dec 2024*
### Abstract 
This study explores the potential of data-driven tools in enhancing quadratic funding (QF) for public goods in the web3 ecosystem. By leveraging the donation window for Gitcoin Grants 22 (GG22), the study deployed a live tool that provided QF donors with actionable insights and customizable metrics to objectively evaluate open-source software (OSS) grantees. Combining data from [Open Source Observer (OSO)](https://www.opensource.observer/) and [RegenData](https://github.com/ufkhan97/regendata), the methodology introduces a composite scoring system that balances repository activity and community engagement, allowing donors to prioritize projects effectively. This feature accommodates diverse donor objectives, whether they are supporting high-growth projects, stable and mature initiatives, or experimental endeavors.

Key findings reveal that data-driven tools empower grantee discovery, promote transparency, and foster accountability, shifting the donor experience from subjective narratives to objective evaluation. Challenges, such as potential biases in data and over-reliance on quantitative metrics, are addressed with future opportunities like predictive analytics, qualitative assessments, and lifecycle impact monitoring. By advancing data-driven decision-making, this study highlights the critical role of analytics in driving equitable and efficient funding strategies for web3 public goods.
### Introduction
Cryptocurrency and blockchain technology offer transformative potential in capital allocation, enabling efficient, transparent, and equitable resource distribution through programmable smart contracts (Owocki, 2024a). By addressing coordination failures and introducing innovative onchain strategies, these technologies have the capacity to reshape how resources are allocated, much like the internet revolutionized information sharing.

For digital public goods in web3, grants are vital in nurturing early-stage projects, empowering teams to retain sovereignty while building competitive ecosystems. Grants also attract and retain talent by supporting developers and creatives working on impactful projects, highlighting their strategic value in ecosystem growth (Gitcoin, 2023).

As the ecosystem evolves, measuring and evaluating the impact of grant programs has become increasingly critical. Moving beyond simple metrics, a blend of outputs, outcomes, and long-term impact offers a more comprehensive approach to assessment. This shift emphasizes transparency and data-driven decision-making as essential to effective public goods funding (Grant Innovation Lab at Metagov, 2024).

This research attempts to validate the effectiveness of data-driven tools in public goods funding in the context of capital allocation using quadratic funding (QF).

> ***How can data-driven tools provide QF donors with actionable insights into the outputs of open-source software (OSS) grantees, enhancing informed decision-making and transparency in public goods funding?***

This study is part of a series of experiments conducted under the [GrantsScope](https://grantsscope.xyz/) project, initially funded by the Gitcoin Citizens Round and later supported by the QF donations since GG18. These experiments include personalized grantee recommendations based on donation history and AI-driven suggestions using Retrieval Augmented Generation (RAG). Refer to [this list](https://grantsscope.xyz/) for additional insights into these initiatives.
### About Gitcoin Grants
Gitcoin Grants is a leading platform in Web3 public goods funding, leveraging quadratic funding (QF) to democratize resource allocation. By matching individual contributions with larger funding pools (Buterin, Hitzig, & Weyl, 2018), Gitcoin Grants amplify community-driven priorities, ensuring diverse voices shape the ecosystem's development. Over 250+ rounds, it has distributed over $66 million, supporting thousands of open-source projects (Gitcoin, 2024).

At the same time, in large QF rounds, where hundreds of grantees vie for attention, the brightest spotlight often falls on those with the strongest marketing. This imbalance creates a cycle where deserving projects may go unnoticed, leading to an uneven distribution of resources and opportunities (Malekar, 2024a). This disparity places additional burdens on grantees to amplify their visibility and diverts their focus from delivering meaningful outcomes. 
### Methodology
This study employs a data-driven approach to empower QF donors with actionable insights into the outputs of open-source software (OSS) grantees in GG22 (Gitcoin Grants). By integrating interactive tools and advanced metrics, the methodology enables users to customize assessments and align their funding decisions with individual preferences. Below, we detail the key steps and components of the methodology:
#### 1. Data Sources
The analysis utilizes two primary datasets:
- **Open Source Observer (OSO):** OSO maintains a large repository of open source projects called [oss-directory](https://github.com/opensource-observer/oss-directory). Indexers are run on every artifact linked to projects in the directory to produce detailed metrics on OSS project activities, including developer contributions and repository performance. GG22 grantees who submitted their application by the early deadline were added to oss-directory to capture their development activity.
- **RegenData:** RegenData was used to extract detailed information about approved grant applications from GG22 OSS rounds. The final dataset provided rich metadata for each project, including its title, recipient address, GitHub repository, Twitter handle, website, description, and a direct link to its Gitcoin Explorer page.

#### 2. Metrics Selection and Normalization
As part of their grantee discovery experience, donors can select up to three key metrics to define their custom composite measure. The available metrics derived from OSO include:
- **Repository Activity:** Commit count, merged pull requests, and closed issues over six months.
- **Community Engagement:** Star count and fork count.
Each selected metric is normalized using Min-Max normalization to scale values between 0 and 1, ensuring equitable comparison across varying magnitudes.

![[gg22_metrics_selection.png|500]]

#### 3. Weight Assignment
Users assign weights to their selected metrics, totaling 100. This weight distribution reflects the donor's priorities and is the basis for calculating the composite score. Donors can emphasize metrics that resonate with their priorities, such as development activity or community involvement, creating a personalized lens for evaluating projects.

![[gg22_weights.png|500]]

#### 4. Composite Score and Impact Efficiency Per Contributor
By allowing donors to define their composite metrics, the design shifts control from a one-size-fits-all evaluation to a customizable approach, empowering donors to actively shape their funding strategies. Based on the metrics selected by the user and relative weights, the composite score is computed as a weighted sum of the normalized metrics:

> Composite Score=(∑(Normalized Metric×Weight))×100

The final score is scaled to a range of 0 to 100, providing an intuitive metric for project comparison. The composite score combines multiple developer activity-related metrics into a single value to simplify complexity, enable comparison, and support objective decision-making. Balancing key dimensions (e.g., activity, popularity), it provides a holistic view, reduces bias, and highlights trends, making it easier to evaluate and prioritize projects or initiatives effectively.

To evaluate the efficiency of contributions, the composite score is divided by the normalized contributor count (over six months). This metric is further normalized to provide a scale of 0 to 100, highlighting the relative impact generated per contributor. The **Impact Efficiency Per Contributor** metric offers a fair and nuanced way to evaluate the productivity of open-source projects by normalizing impact relative to team size. It ensures smaller teams aren’t overshadowed by larger ones, highlights individual contributor effectiveness, and helps identify high-performing projects. 

![[gg22_scores.png]]

### User Interface
The [custom-built web application](https://gg22-grantsscope.streamlit.app/), developed using Streamlit, is designed to give donors fine-tuned control over grantee discovery, enabling them to tailor their evaluations to align with specific funding priorities. This intuitive platform offers:
- **Metric Selection and Weight Assignment**: Donors can define which metrics matter most to them (e.g., commits, merged pull requests, closed issues) and assign weights to create a personalized composite impact score.
- **Advanced Filtering Options**: Projects can be filtered based on attributes like activity levels, contributor count, age of the project, or funding round, allowing donors to pinpoint grantees that meet their exact criteria.
- **Dynamic Rankings**: A customized ranking system highlights projects based on the donor's chosen metrics and weights, making comparisons straightforward and data-driven.

#### Example: Discovering Emerging Grantees Building dApps and Apps
For example, if a donor wants to identify **emerging dApps with fewer than five contributors that demonstrate the highest impact per contributor** (measured by metrics like commits, merged PRs, and closed issues), the application can extract this information using specific filters and sorting options as follows.

![[gg22_example.jpeg]]

In contrast, when the same query is applied without filtering for project age and focuses solely on composite scores, the results may include mature projects or those with larger teams, shifting the focus away from smaller, high-impact initiatives.

![[gg22_contrast_example.png]]

By offering granular control, the application enables QF donors to fund projects that align more closely with their personal or strategic priorities, fostering a more effective and meaningful donation experience. Here are a few examples of the insights donors can uncover using the application:
- Identify Web3 infrastructure grantees with development teams of fewer than 10 members that have the most forked repositories.
- Sort the most mature grantees (first commit before January 1, 2020) in the Developer Tooling round by developer activity.
- Discover grantees with the highest commits per contributor over the last six months but with relatively unknown repositories (lowest star ratings).
### From Narratives to Numbers: Enhancing QF Donations
The user experience demonstrates how data-driven tools empower quadratic funding (QF) donors by shifting the donation experience from subjective narratives to objective evaluation of outputs. Key insights include:
- **Empowering Grantee Discovery with Self-Service Analytics**
    - Enables donors to explore and evaluate grantees independently using actionable, data-driven insights.
    - Allows customization of metrics to align with individual priorities.
    - Provides detailed views of project-level outputs, such as repository activity, community engagement, and developer contributions.
- **Objective Evaluation of Outputs**
    - Offers tools to quantify project outputs, including commits, pull requests, and issue resolutions, for a transparent activity view.
    - Standardizes project comparisons using composite scores and efficiency metrics.
- **Advancing Transparency and Accountability**
    - Improves transparency by delivering measurable insights into grantee performance.
    - Promotes equitable funding decisions by highlighting impactful projects regardless of size or resources.
    - Fosters a culture of data-driven accountability, strengthening the Web3 ecosystem's credibility and sustainability.
### Challenges and Limitations
While the methodology and findings demonstrate the potential of data-driven tools to transform quadratic funding (QF) decisions, several challenges and limitations were identified during the study:
- **Bias in Data Sources**:  Metrics, like commit counts or pull requests, may disproportionately favor specific projects, such as highly active repositories, while undervaluing others in stable or less dynamic development phases.
- **Neglect of Qualitative Aspects**: The reliance on quantitative data risks overlooking qualitative elements, such as a project's social impact or innovation potential, which are more challenging to measure but equally critical.
- **Reductionism**: Complex project contributions may be oversimplified when condensed into composite scores, potentially misrepresenting their true impact.
- **Potential for Misaligned Priorities**: Without sufficient guidance, donors may prioritize certain metrics without fully understanding their implications, leading to suboptimal funding decisions.
- **Over-Reliance on Data Transparency**: In highly competitive environments, excessive transparency could deter some grantees from participating due to fear of reputational risks associated with public performance metrics.
### Future Opportunities
The findings of this study open avenues for further innovation and improvement. The following opportunities represent strategic directions to enhance the utility and impact of the methodology:
#### 1. Integrating Predictive Analytics and AI
- **Forecasting Long-Term Outcomes**: Incorporating predictive analytics or machine learning models can help donors and funders anticipate the future trajectory of a project based on historical trends and performance data. This could include forecasting contributor growth, sustainability, and potential ecosystem impact.
- **Enhancing Decision Support**: AI-driven recommendations could provide donors with tailored suggestions for funding projects that align with their historical preferences (e.g. donation history) and strategic goals (e.g. specific use cases) in addition to current performance and predicted outcomes (Malekar, 2024b).
#### 2. Enabling Community-Driven Features
- **Incorporating Qualitative Input**: Building features that allow delegates or community members to contribute qualitative assessments, such as reviews or testimonials, could complement quantitative metrics. This would ensure a more holistic evaluation of projects, capturing aspects like innovation, social value, and ecosystem alignment that are difficult to quantify.
- **Crowdsourced Metrics Refinement**: Engaging the community in defining or weighting metrics could create a dynamic and inclusive evaluation framework that evolves with ecosystem needs, including metrics-based evaluations that are reviewed and finalized by domain experts (The Optimism Collective, 2024).
#### 3. Extending Analytics Across the Grant Lifecycle
- **Eligibility Assessment**: Analytics could be applied during the grant application stage to evaluate project readiness and alignment with funding priorities, streamlining the eligibility determination process.
- **Impact Monitoring and Reporting**: Data-driven tools could assist grantees in tracking and reporting their progress over the grant lifecycle, providing funders with real-time updates and fostering accountability. This can also help facilitate continuous rewards to impactful contributions based on past results using Auto Retro Funding (Ríos & Cheng, 2024).
#### 4. Cluster-Based Funding Strategies
- **Identifying Performance Clusters**: Analyzing patterns in project outputs and performance can reveal clusters of projects with similar strengths, challenges, or focus areas. This could enable funders to:
    - Develop tailored funding strategies for specific clusters (Lister, 2023; Owocki, 2024b).
    - Allocate resources efficiently to amplify collective impact within a cluster.
- **Fostering Collaboration**: Identifying clusters can also promote collaboration among projects with complementary goals or shared challenges, enhancing the overall ecosystem impact.
### Acknowledgments 
I am deeply grateful to Open Source Observer (OSO) and RegenData by Gitcoin for providing clean, normalized data that significantly reduced barriers in building the data pipeline. Their support allowed me to focus on enhancing the donor experience and generating valuable insights. I am also delighted by the support of 70 contributors who generously donated to this effort during the dApps and Apps Round in GG22. Since 2023, over 800 community members have supported similar experiments by contributing to the [GrantsScope](https://grantsscope.xyz/) project through their QF donations in Gitcoin Grants, following its initial funding in the Gitcoin Citizens Round.
### Appendices
- [StreamLit Prototype](https://gg22-grantsscope.streamlit.app/)
- [Github Repository](https://github.com/rohitmalekar/gg22)
- [Querying RegenData](https://app.regendata.xyz/question/369-gg22-approved-projects) (requires access)
- [How to add a project to OSS Directory?](https://docs.opensource.observer/docs/contribute/project-data)
- [How to create a collection in OSO?](https://docs.opensource.observer/docs/how-oso-works/oss-directory/collection)
- [How to retrieve key metrics for projects?](https://docs.opensource.observer/docs/use-cases/collection-view)
### References
- Buterin, V., Hitzig, Z., & Weyl, E. G. (2018). _A flexible design for funding public goods_. Retrieved from [https://arxiv.org/pdf/1809.06421](https://arxiv.org/pdf/1809.06421)
- Gitcoin. (2023). _The case for grant programs: How to incentivise ecosystem growth by funding innovation_. Retrieved from [https://www.gitcoin.co/blog/the-case-for-grant-programs-how-to-incentivise-ecosystem-growth-by-funding-innovation](https://www.gitcoin.co/blog/the-case-for-grant-programs-how-to-incentivise-ecosystem-growth-by-funding-innovation)
- Gitcoin. (2024). *Gitcoin by the numbers.* Retrieved from https://impact.gitcoin.co/
- Grant Innovation Lab at Metagov. (2024). _State of Web3 grants report_. Retrieved from [https://drive.google.com/file/d/1JBbGos6Bjdvd1LRGDvIijREic4l7Th2I/view](https://drive.google.com/file/d/1JBbGos6Bjdvd1LRGDvIijREic4l7Th2I/view)
- Lister, M. (2023, July). _Grants for public good: A roadmap for resilient democratic funding._ Retrieved from [https://gitcoin.mirror.xyz/YoSf01Pjm7ZDflCrLypbWxN0B0Fv2bYCVGLSOye8xjE](https://gitcoin.mirror.xyz/YoSf01Pjm7ZDflCrLypbWxN0B0Fv2bYCVGLSOye8xjE)
- Malekar, R. [@RohitMalekar](https://twitter.com/RohitMalekar). (2024a, March 28). _Power law in quadratic funding._ X (formerly Twitter). Retrieved from [https://x.com/RohitMalekar/status/1773102167890559420](https://x.com/RohitMalekar/status/1773102167890559420)
- Malekar, R. (2024b, January 23). _Concepts, PoCs, and early results for personalized grantee recommendations._ Retrieved from [https://gov.gitcoin.co/t/concepts-pocs-and-early-results-for-personalized-grantee-recommendations/17469](https://gov.gitcoin.co/t/concepts-pocs-and-early-results-for-personalized-grantee-recommendations/17469)
- Owocki, K. (2024a). *Onchain Capital Allocation Handbook.* Retrieved from https://allobook.gitcoin.co/
- Owocki, K. (2024b, November 6). _Allo.Expert creates strategic intelligence for Gitcoin’s multi-mechanism future._ Retrieved from [https://gov.gitcoin.co/t/allo-expert-creates-strategic-intelligence-for-gitcoins-multi-mechanism-future/19584](https://gov.gitcoin.co/t/allo-expert-creates-strategic-intelligence-for-gitcoins-multi-mechanism-future/19584)
- Ríos, J., & Cheng, R. (2024, November 19). _Auto retro funding: Continuous, simple, automatic._ Retrieved from [https://docs.opensource.observer/blog/auto-retro-funding](https://docs.opensource.observer/blog/auto-retro-funding)
- The Optimism Collective. (2024, November 22). _Retro funding 2025._ Retrieved from [https://optimism.mirror.xyz/zWlA9LROAzRee5BFqbquYHawmruKzLmXbONp_hcCwE4](https://optimism.mirror.xyz/zWlA9LROAzRee5BFqbquYHawmruKzLmXbONp_hcCwE4)
