#!/usr/bin/env python3
"""Read-only behavioral counts for inquiry runs; no semantic truth scoring."""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from swarmkit.serialization import from_data  # noqa: E402
from swarmkit.types import MessageKind, SwarmState  # noqa: E402


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return parsed.timestamp() if parsed.utcoffset() is not None else None
    except (AttributeError, ValueError, TypeError):
        return None


def kind(post):
    action = post.get('action', {})
    return action.get('kind', 'unreported') if isinstance(action, dict) else str(action)


def latency(start, end):
    result = {}
    for field, label in [('event_sequence', 'events'), ('arrival_sequence', 'arrivals')]:
        a, b = start.get(field), end.get(field)
        if type(a) is int and type(b) is int and b >= a:
            result[label] = b - a
    for field, label in [('virtual_time', 'virtual_seconds'), ('created_at', 'wall_seconds')]:
        a, b = timestamp(start.get(field)), timestamp(end.get(field))
        if a is not None and b is not None and b >= a:
            result[label] = b - a
    return result


def diagnose(run):
    """Count recorded acts; a proposed action is never itself a routed message."""
    posts, events, history = (run.get(key, []) for key in ('posts', 'events', 'history'))
    participants = defaultdict(lambda: Counter(posts=0, evidence_bearing_posts=0, rejected_posts=0))
    for peer in run.get('peers', []):
        participants[peer.get('id') if isinstance(peer, dict) else str(peer)]
    action_counts, rejected_counts = Counter(), Counter()
    for post in posts:
        who = post.get('agent_id', post.get('agent', 'unreported'))
        participants[who]['posts'] += 1
        participants[who]['evidence_bearing_posts'] += bool(post.get('evidence'))
        rejected = bool(post.get('reasoning_rejected') or post.get('reasoning_rejection'))
        participants[who]['rejected_posts'] += rejected
        action_counts[kind(post)] += 1
        if rejected:
            rejected_counts[kind(post)] += 1
    messages, snapshot_available = {}, False
    try:
        state = from_data(run.get('state_snapshot'))
        if isinstance(state, SwarmState):
            snapshot_available = True
            messages = {m.id: m for m in state.messages}
    except (ValueError, TypeError, KeyError):
        pass
    routed, route_issues, withheld = {}, Counter(), 0
    for event in events:
        if event.get('kind') != 'peer_message':
            continue
        if event.get('visibility') == 'withheld_at_reasoner':
            withheld += 1
            continue
        message = messages.get(event.get('message_id'))
        if message is None:
            route_issues['missing_canonical_message'] += 1
            continue
        if message.sender != event.get('sender') or list(message.recipients) != event.get('recipients'):
            route_issues['event_canonical_address_mismatch'] += 1
            continue
        if not message.recipients or message.sender in message.recipients:
            route_issues['broadcast_or_self_address'] += 1
            continue
        if message.id in routed:
            route_issues['duplicate_message_event'] += 1
            continue
        routed[message.id] = (message, event)
    requests = {mid: pair for mid, pair in routed.items()
                if pair[0].kind == MessageKind.QUESTION and pair[0].metadata.get('action') == 'request_peer'}
    replies = {mid: pair for mid, pair in routed.items() if pair[0].metadata.get('action') == 'reply'}
    chains, unmatched = [], 0
    answered = set()
    for mid, (reply, event) in replies.items():
        request_id = reply.metadata.get('request_id')
        pair = requests.get(request_id)
        if not pair or request_id not in reply.parents:
            unmatched += 1
            continue
        request, request_event = pair
        before, after = request_event.get('event_sequence'), event.get('event_sequence')
        if (reply.sender not in request.recipients or reply.recipients != (request.sender,)
                or reply.metadata.get('inquiry_id') != request.metadata.get('inquiry_id')
                or type(before) is not int or type(after) is not int or after <= before):
            unmatched += 1
            continue
        answered.add(request_id)
        chains.append({'request_id': request_id, 'reply_id': mid, 'requester': request.sender,
                       'responder': reply.sender, 'inquiry_id': request.metadata.get('inquiry_id'),
                       'reply_has_evidence': bool(reply.evidence), 'latency': latency(request_event, event)})
    revisions, changes, previous = 0, Counter(), {}
    fields = ('question', 'rivals', 'unresolved_premise', 'latest_change', 'evidence_ids', 'participants', 'status')
    for row in sorted(history, key=lambda r: r.get('event_sequence', 0)):
        iid = row.get('inquiry_id')
        if iid in previous:
            revisions += 1
            for field in fields:
                changes[field] += previous[iid].get(field) != row.get(field)
        previous[iid] = row
    # This is a temporal association, not a causal claim: events lack assignment IDs.
    wakes = [e for e in events if e.get('kind') == 'watch_wake']
    watch_posts = [p for p in posts if p.get('phase') == 'watch']
    associations = []
    for wake in wakes:
        sequence = wake.get('event_sequence')
        candidates = [p for p in watch_posts if p.get('inquiry_id') == wake.get('inquiry_id')
                      and type(sequence) is int and type(p.get('event_sequence')) is int
                      and p['event_sequence'] > sequence]
        if candidates:
            following = min(candidates, key=lambda p: p['event_sequence'])
            associations.append({'wake_event_sequence': sequence,
                                 'following_post_event_sequence': following['event_sequence'],
                                 'latency': latency(wake, following)})
    rows = posts + events + history
    clocks = [timestamp(row.get('virtual_time')) for row in rows]
    clocks = [v for v in clocks if v is not None]
    start, end = (min(clocks), max(clocks)) if clocks else (None, None)
    metrics = run.get('metrics', {})
    arrived, eligible = metrics.get('arrived'), metrics.get('eligible')
    evidence_posts = sum(bool(p.get('evidence')) for p in posts)
    return {
        'run_id': run.get('id'), 'status': run.get('status'), 'interim': run.get('status') == 'running',
        'captured_at': datetime.now(timezone.utc).isoformat(),
        'boundary': run.get('diagnostic_snapshot_boundary', 'supplied JSON snapshot'),
        'posts': {'total': len(posts), 'evidence_bearing': evidence_posts, 'uncited': len(posts) - evidence_posts,
                  'evidence_bearing_fraction': evidence_posts / len(posts) if posts else None},
        'proposed_action_counts': dict(action_counts), 'rejected_action_counts': dict(rejected_counts),
        'participants': dict(participants),
        'communication': {'canonical_snapshot_available': snapshot_available,
                          'routed_distinct_peer_messages': len(routed), 'withheld_events': withheld,
                          'route_issues': dict(route_issues), 'requests': len(requests), 'replies': len(replies),
                          'answered_requests': len(answered), 'unanswered_requests': len(requests) - len(answered),
                          'matched_reply_chains': len(chains), 'unmatched_replies': unmatched,
                          'chains_sample': chains[:20], 'sample_limit': 20},
        'theory_records': {'inquiries_in_history': len(previous), 'artifact_versions': len(history),
                           'subsequent_versions': revisions, 'literal_field_changes': dict(changes)},
        'watch_activity': {'wakes': len(wakes), 'watch_phase_posts': len(watch_posts),
                           'wakes_with_later_same_inquiry_watch_post': len(associations),
                           'temporal_association_sample': associations[:20], 'sample_limit': 20},
        'chronology': {'first_record_virtual_time': datetime.fromtimestamp(start, timezone.utc).isoformat() if start is not None else None,
                       'last_record_virtual_time': datetime.fromtimestamp(end, timezone.utc).isoformat() if end is not None else None,
                       'recorded_span_seconds': end - start if start is not None else None,
                       'missing_or_invalid_record_clocks': len(rows) - len(clocks),
                       'arrived': arrived, 'eligible': eligible,
                       'arrival_fraction': arrived / eligible if type(arrived) is int and type(eligible) is int and eligible > 0 else None,
                       'model_exposed_documents': metrics.get('exposed')},
        'limitations': [
            'Evidence-bearing means a nonempty citation list, not valid or sufficient support; run the provenance auditor separately.',
            'Proposed actions include rejected requests. Only canonical, distinctly addressed message events count as routed exchange.',
            'Reply chains establish recorded ancestry and addresses, not that the receiver used, understood, or benefited from a reply.',
            'Version and literal-field changes do not certify a substantive theory revision or successful discovery.',
            'Watch latency is to the next same-inquiry watch-phase post, not a verified assignment link; several wakes can share a post.',
            'Recorded virtual span excludes unlogged periods; arrival coverage is not complete model reading or private-context isolation.',
        ],
    }


def load_forum(path, run_id):
    """Consistent read transaction, clipped to the persisted state watermark."""
    with sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro', uri=True) as db:
        db.execute('BEGIN')
        row = db.execute('SELECT data FROM runs WHERE id=?', (run_id,)).fetchone()
        if row is None:
            raise ValueError('unknown run ID')
        run = json.loads(row[0])
        cutoff = run.get('event_sequence')
        excluded = {}
        for table in ('posts', 'events'):
            records = [json.loads(r[0]) for r in db.execute(
                f'SELECT data FROM {table} WHERE run_id=? ORDER BY id', (run_id,))]
            run[table] = [r for r in records if type(cutoff) is not int or r.get('event_sequence', 0) <= cutoff]
            excluded[table] = len(records) - len(run[table])
        run['diagnostic_snapshot_boundary'] = {'event_sequence': cutoff, 'excluded_newer_tail': excluded}
        return run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--run', type=Path, help='Full exported run JSON (not a bounded monitor view)')
    source.add_argument('--forum', type=Path, help='Read-only SQLite forum')
    parser.add_argument('--run-id')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.forum and not args.run_id:
        parser.error('--forum requires --run-id')
    run = load_forum(args.forum, args.run_id) if args.forum else json.loads(args.run.read_text())
    if run.get('mode') != 'inquiry_swarm' or run.get('monitor_truncation'):
        parser.error('a full inquiry_swarm snapshot is required')
    report = json.dumps(diagnose(run), indent=2, allow_nan=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    else:
        print(report, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
