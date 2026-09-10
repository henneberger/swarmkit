# Full-corpus inquiry experiment protocol

**Launched and running** as `inquiry-run-23e0700d8dc045979be55004fb5ea135`; the first 4,000 records were admitted at launch. Current execution status must be read from the progress file or forum. This experiment extends the inquiry swarm across all **517,401 indexed email records**, rather than repeating a two-week slice. It follows their recorded outer dates, with four persistent investigators choosing questions, source reads, searches, peer requests, replies, watches, revisions, or silence. It does not require a fraud allegation or an unwritten-rule output.

The launcher is [`scripts/run_full_corpus_inquiry.py`](../scripts/run_full_corpus_inquiry.py). It requires explicit `--live`, uses the existing provider ledger, and pauses the gate on exit. Do not reset the ledger or reservations to restart it. `--resume-run RUN_ID` resumes the original investigation and arrival membership; it is not a fresh independent replicate.

## Corpus scope and chronology

The replay bounds are **1980-01-01 through 2044-12-31 inclusive**, covering every indexed record. Metadata-only counts show:

| Recorded year group | Records |
|---|---:|
| 1999 | 11,144 |
| 2000 | 196,100 |
| 2001 | 272,964 |
| 2002 | 35,974 |
| All other years | 1,219 |
| **Total** | **517,401** |

All records have a parseable date with an explicit timezone. This is a parser classification, not proof of correct dates. The 1,219 records outside 1999–2002 include 522 dated 1980 and a small number dated as late as 2044. They are included to account for the whole corpus, but their anomalous dates must not be interpreted as credible historical delivery times.

Arrival order is `(date_utc, document_id)`. Only admitted records are searchable or available for citation. Quoted older messages become accessible when their outer record arrives. Batched admission means agents observe a batch at its final cursor, not at every email's individual instant. This is **replay of recorded dates**, not a reconstruction of authenticated mail delivery or a prospective early-warning trial.

Volume is highly uneven: January–April 1999 contains only 430 records, whereas October 2001 contains 37,139. Fixed-volume batches spread computation with volume rather than exhausting it on the sparse early years. They also compress long sparse periods into a single observation window; reports must preserve that limitation.

## Confirmed work and budget allocation

| Setting | Value |
|---|---:|
| Investigators | 4 |
| Admission batch | 4,000 records |
| Maximum batches | 130 |
| Dispatches per batch | Up to 10 |
| Total dispatched-action cap | 1,500 |
| Per-inquiry dispatched-action cap | 32 |
| Selected documents per investigator per batch | Up to 16 |
| Maximum model output | 3,000 tokens |

The 130 batches can use at most 1,300 regular dispatches, leaving a **nominal 200-dispatch reserve** for outstanding conversations and followups after admission. Unused batch capacity can leave more. A dispatch is not necessarily one successful paid call: rejection, transport failure, and accounting boundaries are recorded separately. Per-inquiry limits and the total cap still govern pending work; reaching the corpus end does not resolve open questions.

The existing shared ledger stood at **$2.882033** when this configuration was agreed. The working target is roughly **$10 cumulative**, with a **$20 operational ceiling** to avoid silently truncating the corpus pass merely because the earlier pilot's average cost was optimistic. This is a spending allowance, not a promise to spend the full ceiling. The previous run's approximately $0.00413 per model call is only a rough planning reference; larger contexts can raise costs. Measured ledger charges remain authoritative and include prior work. The cumulative operational gate is $20, 40 million tokens, and 3,000 calls, preserving the existing 535 calls and $2.882033 rather than resetting counters.

The agenda distributes work across inquiries and reserves periodic exploration. It does **not guarantee four scouting calls in every batch**. Pending investigations and replies compete for the remaining slots. The interpretation should distinguish chronological coverage, model exposure, and followup effort rather than reporting only a call total.

## What “whole corpus” does and does not mean

Every record is admitted into the replay and checked against active literal watches. Exact-body deduplication reduces repeated initial reading. Investigators receive bounded source samples with sender-based continuity, retain their own source evidence, and can search all history already admitted. Private memory retrieval ranks existing exact quotations and factual source scope; it does not synthesize missing evidence.

**The model does not read every full email.** The configuration allows at most 8,320 initial document-selection slots across four investigators and 130 batches, before additional targeted retrieval. Actual exposure can be lower, and excerpts are paged. A selected document, an exposed excerpt, and an exhaustively read document are different measures. Whole-corpus admission provides broad searchable history and watch coverage; sampled model reading cannot certify that all significant situations were noticed.

No retrospective topic list or known case is supplied. Date/corpus bounds and resource limits are controller choices; substantive inquiries should originate in the observed messages. Prior pilot findings are not evidence of what this fresh run discovers.

## Evidence and interpretation

The final account should present developing situations and changes in understanding, with source IDs, outer dates, exact spans, and uncertainty. A forwarded copy is not independent corroboration. A reported action is not confirmed receipt or completion. A named dealmaker does not establish approval of every related transaction. Exact-quotation and temporal audits establish source boundaries; they do not establish semantic entailment or importance.

For every claimed collective contribution, inspect whether one investigator's request caused another to recover relevant evidence and whether the answer changed a subsequent check or conclusion. Empty replies and rejected interpretations belong in the account. Agreement or repeated summaries are not sufficient. Without an equal-budget independent or single-investigator control, this run remains an exploratory demonstration rather than a causal estimate of swarm advantage.

Progress is written atomically to `var/enron/full-corpus-progress.json`, including run ID, status, admitted count, virtual time, model metrics, and update time. The durable forum is `var/enron/forum.sqlite`; final exports are written under `reports/INQUIRY_FULL_CORPUS_V1`. A stale progress timestamp, partial status, or pending capped work must not be presented as a completed successful investigation.

## Recorded intervention during this run

The same run resumed with a revised context/communication policy at **172,000 arrivals, 234 completed model calls**, and virtual time **2000-11-28T13:57:00+00:00**. It is consequently a **mixed-version exploratory run**, not a fixed-policy experiment. Earlier outputs remain part of its history and are not attributed to the revised mechanisms.

The loaded changes were:

- Persistent peer-coverage metadata is ranked for relevance to the current question.
- An assigned inquiry exposes its own relevant artifact context; unrelated inquiry artifacts are no longer injected into every task.
- Exploration emphasizes current incoming developments. Private-memory retrieval on exploration uses matching evidence only, avoiding unrelated recency fallback.
- Synthetic artifact-context messages were removed because agents could mistake their authors for actual peers awaiting replies.
- An optional, bounded, host-assisted source-fact probe can follow a **future agent-opened question** when another peer's coverage is distinctively relevant. It is not a mandatory theory or result and does not retroactively probe old inquiries.

The last mechanism combines an agent-chosen question with host-assisted recruitment; any successful exchange must be labeled accordingly rather than credited to fully autonomous peer selection. Existing evidence provenance, arrival restrictions, budget accounting, and the original run ID are retained. Improvements after this boundary cannot be cleanly attributed to one change without separate controlled comparisons.
