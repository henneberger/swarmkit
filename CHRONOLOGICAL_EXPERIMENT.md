# Chronological swarm experiment: uncovering tacit knowledge

The experiment asks whether a small communicating swarm can reconstruct **unwritten routines, implicit expectations, informal expertise, and context-dependent exceptions** as organizational messages arrive. Finding fraud is not its assigned objective. A useful discovery explains how work appears to get done, under what circumstances, and what evidence would contradict that explanation.

This is an accelerated historical replay of the Enron corpus, not a live deployment or a validated prediction of historical events. Models may already know Enron from training; restricting retrieved information cannot erase that prior knowledge. Every reported archive claim must therefore cite text available at its recorded discovery time.

## What earlier experiments taught us

The [retrospective pilots](reports/EXPERIMENT_FINDINGS.md) showed why source attribution, selective retrieval, and skeptical exchange matter. A forwarded discussion can contain several different speakers and dates; repeated forwarding does not create independent support. A question about a requirement does not establish a policy. Agent agreement and valid quotations do not establish a useful general rule. Those pilots also spent repeated rounds restating uncertainty instead of resolving it.

This replay starts with fresh agent memories and no case-specific queries, prior findings, or previous wiki. The earlier results inform engineering controls, not the swarm's evidence or target list. It uses the same shared evidence types, parsed message segments, persistent API gate, and source inspection UI.

## Observation protocol

1. Use the immutable downloaded corpus identified in [the corpus manifest](reports/CORPUS_MANIFEST.json). Admit outer messages in ascending parsed UTC date, then document ID. This deterministic tie break represents simulated observation order; an email header is not proof of delivery time.
2. The principal replay window is January 1, 1999 through December 31, 2002. This covers 516,182 of 517,401 records. Report the 1,219 records outside that window separately; do not silently repair their dates or treat all of them as erroneous.
3. Store arrived membership and its exact cursor separately from the master archive. Get, search, source spans, and evidence verification must all reject unseen IDs, including messages sharing the current timestamp but not yet admitted. Search ranking uses arrived-only text statistics.
4. A forwarded original becomes available when the outer message arrives. Its claimed earlier date does not move the discovery backward. Preserve attribution, quote boundaries, and parsing uncertainty.
5. Admit batches without an LLM call per message. Review bounded windows of new material; retain the distinction between messages admitted to searchable history and messages actually inspected by a model. Archive coverage is not inference coverage.

## Swarm method

Four peers bring complementary perspectives to the same evolving task: reconstruct routines, recognize contextual boundaries and exceptions, connect expertise and dependencies, and challenge explanations. Each can request relevant context from arrived history. Their observations are exchanged between turns; within a turn, peers reason from a snapshot rather than seeing a later peer's answer before writing their own.

The revised protocol distinguishes explicit observations from candidate tacit hypotheses. A candidate needs at least two distinct segment-origin contexts and an explicit inference gap: what remains unstated, and why the contrast implies a conditional practice. Two contexts are not automatically independent episodes. Thin evidence is retained as an observation. Stable span identifiers prevent aliases from changing meaning between rounds; the host checks text and availability, while peer criticism assesses relevance.

A candidate tacit-knowledge hypothesis should identify:

- The inferred unwritten rule or practice, and who appears to rely on it.
- The situation where it applies, with source-backed examples.
- Whether it is explicitly stated, inferred from behavior, or still speculative.
- Exceptions, contradictory examples, and ordinary alternative explanations.
- The next discriminating retrieval query, and a prospective prediction when one is justified.

An unchanged claim with the same document spans does not become a new revision merely because new Evidence object IDs were allocated. Repeated observations across distinct episodes are stronger support than several copies of one exchange. A useful query seeks a missing role, exception, resolution, or comparable episode; it does not retrieve the entire archive into every prompt. Memory retains hypotheses and open tests so later arrivals can refine, contradict, or retire them. A chronological revision preserves the previous claim and its original discovery time.

An inferred routine is not automatically recovered human expertise. A genuine transfer test would require using the inferred procedure on a held-out decision task, assessing performance against a baseline, and checking whether the contextual conditions still hold. This experiment reports candidate rules and later evidence; it does not silently substitute citation validity for that test.

## Call and context gates

The replay has two layers of control. A cheap arrival/novelty gate coalesces messages into review windows, avoids repeated body copies, selects a bounded sample, and skips windows without sufficient new material. A run-level ceiling bounds windows, turns, documents, output tokens, and retrieval requests. Periodic review is necessary because novelty heuristics can otherwise miss quiet routines.

Every paid request also passes through the existing SQLite call ledger, shared with all earlier experiments. It reserves estimated input bytes and maximum output at conservative prices before dispatch, limits concurrency and requests per minute, preserves unknown-outcome charges, and stops admissions when a configured allowance is exhausted. Expanding a call allowance is an audited change; it does not reset spending. The planning target remains $10 across experiments, with user-authorized flexibility if needed.

Selection is deterministic and does not use a fraud lexicon, known Enron case names, or retrospective labels. Because only a small sample reaches the model, the report must expose that limitation and avoid claiming exhaustive discovery. The executed full configuration uses 24 windows of up to 22,000 arrivals, 32 selected documents per window split across four peers, and at most two turns per peer/window (192 model calls), with one candidate per call and a 3,000-token output reservation. Each peer can retrieve up to three matching arrived documents for its focused follow-up query. Source text is bounded to 1,600 characters per opened document, and memory is compacted; both choices limit what the model can infer. A practical full replay uses enough windows or batch capacity to admit the entire stated period; stopping early is labeled partial.

## Validation before scale

Offline tests cover exact chronological order, same-time unseen messages, later corrections, late forwards with earlier inline dates, persisted arrival cursors, read-only master access, and the absence of future evidence in retrieval. Engine tests cover bounded calls, duplicate/empty gating, peer exchange, and source selection checks.

A small live replay then checks real provider output, the neutral tacit-knowledge instructions, quotation acceptance, targeted retrieval, actual cost, and chronological export before the full run. If a control fails, fix it and repeat the small test before scaling. Do not read full-run future messages during the small run to improve its results.

## Reporting and interpretation

The result is an append-only chronological account organized by virtual discovery time. Each entry records the observation window, arrived and inspected counts, peer observations, inferred practices, supporting and opposing sources, unresolved tests, and revisions to earlier hypotheses. Wall-clock execution time and virtual archive time are separate.

Evaluate operational success first: no future-access violations, bounded requests, reproducible selection, exact evidence spans, complete stated admission, and useful targeted retrieval. Separately assess substantive quality: whether a hypothesis goes beyond summarizing an email, remains correctly scoped, handles counterexamples, and helps interpret a later episode. Model-written assertions remain provisional until independently reviewed. No swarm advantage, firm-wide rule, wrongdoing, or successful tacit-skill transfer is implied by a completed run.

## Output recovery without extra requests

A large diagnostic exposed a brittle assumption: one model returning a hypothesis object instead of a list stopped all later reasoning. The final v5 controller normalizes compatible singleton collections, then applies the same source and field checks. It never invents missing support. An invalid or truncated model response becomes an explicit abstention with its usage charged; subsequent scheduled windows can continue without automatic repair calls. A finished run with such abstentions is labeled `completed_with_rejections`. API/gate failures and source-boundary exceptions still halt further paid reasoning. Rejected candidate objects and rejected prediction checks have separate counters from whole-turn abstentions and quote failures.
