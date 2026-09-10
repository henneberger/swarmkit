#!/usr/bin/env python3
"""Fail before publication if staged project blobs contain credential material.

Scans staged content (not just working copies); gitlinks are intentionally not
expanded. Exact locally configured DeepSeek keys are checked even in binaries.
Only file names and detector names are printed, never matched secret text.
"""
from __future__ import annotations

import gzip
import os
import re
import subprocess
from pathlib import Path


def main() -> int:
    secrets = {os.environ.get('DEEPSEEK_API_KEY', ''), os.environ.get('DEEPSEEK_API', '')}
    for path in (Path('.env'), Path('.env.local')):
        if path.exists():
            for line in path.read_text().splitlines():
                name, sep, value = line.partition('=')
                if sep and name.strip() in {'DEEPSEEK_API_KEY', 'DEEPSEEK_API'}:
                    secrets.add(value.strip().strip('\"\''))
    secret_bytes = [key.encode() for key in secrets if len(key) >= 8]
    rules = {
        'private key': re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
        'provider key': re.compile(rb'\bsk-[A-Za-z0-9_-]{24,}\b'),
        'GitHub token': re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b'),
    }
    entries = subprocess.check_output(['git', 'ls-files', '--stage', '-z']).split(b'\0')
    failures = []
    count = 0
    for entry in entries:
        if not entry:
            continue
        metadata, raw_path = entry.split(b'\t', 1)
        mode, oid, _ = metadata.decode().split()
        if mode == '160000':
            continue
        path = raw_path.decode()
        name = Path(path).name
        if (name.startswith('.env') and name != '.env.example') or name.endswith(('.pem', '.key')):
            failures.append((path, 'credential file name'))
        blob = subprocess.check_output(['git', 'cat-file', 'blob', oid])
        if name.endswith('.gz'):
            try:
                blob = gzip.decompress(blob)
            except (OSError, EOFError):
                failures.append((path, 'invalid gzip artifact'))
        count += 1
        if any(key in blob for key in secret_bytes):
            failures.append((path, 'configured DeepSeek key'))
        for label, pattern in rules.items():
            if pattern.search(blob):
                failures.append((path, label))
    for path, detector in failures:
        print(f'BLOCKED: {path} ({detector})')
    if failures:
        return 1
    print(f'Checked {count} staged project files; no detected credentials. Submodules remain pinned references.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
