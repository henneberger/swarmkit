"""Audit export preserves replay chronology and source/communication provenance."""

import copy
import json

import pytest

from swarmkit.enron.inquiry_report import export_inquiries


def test_chronology_uses_cursor_and_occurrence_not_quoted_dates(tmp_path):
    run = {
        "id": "r1", "mode": "inquiry_swarm", "model": "fixture", "status": "watching",
        "metrics": {"arrived": 9, "scheduled_calls": 3},
        "inquiries": [{"inquiry_id": "q1", "question": "Why did the value change?",
                       "why_matters": "The repair may be transient", "rivals": ["Refresh", "Manual edit"],
                       "latest_change": "Outcome still unknown", "next_actions": ["Read the next refresh"],
                       "owner": "reader", "participants": ["reader", "challenger"], "status": "open"}],
        "posts": [
            {"agent_id": "reader", "inquiry_id": "q1", "action": "inspect", "text": "LATERPOST",
             "virtual_time": "2001-01-02T00:00:00Z", "arrival_sequence": 9,
             "created_at": "1980-01-01", "evidence": [{"document_id": "doc1", "id": "e1",
                 "quote": "From 1900: <script>alert(1)</script> **not a title**", "valid": True,
                 "metadata": {"claimed_date": "1900-01-01", "start": 4, "end": 24,
                              "raw_sha256": "rawhash", "quote_fingerprint": "fingerprint"}}]},
            {"agent_id": "reader", "inquiry_id": "q1", "action": "request_peer", "text": "SECONDPOST",
             "virtual_time": "2001-01-01T01:00:00+01:00", "arrival_sequence": 4,
             "occurrence_order": 2, "metadata": {"sender": "reader", "recipients": ["challenger"],
                                                  "visibility": "addressed", "parent_message_id": "private1"}},
            {"text": "THIRDPOST", "virtual_time": "2001-01-01T00:00:00Z", "arrival_sequence": 5},
        ],
        "history": [{"inquiry_id": "q1", "version": 2, "latest_change": "FIRSTCHANGE",
                     "virtual_time": "2001-01-01T00:00:00Z", "arrival_sequence": 4, "occurrence_order": 1}],
        "events": [
            {"kind": "private_read", "text": "FIRSTEVENT", "virtual_time": "2001-01-01T00:00:00Z",
             "arrival_sequence": 4, "occurrence_order": 0, "private": True, "message_id": "private1"},
            {"kind": "watch_wake", "text": "UNKNOWNPOSITION", "created_at": "1800-01-01", "custom": 7},
        ],
        "unknown_future_field": {"preserve": [1, 2, 3]},
    }
    original = copy.deepcopy(run)
    destination = tmp_path / "nested" / "inquiries.md"
    export_inquiries(run, destination)
    body = destination.read_text()
    positions = [body.index(word) for word in (
        "FIRSTEVENT", "FIRSTCHANGE", "SECONDPOST", "THIRDPOST", "LATERPOST", "UNKNOWNPOSITION")]
    assert positions == sorted(positions)
    assert "Replay time unavailable or invalid" in body
    assert "not establish exact within-cutoff interleaving" in body
    assert "Competing explanations" in body and "Refresh" in body and "Manual edit" in body
    assert "Outcome still unknown" in body
    assert "Recorded exchange trace" in body and '"recipients": [' in body
    assert '"private": true' in body and '"parent_message_id": "private1"' in body
    assert "Source-text check: passed; no human review recorded" in body
    assert "<script>" not in body and "&lt;script&gt;" in body
    assert "\\*\\*not a title\\*\\*" in body
    assert '"raw_sha256": "rawhash"' in body and '"start": 4' in body
    assert "Scheduled calls" in body and "rather than successful completions" in body
    assert json.loads(destination.with_suffix(".json").read_text()) == original
    assert run == original


def test_ties_keep_source_order_and_invalid_dates_do_not_backdate(tmp_path):
    run = {"id": "r", "mode": "inquiry_swarm", "posts": [
        {"text": "ONE", "virtual_time": "2000-01-01T00:00:00Z", "arrival_sequence": 0},
        {"text": "TWO", "virtual_time": "2000-01-01T00:00:00Z", "arrival_sequence": 0},
        {"text": "NAIVE", "virtual_time": "1900-01-01", "arrival_sequence": 1},
        {"text": "INVALID", "virtual_time": "not a date", "arrival_sequence": 2},
    ], "history": [{"latest_change": "THREE", "virtual_time": "2000-01-01T00:00:00Z",
                     "arrival_sequence": 0}]}
    destination = tmp_path / "report.md"
    export_inquiries(run, destination)
    body = destination.read_text()
    positions = [body.index(text) for text in ("ONE", "TWO", "THREE", "NAIVE", "INVALID")]
    assert positions == sorted(positions)
    assert "Original virtual-time value" in body


def test_empty_run_and_literal_fence_content(tmp_path):
    run = {"id": "empty", "mode": "inquiry_swarm", "inquiries": [], "history": [],
           "posts": [], "events": [], "config": {"text": "```\n<script>bad()</script>"}}
    destination = tmp_path / "empty.md"
    export_inquiries(run, destination)
    body = destination.read_text()
    assert "No inquiries were recorded" in body
    assert "No activity or theory changes were recorded" in body
    assert "````json" in body
    assert json.loads(destination.with_suffix(".json").read_text()) == run


@pytest.mark.parametrize("run", [
    {"mode": "chronological_replay"}, {"mode": "inquiry_swarm", "posts": {}},
    {"mode": "inquiry_swarm", "history": ["bad"]},
    {"mode": "inquiry_swarm", "metrics": {"cost": float("nan")}},
])
def test_invalid_snapshot_does_not_create_partial_output(tmp_path, run):
    destination = tmp_path / "bad.md"
    with pytest.raises((ValueError, TypeError)):
        export_inquiries(run, destination)
    assert not destination.exists()
    assert not destination.with_suffix(".json").exists()


def test_json_destination_cannot_overwrite_markdown_companion(tmp_path):
    with pytest.raises(ValueError, match=".json"):
        export_inquiries({"mode": "inquiry_swarm"}, tmp_path / "output.json")


def test_reader_report_summarizes_telemetry_but_complete_audit_retains_it(tmp_path):
    run = {
        "mode": "inquiry_swarm", "state_snapshot": {"memory": "HUGE_SHARED_STATE"},
        "config": {"peer_exchange": True}, "metrics": {"scheduled_calls": 2, "model_calls": 1},
        "posts": [{"text": "An investigation changed", "action": {"kind": "revise", "question": "Why?"},
                   "virtual_time": "2000-01-01T00:00:00Z", "reasoning_rejected": False}],
        "events": [
            {"kind": "prompt_exposure", "agent": "a", "document_ids": ["d1", "d1", "d2"],
             "raw_prompt": "PROMPT_TELEMETRY_ONLY"},
            {"kind": "prompt_exposure", "agent": "a", "document_ids": ["d2"]},
            {"kind": "historical_read", "document_id": "d3", "offsets": [0, 100]},
            {"kind": "peer_message", "sender": "a", "recipients": ["b"], "inquiry_id": "q1",
             "action": "request_peer", "virtual_time": "2000-01-02T00:00:00Z"},
        ],
    }
    destination = tmp_path / "readable.md"
    export_inquiries(run, destination)
    body = destination.read_text()
    assert "HUGE_SHARED_STATE" not in body
    assert "PROMPT_TELEMETRY_ONLY" not in body
    assert '"prompt_exposure": 2' in body and '"historical_read": 1' in body
    assert '"a": 2' in body
    assert "An investigation changed" in body and "**Action:** revise" in body
    assert "Reasoning rejection" not in body
    assert '"recipients": [' in body
    assert json.loads(destination.with_suffix(".json").read_text()) == run
