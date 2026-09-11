# Evaluating swarm communication strategies

Research note, **10 September 2026**. The purpose is to help experiment with communication in the existing library. The focused evaluator and original diagnostic fixtures are now implemented; see [running communication experiments](COMMUNICATION_EVAL_USAGE.md). This note records the research rationale. It narrows the broader [evaluation research](BENCHMARK_RESEARCH.md) to a practical question: **which messages, delivered to which agents at which times, improve externally verified outcomes for their cost?**

## What the research says to measure

Separate three questions:

1. **Does the message carry relevant information?** Does it reveal a private observation, constraint, failed experiment, intention or request?
2. **Does the receiver use it?** Does intervening on message delivery change the receiver's decision or subsequent actions?
3. **Does that use help?** Does the intervention improve task success, reduce wasted work, or prevent an error?

[Lowe et al., *On the Pitfalls of Measuring Emergent Communication*](https://arxiv.org/abs/1903.05168) demonstrate why this distinction matters: messages can predict a sender's behavior even when they have no effect on another agent. Message/action correlation is therefore insufficient evidence of useful communication. [Jaques et al., *Social Influence as Intrinsic Motivation*](https://arxiv.org/abs/1810.08647) studies counterfactual influence on other agents' actions. Influence is useful to measure, but should be paired with external task utility; changing a teammate's behavior can also be harmful.

For language agents, [HiddenBench](https://arxiv.org/abs/2505.11556v4) motivates testing whether critical private evidence is surfaced. [SILO-BENCH](https://arxiv.org/abs/2603.01045v2) motivates separating information exchange from correct integration. Together they suggest measuring **delivery, use and outcome**, rather than grading how collaborative a conversation sounds.

## Communication choices to vary

Change one of these at a time initially. Keep the task instances, model setup, agent capabilities and noncommunication tools fixed.

| Choice | Useful comparisons | Question answered |
|---|---|---|
| Who hears whom | Full broadcast, hub, ring, sparse random graph, capability routing, overlapping groups | Does routing deliver information to the agents who need it? |
| When to speak | Every round, periodic, new evidence only, belief-change trigger, request-response | Which communications are worth sending, and how long can the system wait? |
| What to send | Answer only, supporting evidence, uncertainty, counterevidence, intentions/commitments, requests | What information prevents integration errors or duplicated work? |
| How much to send | Fixed token/byte cap, evidence-card cap, short summary, full relevant source | Where does compression remove necessary information? |
| Delivery behavior | Immediate, delayed, dropped, duplicated, out of order | Which strategies tolerate realistic channel limitations? |
| Dialogue procedure | Unstructured exchange, independent work then share, structured disclosure, critique then revise, explicit acknowledgments | Does the interaction procedure improve decisions or execution? |

[TarMAC](https://arxiv.org/abs/1810.11187) supplies a research precedent for learning whom to address and what to communicate. [IC3Net](https://arxiv.org/abs/1812.09755) supplies one for learning when to communicate. Both concern trained MARL architectures; they motivate experimental axes, not a claim that a prompt or an existing SwarmKit gate reproduces their algorithms.

## Tasks that make communication experiments informative

Use a small selection of task conditions with an exact or independently checked outcome. You do not need a large new benchmark catalog to begin.

| Condition | What the task must require | Useful source |
|---|---|---|
| Complementary private information | No individual initially has all the facts needed for the answer | HiddenBench; SILO-BENCH |
| Interdependent work | One agent's plan or result constrains another's; local success can still produce joint failure | [CooperBench](https://arxiv.org/abs/2601.13295) |
| Timing/resource coordination | Agents must avoid contention or coordinate actions and handoffs | [DPBench](https://arxiv.org/abs/2602.13255), [ALEM](https://arxiv.org/abs/2606.08340v1) |
| Redundant information | Agents already have everything necessary, so extra discussion may have little value | Deliberate negative control |

Start with distributed-information tasks because they make missing, delivered and used facts inspectable. Add an interdependent-work task to see whether findings transfer to coordination. That is a recommended research sequence, not a claim that either category alone measures all swarm competence.

Vary the **need for communication** independently of task difficulty: keep the same total facts but change their partition across agents; then separately change total task size. A strategy that excels only because one agent happened to receive all decisive evidence should not appear to be an excellent communication policy.

## Controls that distinguish competing explanations

**Same team, no explicit messages.** Keep model calls and decision opportunities matched initially. This estimates the contribution of the explicit channel under that execution policy. Record whether files, artifacts, shared memory or environment actions still communicate information; this condition is not necessarily independent work.

**Independent workers with a fixed aggregator.** Keep their states and external effects separate. Choose majority voting, a designated decision rule, or another aggregator before seeing answers. Include aggregation cost. Do not select the best answer using hidden ground truth. [Debate or Vote](https://arxiv.org/abs/2508.17536v2) motivates this control for separating exchange gains from independent sampling gains.

**Pooled information.** Supply all evidence to a single agent, or to the same team without an acquisition phase. This diagnoses how much failure remains after removing information acquisition. It changes access and is not a pure communication ablation or a guaranteed performance ceiling.

**Randomized delivery intervention.** At a defined checkpoint, suppress a message or replace its content with a declared control, then rerun the receiver and downstream trajectory. Hold the pre-intervention state fixed. Repeat across tasks and randomness. Compare both receiver behavior and task utility.

Shuffling messages is useful but imperfect: it may introduce contradictions or implausible context rather than merely remove useful information. A same-length neutral message also changes semantics. State which intervention was used and what it can establish. For trained policies, distinguish disabling communication after training from training/evaluating a no-communication policy.

## A compact measurement sheet

| Measure | Definition/use | Do not infer |
|---|---|---|
| Verified task outcome | Exact answer, passing integration checks, valid final state or completed work | Conversation quality alone is not success |
| Paired outcome difference | Mean task-utility difference between strategy and control on paired instances | A universal architecture advantage from one task distribution |
| Necessary-evidence delivery | Fraction of evaluator-known required facts reaching the designated decision maker by its decision time | Reading, understanding or correct use merely from delivery |
| Evidence-use correctness | Correct use of relevant facts, checked by task-specific reasoning/output tests or intervention | Citation alone is not proof of use |
| Delivery latency | Time/rounds from fact availability to receipt by the agent that needs it | Network speed if the measure includes model deliberation |
| Duplicate work | Repeated experiments, conflicting assignments, duplicated tool actions | Repeated messages are not always wasted; retries may be useful |
| Harmful propagation | Incorrect evidence adopted or acted on, plus recovery after correction | Agreement or popularity is not independent corroboration |
| Communication cost | Generated message tokens/bytes; delivered copies; receiver input processing; routing/summary calls | One broadcast is not one receiver-side cost |
| Total cost and time | All model/tool work, elapsed time, concurrency, and evaluator cost separately | Equal rounds or equal agent count is not equal compute |

Prefer **quality–cost curves** over a single quality-per-token ratio: a cheap strategy that usually fails can look attractive under an arbitrary ratio. Report quality at several declared budgets and the least observed cost that reaches a fixed quality target. Where uncertainty is material, avoid calling small differences a win.

Reasoning-token budgets alone may omit prompt processing, final output and communication overhead. The [equal-thinking-budget study](https://arxiv.org/abs/2604.02460v2) documents relevant measurement limitations in its specific multi-hop setting. Missing usage should remain unknown rather than becoming zero.

## Repo-specific implications from code inspection

| Existing mechanism | What can be explored | Important evaluation detail |
|---|---|---|
| [`MessageBus`](../src/swarmkit/runtime.py) and [topologies](../src/swarmkit/topology.py) | Routing, explicit-channel removal, per-recipient drops | `state.messages` stores the submitted recipient specification, not a complete receipt log. `publish()` returns actual recipients; record those or instrument delivery |
| [`ExchangeThenDecide`](../src/swarmkit/deliberation.py) | Structured fact/objection exchange under topology constraints | Set `ExchangeConfig(delivery="inbox")`. Default `all_peer` uses a common evidence board regardless of bus routing |
| [`InformationGate`](../src/swarmkit/communication.py) | New-evidence, belief-change and silence-threshold policies | Messages without belief metadata pass through. Reset gate state between independent runs; verify that it is actually filtering the intended messages |
| [`EvidenceCompressor`](../src/swarmkit/communication.py) | Selection of bounded evidence cards | `max_cards` bounds cards, not tokens or bytes. Selection may leave important task information out even when provenance is retained |
| [`GossipRelay`](../src/swarmkit/social.py) | Fanout, cards per round, lifetime and multihop propagation | It updates internal knowledge from its own planned deliveries. A downstream bus drop does not automatically undo that knowledge update. Put delivery restrictions at the appropriate mechanism boundary before interpreting the experiment |
| [`SwarmRuntime`](../src/swarmkit/runtime.py) | Per-round model callbacks and controlled message exposure | Agent contexts receive copies of all current artifacts. Shared artifacts can remain an information channel after messages are disabled |
| [`private_evidence_recovery`](../src/swarmkit/evaluation.py) | Fact-ID coverage at a selected point in time | Evaluate each intended recipient's exposure. Coverage over all sender messages can count facts never received by a decision maker |
| [`counterfactual_message_credit`](../src/swarmkit/learning.py) | Deterministic leave-one-message-out utility differences | It calls the supplied evaluator; it does not itself replay model/environment trajectories. Static rescoring is not an end-to-end causal experiment |
| [`matched_independent_control`](../src/swarmkit/evaluation.py) | Paired interacting/isolated callbacks | Declared budgets are passed to callbacks, not enforced inside opaque model calls. Initial inboxes also remain part of each isolated input |

These remain constraints on using the original algorithms. The new communication evaluator uses private contexts and explicit receipt tracking, without changing those algorithms. Before experimenting, draw the actual information paths—messages, internal boards, artifacts, memory and tool effects—and identify which path each ablation changes.

## A manageable first study

The following is a proposed pilot, not a literature-prescribed sample size:

1. Choose one distributed-information task family with known decisive evidence. Freeze a development split for tuning and a separate evaluation split.
2. Compare four strategies: no explicit messages, all-to-all evidence exchange, structured request/disclosure, and gated or targeted exchange. Keep the model, evidence partition, decision slots and tools fixed.
3. Evaluate at two communication allowances. Measure total computation as well as the allowance; an unused message budget need not reduce actual model generation.
4. Use approximately 30 paired evaluation instances for an initial diagnostic and repeat stochastic conditions when affordable. Report paired intervals; increase the sample when uncertainty prevents a conclusion. These numbers are a starting budget choice, not a power guarantee.
5. For promising strategies, vary topology, add delays/loss and hold out partners or larger task structures. Then test an interdependent-work task before generalizing.

There are two different cost experiments. **Fixed decision computation** helps isolate information effects. **Reallocating saved communication cost to useful work** tests whole-system efficiency. Report both separately. Filtering an already-generated message saves neither its generation tokens nor its generation latency; an earlier send/no-send decision can.

The most useful output for experimentation is a table of outcomes and costs for each strategy, with diagnostic plots of evidence arrival, duplicate work and receiver behavior. Keep independent runs as the statistical unit; messages within a conversation are not independent samples. Treat natural-language transcripts as explanations to inspect after measuring the task, not as the primary score.

## Reading order

Start with [Pitfalls](https://arxiv.org/abs/1903.05168) for measurement mistakes, [HiddenBench](https://arxiv.org/abs/2505.11556v4) and [SILO-BENCH](https://arxiv.org/abs/2603.01045v2) for information-exchange evaluations, and [Debate or Vote](https://arxiv.org/abs/2508.17536v2) for controls. Read [TarMAC](https://arxiv.org/abs/1810.11187), [IC3Net](https://arxiv.org/abs/1812.09755) and [Social Influence](https://arxiv.org/abs/1810.08647) when exploring targeted communication, gating and intervention metrics. The [new paper snapshots](../sources/communication-evaluation/README.md) and [existing benchmark archive](../sources/benchmarks/README.md) preserve source material. None of these studies establishes a universally best communication strategy for this repo.
