# Run communication experiments

Use `swarmkit.benchmarks` to vary communication while keeping task instances, private information and decision opportunities fixed. It runs the library's canonical `Agent.act(AgentContext) -> AgentOutput` interface, with optional async callbacks. Two original, exactly graded diagnostic generators are included: selecting an option from distributed cost evidence and jointly scheduling agents under private availability constraints. They are starting fixtures, not reproductions of HiddenBench, SILO-BENCH or CooperBench.

## Run the offline pilot

```sh
python -m swarmkit.benchmarks --cases 30 --agents 4 --rounds 3 --budgets 4 16 --output evidence-results.json
python -m swarmkit.benchmarks --task schedule --cases 30 --output schedule-results.json
```

Each command compares no messages, broadcast, request/disclosure, targeted exchange and novelty-gated exchange. Reports contain individual outcomes, delivered/dropped/late messages, byte counts, known usage, quality/cost summaries, and paired bootstrap intervals. Pairing uses task ID and run seed; repeated seeds of the same task are averaged before resampling independent tasks. Thirty cases are a diagnostic budget choice, not a power guarantee. A degenerate interval from a constant small sample does not establish general equivalence.

The reference agents are deterministic Python policies. They use zero model tokens; this is explicitly reported by the CLI. They demonstrate mechanism behavior, not language-model capability. The request policy spends messages asking for facts: at a tight four-message allowance, requests can exhaust the allowance before any evidence is sent. This is a useful check that the evaluation measures timing and bandwidth constraints.

`distributed_evidence(seed, agents, options, redundant, split)` changes group size, action count or information redundancy. `interdependent_schedule(seed, agents, slack, split)` changes group size and slack. Split labels seed separate random streams; use `split="dev"` for tuning and `split="test"` for evaluation. Public agent contexts omit generation seeds and evaluator answers. The reference schedule planner caps exhaustive search at one million assignments; replace it when testing larger teams.

## Plug in communication and agents

```python
import asyncio
from swarmkit.benchmarks import (
    ChannelConfig, CommunicationEvaluator, EvidenceAgent, distributed_evidence,
)
from swarmkit.topology import RingTopology

async def experiment():
    case = distributed_evidence(seed=7, agents=6)
    population = {name: EvidenceAgent("gated") for name in case.private}
    evaluator = CommunicationEvaluator(
        rounds=5,
        topology=RingTopology(),
        channel=ChannelConfig(max_messages=24, max_bytes=50_000, delay=0, loss=0.1),
    )
    run = await evaluator.run(case, population, seed=19)
    print(run.metrics)
    return run

asyncio.run(experiment())
```

Replace the `EvidenceAgent` objects with your own agents. Contexts expose only the recipient's private evidence, memory, delivered messages and the public task. All contexts are copied before any output is incorporated. Return changes through `AgentOutput.memory_updates`; mutate neither global state nor another agent's context. Artifacts are rejected to avoid creating a second shared channel. Model calls are dispatched sequentially within synchronous rounds, so measured elapsed time is harness wall time, not a parallel-runtime latency prediction.

`topology` accepts an existing topology policy. Prefer static/pure topology callbacks: neighbor discovery receives a state copy, so changes to its state argument do not persist. `gate` accepts message filters such as `InformationGate`; `transform` can compress or select evidence before delivery. Belief-based gates require the corresponding metadata. Gate/transform objects are deep-copied per experiment; function closures over external mutable objects are caller-owned and must be reset. Novelty gating in the reference agent happens before message generation; downstream filtering cannot save generation tokens.

Channel semantics:

- A message generated in round `t` arrives before calls in round `t + 1 + delay`.
- `max_messages` and `max_bytes` cap admitted sender messages for the whole episode, including messages subsequently lost. A broadcast is charged once against admission; delivered copies are counted separately.
- Bytes include serialized content, evidence and metadata. They are not model tokens. Receiver input bytes count each repeated exposure through the complete inbox.
- Loss, duplication and reordering use keyed randomness per message/recipient. Removing one message does not shift the channel randomness for all others.
- A copied delivery does not imply a new independent fact. Delivery logs include IDs and timing; evidence coverage is ID exposure at the recipient's last decision, not a claim that the evidence is true or correctly used.
- Agent/model/tool work is outside channel budgets. `calls` counts harness agent invocations. Tokens and monetary cost remain `None` unless `trust_reported_usage=True`; then the agent must provide complete measured `Usage`, including its internal tool/model activity as applicable.

Provider wrappers own their actual usage accounting, stochastic state, concurrency and external effects. The evaluator does not infer hidden reasoning tokens or sandbox code. The evaluator's own grading time is separate in `evaluator_seconds`; charge paid grading calls in an application-level meter if you add them.

## Matched controls

Use `ChannelConfig(disabled=True)` with the **same agents** to ablate explicit communication while retaining decision slots. Compare with `EvidenceAgent("none")` or independent model agents to study a different no-communication policy. For independent sampling with fixed majority aggregation, use `aggregation="vote"` and a disabled channel; ties are lexicographic and no oracle selects the best answer. `aggregation="designated"` grades the configured `decision_maker` (default first agent). Use `aggregation="joint"` when all participants' final actions matter, as in scheduling.

Use `run(..., pooled=True)` to give every participant the union of private facts. This diagnoses information acquisition separately; it changes information access and is not a pure message ablation. Redundant-evidence tasks are another useful control.

`paired_summary(treatment_runs, control_runs)` rejects unmatched or duplicated task/seed pairs. `quality_cost_summary(runs)` reports one condition's mean outcome and observed costs. Compare those summaries across several allowances instead of optimizing a quality/token ratio.

## Remove a message and replay

```python
import asyncio
from swarmkit.benchmarks import CommunicationEvaluator, EvidenceAgent, distributed_evidence

async def intervention():
    case = distributed_evidence(seed=5)
    agents = {a: EvidenceAgent("broadcast") for a in case.private}
    evaluator = CommunicationEvaluator(rounds=2)
    baseline = await evaluator.run(case, agents, seed=11)
    effect = await evaluator.replay_without(case, agents, baseline, "0:a1:0")
    print(effect["decision_changed"], effect["success_effect"])

asyncio.run(intervention())
```

Message IDs are stable `round:sender:index` identities assigned by the evaluator. Checkpoints preserve pre-round agent objects, private state, pending deliveries, channel-policy objects and prefix accounting. `replay_without()` reexecutes the message-generation round and all subsequent agent decisions while suppressing every copy of that message. `run(..., checkpoint=..., replace_messages={id: "neutral"})` instead replaces content and removes its evidence and metadata upon delivery. Replacements alter semantics and are not a perfect null intervention.

For deterministic local policies the replay is exact. An API model, a callback with external mutable state, or an external tool needs a replayable application wrapper and repeated randomized trials. Pure Python deep copies cannot restore remote model randomness. Prefix usage is included in replay totals; `replay_suffix_only_timing` flags that elapsed wall time covers only the replayed suffix. Checkpoints contain private state and remain in memory; JSON reports omit them.

## Bring a real task

Construct `CommunicationCase(id, task, private, required, evaluate, split)`:

- `task` contains public instructions and legal output formats, never evaluator answers.
- `private` maps agent IDs to their initial evidence.
- `required` maps intended recipients to evaluator-known fact IDs needed for the task.
- `evaluate(decisions)` returns finite task metrics including `success`. It receives only designated, aggregated or joint decisions according to the selected mode.

Use passing integration tests, a valid final environment state, or independently checked task outputs as the primary score. Add task-specific metrics for correct evidence use, conflicting assignments, verified duplicated work or harmful propagation. The harness cannot infer those from fluent conversation or citation counts. The scheduling fixture illustrates objective conflict counting. Its receipt and decision logs support inspection of *why* a strategy succeeds or fails.

The [research note](COMMUNICATION_EVALUATION.md) explains the controls and relevant papers. Existing `ExchangeThenDecide` and `GossipRelay` are stateful swarm algorithms, not `Agent` callbacks; they need adapters that preserve the information boundary before using this harness. Their shared-board/internal-delivery caveats still apply outside this evaluator.
