# Proposed Enron small-swarm integration

Reviewed current `README.md`, `docs/API.md`, and actual runtime, deliberation, knowledge, and canonical types. The library supplies coordination mechanisms; the following application integrations are **proposed, not implemented**.

## Four-agent pipeline

Use four `AgentState` records and `CallableAgent` callbacks under `SwarmRuntime`: a chronology investigator, commitments/transactions investigator, contradiction/context investigator, and synthesis/checking investigator. Give investigators distinct initial mailbox/thread partitions and bounded read-only retrieval adapters. Keep the common question in `Task`; pass private retrieval access through application-owned adapters, not public task metadata. All four should contribute evidence and challenge premises; the fourth should not receive an omniscient shortcut to everyone’s private material.

Run explicit phases: independent retrieval/extraction → evidence-card exchange → targeted follow-up and counterexample search → claim-by-claim checking → synthesis. Each callback returns canonical `Evidence` inside `Message`, local `memory_updates`, and measured `Usage`. Context mutations alone do not persist. `CompletionAgent` retains delivered evidence between phases, but its free-text exploration does not extract structured evidence or check entailment; a custom adapter is required.

Start with `MessageBus(FullTopology())` and explicit disclosure limits, then compare ring or selective routing. `ExchangeThenDecide(ExchangeConfig(delivery="inbox"))` can support finite hypotheses after extraction. Its default **`all_peer` uses a public board independent of bus topology**; a sparse bus around that default does not preserve partition visibility. Inbox mode also needs supporting ancestry delivered explicitly. Default scoring is symbolic candidate support, not reading comprehension. Open-ended investigation requires custom claim generation/checking and an “insufficient evidence” outcome. `WeightedConsensus.aggregate` combines existing decisions; agreement does not verify claims. Runtime phases and symbolic `Pipeline` are distinct execution paths; avoid duplicate commits/time increments.

## Missing data and evidence integrations

Implement a deterministic email loader and read-only search index with partition filters, thread expansion, query/result limits, and retrieval logs. No corpus loader, lexical/vector index, provider client, email parser, or document-level access enforcement currently exists.

Proposed application document schema: dataset version; original locator; raw and normalized hashes; Message-ID; original/normalized timestamp and timezone; participants; subject; thread references; duplicate-copy identifiers; body spans; quoted/forwarded regions; attachment availability. Keep canonical `Evidence`; place document ID, exact quote and offsets, retrieval query, access scope, extraction model/version, and observation-versus-inference status in metadata. Derived cards use `parents`; artifacts enumerate claims, supporting IDs, counterevidence, missing premises, and uncertainty.

**Source roots are strings, not evidence IDs.** `EvidenceRegistry.roots()` returns root `Evidence.source` values and collapses repeated support from the same root. Canonicalize copies of one original email and repeated quoted passages to their underlying source family; do not treat every mailbox path, extractor, or forwarded copy as independent. Conversely, assigning the whole corpus one source destroys useful distinctions. Message-ID requires fallback/deduplication rules. The registry validates ancestry but cannot authenticate attribution or detect semantic correlation among different emails.

## Verification and privacy boundaries

Build a verifier that resolves every citation against immutable documents, checks exact spans, assesses entailment and counterevidence, and flags temporal/entity ambiguity. Return `Feedback` with explicit check results. “Verified” must mean these stated checks passed, not proven motive or causation.

`ArtifactStore.admit()` rejects failed verification, but is separate from runtime storage. The runtime verifier merely annotates artifacts; failed artifacts still enter public state. Add an application admission step before publishing accepted artifacts. **Every runtime agent receives every `state.artifacts` item and the complete task**; private cards must remain in local evidence/memory or addressed messages. Checkpoints contain private material. These are logical boundaries, not an execution sandbox.

Treat email bodies as untrusted data. Use quoted typed retrieval results and bounded read-only tools; never execute instructions, links, or attachments because an email requests it. Prompt wording alone is insufficient isolation.

Evaluate against matched independent investigators with equal retrieval/token budgets: citation validity, supported-claim precision, private-evidence contribution ablations, and deduplicated thread/time-held-out transfer. `private_evidence_recovery` measures exposure only; it does not establish understanding or discovery.
