# What the integrated Foundry experiment revealed

The useful result is a picture of how the whole organization behaved, rather than a ranking of communication protocols. These observations come from live DeepSeek V4.1 Flash (`deepseek-flash`) decisions, actual simulator events and retained API traces.

## Knowledge became organizational memory

The experiment connected private investigation, communication, partner matching, independent commitments, physical verification and a shared archive. Agents used messages to propose complete recipes and request commitments from complementary specialists. Published devices and retained notes gave later decisions a shared reference point. Across the 48 primary episodes, the simulator recorded 462 cultural-transfer adoptions and 185 published successful recipes, with one successful recipe withheld. Some first-pass accepted devices involved invalid fallback commitments; these counts describe that observed trajectory, not a corrected causal estimate.

This suggests that the organizational unit worth studying is a reusable, verified plan plus the people committed to executing it. Individual messages are part of that process rather than its sole product. This is an interpretation of the traces, not proof that every archive adoption improved a decision.

## Memory also carried obsolete assumptions forward

A concrete baseline trace is `primary-1102-shared-disrupted-targeted`, agent `firm0.sensor`. At step 4 it retained a coordinated recipe with measured quality 28. At step 8, after physics changed to version 1, it still used that old result as its starting point and declined a fresh query because the components had been queried in the previous generation. At step 12 it resumed investigation while trying to negotiate a complete revised recipe.

The whole-system tension is preservation versus revision: a common plan helps people agree, but prior success can make obsolete evidence persuasive. Verification established truth for a particular physics version; agents did not consistently preserve that distinction in their reasoning. The episode supports studying revalidation and institutional forgetting alongside knowledge retention. It does not establish that archives generally harm adaptation.

## Organizational habits persisted more than economic strategies changed

The agents largely maintained familiar teams: 278 awarded teams stayed within a firm and six crossed firm boundaries. All 999 valid first-round bids in the primary episodes were 3, the example value in the response schema. No forecast trades occurred. Publication was overwhelmingly the default.

The economic machinery therefore functioned mostly as the organization’s operating rules. It did not produce observable price discovery, active forecasting markets or substantial strategic withholding in this run. Example anchoring is a plausible explanation for fixed bids, but the experiment does not isolate its cause. Giving agents economic choices did not itself make those choices an active part of their strategy.

## Collective investigation did not automatically divide the work

The primary episodes dispatched 971 investigations, of which 592 repeated a topic already investigated in that physics version. The duplication counter concerns dispatched research, not the initial allocation of facts. Agents could coordinate recipes while still duplicating the work used to discover them. Agreement on what to build and agreement on who should investigate what were distinct organizational problems.

## Overall interpretation

We observed a small research organization built around shared plans, familiar partners and accumulated knowledge. The most interesting interaction was between coordination and institutional memory: the same mechanisms that made collective action possible could also preserve old assumptions. A diverse strategic economy did not emerge merely from composing many economic mechanisms.

These findings identify what an integrated continuation would need to explain: how discoveries become commitments, how institutions divide investigation, when knowledge should be revalidated, and what makes agents actually use economic choices. They are not a request to start more experiments; this run is closed.

## Execution record

The first pass completed all 48 primary episodes, all six mixed-population episodes and ten of twelve interventions: 64 of 66 planned episodes. Two intervention episodes ended with provider errors. The persistent gate recorded 6,566 attempts and $11.6921 in conservative charged/reserved cost, including development and 12 requests with unknown outcomes. No requests remained active at closure.

An audit found that invalid final responses could accidentally earn value through a default component choice. Commit `3fb47d2` fixes that behavior and adds a regression test. The planned corrected full replay did not start because the first pass was incomplete. We consequently do not present these first-pass numbers as a fully corrected study. The observations above describe the recorded organization; they are not clean estimates of causal contributions or a validated strategy ranking.

The full local record remains in `var/foundry/test-v1/`, including `manifest.json`, `summary.json`, `episodes/` and `responses/`. The original implementation is preserved in `fdf54db`. The [experimental contract](../FOUNDRY_MODEL_EXPERIMENT.md) describes the design and development changes.
