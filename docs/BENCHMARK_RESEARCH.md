# Research on evaluating swarms and multi-agent systems

Reviewed **10 September 2026**. The unit of evaluation is the complete system: agents, model mix, topology, tools, memory, scheduling, and failure handling. This review informs the [eight-track evaluation specification](BENCHMARK_SUITE.md). The specification is a research deliverable; benchmark environments and adapters are not implemented or registered in SwarmKit.

## Main finding

There is no single established benchmark or winning architecture that covers swarm competence. The useful frontier combines **distributed reasoning, joint artifact construction, role-constrained workflows, dynamic execution, decentralized coordination, strategic interaction, and learning across episodes**. Different evaluations measure different subsets of those capabilities. Scores from them are not interchangeable.

For this repository, a useful suite should combine existing realistic tasks with generated diagnostic workloads, and evaluate whether its communication, scheduling, verification, and knowledge-transfer mechanisms contribute under controlled resource budgets. Difficulty should vary along several axes, including dependency depth, information partitioning, permission boundaries, concurrent resource demands, environmental changes, and partner novelty. Grid size is only one possible axis.

This is a selective primary-source review, not an exhaustive systematic review. Sources were searched, papers and repositories downloaded, and selected implementation paths inspected. No upstream model experiments were reproduced. Publication status refers to source metadata where available; recent preprints are not treated as validated consensus. Headline model scores are deliberately not used to rank systems with different task and compute conditions.

## Evidence map

| Work | What it evaluates | What to take from it | Important scope limit |
|---|---|---|---|
| [MASEval, 2026](https://arxiv.org/abs/2603.08835) | Whole-system comparisons across frameworks and benchmarks | Make topology, execution/error handling, and tracing first-class experimental variables | Evaluation infrastructure, not a new task distribution or proof that one framework is universally best |
| [MultiAgentBench / MARBLE, ACL 2025](https://aclanthology.org/2025.acl-long.421/) | Research, coding, database, bargaining, social-game, and embodied scenarios | Use multiple work domains; record milestones alongside end outcomes | Scoring varies across domains. Some implementation paths use LLM judges, so a single aggregate can hide grader differences |
| [CooperBench, 2026](https://arxiv.org/abs/2601.13295) | Concurrent software changes with potentially conflicting implementations | Test whether agents produce a jointly correct artifact, honor commitments, and resolve interference | Primarily two-agent coding; its observed coordination deficit is specific to its tasks and tested systems |
| [EntCollabBench, 2026](https://arxiv.org/abs/2605.08761) | Delegation across specialized enterprise roles, restricted tools, state changes and approvals | Make role permissions and workflow closure part of task success | The paper describes deterministic/state-based evaluation; the downloaded public judging entry point uses model voting. Fidelity requires resolving that discrepancy |
| [Gaia2, 2026](https://arxiv.org/abs/2602.11964) | Asynchronous environments, changing events, deadlines, ambiguity and collaboration | Let the environment progress independently; verify actions and state changes | An agent-environment benchmark with collaboration scenarios, not a clean isolation of decentralized swarm gains |
| [SILO-BENCH, ACL 2026](https://arxiv.org/abs/2603.01045v2) | Algorithmic computation with information distributed among agents | Distinguish acquiring missing information from correctly integrating it; vary communication structure | Algorithmic silos are narrower than tool execution, open-ended discovery, or strategic incentives |
| [HiddenBench, ICML 2026](https://arxiv.org/abs/2505.11556v4) | Decision making under hidden information asymmetry | Test whether agents discover that relevant evidence is missing and request it | Structured hidden-profile tasks; full-information single-agent comparisons change information access and are diagnostic controls |
| [DPBench, current 2026 revision](https://arxiv.org/abs/2602.13255) | Simultaneous resource contention in Dining-Philosophers-style settings | Measure deadlock, symmetry breaking, fairness and throughput; keep simultaneous actions simultaneous | A tightly controlled coordination diagnostic, not evidence that all concurrent workflows require the same mechanism |
| [SwarmBench, 2025 revision](https://arxiv.org/abs/2505.04364v4) | Pursuit, synchronization, foraging, flocking and cooperative transport with local observations | Test spatial decentralization, local communication and congestion | Spatial swarm behavior does not establish useful collective research or organizational memory |
| [ALEM, 2026](https://arxiv.org/abs/2606.08340v1) | Long-horizon coordination in generated survival worlds with specialization and joint actions | Vary temporal coupling and coordination requirements separately from individual competence | A substantial game environment; importing its name or procedural generation does not reproduce its coordination demands |
| [Collab-Overcooked, 2025](https://arxiv.org/abs/2502.20073v3) | Collaborative execution of interdependent production tasks | Separate collaboration process from final task completion; study handoffs | A structured embodied domain; cooking success is only one kind of teamwork |
| [Melting Pot, 2021](https://arxiv.org/abs/2107.06857) | Generalization to unfamiliar partners and social situations | Hold out partner populations, not only task seeds; evaluate cooperation and mixed incentives | Reinforcement-learning populations and substrates differ from tool-using language-agent systems |
| [SMACv2, NeurIPS 2023](https://arxiv.org/abs/2212.07489) | Generated cooperative MARL scenarios with meaningful partial observability | Check whether success really requires observation-conditioned behavior | A fixed/open-loop strategy exploiting predictable task timing can invalidate a benchmark's intended interpretation |
| [TAMAS, ACL 2026](https://arxiv.org/abs/2511.05269) | Adversarial risks across multi-agent tools and communication configurations | Measure whether manipulated messages or tool responses propagate into consequential actions | Adversarial robustness is distinct from ordinary reliability and from clean task competence |
| [MEAL, ICML 2026 revision](https://arxiv.org/abs/2506.14990v3) | Continual multi-agent reinforcement learning across long task sequences | Evaluate retention, adaptation and interference over many episodes | Neural continual learning is not equivalent to transferring written procedures or shared artifacts; that is a proposed SwarmKit extension |
| [ScienceAgentBench](https://arxiv.org/abs/2410.05080) and [DiscoveryBench](https://arxiv.org/abs/2407.01725) | Scientific workflow tasks and data-driven discovery | Evaluate executable analyses and independently checked findings, rather than confident research prose | Domain benchmarks are not inherently multi-agent evaluations; the swarm contribution requires separate controls |
| [AsymPuzl, 2025](https://arxiv.org/abs/2512.03466v1) | Minimal asymmetric-information cooperation with feedback variations | Useful optional microdiagnostic for communication and feedback | Supports a specific controlled experiment. It does not justify centering a general swarm suite on puzzles |

The evidence supports a **portfolio of evaluations**, with domain success and collective contribution reported separately. It does not support deriving the whole portfolio from one entertaining task format.

## What the code review changed

The [archive manifest](../sources/benchmarks/manifest.json) identifies downloaded commits. The [repository audit](../sources/benchmarks/repository-audit.md) links the inspected files at those commits. These are selected code inspections, not complete audits.

**SILO-BENCH has an inspectable answer-checking path.** `src/engine.py::evaluate` loads expected per-agent outputs from task metadata and treats absent final submissions as wrong. `src/utils/metrics.py` distinguishes exact answers from level-dependent partial correctness. This is a useful native-diagnostic reference: the evaluator can determine correctness without asking a language model to assess the conversation.

**CooperBench checks the merged work.** `src/cooperbench/eval/evaluate.py` and its sandbox helpers distinguish solo and cooperative patches and invoke tests for feature implementations. Its Python/environment/backend requirements belong in an optional adapter, outside SwarmKit's lightweight core. Repository checkouts alone do not include a configured runnable experiment with downloaded datasets, execution backends, and model credentials.

**MARBLE's scoring is not uniformly objective.** The old official repository redirects readers to `ulab-uiuc/MARBLE`; both commits were archived. The latter's `marble/evaluator/evaluator.py::parse_score` can return a default rating of 3 on failed parsing. Communication/planning assessments use model-generated ratings. An adapter must preserve which metrics are judged, record parsing failures, and avoid silently interpreting a default as measured competence.

**EntCollabBench's paper and public judging entry point require reconciliation.** The paper describes execution traces, database verification and deterministic policy adjudication. The downloaded `scripts/judge/judge.py` requires `JUDGE_MODELS`, invokes a model-voting routine, and labels its CLI as an LLM-as-judge evaluator. Its README likewise describes judge-model setup. This does not establish that all deterministic checks are absent from every service; it does mean the inspected command cannot honestly be described as a purely deterministic grader. Inspect the full service/evaluator path before adopting it as ground truth.

**MASEval separates system execution from evaluation and records failures.** Its `maseval/core/benchmark.py` provides separate hooks and controls for setup, task, and evaluation errors. SwarmKit should preserve these distinctions: a broken grading service is neither a successful agent episode nor an ordinary wrong answer.

**ALEM exposes explicit communication and observation surfaces.** The downloaded README and prompt example document per-agent text observations, bounded communication and scratchpad memory. This is a useful interface reference, but a small dependency toy would not be an ALEM implementation or substitute.

## How to measure the value of a swarm

Several recent comparisons warn that reported multi-agent gains can disappear when compute is controlled. [Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets](https://arxiv.org/abs/2604.02460v2) studies a specific multi-hop setting and explicitly discusses API budget artifacts. Its conclusions are not a theorem about all interactive swarms. [Debate or Vote](https://arxiv.org/abs/2508.17536v2) motivates independent-sampling controls; it does not rule out benefits from new evidence or coordinated actions.

The [scaling-agent-systems study](https://arxiv.org/abs/2512.08296v3) likewise motivates task-dependent comparisons. SwarmKit already archives these sources and provides related evaluation utilities, but those wrappers cannot meter opaque external model calls themselves.

Each evaluation should answer three separate questions:

1. **Capability:** did the system accomplish the externally specified task?
2. **Contribution:** did the collective mechanism improve the result relative to a properly defined control?
3. **Efficiency and robustness:** what did that improvement cost, and does it survive changes in partners, scale, failures and task distribution?

Use both fixed-total-work and fixed-time experiments, reported separately. Record input/output/reasoning tokens where available, model calls, tool work, evaluator work, elapsed time, and peak concurrency. Matching only the number of turns is not matching compute. Unreported token use must be unknown, not zero.

Recommended controls include a single agent with equivalent aggregate tools/information where feasible; independent workers with a predeclared aggregator; the same team with explicit messages disabled; alternative topologies; and simple task-specific algorithms. A pooled-information control diagnoses reasoning after eliminating information acquisition. It changes the information condition and must be labeled accordingly.

Disabling messages does not create independence if agents can still read each other's files, shared artifacts, tool writes, or environment actions. Conversely, a lone agent lacking the other roles' permissions is a capability-ablation control, not a fair test of single-agent reasoning. Controls need a written access matrix.

## What this means for this repo

The most direct links to implemented SwarmKit mechanisms are:

- **Evidence acquisition and integration:** `Evidence`, `InformationGate`, `GossipRelay`, `ExchangeThenDecide`, and provenance-aware evaluation.
- **Joint work and handoffs:** `DAGExecutor`, agent contexts, scoped task descriptions, and artifact verification.
- **Decentralized coordination:** communication topologies and hypergraph membership, measured against real simultaneous or interdependent execution requirements.
- **Collective knowledge:** `ArtifactStore`, `PeerAdoption`, `ProcedureAbstraction`, `CulturalTransfer`, and retirement/rollback.
- **Learning and selection:** population search, communication-policy learning and counterfactual evaluation.
- **Economic behavior:** the proposed economic-game layer, which is still research rather than installed functionality.

Hypergraphs are useful when several agents' contributions jointly determine completion or utility. Benchmark definitions should identify these joint requirements and their feasible alternatives. Counting group messages or drawing a hypergraph does not demonstrate higher-order cooperation.

The resulting [suite specification](BENCHMARK_SUITE.md) defines eight primary tracks, their scoring, size controls, baselines and implementation paths. Existing realistic benchmarks should be adapted where possible. Generated cases should isolate a diagnosed mechanism or fill a genuine coverage gap; they should not be relabeled reproductions of the papers motivating them.
