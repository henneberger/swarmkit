"""Chronological, source-backed export for the tacit-knowledge replay."""
from __future__ import annotations

import json
from pathlib import Path


def export_chronicle(run: dict, destination: Path) -> None:
    """Preserve observation order and source provenance without an extra model call."""
    lines = [
        '# Chronological swarm: tacit knowledge from arriving emails', '',
        f"Run `{run['id']}` · model `{run.get('model')}` · status **{run.get('status')}**", '',
        'The objective is to infer unwritten routines, implicit expectations, contextual exceptions, '
        'and expertise dependencies. These are provisional model interpretations, not validated '
        'organizational rules. Discovery time is the replay cursor; inline quoted dates do not '
        'backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.', '',
        'Messages admitted to searchable history greatly outnumber messages inspected by the swarm. '
        'Exact quotation checks establish source text, not the correctness of an inferred rule. '
        'Model pretraining knowledge is not controlled by the temporal retrieval boundary.', '',
        '## Protocol and resource use', '', '```json',
        json.dumps({key: value for key, value in run.items()
                    if key not in ('posts', 'events', 'wiki', 'errors')}, indent=2), '```', '',
        '## Observation timeline', '',
    ]
    previous_window = None
    for post in run.get('posts', []):
        window = post.get('window', post.get('round'))
        virtual = post.get('virtual_time', 'unknown')
        if (window, virtual) != previous_window:
            lines += [f'### {virtual} — review window {window}', '']
            previous_window = (window, virtual)
        lines += [f"**{post.get('agent_id', 'peer')} / {post.get('phase', 'observation')}**", '',
                  str(post.get('text', '')), '']
        cards = [card for card in run.get('wiki', []) if card.get('window') == window
                 and card.get('agent_id') == post.get('agent_id')
                 and card.get('phase', 'revise') == post.get('phase')]
        for card in cards:
            label = 'Candidate tacit rule' if card.get('knowledge_type') == 'tacit_hypothesis' else 'Observation'
            lines += [f"**{label} — revision {card.get('revision', 1)}**", '',
                      card.get('unwritten_rule', card.get('text', '')), '']
            for field in ('inference_gap', 'evidence_basis', 'source_counts', 'applies_when', 'exceptions', 'alternative', 'uncertainty', 'next_query', 'prediction'):
                if card.get(field):
                    lines += [f"{field.replace('_', ' ').capitalize()}: {card[field]}", '']
            lines += [f"Hypothesis `{card.get('hypothesis_id')}`; transfer tested: false.", '']
        for key in ('hypotheses', 'predictions', 'prediction_checks', 'revisions', 'retrieval_queries'):
            if post.get(key):
                lines += [f'**{key.replace("_", " ").title()}**', '',
                          '```json', json.dumps(post[key], indent=2), '```', '']
        for item in post.get('evidence', []):
            metadata = item.get('metadata', {})
            lines += [f"Source `{item.get('document_id', metadata.get('document_id', ''))}`; "
                      f"evidence `{item.get('id', '')}`; origin `{item.get('source', '')}`.", '']
            if metadata:
                lines += ['Attribution and exact offsets: `' + json.dumps(metadata, ensure_ascii=False) + '`', '']
            lines += ['> ' + str(item.get('quote', '')).replace('\n', '\n> '), '']
    if not run.get('posts'):
        lines += ['No model observations were produced.', '']
    lines += ['## Admission, gating, and retrieval audit', '',
              'The full machine-readable companion export contains the ordered event log. '
              'The following records expose selection and model-call gates.', '']
    for event in run.get('events', []):
        if event.get('kind') in ('window', 'window_admitted', 'window_skipped', 'gate', 'retrieval',
                                 'selection', 'error', 'window_complete', 'admission', 'arrival_window'):
            lines += ['```json', json.dumps(event, indent=2), '```', '']
    errors = run.get('agent_errors', run.get('errors'))
    if errors:
        lines += ['## Execution errors', '', '```json', json.dumps(errors, indent=2), '```', '']
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text('\n'.join(lines))
    destination.with_suffix('.json').write_text(json.dumps(run, indent=2))
