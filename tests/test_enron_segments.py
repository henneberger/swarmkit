from dataclasses import replace

from swarmkit.enron.schemas import EmailDocument
from swarmkit.enron.segments import parse_segments


def document(body, id='outer'):
    return EmailDocument(id, 'Outer subject', 'outer@example.invalid', (), None, 'missing', '', body,
                         'raw', 'body', 'authored', 'locator', 'family', '', (), ())


def assert_partition(doc, segments):
    assert ''.join(s.text for s in segments) == doc.body
    assert segments[0].start == 0 and segments[-1].end == len(doc.body)
    assert all(a.end == b.start for a, b in zip(segments, segments[1:], strict=False))
    assert all(doc.body[s.start:s.end] == s.text for s in segments)


def test_outlook_layout_exact_offsets_and_duplicate_forward_family():
    content = ('Ryan,\n\nI feel strongly that I cannot support\nthe valuations my group has produced so far '
               'for the LJM/Raptor\nrelated transactions without examination of all the related legal documents.\n')
    header = (' -----Original Message-----\nFrom: \tKaminski, Vince J  \n'
              'Sent:\tThursday, October 04, 2001 8:28 AM\nTo:\tSiurek, Ryan\n'
              'Cc:\tKaminski, Vince J; Buy, Rick; Port, David\nSubject:\tLJM/Raptor valuations\n')
    # Layout and short source excerpt from the archived mail, not synthetic facts.
    first = document('\n\n' + header + content)
    second = document('FYI\n' + header + '\n' + header + content, 'other')
    a, b = parse_segments(first), parse_segments(second)
    assert_partition(first, a)
    assert_partition(second, b)
    assert a[-1].claimed_sender == 'Kaminski, Vince J'
    assert a[-1].claimed_date == 'Thursday, October 04, 2001 8:28 AM'
    assert a[-1].kind == 'forwarded' and a[-1].depth == 1
    assert a[-1].source_family == b[-1].source_family
    assert b[-1].depth == 2
    assert a[-1].claimed_sender != first.sender
    assert a[1].kind == 'header'


def test_lotus_layout_recognizes_bare_sender_and_date_not_signature():
    body = ('Outer answer.\nSteve\n---------------------- Forwarded by Person/LON/ECT on 18/12/2000 \n'
            '10:27 ---------------------------\n\nSteven Leppard\n11/12/2000 09:59\n'
            'To: Person/HOU/ECT@ECT\ncc: Other Person\nSubject: Re: EnergyDesk\n'
            '\nFirst embedded body.\n\nJames New@ECT\n12/08/2000 12:38 PM\n'
            'To: Someone\ncc: Someone else\nSubject: EnergyDesk\n\nSecond embedded body.\n')
    doc = document(body)
    parts = parse_segments(doc)
    assert_partition(doc, parts)
    content = [p for p in parts if p.kind == 'forwarded']
    assert [p.claimed_sender for p in content] == ['Steven Leppard', 'James New@ECT']
    assert content[0].claimed_date == '11/12/2000 09:59'
    assert parts[0].text.endswith('Steve\n')


def test_quote_prefix_preservation_and_short_text_never_global_family():
    text = 'A sufficiently long original statement explains the operational procedure and its limitations in detail.'
    original = parse_segments(document(text))[0]
    quoted_doc = document('> ' + text, 'copy')
    quoted = parse_segments(quoted_doc)[0]
    assert_partition(quoted_doc, (quoted,))
    assert quoted.claimed_sender is None and quoted.claimed_date is None
    assert quoted.content_fingerprint == original.content_fingerprint
    assert quoted.source_family == original.source_family
    short = document('Thanks')
    assert parse_segments(short)[0].source_family != parse_segments(replace(short, id='another'))[0].source_family


def test_plain_text_dates_do_not_create_header_and_no_content_is_lost():
    doc = document('The review happened yesterday.\n12/08/2000\nThis is prose without recipient/subject headers.\n')
    parts = parse_segments(doc)
    assert len(parts) == 1 and parts[0].kind == 'authored'
    assert_partition(doc, parts)


def test_nested_quote_depths_and_blank_body():
    doc = document('Own reply\n> First quoted level\n> > Earlier quoted level\nBack to reply\n')
    parts = parse_segments(doc)
    assert_partition(doc, parts)
    assert [s.depth for s in parts if s.kind == 'quoted'] == [1, 2]
    assert all(s.claimed_sender is None for s in parts if s.kind == 'quoted')
    assert parse_segments(document('')) == ()


def test_marker_free_ccmail_inline_sender_date_keeps_outer_reply_separate():
    # Short public-corpus excerpt/layout from mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b.
    # Bodies are shortened; exact original attribution syntax is retained.
    body = ('Just received this message this very minute.  The draft already went.  Sorry.\n\n'
            'From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\n'
            'To: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n'
            'You can copy me with a blind copy.\n\n'
            'From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\n'
            'To:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n'
            'The draft is ready to go.\n')
    doc = document(body)
    parts = parse_segments(doc)
    assert_partition(doc, parts)
    assert [s.kind for s in parts] == ['authored', 'header', 'forwarded', 'header', 'forwarded']
    assert parts[0].text.startswith('Just received')
    assert parts[2].claimed_sender == 'Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL'
    assert parts[2].claimed_date == '06/18/99 11:39 AM'
    assert parts[4].claimed_sender == '"Sara Shackleton/HOU/ECT" AT ECT@ccMail'
    assert parts[4].claimed_date == '18/06/99 09:53 AM CDT'
    assert parts[2].claimed_sender != doc.sender


def test_marker_free_from_prose_without_complete_headers_is_not_a_chain():
    for body in ('From: research on 01/02/2001\nThis is a prose discussion.\n'
                 'To: another department\nSubject: our eventual meeting\n',
                 'From: a colleague\nTo: another colleague\nSubject: a header-like example without date\n'):
        doc = document(body)
        parts = parse_segments(doc)
        assert_partition(doc, parts)
        assert len(parts) == 1 and parts[0].kind == 'authored'
