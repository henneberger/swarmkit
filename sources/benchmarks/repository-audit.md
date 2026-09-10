# Benchmark repository inspection

Static inspection of selected paths; no upstream execution or full benchmark reproduction. License files and exact commits are in the [manifest](manifest.json). A downloaded checkout does not imply that external datasets or services have been configured.

| Repository / pinned code | Finding |
|---|---|
| [jwyjohn/acl26-silo-bench](https://github.com/jwyjohn/acl26-silo-bench/blob/e74127782ed1c42fff474249961f022c063d76f2/src/engine.py#L440) (`e74127782ed1`) | Loads hidden expected outputs, counts missing submissions as wrong; separate partial correctness metrics. |
| [alem-world/alem-env](https://github.com/alem-world/alem-env/blob/14d412e5ee961f9c43d6ce92ee05fee9cd1efc5e/README.md#L1) (`14d412e5ee96`) | Documents per-agent observations, messages and scratchpad. Environment infrastructure, not a small puzzle generator. |
| [MultiagentBench/MARBLE](https://github.com/MultiagentBench/MARBLE/blob/8892e9cfb69282db568e6b018f2b1cd8eec31ba6/README.md#L1) (`8892e9cfb692`) | Redirects to ulab-uiuc/MARBLE. Retained as the paper-linked historical repository. |
| [cooperbench/CooperBench](https://github.com/cooperbench/CooperBench/blob/cdd16702860bbfad28e26d17e7a679caff1a31e3/src/cooperbench/eval/evaluate.py#L310) (`cdd16702860b`) | Separate solo/cooperative patches and feature testing paths. Optional execution backend and dataset setup required. |
| [maseval/MASEval](https://github.com/maseval/MASEval/blob/b58f6f9ae27f7d0951aa33b3024f28dcf210a6ff/maseval/core/benchmark.py#L142) (`b58f6f9ae27f`) | Framework-neutral evaluation hooks and distinct setup/task/evaluation error controls. |
| [yutao1024/EntCollabBench](https://github.com/yutao1024/EntCollabBench/blob/9d085fcb86adaf20254c09e2ca35123e535a9643/scripts/judge/judge.py#L701) (`9d085fcb86ad`) | Public judge entry point requires model names and uses majority voting; reconcile with paper deterministic-grading claims before adoption. |
| [ulab-uiuc/MARBLE](https://github.com/ulab-uiuc/MARBLE/blob/8d60fa17b5596b44458a52d4296061b9fc13d6f2/marble/evaluator/evaluator.py#L331) (`8d60fa17b559`) | parse_score can default to 3 after parsing failure; some communication/planning scores are model-judged. |
