from swarmkit.enron.chronicle import export_chronicle
from swarmkit.enron.cli import export_markdown, parser


def test_chronicle_preserves_discovery_order_and_companion_audit(tmp_path):
    run = {'id': 'r', 'model': 'fixture', 'status': 'completed', 'mode': 'chronological_replay',
           'posts': [{'virtual_time': '2001-01-02T00:00:00Z', 'arrival_sequence': 1,
                      'window': 1, 'agent_id': 'practice', 'text': 'Initial rule',
                      'evidence': [{'document_id': 'a', 'quote': 'exact\ntext',
                                    'metadata': {'start': 1, 'end': 11}}]},
                     {'virtual_time': '2001-01-03T00:00:00Z', 'arrival_sequence': 2,
                      'window': 2, 'agent_id': 'skeptic', 'text': 'Later exception'}]}
    path = tmp_path / 'report.md'
    export_markdown(run, path)
    assert path.read_text().index('Initial rule') < path.read_text().index('Later exception')
    assert '> exact\n> text' in path.read_text()
    assert 'arrival_sequence' in path.with_suffix('.json').read_text()


def test_replay_cli_defaults_and_offline_export(tmp_path):
    args = parser().parse_args(['replay', '--replay-id', 'small'])
    assert not args.live and not args.synthetic
    assert args.batch_size * args.max_windows >= 516182
    export_chronicle({'id': 'empty', 'posts': []}, tmp_path / 'empty.md')
    assert 'No model observations' in (tmp_path / 'empty.md').read_text()
