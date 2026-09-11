"""Offline Foundry, matched channel ablation, and one message-removal replay."""

import asyncio
import json
from dataclasses import replace

from swarmkit.benchmarks import ChannelConfig
from swarmkit.foundry import FoundryConfig, FoundryExperiment, FoundryWorld


async def run():
    world = FoundryWorld(firms=2, components=2, generations=2)
    config = FoundryConfig(communication="broadcast", checkpoint=True, turnover=0)
    experiment = FoundryExperiment(world, config)
    baseline = await experiment.run()
    silent = await FoundryExperiment(
        world, replace(config, checkpoint=False, channel=ChannelConfig(disabled=True))
    ).run()
    message_id = next(d.message_id for d in baseline.deliveries if d.status == "delivered")
    effect = await experiment.replay_without(baseline, message_id)
    return {
        "accepted_value": baseline.metrics["accepted_value"],
        "silent_accepted_value": silent.metrics["accepted_value"],
        "same_agent_calls": baseline.metrics["agent_calls"] == silent.metrics["agent_calls"],
        "suppressed_message": message_id,
        "message_effect": effect["accepted_value_effect"],
        "changed_orders": effect["changed_orders"],
        "conservation_error": baseline.metrics["ledger_conservation_error"],
    }


if __name__ == "__main__":
    print(json.dumps(asyncio.run(run()), indent=2))
