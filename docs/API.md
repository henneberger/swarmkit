# API and composition

All population-facing records come from `swarmkit.types`. The top-level package re-exports the shared contracts, runtime, and registry; algorithm implementations are grouped by domain.

## Execution contracts

There are two complementary execution paths:

1. **Synchronous algorithms:** `Pipeline([algorithm, ...]).step(state, task)` invokes `step`, commits returned messages/artifacts, and increments `state.step` once per stage. This path implements symbolic mechanisms and model-independent experiments.
2. **Agent callbacks:** `await SwarmRuntime(state, agents, ...).round(task, phase=...)` or `.run(task, phases=...)` invokes your model/tool-backed agents using round-start snapshots. Policies constrain communication; the runtime does not interpret a task as permission to execute arbitrary code.

Call `algorithm.step` directly to inspect its outputs before delivery. Such callers own the subsequent `apply_result` and step increment. Do not increment time both manually and through `Pipeline`.

Methods that retain episode state bind it to task ids or namespaces. Use a fresh state, a documented reset method, or a new namespace for an independent episode. Configured policies/trainers, artifact stores, and feed/trust objects may carry their own state; a `SwarmState` checkpoint is not a serialized deployment of every object.

## Topology-constrained disclosure

```python
from swarmkit import MessageBus, Pipeline
from swarmkit.deliberation import ExchangeConfig, ExchangeThenDecide
from swarmkit.topology import RingTopology

# Use with a SwarmState and Task from the README example.
exchange = ExchangeThenDecide(ExchangeConfig(delivery="inbox"))
bus = MessageBus(topology=RingTopology())
result = Pipeline([exchange, exchange, exchange], bus=bus).step(state, task)
```

The topology applies to addressed messages as well as broadcasts. Empty `Message.recipients` means broadcast to reachable active peers. A sender never receives its own broadcast. `MessageBus` deduplicates ids and rejects conflicting id reuse. A `recipient_filter` can apply additional exposure rules.

The exchange protocol's default `all_peer` mode uses an internal public evidence board. Wrapping that mode in a sparse bus does not change the board. Choose `delivery="inbox"` for real topology restrictions. Evidence may need multiple rounds to traverse a sparse graph; consensus cannot assume unreachable facts have been surfaced.

`GossipRelay(neighbors=topology.neighbors, ...)` is another synchronous evidence-propagation mechanism. It freezes the previous delivery state so a card cannot traverse multiple edges within one round. Bandwidth and lifetime limits are configurable. It records delivered evidence internally and returns messages for normal bus commit.

## Connect a model or tool-backed agent

The minimal adapter returns the common `AgentOutput`:

```python
from swarmkit import AgentOutput, Budget, CallableAgent, Message, SwarmRuntime

async def act(context):
    # Use context.task, context.agent.private_evidence, and context.messages.
    # Call your chosen provider/tool here; return its measured usage if available.
    text = "I can test the route assumption."
    return AgentOutput(messages=(Message(context.agent.id, text),))

runtime = SwarmRuntime(
    state,
    {agent_id: CallableAgent(act) for agent_id in state.active_ids},
    budget=Budget(max_calls=12),
    concurrency=3,
)
# In an async function or notebook:
result = await runtime.run(task, phases=("explore", "decide"))
```

For a text-completion client:

```python
from swarmkit import CompletionAgent

async def complete(prompt: str) -> str:
    return await your_client.complete(prompt)  # Supply your actual client.

agent = CompletionAgent(complete, system="Share evidence and identify assumptions.")
```

`CompletionAgent` asks for structured decision JSON in the `decide` phase. It rejects unknown candidates and unavailable evidence ids. Received evidence is retained in task-scoped memory between phases. It cannot verify claims a model writes in free text; use structured `Evidence` and an evaluator for that.

`AgentOutput.memory_updates` explicitly persists local memory updates. Mutating the context copy itself does not modify the authoritative state. Artifacts returned by an agent are marked unverified unless the runtime's configured verifier accepts them.

A round processes valid independent outputs even if another callback fails. `fail_fast=True` raises after dispatch completes and rolls back the round's output commits. External API calls and usage cannot be rolled back. Cancellation commits no partial round output; synchronous thread callbacks may continue running against their private copies.

## Verified artifacts and local adoption

```python
from swarmkit import Artifact, Feedback
from swarmkit.knowledge import ArtifactStore, PeerAdoption

store = ArtifactStore(
    verifier=lambda artifact: Feedback(
        utility=score_construction(artifact.content),
        verified=check_construction(artifact.content),
    )
)
artifact = store.admit(Artifact("construction-v1", "scout", construction))

# Compare a recipient's existing method with the candidate under local conditions.
def evaluate(agent, candidate, task):
    return measure_on_local_cases(agent, candidate, task)  # Returns Feedback.

adoption = PeerAdoption(store, evaluate, minimum_gain=0.01)
accepted = adoption.adopt(state.agents["planner"], artifact.id, task)
```

Admission rejects missing/cyclic ancestry and failed external checks. `PeerAdoption.audit` rechecks retained utility and can restore a previous adoption after a regression. Inherited artifacts retain their original author and ancestry; a revision receives a fresh id and parent links.

`ProcedureAbstraction` accepts a candidate generator and a held-out evaluator. It checks reusable procedures against explicit new cases. The library provides the generation/evaluation lifecycle, not a universal abstraction oracle.

## Learn who should communicate

```python
from swarmkit.topology import BernoulliDAGPolicy

policy = BernoulliDAGPolicy()
# Sample topology, use it through MessageBus, evaluate the task, then give feedback.
# See examples/learn_topology.py for the complete executable feedback loop.
```

A sample is held stable within one step. `update` applies the sampled graph's feedback once, including absent-edge gradients. Pruning removes weak edges permanently; use a fresh policy namespace for an independent experiment. The fixed agent order defines DAG direction, so choose it deliberately.

`ParticleSwarmSearch` optimizes populations of `Artifact` configurations. Its mutation callback receives current, personal-best and global-best artifacts, bounded failure history, and the state's RNG. This supports textual, symbolic or numerical candidate designs without pretending they all share one numeric velocity formula.

## Numerical communication

```python
from swarmkit import LatentPayload, Message
from swarmkit.communication import GeometricAlignment, LatentMemory

codec = GeometricAlignment("sender-model", "receiver-model").fit(
    paired_sender_states, paired_receiver_states,
)
packet = codec.transform(LatentPayload(new_sender_states, "sender-model"))
memory = LatentMemory(max_tokens=128)
memory.append(packet)
message = Message("scout", "", recipients=("planner",), metadata={"latent": memory.read()})
```

Calibration rows must be semantically aligned. The final array axis is the feature dimension; `KVCacheTranslator` requires matching leading axes across calibration caches. Models, layers, dimensions and finite values are checked. Core serialization handles these shared numeric packets.

`ContrastiveLatentCodec` learns paired retrieval against mismatched negatives. `LatentBottleneck` provides an observable compression/reconstruction baseline. Neither lower reconstruction loss nor higher retrieval accuracy is itself proof of factual preservation. A real integration needs hidden-state access and downstream evaluation.

## Evaluate collective benefit

The evaluation module separates population properties from knowledge outcomes:

- `population_diversity`, `interaction_reciprocity`, `hyperedge_irreducibility`: structural diagnostics.
- `private_evidence_recovery`, `ancestry_adjusted_agreement`: disclosure and dependence diagnostics.
- `transfer_gain`: paired recipient utility change.
- `matched_independent_control`: same initial evidence and divided total work budget for isolated agents.

Callbacks must honor evaluation budgets and keep held-out cases hidden during discovery. One interacting population is one experimental unit; its members are not independent replications.

## Checkpoints

```python
from swarmkit.serialization import save, load

save(state, "swarm-state.json")
restored = load("swarm-state.json")
```

JSON snapshots preserve shared dataclasses, tuples/sets/maps, numerical arrays, and the RNG state. Unsupported objects fail explicitly. This avoids pickle and arbitrary class imports. Paths and externally held verifiers/models remain caller-managed. Do not assume a snapshot excludes private evidence: it intentionally contains the full local population state.
