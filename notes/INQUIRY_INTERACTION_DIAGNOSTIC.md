# Why the full-corpus inquiry run had no peer requests

Read-only diagnosis of `inquiry-run-23e0700d8dc045979be55004fb5ea135` during its first approximately 100 actions. This is a snapshot, not a final run evaluation.

The database contained **zero `request_peer` proposals**, including rejected proposals. At the captured 101-post checkpoint, actions were 41 waits, 31 reads, 20 watches, three searches, three opens, and three unsolicited replies. The three inquiries had one participant each. Thus there is no observed request for the router to reject, misaddress, or lose. The unsolicited replies are not evidence of a working conversation: no actual peer request preceded the first such rejection.

The reasoner receives the four exact agent IDs, a public directory of recent sender/subject coverage, shared inquiry questions, and the `request_peer` action. Nonmembers can ask factual questions without joining an inquiry. The agenda validates explicit recipients or chooses a recipient with `CapabilitySuccessRouter`, creates an addressed canonical message, and schedules `peer_review`. The runner reconstructs the assigned request from canonical message history even if an earlier task consumed its inbox. Offline tests exercise that path and the withheld-communication control. No demonstrated host prohibition on requesting a peer was found.

There are substantive affordance limitations:

* All four capability sets are empty. A request without an explicit recipient therefore receives no meaningful capability ranking; deterministic ties are possible. This has not yet caused the observed zero requests because no request was proposed.
* The public coverage directory retains only eight descriptors per peer. Older matter expertise can disappear even when its source remains in private memory. A peer may consequently look like a collection of unrelated recent subjects.
* Agents can retrieve any arrived historical document themselves. Private initial exposure creates different context, but asking a peer is not necessary to unlock exclusive archive access. The model can rationally prefer a direct search or read.
* Questions do not recruit collaborators automatically. Opening queues owner investigation; watching can then suspend it. A public question alone supplies neither an addressed obligation nor a concrete counterpart who knows the missing fact.

The observed action policy is therefore largely individual investigation over a shared archive, despite functioning communication machinery. It should not be described as demonstrated collective discovery. The earlier workflow fixes—explicit membership/allowed-action fields, actionable join feedback, assigned request IDs, and distinct-watch coalescing—repair concrete defects but cannot establish that peers will choose useful collaboration.

A subsequent controlled comparison could test whether relevant historical coverage descriptors or genuinely complementary access make peer requests useful. That would be an experimental change requiring its own label, not a correction proven necessary by these logs. No conversation, agreement, or inquiry membership should be injected merely to improve a swarm activity count.
