from __future__ import annotations

import hashlib
import io
import tarfile
from dataclasses import replace
from datetime import datetime
from email import policy
from email.message import EmailMessage
from pathlib import Path

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.knowledge import EvidenceRegistry

FIXTURE = Path(__file__).parent / 'fixtures' / 'enron_demo'


def mail(body='A sufficiently long authored observation records an ordinary operational approval '
              'and requests that the supporting documentation remain available for review.', *,
         message_id='one', date='Mon, 05 Feb 2001 09:00:00 -0600', subject='Approval', html=False):
    message = EmailMessage(policy=policy.SMTP)
    message['From'] = 'Fictional Author <author@example.invalid>'
    message['To'] = 'Fictional Reader <reader@example.invalid>'
    message['Subject'] = subject
    message['Message-ID'] = f'<{message_id}@example.invalid>'
    if date:
        message['Date'] = date
    message.set_content(body, subtype='html' if html else 'plain', charset='utf-8')
    return message.as_bytes()


def test_fixture_index_search_thread_cutoff_and_status(tmp_path):
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        stats = corpus.ingest_directory(FIXTURE)
        assert stats.inserted == 12 and stats.skipped == 0
        assert corpus.stats()['documents'] == 12
        assert corpus.stats()['synthetic_documents'] == 12
        assert corpus.stats()['raw_bytes'] > 0
        docs = corpus.search('Harbor approval', match='all')
        assert len(docs) == 4 and all(doc.synthetic for doc in docs)
        assert len(corpus.thread(docs[0].id)) == 4
        assert all(doc.thread_basis == 'header_links' for doc in corpus.thread(docs[0].id))
        old = corpus.search('Harbor', cutoff='2001-02-05')
        assert len(old) == 2
        assert all(doc.date_utc <= '2001-02-05T23:59:59+00:00' for doc in old)
        assert corpus.around(old[0].id, window_days=2)
        assert corpus.search('Beacon', cutoff='2001-02-05') == []
        assert len(corpus.search('Harbor Beacon')) == 8
        assert corpus.search('Harbor Beacon', match='all') == []
        assert corpus.get('missing') is None


def test_raw_snapshot_and_exact_unicode_offsets_survive_source_change(tmp_path):
    original = mail('The café ledger records Ω units; verify this exact quotation, not a paraphrase.')
    source = tmp_path / 'source'
    source.mkdir()
    file = source / 'email'
    file.write_bytes(original)
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(source)
        document = corpus.search('café')[0]
        assert document.raw_sha256 == hashlib.sha256(original).hexdigest()
        start = document.body.index('café')
        end = start + len('café ledger records Ω units')
        evidence = corpus.evidence(document.id, start, end)
        assert corpus.verify_evidence(evidence)
        assert evidence.metadata['quote'] == 'café ledger records Ω units'
        file.write_bytes(mail('A replacement message is not the indexed immutable source.'))
        assert corpus.raw(document.id) == original
        assert corpus.verify_evidence(evidence)
        bad = replace(evidence, metadata={**evidence.metadata, 'end': end + 1})
        assert not corpus.verify_evidence(bad)
        assert not corpus.verify_evidence(replace(evidence, source='invented-source'))
        with pytest.raises(ValueError):
            corpus.evidence(document.id, True, 20)


def test_raw_and_authored_duplicates_do_not_inflate_source_count(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    raw = mail()
    (source / 'a.eml').write_bytes(raw)
    (source / 'copy.eml').write_bytes(raw)
    (source / 'resent.eml').write_bytes(mail(message_id='two'))
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        result = corpus.ingest_directory(source)
        assert result.inserted == 2 and result.duplicates == 1
        docs = corpus.search('approval')
        assert len({d.source_family for d in docs}) == 1
        assert sorted(len(d.raw_locators) for d in docs) == [1, 2]
        cards = [corpus.evidence(d.id, 0, 50, owner=f'peer-{i}', supports=('review',))
                 for i, d in enumerate(docs)]
        registry = EvidenceRegistry(cards)
        assert registry.scores(('review',)) == {'review': 1}
        assert corpus.ingest_directory(source).duplicates == 3
        assert corpus.count() == 2
        assert corpus.stats()['raw_copies'] == 3
        # Different interpretations of the same span are different cards, same origin.
        other = corpus.evidence(docs[0].id, 0, 50, claim='A hypothesis', owner='another-peer')
        registry.add(other)
        assert len(registry.independent_sources()) == 1


def test_streaming_tar_skips_traversal_links_and_limits_without_extracting(tmp_path):
    archive = tmp_path / 'input.tar.gz'
    with tarfile.open(archive, 'w:gz') as tar:
        for name in ('../../outside.eml', '/absolute.eml', 'maildir/good.eml'):
            raw = mail(message_id=name.replace('/', 'x'))
            info = tarfile.TarInfo(name)
            info.size = len(raw)
            tar.addfile(info, io.BytesIO(raw))
        link = tarfile.TarInfo('maildir/link')
        link.type = tarfile.SYMTYPE
        link.linkname = '/etc/passwd'
        tar.addfile(link)
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        stats = corpus.ingest_tar(archive)
        assert stats.inserted == 1 and stats.skipped == 3
        assert corpus.count() == 1
        assert '!/maildir/good.eml' in corpus.search('approval')[0].raw_locator
        assert not (tmp_path / 'maildir').exists()
        assert corpus.ingest_tar(archive, limit=0).attempted == 0
        assert corpus.ingest_tar(archive, limit=1).duplicates == 1


def test_mime_plain_preferred_attachments_excluded_html_is_inert(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    message = EmailMessage()
    message['From'] = 'author@example.invalid'
    message['Subject'] = 'Mixed'
    message.set_content('The preferred plaintext body includes the stable observation.')
    message.add_alternative('<p>Alternative hidden body</p>', subtype='html')
    message.add_attachment('Attachmentsecret should not be part of the body.', filename='note.txt')
    (source / 'mixed').write_bytes(message.as_bytes())
    (source / 'html').write_bytes(mail('<script>EXECUTESECRET()</script><p>Visible &amp; inert text</p>',
                                      html=True, message_id='html'))
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(source)
        assert corpus.search('preferred')
        assert not corpus.search('Attachmentsecret')
        assert not corpus.search('Alternative')
        html = corpus.search('Visible')[0]
        assert 'Visible & inert text' in html.body
        assert 'EXECUTESECRET' not in html.body


def test_ambiguous_dates_never_pass_temporal_cutoff(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    (source / 'valid').write_bytes(mail(message_id='valid'))
    (source / 'ambiguous').write_bytes(mail(message_id='ambiguous', date='Mon, 05 Feb 2001 09:00:00 -0000'))
    (source / 'missing').write_bytes(mail(message_id='missing', date=''))
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(source)
        assert len(corpus.search('approval')) == 3
        dated = corpus.search('approval', cutoff='2001-02-05T16:00:00Z')
        assert len(dated) == 1 and dated[0].date_utc == '2001-02-05T15:00:00+00:00'
        assert corpus.stats()['ambiguous_dates'] == 2
        with pytest.raises(ValueError):
            corpus.search('approval', cutoff=datetime(2001, 2, 5))


def test_bounded_literal_fts_handles_operators_without_sql_or_fts_execution(tmp_path):
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(FIXTURE, limit=3)
        assert corpus.count() == 3
        for query in ('" OR * NEAR(', "'; DROP TABLE documents; --", 'body:approval', '()"*'):
            assert isinstance(corpus.search(query, limit=1), list)
        assert corpus.count() == 3
        assert corpus.search('', limit=0) == []
        for limit in (-1, 201, True):
            with pytest.raises(ValueError):
                corpus.search('approval', limit=limit)
        with pytest.raises(ValueError):
            corpus.search('x' * 2049)
        with pytest.raises(ValueError):
            corpus.search(' '.join(['word'] * 33))


def test_subject_thread_fallback_is_labeled_and_cutoff_does_not_leak_future(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    (source / 'a').write_bytes(mail(message_id='a', subject='Routine note'))
    (source / 'b').write_bytes(mail(message_id='b', subject='Re: Routine note',
                                  date='Tue, 06 Feb 2001 09:00:00 -0600'))
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(source)
        early = corpus.search('routine', cutoff='2001-02-05')[0]
        thread = corpus.thread(early.id)
        assert len(thread) == 2
        assert {d.thread_basis for d in thread} == {'subject_time_heuristic'}
        assert len(corpus.thread(early.id, cutoff='2001-02-05')) == 1
        later = next(d for d in thread if d.id != early.id)
        assert corpus.around(later.id, cutoff='2001-02-05') == []


def test_rank_streaming_matches_bm25_scores_and_filters_before_limit(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    # Future high-frequency matches outrank the historical matches; they must
    # not consume a top-k budget before the temporal predicate is applied.
    for i in range(12):
        date = 'Mon, 05 Feb 2001 09:00:00 -0600' if i < 5 else 'Tue, 06 Feb 2001 09:00:00 -0600'
        body = ('rareterm ' * (i + 1)) + ('filler ' * (30 - i))
        (source / str(i)).write_bytes(mail(body, message_id=str(i), date=date, subject='Ranking fixture'))
    with EmailCorpus(tmp_path / 'corpus.db') as corpus:
        corpus.ingest_directory(source)
        for cutoff in (None, '2001-02-05'):
            params = ['"rareterm"']
            sql = ('SELECT d.id,bm25(document_fts) AS score FROM document_fts f '
                   'JOIN documents d ON d.id=f.doc_id WHERE document_fts MATCH ?')
            if cutoff:
                sql += ' AND d.date_utc<=?'
                params.append('2001-02-05T23:59:59+00:00')
            expected = corpus._db.execute(sql + ' ORDER BY score,d.id LIMIT 3', params).fetchall()
            assert len({row['score'] for row in expected}) == 3
            assert [doc.id for doc in corpus.search('rareterm', limit=3, cutoff=cutoff)] == [
                row['id'] for row in expected]
        assert len(corpus.search('rareterm', limit=8, cutoff='2001-02-05')) == 5
        assert len(corpus.search('rareterm', limit=8)) == 8
