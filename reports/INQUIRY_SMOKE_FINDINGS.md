# Inquiry swarm smoke test: discovery not established

The first live inquiry run inspected a chronological prefix of a metadata-selected May 1999 interval. Its purpose was to test agent-directed investigation before increasing scale. It made 14 DeepSeek V4 Flash calls, costing $0.02300276 under the conservative shared ledger, and exposed portions of 32 documents among 80 admitted records. The gate was paused afterward; cumulative ledger cost was $2.21560372 across 357 calls.

The most consequential finding was an implementation defect: eight proposed actions were rejected. Agents often requested the rest of a truncated email before committing to an interpretation. The agenda unnecessarily required an existing inquiry and a source citation or unresolved-premise field even for these acquisition actions. It also rejected watches that omitted an unresolved premise already stored in the inquiry. Rejections were logged but not returned as explicit feedback to the investigator, allowing repeated invalid requests.

The run opened one question about the basis of a contractual disagreement and a claimed underpayment. It did not demonstrate complementary peer exchange or a collective inference. The question alone is not a discovery result, and this run provides no reason to claim swarm advantage.

The correction separates source acquisition from changes to an explanation: an investigator may read or search before opening a question; the executor still enforces arrived-only access and bounded context. Watches may retain the inquiry's recorded unresolved premise. Rejected actions become explicit private feedback. A follow-up small test must verify those behaviors before a larger run.

The complete chronological record is [INQUIRY_SMOKE_V1.md](INQUIRY_SMOKE_V1.md), with its [JSON audit companion](INQUIRY_SMOKE_V1.json). The corpus interval was selected from structural metadata, without reading topics or seeding a known case; see [selection method](../notes/INQUIRY_PILOT_SELECTION.md). Model interpretations remain provisional.

## Second smoke test

[Run V2](INQUIRY_SMOKE_V2.md) made 16 calls costing $0.02621872, admitted 80 records, and exposed portions of 27 documents. It executed requested source continuations. Three searches were still rejected: two supplied `terms` instead of `query`, and one included irrelevant null collection fields. The adapter now accepts string search terms as a query and removes absent/null optional fields without inventing evidence. Exact span and arrival checks remain unchanged.

The run also repeatedly tried to continue a source that itself ends mid-sentence. The executor now reports whether a requested offset contains readable characters and whether the same read was already requested. Source-end markers are explicitly distinguished from prompt truncation. No peer exchange or collective inference was demonstrated in V2.

## Third smoke test and research assessment

[Run V3](INQUIRY_SMOKE_V3.md) made 14 calls costing $0.02842268, admitted 80 records, and exposed portions of 24 documents. No agenda actions were rejected, but three model responses became accounted abstentions. The adapter did not retain their rejection categories in this version, so the available record does not establish why. Subsequent code records the rejection reason and provider finish reason. This is another diagnostic, not a successful pilot.

Across V1/V2, no investigator requested a peer, joined a peer's inquiry, or revised an explanation through peer exchange. An independent review also found a Sonoco question accompanied by Riverside references in V2: authenticated quotations do not ensure the sources concern the same matter. The agents behaved as independent readers with an unused collaboration interface.

The next research mechanism worth testing is bounded missing-fact probing on a stalled inquiry. A relevant peer should inspect its own existing context for the specific missing premise, return a previously unshared exact span or explicitly report none, and let the owner decide the next action. Compare this protocol against an equal-budget extra search by the owner. Any automatically triggered solicitation must be recorded as a protocol intervention, not misrepresented as spontaneous agent recruitment. No larger run is justified by these smoke tests alone.
