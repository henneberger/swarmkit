# Small-swarm mechanisms for unspoken knowledge in an email corpus

Design proposal, not an analysis of Enron emails. No findings about any person or transaction are asserted. The research basis is evidence-first exchange, measured peer uptake and verified artifact reuse in `SWARMS_REPORT.md`, particularly [HiddenBench](https://arxiv.org/abs/2505.11556v4) and [SwarmWorld](https://arxiv.org/abs/2608.26081v1).

## What can actually be discovered

Separate three outputs: **documented fact** (an attributed statement exists in a specific email), **inferred practice** (a recurring approval shortcut or implicit division of responsibility), and **investigative hypothesis** (a pattern may indicate concealment or misconduct). An email’s assertion is not automatically a true external event. Human tacit experience absent from the archive cannot be recovered merely by adding agents. A swarm can expose distributed traces and propose explanations whose assumptions and missing evidence remain visible.

## Four peers with independent search and shared tests

Seed four perspectives: temporal inconsistencies; transaction/commitment discrepancies; informal routines and authority; benign alternatives and disconfirmation. These are starting search biases, not exclusive roles or sequential handoffs. Each peer independently chooses leads, searches accessible source material, requests facts from others, and forks/retests published artifacts. Rotate perspectives between episodes to avoid a permanent prosecutor/defender split.

Each lead begins with independent observations before peers see one another’s conclusions. A card includes immutable message identifier, quoted span, timestamp, thread ancestry, observation versus interpretation, proposed explanation, and a concrete falsification query. Prefer a few high-information cards to full transcripts. Preserve disagreements as search requests: “Find an earlier authorization,” “Find routine examples using this phrase,” or “Check whether later messages correct the figure.” Retrieval partitions are exploration seeds; peers may request cross-partition evidence, with those disclosures logged.

Run two exchange rounds, each requiring a new factual observation and an objection to the leading explanation, followed by a provisional decision: investigate further, adequately explained, or unresolved. A peer can reopen a decision with new evidence. Four agreeing agents repeating one message provide one evidential origin, not four corroborations. Use root message/event ancestry to track copies and forwarded text; do not assume different mailboxes imply independent sources.

## Discovering implicit practices through contrast and testing

**Hypothetical example only:** a formal approval is consistently dated after operational action. One peer identifies timing; another finds repeated transactions; a third infers an informal preapproval practice; the fourth searches for ordinary retrospective paperwork and delegated authority. The output is a testable practice hypothesis with counterexamples, not “fraud found.”

Translate candidate practices into executable retrieval or measurement procedures: compare action/approval dates, classify stated exceptions, or count who requests versus grants permission. Each procedure declares observable inputs, missingness rules, alternative explanations and its intended population. Another peer reruns it on unseen threads and time periods. Only validated procedures enter the reusable library; unsupported interpretations remain provisional. Absence of an email counts as missing evidence unless archive completeness supports a stronger conclusion.

## Evaluation and implementation boundaries

Compare identical retrieval/token budgets: one investigator; four isolated investigators with merged results; and the communicating swarm. Blind reviewers assess attributable evidence, substantive novelty, alternative explanations and false-positive investigative leads. Separately measure private-fact exposure, recipient uptake, source-independent support, retained procedure performance and time to a useful lead. Temporal holdouts must separate whole threads and forwarded duplicates, not random email rows. Include benign matched cases, missing-context cases and planted synthetic contradictions; historical outcome labels must be withheld from discovery and reviewed for hindsight leakage.

Use `ExchangeConfig(delivery='inbox')` when testing restricted routing; default `all_peer` deliberately bypasses sparse transport. `EvidenceRegistry` deduplicates supplied ancestry but cannot authenticate sources. Replace `evidence_decision` with an evidence-grounded adjudication callback: source scores and `WeightedConsensus` are not fraud probabilities. `ArtifactStore.verified` should mean passed declared checks, never established wrongdoing. `PeerAdoption` supports local retesting/rollback; `ProcedureAbstraction` checks declared held-out IDs but cannot detect semantic leakage. Preserve original evidence indefinitely; apply `DecayingMemory` only to revisitable working summaries and stale leads.
