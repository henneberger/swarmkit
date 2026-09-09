# Validation and experiment log

This log distinguishes engineering checks from evidence of investigative accuracy. No quotation check proves fraud or the truth of an email assertion.

## Small tests before the Enron pilot

1. Offline unit/integration/browser suite: 171 tests passed at this checkpoint. No test-suite API calls.
2. One-call DeepSeek V4 Flash smoke: valid JSON response, 43 tokens, conservative cost $0.00002332.
3. Four-peer, one-round live test on 12 fictional emails: four completed invocations; 12 exact quotations accepted; zero rejected; no peer errors. The peers identified the ordinary emergency-approval explanation.
4. First full synthetic cycle: 24 invocations, 60 accepted and 12 rejected quotations, plus one rejected finding. This exposed cached-evidence handling and citation-ID guidance issues. The real-corpus pilot was held until they were addressed.
5. Corrected full synthetic cycle: 24 invocations, 72 accepted quotations, zero rejected quotations/findings, no peer errors. No candidate cases or knowledge cards were published; this is a valid abstaining outcome on the selected benign example.

At this checkpoint, all paid testing uses one ledger: 53 attempted calls, 577,753 reported/accounted tokens, $0.27769236 at conservative peak prices; no unknown outcomes or active calls.

## Fixes motivated by tests

- A repeated quotation may be reused when that exact span is visible in the current evidence packet. Other unseen text from the same document remains unavailable.
- Findings can reference only IDs in the current prompt's explicit evidence allowlist. Missing documentation alone does not qualify as tacit knowledge.
- Empty corpora stop before paid calls; incomplete or failed peer phases cannot produce a completed status.
- Independent-investigator mode sends no peer messages.
- FTS rank ordering avoids an unnecessary full-match sort; measured query time improved from 6.518 seconds to 0.097 seconds on the growing local index. This is a local observation, not a general benchmark.

The real-corpus experiment and final totals are recorded below after completion.


## Initial real-corpus diagnostic

The first 24-call real-corpus run completed transport successfully but accepted only six quotations and rejected 36; it published no case cards. This is an unsuccessful evidence-acquisition result, not a successful fraud investigation. Peers repeatedly described a valuation-documentation concern without successfully preserving its quotations. The diagnostic is retained in [ENRON_INITIAL_DIAGNOSTIC.md](ENRON_INITIAL_DIAGNOSTIC.md). The next iteration changes citation selection to deterministic, supplied source spans and tests that mechanism before another full run.


## Real-source span test and token gate

A four-invocation real-source smoke test accepted ten source spans with zero rejections. Two subsequent six-round investigations preserved 54 and 60 quotations respectively with zero citation rejections, but the shared conservative token-reservation limit blocked six final invocations. Both runs are correctly marked incomplete; neither published case cards. At that checkpoint spending was $0.82887992 across 123 paid attempts. The gate prevented dispatch before the configured reservation limit was crossed.

The token allowance was explicitly raised from 2 million to 5 million and the call allowance to 240, preserving all counters and the $10 dollar allowance. Before further paid calls, the user requested structured parsing of forwarded/replied email chains. The gate was paused while the parser and prompt representation were revised.

## Structured parsing and completed retrospective comparisons

The parser now partitions decoded bodies into exact attributed segments instead of presenting a forwarded conversation as one speaker. A small real-source retest accepted 11 selected quotations with zero rejections before the completed large pilots. The parsed valuation and EnergyDesk runs used 24 calls each and accepted 69 and 72 quotations respectively, with zero rejected selections. The independent valuation baseline used 24 calls and accepted 67 selections, also with zero rejections. All three completed, but none published formal candidate cards; peer assessments and subsequent reviewer synthesis are distinguished in [EXPERIMENT_FINDINGS.md](EXPERIMENT_FINDINGS.md).

Before the chronological experiment, the shared ledger recorded 203 attempted calls, 3,137,640 tokens, and $1.44371480 at conservative peak/cache-miss rates, with no active or unknown-outcome calls. The new replay raises the operational allowance to 480 calls and 12 million tokens while retaining the $10 dispatch allowance and every existing charge. This is an audited capacity change, not a fresh budget.

## Chronological tacit-knowledge experiment

The new [protocol](../CHRONOLOGICAL_EXPERIMENT.md) starts fresh memories and arrival state. Unlike the retrospective pilots, it supplies no case-specific queries. Its objective is to infer unwritten routines, contextual expectations, expertise dependencies, and exceptions, then revise them as further messages arrive. The archive view uses arrived-only search statistics and exact arrival membership; a late forward cannot expose its text at an earlier virtual time.

The first chronological live smoke test admitted 4,000 messages, exposed 67 distinct documents in model prompts, used 16 calls, and produced 64 mechanically valid citation selections with 15 rejected output items. All 64 emitted selections passed exact quote/hash/arrival-sequence audit. Its six candidate revisions represented only two rules, largely repeating explicit single-email instructions. Independent agent review also found semantic citation misbinding: a correctly quoted Confirmation Desk email was attached to a different Houston-correspondence claim. This demonstrates why temporal and quotation checks cannot certify inference quality. The [diagnostic](CHRONOLOGICAL_SMALL_DIAGNOSTIC.md) is retained; it did not qualify the method for scale.

The next iteration adds stable span identifiers, an explicit inference gap, stronger contrast and scope requirements, meaningful revision deduplication, and schema rejection diagnostics. Marker-free embedded email headers found in the diagnostic also receive a parser regression fix. These are general method changes; the fresh replay receives none of the diagnostic's case-specific findings.

The second chronological prefix test stopped after 12 invocations because three responses exceeded the 1,800-token output capacity and were not valid complete JSON. That run is retained as [CHRONOLOGICAL_TRUNCATION_DIAGNOSTIC.md](CHRONOLOGICAL_TRUNCATION_DIAGNOSTIC.md); no large run followed it. The final small-test protocol limits responses to one concise candidate and reserves up to 3,000 output tokens per request.

The third prefix test completed its planned 16 invocations: 4,000 arrivals, 74 distinct prompt-exposed documents, eight targeted history searches, and 55 accepted quotations with zero rejected citation selections. All 55 passed exact quote/hash/arrival-sequence audit. It cost $0.06941748 in the shared ledger. Three unsupported candidate objects and eleven invalid prediction-check attempts were rejected separately; those do not become knowledge or validated predictions. The status is `partial` because the intentionally small test covers a prefix of the defined period, not because reasoning failed. See [the small report](CHRONOLOGICAL_SMALL.md) and [its audit](CHRONOLOGICAL_SMALL.audit.json).

The result qualifies the mechanism for a broader exploratory replay, not for a claim of recovered tacit expertise. Candidate rules can still overgeneralize from one exchange; distinct segments or outer messages do not automatically establish independent episodes. Cards now expose host-computed source counts alongside the model's interpretation.

A final context-access refinement follows the small-test review: truncated source spans are explicitly marked, and agents can request a bounded continuation at an exact body offset through the same arrived-only corpus view. This addresses a concrete failure where a 700-character excerpt stopped before the rest of a reported operational assumption. Reading additional context does not authorize unseen messages or an extra ungated provider request.

The v4 continuation smoke test completed eight invocations over 4,000 arrivals, performed four actual continuation reads, accepted 26 quotations with zero citation rejections, and passed the exact source/arrival audit. No agent errors occurred. Three unsupported hypothesis objects were rejected rather than published. Its shared-ledger cost was $0.02511080. This was the final live gate before the full v4 replay; see [CHRONOLOGICAL_CONTEXT_SMOKE.md](CHRONOLOGICAL_CONTEXT_SMOKE.md).

The complete offline test suite then passed 211 tests. A built 0.2.0 wheel was installed into a fresh virtual environment; its CLI successfully ingested the fictional corpus and completed a zero-provider-call chronological replay. These are software/plumbing checks, separate from the quality of real-email inference.

The first large v4 replay admitted the whole period but stopped reasoning at window five: one complete JSON response used a hypothesis object where the top-level schema required an array. The candidate also lacked support references and should have been rejected individually. The run therefore used only 36 provider calls, exposed 163 documents in prompts, and is retained as [CHRONOLOGICAL_SCHEMA_DIAGNOSTIC.md](CHRONOLOGICAL_SCHEMA_DIAGNOSTIC.md). Its 120 emitted quotations and recorded prompt/search/read visibility passed audit; that does not make its reasoning coverage complete.

V5 distinguishes a recoverable model-output rejection from an API/gate failure or source-boundary violation. A schema-compatible singleton collection can be normalized, but unsupported claims are still rejected. Invalid/truncated reasoning becomes an explicit, charged abstention and cannot publish evidence or knowledge. Later windows may continue; a completed run containing such abstentions is labeled `completed_with_rejections`. Provider/gate/source errors still stop further dispatch. The shared call allowance was raised to 520 without resetting any usage or changing the $10 dollar allowance.


The subsequent v5 run was stopped at the request for a fundamental design reassessment. The shared API gate was paused, active calls drained, and the replay process interrupted. No complete v5 discovery result is claimed. Total shared-ledger activity at that checkpoint was 343 attempts and $2.19260096, with zero active or unknown-outcome calls. See [SWARM_REASSESSMENT.md](../SWARM_REASSESSMENT.md) and [the stopped baseline](CHRONOLOGICAL_STOPPED_BASELINE.md). Software tests passed 214 cases, but those checks do not establish interestingness or collective discovery.

## Inquiry architecture checkpoint

The new `inquire` path composes canonical runtime/types, addressed capability routing, private source histories, versioned inquiry artifacts, bounded acquisition actions, and source-aware watches. The research mapping distinguishes implemented mechanisms from omitted or unvalidated features: [INQUIRY_MECHANISMS.md](../docs/INQUIRY_MECHANISMS.md).

The full offline suite passed 252 tests before the final status-endpoint regression; the subsequently changed model/runner modules passed their focused tests, including the real CLI status shape. The actual loopback server on port 8767 returned a successful status response, and Chromium loaded the inquiry portfolio with no browser errors. [UI screenshot](../docs/images/inquiry-diagnostic.png) shows a diagnostic run, not a validated discovery.

Three bounded live smoke runs made 44 calls costing $0.07764416 combined. They exposed acquisition/schema issues and failed to demonstrate peer-mediated discovery. See [INQUIRY_SMOKE_FINDINGS.md](INQUIRY_SMOKE_FINDINGS.md). Afterward the persistent shared ledger recorded 387 calls and $2.27024512, paused with zero active or unknown calls. No counters were reset. Larger execution is deferred pending an operational missing-fact exchange and a meaningful control.
