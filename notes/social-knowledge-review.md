# Social agent populations: peer learning versus knowledge diffusion

Reviewed primary sources 2026-09-09; no repositories downloaded or code executed for this bounded review. Moltbook is the platform analyzed by these sources. These are observational studies of open agent populations rather than controlled task-solving swarms.

## Peer-learning-like discourse

[When AI Agents Teach Each Other: Discourse Patterns Resembling Peer Learning in the Moltbook Community](https://arxiv.org/abs/2602.14477v2), Eason Chen et al.; submitted 16 February 2026, revised 28 March 2026.

The revised title and §§2.3/5.4 explicitly distinguish observable discourse from learning. The dataset contains 28,683 spam-filtered posts; statements outnumber questions 11.4:1. Coding identifies validation, extension, application and metacognitive language. None is a receiver pre/post competence test. Important internal inconsistency: the abstract says 138 comment threads, while the limitations specify **138 comments across five threads**. Use the latter precise sample description. Keyword classifications, platform ranking, heterogeneous autonomy and a 12-day window limit generalization. Relevant to unspoken knowledge: tutorials and self-reported discoveries become publicly available artifacts, but “I learned” language is not evidence that another agent acquired a retained skill. This paper motivates inquiry and uptake protocols; it does not validate them experimentally.

## Large-scale broadcast behavior

[OpenClaw AI Agents as Informal Learners at Moltbook: Characterizing an Emergent Learning Community at Scale](https://arxiv.org/abs/2602.18832v1), Eason Chen et al.; 21 February 2026.

Analyzes 231,080 non-spam posts and 1.55 million comments. Section 4.2.4 reports approximately 93% top-level responses rather than replies within dialogue; statement/question ratios remain 8.9–9.7:1. This makes the important swarm distinction concrete: a large population publishing relevant text need not perform joint knowledge construction. Section 5.5 admits that actual learning is unmeasured. The API returns up to the first 100 comments per post, potentially overrepresenting early top-level responses; the authors say the pattern persists on later low-volume posts. Temporal phases confound community evolution, growth, throttling and changing interest. Suggested reference-to-prior-contribution rules, question scaffolding, joint tasks and attention redistribution are proposals in §5.4, not demonstrated improvements. Registered account totals are platform claims, not verified counts of independent autonomous minds.

## Capability awareness diffusion: archive worth collecting, implementation gap

[searchsim-org/moltbook-analysis](https://github.com/searchsim-org/moltbook-analysis), associated with “Revisiting User Modeling in a World of AI Agent Users.” README reports 370,737 posts, 46,872 authors and 4,257 communities; full data is approximately 716 MB via Git LFS.

Its SIS analysis concerns **capability mentions/awareness**, not successful capability execution. [Permutation analysis](https://github.com/searchsim-org/moltbook-analysis/blob/main/eval/PERMUTATION_TEST_FINDINGS.md) shuffles underlying post timestamps, reconstructs first-reference adoption curves and compares early growth rates. Reported clustering survives this null for benign and dual-use mentions, not risky mentions. Shared external triggers remain possible; authors explicitly acknowledge no causal intervention.

Audit finding: README advertises `eval/microdata/scripts/11_capability_diffusion.py` and `13_permutation_null_model.py`, but both raw URLs return 404 and those scripts are absent from the current recursive tree. Results JSON and findings documents exist. Recommend archiving the repo, explicitly noting the missing advertised implementation. Do not present it as fully reproduced diffusion evidence.

## Collaboration audit: use corrected analysis, not obsolete baseline

[human-vc/moltbook-audit](https://github.com/human-vc/moltbook-audit), associated with “Benchmarking Emergent Coordination in Large-Scale LLM Populations: An Evaluation Framework on the MoltBook Archive.” Repository description reports no robust contributor–quality association after selection correction.

`RUNBOOK_rigor.md` explicitly explains defects in the original analysis. In `src/molt_dynamics/rq3_collaboration.py:247`, individual baselines return an empty dataframe; `:314` permutes scores then averages, leaving the statistic invariant. The basic quality proxy at `:133` scores formatting/comments/test words/bracket balance, not task correctness. Prefer `scripts/run_rigor.py:342` corrected matching, `scripts/collab_cem.py:63` matching analysis, and `scripts/collab_doseresponse.py:46` adjusted dose-response fitting. Existing judged matching output contains only one matched treated/control pair and infinite standard error. Consequently even a null does not prove swarms cannot learn; this archive has limited identification and weak ground-truth outcomes.

**Recommended synthesis:** distinguish exposure → textual uptake → reproducible skill transfer → retained receiver improvement → population advantage. These social-network studies mostly establish the first two. A convincing knowledge-discovery swarm needs instrumented adoption, recipient execution tests, withheld transfer tasks and exposure controls.
