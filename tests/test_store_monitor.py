from swarmkit.enron.store import InvestigationStore


def test_monitor_bounds_activity_without_changing_canonical_run(tmp_path):
    store = InvestigationStore(tmp_path / 'forum.sqlite')
    store.save_run({'id': 'r', 'status': 'running', 'metrics': {'arrived': 4000},
                    'state_snapshot': {'private': 'retained'}, 'resume_state': {'cursor': 4},
                    'history': [{'version': 1}], 'inquiries': [{'question': 'why'}]})
    for i in range(205):
        store.post('r', {'sequence': i})
    summary = store.monitor_runs()[0]
    assert summary['metrics']['arrived'] == 4000
    assert 'state_snapshot' not in summary and 'history' not in summary
    detail = store.monitor_run('r')
    assert len(detail['posts']) == 200
    assert detail['posts'][0]['sequence'] == 5
    assert detail['posts'][-1]['sequence'] == 204
    assert detail['monitor_truncation']['posts'] == {'total': 205, 'shown': 200}
    assert 'state_snapshot' not in detail
    assert detail['history'] == [{'version': 1}]
    canonical = store.run('r')
    assert len(canonical['posts']) == 205
    assert canonical['state_snapshot'] == {'private': 'retained'}
    assert store.monitor_run("r' OR 1=1 --") is None
