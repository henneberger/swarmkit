from email.message import EmailMessage

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.replay import ReplayCorpus


def build(tmp_path):
    folder = tmp_path / 'mail'
    folder.mkdir()
    bodies = [('first', 'Mon, 01 Jan 2001 12:00:00 +0000', 'Initial status: ordinary review pending.'),
              ('tie', 'Mon, 01 Jan 2001 12:00:00 +0000', 'Different status at the same timestamp.'),
              ('corrected', 'Tue, 02 Jan 2001 12:00:00 +0000', 'Correction: the earlier status is withdrawn.'),
              ('forward', 'Wed, 03 Jan 2001 12:00:00 +0000',
               '-----Original Message-----\nFrom: Earlier Person\nSent: January 1, 1998\n'
               'To: Reader\nSubject: Status\nAn older claim becomes visible only when forwarded now.'),
              ('unknown', '', 'Undated status unknown.'),
              ('outside', 'Thu, 01 Jan 1998 12:00:00 +0000', 'Quarantined status.')]
    for name, date, body in bodies:
        mail = EmailMessage()
        mail['From'] = 'author@example.invalid'
        mail['Subject'] = name + ' status'
        mail['Message-ID'] = '<' + name + '@example.invalid>'
        if date:
            mail['Date'] = date
        mail.set_content(body)
        (folder / name).write_bytes(mail.as_bytes())
    master = tmp_path / 'corpus.sqlite'
    with EmailCorpus(master) as corpus:
        corpus.ingest_directory(folder)
        docs = {d.subject.split()[0]: d for d in corpus.search('status')}
        future = docs['corrected']
        evidence = corpus.evidence(future.id, 0, 10)
    return master, docs, evidence


def test_exact_arrival_membership_blocks_ties_corrections_and_evidence(tmp_path):
    master, docs, future_evidence = build(tmp_path)
    with ReplayCorpus(master, tmp_path / 'replay.sqlite') as replay:
        assert replay.search('status') == []
        assert replay.get(docs['corrected'].id) is None
        assert not replay.verify_evidence(future_evidence)
        with pytest.raises(KeyError):
            replay.segments(docs['corrected'].id)
        first = replay.admit_next(1)[0]
        tie = next(d for d in (docs['first'], docs['tie']) if d.id != first.id)
        assert replay.get(tie.id) is None
        assert [d.id for d in replay.search('status', cutoff='2002-12-31')] == [first.id]
        assert replay.admit_next(1)[0].id == tie.id
        replay.admit_next(1)
        assert replay.verify_evidence(future_evidence)
        assert len(replay.search('status', cutoff='2001-01-01')) == 2
        assert replay.search('correction', cutoff='2001-01-01') == []
        assert replay.get(docs['forward'].id) is None
        replay.admit_next(1)
        segment = replay.segments(docs['forward'].id)[-1]
        assert segment.claimed_date == 'January 1, 1998'
        assert replay.observation(docs['forward'].id)['date_utc'].startswith('2001-01-03')
        assert replay.get(docs['unknown'].id) is None
        assert replay.get(docs['outside'].id) is None
        assert replay.stats()['quarantined'] == 2
        assert replay.stats()['unknown_dates'] == 1
        assert replay.stats()['complete']
        assert replay.admit_next() == []


def test_persistence_readonly_master_and_bound_validation(tmp_path):
    master, docs, _ = build(tmp_path)
    path = tmp_path / 'replay.sqlite'
    with ReplayCorpus(master, path) as replay:
        arrivals = replay.admit_next_metadata(2)
        assert [r['sequence'] for r in arrivals] == [1, 2]
        assert 'body' not in arrivals[0]
        import sqlite3
        with pytest.raises(sqlite3.OperationalError, match='readonly'):
            replay._db.execute('DELETE FROM archive.documents')
    with ReplayCorpus(master, path) as resumed:
        assert resumed.count() == 2
        assert resumed.admit_next(1)[0].id == docs['corrected'].id
        with pytest.raises(ValueError):
            resumed.search('status', cutoff='2001-01-01T12:00:00')
        with pytest.raises(ValueError):
            resumed.admit_next(-1)
        assert resumed.admit_next(0) == []
    with pytest.raises(ValueError, match='differs'):
        ReplayCorpus(master, path, end='2001-01-01')
    for start, end in [(None, '2002-12-31'), ('2002-01-01', '2001-01-01')]:
        with pytest.raises(ValueError):
            ReplayCorpus(master, tmp_path / 'invalid.sqlite', start=start, end=end)


def test_cutoff_and_arrival_filter_apply_before_limit(tmp_path):
    master, docs, _ = build(tmp_path)
    with ReplayCorpus(master, tmp_path / 'replay.sqlite') as replay:
        admitted = replay.admit_next(2)
        assert len(replay.search('status', limit=2)) == 2
        assert {d.id for d in replay.search('status', limit=2)} == {d.id for d in admitted}
        assert replay.search('status " OR *', match='all') == []
        assert replay.search('status', limit=0) == []
        assert replay.get(docs['corrected'].id) is None


def test_bounded_window_admission_and_local_fts_has_no_future_text(tmp_path):
    master, _, _ = build(tmp_path)
    with ReplayCorpus(master, tmp_path / 'replay.sqlite') as replay:
        assert replay.peek_next_date() == '2001-01-01T12:00:00+00:00'
        assert replay.admit_until('2000-12-31') == []
        assert len(replay.admit_until('2001-01-01', batch_size=1)) == 1
        assert replay.peek_next_date() == '2001-01-01T12:00:00+00:00'
        assert len(replay.admit_until('2001-01-01', batch_size=1)) == 1
        assert replay.admit_until('2001-01-01') == []
        assert replay.peek_next_date() == '2001-01-02T12:00:00+00:00'
        # Ranking index itself contains no unarrived correction, not merely
        # a post-ranking output filter against the complete archive.
        assert replay._db.execute('SELECT count(*) FROM arrived_fts').fetchone()[0] == 2
        assert replay._db.execute("SELECT count(*) FROM arrived_fts WHERE arrived_fts MATCH 'correction'").fetchone()[0] == 0
        with pytest.raises(ValueError):
            replay.admit_until(None)
