# Enron corpus provenance and processing

This repository uses the [CMU Enron Email Dataset, May 7, 2015 release](https://www.cs.cmu.edu/~enron/), downloaded from the [release archive](https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz). The locally downloaded archive is **443,254,787 bytes**, SHA-256 **`b3da1b3fe0369ec3140bb4fbce94702c33b7da810ec15d718b3fadf5cd748ca7`**. This digest identifies our downloaded bytes; it is not a publisher-signed authenticity attestation. The machine-readable [manifest](../reports/CORPUS_MANIFEST.json) records indexing completion separately from download completion.

CMU describes a prepared, corrected research collection of approximately half a million messages, with attachments omitted, some redactions, and normalized addresses. It is not a complete original corporate archive. The landing page also links later authenticity concerns; our byte hashes cannot authenticate the original sender or historical event. [Source: CMU dataset documentation](https://www.cs.cmu.edu/~enron/).

## Reproduce locally

Install the project in the environment, then run:

```sh
swarmkit-enron fetch --output data/enron/enron_mail_20150507.tar.gz
shasum -a 256 data/enron/enron_mail_20150507.tar.gz
swarmkit-enron --workspace var/enron ingest data/enron/enron_mail_20150507.tar.gz > var/enron-ingest-summary.json
swarmkit-enron --workspace var/enron status
```

`fetch` preserves an existing destination by refusing to overwrite it. Skip it if the verified archive already exists. Omit `--limit` for the full archive. Re-ingestion resumes safely by raw SHA-256, although streaming a compressed archive still requires reading preceding members. `data/`, `var/`, and SQLite files are ignored by Git. The public manifest and this document contain only provenance and counts, not bulk email text. The 12 files in `tests/fixtures/enron_demo` are clearly labeled fictional synthetic messages and belong in a separate database.

## Completed local index

Full archive ingestion completed with **517,401 attempted and indexed documents**, zero skipped records, zero raw-hash duplicates, and zero reported ingestion errors. The stored raw-message bytes total **1,421,183,736**. The index contains **272016 authored/raw source families**, **0 unknown or ambiguous dates**, and **zero synthetic documents**. FTS row count equals document count. Zero raw duplicates does not imply independent messages: mailbox/header variations can change raw hashes while preserving authored content. The manifest records final counts and extraction version; these ingestion checks are not a complete semantic parser audit.

## What the index preserves

[The corpus implementation](../src/swarmkit/enron/corpus.py) streams tar members without extracting paths or executing email content. Links, special files, unsafe archive paths, oversized messages, and files lacking recognizable email headers are skipped. The default per-message limit is 16 MiB. Inserts commit in batches of 250 attempted messages and at completion. Inspect the ingestion summary's skipped count and bounded error list before equating archive completion with complete successful parsing.

Each unique raw message receives `mail-<full raw SHA-256>`. SQLite retains its raw bytes, all observed archive-member/file locators, decoded body, raw and body hashes, parsing notes, and original date header. Identical raw copies add locators without inflating document counts. Locators identify where bytes came from; the stored raw snapshot remains available if the source archive moves or changes.

`decoded-body-v1` offsets are half-open Python Unicode character ranges `[start,end)` in the stored body. They are neither UTF-8 byte positions nor JavaScript UTF-16 string indices. Clients should use supplied quote text and server verification; browser-generated offsets require conversion for non-BMP characters. The exact quote verifier recomputes raw/body hashes and checks locator, extraction version, source family, boundaries, and body substring. It validates attribution to stored text, **not the interpretation, sender authenticity, or an allegation**.

MIME extraction prefers plain text, otherwise converts HTML to inert visible text. Attachments and attached RFC822 messages are excluded. Line endings become LF; unknown or invalid charset decoding falls back to UTF-8 replacement with a parsing note. HTML structure and original byte offsets are not recoverable from body offsets; retain the raw snapshot. Header decoding and address parsing use Python's email parser. The parser does not infer original identities from normalized or malformed addresses.

## Retrieval and dependence limits

Explicit date offsets are normalized to UTC. Missing, invalid, and timezone-ambiguous dates remain unknown; a historical cutoff excludes them. Date-only cutoffs include the entire UTC day. A sent-date header is not a receipt timestamp or proof that another participant knew its content by that time.

Search accepts up to 32 literal tokens / 2,048 characters and returns at most 200 documents. Default OR provides lead recall; `match='all'` requires every token. FTS/SQL operators supplied by the caller are treated as literal words. Ranking is lexical BM25, without semantic entailment, entity resolution, stemming guarantees, or query stopword removal. Broad natural-language OR queries can retrieve many irrelevant messages. A LIMIT bounds returned records, not the number of postings ranked.

Thread expansion first traverses Message-ID/References/In-Reply-To links. If no linked peers exist, matching normalized subjects within ±30 days provide an explicitly labeled `subject_time_heuristic`. It can merge unrelated repeated subjects or miss renamed and long-running conversations. `around` retrieves chronological neighbors and makes no relatedness claim. Both methods obey cutoffs and result caps.

Authored-content families normalize whitespace in a conservative unquoted prefix and include the parsed sender; very short text falls back to raw identity. These families suppress some copies/resends. They do not establish independent corroboration or resolve every forwarded quote, paraphrase, shared template, or cross-document source dependency. Every generated evidence record labels independence as `not_established`. Exact normalized-quote fingerprints offer an additional clue, not an independence estimator. Multiple agents repeating one document must not be treated as multiple independent witnesses.

## Read-only checks during indexing

At 170,000 committed documents, all raw and decoded-body SHA-256 values in the first 100 records recomputed correctly. Two ingestion-order samples of 2,000 records each contained no empty decoded bodies, no recorded parser notes, and only explicit-timezone dates. These are convenience samples, not estimates for the full corpus.

The first sample had Message-ID on all 2,000 records but no In-Reply-To or References; the second also lacked reply-link headers. Consequently, synthetic fixture thread behavior is more precise than the sampled real data, where subject/time fallback is central. This absence does not prove that all corpus messages lack those headers.

A broad two-term OR query returning 10 IDs took 2.52 seconds while ingestion was active; a selective two-term AND query took 0.002 seconds. SQLite's plan ranked matches into a temporary B-tree before LIMIT because of BM25 plus deterministic document-ID sorting. The retrieval code now orders by FTS5's hidden `rank` column (default BM25), allowing its ranked virtual-table scan to stop without the additional document-ID sort. Equal-score tie order is unspecified. Date predicates remain in the same query before LIMIT, so future matches cannot consume the historical result budget. No ingestion schema or parser changes were made.

A subsequent read-only comparison on the growing actual index measured 6.518 seconds for the old sort and 0.097 seconds for rank ordering, with the temporary B-tree eliminated from the query plan. At 289,500 committed documents, rank-ordered retrieval of 10 full document rows took 0.189 seconds without a cutoff and 0.071 seconds with a December 31, 2000 cutoff; returned scores were sorted and all dated results respected the cutoff. A synthetic regression test verifies parity with explicit BM25 ranking on distinct scores and checks that higher-ranking future documents cannot crowd historical results out of LIMIT. These single observations under concurrent indexing are not controlled benchmarks or a latency guarantee. Broad OR matching, selective cutoffs, repeated full-corpus statistics, copied raw BLOBs in retrieval rows, and raw-snapshot retention can still increase latency, memory traffic, and disk requirements. Prefer distinctive lead terms and cache status outside tight UI polling loops.

No actual case findings or conclusions about individuals are reported here.


## Structured reply and forward parsing

`EmailCorpus.segments(document_id)` partitions the unchanged decoded body into exact, disjoint header and content intervals. The current parser recognizes common Outlook original-message markers, Lotus Notes forwarded blocks and sender/date/header sequences, and nested quote prefixes. Each segment carries its original offsets, kind, depth, claimed sender/date/subject, parsing ambiguity, and a normalized content fingerprint. Inline dates remain verbatim claims; the parser does not invent timezone information or authenticate speakers.

The LJM seed's five forwarded copies share one substantial forwarded-content family. EnergyDesk's later reply separates its outer message and four embedded sender/date contexts. These checks demonstrate the observed formats, not perfect coverage of every email. Short generic messages retain document-specific families to avoid merging unrelated acknowledgments.

Agent prompts expose attributed content segments with server-issued citation spans. Substantial repeated content can reference the first visible occurrence while retaining each occurrence's outer headers and claimed inline attribution. Header text and ordering remain separate from the message's substantive statement. The UI presents these segments and a collapsible original body. A content fingerprint is a dependence cue, not independent corroboration or proof of common authorship.
