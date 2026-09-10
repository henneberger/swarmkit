"""Behavioral diagnostics distinguish routed ancestry from proposed envelopes."""
import importlib.util
import json
import sqlite3
from pathlib import Path

from swarmkit.serialization import to_data
from swarmkit.types import Evidence, Message, MessageKind, SwarmState

SPEC = importlib.util.spec_from_file_location('diagnose_inquiry', Path(__file__).parents[1] / 'scripts/diagnose_inquiry.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def event(message, sequence, day, **extra):
    return {'kind': 'peer_message', 'message_id': message.id, 'sender': message.sender,
            'recipients': list(message.recipients), 'event_sequence': sequence,
            'arrival_sequence': sequence * 10, 'virtual_time': f'2000-01-{day:02d}T00:00:00Z',
            'visibility': 'addressed', **extra}


def test_actual_request_reply_ancestry_excludes_self_envelopes_and_withheld():
    evidence = Evidence('e', 'Claim', 'doc', 'b')
    request = Message('a', 'Please inspect', ('b',), MessageKind.QUESTION, id='req',
                      metadata={'action': 'request_peer', 'inquiry_id': 'q'})
    reply = Message('b', 'Here is the source', ('a',), MessageKind.RESULT, evidence=(evidence,),
                    parents=('req',), id='reply', metadata={'action': 'reply', 'request_id': 'req', 'inquiry_id': 'q'})
    forged = Message('b', 'No ancestor', ('a',), MessageKind.RESULT, id='forged',
                     metadata={'action': 'reply', 'request_id': 'req', 'inquiry_id': 'q'})
    envelope = Message('a', 'Proposed request', ('a',), MessageKind.QUESTION, id='envelope',
                       metadata={'action': 'request_peer'})
    withheld = Message('a', 'Hidden', ('b',), MessageKind.QUESTION, id='hidden',
                       metadata={'action': 'request_peer'})
    run = {'state_snapshot': to_data(SwarmState(messages=[request, reply, forged, envelope, withheld])),
           'posts': [{'agent_id': 'a', 'action': {'kind': 'request_peer'}, 'evidence': [], 'reasoning_rejected': True},
                     {'agent_id': 'b', 'action': {'kind': 'reply'}, 'evidence': [{'id': 'e'}]}],
           'events': [event(request, 1, 1), event(reply, 3, 2), event(forged, 4, 3),
                      event(envelope, 5, 4), event(withheld, 6, 5, visibility='withheld_at_reasoner')]}
    result = MODULE.diagnose(run)
    communication = result['communication']
    assert communication['requests'] == 1
    assert communication['matched_reply_chains'] == 1
    assert communication['unmatched_replies'] == 1
    assert communication['withheld_events'] == 1
    assert communication['route_issues'] == {'broadcast_or_self_address': 1}
    assert communication['chains_sample'][0]['latency'] == {'events': 2, 'arrivals': 20, 'virtual_seconds': 86400.0}
    assert result['posts'] == {'total': 2, 'evidence_bearing': 1, 'uncited': 1, 'evidence_bearing_fraction': 0.5}
    assert result['rejected_action_counts'] == {'request_peer': 1}
    assert result['participants']['b']['evidence_bearing_posts'] == 1


def test_zero_messages_and_actions_do_not_invent_edges_or_rates():
    result = MODULE.diagnose({'posts': [{'agent_id': 'a', 'action': {'kind': 'request_peer'}}]})
    assert result['communication']['requests'] == 0
    assert result['communication']['matched_reply_chains'] == 0
    assert not result['communication']['canonical_snapshot_available']
    empty = MODULE.diagnose({})
    assert empty['posts']['evidence_bearing_fraction'] is None
    assert empty['chronology']['recorded_span_seconds'] is None
    assert empty['chronology']['arrival_fraction'] is None
    json.dumps(empty, allow_nan=False)


def test_literal_changes_and_watch_latency_use_outer_clock_not_quoted_dates():
    run = {'history': [
        {'inquiry_id': 'q', 'event_sequence': 1, 'version': 1, 'question': 'Q', 'rivals': ['A'], 'status': 'open'},
        {'inquiry_id': 'q', 'event_sequence': 2, 'version': 2, 'question': 'Q', 'rivals': ['A'], 'status': 'watching'},
        {'inquiry_id': 'q', 'event_sequence': 3, 'version': 3, 'question': 'Q', 'rivals': ['B'], 'status': 'watching'},
    ], 'events': [{'kind': 'watch_wake', 'inquiry_id': 'q', 'event_sequence': 4, 'arrival_sequence': 10,
                   'virtual_time': '2000-01-01T00:00:00Z'}],
        'posts': [{'phase': 'watch', 'inquiry_id': 'q', 'event_sequence': 5, 'arrival_sequence': 20,
                   'virtual_time': '2000-01-02T00:00:00Z', 'evidence': [{'claimed_date': '1900-01-01'}]}],
        'metrics': {'arrived': 20, 'eligible': 100, 'exposed': 2}}
    result = MODULE.diagnose(run)
    assert result['theory_records']['subsequent_versions'] == 2
    assert result['theory_records']['literal_field_changes']['rivals'] == 1
    assert result['theory_records']['literal_field_changes']['question'] == 0
    assert result['watch_activity']['temporal_association_sample'][0]['latency']['virtual_seconds'] == 86400
    assert result['chronology']['recorded_span_seconds'] == 86400
    assert result['chronology']['arrival_fraction'] == 0.2
    assert result['chronology']['model_exposed_documents'] == 2


def test_read_only_forum_clips_live_unpersisted_tail(tmp_path):
    path = tmp_path / 'forum.sqlite'
    with sqlite3.connect(path) as db:
        db.executescript('CREATE TABLE runs(id TEXT,data TEXT); CREATE TABLE posts(id INTEGER,run_id TEXT,data TEXT); CREATE TABLE events(id INTEGER,run_id TEXT,data TEXT);')
        db.execute('INSERT INTO runs VALUES (?,?)', ('r', json.dumps({'id': 'r', 'event_sequence': 2})))
        for seq in (1, 3):
            db.execute('INSERT INTO posts VALUES (?,?,?)', (seq, 'r', json.dumps({'event_sequence': seq})))
    before = path.read_bytes()
    run = MODULE.load_forum(path, 'r')
    assert run['posts'] == [{'event_sequence': 1}]
    assert run['diagnostic_snapshot_boundary']['excluded_newer_tail']['posts'] == 1
    assert path.read_bytes() == before
