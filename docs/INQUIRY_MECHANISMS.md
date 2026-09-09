# Inquiry swarm: research mechanisms and implementation limits

The current inquiry system is a **research-inspired prototype, not a reproduction of a demonstrated discovery swarm**. It replaces compulsory interpretations of unwritten routines with investigator-chosen questions, targeted requests, source inspection, competing explanations, watches, and closure. These affordances permit collective investigation; they do not establish that the agents choose useful investigations or outperform one investigator.

This mapping covers [`InquiryAgenda`](../src/swarmkit/enron/inquiries.py), [`InquiryReasoner`](../src/swarmkit/enron/inquiry_model.py), and their immediate dependencies. It distinguishes code actually composed into this path from methods merely available elsewhere in the library.

## Complementary facts: adapted from HiddenBench, not reproduced

HiddenBench deliberately distributes complementary information about the **same decision**. Its v4 Exchange-then-Decide intervention requires two rounds of relevant fact disclosure and objections before deciding. On the 18-task intervention subset, GPT-4.1 accuracy rises from .037 to .800; mechanically revealing information reaches .926 in the separate Reveal-All experiment. These results identify information surfacing as a major bottleneck under that benchmark's construction. They do not show that unrelated private email samples create useful complementarity. [Primary paper, §§6.3–6.4, Tables 6–7](https://arxiv.org/abs/2505.11556v4); [archived text](../sources/papers/2505.11556/paper.txt).

The inquiry path **adapts active probing**: `request_peer` sends a specific question, queues work for a recipient, and permits a reply carrying previously private evidence. `revise` produces a new artifact version and an addressed result for participants. `InquiryReasoner` resolves citations only from supplied source spans and retained or delivered evidence. `InquiryAgenda` separately accepts source-validity and optional actor-exposure callbacks; source validity alone does not establish private accessibility.

The library's [`ExchangeThenDecide`](../src/swarmkit/deliberation.py) is **not called** by the inquiry path. That symbolic protocol requires `Task.candidates`, enforces exchange rounds, and offers an inbox mode respecting delivered evidence. Open-ended inquiry has neither predetermined answers nor a mandatory decision phase. The runner now provides a bounded directory of sender/subject coverage from sources each peer was actually shown. This makes possible partners visible without publishing their full evidence. Whether the agents use that directory to recognize a missing constraint remains unproven.

## Routing: actual reuse, with substantial AgentNet omissions

`InquiryAgenda` directly uses [`CapabilitySuccessRouter`](../src/swarmkit/topology.py), an AgentNet-inspired approximation. It scores available peers using capability-set overlap and a sender–recipient success estimate, excluding existing inquiry participants when automatically recruiting a new peer. The default agenda sets exploration to zero. Explicit recipients bypass this choice.

AgentNet's primary design combines local routers and executors, success-weighted connections, and retrieval of relevant local trajectory fragments. Equation 2 updates connection weights from task success; Equation 4 retrieves semantically relevant prior fragments. [Primary paper](https://arxiv.org/abs/2504.00587v2); [archived equations and Algorithm 1](../sources/papers/2504.00587/paper.txt).

Our router substitutes set overlap for richer task/capability matching and exposes an EMA `record()` method. **The agenda never calls `record()`**, so new inquiries do not teach it successful routing. Its central scheduler also differs from AgentNet's decentralized execution. `InquiryReasoner` retains a rolling summary and at most 32 evidence items, presenting at most 16 remembered items; this is not AgentNet's relevant successful-trajectory retrieval. A plausible reply, agreement, or longer discussion is not a valid success reward. Any future update needs an independently assessable outcome, such as supplying the requested missing source, with broader explanatory success evaluated separately.

## Persistent artifacts: a shared workspace, not demonstrated stigmergic discovery

Each accepted change creates a canonical `Artifact` with a parent version, evidence, rivals, outstanding actions, and status. The scheduler revisits inquiries and reserves periodic exploration. Literal watches wake owners when matching arrived evidence appears, deduplicating by source family unless occurrence tracking is explicitly requested. These are concrete persistence and coordination mechanisms.

SwarmWorld's stronger mechanism has persistent, spatially situated artifacts that change a deterministic environment encountered by later agents. Frozen technological portfolios face unseen disturbances after agents are removed. Its ablations separate communication, inheritance, physical stigmergy, and isolated search; shared worlds improve several portfolio/resilience outcomes without universally producing the best individual artifact. [Primary paper, §§2.1–2.2](https://arxiv.org/abs/2608.26081v1); [archived text](../sources/papers/2608.26081/paper.txt).

Our artifacts alter a shared investigative workspace, so they can support indirect coordination. They do **not** yet provide SwarmWorld's environmental consequences, executable inheritance, or held-out functional evaluation. The path stores artifacts directly and marks `semantic_validation=False`; it does not compose the library's [`ArtifactStore`, `PeerAdoption`, or `ProcedureAbstraction`](../src/swarmkit/knowledge.py). Exact source checking verifies a quotation, not an explanation. Closing an inquiry is an agent action, not an independently established resolution.

## Selective communication: no entropy inferred from prose

The reasoner chooses one action and can wait; addressed questions and watches avoid compulsory all-agent discussion. This is qualitative selectivity. The numerical entropy-delta gate in *The Cost of Consensus* operates on explicitly defined probability distributions in a search simulation. [Primary paper](https://arxiv.org/abs/2605.06988v1); [archived protocol definitions](../sources/papers/2605.06988/paper.txt).

The library's [`InformationGate`](../src/swarmkit/communication.py) supports probability-vector change tests, but the inquiry path does not use it. Prose confidence, unfamiliar wording, and a new source identifier are not calibrated entropy or expected information gain. Likewise, the agenda's least-recently-served scheduling is fairness under budgets, not learned allocation by discovery value.

## Two concrete improvements and the experiments they require

1. **Test missing-information recruitment.** The runner provides a bounded, arrival-safe source-coverage directory and public inquiry questions, without disclosing private facts wholesale. Requests should identify a missing constraint and the rival explanations an answer could distinguish. Compare this against random routing, identical-context peers, and automatic aggregation of all retrieved evidence. This tests whether targeted exchange contributes beyond parallel retrieval.
2. **Make checks and their outcomes reusable.** Replace free-text `next_actions` alone with versioned check records: competing implications, proposed query/read, observed result, source context, and remaining ambiguity. Permit another investigator to execute or repair a check. Reward source acquisition only after exact verification; judge substantive resolution separately. Compare shared check histories against summary-only memory and independent histories.

Before claiming collective gain, also compare equal total tokens, calls, source access, and memory against a strong single investigator and independent investigators pooled only at evaluation. Withhold individual peer replies to test whether they change later actions and supported conclusions; disable watches to measure discovery delay. Use blinded judgments and held-out episodes, not artifact counts.

The `--withhold-peer-exchange` condition retains public questions and coverage but hides peer messages and merged inquiry context from the reasoner. It is a communication ablation, not the fully isolated control described above.

The [fictional inquiry scenario tests](../tests/test_inquiry_discovery_scenario.py) already establish routing, exposure, watch, and temporal plumbing with a scripted reasoning policy. **They do not demonstrate LLM discovery, semantic entailment, interestingness, or a swarm advantage.** Those remain empirical questions.
