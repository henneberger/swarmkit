# Reassessing the swarm discovery experiment

The Enron email experiment should discover interesting developments as events unfold: explanations that connect dispersed facts, hidden dependencies that change what an event means, contradictions between people's accounts, and consequences that are not apparent from individual messages. Tacit knowledge can contribute to those discoveries. Extracting generic unwritten rules is not an adequate objective.

The current implementation optimizes the wrong unit of work. It is a chronological sample-review pipeline with genuine peer messages, but its agents do not control which investigation to pursue, whom to recruit, how deeply to investigate, or when an unresolved question deserves renewed attention. More careful quotation handling cannot repair that mismatch.

**The paid experiment is stopped and the shared API gate is paused.** The existing runner is retained as a fixed-schedule baseline. The architecture below is a reassessment and proposed replacement, not an implemented or validated discovery system.

## 1. The mistake was architectural

The pipeline selects 32 documents from a window of up to 22,000 arrivals, divides them among four fixed perspectives, gives each peer an observation turn and a revision turn, and asks for a conditional practice. Its sampling, role prompts, schedule, retrieval allowance, and output shape all push toward the same outcome: plausible generalizations from scattered examples.

That is roughly one initially selected message per 688 arrivals. The number of searchable messages was much larger than the number inspected. More importantly, a random set of different messages is not a coherent developing situation. A subject-diversity cap can suppress exactly the repeated discussion needed to understand an objection, a promise, a response, and a consequence. Deduplicating content is useful, but a familiar warning reaching a new audience can be a new event even when its text is unchanged.

The four perspectives—routines, expectations, expertise, and contrasts—do not create four bodies of expertise. Samples change between windows, while peer broadcasting and centrally exposed hypotheses rapidly make the agents' visible material similar. Their next actions remain prescribed. This tests a particular review workflow, not the self-organization and collective exploration emphasized in the research.

The output requirement then makes matters worse. A request becomes a supposed norm. Missing context becomes a supposed informal understanding. A source that expresses uncertainty becomes evidence that a decision was made. Adding an uncertainty paragraph does not rescue an overbroad assertion. Requiring two segment families does not establish two independent episodes or make an explanation interesting.

Several diagnostics made these failures visible. The first small replay produced six card revisions representing only two mostly explicit instructions. Later tests improved source binding but still inferred actual deference where a discussion showed no final decision, shared understanding where someone requested clarification, and absence of formal assignment from absence of assignment evidence. These are documented in the [grounding review](notes/chronological-small-grounding-review.md) and [discovery reassessment](notes/SWARM_REASSESSMENT_DISCOVERY.md).

The engineering controls solved real problems: attribution, temporal access, citation identities, continuation reads, and API accounting. But citation acceptance, advancing the archive cursor, and producing well-formed cards became proxy goals. None measures whether the swarm learned something worth following.

## 2. What the research actually says to build around

### Complementary information about the same unresolved matter

HiddenBench separates individual reasoning from collective reasoning by distributing facts needed for a common decision. Its failure mechanism is not lack of personas: participants fail to elicit information others possess and converge prematurely on shared evidence. Its Exchange-then-Decide intervention asks for relevant facts and a reason the leading interpretation could be wrong before commitment. The protocol is a bounded intervention on a defined decision, not a recipe for broadcasting unrelated mail.[^hidden]

The implication for email discovery is to create an actual reason to consult another agent. One agent knows a commitment; another knows a constraint; another has seen a downstream result. An inquiry connects those pieces. Communication should change the next search or the explanation, not merely supply another opinion.

### Agents controlling the work and their collaborators

AgentNet includes execution, decomposition, forwarding, and local trajectory memory. The relevant idea is that an agent can recognize that another participant's experience is needed and route part of the work accordingly. Assigning a fixed “expertise” reviewer to every batch is not that mechanism.[^agentnet]

SwarmSys similarly motivates adaptive allocation through task/agent profiles and contribution traces. Its methods should not be reduced to adding a numerical “pheromone” field to a forum. A trace must influence where work goes, and its reinforcement needs a defensible connection to a useful result.[^swarmsys]

The replacement therefore needs action-capable agents, an evolving record of who has seen what, and temporary inquiry teams. The controller should enforce budgets and information boundaries. It should not prewrite the substantive workflow for every situation.

### Persistent work that other agents can use

SwarmWorld evaluates persistent executable artifacts under a simulator after their creators are removed, and compares interacting societies with isolated search. It reports benefits that depend on the outcome and timescale; interaction is not universally superior at producing the strongest individual artifact. Its key lesson is to distinguish social activity from an independently useful result.[^world]

An email archive does not supply the same deterministic evaluator. That limits the analogy. A persistent forum is still useful if a question, failed search, evidence trail, or contextual explanation changes another agent's actions. A reusable investigative procedure needs a separate transfer test. Merely storing a persuasive rule does not establish collective knowledge.

Research-swarm examples make the distinction tangible. Anthropic's weak-to-strong researchers shared experimental findings and code while preserving different search directions. EinsteinArena's construction account describes peers improving a concrete geometric candidate through repair and verification. These are inspectable objects whose improvement can be measured; neither example by itself supplies a clean causal estimate of communication's benefit. They motivate exchanging incomplete work that a peer can extend, rather than exchanging only finished prose.[^researchswarms]

The Moltbook research adds a related warning: social-network affordances can produce large amounts of posting without sustained reciprocal engagement. A forum matters here only if agents return, answer particular questions, revise their positions, and carry unfinished work forward.[^molt]

### Communication as a scarce, purposeful action

GPTSwarm and AgentPrune show ways to optimize or reduce communication structure against task objectives. They do not supply an objective for interesting discovery. Learning topology now, using card counts or agent-rated novelty as the reward, would optimize the wrong behavior faster.[^gptswarm][^prune]

The first useful communication policy is simpler: speak when a new fact, contradiction, missing premise, or request is relevant to a specific recipient's investigation. Preserve some exploratory encounters so existing interests do not become a closed loop. Do not reward agreement or message volume.

## 3. Interestingness is a change in understanding

An interesting lead has an explanatory gap with possible consequences. Resolving it could change expectations about an outcome, a dependency, an actor's knowledge, or what happens next. It has something to investigate: another account, a missing step, a version difference, a later outcome, or a competing explanation.

This should not become a numerical “interestingness score” invented by the same model that proposes the lead. The agent should explain why the gap matters and what would make it mundane. Those reasons can be inspected and compared with what subsequent investigation delivers.

A commonplace process can be interesting when its failure reveals a hidden dependency. An unusual email can be irrelevant. A striking single event can justify opening an inquiry without already supporting a general rule. Fraud is neither the target nor a required outcome. A benign explanation that overturns an attractive theory is useful progress.

Three examples from the diagnostics illustrate the difference. They are examples for evaluating the design, not topics to seed into a fresh replay:

- **A correction that can erase itself.** A surfaced meter-data exchange describes missing upstream values becoming zero, downstream estimates replacing them, and a later refresh overwriting a correction. “Staff use informal overrides” misses the point. The interesting possibility is that systems disagree about which value is authoritative, so a reported repair can be undone by normal operation. The inquiry should establish the reported sequence, downstream effect, and whether a durable fix follows. Source: `mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf`; see the [source-specific review](notes/SWARM_REASSESSMENT_DISCOVERY.md).
- **Ready in one sense, blocked in another.** A clearing discussion juxtaposes finalized legal documents with uncertainty about the operating clearing arrangement. “People prefer familiar vendors” invents the explanation. The live question is whether legal and operational readiness have diverged, or whether the apparent conflict is merely administrative. Source: `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`.
- **Ordinary scheduling.** A visitor and host adjusting dates around their travel does not, by itself, imply an organizational priority rule or a hidden power dynamic. It normally deserves no investigation unless later context changes its significance. Source: `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`.

Tacit knowledge becomes useful when it explains such a situation: an unstated meaning of “ready,” knowledge of which system overwrites which field, or a dependency participants assume others understand. It need not be reformulated as a universal procedure. The explanatory contribution, its scope, and its consequences matter more than the label.

## 4. The replacement unit is an ongoing inquiry

An inquiry begins with a question, not a required conclusion. It persists across arrivals and can remain unresolved, split into alternatives, merge with another inquiry, or close as uninteresting.

Its working record contains the bounded situation, the observations that opened it, competing explanations, missing premises, what each participant has contributed, the next action worth taking, and what evidence would change the current view. Requests, promises, actions, and outcomes remain separate. Negative evidence is limited to what a defined search could reasonably reveal.

The swarm's primary actions should be substantive:

| Agent action | Purpose |
|---|---|
| Open or join an inquiry | Identify an explanatory gap or contribute relevant experience |
| Ask a particular peer | Obtain a missing fact, context, or alternative interpretation |
| Follow an episode or read a source fully | Recover the sequence needed to understand an event |
| Search a rival explanation | Test a different mechanism rather than perform ceremonial dissent |
| Connect two inquiries | Propose a source-backed dependency that changes both accounts |
| Set a watch and suspend work | Wait for a relevant arrival instead of paying for repetition |
| Revise, split, or close an inquiry | Record an actual change, including a mundane resolution |

These are proposed action affordances, not commands that every agent must execute in a fixed order. Agents should choose their work within bounded budgets. Independence should be protected long enough for complementary views to develop. The common board should expose useful questions and evidence trails, not force all agents to ingest the same last twelve hypotheses.

Agents can hold overlapping but different histories, with a lightweight directory of topics and episodes they have actually inspected. Such coverage is not automatically expertise. Peer recruitment begins with a concrete question; later evidence of useful contributions can refine routing. A three-agent inquiry team can form and dissolve while another agent continues exploring.

A minimal illustrative sequence is: an agent notices a commitment that seems inconsistent with a constraint; a second agent supplies an earlier qualification; a third checks whether the qualification applies to this version; a later email changes the interpretation. The record should show who supplied which piece and what action it caused. That sequence, rather than four reformulations of the same message, is the mechanism to test.

## 5. Chronology should create evolving investigations

Chronological admission remains essential, including exact same-timestamp ordering and the rule that a forwarded message becomes available only when its outer message arrives. Source retrieval, continuation reads, and every peer contribution must respect the current observation boundary.

But the clock should not force an inquiry to stop after one lookup. Give the swarm a bounded action allowance between advances. It may spend several actions on a promising question, spend none on an uneventful batch, or suspend work until a relevant reply arrives. Later messages can reactivate old questions through thread continuity, participants, referenced objects, or explicit watch conditions.

Cheap sensing should serve two channels: continuity for ongoing inquiries and exploration for new ones. Content deduplication should not erase transmission events. Random sampling can remain a neutral exploration channel, but it should not determine nearly all attention.

The next experiment should use a manageable, coherent chronological slice, selected without known-case labels or future outcome knowledge. Reading a connected slice well is more informative than advertising half a million searchable emails while inspecting scattered fragments. The selection rule and actual inspected coverage must be reported. Using future communication structure to choose the slice would itself introduce leakage and must be avoided.

No historical replay can erase the model's prior knowledge of Enron. Its claims must remain grounded in available sources, and any early-warning interpretation needs additional controls. This is a limitation of the setting, not a reason to turn the experiment into generic rule extraction.

## 6. Allocate the budget to unanswered questions

Keep the existing atomic provider gate. Change the policy above it.

There should be no obligation to give every peer a turn on every arrival window. A request for computation should identify the inquiry, the action, the evidence it seeks, and what the result could change. The controller can enforce per-inquiry ceilings, concurrency, an exploration allowance, and a shared total. It need not decide the answer.

A missing source continuation may be worth more than another model discussion. A specific peer request may be worth more than broadcasting a summary. An inquiry with no feasible discriminating step can wait. A well-supported contradiction can justify deeper work. These are transparent allocation heuristics initially, not calibrated expected-information-gain estimates.

A candidate's self-rated significance must not purchase unlimited calls. More participants, more revisions, and longer discussion are costs unless they produce useful evidence or a change in understanding. Failed investigations and abandoned leads stay in the ledger and report.

Malformed model output should remain a recorded abstention, with usage accounted. Provider, budget, and source-boundary failures still require the existing conservative controls. Those mechanisms are infrastructure; they are not the discovery objective.

## 7. Use the library where its contract fits

The library already contains relevant mechanisms. Adding all of them would not make the system a better swarm.

| Existing component | Appropriate use and limit |
|---|---|
| `SwarmRuntime` and `MessageBus` | Execute selected participants and addressed exchanges. Shared runtime artifacts are public; private inquiry state needs explicit handling. |
| `CapabilitySuccessRouter` | Route a concrete request using relevant coverage and exploration. Its success feedback needs a real application signal; agreement is unsuitable. |
| `EvidenceRegistry` | Preserve ancestry and avoid counting copied sources repeatedly. It does not establish truth or semantic independence. |
| `InformationGate` and `EvidenceCompressor` | Send relevant changes and bounded evidence packets. Belief-change gating requires stable alternatives; card limits alone do not limit tokens. |
| `FeedPolicy` and an inquiry board | Make unfinished questions and relevant contributions discoverable. Popularity should not become evidence strength. |
| `DAGExecutor` | Execute a proposed dependency frontier, such as inspecting two versions before comparing them. It does not invent the inquiry. |
| `ArtifactStore`, `PeerAdoption`, `ProcedureAbstraction` | Preserve and test reusable methods after there is something substantive to transfer. Quote validity cannot stand in for procedure utility. |
| `StigmergicPolicy` | Reinforce useful, evaluated artifacts through persistent traces. Its current verified-artifact contract is not a license to mark speculative theories true. |

The main missing component is an inquiry agenda connected to agent-chosen actions. Learned topology, generalized reputation, and latent communication should wait until useful interaction can be observed and evaluated. The [pipeline audit](notes/SWARM_REASSESSMENT_PIPELINE.md) maps the concrete APIs and limitations.

## 8. Show that the interaction mattered

The first milestone should be one convincing unfolding inquiry, not another full-corpus run or a larger number of cards. It should show distinct contributions, a changed search or explanation caused by communication, and an outcome or unresolved prediction that is correctly scoped.

Use controls to diagnose the mechanism while keeping the project focused on swarms. Compare an interacting population with independent investigators plus aggregation and a budget-matched persistent investigator. Count retrieval exposure, repeated context, synthesis, and failed work. A separate equal-evidence comparison can distinguish better search from better integration.

For a promising result, remove or delay the peer message said to be decisive. Does the recipient still find the connection? Substitute a duplicate or irrelevant message. Does confidence rise anyway? Swap which peer initially holds a fact. These tests can reveal whether the system combines knowledge or merely gives one agent more context under an elaborate interface.

Interest and support should be reviewed at the original discovery cutoff; later outcomes are evaluated separately. A successful benign resolution, a corrected inference, or an abandoned attractive theory can count as progress. A copied claim, invented motive, or unchanged paraphrase cannot. Synthetic exercises can test coordination mechanics, but they cannot demonstrate that the real archive produced an interesting discovery.

A full benchmark is not required before an exploratory prototype becomes useful. But a claim of swarm advantage requires evidence beyond an appealing narrative. The first small comparison should expose failure, not provide another activity metric to optimize.

## 9. The interface should display developing understanding

The main view should be a small portfolio of live questions. Each shows why it matters, the competing explanations, the latest evidence that changed the account, who is investigating which gap, and what would resolve it. A chronological history preserves initial interpretations, peer challenges, surprises, revisions, and closures.

For example, the visible progression might be: “apparently ready”; “another agent found an unresolved dependency”; “two explanations remain”; “a later reply resolves the naming issue”; “closed as administrative.” This is intellectual progress even though it produces no dramatic allegation or generalized rule.

A forum supplies the interaction surface, and a wiki can preserve the best current account. Neither should bury the interesting developments under every model utterance. API counters and quotation audits belong in an inspection layer. The front page should answer what the swarm is trying to understand and what changed.

## 10. Immediate disposition

Retain the temporal source service, attributed email parsing, stable source references, continuation access, budget gate, and diagnostic history. Demote the current fixed-review runner to a baseline. Remove compulsory unwritten-rule output, fixed all-peer spending, arbitrary global hypothesis sharing, and card counts as indicators of discovery.

The proposed replacement is a small, persistent, agent-directed inquiry swarm. Its defining feature is that agents can change one another's investigative trajectory while preserving different knowledge and competing explanations. The next implementation milestone is an inspectable example of that mechanism on a neutral chronological slice.

No replacement run has been started. At the pause checkpoint, the shared ledger recorded **343 provider attempts and $2.19260096** in conservative accounting, with no active calls. The latest interrupted run is preserved as a [stopped baseline](reports/CHRONOLOGICAL_STOPPED_BASELINE.md). Its engineering progress is not presented as proof of interesting discovery.

## Sources

[^hidden]: Li, Naito, and Shirado. [Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs](https://arxiv.org/abs/2505.11556v4), especially Section 6.4. [Archived text](sources/papers/2505.11556/paper.txt). The intervention is evaluated on bounded decision tasks; transferring it to open-ended email discovery is a design hypothesis.

[^agentnet]: Yang et al. [AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2504.00587v2). [Archived text](sources/papers/2504.00587/paper.txt). Relevant mechanisms include local routing/execution memory and decentralized task action.

[^swarmsys]: Li et al. [SwarmSys: Decentralized Swarm-Inspired Agents for Scalable and Adaptive Reasoning](https://arxiv.org/abs/2510.10047v1). [Archived text](sources/papers/2510.10047/paper.txt). The library's numerical trace policy is an adaptation, not a reproduction of the paper.

[^world]: Pal, Wang, and Buehler. [SwarmWorld: Stigmergic technological evolution in societies of language-model agents](https://arxiv.org/abs/2608.26081v1), especially Sections 2.1–2.2. [Archived text](sources/papers/2608.26081/paper.txt). Preprint evidence from a simulated construction environment, not email analysis.

[^molt]: Zerhoudi et al. [Form Without Function: Agent Social Behavior in the Moltbook Network](https://arxiv.org/abs/2604.13052v1). [Archived text](sources/papers/2604.13052/paper.txt). Observational evidence about a particular platform, not a causal test of this proposed swarm.

[^gptswarm]: Zhuge et al. [GPTSwarm: Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823). [Method catalog](docs/METHODS.md). Graph optimization requires an evaluation objective supplied by the application.

[^prune]: Zhang et al. [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2410.02506v1). [Archived text](sources/papers/2410.02506/paper.txt). Communication sparsification does not itself define useful discovery.

[^researchswarms]: Anthropic, [Automated weak-to-strong researcher](https://alignment.anthropic.com/2026/automated-w2s-researcher/) ([archived post](sources/posts/anthropic-w2s/page.txt)); Together AI, [EinsteinArena](https://www.together.ai/blog/einsteinarena) ([archived post](sources/posts/einsteinarena/page.txt)). See the [independent primary-source reassessment](notes/SWARM_REASSESSMENT_RESEARCH.md) for implementation anchors and evaluation limitations.
