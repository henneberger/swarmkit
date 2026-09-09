# Retrieval and citation review — first actual pilot

Internal source-review leads only. Email statements are attributed text, not independently verified events or legal conclusions. No new model calls were made.

## Citation failure mechanism

Pilot run `run-5c15135fdc05465395537b7629a8d953` recorded 6 accepted and 36 rejected citations, with zero published cards. Rejection events retain only kind/time/agent, not proposed quote or reason, so an exact causal breakdown is unavailable. The dominant retrieved objection contains hard LF wraps inside sentences. Replacing those wraps with spaces produces a plausible-looking quotation that fails an exact body-substring check. This is a concrete plausible failure mechanism, not proof that all 36 failures had this cause. Deterministic server-issued span IDs let models select preverified text without retyping whitespace. Keep the original exact quote and offsets; any normalization-based matching should resolve back to the original span and report its match mode.

## Exact source spans

Offsets below are half-open Python character positions in `decoded-body-v1`; JSON strings preserve newline and whitespace characters exactly.

### Valuation objection
Document `mail-d4f9955314d555fb1c7f37306b179688079c72b28117d350ce596af6b522e592`; subject `FW: LJM/Raptor valuations`; outer message date `2001-10-08T18:37:21+00:00`.
Span `[296,473)`; body SHA-256 `f415e9f0ff383575a17a0587616e7493c14b064044a542e26016fb52126c6f71`.
```json
"I feel strongly that I cannot support\nthe valuations my group has produced so far for the LJM/Raptor\nrelated transactions without examination of all the related legal documents."
```

### Reported initial sign-off
Document `mail-c4c875c613a22c9dc6f8bc7f564ef5bf4f1b4de231ceb30c56b72b78597c94e7`; subject `RE: Raptor Debris`; outer message date `2001-10-09T20:27:12+00:00`.
Span `[134,251)`; body SHA-256 `c5019336d1fc2b833011160a8b87821a292b52b24392fa24d11e126e60baa160`.
```json
"The business units, RAC and Arthur Andersen all signed off on the initial valuations for the assets hedged in Raptor."
```

### Assumed endorsement convention
Document `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb`; subject `Re: EnergyDesk`; outer message date `2000-12-11T09:59:00+00:00`.
Span `[1780,1945)`; body SHA-256 `0ebf2b4eeb2dd313e659c69adf3a58ceeb0ac042cbe4365e4213e3d90806a378`.
```json
"The standard models used at Enron, like SPRDOPT and other routines \nin Exotica.xls are written by Research and therefore I have always assumed \nendorsed by Research."
```

### Resident expertise assumption
Document `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb`; subject `Re: EnergyDesk`; outer message date `2000-12-11T09:59:00+00:00`.
Span `[940,1150)`; body SHA-256 `0ebf2b4eeb2dd313e659c69adf3a58ceeb0ac042cbe4365e4213e3d90806a378`.
```json
"I've tried to emphasise that we support Exotica for internal purposes only, \nand that our entire setup presupposes the presence of resident quants on the \ntrading floor to support the tools that Research write."
```

### Challenge to internal validation
Document `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49`; subject `Re: EnergyDesk`; outer message date `2000-12-18T17:36:00+00:00`.
Span `[92,197)`; body SHA-256 `48fdcabdca7ee10743f44d3d95fd1eaa746de1ff12fab5b05ec6413a9a84634a`.
```json
"As you have correctly pointed out, the model validation issues cannot\nbe handled  internally by Research."
```

The objection is inside a forwarded October 4 message; the outer October 8 timestamp is not the original statement date. The sign-off sentence concerns initial valuations and is potentially countervailing context, but does not establish that the later document-access objection was answered. Do not collapse these distinct scopes into a proved contradiction or resolution.

## Candidate implicit procedure, separate from LJM

The EnergyDesk exchange supports a testable procedural hypothesis: some participants treated Research-authored models as endorsed by authorship and expected resident quantitative expertise to support internal deployment, while others sought independent validation and explicit sign-off. These are expressed assumptions and disagreement in one exchange, not a proved firm-wide unwritten rule. The later reply challenges internal-only validation. A four-peer test should separately retrieve claimed ownership norms, observed deployment decisions, explicit policy, and exceptions; then seek an unrelated held-out deployment thread. Restrict any surviving procedure claim to contexts supported by those observations. This is a valuation-method governance lead, not direct evidence about the LJM objection.

## Forwarding and retrieval dependence

The exact original seed query returned five top documents, all forwarding the same objection. Each has a different raw source family because its authored prefix is empty or too short for authored-content grouping. Thus the first five slots represent one underlying objection, not five independent witnesses. Two of these records even have identical decoded bodies while raw headers differ. The earliest forwarded example above contains the same central claim as later November forwards; repeated forwarding alone does not prove that the issue stayed unresolved.

The EnergyDesk search `valuation sign process` with literal AND returns multiple identical-body copies and a later reply quoting the entire earlier exchange. Authored-family grouping catches several direct copies, but source-level grouping alone misses quoted ancestors in different authored messages. Rank a bounded larger pool, prefer diverse body hashes/source families, and detect overlapping quoted spans across documents before counting support. A shared normalized quote fingerprint is a useful dependence cue, not proof of source independence. Preserve forwarding lineage as a separate observation.

Broad OR seed terms also admit unrelated approval workflows. Retrieval relevance and citation integrity are separate gates: accepting a perfectly quoted SAP approval request does not make it relevant evidence for the valuation question. A peer should challenge this scope mismatch before evidence enters the candidate card.
