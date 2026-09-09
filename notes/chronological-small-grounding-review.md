# Small chronological run: grounding and hypothesis quality

Review of `reports/CHRONOLOGICAL_SMALL.json`: 16 calls, 64 accepted citations, 15 rejected items, six card versions representing only two hypothesis identities. Temporal/quote integrity passed. This does not certify that the selected quotation entails the attached interpretation.

## Concrete failures

**Semantic citation misbinding.** Final card `rule-1ef82f4584af4e288684abc63319de50`, revising `hypothesis-54af0a26f69245cfbfbdab226982a021`, claims customer-facing legal documentation must originate in Houston. Its sole supporting document is `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`, which describes forwarding a confirmation termination letter to the Confirmation Desk. The evidence's `claim` field describes the Houston correspondence while its exact `quote` describes the unrelated routing action. Citation location and chronology are valid; claimed entailment is not.

**An instruction became an unwritten universal rule.** The actual customer-document correspondence is `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`. One instruction about this draft was generalized into a rule covering legal documents to all customers. Proposed jurisdiction/delegation exceptions were not established by cited evidence. Adding “single instance” to an uncertainty field does not repair the universal scope of the rule itself.

**An ordinary routing action became a claimed invariant.** The Confirmation Desk card says routing holds regardless of origin or individual. One observed handoff establishes one handoff. It does not establish invariant routing, a hidden decision condition, or the boundaries of expertise. The proposed future test—whether later emails mention that desk—would not distinguish a universal routing rule from occasional use of a relevant desk.

**Revision counts inflate apparent learning.** Several versions repeat the same rule with the same underlying quote under different owner/claim-derived evidence IDs. One version even includes two variants of that same quote. These are neither independent observations nor demonstrations of learning. Compare changes in substantive rule, scope, alternatives, and source spans/families; do not count changed evidence wording alone as new support.

## Parsing correction

The second source used marker-free ccMail headers that previously stayed inside one content segment. The parser now keeps exact disjoint spans: outer reply `[0,80)`; first embedded Brent content `[208,490)`; earlier Sara content `[626,772)`; earlier Brent content `[890,1134)`. Headers occupy the intervening spans. Inline dates remain verbatim and unverified. The outer reply states the draft had already been dispatched when the instruction was received. This countercontext prevents equating the requested procedure with an observed completed workflow.

A useful *question* for this exchange is whether internal review participation and customer-facing document ownership were separate roles, and whether instructions arrived before the relevant handoff. Those are candidate coordination conditions to test; they are not established firm-wide rules. These case-specific observations must not be inserted into the fresh full-run prompt.

## General protocol changes for the fresh experiment

1. **Extract traces before rules.** Distinguish observed action, stated expectation/instruction, reported outcome, and inferred condition. Preserve the responsible speaker and exact source for each. An explicit instruction alone remains an observation.
2. **Require an explanatory contrast.** A candidate implicit condition should link at least two complementary observations, explain a mismatch or context-dependent choice, and identify what a rival explanation would predict differently. Two spans in one chain remain a single-episode hypothesis, not repeated independent practice.
3. **Scope the claim itself.** Avoid unsupported universals. Unknown exceptions should remain unknown; plausible invented exceptions are not evidence. A cautious footer cannot substitute for a bounded rule.
4. **Challenge entailment before promotion.** The contrasting peer should inspect whether each support concerns the claimed actors, action, context, and outcome. Stable evidence IDs and visible attribution reduce alias confusion; a model's paraphrased evidence claim must never replace the source quotation during review. Mark semantic support unverified until this check passes, and retain disagreements.
5. **Use discriminating later tests.** State the context, predicted action, rival action, and disconfirming observation before later arrivals. A repeated keyword or forwarded copy should not qualify. Track immutable forecast versions and evaluate supported/challenged outcomes separately from the model's confidence.

The objective is an evidence-constrained explanation of how coordination depends on context, followed by a meaningful later test. More fluent summaries, more card versions, and higher exact-citation acceptance do not by themselves achieve it.

## Follow-up: typed-candidate run and truncation diagnostic

Run `replay-run-cc46fb05f93d435fad890e48534a9436` improved source binding and explicitly labeled thin evidence as observations. It finished incomplete after 12 calls because three window-two responses failed JSON decoding; these results are preserved separately as the truncation diagnostic. Operational completion must be checked on the subsequent fresh run.

A substantive distinction remains: two source families do not establish two independent episodes. The dependency hypothesis cites two complementary actor positions in **one** document, `mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332`: a draft awaiting credit input and a forwarded inquiry about a lost trading opportunity. These can motivate a single-exchange coordination hypothesis. The model's description of them as separate episodes is incorrect. Even different outer document IDs can be copies of one exchange. Counts should therefore report exact outer documents and segment families while leaving episode independence unestablished unless reviewed.

The contract-review hypothesis also overstates its inference gap. Source `mail-e1b2c5100b857c183b6db79b0a7d6f29c58ddaececee5a27f0c52083fb676515` explicitly anticipates a response after reviewing proposed revisions. Pairing it with an internal request for comments does not by itself reveal an unstated review culture. It is chiefly evidence of expressed expectations, pending observation of what the recipient actually does.

Source `mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b` does supply a useful structural question: distinguish trader location, the legal entity named on a ticket, and the office handling confirmation. They need not coincide. A discriminating follow-up would compare which of those properties predicts who handles documentation, without assuming centralization motives or a universal practice. This is reviewer interpretation of a lead, not independently validated tacit knowledge and not a case-specific seed for the fresh run.

Once operational checks pass, a broader neutral replay is reasonable as **exploratory candidate generation**. It should preserve observations, uncertain mechanisms, contrary evidence, and revisions for review. Semantic limitations need to be reported candidly rather than obscured by exact-citation success or a growing number of cards.

## Fresh bounded run v3: suitable for exploration, not a validated-rule result

Run `replay-run-0beedd818b044860833c8d2b6a23471b` completed its planned prefix with 16 calls, no agent errors, and 55 accepted/zero rejected citation selections. Its `partial` status denotes incomplete whole-corpus coverage, not a failed invocation. The independent temporal/exact-source audit passed. Reviewed cards bind to relevant source subjects; the earlier Houston-versus-Confirmation-Desk misbinding was not observed in these reviewed cards. This supports proceeding to a broader neutral exploratory run without claiming that inferred practices have been validated.

Semantic limits remain concrete:

- `rule-e418435a0f9f42c0b04a6de0b3730f80` infers deference to US legal requirements from `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`. The cited exchange shows competing views and a suggestion to investigate with US lawyers, not an actual decision to defer. The supported lead concerns jurisdiction-specific uncertainty and disagreement; outcome requires later evidence.
- `rule-396f82f7916e492ebbaa8c78be6be2ac` infers reliable shared context from terse reminders. One cited source, `mail-455c7b88a8af6dd47e93b6b85a9bd6d9298f8db7d88f4db154c0ce0e6b108117`, explicitly asks what the problems are and reports not having heard. That is countercontext to the assumption that no explanation is needed. A useful later test compares whether terse messages receive action, clarification requests, or no answer; brevity alone does not establish shared knowledge.
- Coordination cards infer a lack of formal assignment from emails that do not mention assignment. The absence of an assignment in the supplied excerpt is not evidence that none existed. The narrow observation is that particular people are referred to as handling parts of the work.
- The reported mismatch between Legal's reading and Credit's operating assumption is a potentially useful knowledge-distribution lead (`mail-338aeeaa0f70a9999ee3477abe36405ce2d50d30d63ae7bd839fd581ecf7ebeb`). However, the displayed 700-character quotation ends mid-clause before the full description of Credit's belief. Read the complete source before adopting that detailed interpretation; the excerpt is insufficient by itself. More generally, an exact prefix can still omit the decisive qualification or completion.

Discriminating follow-ups should seek outcomes and alternative explanations: whether legal advice changed the draft, whether recipients needed missing context, whether role assignments predated coordination messages, and whether the reported assumption was acknowledged or corrected. Keep model hypotheses, reviewer corrections, and later evidence separate in the final account. None of these small-run sources should become targeted seeds for the fresh full replay.
