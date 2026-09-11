# Integrated agent communication experiment

## Question and unit of analysis

Which communication institutions let a model-agent economy discover, coordinate, deliver and retain useful knowledge, and how do those effects change with incentives and disruption? The experimental unit is a complete four-generation world, not an individual message or order.

This is an exploratory integrated study. Three held-out world seeds support paired descriptive comparisons, not a definitive strategy ranking or a powered significance claim. Every decision uses DeepSeek V4.1 Flash through the `deepseek-flash` API alias, temperature 0, thinking disabled, JSON output. The API alias can change; each response's model identifier, request ID, time and usage are retained. Temperature zero is not a deterministic-provider guarantee.

## Frozen design

Development uses seed 901 in the `dev` split: a pooled-information feasibility condition and a private-observation condition. Prompt/schema repairs are allowed only here and are recorded before freezing the test manifest. Test seeds are 1101, 1102 and 1103 in the `test` split. No prompt or strategy tuning uses test outcomes.

The primary design is **4 communication institutions × 2 incentives × 2 environments × 3 worlds = 48 episodes**:

- Broadcast; agent-selected targeted communication; a coordinator hub with the same observations and call allowance as everyone else; and broadcast agents with message delivery disabled. No hardcoded disclosure, research or design policy chooses their actions.
- Shared verified value minus real costs; or each agent's own net return. Artifact access and contract rules stay the same under both objectives.
- Stable environment; or a disruption bundle (physics change halfway through, 50% turnover, 10% message loss, and one equipment slot). The environmental comparison estimates the bundle, not each constituent effect.

Each episode has six agents in two firms, two component choices per specialty, four generations and four synchronous rounds. It includes model-chosen bids, two-sided partner rankings with deferred acceptance, verified Contract Net payments, an LMSR forecast market, private research, complementary three-party production, equipment/material constraints, trust feedback, publication decisions, an expiring public artifact archive and cultural transfer. The remaining library methods are available as extensions; they are not all forced into this experiment.

Round 0 bids and investigates; round 1 ranks partners after bid reveal and received messages; round 2 coordinates the awarded team; round 3 commits independently to component choices and publication. Research results and messages arrive after the action that generated them. Final-round messages cannot affect current production. All participants receive the same number of model decision opportunities.

The model may withhold information, refuse partnerships, stop investigating, speculate in the market or decline publication. None of these is automatically scored as incorrect. Invalid JSON/action schemas are recorded as failed turns with no research/messages, refusal of contracts and no publication; a numerical solving policy never takes over. There are no automatic repair calls to give one condition more inference opportunities.

## One program, with explanatory comparisons

Alongside the primary factorial:

- Cross-play mixes broadcast and targeted populations across firms under private incentives and disruption, evaluating both assignments on each held-out world. Homogeneous counterparts reuse primary runs. Population payoffs feed AlphaRank and the empirical PSRO meta-solver; no learned best-response claim is made.
- Targeted/disrupted conditions in each incentive regime are rerun with archive access disabled on the same worlds (six episodes).
- The same six conditions receive a predeclared message intervention: suppress the earliest delivered message carrying evidence, with message ID breaking ties. If none exists, report the intervention unavailable rather than choosing a favorable message. Exact-context responses are reused; changed contexts make fresh provider calls. These are coupled exploratory interventions, not proof that provider stochasticity is eliminated.

These treatments keep the complete economic task. They explain cooperation, coordination and retention within it rather than replacing it with isolated puzzles.

## Measurement and inference budget

Primary outcome: total independently accepted order value. Also record actual execution/research costs, net social payoff, individual surplus, coordination mismatches, evidence exposure, unsuccessful contract formation, repeated experiments, publication and artifact adoption, recovery by generation, message traffic, protocol failures, model input/output tokens, cached replay calls and wall time.

Per callback: one request, the same output-token ceiling, the same prompt-byte cap, and no provider retries. Context overflow removes oldest message text then oldest artifacts, explicitly recording omissions; private measurement cards remain. Different protocols inherently change received information and actual token use. Report their realized costs rather than claim identical actual spend. A persistent shared gate caps the entire program at **$15 conservative upper-bound API cost, 10,000 attempts and 30 million charged/reserved tokens**, including development, failed calls and interventions. The gate retains its historical $0.44/$1.32 per-million bound, above V4.1's published peak $0.30/$1.20 prices; it does not estimate the exact cache/time-discounted invoice.

Primary communication differences are paired against silent control within incentive/environment/world. Report protocol × incentive and protocol × environment difference-in-differences across the same world seeds. Bootstrap whole worlds, never orders/messages. Cross-play reports the finite evaluated population only. Production value is not API dollars; no arbitrary currency conversion is imposed.

## Reproduction and evidence

Run development and then the held-out phase:

```sh
python -m swarmkit.foundry.model_study --phase dev --output var/foundry/my-development
python -m swarmkit.foundry.model_study --phase test --development var/foundry/my-development --output var/foundry/my-test
```

Set `DEEPSEEK_API_KEY` or `DEEPSEEK_API` in the process environment. Each phase writes its manifest before any episode calls. Development passes only when pooled-information success is at least 50% and each development episode has at most 10% invalid actions. Test startup verifies that the agent, provider and environment sources match development. Full prompts, model responses, decisions and simulator outcomes stay in the ignored output directory. Existing completed episodes and exact-context responses are reused on restart only under the same manifest. A changed implementation requires a new output directory.

The primary matrix has 48 episodes. Cross-play adds six mixed episodes while reusing six homogeneous primary episodes; archive and message interventions add six each, for 66 planned held-out episodes. Each has 96 logical model callbacks. Replays can reuse recorded callbacks, so logical token totals differ from newly billed API usage. The shared gate reports actual new attempts and conservative charged/reserved usage across the whole program.

Development interface repairs: the first calibration rejected optional message IDs/sender fields copied from inboxes. The adapter now discards caller-supplied IDs and verifies optional sender identity. The second rejected citations of visible artifacts as if they were forged component measurements; these now remain artifact-reference metadata, with no invented measurement cards. One remaining malformed JSON response was counted as an invalid turn. No decision policy was replaced with a scripted solver.

Transport/provider failures stop the affected episode and prevent a complete-results claim. Other in-flight requests finish and remain accounted for. Study summaries expose incomplete episodes. A credential is never included in a prompt, manifest or report.

## Use the components for your own experiment

The fixed study is a reproducible starting design. For a custom world or population, compose the adapter directly:

```python
import asyncio
from swarmkit.foundry import FoundryConfig, FoundryExperiment, FoundryWorld
from swarmkit.foundry.model_agents import ModelScientist
from swarmkit.providers.deepseek import DeepSeekClient, GateLimits, SQLiteCallGate

async def run():
    gate = SQLiteCallGate("var/my-foundry.sqlite", enabled=True,
                          limits=GateLimits(max_calls=120, max_tokens=1_000_000, max_usd=1))
    client = DeepSeekClient(gate=gate)
    world = FoundryWorld(seed=7, firms=2, components=2, generations=4)
    config = FoundryConfig(rounds=4, agent_teams=True, agent_publication=True,
                           artifact_visibility="public", agent_concurrency=4,
                           trust_reported_usage=True)
    experiment = FoundryExperiment(world, config)
    agents = {a: ModelScientist(client, protocol="targeted", directory="var/my-traces",
                               namespace="custom-world-7") for a in world.agents}
    result = await experiment.run(agents)
    return result.report()

report = asyncio.run(run())
```

Change the world, protocol population and institution together when testing a new hypothesis, and keep a matched control. `ModelScientist.prompt()` is the prompt construction boundary; `parse()` validates actions and `act()` records usage and responses. A new protocol implementation or prompt is a new treatment and needs its own development checks and frozen manifest. The model receives task observations only, not repository access or an external tool-execution sandbox.

Generate shareable result artifacts after a complete held-out run with `python scripts/report_foundry_models.py var/foundry/my-test`. This optional reporting script uses Matplotlib; the simulator and live runner still require only the library's core dependencies.

Model/version and pricing sources, checked September 10, 2026: [DeepSeek release](https://deepseek.com/en/news/deepseek-v4-1-flash/) and [official pricing](https://api-docs.deepseek.com/quick_start/pricing/).
