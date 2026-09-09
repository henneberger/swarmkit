# Independent review of the first real chronological replay

Reviewed `replay-run-2e65401d5c554abb86335e162950acac` in [CHRONOLOGICAL_SMALL_DIAGNOSTIC.md](../reports/CHRONOLOGICAL_SMALL_DIAGNOSTIC.md) and its machine-readable companion. The run is **partial**, ending at September 8, 1999: 4,000 admitted messages, 64 selected, 67 unique documents exposed including retrieval, 16 calls, 110,212 tokens, and approximately $0.0568 recorded cost. These coverage counts distinguish searchable history from actual model inspection. The UI screenshot [chronological.png](../docs/images/chronological.png) initially captured this real run in progress.

## Outcome: useful candidate episodes, weak tacit-rule inference

The six stored revisions represent only two distinct hypotheses, with unchanged core wording. Both originate from the expectations peer in window one. One says confirmation documents go to the Confirmation Desk regardless of originating office; the other says customer-facing legal documents must originate from Houston. Each initially cites one email. Every revision has empty counterevidence and untested transfer. The later confirmation revisions reuse the same source; the final one has two evidence IDs but still only one underlying document and span. Revision count therefore measures persisted peer contributions, not six discoveries or demonstrated learning.

The Confirmation Desk claim broadens an explicit report of one forwarding action into an organizational default. Its qualifier “regardless of the originating office or individual” is not established by the cited action. The Houston claim similarly promotes one explicit instruction to a general obligation. Both uncertainty fields acknowledge the one-instance limitation, which is useful, but the categorical main claims remain too strong. Neither presently qualifies as a demonstrated unwritten routine inferred across episodes.

The expectations peer initially makes the better judgment: these are explicit instructions or common practices, insufficient for a tacit hypothesis. After peer exchange it describes recurring implicit expectations without establishing another independent instance. Three additional peers copy the Confirmation Desk rule in window two. Across 16 posts there are only 11 unique summary strings, with further near-paraphrases. This is evidence of communication and shared retention, not yet collective knowledge gain. Prediction checks remain unresolved; absence of inspected corroboration is not absence of relevant mail among all arrivals.

## A more revealing inference opportunity

The full “PC draft” source, `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`, contains a contrast the rule misses. Brent asks about readiness because a trading opportunity was lost. Sara says the draft needs one credit item and offers a copy. Brent then specifies blind copying and Houston-only outward distribution. The outer reply says the draft had already gone when that instruction arrived.

This supports a bounded **question** about coordination: does completion of credit input act as the drafter’s operational send trigger while another office assumes an opportunity to impose distribution conditions? The timing mismatch is more informative about implicit expectations than simply rephrasing the distribution instruction. One thread still cannot establish a recurrent rule; sender/date attribution and direction of each reply also need care. Another independently authored episode with the same or opposing trigger would test this hypothesis.

## Proposed prompt and evaluation changes

Require each candidate to identify the observed sequence, the mismatch between participants’ apparent assumptions, and what the inference adds beyond quoted explicit instructions. Prefer conditional, local hypotheses over organization-wide rules. Label single-episode possibilities as questions; require distinct episodes for a broader practice claim.

Ask revisions to name a substantive change: narrower applicability, an exception, counterevidence, new independent support, or withdrawal. Permit “no change” without writing another revision. Track unique supporting episodes and unchanged-rule reuse separately from agent agreement. Retrieve contrasting behavior as well as matching keywords; searching only “confirmation desk” invites confirmation bias.

The existing temporal admission boundary and exact quotes are useful scaffolding. The present pilot has not established superior inference from swarm communication, meaningful revision, or out-of-sample tacit-knowledge transfer. A matched independent baseline and later-arrival predictions remain necessary to assess those claims.
