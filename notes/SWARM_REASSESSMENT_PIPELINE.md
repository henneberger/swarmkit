# Reassessing the swarm pipeline

The existing pipeline is a chronological sample-review system with peer messages. It has not established a useful discovery swarm. Its source controls are valuable, but operational correctness was repeatedly treated as progress toward an objective the architecture barely represented. The user wants interesting developments to emerge through investigation as events unfold. We substituted the easier deliverable of well-formed, cautiously worded “tacit rules.” That substitution explains much of the trivial output.

This is an independent design critique, not a defense of the implementation. The recommendations below are proposed changes, not implemented capabilities or validated research results. No further paid calls are warranted merely to rerun the same architecture.

## 1. Where the causal chain breaks

In [stream.py](../src/swarmkit/enron/stream.py), `_arrive` samples a reservoir of novel bodies, limits repeated subjects, and selects a fixed number of documents. `_act` divides them among four fixed perspectives. Everybody receives an observe turn and usually one revise turn; the latter permits a tightly capped historical query. `_publish` appends hypotheses. `run` advances the corpus in fixed arrival-count batches regardless of which question remains unresolved.

There is genuine communication: one peer can read another’s evidence and change a query. That is a possible source of benefit, not evidence that the whole design supports collective discovery. The decisive choices remain outside the agents: which matter deserves attention, who should investigate it, how much context to obtain, whether to recruit another participant, and when enough has been learned. “Routines,” “expectations,” “expertise,” and “contrasts” are prompt perspectives, not evolving capabilities grounded in different investigative histories.

Random sampling removes retrospective case cherry-picking, but also destroys much of the structure needed to notice developments. Eight unrelated messages per investigator are a weak basis for connecting an objection, a changed commitment, a decision, and a later consequence. Subject diversity can actively exclude the repeated conversation needed to understand an episode. Byte novelty identifies different text, not a changed situation. Forward deduplication is useful, but circulation to a new audience can itself be meaningful and must remain visible.

The clock then advances even when the important next action is to finish reading a document. A global one-query allowance competes with continuation reads, thread reconstruction, counterexample searches, and peer-requested follow-up. Having a `read:` tool does not solve this allocation problem.

Finally, the output schema asks for a conditional practice. Models turn explicit instructions into general routines, add conventional uncertainty, and repeat the result. More stringent fields produced cleaner labels; they did not create investigative opportunities. Rejections and exact-quote audits address reliability at the boundary, not discovery quality. Stable citations can still support the wrong actor, proposition, or scope.

## 2. What the swarm research actually contributes

The relevant lesson is not “add more agents.” It is to make interaction change the search process.

- [AgentNet](https://arxiv.org/abs/2504.00587) makes execution, decomposition, and forwarding part of agent action. Our peers cannot commission a focused investigation or transfer an unresolved question to someone with relevant experience.
- [SwarmSys](https://arxiv.org/abs/2510.10047) emphasizes evolving task/agent profiles and validated contribution traces. Our forum records outputs but scarcely affects future task allocation. The numeric pheromone implementation in this library is an adaptation, not a reproduction of SwarmSys.
- [HiddenBench](https://arxiv.org/abs/2505.11556) shows why relevant private information must be elicited before commitment. It does not imply that broadcasting arbitrary samples manufactures complementary evidence. We need questions that identify which missing fact a peer could supply.
- [SwarmWorld](https://arxiv.org/abs/2608.26081) tests whether inherited artifacts remain useful after their creators disappear. A persistent wiki is not that test. An investigation procedure needs to help a different agent answer a new question, with controlled evidence and cost.
- [GPTSwarm](https://arxiv.org/abs/2402.16823) makes communication structure optimizable against an objective. We lack a credible discovery reward; optimizing message edges now would optimize a poorly specified target.

These papers motivate mechanisms, not an established end-to-end solution for discovering developments in email. Their strongest transferable proposition is testable: a peer’s contribution should enable an action or inference that the recipient would otherwise miss.

## 3. Replace the unit of work with an inquiry episode

The primary object should be a live question about a developing situation, not a rule card.

An **inquiry** contains: what appears to have changed; the participating actors and bounded episode; attributable event assertions; competing explanations; missing premises; explicit next actions; the observations that would discriminate among explanations; current ownership; and pause/closure conditions. A tacit practice may eventually explain an episode, but is one possible result among several.

A useful development might be a commitment changing despite an unresolved dependency, an apparent disagreement later resolved by different definitions, a responsibility moving to someone unexpected, or a warning reaching a new audience. None requires scandal. A well-supported benign resolution is more informative than a dramatic speculative theory.

For example, hypothetically: one scout encounters an unresolved operational dependency; another later finds a confident delivery commitment. A focused inquiry asks whether the dependency was resolved, waived, or misunderstood. A third agent locates an earlier delegation; a fourth checks whether that delegation covers this situation. The eventual account explains what changed and which explanation survived. This is interesting because dispersed evidence changes understanding, not because the agents label it unusual.

Keep three distinct products: source-grounded episode timelines, contested working theories, and tested reusable procedures. Do not require each observation to become “tacit knowledge.”

## 4. An agent-driven inquiry architecture

**Arrival sensing.** Preserve the arrived-only corpus and exact sequence boundary. Cheap deterministic processing identifies thread continuations, new participants, explicit replies, recurring references, and messages relevant to existing watch conditions. Neutral reservoir sampling remains an exploration channel, not the entire attention policy. A newly matching message wakes an inquiry; ordinary unselected arrivals remain searchable, without being pronounced irrelevant.

**Open an inquiry.** A scout can submit a question with two related traces, or one trace plus a concrete missing premise. The scout states why resolving it matters and what result would make the question uninteresting. No self-rated “novelty score” automatically purchases more computation.

**Choose actions.** Agents request bounded actions: reopen context, follow a thread, compare another episode, resolve an identity/date/unit ambiguity, ask a peer, formulate a rival, or suspend the question. Each request names its expected information and a stopping condition. The controller enforces access and budget; it does not prescribe the substantive answer or insist everyone speak.

**Recruit complementary peers.** A requesting agent describes what it needs: prior familiarity with a thread, ability to reconcile quantities, or a search for a benign interpretation. A router selects an available peer using capabilities and demonstrated task outcomes. The recipient receives the question and essential provenance, conducts independent work, then returns evidence and what it changes. Four workers are enough initially; fluid assignment matters more than population size.

**Contest before synthesizing.** An inquiry with a promising explanation receives an independent rival search. The challenger must identify an actual competing mechanism or a specific unsupported link, not generate ceremonial disagreement. A synthesis states which assertions are supported, which inference connects them, and what would reverse the interpretation. Failure to find evidence remains a scoped search result.

**Persist and reactivate.** Store unanswered questions, failed searches, disputed links, and accepted context packs as well as conclusions. Later arrivals can reopen a suspended question. Agents should discover useful work through these persistent traces; a forum is serving coordination only when a trace changes somebody’s next action.

**Allocate resources adaptively.** Start with small action budgets and extend an inquiry when a source resolves a missing premise, introduces a consequential contradiction, or supplies a feasible discriminating test. Reserve an explicit exploration share; cap concentration on any one inquiry. Self-reported certainty, message volume, and agreement are not rewards. Initially use transparent priorities and human-reviewed outcomes rather than pretending to have calibrated information gain.

**Preserve unfolding.** Keep arrival time, investigation time, and publication time separate. Agents may investigate only through the current arrival watermark. Spend a bounded investigation allowance between advances; when exhausted, carry the question forward rather than filling a schema. A published update should answer: what became known now, what earlier view changed, and what remains open? Forecasts stay immutable and can only be evaluated against later arrivals.

## 5. What existing library code can and cannot supply

| Component | Useful mechanism and required application work |
|---|---|
| `SwarmRuntime`, `CallableAgent`, `MessageBus` | Snapshot execution and addressed messages already work. Use selected participants for inquiry actions. The runtime does not discover tasks or sandbox callbacks. All runtime artifacts are public; private investigations must remain in local memory or explicitly filtered application views. |
| `CapabilitySuccessRouter.route/record` | Implements capability overlap, exploration, and success feedback. Use it for explicit peer requests. It lacks workload-aware allocation and meaningful success labels; those must be supplied. Avoid using one global required-capability field for concurrent unrelated questions. |
| `DAGExecutor` | Executes an already-declared dependency frontier. Suitable for “retrieve both contexts, then compare.” It does not invent or dynamically expand an investigation; an application agenda must submit subsequent frontiers. |
| `EvidenceRegistry` | Preserves ancestry and collapses supplied source roots. It cannot authenticate attribution, determine semantic entailment, or recognize every shared rumor. Segment dependence metadata remains necessary. |
| `ArtifactStore`, `PeerAdoption` | Support explicit admission, local testing, and rollback. Define separate checks for citation integrity and procedure utility. Runtime verification alone does not reject publication. Never equate an artifact’s `verified` flag with a true explanatory theory. |
| `StigmergicPolicy` | Can prioritize locally useful, verified artifacts through decaying contribution traces. It does not currently manage provisional inquiry queues. Use it first for tested context/retrieval procedures; build a separate board for unresolved theories. |
| `FeedPolicy`, `InformationGate`, `EvidenceCompressor` | Offer selective exposure and bounded communication. Popularity is unsuitable as evidence strength; disable or replace social-proof rewards. Belief-change gating requires stable alternatives, and card limits do not enforce token budgets. |

`ExchangeThenDecide` is useful for a bounded question with explicit alternatives, not as the whole discovery engine. Its default `all_peer` board bypasses bus visibility; use inbox mode if visibility matters. `HypergraphTopology` can represent temporary inquiry teams, but does not form them. Neither learning a DAG nor adding latent channels addresses missing inquiry agency. `ProcedureAbstraction` belongs later, after genuine episodes and protected comparison cases exist.

The minimal core is therefore: an arrived-only source service, an inquiry agenda, action-capable agents, addressed evidence exchange, independent challenge, and an append-only inquiry history. Most of the missing work is in the agenda and its connection to agents, not in importing additional algorithms.

## 6. Delete or demote these design choices

Remove fixed eight-call spending per window, compulsory rule production, and the assumption that each peer must review every batch. Replace arbitrary “last twelve hypotheses” sharing with inquiry-specific subscriptions and explicit requests. Stop using byte novelty as a proxy for substantive priority. Keep source deduplication, but show forwarding occurrences when relevant.

Demote the current random-mail, four-perspective pipeline to a baseline. Retain chronological access controls, parsed attribution, stable source spans, continuation reads, sanitized diagnostics, and the central budget ledger as infrastructure. Operational fixes should remain fixed; they should not keep substituting for a new discovery design.

Do not add naming games, generalized reputation, every topology, reinforcement learning, or more model personas to the minimum system. A learned allocator needs evidence of useful actions first. An attractive activity feed cannot establish collective intelligence.

## 7. Test the causal mechanism before another full-corpus run

Construct a small chronological evaluation set with several related threads per episode, misleading forwards, mundane resolutions, and dispersed clues. Freeze later outcomes. Reviewer-selected interesting episodes introduce selection bias, so include neutral episodes and report performance on both.

Compare: one capable investigator with the entire budget; independent investigators with a fixed final merger; shared source cards without negotiation; the adaptive inquiry swarm; and the existing fixed-review pipeline. Match retrieval, model, synthesis, and review costs. Separately compare equal-information conditions, since communication can help simply by exposing more evidence.

Measure supported developments discovered, useful corrections, time to connect complementary clues, unresolved questions that later reopen productively, and reviewer effort per useful update. Blind reviewers to treatment. Do not score “interesting” using agent self-praise or a count of produced theories.

For each claimed swarm success, show the causal trace: peer A’s specific evidence caused B’s new action; C challenged a premise; the resulting explanation differed from the independent control. Replay with the crucial message removed. `counterfactual_message_credit` can assist controlled evaluations, but its deterministic leave-one-message-out score is not a general causal estimator for stochastic agents.

Proceed only if this small test demonstrates useful interaction. A strong single investigator outperforming the swarm is a result to accept. The next milestone is one convincing, source-grounded unfolding inquiry whose outcome depends on collaboration—not another large run that produces many cautious cards.
