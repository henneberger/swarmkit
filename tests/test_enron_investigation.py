"""Synthetic offline integration tests; no provider or corpus network access."""

import json
from types import SimpleNamespace

import pytest

from swarmkit.enron.cli import parser
from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.investigate import (
    PEERS,
    PHASES,
    InvestigationConfig,
    Investigator,
    OfflineClient,
)
from swarmkit.enron.store import InvestigationStore
from swarmkit.types import AgentContext, AgentState, Task, Usage


@pytest.fixture
def setup(tmp_path):
    sources = tmp_path / "emails"
    sources.mkdir()
    for index, word in enumerate(("revision", "approval", "valuation", "delegation")):
        (sources / str(index)).write_text(
            f"From: peer{index}@example.test\nTo: team@example.test\n"
            f"Message-ID: <synthetic-{index}@example.test>\n"
            "Date: Mon, 1 Jan 2001 10:00:00 +0000\n"
            f"Subject: Synthetic approval {word}\n\n"
            f"The synthetic approval {word} requires a dated supporting record.\n"
            "The accessible record does not establish whether the action was authorized.\n"
        )
    corpus = EmailCorpus(tmp_path / "corpus.sqlite")
    corpus.ingest_directory(sources)
    store = InvestigationStore(tmp_path / "forum.sqlite")
    yield corpus, store
    corpus.close()


def prompt_body(document):
    """Reconstruct only the exact text visible in supplied source spans."""
    return "".join(span["text"] for span in document["spans"])


class RecordingClient(OfflineClient):
    def __init__(self):
        self.payloads = []

    async def complete(self, messages, **kwargs):
        payload = json.loads(messages[-1]["content"])
        self.payloads.append(payload)
        result = await super().complete(messages, **kwargs)
        data = json.loads(result.text)
        data["summary"] = f"{payload['phase']}:{payload['agent']}"
        # A controlled behavioral effect: peer exposure changes the next search.
        data["queries"] = ["dated supporting" if payload["peer_messages"] else "approval"]
        return SimpleNamespace(text=json.dumps(data), usage=Usage(calls=0))


async def test_six_round_snapshot_exchange_and_provisional_findings(setup):
    corpus, store = setup
    client = RecordingClient()
    investigator = Investigator(corpus, store, client, InvestigationConfig("approval", synthetic=True))
    run = await investigator.run()
    assert run["status"] == "completed"
    assert run["completed_invocations"] == 24
    assert run["runtime_usage"]["calls"] == 24
    assert len(run["posts"]) == len(client.payloads) == 24
    for index, phase in enumerate(PHASES):
        batch = [p for p in client.payloads if p["phase"] == phase]
        assert {p["agent"] for p in batch} == set(PEERS)
        for payload in batch:
            peers = payload["peer_messages"]
            if not index:
                assert peers == []
            else:
                assert len(peers) == 3
                assert {p["sender"] for p in peers} == set(PEERS) - {payload["agent"]}
                assert all(p["text"].startswith(PHASES[index - 1] + ":") for p in peers)
    assert any(e["kind"] == "retrieval" and e["query"] == "dated supporting" for e in run["events"])
    assert len(run["wiki"]) == 4
    for finding in run["wiki"]:
        assert "provisional" in finding["status"]
        assert not finding["transfer_tested"]
        assert finding["independence_status"] == "not_established"
        assert "independent_source_count" not in finding
        assert all(e["semantic_status"] == "unreviewed" for e in finding["evidence"])
        payload = next(
            p for p in client.payloads if p["phase"] == "assess" and p["agent"] == finding["agent_id"]
        )
        assert {e["id"] for e in finding["evidence"]} <= {e["id"] for e in payload["evidence"]}


async def test_independent_control_has_no_peer_messages(setup):
    corpus, store = setup
    client = RecordingClient()
    investigator = Investigator(
        corpus, store, client, InvestigationConfig("approval", independent=True, synthetic=True)
    )
    run = await investigator.run()
    assert run["status"] == "completed"
    assert run["completed_invocations"] == 24
    assert all(p["peer_messages"] == [] for p in client.payloads)
    assert not any(e["kind"] == "retrieval" and e["query"] == "dated supporting" for e in run["events"])
    # Posts remain an audit trail, not inputs to the independent investigators.
    assert len(run["posts"]) == 24
    context = AgentContext(Task("isolated", "approval"), AgentState("chronology"), phase="scout")
    output = await investigator.act(context)
    assert output.messages == ()


@pytest.mark.parametrize(
    "bad", ["not JSON", "{}", '{"summary":12,"queries":[],"observations":[],"findings":[]}']
)
async def test_one_bad_peer_cannot_mark_run_completed(setup, bad):
    corpus, store = setup

    class BadPeer(RecordingClient):
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            if payload["agent"] == "skeptic" and payload["phase"] == "retrieve":
                return SimpleNamespace(text=bad, usage=Usage(calls=0))
            return await super().complete(messages, **kwargs)

    run = await Investigator(corpus, store, BadPeer(), InvestigationConfig("approval", synthetic=True)).run()
    assert run["status"] == "incomplete"
    assert run["completed_invocations"] == 23
    assert run["agent_errors"][0]["agent"] == "skeptic"
    assert run["agent_errors"][0]["phase"] == "retrieve"
    assert len(run["posts"]) == 23


async def test_all_peers_fail_stops_incomplete_without_leaking_error(setup):
    corpus, store = setup

    class Broken:
        async def complete(self, *args, **kwargs):
            raise RuntimeError("credential-must-not-be-recorded")

    run = await Investigator(corpus, store, Broken(), InvestigationConfig("approval", synthetic=True)).run()
    assert run["status"] == "incomplete"
    assert run["completed_invocations"] == 0
    assert run["runtime_usage"]["calls"] == 4
    assert "credential-must-not-be-recorded" not in json.dumps(run)


async def test_exact_quotes_only_current_body_window(setup):
    corpus, store = setup
    captured = {}

    class Extractor:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            captured.update(payload)
            doc = payload["documents"][0]
            observations = [
                {"document_id": doc["id"], "quote": prompt_body(doc)[:45], "claim": "Supported text exists."},
                {
                    "document_id": doc["id"],
                    "quote": "The accessible record does not establish",
                    "claim": "Hidden window",
                },
                {
                    "document_id": "invented-document",
                    "quote": prompt_body(doc)[:45],
                    "claim": "Guessed document",
                },
            ]
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Check supplied spans.",
                        "queries": [],
                        "observations": observations,
                        "findings": [],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, Extractor(), InvestigationConfig("approval", body_chars=60, synthetic=True)
    )
    output = await investigator.act(AgentContext(Task("test", "approval"), AgentState("chronology")))
    evidence = output.messages[0].evidence
    assert len(evidence) == 1
    assert corpus.verify_evidence(evidence[0])
    assert evidence[0].metadata["quote"] in prompt_body(captured["documents"][0])
    assert investigator.record["quote_checks"] == {"accepted": 1, "rejected": 2}


async def test_findings_cannot_cite_unseen_old_or_guessed_ids(setup):
    corpus, store = setup
    document = corpus.search("approval", limit=1)[0]
    evidence = [
        corpus.evidence(document.id, 0, 45, claim=f"Claim {index}", owner="chronology") for index in range(21)
    ]
    known = {e.id: e for e in evidence}
    assert len(known) == 21

    class Citer:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            assert len(payload["evidence"]) == 20
            assert payload["finding_evidence_id_allowlist"] == [e["id"] for e in payload["evidence"]]
            assert "NOT document_id" in messages[0]["content"]
            assert "Zero findings is a valid outcome" in messages[0]["content"]
            assert evidence[0].id not in {e["id"] for e in payload["evidence"]}
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Review claims.",
                        "queries": [],
                        "observations": [],
                        "findings": [
                            {"title": "Unseen old card", "evidence_ids": [evidence[0].id]},
                            {"title": "Guessed ID", "evidence_ids": ["ev-guessed"]},
                        ],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(corpus, store, Citer(), InvestigationConfig("approval", synthetic=True))
    context = AgentContext(
        Task("test", "approval"), AgentState("chronology", memory={"evidence": known}), phase="assess"
    )
    output = await investigator.act(context)
    assert output.artifacts == ()
    events = store.run(investigator.id)["events"]
    assert len([e for e in events if e["kind"] == "finding_rejected"]) == 2


def test_cli_global_ledger_and_explicit_live_defaults():
    args = parser().parse_args(["--workspace", "alternate-corpus", "run", "--query", "approval"])
    assert str(args.ledger) == "var/api-ledger.sqlite"
    assert (args.max_calls, args.max_tokens, args.max_usd) == (96, 2_000_000, 10.0)
    assert not args.live


async def test_empty_corpus_stops_before_any_provider_call(tmp_path):
    class NeverCall:
        async def complete(self, *args, **kwargs):
            pytest.fail("empty corpus must not spend API budget")

    with EmailCorpus(tmp_path / "empty.sqlite") as corpus:
        store = InvestigationStore(tmp_path / "forum.sqlite")
        result = await Investigator(corpus, store, NeverCall(), InvestigationConfig("approval")).run()
    assert result["status"] == "stopped_no_documents"
    assert result["runtime_usage"]["calls"] == 0
    assert result["posts"] == []
    assert "no indexed documents" in result["stop_reason"]


async def test_visible_cached_quote_survives_exhausted_retrieval_but_unseen_text_does_not(setup):
    corpus, store = setup
    doc = corpus.search("approval", limit=1)[0]
    line = doc.body.splitlines()[0]
    original = corpus.evidence(doc.id, 0, len(line), claim="Original attributed statement.", owner="practice")
    unseen = doc.body.splitlines()[1]

    class RepeatVisible:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            assert payload["documents"] == []
            assert payload["evidence"][0]["quote"] == line
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Review prior supplied evidence.",
                        "queries": [],
                        "findings": [],
                        "observations": [
                            {"document_id": doc.id, "quote": line, "claim": "Repeated full quote."},
                            {"document_id": doc.id, "quote": line[4:], "claim": "A visible subspan."},
                            {
                                "document_id": doc.id,
                                "quote": unseen,
                                "claim": "Unseen part of known document.",
                            },
                        ],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, RepeatVisible(), InvestigationConfig("approval", max_queries=1, synthetic=True)
    )
    investigator.queries = 1
    context = AgentContext(
        Task("cached", "approval"),
        AgentState("chronology", memory={"evidence": {original.id: original}}),
        phase="assess",
    )
    output = await investigator.act(context)
    accepted = output.messages[0].evidence
    assert len(accepted) == 2
    assert all(corpus.verify_evidence(e) for e in accepted)
    assert {e.source for e in accepted} == {original.source}
    assert accepted[0].metadata["start"] == 0
    assert accepted[1].metadata["start"] == 4
    assert investigator.record["quote_checks"] == {"accepted": 2, "rejected": 1}


async def test_span_selection_preserves_wrapped_text_and_rejects_unknown_spans(setup):
    corpus, store = setup
    captured = {}

    class SpanClient:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            document = payload["documents"][0]
            span = document["spans"][0]
            captured.update(document=document, span=span)
            assert span["end"] <= 60
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Use host-selected source spans.",
                        "queries": [],
                        "findings": [],
                        "observations": [
                            {
                                "document_id": document["alias"],
                                "span_id": span["id"],
                                "quote": "RE-TYPED TEXT IS NOT THE SOURCE",
                                "claim": "Check this span.",
                            },
                            {"span_id": document["alias"] + ":s999", "claim": "Unseen region."},
                            {"document_id": "d999", "span_id": span["id"], "claim": "Mismatched document."},
                        ],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, SpanClient(), InvestigationConfig("approval", body_chars=60, synthetic=True)
    )
    output = await investigator.act(AgentContext(Task("spans", "approval"), AgentState("chronology")))
    assert len(output.messages[0].evidence) == 1
    ev = output.messages[0].evidence[0]
    assert ev.metadata["quote"] == captured["span"]["text"]
    assert ev.metadata["start"] == captured["span"]["start"]
    assert ev.metadata["document_id"] == captured["document"]["id"]
    assert corpus.verify_evidence(ev)
    assert investigator.record["quote_checks"] == {"accepted": 1, "rejected": 2}
    rejected = [e for e in store.run(investigator.id)["events"] if e["kind"] == "citation_rejected"]
    assert all(e["reason"] == "unknown_or_mismatched_span" for e in rejected)


async def test_cached_span_and_short_evidence_alias_resolve_only_current_prompt(setup):
    corpus, store = setup
    document = corpus.search("approval", limit=1)[0]
    original = corpus.evidence(
        document.id, 0, len(document.body), claim="Wrapped source text.", owner="practice"
    )

    class AliasClient:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            assert payload["documents"] == []
            assert payload["finding_evidence_aliases"] == {"e1": original.id}
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Review received evidence.",
                        "queries": [],
                        "observations": [
                            {"span_id": payload["evidence"][0]["span_id"], "claim": "Visible text."}
                        ],
                        "findings": [
                            {"title": "Supported case", "evidence_ids": ["e1"]},
                            {"title": "Invisible alias", "evidence_ids": ["e2"]},
                        ],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, AliasClient(), InvestigationConfig("approval", max_queries=1, synthetic=True)
    )
    investigator.queries = 1
    context = AgentContext(
        Task("aliases", "approval"),
        AgentState("chronology", memory={"evidence": {original.id: original}}),
        phase="assess",
    )
    output = await investigator.act(context)
    assert len(output.artifacts) == 1
    assert output.artifacts[0].evidence == (original,)
    repeated = output.messages[0].evidence[0]
    assert repeated.metadata["quote"] == document.body
    assert "\n" in repeated.metadata["quote"]
    assert repeated.source == original.source
    assert corpus.verify_evidence(repeated)


async def test_rejected_quote_diagnostics_redact_provider_secret(setup):
    corpus, store = setup

    class InvalidQuote:
        _api_key = "SECRET-FOR-LOCAL-TEST"

        async def complete(self, messages, **kwargs):
            doc = json.loads(messages[-1]["content"])["documents"][0]
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "Invalid quotation check.",
                        "queries": [],
                        "findings": [],
                        "observations": [
                            {
                                "document_id": doc["id"],
                                "quote": "Invented SECRET-FOR-LOCAL-TEST quotation",
                                "claim": "No source.",
                            }
                        ],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, InvalidQuote(), InvestigationConfig("approval", synthetic=True)
    )
    await investigator.act(AgentContext(Task("diagnostic", "approval"), AgentState("chronology")))
    events = store.run(investigator.id)["events"]
    assert "SECRET-FOR-LOCAL-TEST" not in json.dumps(events)
    rejected = next(e for e in events if e["kind"] == "citation_rejected")
    assert "[redacted]" in rejected["quote_preview"]


def test_focused_retrieval_and_hard_query_allowance(setup):
    corpus, store = setup
    investigator = Investigator(
        corpus, store, OfflineClient(), InvestigationConfig("approval", max_queries=2, documents_per_query=2)
    )
    results = investigator.retrieve("all: approval revision")
    assert len(results) == 1
    assert "revision" in results[0].body
    assert len(investigator.retrieve("approval")) == 2
    assert investigator.retrieve("approval") == []
    events = store.run(investigator.id)["events"]
    assert len(events) == 2
    assert events[0]["match"] == "all"
    assert events[0]["query"] == "approval revision"


def test_result_pool_deduplicates_wrapped_identical_bodies(setup, tmp_path):
    corpus, store = setup
    sources = tmp_path / "copies"
    sources.mkdir()
    body = corpus.search("revision", match="all", limit=1)[0].body
    for index in range(3):
        wrapped = body.replace(" ", "  ") if index else body
        (sources / str(index)).write_text(
            f"From: copy{index}@example.test\nMessage-ID: <copy{index}@example.test>\n"
            f"Subject: approval revision\n\n{wrapped}"
        )
    corpus.ingest_directory(sources)
    investigator = Investigator(
        corpus, store, OfflineClient(), InvestigationConfig("approval", documents_per_query=2)
    )
    results = investigator.retrieve("approval")
    assert len(results) == 2
    assert len({" ".join(d.body.split()) for d in results}) == 2
    assert len(investigator.opened) == 2


async def test_prompt_uses_single_source_text_and_compact_evidence_views(setup):
    corpus, store = setup
    original_doc = corpus.search("approval", limit=1)[0]
    original = corpus.evidence(original_doc.id, 0, 45, claim="An attributed claim.", owner="practice")

    class CompactClient:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            for document in payload["documents"]:
                assert "body" not in document
                expected = corpus.get(document["id"]).body[:60]
                assert prompt_body(document) == expected
                assert len(document["spans"]) <= 30
            evidence = payload["evidence"][0]
            assert set(evidence) == {"id", "alias", "span_id", "document_id", "quote", "claim", "source"}
            assert evidence["quote"] == original.metadata["quote"]
            return SimpleNamespace(
                text=json.dumps(
                    {"summary": "Compact input reviewed.", "queries": [], "observations": [], "findings": []}
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, CompactClient(), InvestigationConfig("approval", body_chars=60, synthetic=True)
    )
    context = AgentContext(
        Task("compact", "approval"), AgentState("chronology", memory={"evidence": {original.id: original}})
    )
    output = await investigator.act(context)
    assert output.memory_updates["evidence"][original.id].metadata == original.metadata


async def test_chain_segments_deduplicate_text_but_preserve_occurrence_attribution(setup, tmp_path):
    corpus, store = setup
    chain_dir = tmp_path / "chains"
    chain_dir.mkdir()
    shared = (
        "The chainmarker valuation objection remains unresolved pending the written assumptions "
        "used for approval and the named reviewer's dated sign-off.\n"
    )
    inline = (
        "-----Original Message-----\nFrom: analyst@example.test\n"
        "Sent: Monday, January 1, 2001 09:00\nTo: reviewers@example.test\n"
        "Subject: chainmarker approval\n\n" + shared
    )
    for index in range(2):
        (chain_dir / str(index)).write_text(
            f"From: forwarder{index}@example.test\nTo: team@example.test\n"
            f"Message-ID: <chain-{index}@example.test>\nIn-Reply-To: <earlier@example.test>\n"
            "References: <earlier@example.test>\nDate: Tue, 2 Jan 2001 10:00:00 +0000\n"
            "Subject: chainmarker approval\n\n"
            f"This is outer forwarding occurrence number {index}, retained for attribution.\n"
            + inline
            + (inline if index == 0 else "")
        )
    corpus.ingest_directory(chain_dir)
    documents = corpus.search("chainmarker", limit=2, match="all")
    captured = {}

    class ChainClient:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            captured.update(payload)
            forwarded = [
                segment
                for doc in payload["documents"]
                for segment in doc["segments"]
                if segment["kind"] == "forwarded"
            ]
            assert len(forwarded) == 3
            first = next(segment for segment in forwarded if segment["span_ids"])
            assert sum(bool(segment.get("content_ref")) for segment in forwarded) == 2
            assert all(segment["claimed_sender"] == "analyst@example.test" for segment in forwarded)
            assert all("inline attribution unverified" in segment["ambiguities"] for segment in forwarded)
            return SimpleNamespace(
                text=json.dumps(
                    {
                        "summary": "One statement forwarded three times.",
                        "queries": [],
                        "findings": [],
                        "observations": [{"span_id": first["span_ids"][0], "claim": "A recorded objection."}],
                    }
                ),
                usage=Usage(),
            )

    investigator = Investigator(
        corpus, store, ChainClient(), InvestigationConfig("chainmarker", synthetic=True)
    )
    investigator.retrieve = lambda _: documents
    result = await investigator.act(AgentContext(Task("chain", "chainmarker"), AgentState("chronology")))
    transmitted = "".join(span["text"] for doc in captured["documents"] for span in doc["spans"])
    assert transmitted.count(shared) == 1
    assert {doc["sender"] for doc in captured["documents"]} == {
        "forwarder0@example.test",
        "forwarder1@example.test",
    }
    assert all(doc["in_reply_to"] and doc["references"] for doc in captured["documents"])
    evidence = result.messages[0].evidence[0]
    assert corpus.verify_evidence(evidence)
    assert evidence.metadata["segment_kind"] == "forwarded"
    assert evidence.metadata["claimed_sender"] == "analyst@example.test"


async def test_selected_short_reply_keeps_exact_later_occurrence(setup, tmp_path):
    corpus, store = setup
    folder = tmp_path / 'short-reply'
    folder.mkdir()
    body = ('Approved\nThe first occurrence belongs to a different context.\n\n'
            '-----Original Message-----\nFrom: reviewer@example.test\n'
            'Sent: Monday, January 01, 2001 9:00 AM\nTo: team@example.test\n'
            'Subject: repeatprobe\n\nApproved\n')
    (folder / 'one').write_text('From: forwarder@example.test\nSubject: repeatprobe\n\n' + body)
    corpus.ingest_directory(folder)
    doc = corpus.search('repeatprobe', limit=1)[0]

    class SelectReply:
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]['content'])
            candidate = next(d for d in payload['documents'] if d['id'] == doc.id)
            span = next(s for s in candidate['spans'] if s['text'].strip() == 'Approved')
            return SimpleNamespace(text=json.dumps({
                'summary': 'A quoted reply says Approved; attribution is unverified.',
                'queries': [], 'observations': [{'span_id': span['id'], 'claim': 'The quoted reply says Approved.'}],
                'findings': []}), usage=Usage(calls=0))

    investigator = Investigator(corpus, store, SelectReply(), InvestigationConfig('repeatprobe', rounds=1))
    output = await investigator.act(AgentContext(Task('test', 'repeatprobe'), AgentState('chronology')))
    evidence = output.messages[0].evidence[0]
    assert evidence.metadata['start'] == doc.body.rfind('\nApproved\n')
    assert evidence.metadata['quote'].strip() == 'Approved'
    assert corpus.verify_evidence(evidence)
    assert investigator.record['quote_checks'] == {'accepted': 1, 'rejected': 0}
