# SwarmKit

**Composable algorithms for agentic swarms and collective knowledge.**

SwarmKit is a Python library for building populations of agents that explore independently, exchange evidence, challenge conclusions, and reuse discoveries. It brings communication, deliberation, learning, and evaluation into one shared type system, so you can combine mechanisms and test what each contributes.

The library includes **49 registered methods**, a provider-neutral async runtime, deterministic offline examples, and an optional DeepSeek client with persistent spending controls. Python **3.10+** is required; **NumPy is the only required third-party runtime dependency**.

[Method catalog](docs/METHODS.md) · [API and composition guide](docs/API.md) · [Research background](SWARMS_REPORT.md) · [Attribution](THIRD_PARTY_NOTICES.md)

## Goals and motivation

The central question is: **when does interaction let a group discover or accomplish something its members would miss working independently?**

An agent may hold a useful observation that never reaches the person making a decision. Several agents may agree because they inherited the same mistaken source. A successful solution may disappear at the end of a run, or fail when another agent tries to reuse it. SwarmKit makes these situations explicit through private evidence, controlled communication, source ancestry, persistent artifacts, and local evaluation.

Its goals are to:

- **Make swarm mechanisms composable.** Change the communication graph, decision rule, memory policy, or learning procedure without rebuilding the surrounding experiment.
- **Make information flow inspectable.** Track who knew what, which evidence was shared, and where conclusions and artifacts came from.
- **Turn discoveries into reusable knowledge.** Preserve lineage, test an artifact before adopting it, and roll back adoption when its utility regresses.
- **Measure the value of collaboration.** Compare interacting agents with independent controls, account for work and cost, and evaluate transfer on held-out cases.
- **Connect research ideas to executable components.** Give each registered method an implementation, source attribution, and an explicit description of its fidelity and limits.

You supply the agents, tools, task-specific evaluators, and environment. SwarmKit supplies the mechanisms for organizing their interaction and examining the results.

## Feature tour

### One set of contracts, two ways to execute

`AgentState`, `SwarmState`, `Task`, `Evidence`, `Message`, `Decision`, `Artifact`, `Feedback`, `Usage`, and `Budget` are shared across the library.

Use `Pipeline` to compose synchronous algorithms for symbolic experiments and offline baselines. Use `SwarmRuntime` for async model or tool callbacks, with phases, bounded concurrency, message routing, and usage accounting. Agents receive round-start snapshots, so one callback cannot silently change another agent's input during the same round. Explicit memory updates persist between rounds.

`CallableAgent` accepts your own callback; `CompletionAgent` adapts a text-completion function. The core runtime does not require a particular model provider.

### Control who communicates, and when

Choose full, ring, star, random, spatial, or hypergraph neighborhoods through `MessageBus`. Explore learned Bernoulli graph policies, pruning, agent dropout, and capability-based routing. Topology constraints apply to both broadcasts and addressed messages.

Information gates can trigger communication from novelty or changes in beliefs. Evidence compression bounds the number of shared cards while retaining provenance and counterevidence. Gossip relays propagate evidence with bandwidth and lifetime limits. Together, these let you study selective communication and its effect on cost and information access.

### Exchange evidence before committing to an answer

Start with `IndependentVoting`, then introduce `ExchangeThenDecide`, critique/revision callbacks, or weighted consensus. Evidence records express support and contradiction; an evidence registry tracks ancestry and shared roots.

This makes it possible to test whether a minority observation changes a decision and whether apparent agreement rests on repeated copies of the same source. For experiments with restricted communication, select `ExchangeConfig(delivery="inbox")`; the default exchange mode uses an all-peer evidence board.

### Preserve discoveries and test their reuse

`ArtifactStore` admits artifacts through a caller-supplied verifier and preserves their ancestry. `PeerAdoption` compares a candidate with the recipient's existing approach, tests local utility, and supports rollback after regressions.

Other components model decaying memory, transfer across generations, and procedure abstraction evaluated on held-out cases. Stigmergic policies let agents discover and reuse artifacts through shared environmental traces. These mechanisms support experiments in knowledge accumulation across tasks and populations.

### Search, learn, and model social behavior

Population artifact search combines personal and global best candidates with failure history. Coordination learning and scheduling components expose feedback-driven choices about how agents work together.

Naming games, proportional copying, feeds, directional trust, and convention/diversity measures support controlled studies of social dynamics. You can examine how a convention spreads separately from whether a claim is supported or a procedure is useful.

### Experiment with numerical communication

`LatentPayload` and `KVCache` extend the same message boundary to numerical state. Components include latent memory, geometric alignment, vocabulary anchoring, linear adapters, KV translation, contrastive training, and a compression/reconstruction baseline.

These are building blocks for integrations where you have access to compatible model internals. You must supply real hidden states and calibration data; downstream evaluation determines whether a transformed payload preserves useful information.

### Evaluate and reproduce the experiment

Evaluation helpers cover private-evidence recovery, ancestry-adjusted agreement, population diversity, interaction structure, transfer gain, and matched independent controls. They let you separate communication activity, agreement, and useful outcomes.

JSON checkpoints preserve shared records, numerical arrays, and RNG state. Models, verifiers, and externally held policy state remain caller-managed. Seeded mechanisms and offline fixtures make small experiments repeatable before you connect a paid model.

The optional `swarmkit.providers.deepseek` integration adds a SQLite call gate that reserves calls, tokens, and estimated spending before dispatch across processes sharing a ledger. Generic runtime budgets account for returned usage; they do not independently reserve provider spending. See the [API guide](docs/API.md) and [provider implementation](src/swarmkit/providers/deepseek.py) for the contracts.

## Get started

Install from a checkout:

```bash
git clone git@github.com:henneberger/swarmkit.git
cd swarmkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

The distribution is named `swarmkit-research`; Python imports and the library CLI use `swarmkit`.

Run an offline demonstration and browse the registry:

```bash
swarmkit demo
swarmkit list
swarmkit list --family knowledge --json
```

No API credentials or network calls are needed for these commands.

### A small evidence-exchange experiment

Three agents share an old map. Only one has a new survey. Compare their independent decisions with decisions after evidence exchange:

```python
from swarmkit import AgentState, Evidence, Pipeline, SwarmState, Task
from swarmkit.deliberation import (
    ExchangeThenDecide,
    IndependentVoting,
    WeightedConsensus,
)

shared = Evidence(
    "old-map", "Old map recommends A", "map", "planner",
    supports=("A",), confidence=0.4,
)
survey = Evidence(
    "new-survey", "A is closed; B is passable", "survey", "scout",
    supports=("B",), contradicts=("A",),
)
state = SwarmState(
    {
        name: AgentState(
            name,
            private_evidence=(shared, survey) if name == "scout" else (shared,),
        )
        for name in ("planner", "scout", "reviewer")
    },
    seed=7,
)
task = Task("route", "Choose the currently passable route", candidates=("A", "B"))
consensus = WeightedConsensus()

before = IndependentVoting().step(state, task)
exchange = ExchangeThenDecide()
after = Pipeline([exchange, exchange, exchange]).step(state, task)

print(consensus.aggregate(before.decisions, task).metadata["winner"])  # A
print(consensus.aggregate(after.decisions, task).metadata["winner"])   # B
```

This fixture uses symbolic evidence scoring. It demonstrates the information-flow mechanism; it does not establish model performance or a general advantage for swarms.

Continue with executable compositions:

| Example | What it demonstrates |
|---|---|
| [Collective discovery](examples/collective_discovery.py) | Private evidence → exchange → verified artifact → local adoption |
| [Social culture](examples/social_culture.py) | Convention formation, ranked visibility, evidence relay, and memory maintenance |
| [Learn topology](examples/learn_topology.py) | Feedback-driven communication graph learning and pruning |

The [API guide](docs/API.md) covers model callbacks, topology-constrained delivery, artifact verification, latent payloads, and checkpoints.

## Why it is relevant

SwarmKit is useful when **information, exploration, or experience is distributed across agents**, and you need to understand whether connecting them improves the result.

For an application developer, it provides interchangeable pieces for evidence-sharing assistants, collaborative search, and tested reuse of solutions. For a researcher, it provides common contracts for comparing communication graphs, disclosure rules, memory, social influence, and independent baselines. For someone exploring swarm methods, its small offline examples make mechanisms accessible before adding model behavior and API costs.

The practical benefit is an experiment you can change and inspect: hold the task and initial evidence fixed, vary how agents communicate, and measure which information reaches a decision, what gets reused, and what the interaction costs.

## Scope and research fidelity

SwarmKit is a research library. Its registered entries include primitives, mechanisms, components, adaptations, baselines, designs, and metrics. They do not reproduce every source paper's training setup or benchmark results. The [method catalog](docs/METHODS.md) records the distinction for each entry.

A `verified` artifact has passed the supplied verifier's contract. Source ancestry depends on the source identifiers you provide. Consensus measures agreement. Meaningful claims about correctness or collective benefit require suitable external checks, held-out evaluation, and independent experimental runs.

The repository also contains an [Enron investigation application](ENRON_SWARM_DESIGN.md) built with the library. Its corpus tooling, UI, and experiment reports are an application case study; they are not prerequisites for using SwarmKit or evidence of a demonstrated general swarm advantage.

## Development and project layout

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
python -m ruff check src tests examples scripts/check_secrets.py
python -m build
python scripts/check_secrets.py
```

Tests use synthetic fixtures and fake provider transports; API credentials are not required.

| Path | Contents |
|---|---|
| `src/swarmkit/` | Shared contracts, runtime, algorithm modules, and registry |
| `src/swarmkit/providers/` | Optional provider integration and persistent call gate |
| `examples/` | Offline library compositions |
| `tests/` | Unit and integration tests |
| `docs/` | Method catalog, API contracts, and application documentation |
| `sources/`, `repositories/` | Research inventory and pinned upstream Git submodules |
| `src/swarmkit/enron/`, `reports/` | Investigation application and experiment records |

Research submodules are optional for library use. To fetch them for comparison:

```bash
GIT_LFS_SKIP_SMUDGE=1 git submodule update --init --recursive --depth 1
```

New project code is [MIT-licensed](LICENSE). Research documents and upstream projects retain their respective rights; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
