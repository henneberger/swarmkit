# Communication evaluation research sources

Collected 10 September 2026 for the [communication evaluation guide](../../docs/COMMUNICATION_EVALUATION.md). Use this supplement when designing experiments with message routing, gating, compression and communication ablations in SwarmKit.

| Paper | Why read it | Local copy |
|---|---|---|
| [On the Pitfalls of Measuring Emergent Communication](https://arxiv.org/abs/1903.05168) | Distinguishes signaling from actual effects on receivers | [PDF](papers/1903.05168/paper.pdf), [text](papers/1903.05168/paper.txt) |
| [Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1810.08647) | Counterfactual influence on other agents' actions | [PDF](papers/1810.08647/paper.pdf), [text](papers/1810.08647/paper.txt) |
| [TarMAC: Targeted Multi-Agent Communication](https://arxiv.org/abs/1810.11187) | Learning whom to address and what to communicate | [PDF](papers/1810.11187/paper.pdf), [text](papers/1810.11187/paper.txt) |
| [Learning when to Communicate at Scale in Multiagent Cooperative and Competitive Tasks](https://arxiv.org/abs/1812.09755) | Learned communication gating | [PDF](papers/1812.09755/paper.pdf), [text](papers/1812.09755/paper.txt) |

The [existing benchmark archive](../benchmarks/README.md) supplies the recent language-agent studies used in the guide, including HiddenBench, SILO-BENCH, CooperBench and Debate or Vote. This supplement adds foundational communication research; it is not a separate claim to cover all current benchmarks.

[Collection plan](collection-plan.json) records requested sources. [Manifest](manifest.json) and per-paper `record.json` files record retrieval times, resolved URLs and SHA-256 hashes. Each paper directory includes an abstract-page snapshot and extracted text as well as its PDF. Extracted text may contain layout artifacts; consult the PDF for equations and tables.

Downloads use the existing `scripts/collect_economic_games.py` collector with its `BASE` set to this directory. To verify the recorded source hashes from the repository root:

```sh
python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import collect_economic_games as collector
collector.BASE = Path.cwd() / 'sources/communication-evaluation'
sys.argv = ['collect_economic_games.py', '--verify']
collector.main()
PY
```

All upstream material retains its original rights and terms; see [third-party notices](../../THIRD_PARTY_NOTICES.md). These are research references, not bundled algorithm implementations.
