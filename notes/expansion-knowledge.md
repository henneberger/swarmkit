# Expansion: cumulative knowledge in interacting populations

Primary-source scan checked 2026-09-09 against `sources/catalog.json`. Three new candidates below. Full-text methods/results inspected online; source code candidates checked by public APIs without cloning or running them. Existing copying/whistleblowing papers and another reviewer's social-convention source omitted. Scope labels matter: the third is a non-LLM cultural-learning precursor, not a deployed agentic swarm.

## 2606.30668v1 — Emergent Culture in Minimal LLM Systems

Simon Jones and Sabine Hauert; 21 June 2026; arXiv lists acceptance at ALife 2026. [Full text](https://arxiv.org/html/2606.30668v1), [code/data](https://bitbucket.org/hauertlab/swarm_llm).

Three stateless agents receive messaging tools and a decaying shared key-value store. They preserve information by reading, reconstructing and rewriting it. The store therefore becomes collectively maintained memory rather than a passive transcript. Ten runs exhibit different storage strategies: monolithic accumulation, per-cycle rewritten records, or descriptive keys serving as memory. Recurrence Quantification Analysis and persistent-vocabulary measurements find structure lasting beyond the roughly 16-cycle corruption/deletion horizon.

The paper explicitly does **not** isolate decay causally: no zero-decay sweep. It also lacks an equal-budget independent-agent comparison and task-correctness benchmark. Semantic persistence and organized creativity are the demonstrated outcomes, not verified discoveries. Prompt wording matters: an invitation to explore/play is needed to sustain activity. This is particularly relevant to higher-level abstractions because agents reconstruct shared meanings despite local memory loss, but no claim of scientific truth follows.

Verified public Bitbucket tree at commit `e8bb0f3834affa35504b0cb2b4b6bab0a9c422d1`; includes `swarm/`, `core/`, prompts and experiment data. `core/tools.py:163` builds the swarm tool registry; this is a real implementation candidate outside GitHub.

## 2510.14401v2 — The Role of Social Learning and Collective Norm Formation in Fostering Cooperation in LLM Multi-Agent Systems

Prateek Gupta et al.; first 16 October 2025, reviewed revision 27 January 2026. [Full text](https://arxiv.org/html/2510.14401v2).

A common-pool-resource society combines harvesting, costly monitoring/punishment, learning from successful peers, and proposed collective rules. The important implementation distinction in §3.1.3: rule-based agents use logistic payoff-biased strategy copying, whereas **LLM agents adapt in context from textual peer outcomes**. They do not numerically copy strategy vectors. Collective rule selection uses two short calls per agent: propose a natural-language norm, then vote; the winner is broadcast verbatim.

Section 4.2.5 separates full system, social-learning-only, voting-only and neither, with ten trials per condition. Removing both yields poor survival; voting alone can outperform the full system under selfish priors. Imitating successful peers can favor short-term overharvesters. Thus diffusion of locally successful knowledge needs shared constraints that account for collective consequences. Outcomes concern survival/cooperation in a designed simulator, not discovering external scientific knowledge or permanent weight changes.

No source repository link found in full text or targeted primary-source search. Recommend paper collection with code marked unverified/unavailable, rather than inventing a repository match.

## 2406.00392v2 — Artificial Generational Intelligence: Cultural Accumulation in Reinforcement Learning

Jonathan Cook et al.; first 1 June 2024, reviewed revision 28 October 2024. [Full text](https://arxiv.org/html/2406.00392v2), [repository](https://github.com/FLAIROx/cultural-accumulation).

This is an explicitly **non-LLM precursor**: learned social observation and independent exploration accumulate capabilities across successive generations. The paper distinguishes episodic generations, carrying knowledge through context, from training-time generations, carrying skills through trained policies. Algorithm 1 decreases demonstrator observation across trials, forcing newcomers to move from social information toward independent behavior. Accumulating agents outperform single-lifetime agents given the same cumulative experience in the studied environments. That control makes this stronger evidence of useful cultural accumulation than counting shared messages.

It does not establish the same result for free-form language swarms or open science. If strict current-agentic scope excludes precursors, put this in a brief methods lineage rather than treating it as an agent framework.

Verified repo commit `6b0df15bf46d4453d1974dde7af04102a77819b2`. `goal_seq/in_context_accumulation.py:119` evaluates learner/demonstrator trajectories; `:226` loops generations and `:234` passes demonstration actions onward. `goal_seq/in_weights_accumulation.py:128` builds training and `:262` performs update epochs. Code requires preexisting checkpoints/configuration; static inspection is not reproduction.

## Recommended addition to synthesis

Separate preserving shared meaning, adopting a group rule and accumulating useful skills. They use related social substrates but require different tests. These sources suggest testing retention after memory turnover, removing copying/voting channels independently, and matching total experience—not assuming that persistence, agreement or imitation is itself knowledge discovery.
