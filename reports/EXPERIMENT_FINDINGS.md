# What the Enron swarm pilots surfaced

The pilots surfaced two useful investigation leads: a documented qualification on valuation support, and disagreement about who owned model validation. They did **not** establish fraud, recover unwritten human expertise, or demonstrate that communicating agents outperform independent agents. The strongest result is a set of inspectable questions with source attribution; both runs finished without publishing a formal model-generated knowledge card.

This report separates the DeepSeek peers' recorded assessments from additional reviewer synthesis. It reviews [the valuation pilot](ENRON_PILOT.md), [the EnergyDesk pilot](ENRON_KNOWLEDGE.md), and exact stored source spans. It is not an independently validated historical account.

## What the peers actually produced

The parsed valuation run `run-5d74c7cad1bb4b10951ce6977ec621d5` and EnergyDesk run `run-3756cce6b87a47268a010b2d390d6606` each completed 24 model calls across four communicating peers. Their reports record 69 and 72 accepted citation selections respectively, zero rejected selections, and zero published cards. Accepted selections include reuse of the same material; they are not counts of independent facts or corroborating witnesses.

In the valuation run, the peers converged on an objection to supporting LJM/Raptor valuations without the relevant legal documents. They asked whether the documents were subsequently supplied and whether a response or approval followed. The skeptic retained benign alternatives, including ordinary due diligence and resolution outside the retrieved correspondence. The later rounds largely repeated this assessment. [Recorded valuation assessments](ENRON_PILOT.md).

In EnergyDesk, all four peers identified incompatible expectations about Research and RAC sign-off. They asked for a formal policy and the eventual deployment decision. This is a useful retrieval result, but some wording exceeded the source: James New's conditional inquiry became an asserted requirement in peer summaries. His email asks whether his understanding is correct; it does not establish the rule. Likewise, Port's position concerns signing off valuation methods, not the absence of every RAC responsibility. [Recorded EnergyDesk assessments](ENRON_KNOWLEDGE.md); source E1 below.

## Reviewer synthesis: valuation support had an explicit qualification

The October 4 statement, preserved in a forwarded message, says the author cannot support the valuations without examining the related legal documents. Its significance is a boundary on what the quantitative analysis could substantiate: calculations based on verbal descriptions do not establish that the implemented contracts match those descriptions. This is an investigative lead about the connection between analysis, contract terms, and approval scope. [L1].

The full pilot retrieved something more informative than additional forwards: an October 22 authored reply stating:

> Those documents were not provided and therefore
> we cannot sign off on any analysis done in the past.

That is an explicit report of non-provision by the writer at that point, not merely an inference from the absence of a reply in a search result. It remains an attributed statement: it does not establish what every other participant possessed, what happened later, or the correctness of any valuation. The same reply flags a perceived conflict between a restriction and a put. That supplies a specific contract question to investigate, rather than a generic suspicion. [L2].

There is countervailing context. An October 9 email reports that business units, RAC, and Arthur Andersen signed off on **initial** valuations. That assertion and the qualification above could concern different stages, assumptions, deliverables, or signatories. Neither source alone proves that the other is false. They justify reconstructing precisely what was approved, by whom, against which contract version, and with what reservations. The sign-off source was inspected during reviewer follow-up; it should not be represented as a discovery newly made by the final parsed swarm run. [L3].

The bounded hypothesis is that an approval assertion and a research qualification may have traveled with different scopes. The next test is to match the actual analysis version, contractual restrictions, approval artifact, and recipients. Only then could a reviewer assess whether qualifications were preserved, misunderstood, addressed, or bypassed. This experiment supplies none of those outcomes as established fact.

## Reviewer synthesis: competing assumptions exposed a governance problem

The EnergyDesk exchange is especially relevant to implicit knowledge. Participants state assumptions that are often left unstated until a transfer or deployment forces them into conflict:

- **Authorship as endorsement.** Port describes assuming that Research-authored models were endorsed by Research. That links responsibility to who wrote a model. [E1, endorsement span].
- **Ownership and review capacity.** Leppard distinguishes London Research from the group that owns the code and questions both its capacity to audit another group's work and self-validation by the originating group. Organizational labels therefore do not uniquely identify a capable independent reviewer. [E1, ownership span].
- **An operating environment as an implicit dependency.** Leppard says internal support presupposes resident quantitative expertise on the trading floor. Moving the software into a different setting may remove part of the process that made it usable. The relevant unit of transfer may be software plus local expertise, not software alone. [E1, support span].
- **Independent validation as a competing expectation.** New asks whether Research and RAC must sign off, while Kaminski's later response agrees that validation cannot be handled internally by Research. These statements motivate clarification; they do not supply the final policy or prove noncompliance. [E1, inquiry span; E2].

A defensible procedural hypothesis is: **in this exchange, responsibility for model approval was interpreted differently depending on authorship, organizational ownership, and expected local support; deployment exposed the mismatch.** The correspondence also contains escalation and requests for clarification, which are evidence of people trying to resolve uncertainty. It does not show that the deployment proceeded without review.

This is a bounded reconstruction of expressed assumptions across an exchange. Calling it recovered tacit expertise would overstate the result: the emails do not teach the model how an experienced reviewer actually recognizes a bad valuation. Generalizing it into firm-wide practice requires independent deployment episodes and explicit exceptions. Demonstrating transfer requires a held-out task where the inferred procedure improves a receiver's decisions.

## What remains untested about the swarm

The peers communicated, reused source evidence, challenged missing resolution, and produced similar assessments. Similarity can reflect useful information sharing, shared initial retrieval, or repeated agreement. The content of the EnergyDesk disagreement was already present in an embedded chain; distributing it among four agents does not by itself establish discovery beyond a careful single reader. The completed [independent baseline](ENRON_BASELINE.md) used 24 calls, accepted 67 citation selections with zero rejections, and published zero cards. These operational counts do not measure inference quality; no comparative swarm advantage is established.

Useful follow-up questions are concrete:

1. For LJM, which contract versions and model assumptions correspond to each sign-off assertion, and does later correspondence explicitly acknowledge the qualification or settle the restriction/put issue?
2. For EnergyDesk, is there a dated policy distinguishing authorship, technical validation, business approval, and deployment support? What happened to the proposed Oslo deployment and the requested escalation?
3. In an unrelated deployment thread held out from hypothesis construction, does the same ownership/support mismatch predict a documented clarification, review, or deployment change? Which ordinary successful cases contradict the hypothesis?
4. With identical starting documents and matched call budgets, does communication improve distinct source coverage, correction of scope errors, or resolution of a question? Repeated citations and consensus should not earn credit as new evidence.

Both pilots used retrospective, topic-specific queries, including already-known entity names, with no historical cutoff. Later commentary and forwarded material were available. They are not demonstrations of early warning or prospective fraud detection. A prospective evaluation would need an as-of-date corpus, exclusion of later commentary and quoted future information, predeclared questions, and independently reviewed outcomes.

## Exact source references

IDs resolve in the local corpus source viewer. Offsets are half-open Python character ranges in immutable `decoded-body-v1`; inline dates and authors are claims carried by the text. Raw/body hashes and archive provenance remain available through the corpus and [manifest](CORPUS_MANIFEST.json). These narrow spans support the statements above; the whole surrounding chain is needed to evaluate context.

| Key | Document ID | Exact body spans and scope |
|---|---|---|
| L1 | `mail-d4f9955314d555fb1c7f37306b179688079c72b28117d350ce596af6b522e592` | `[296,473)` qualification; outer October 8, 2001 message forwards an October 4 statement. |
| L2 | `mail-01399d6d4b430a93bff048b9c6c4cf62405c26161e4119cadcb3341c840cfd43` | `[197,297)` reported non-provision; `[594,748)` perceived restriction/put conflict; outer October 22, 2001 authored reply. |
| L3 | `mail-c4c875c613a22c9dc6f8bc7f564ef5bf4f1b4de231ceb30c56b72b78597c94e7` | `[134,251)` reported initial sign-off; October 9, 2001. |
| E1 | `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` | `[1780,1945)` endorsement; `[344,658)` ownership; `[940,1150)` resident support; `[2805,3289)` conditional sign-off inquiry. Embedded speakers must remain distinct. |
| E2 | `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` | `[92,197)` challenge to internal-only validation; outer December 18, 2000 reply. |
