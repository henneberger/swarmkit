# Swarm benchmark research archive

Research date: 10 September 2026. See the [research review](../../docs/BENCHMARK_RESEARCH.md) and [eight-track suite specification](../../docs/BENCHMARK_SUITE.md). These are research and evaluation designs, not installed benchmark implementations.

Archived 16 papers and 7 Git checkouts. Full checkouts are Git-ignored; their recorded commits can be restored with the collector. Root README/license snapshots remain trackable. No upstream experiments were run.

- [Collection plan](collection-plan.json)
- [Manifest with hashes and commits](manifest.json)
- [Repository audit](repository-audit.md)
- [Machine-readable evaluation specifications](suite-spec.json)

Run from the repository root:

```sh
python3 scripts/collect_benchmarks.py
python3 scripts/collect_benchmarks.py --verify
```

Collection needs network access and `pdftotext`. Verification checks archived artifact hashes and checkout commits locally. Existing completed snapshots are preserved. Source documents retain their original rights and are excluded from Python package distributions.

## New paper snapshots

| Paper | PDF | Text | Status |
|---|---|---|---|
| [AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation](https://arxiv.org/abs/2512.03466v1) | [PDF](papers/2512.03466v1/paper.pdf) | [Text](papers/2512.03466v1/paper.txt) | ok |
| [Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems](https://arxiv.org/abs/2603.01045v2) | [PDF](papers/2603.01045v2/paper.pdf) | [Text](papers/2603.01045v2/paper.txt) | ok |
| [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340v1) | [PDF](papers/2606.08340v1/paper.pdf) | [Text](papers/2606.08340v1/paper.txt) | ok |
| [MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents](https://arxiv.org/abs/2503.01935v1) | [PDF](papers/2503.01935v1/paper.pdf) | [Text](papers/2503.01935v1/paper.txt) | ok |
| [Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://arxiv.org/abs/2502.20073v3) | [PDF](papers/2502.20073v3/paper.pdf) | [Text](papers/2502.20073v3/paper.txt) | ok |
| [Scalable Evaluation of Multi-Agent Reinforcement Learning with Melting Pot](https://arxiv.org/abs/2107.06857v1) | [PDF](papers/2107.06857v1/paper.pdf) | [Text](papers/2107.06857v1/paper.txt) | ok |
| [CooperBench: Why Coding Agents Cannot be Your Teammates Yet](https://arxiv.org/abs/2601.13295) | [PDF](papers/2601.13295/paper.pdf) | [Text](papers/2601.13295/paper.txt) | ok |
| [MASEval: Extending Multi-Agent Evaluation from Models to Systems](https://arxiv.org/abs/2603.08835) | [PDF](papers/2603.08835/paper.pdf) | [Text](papers/2603.08835/paper.txt) | ok |
| [Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows](https://arxiv.org/abs/2605.08761) | [PDF](papers/2605.08761/paper.pdf) | [Text](papers/2605.08761/paper.txt) | ok |
| [Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments](https://arxiv.org/abs/2602.11964) | [PDF](papers/2602.11964/paper.pdf) | [Text](papers/2602.11964/paper.txt) | ok |
| [TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2511.05269) | [PDF](papers/2511.05269/paper.pdf) | [Text](papers/2511.05269/paper.txt) | ok |
| [DPBench: Structural Determinants of Multi-Agent LLM Coordination Under Simultaneous Resource Contention](https://arxiv.org/abs/2602.13255) | [PDF](papers/2602.13255/paper.pdf) | [Text](papers/2602.13255/paper.txt) | ok |
| [MEAL: A Benchmark for Continual Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2506.14990) | [PDF](papers/2506.14990/paper.pdf) | [Text](papers/2506.14990/paper.txt) | ok |
| [SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2212.07489) | [PDF](papers/2212.07489/paper.pdf) | [Text](papers/2212.07489/paper.txt) | ok |
| [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080) | [PDF](papers/2410.05080/paper.pdf) | [Text](papers/2410.05080/paper.txt) | ok |
| [DiscoveryBench: Towards Data-Driven Discovery with Large Language Models](https://arxiv.org/abs/2407.01725) | [PDF](papers/2407.01725/paper.pdf) | [Text](papers/2407.01725/paper.txt) | ok |

## Existing sources reused

The review also uses sources already archived in this repo: HiddenBench (`sources/papers/2505.11556`), SwarmBench (`sources/papers/2505.04364`), the scaling study (`sources/papers/2512.08296`), equal-budget reasoning (`sources/papers/2604.02460`), Debate or Vote (`sources/papers/2508.17536`), and the [economic-games collection](../economic-games/README.md). Consult their existing records for versions and provenance.

An initial request for nonexistent revision `2503.01935v2` failed. The corrected `v1` PDF and page are in the manifest; the failed request record is retained in `papers/2503.01935v2/record.json`.
