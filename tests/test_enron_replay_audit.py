"""Offline regression coverage for exact-source and temporal audit certification."""

from __future__ import annotations

import importlib.util
from email.message import EmailMessage
from pathlib import Path

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.investigate import evidence_view
from swarmkit.enron.replay import ReplayCorpus

spec = importlib.util.spec_from_file_location(
    "audit_replay", Path(__file__).parents[1] / "scripts" / "audit_replay.py"
)
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)
audit = audit_module.audit


def test_audit_valid_source_tampered_quote_and_same_time_hidden_arrival(tmp_path):
    source = tmp_path / "emails"
    source.mkdir()
    for i in range(2):
        mail = EmailMessage()
        mail["From"] = "fictional@example.invalid"
        mail["Date"] = "Mon, 01 Jan 2001 12:00:00 +0000"
        mail["Subject"] = f"Synthetic audit {i}"
        mail.set_content(f"SYNTHETIC: fictional observation number {i}.")
        (source / str(i)).write_bytes(mail.as_bytes())
    corpus_path = tmp_path / "corpus.sqlite"
    replay_path = tmp_path / "replay.sqlite"
    with EmailCorpus(corpus_path) as master:
        master.ingest_directory(source)
        docs = master.search("synthetic")
        with ReplayCorpus(corpus_path, replay_path) as replay:
            arrived = replay.admit_next(1)[0]
            hidden = next(d for d in docs if d.id != arrived.id)
            ev = evidence_view(replay.evidence(arrived.id, 0, 10))
            post = {"virtual_time": replay.stats()["virtual_time"], "arrival_sequence": 1, "evidence": [ev]}
            assert audit({"posts": [post]}, corpus_path, replay_path)["passed"]
            hidden_ev = evidence_view(master.evidence(hidden.id, 0, 10))
            result = audit({"posts": [{**post, "evidence": [hidden_ev]}]}, corpus_path, replay_path)
            assert result["failures"][0]["reason"] == "not_arrived_at_post_sequence"
            # Even after later admission, replay audit must use the post's earlier watermark.
            replay.admit_next(1)
            result = audit({"posts": [{**post, "evidence": [hidden_ev]}]}, corpus_path, replay_path)
            assert result["failures"][0]["reason"] == "not_arrived_at_post_sequence"
            bad = {**ev, "quote": "invented quote"}
            result = audit({"posts": [{**post, "evidence": [bad]}]}, corpus_path, replay_path)
            assert result["failures"][0]["reason"] == "quote_mismatch"
            early = {**post, "virtual_time": "2000-12-31T00:00:00Z"}
            assert (
                audit({"posts": [early]}, corpus_path, replay_path)["failures"][0]["reason"]
                == "future_outer_date"
            )
            no_sequence = {k: v for k, v in post.items() if k != "arrival_sequence"}
            assert not audit({"posts": [no_sequence]}, corpus_path, replay_path)["passed"]
            assert not audit({"posts": []}, corpus_path, replay_path)["passed"]


def test_offline_stream_export_passes_temporal_and_exact_source_audit(tmp_path):
    import asyncio

    from swarmkit.enron.store import InvestigationStore
    from swarmkit.enron.stream import ChronologicalSwarm, StreamConfig, StreamOfflineClient

    corpus_path = tmp_path / "corpus.sqlite"
    replay_path = tmp_path / "replay.sqlite"
    fixture = Path(__file__).parent / "fixtures" / "enron_demo"
    with EmailCorpus(corpus_path) as master:
        master.ingest_directory(fixture)
    with ReplayCorpus(corpus_path, replay_path) as replay:
        engine = ChronologicalSwarm(
            replay,
            InvestigationStore(tmp_path / "forum.sqlite"),
            StreamOfflineClient(),
            StreamConfig(batch_size=3, max_windows=4, synthetic=True),
        )
        run = asyncio.run(engine.run())
        result = audit(run, corpus_path, replay_path)
        assert run["status"] == "completed"
        assert result["checked_citations"] > 0
        assert result["passed"], result["failures"]


def test_exposure_and_retrieval_events_cannot_use_later_same_time_arrivals(tmp_path):
    from copy import deepcopy

    source = tmp_path / "mail"
    source.mkdir()
    for index in range(2):
        (source / str(index)).write_text(
            "From: colleague@example.test\nDate: Mon, 1 Jan 2001 12:00:00 +0000\n"
            f"Subject: Source {index}\n\nDistinct source number {index} with enough text for a checked quote."
        )
    corpus_path, replay_path = tmp_path / "master.sqlite", tmp_path / "arrived.sqlite"
    with EmailCorpus(corpus_path) as corpus:
        corpus.ingest_directory(source)
    with ReplayCorpus(corpus_path, replay_path) as replay:
        first, second = replay.admit_next(2)
        post = {
            "virtual_time": first.date_utc,
            "arrival_sequence": 1,
            "evidence": [evidence_view(replay.evidence(first.id, 0, 20))],
        }
        events = [
            {"kind": kind, "virtual_time": first.date_utc, "arrival_sequence": 1, "document_ids": [first.id]}
            for kind in ("prompt_exposure", "historical_retrieval")
        ]
        events.append(
            {
                "kind": "historical_read",
                "virtual_time": first.date_utc,
                "arrival_sequence": 1,
                "document_id": first.id,
                "offset": 20,
            }
        )
        run = {"posts": [post], "events": events}
        result = audit(run, corpus_path, replay_path)
        assert result["passed"]
        assert result["checked_exposure_events"] == result["checked_exposure_documents"] == 3
        assert result["unique_exposure_documents"] == 1
        for index in range(3):
            bad = deepcopy(run)
            if index == 2:
                bad["events"][index]["document_id"] = second.id
            else:
                bad["events"][index]["document_ids"] = [second.id]
            result = audit(bad, corpus_path, replay_path)
            assert result["failures"][0]["reason"] == "not_arrived_at_event_sequence"
        bad = deepcopy(run)
        bad["events"][2]["offset"] = len(first.body)
        assert audit(bad, corpus_path, replay_path)["failures"][0]["reason"] == "invalid_read_offset"
        bad = deepcopy(run)
        del bad["events"][0]["arrival_sequence"]
        assert (
            audit(bad, corpus_path, replay_path)["failures"][0]["reason"]
            == "missing_or_invalid_arrival_sequence"
        )
