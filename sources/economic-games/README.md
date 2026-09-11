# Economic games research archive

Collected 10 September 2026 for [the SwarmKit economic-games research and implementation guide](../../docs/ECONOMIC_GAMES_RESEARCH.md).

**Downloaded: 25 PDFs (24 with searchable extracted text), 5 blog posts, and 14 shallow Git repository checkouts.** One additional requested PDF (Shapley/RAND) was blocked with HTTP 403. Myerson's working-paper PDF downloaded, but its publisher landing page returned 403 and the PDF is scanned.

The archive occupies approximately 1.5 GB including full shallow checkouts. No upstream code was executed or installed. Paper findings and benchmark scores were not reproduced.

- [Collection plan](collection-plan.json): selected sources and their purposes.
- [Manifest](manifest.json): retrieval times, source URLs, hashes, repository commits, text availability and failures.
- [Candidate methods](method-candidates.json): 26 implemented components with fidelity, API names, applications, assumptions, strategies and metrics. See the [usage guide](../../docs/ECONOMICS_USAGE.md).
- [Repository audit](repository-audit.md): inspected paths and integration judgments.
- [BibTeX](references.bib): source metadata, including explicit retrieval status.

PDFs and HTML retain their original rights; this collection is not covered by SwarmKit's MIT license. Local checkouts retain upstream licensing. Source material is excluded from package distributions by the existing `MANIFEST.in`.

Repository `checkout/` folders are intentionally Git-ignored; commit records and root README/license snapshots remain trackable. To recreate a missing checkout, the collector fetches the recorded commit. Re-running preserves completed source snapshots; it does not update to newer repository HEADs. Exact source availability still depends on upstream hosting.

From the repository root:

```sh
python3 scripts/collect_economic_games.py
python3 scripts/collect_economic_games.py --verify
```

`pdftotext` must be installed for PDF extraction. Collection needs public network access. Verification is local and checks SHA-256 hashes and recorded Git commits. For a new literature update, use a separate dated collection rather than silently replacing these snapshots.

## Papers and lecture notes

| Source | Local PDF | Searchable text | Retrieval |
|---|---|---|---|
| [Evolutionary dynamics of higher-order interactions in social networks](https://arxiv.org/abs/2001.10313) | [PDF](papers/2001.10313/paper.pdf) | [Text](papers/2001.10313/paper.txt) | ok |
| [Cooperation in Public Goods Games: Leveraging Other-Regarding Reinforcement Learning on Hypergraphs](https://arxiv.org/abs/2410.10921) | [PDF](papers/2410.10921/paper.pdf) | [Text](papers/2410.10921/paper.txt) | ok |
| [OpenSpiel: A Framework for Reinforcement Learning in Games](https://arxiv.org/abs/1908.09453) | [PDF](papers/1908.09453/paper.pdf) | [Text](papers/1908.09453/paper.txt) | ok |
| [A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning](https://arxiv.org/abs/1711.00832) | [PDF](papers/1711.00832/paper.pdf) | [Text](papers/1711.00832/paper.txt) | ok |
| [Alpha-Rank: Multi-Agent Evaluation by Evolution](https://arxiv.org/abs/1903.01373) | [PDF](papers/1903.01373/paper.pdf) | [Text](papers/1903.01373/paper.txt) | ok |
| [Learning with Opponent-Learning Awareness](https://arxiv.org/abs/1709.04326) | [PDF](papers/1709.04326/paper.pdf) | [Text](papers/1709.04326/paper.txt) | ok |
| [Proximal Learning With Opponent-Learning Awareness](https://arxiv.org/abs/2210.10125) | [PDF](papers/2210.10125/paper.pdf) | [Text](papers/2210.10125/paper.txt) | ok |
| [Mean Field Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1802.05438) | [PDF](papers/1802.05438/paper.pdf) | [Text](papers/1802.05438/paper.txt) | ok |
| [Multi Type Mean Field Reinforcement Learning](https://arxiv.org/abs/2002.02513) | [PDF](papers/2002.02513/paper.pdf) | [Text](papers/2002.02513/paper.txt) | ok |
| [Optimal Auctions through Deep Learning: Advances in Differentiable Economics](https://arxiv.org/abs/1706.03459) | [PDF](papers/1706.03459/paper.pdf) | [Text](papers/1706.03459/paper.txt) | ok |
| [The AI Economist: Optimal Economic Policy Design via Two-level Deep Reinforcement Learning](https://arxiv.org/abs/2108.02755) | [PDF](papers/2108.02755/paper.pdf) | [Text](papers/2108.02755/paper.txt) | ok |
| [Put Your Money Where Your Mouth Is: Evaluating Strategic Planning and Execution of LLM Agents in an Auction Arena](https://arxiv.org/abs/2310.05746) | [PDF](papers/2310.05746/paper.pdf) | [Text](papers/2310.05746/paper.txt) | ok |
| [Competitive Market Behavior of LLMs](https://arxiv.org/abs/2609.02580) | [PDF](papers/2609.02580/paper.pdf) | [Text](papers/2609.02580/paper.txt) | ok |
| [Information Design With Large Language Models](https://arxiv.org/abs/2509.25565) | [PDF](papers/2509.25565/paper.pdf) | [Text](papers/2509.25565/paper.txt) | ok |
| [Deal or No Deal? End-to-End Learning for Negotiation Dialogues](https://arxiv.org/abs/1706.05125) | [PDF](papers/1706.05125/paper.pdf) | [Text](papers/1706.05125/paper.txt) | ok |
| [Efficacy of Language Model Self-Play in Non-Zero-Sum Games](https://arxiv.org/abs/2406.18872) | [PDF](papers/2406.18872/paper.pdf) | [Text](papers/2406.18872/paper.txt) | ok |
| [GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents](https://arxiv.org/abs/2406.06613) | [PDF](papers/2406.06613/paper.pdf) | [Text](papers/2406.06613/paper.txt) | ok |
| [The Price of Anarchy in Auctions](https://arxiv.org/abs/1607.07684) | [PDF](papers/1607.07684/paper.pdf) | [Text](papers/1607.07684/paper.txt) | ok |
| [The Contract Net Protocol](https://reidgsmith.com/The_Contract_Net_Protocol_Dec-1980.pdf) | [PDF](papers/smith-1980-contract-net/paper.pdf) | [Text](papers/smith-1980-contract-net/paper.txt) | ok |
| [College Admissions and the Stability of Marriage](https://www.math.utoronto.ca/mccann/assignments/477/GaleShapley62.pdf) | [PDF](papers/gale-shapley-1962/paper.pdf) | [Text](papers/gale-shapley-1962/paper.txt) | ok |
| [The Bargaining Problem](https://www.haverford.edu/sites/default/files/Nash1950.pdf) | [PDF](papers/nash-1950-bargaining/paper.pdf) | [Text](papers/nash-1950-bargaining/paper.txt) | ok |
| [A Simple Adaptive Procedure Leading to Correlated Equilibrium](https://ma.huji.ac.il/~hart/abs/adapt.html) | [PDF](papers/hart-mas-colell-2000/paper.pdf) | [Text](papers/hart-mas-colell-2000/paper.txt) | ok |
| [Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation](https://hanson.gmu.edu/mktscore.pdf) | [PDF](papers/hanson-market-scoring/paper.pdf) | [Text](papers/hanson-market-scoring/paper.txt) | ok |
| [CS364A Algorithmic Game Theory lecture notes](https://theory.stanford.edu/~tim/f13/f13.html) | [PDF](papers/roughgarden-2013-agt/paper.pdf) | [Text](papers/roughgarden-2013-agt/paper.txt) | ok |
| [Graphs and Cooperation in Games (working paper)](https://pubsonline.informs.org/doi/10.1287/moor.2.3.225) | [PDF](papers/myerson-1977-graphs/paper.pdf) | No | partial |
| [A Value for n-Person Games (1952 RAND precursor to 1953 chapter)](https://www.rand.org/pubs/papers/P295.html) | Unavailable | No | failed |

## Blog posts

| Source | Local snapshot |
|---|---|
| [Understanding Agent Cooperation](https://deepmind.google/blog/understanding-agent-cooperation/) | [HTML](posts/deepmind-cooperation/page.html) · [Text](posts/deepmind-cooperation/page.txt) |
| [Melting Pot: an evaluation suite for multi-agent reinforcement learning](https://deepmind.google/blog/melting-pot-an-evaluation-suite-for-multi-agent-reinforcement-learning/) | [HTML](posts/deepmind-melting-pot/page.html) · [Text](posts/deepmind-melting-pot/page.txt) |
| [Emergent Bartering Behaviour in Multi-Agent Reinforcement Learning](https://deepmind.google/blog/emergent-bartering-behaviour-in-multi-agent-reinforcement-learning/) | [HTML](posts/deepmind-barter/page.html) · [Text](posts/deepmind-barter/page.txt) |
| [The AI Economist: Improving Equality and Productivity with AI-Driven Tax Policies](https://www.salesforce.com/blog/the-ai-economist/) | [HTML](posts/salesforce-ai-economist/page.html) · [Text](posts/salesforce-ai-economist/page.txt) |
| [The AI Economist: Join the Moonshot](https://www.salesforce.com/blog/the-ai-economist-moonshot/) | [HTML](posts/salesforce-ai-economist-release/page.html) · [Text](posts/salesforce-ai-economist-release/page.txt) |
