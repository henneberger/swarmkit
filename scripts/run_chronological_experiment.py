#!/usr/bin/env python3
"""Run a small replay, audit it, then permit a fresh full chronological replay.

This script preserves the shared ledger and never changes its limits. It uses
fresh membership names; existing replay names are rejected by the application.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--workspace', type=Path, default=Path('var/enron'))
    parser.add_argument('--ledger', type=Path, default=Path('var/api-ledger.sqlite'))
    parser.add_argument('--prefix', default='chronological')
    parser.add_argument('--reports', type=Path, default=Path('reports'))
    parser.add_argument('--documents-per-window', type=int, default=32)
    args = parser.parse_args()
    if not args.live:
        parser.error('--live is required for paid experiments')
    for suffix in ('small', 'full'):
        if (args.workspace / 'replays' / f'{args.prefix}-{suffix}.sqlite').exists():
            parser.error('Replay state already exists; use a new prefix. No state was deleted.')
    from audit_replay import audit

    for suffix, batch, windows in (('small', 2000, 2), ('full', 22000, 24)):
        name = f'{args.prefix}-{suffix}'
        output = args.reports / f'{name}.md'
        subprocess.run([sys.executable, '-m', 'swarmkit.enron.cli', '--workspace', str(args.workspace),
                        '--ledger', str(args.ledger), 'replay', '--live', '--replay-id', name,
                        '--batch-size', str(batch), '--max-windows', str(windows),
                        '--documents-per-window', str(args.documents_per_window),
                        '--export', str(output)], check=True)
        result = json.loads(output.with_suffix('.json').read_text())
        checked = audit(result, args.workspace / 'corpus.sqlite',
                        args.workspace / 'replays' / f'{name}.sqlite')
        output.with_suffix('.audit.json').write_text(json.dumps(checked, indent=2))
        if (not checked['passed'] or result.get('agent_errors')
                or result.get('quote_checks', {}).get('rejected', 0)
                or (suffix == 'small' and result.get('reasoning_rejections', 0))
                or (suffix == 'full' and result['status'] not in ('completed', 'completed_with_rejections'))):
            raise SystemExit('Small/full replay validation failed; remaining stages were not started.')
        print(json.dumps({'stage': suffix, 'audit': checked}), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
