# Implemented social mechanisms and evaluation

Owned files: `src/swarmkit/social.py`, `src/swarmkit/evaluation.py`, `tests/test_social.py`, `tests/test_evaluation.py`. Fresh implementations; no upstream source was copied. These use canonical `AgentState`, `SwarmState`, `Task`, `Evidence`, `Message`, `Decision`, and `AlgorithmResult` contracts.

## Public API

- `NamingGame(memory_size=5, committed={}, choose=None).step(state, task)`: samples one active pair, asks each policy for a label before updating either member, rewards agreement, and records bounded local history. Committed agents always select their configured label. Without a callback, the policy copies a uniformly sampled remembered partner label or initially samples uniformly. This is an honest classical baseline, **not an LLM reproduction** of [Ashery et al.](https://arxiv.org/abs/2410.08948v2). A `choose(agent, task, rng)` callback can supply another policy.
- `ProportionalCopying(innovation=.07, visible=None).step`: samples visible labels proportional to occurrence, with uniform innovation. Default visibility is the inbox; custom `visible(state, agent_id)` can model a page/feed. Adapted null model from [copying study](https://arxiv.org/abs/2609.09150v1), without claiming its fitted parameters universally apply.
- `FeedPolicy(...).rank(messages, now, limit=None, reputation=None)`: deterministic position/recency/log-endorsement/reputation scoring, followed by greedy topic diversification. **Original configurable design**, not a verified Moltbook algorithm.
- `TrustNetwork.observe(observer, subject, topic, success, weight=1)` tracks directional Beta reliability. `.trust(..., max_hops=2, decay=.9)` takes the strongest simple-path product; cycles cannot amplify it, and parallel endorsements are not summed. `.admit(observer, evidence, topic, verify, threshold=.5)` combines contextual trust, evidence confidence and an explicit external verifier. This is an original design, not a claimed platform formula.
- `GossipRelay(neighbors, fanout=None, cards_per_round=1, ttl=None).step`: synchronous deterministic-card transmission with optional random bounded fanout. A snapshot prevents same-step cascades. Repeated cards count only once per recipient. Evidence lifetime starts at first appearance and copying does not renew it. Unknown/inactive recipients are excluded. An optional admission callback gates receipt. Adapted from the [distributed-evidence relay benchmark](https://github.com/Darwin-Agent/topological-collapse-agent-societies/tree/main/llm_relay_benchmark), not model-authored reasoning transfer.

All social algorithms use `state.rng`, including message IDs. Callers advance `state.step` and record/route returned messages. Relay also maintains its own knowledge inventory under its namespace in `state.data`; results expose that inventory in `metadata['knowledge']`. Do not invoke two unrelated relay configurations with the same namespace unless shared inventory is intended.

Evaluation functions:

- `population_diversity(labels, normalized=True)`: Shannon entropy, optionally normalized by observed category richness.
- `interaction_reciprocity(messages, population=())`: reverse-present fraction of unique directed edges; broadcasts require explicit population to expand.
- `private_evidence_recovery(required, observed)`: coverage of unique required IDs, independent of message duplication.
- `ancestry_adjusted_agreement(decisions, evidence, answer=None)`: each independent root-source contributes unit mass, split over citing decisions. Ungrounded votes add no mass. Unknown ancestry and cycles raise errors. This defined diagnostic does not infer actual statistical independence.
- `hyperedge_irreducibility(hyperedges)`: exact Eq. 3 from [2608.15519v1](https://arxiv.org/abs/2608.15519v1), including global hyperdegree and averaging only events of size at least three. Returns `None` without qualifying events. It is not an intelligence metric.
- `transfer_gain(cases, before, after)`: paired average held-out utility difference using isolated copies.
- `matched_independent_control(state, task, total_budget, swarm_runner, independent_runner, score)`: same initial state/evidence, aggregate budget split over isolated runners, paired scorer, returning `MatchedComparison`. Independent callbacks receive only one agent and their own RNG. Opaque callback usage cannot be metered by this helper; callers must enforce the agreed budget and identical tools/data access.

Tests cover determinism, committed labels, memory limits, frequency copying, diversity ranking, trust direction/context/cycles, disconnected relay, synchronous propagation, expiry, admission, duplicate coverage, conflicting IDs, ancestry cycles, exact hyperedge arithmetic, paired transfer, and isolated matched budgets. No external services, expensive inference or downloaded code execution is required.
