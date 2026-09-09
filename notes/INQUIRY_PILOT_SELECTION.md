# Structurally selected chronological inquiry pilot

Recommendation: use **1999-05-10 00:00 UTC through 1999-05-24 00:00 UTC exclusive**, preserving `(date_utc, id)` arrival order. This contains **389 raw email records**, below the requested 500-email limit. With `ReplayCorpus` date-only inclusive bounds, use `start='1999-05-10', end='1999-05-23'`.

This recommendation uses dates, source/body hashes, mailbox locators, normalized-subject equality, and sender counts. **No message body or subject text was read to choose the interval.** It does not target a known event, person, allegation, or retrospective finding. It is nevertheless retrospective structural pilot selection, not a prospectively chosen early-warning evaluation. Continuity is a retrieval opportunity, not evidence that anything interesting happened.

## Measured comparison

All counts came from read-only SQLite queries against `var/enron/corpus.sqlite`. No index or corpus row was created or changed; at most 5,000 metadata rows were held at once.

| Property | First 80 globally dated records from 1999 | Recommended two-week interval |
|---|---:|---:|
| Raw records | 80 | 389 |
| First/last period | Jan 4 10:21 to Jan 18 15:10 UTC | May 10 inclusive to May 24 exclusive |
| Distinct source-family labels | 42 | 230 |
| Distinct exact decoded-body hashes | 40 | 200 |
| Mailboxes represented | 1 | 10 |
| Distinct senders | 4 | 29 |
| Nonempty normalized-subject groups | 33 | 136 |
| Cross-day subject groups after source-family deduplication | Not measured for raw-80 comparison | 23 |
| Unique-family records in those cross-day groups | Not measured for raw-80 comparison | 70 |
| Explicit reply/reference-header records after family deduplication | Not measured for raw-80 comparison | 0 |

The early global prefix is not primarily a diversity problem: it is one mailbox with substantial copying. The proposed interval offers more participants and cross-day continuity. Source families are heuristic deduplication labels, **not certified independent origins**. Matching subjects are also weak thread cues; zero explicit reply/reference headers means reliable continuity needs source inspection rather than assuming RFC reply chains.

We also inspected two other calendar intervals using the same metadata-only calculations:

| Interval, end exclusive | Raw | Families | Bodies | Mailboxes | Senders | Cross-day subject groups / records |
|---|---:|---:|---:|---:|---:|---:|
| May 17–24 | 131 | 78 | 67 | 8 | 13 | 3 / 11 |
| June 1–8 | 156 | 89 | 78 | 8 | 24 | 3 / 7 |

The two-week recommendation preserves substantially more cross-day links while staying under the raw-record cap. It was selected from these inspected alternatives; no claim of unbiased interval sampling is appropriate.

The current four-investigator sender-hash allocation, applied to the recommended interval after first-occurrence exact-body deduplication, produces **66, 32, 47, and 55** distinct bodies for investigators 1–4 respectively. This is a usable initial distribution, not guaranteed complementary knowledge. Retain all 389 arrivals and their dates for watches/provenance; deduplication should reduce repeated prompt text without deleting distinct receipt contexts. Small admission batches can preserve response opportunities. Do not require all agents to discuss every arrival.

## Reproducible query and calculations

Open the corpus with `sqlite3.connect('file:var/enron/corpus.sqlite?mode=ro', uri=True)`. For the recommended interval:

```sql
SELECT id, date_utc, source_family, body_sha256, normalized_subject,
       sender, recipients, raw_locator, in_reply_to, refs
FROM documents
WHERE date_utc >= '1999-05-10T00:00:00+00:00'
  AND date_utc <  '1999-05-24T00:00:00+00:00'
ORDER BY date_utc, id;
```

For the first-80 comparison, replace the bounds with `1999-01-01` and `2000-01-01`, and append `LIMIT 80`. Preliminary prefix exploration used `LIMIT 5000` and the same metadata columns, never bodies.

Count source families and body hashes independently. Extract the mailbox as the path component immediately following `/maildir/` in `raw_locator`, and count distinct values without displaying mailbox identities. Keep the first chronological row of each source family for continuity calculations. Group these rows by nonempty `normalized_subject`; a cross-day group contains at least two distinct `date_utc[:10]` values. Count explicit reply/reference records where either serialized field differs from `[]`. The current ownership bucket is `int(sha256(sender.casefold().strip()).hexdigest()[:16], 16) % 4`, using the first row of each body hash for its owner.

These are bounded metadata queries using existing date access. No subject text, address, source body, or raw MIME needs to be printed or exported to reproduce the table.

## InquiryReasoner correctness review

Reviewed `inquiry_model.py`, `source_context.py`, and the calling path in `inquiry_experiment.py`. Findings below describe the inspected state, before any concurrent fixes are confirmed.

- **Confirmed missing adapter recipient guard; reported to root and engine owner, fix not independently verified.** An offline synthetic fake-client probe passed a valid arrived Evidence inside a Message addressed to `intended-recipient` into `InquiryReasoner.act` for `wrong-recipient`. Both message text and evidence reached that actor's prompt. The ordinary experiment path supplies the actor's routed inbox, so this is a missing defense at the public adapter boundary, not evidence of leakage in a live run. Require addressed-to-actor or explicitly authorized broadcast messages before reading their text/evidence. The probe made zero paid calls.
- **Watch context can miss the trigger; reported, fix pending verification.** The experiment watch branch fetched the triggering document but discarded the evidence offset. `SourceContext` then exposed its initial page, potentially omitting a matching passage beyond the first 700-character segment excerpt. Pass the actual triggering span/offset, with surrounding context, to the reasoner.
- **The no-peer-exchange setting is not complete independence.** Even when evidence replies are disabled, the inspected adapter caller still exposes other investigators' inquiry questions and sender/subject coverage. These can redirect search. Either hide this material for the independent control or explicitly label the condition as an evidence-reply-only ablation. A shared directory can be useful in the treatment without being neutral in the control.
- **Assigned inquiry may be omitted.** `InquiryReasoner` takes the first eight directory entries without prioritizing the current assignment. Later inquiries can lose their own question/rivals despite receiving a task ID. Present the assigned inquiry first, then relevant owned/participating inquiries.
- **Working source safeguards:** supplied citations must resolve to current prompt references; peer and retained evidence must verify against arrived membership; bad JSON/reference output becomes an abstention with provider usage retained. These protect source and temporal accounting. They do not verify semantic entailment, authorize arbitrary caller-supplied messages, or authenticate inline attribution.

No paid evaluation should be interpreted as a privacy, grounding, or discovery success merely because quotations pass exact-span validation. The proposed slice is a practical context choice for a bounded experiment, not a prediction that it contains a discovery.

### Fixes verified before the first live smoke test

The adapter now rejects a message addressed to another investigator before any model call (regression test in `test_inquiry_model.py`). The runner passes watch-trigger offsets, prioritizes the assigned inquiry in its directory, and explicitly names the communication ablation rather than claiming independence. These changes resolve the inspected boundary defects; they do not establish discovery quality.
