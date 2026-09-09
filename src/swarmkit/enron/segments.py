"""Conservative Outlook/Lotus Notes chain segmentation; never authenticate inline headers.

Segments partition the immutable decoded body. Header attribution is claimed text,
not verified sender identity. Unsupported delimiters remain explicitly ambiguous.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import replace

from .schemas import EmailDocument, EmailSegment

_MARKER = re.compile(r'^\s*(?:-{2,}\s*Original Message\s*-*|[-_]{2,}\s*Forwarded by\b|Begin forwarded message:)', re.I)
_HEADER = re.compile(r'^\s*(From|Sent|Date|To|Cc|Subject):\s*(.*)$', re.I)
_DATE = re.compile(r'\b(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b')


def parse_segments(document: EmailDocument) -> tuple[EmailSegment, ...]:
    """Partition decoded body into exact header/content spans; preserve every character.

    Recognizes common Outlook markers and Lotus Notes sender/date/To/Subject
    blocks. Nested ``>`` prefixes produce quoted spans with unknown attribution
    unless a recognized inline header supplies it. No human date interpretation
    is inferred for ambiguous inline dates. Families identify matching normalized
    content only, never independent corroboration or matching authorship.
    """
    body = document.body
    lines = body.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    output = []
    sender, date, subject = document.sender or None, document.raw_date or None, document.subject or None
    kind, depth = 'authored', 0

    def emit(a, b, segment_kind, current_depth, who, when, title, ambiguities):
        if a == b:
            return
        text = body[offsets[a]:offsets[b]]
        # Prefix stripping is only for dependence fingerprinting, never quote offsets.
        normalized = ' '.join(re.sub(r'^\s*(?:>\s*)+', '', text, flags=re.M).split())
        fingerprint = hashlib.sha256(normalized.encode()).hexdigest()
        substantial = len(normalized) >= 80 and len(normalized.split()) >= 10
        family = ('enron-segment:' + fingerprint if substantial and segment_kind != 'header'
                  else f'enron-span:{document.id}:{offsets[a]}:{offsets[b]}')
        output.append(EmailSegment(
            document.id, f'{document.id}:segment:{offsets[a]}:{offsets[b]}', offsets[a], offsets[b],
            text, segment_kind, who, when, title, current_depth,
            'heuristic' if current_depth or segment_kind == 'header' else 'outer_header_claim',
            tuple(ambiguities), fingerprint, family))

    def clean(line):
        return re.sub(r'^\s*(?:>\s*)+', '', line).rstrip('\r\n')

    def quote_level(line):
        match = re.match(r'^\s*((?:>\s*)+)', line)
        return match.group(1).count('>') if match else 0

    i = 0
    start = 0
    while i < len(lines):
        line = clean(lines[i])
        marker = bool(_MARKER.match(line))
        from_start = bool(re.match(r'^\s*From:\s*\S', line, re.I))
        # Lotus Notes embeds bare sender + numeric date + To/cc/Subject without a marker.
        block_end = None
        fields = {}
        if marker or from_start or (line.strip() and not _HEADER.match(line) and i + 1 < len(lines)
                      and _DATE.match(clean(lines[i + 1]).strip())):
            saw_recipient = False
            saw_date = False
            for j in range(i + (1 if marker else 0), min(len(lines), i + 45)):
                candidate = clean(lines[j])
                header = _HEADER.match(candidate)
                if header:
                    key, value = header.groups()
                    fields[key.lower()] = value.strip()
                    if key.lower() == 'from':
                        inline_date = re.match(r'^(.*?)\s+on\s+(\d{1,2}/\d{1,2}/\d{2,4}\b.*)$',
                                               value.strip(), re.I)
                        if inline_date:
                            fields['from'], fields['date'] = inline_date.groups()
                            saw_date = True
                    if key.lower() in ('sent', 'date') and value.strip():
                        saw_date = True
                    saw_recipient |= key.lower() == 'to'
                    if key.lower() == 'subject':
                        block_end = j + 1
                        break
                elif _DATE.search(candidate):
                    saw_date = True
                    fields.setdefault('date', candidate.strip())
                elif (candidate.strip() and not fields.get('from') and j + 1 < len(lines)
                      and _DATE.match(clean(lines[j + 1]).strip())):
                    fields['from'] = candidate.strip()
                elif from_start and candidate.strip() and not candidate[0].isspace():
                    # A header-looking prose sentence must not absorb later body
                    # paragraphs merely because they happen to contain To/Subject.
                    break
            if not marker and not (block_end and saw_recipient and saw_date):
                block_end = None
        if block_end is not None:
            emit(start, i, kind, depth, sender, date, subject,
                 ['inline attribution unverified'] if depth else [])
            depth += 1
            sender = fields.get('from') or None
            date = fields.get('sent') or fields.get('date') or None
            subject = fields.get('subject') or None
            emit(i, block_end, 'header', depth, sender, date, subject,
                 ['inline attribution unverified', 'inline date retained verbatim; timezone/order not inferred'])
            kind = 'forwarded'
            i = block_end
            start = i
            continue
        quote_depth = quote_level(lines[i])
        if quote_depth:
            emit(start, i, kind, depth, sender, date, subject,
                 ['inline attribution unverified'] if depth else [])
            end = i + 1
            while end < len(lines) and quote_level(lines[end]) == quote_depth:
                end += 1
            emit(i, end, 'quoted', max(depth, quote_depth), None, None, None,
                 ['quoted speaker/date unknown', 'quote prefixes retained in exact text'])
            start = end
            i = end
            continue
        i += 1
    emit(start, len(lines), kind, depth, sender, date, subject,
         ['inline attribution unverified'] if depth else [])
    # A body with no recognized chain syntax is still only an outer-header claim.
    return tuple(replace(s, ambiguities=s.ambiguities + ('unsupported inline formats may remain',))
                 for s in output)
