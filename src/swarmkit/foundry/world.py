"""Generated, evaluator-owned device physics and public order contracts.

Three component qualities plus a genuine three-way interaction determine quality.
The simulator is synthetic, deterministic, and independent of language judgments.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass

from ..types import Evidence

ROLES = ("sensor", "power", "firmware")


def keyed(seed, *parts):
    raw = hashlib.sha256(repr((seed, parts)).encode()).digest()
    return int.from_bytes(raw[:8], "big") / 2**64


def fact_id(version, topic):
    return f"v{version}:{topic}"


@dataclass(frozen=True)
class FoundryWorld:
    seed: int = 0
    split: str = "test"
    firms: int = 4
    components: int = 3
    generations: int = 4
    change_every: int = 2

    def __post_init__(self):
        for name in ("firms", "components", "generations", "change_every"):
            value = getattr(self, name)
            if type(value) is not int or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        if self.firms < 2 or self.components < 2 or self.components > 8:
            raise ValueError("at least two firms; component count between 2 and 8")
        if type(self.seed) is not int or self.seed < 0 or not self.split:
            raise ValueError("nonnegative seed and nonempty split required")

    @property
    def id(self):
        return hashlib.sha256(repr(self).encode()).hexdigest()[:20]

    @property
    def agents(self):
        return tuple(f"firm{f}.{role}" for f in range(self.firms) for role in ROLES)

    @property
    def recipes(self):
        return tuple(itertools.product(range(self.components), repeat=3))

    def version(self, generation):
        return generation // self.change_every

    def topics(self):
        return tuple(f"{role}/{i}" for role in ROLES for i in range(self.components)) + tuple(
            "interaction/" + ",".join(map(str, recipe)) for recipe in self.recipes
        )

    @staticmethod
    def topic_role(topic):
        return topic.split("/")[0] if not topic.startswith("interaction/") else "firmware"

    def value(self, version, topic):
        if topic not in self.topics():
            raise ValueError("unknown experiment topic")
        draw = keyed(self.seed, self.split, "physics", version, topic)
        return int(draw * 21) - 12 if topic.startswith("interaction/") else 4 + int(draw * 8)

    def card(self, version, topic):
        # Evaluator-issued measurements; IDs encode topics, never their values or seeds.
        owner = self.owner(topic)
        return Evidence(
            fact_id(version, topic),
            json.dumps(
                {"topic": topic, "value": self.value(version, topic), "version": version}, sort_keys=True
            ),
            f"bench:{version}:{topic}",
            owner,
            metadata={"version": version, "topic": topic},
        )

    def owner(self, topic):
        firm = min(self.firms - 1, int(keyed(self.seed, self.split, "owner", topic) * self.firms))
        return f"firm{firm}.{self.topic_role(topic)}"

    def private(self, agent, version):
        return tuple(self.card(version, topic) for topic in self.topics() if self.owner(topic) == agent)

    def cost(self, agent):
        return 1 + int(keyed(self.seed, self.split, "cost", agent) * 4)

    def quality(self, version, recipe):
        self.validate_recipe(recipe)
        return sum(
            self.value(version, f"{role}/{c}") for role, c in zip(ROLES, recipe, strict=True)
        ) + self.value(version, "interaction/" + ",".join(map(str, recipe)))

    def validate_recipe(self, recipe):
        if (
            not isinstance(recipe, (list, tuple))
            or len(recipe) != 3
            or any(type(c) is not int or not 0 <= c < self.components for c in recipe)
        ):
            raise ValueError("recipe requires three legal integer component choices")

    def required(self, version, recipe):
        self.validate_recipe(recipe)
        return tuple(fact_id(version, f"{role}/{c}") for role, c in zip(ROLES, recipe, strict=True)) + (
            fact_id(version, "interaction/" + ",".join(map(str, recipe))),
        )

    def orders(self, generation):
        version = self.version(generation)
        optimum = max(self.quality(version, r) for r in self.recipes)
        return tuple(
            {
                "id": f"order:{generation}:{firm}",
                "coordinator": f"firm{firm}.sensor",
                "threshold": optimum - 2 - (firm % 2),
                "value": 50 + 5 * firm,
                "deadline": 6 + 2 * self.firms,
                "budget": 30.0,
            }
            for firm in range(self.firms)
        )

    def verify(self, generation, recipe, completion, order):
        quality = self.quality(self.version(generation), recipe)
        return {
            "quality": quality,
            "valid_device": quality >= order["threshold"],
            "on_time": completion <= order["deadline"],
            "success": quality >= order["threshold"] and completion <= order["deadline"],
        }
