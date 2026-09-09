"""Exact source scope survives paging and forwarding; no inferred matter labels."""

from dataclasses import replace
from email.message import EmailMessage

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.enron.source_context import SourceContext


@pytest.fixture
def scoped_sources(tmp_path):
    folder = tmp_path / 'mail'
    folder.mkdir()
    rows = [
        ('Copper guaranty', 'mark.finch@example.invalid',
         'Use the Copper guaranty form. No unlimited guaranty was offered for Copper.'),
        ('Silver swap', 'sara.moss@example.invalid',
         'Forwarding the Silver swap question.\n\n'
         '-----Original Message-----\n'
         'From: Mark Brook <mark.brook@example.invalid>\n'
         'Sent: January 30, 2001 10:00\n'
         'To: Sara Moss\n'
         'Subject: Silver swap draft\n\n'
         'Ask the bank whether it needs a guarantee for Silver. '
         + 'The draft remains under review. ' * 35),
        ('Unattributed note', 'mark.finch@example.invalid',
         'An unattributed quotation follows.\n\n'
         '> The recipient has not yet confirmed this separate draft arrangement.\n'),
    ]
    for index, (subject, sender, body) in enumerate(rows):
        mail = EmailMessage()
        mail['Subject'] = subject
        mail['From'] = sender
        mail['To'] = 'reader@example.invalid'
        mail['Date'] = f'Thu, 01 Feb 2001 0{index + 1}:00:00 +0000'
        mail['X-Synthetic-Fixture'] = 'true'
        mail.set_content(body)
        (folder / str(index)).write_bytes(mail.as_bytes())
    master = tmp_path / 'master.sqlite'
    with EmailCorpus(master) as corpus:
        corpus.ingest_directory(folder)
    with ReplayCorpus(master, tmp_path / 'arrived.sqlite') as replay:
        docs = {doc.subject: doc for doc in replay.admit_next(3)}
        yield replay, docs


def test_different_matters_and_shared_first_names_keep_exact_scope(scoped_sources):
    replay, docs = scoped_sources
    views, refs = SourceContext(replay).build(list(docs.values()))
    copper = next(e for e in refs.values() if e.metadata['outer_subject'] == 'Copper guaranty')
    silver = next(e for e in refs.values() if e.metadata['kind'] == 'forwarded')
    assert copper.metadata['outer_sender'] == 'mark.finch@example.invalid'
    assert silver.metadata['outer_sender'] == 'sara.moss@example.invalid'
    assert silver.metadata['claimed_sender'] == 'Mark Brook <mark.brook@example.invalid>'
    assert silver.metadata['claimed_subject'] == 'Silver swap draft'
    assert silver.metadata['outer_subject'] == 'Silver swap'
    assert silver.metadata['claimed_date'] == 'January 30, 2001 10:00'
    assert silver.metadata['outer_date'].startswith('2001-02-01')
    assert silver.metadata['outer_recipients'] == docs['Silver swap'].recipients
    assert silver.metadata['segment_start'] <= silver.metadata['start']
    assert silver.metadata['end'] <= silver.metadata['segment_end']
    assert silver.metadata['attribution_confidence']
    assert 'topic' not in silver.metadata
    for view in views:
        for segment in view['segments']:
            evidence = refs[segment['span_id']]
            for key in ('outer_subject', 'outer_sender', 'claimed_subject', 'claimed_sender', 'kind'):
                assert segment[key] == evidence.metadata[key]
            assert segment['text'] == evidence.metadata['quote']
            assert replay.verify_evidence(evidence)


def test_continuation_retains_forward_scope_and_unknown_speaker_stays_unknown(scoped_sources):
    replay, docs = scoped_sources
    context = SourceContext(replay)
    _, refs = context.build([docs['Silver swap']])
    first = next(e for e in refs.values() if e.metadata['kind'] == 'forwarded')
    assert first.metadata['excerpt_truncated']
    offset = first.metadata['end']
    views, continued = context.build([docs['Silver swap']], {docs['Silver swap'].id: offset})
    later = next(iter(continued.values()))
    assert later.metadata['start'] == offset
    assert views[0]['segments'][0]['starts_mid_segment']
    for key in ('outer_subject', 'claimed_subject', 'claimed_sender', 'kind', 'segment_id'):
        assert later.metadata[key] == first.metadata[key]
    _, unknown = context.build([docs['Unattributed note']])
    quote = next(e for e in unknown.values() if e.metadata['kind'] == 'quoted')
    assert quote.metadata['claimed_sender'] is None
    assert quote.metadata['outer_sender'] == 'mark.finch@example.invalid'
    assert quote.metadata['ambiguities']


def test_document_text_cannot_disagree_with_its_resolved_citation(scoped_sources):
    replay, docs = scoped_sources
    original = docs['Copper guaranty']
    tampered = replace(original, body=original.body.replace('Copper', 'Silver'))
    with pytest.raises(ValueError, match='differs from canonical'):
        SourceContext(replay).build([tampered])
