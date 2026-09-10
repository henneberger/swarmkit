# Swarm evaluation suite specification

Version 0.1, **10 September 2026**. This constructs eight evaluation tracks from the [research review](BENCHMARK_RESEARCH.md). **These are specifications, not runnable benchmark environments or claimed results.** No puzzle-centered implementation is included. The machine-readable counterpart is [suite-spec.json](../sources/benchmarks/suite-spec.json).

The objective is to measure whether SwarmKit's collective mechanisms improve useful outcomes, at known cost, across several kinds of interdependence. Report a capability profile rather than one unsupported “swarm intelligence” number. Start with realistic benchmark adapters and a few controlled probes; keep optional heavy dependencies outside the core.

## The eight primary tracks

| ID | Evaluation | Primary outcome | Initial implementation path |
|---|---|---|---|
| E1 | Distributed evidence and computation | Correct answer and recovery of necessary evidence | SILO-BENCH/HiddenBench adapters; generated database joins and hidden-profile cases |
| E2 | Joint artifact construction | All component and integration checks pass | CooperBench adapter; controlled cross-component change fixtures |
| E3 | Heterogeneous tool workflows | Correct final state reached through authorized roles | Enterprise workflow adapter after grader audit; deterministic local service fixtures |
| E4 | Dynamic execution and recovery | Task completed despite asynchronous changes and failures | Gaia2/ARE adapter or explicit event-driven workflow fixtures |
| E5 | Decentralized coordination and resource contention | Throughput, fairness and jointly feasible execution | DPBench/SwarmBench adapters; generated resource/dependency workloads |
| E6 | Economic and strategic interaction | Feasible allocation, surplus, and robustness to strategic partners | Downloaded auction/negotiation references; proposed economic layer |
| E7 | Collective exploration and discovery | Independently verified findings per resource budget | Scientific-workflow benchmarks plus controlled experimental environments |
| E8 | Persistent collective learning and transfer | Held-out transfer gain, retention and adaptation | SwarmKit knowledge mechanisms; MEAL-inspired episode sequences |

These are our design choices informed by the research, not a taxonomy copied from a single benchmark. E1–E5 have direct task references; E6 connects the prior economic research; E7–E8 require particular care to distinguish domain progress from a demonstrated collective effect.

### E1 — Distributed evidence and computation

**Scenario.** Agents hold different tables, logs or observations. The system must answer a question that requires combining them: identify the only compatible supplier across constraints, reconcile a transaction chain, join records to identify a root cause, or revise a shared initial hypothesis when a private fact invalidates it.

**Scale independently.** Agent count; records per shard; join/dependency depth; key skew; evidence redundancy; fraction of decisive facts held privately; conflicting observations; communication bandwidth; and graph connectivity. Hold total evidence fixed when studying partition count, then run a separate growing-total-data experiment.

**Verifier.** A hidden reference query or known generative model supplies the answer and its supporting record IDs. Require the answer and valid supporting references; compute task correctness and evidence recall separately. Some tasks need one final answer, others require globally consistent per-agent outputs—declare which.

**Controls.** Same model with all inputs; private-input independent workers plus a fixed aggregator; team with explicit messaging disabled and shared channels accounted for; structured versus free-form disclosure. Use exact SQL/algorithmic solvers as task oracles, not claimed language-agent baselines.

**Hard failure.** Everyone agrees on an unsupported answer, missing evidence is copied until it looks corroborated, or an agent acquires the facts but integrates them incorrectly. Measure these separately rather than using agreement as success.

**Sources and fit.** SILO-BENCH and HiddenBench; directly exercises SwarmKit's evidence, communication, topology and deliberation components.

### E2 — Joint artifact construction

**Scenario.** Several agents implement individually specified changes to a shared system. Examples include an API change, a dependent client change, and a migration that must all work together. An individual contribution can pass its local tests while breaking the combined artifact.

**Scale independently.** Number of contributors; dependency graph width/depth; overlapping files or interfaces; number of conflicting assumptions; test observability; and delayed handoffs. Preserve comparable task work when varying agent count.

**Verifier.** Freeze the base commit and hidden component/integration tests. Evaluate each contribution and the final merged artifact. Record patch conflicts, interface mismatches, abandoned work, and regressions. Agents cannot modify the evaluator or its hidden tests.

**Controls.** A single agent doing the same total workload; parallel agents without messaging; explicit interface-contract exchange; a central integrator; and peer integration. Use the same permitted repository and test access.

**Hard failure.** All local tasks appear complete but the delivered program fails integration. Commitments in messages are measured against actual changes, not judged for persuasiveness.

**Sources and fit.** CooperBench is the closest direct reference. Adapt it before inventing a toy coding replacement. SwarmKit's scheduling and artifact mechanisms provide integration points; its core does not provide code-execution isolation.

### E3 — Heterogeneous tool workflows

**Scenario.** A request spans several stateful services and agent roles. For example, resolve an inventory exception, update a purchase order, arrange delivery, and reconcile the resulting ledger. Each role has limited tools and information; successful delegation must preserve identifiers, requirements and completion conditions.

**Scale independently.** Role count; cross-role dependencies; tool schema complexity; permission partitioning; necessary context per handoff; workflow length; and concurrent requests sharing records.

**Verifier.** Check final database state, referential integrity, required events and allowed actions against a fixed specification. A natural-language “done” message is not completion. Judge failures and unavailable services are recorded distinctly from task failures.

**Controls.** Authorized single-agent control with equivalent aggregate access when the task allows it; role-preserving team baselines; explicit structured handoff versus free-form delegation; and capability-based routing versus learned routing. A permission-restricted single role is only a capability ablation.

**Hard failure.** The right department receives the wrong entity ID, changes are made in only one service, or agents stop after delegation without verifying closure.

**Sources and fit.** EntCollabBench and MARBLE enterprise/database settings. Resolve the documented discrepancy between EntCollabBench's paper and public LLM-judge path before treating its command-line scores as deterministic ground truth.

### E4 — Dynamic execution and recovery

**Scenario.** During an ongoing workflow, an external event changes the goal or invalidates a plan: a reservation disappears, a job completes out of order, a tool times out after applying its write, a worker leaves, or a new urgent task arrives. The system must detect the event, update its plan and finish coherently.

**Scale independently.** Event rate; event delay; task horizon; worker dropout; probability of ambiguous tool completion; deadline tightness; and state-change frequency. Use a controlled virtual clock for reproducibility and a separate real-time evaluation for latency claims.

**Verifier.** Check final state and event ordering. Count duplicate irreversible effects, missed deadlines, stale-plan actions, recovery duration, and unfinished obligations. Include a run with no disturbance for the same base task.

**Controls.** Fixed retry policy; centralized event loop; decentralized reallocation; no shared recovery memory; and idempotent versus naive execution. Pair the same exogenous event schedule where possible, while defining how schedules respond to different action timings.

**Hard failure.** A timeout causes a second payment, the system retries a cancelled task, or all agents continue work based on outdated state. Static final-answer tasks cannot reveal these failures.

**Sources and fit.** Gaia2/ARE supplies the dynamic-environment reference; MASEval motivates explicit setup/task/evaluation error categories. SwarmKit's async runtime and persistence need an environment adapter with clearly defined event semantics.

### E5 — Decentralized coordination and resource contention

**Scenario.** Agents must finish jobs while sharing tools, transport capacity, or space. Some jobs need simultaneous contributions from a coalition; others need sequential handoffs. Resource contention can create deadlock or starvation even when every agent follows a locally reasonable plan.

**Scale independently.** Agent count; shared resources; resource-to-agent ratio; dependency width/depth; local visibility; hyperedge arity/overlap; action simultaneity; communication delay/loss; and topology.

**Verifier.** A resource ledger and task state machine enforce feasibility. Measure completed work, makespan, utilization, deadlocks, starvation, and coalition completion. Compare to an exact scheduling optimum only on small solvable instances; label larger bounds or heuristics accurately.

**Controls.** Random legal policy; deterministic priority rule; centralized scheduler; local policies; pairwise coordination; and hyperedge-aware coordination. Keep per-agent simultaneous action slots identical across conditions.

**Hard failure.** Everyone waits for someone else, retries the same conflict, or succeeds only because the harness resolves nominally simultaneous moves sequentially. Benchmark the harness's timing semantics with deliberately conflicting actions.

**Sources and fit.** DPBench, SwarmBench, Collab-Overcooked and ALEM. This evaluates actual execution interdependence, beyond measuring the shape of communication.

### E6 — Economic and strategic interaction

**Scenario.** Agents with private costs or values negotiate task contracts, buy or sell capacity, bid for complementary resources, or fund a shared artifact. Cooperation can improve total value while individual incentives favor withholding, free riding or aggressive bidding.

**Scale independently.** Market size; valuation/cost distributions; bundle complementarities; budget tightness; repeated interaction horizon; information asymmetry; partner mixture; and coalition size.

**Verifier.** Check allocations, inventories, balances, payments and delivered outcomes. Report total surplus and individual utility separately. Use exact small-instance optimum comparisons; estimate unilateral and coordinated deviation gains with a declared search budget. A sampled best deviation is not a proof of equilibrium.

**Controls.** Fixed allocation; truthful-reference and random legal bids; simple adaptive policies; homogeneous and mixed LLM/scripted populations; mechanism changes with the same population; unseen partners. Truthful-reference behavior is not optimal in every mechanism.

**Hard failure.** High private profit comes from a broken ledger, collusion harms system welfare, or a team collects payment without completing the verified task. Do not collapse agent utility and principal utility into an unexplained score.

**Sources and fit.** [Economic-games research](ECONOMIC_GAMES_RESEARCH.md), including the downloaded September 2026 double-auction experiment and negotiation libraries. This track depends on economic functionality not yet implemented in SwarmKit.

### E7 — Collective exploration and discovery

**Scenario.** Agents allocate a limited experimental budget across hypotheses and combine results to produce a useful, independently checkable finding. Examples include identifying which change improves a data-processing pipeline, finding a failure region of an algorithm, or deriving a predictive rule across experimental conditions.

**Scale independently.** Hypothesis count; experiment cost; noise; number of complementary observations; accessible tool types; repeated-query value; and nonseparable interactions. Vary whether a finding requires combining experiments from several agents.

**Verifier.** Freeze hidden validation data or an external executable test. Require a reproducible artifact: a tested program, predicted held-out outcomes, or a falsifiable hypothesis with supporting observations. Count verified findings, useful coverage, duplicate experiments, false discoveries, and resource expenditure.

**Controls.** Single investigator with the same tools/budget; independent parallel search with a fixed selection rule; shared experiment registry; peer critique; and shared artifacts. Allow each control comparable opportunities to discover new information. Avoid selecting the best output using hidden answers unless it is explicitly labeled an oracle ceiling.

**Hard failure.** Agents repeat the same experiments, share an attractive but false explanation, or optimize a visible proxy that fails hidden validation. More discussion and more hypotheses are not success by themselves.

**Sources and fit.** ScienceAgentBench/DiscoveryBench are domain-task references, not direct collective-effect proofs. SwarmKit's population search, artifact verification and evidence lineage make this a particularly relevant proposed extension.

### E8 — Persistent collective learning and transfer

**Scenario.** A swarm solves a sequence of related tasks, records reusable procedures, transfers them to new agents, and adapts when the environment changes. Some inherited procedures become invalid. Success requires retaining useful knowledge and retiring harmful knowledge.

**Scale independently.** Sequence length; task-family diversity; relatedness between training and evaluation; agent turnover; memory budget; environmental drift; and the fraction of misleading inherited artifacts.

**Verifier.** Evaluate new tasks and fresh agents with discoveries frozen before the test phase. Measure paired transfer gain, retained performance on older tasks, adaptation cost, invalid-artifact adoption and rollback. Use held-out task families as well as held-out seeds.

**Controls.** No persistent memory; each agent's private memory only; shared raw logs; shared verified artifacts; structured procedures; and no retirement/rollback. Match the information/storage budget or report it explicitly. Reset memory between independent replications, but preserve it within each declared continual episode sequence.

**Hard failure.** Scores rise because test examples leaked into memory, or a once-useful procedure is copied after the world changes. Corpus popularity and reuse count are not evidence of positive transfer.

**Sources and fit.** MEAL motivates continual multi-agent evaluation, while the move to explicit artifacts is our proposal. This track directly tests `PeerAdoption`, `ProcedureAbstraction`, `CulturalTransfer`, audits and retirement.

## Common evaluation contract

Each task or task generator needs a versioned manifest containing:

| Field | Required meaning |
|---|---|
| Task identity | Family, generator/dataset version, split, instance ID, evaluator version, upstream commit where applicable |
| Objective and completion | Externally observable success condition, stopping rule, valid abstention, partial-credit definition |
| Information and authority | Per-role observations, tools, private data, public artifacts, shared-state channels, who can commit results |
| Timing | Sequential/simultaneous/asynchronous behavior, clock semantics, message delay, deadlines, external-event rules |
| Resources | Aggregate and per-agent budgets; counted units; dispatch limits; retry and evaluator accounting |
| Interdependence | Whether agents contribute information, tools, simultaneous actions, complementary artifacts, or conflicting objectives |
| Ground truth | Hidden solver/checks, grader type, expected invariants, grader failure behavior and leakage boundary |
| Experimental condition | System identity, models, prompts, topology, memory, control variant and perturbations |
| Trace and outcome | Tool effects, delivered messages, artifacts, usage, task success/failure, infrastructure errors and truncation |

A message transcript is insufficient for many tracks. Persist the state transitions and actual artifacts required to verify the task. Shared message content is untrusted task data; adversarial tests must not let it redefine the evaluator's rules.

Use the existing `Task`, `AgentContext`, `AgentOutput`, `Artifact`, `Feedback` and `Usage` records where they fit. Put hidden answers and generators in the evaluator boundary, outside agent inputs. A task's public generation seed can leak the answer if agents can reproduce its generator; retain seeds in evaluator manifests and publish them only after a frozen evaluation where appropriate. An in-process Python callback is a trusted integration boundary, not a sandbox for hostile agents.

## Cross-cutting test matrix

Apply these perturbations across primary tracks rather than treating each as another unrelated game:

- **Information:** distributed, pooled, redundant, contradictory, delayed or missing.
- **Communication:** full, sparse, local/hypergraph, delayed, lossy, bandwidth-limited; distinguish explicit messaging from shared environment channels.
- **Population:** homogeneous, role-specialized, mixed capability, unfamiliar partners, entry/exit and dropout.
- **Incentives:** aligned, partially aligned, private costs, free riding and coordinated deviations where meaningful.
- **Reliability:** tool errors, ambiguous completion, malformed handoffs, stale artifacts and recovery.
- **Adversarial robustness:** corrupted peer messages/tool outputs and contaminated shared memory, with clean-task controls and attack budgets. TAMAS motivates this axis; ordinary packet loss is not an adversarial-security result.
- **Generalization:** new seeds, new task structures, larger scale, changed tools, partner holdout and continual sequences.

Use a manageable factorial or fractional-factorial design. For an initial study, choose three scale levels and three control variants on a fixed set of paired instances. Freeze those choices before evaluation; expand where results expose an unresolved failure mode.

## Reporting and statistical requirements

Report each track separately. A normalized scheduling utility, a binary coding success and a model-judged research score do not become commensurate merely because they all lie in `[0, 1]`.

Predeclare a primary task metric and secondary process metrics. Publish denominators, incomplete runs, budget truncations, infrastructure errors and grading failures. Missing results cannot silently disappear or become a neutral default score. Record evaluator model/version and parsing failures wherever judgment is unavoidable.

Use paired task instances, model settings, and exogenous schedules when possible. Compute intervals over independent tasks/runs; use cluster-aware analysis for continual sequences and repeated measures. Report effect size and uncertainty alongside cost. Do not treat hundreds of messages within one episode as hundreds of independent samples.

For communication effects, compare the same architecture with the relevant communication channel altered. For architecture effects, compare the full systems with resource/access differences disclosed. For economic results, preserve per-agent payoffs; for continual results, preserve ordering and state inheritance. Each supports a different claim.

## Priority and scope

**First integration group:** E1, E2 and E3 provide a strong combination of reasoning, jointly verified artifacts and realistic delegation. Reuse SILO-BENCH, CooperBench and a fully audited enterprise workflow grader. MASEval is worth evaluating as an optional harness integration before duplicating its infrastructure.

**Next group:** E4 and E5 add timing, recovery and decentralized execution; they stress properties that static tasks miss. E6 connects the economic-modeling library when its ledgers and mechanisms exist.

**Distinctive SwarmKit research:** E7 and E8 test collective discovery and reusable knowledge. They align closely with this repo but require stronger leakage controls and transfer verification than a normal one-episode benchmark.

**Optional microdiagnostics:** a constrained word grid or puzzle box can isolate feedback, information partitioning, and causal experimentation. They are outside the eight primary tracks and should not dominate the suite or be presented as the direction established by the broader literature. Their inclusion is useful only when tied to a specific failure hypothesis.

The acceptance gate for any future adapter or native task is: a correct oracle/known-good artifact passes; a deliberately wrong result fails; privacy/permission boundaries hold; simultaneous semantics are tested where applicable; setup and grading errors remain visible; and the documented controls can actually be run. Source download and a plausible task description do not satisfy this gate.
