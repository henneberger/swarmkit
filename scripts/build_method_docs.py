"""Regenerate the public algorithm/fidelity table from the executable registry."""
from pathlib import Path
import inspect
from swarmkit.catalog import methods, resolve

root = Path(__file__).resolve().parents[1]
rows = [
    '# Algorithm and method catalog', '',
    'This table is generated from `swarmkit.catalog.methods()`. All listed targets are importable implementations. Runtime protocols and shared records are described in [API.md](API.md).', '',
    'Fidelity labels: **primitive** is general infrastructure; **mechanism** implements the stated local operation; **component** supplies one part of a larger method; **adaptation** changes the published method for a common API; **baseline** is a deliberately simpler comparator; **design** is an explicit synthesis; **metric** measures a limited property. **implemented_core** is a self-contained economic component; **numpy_adaptation** is a small numerical research adaptation; **callback_training** executes caller-supplied learning; **optional_adapter** invokes an external solver. None claims to reproduce a paper’s full experimental results.', '',
    f'There are **{len(methods())} registered entries**. Some entries expose several operations (for example graph sampling, learning and pruning).', '',
]
for family in dict.fromkeys(item.family for item in methods()):
    rows += ['## '+family.replace('_',' ').title(), '',
             '| Registry name / API | Implemented operation | Fidelity and limits | Sources |',
             '|---|---|---|---|']
    for item in methods(family):
        implementation = resolve(item.name)
        file = Path(inspect.getsourcefile(implementation)).relative_to(root)
        line = inspect.getsourcelines(implementation)[1]
        source = ' · '.join(f'[source {i+1}]({url})' for i,url in enumerate(item.sources)) or 'General primitive'
        rows.append(f'| `{item.name}` · [{item.target}](../{file}#L{line}) | {item.description} | **{item.fidelity}**. {item.limitations} | {source} |')
    rows.append('')
rows += [
    '## What the package does not bundle', '',
    'Provider credentials, proprietary orchestration checkpoints, full transformer training stacks, model-specific hidden-state extraction, complete robot/world simulators, large benchmark datasets and upstream services are not bundled. Callbacks provide task-specific model inference, evaluation, decomposition, mutation and abstraction generation. These are explicit extension points, not silently successful placeholders.', '',
    'For arbitrary transformer training, use the reward and policy primitives as components of an external trainer. For latent channels, supply actual aligned model states and evaluate downstream behavior. For scientific discovery, provide independent artifact validators and held-out tasks.', '',
    'The research-to-code mapping emphasizes mechanisms relevant to swarms. Platform observation studies inform metrics and controls; their results are not represented as algorithms that reproduce an entire social network.', '',
]
(root/'docs/METHODS.md').write_text('\n'.join(rows))
