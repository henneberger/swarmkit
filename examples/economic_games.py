"""Offline verified team procurement and complementary bundle allocation.

Run: python examples/economic_games.py
"""

import json

from swarmkit.economics import (
    CombinatorialAuction,
    ContractNet,
    Ledger,
    NormalFormGame,
    RepeatedGame,
    VCGPayments,
    fixed,
    tit_for_tat,
)
from swarmkit.types import Artifact, Feedback


def run():
    ledger = Ledger({"manager": 20, "scout": 0, "analyst": 0, "reviewer": 0})
    contracts = ContractNet(ledger)
    offers = {
        "specialists": {
            "members": ["scout", "analyst", "reviewer"],
            "capabilities": ["discover", "analyze", "verify"],
            "cost": 12,
        }
    }
    award = contracts.award("report-1", "task-1", "manager", ["discover", "analyze", "verify"], offers)
    artifact = Artifact(
        "artifact-1", "reviewer", {"answer": 42}, metadata={"task_id": "task-1", "contract_id": "report-1"}
    )

    def verify(candidate):
        passed = candidate.content == {"answer": 42}
        return Feedback(float(passed), verified=passed)

    paid = contracts.complete("report-1", artifact, verify)
    # Retry does not transfer credits again.
    contracts.complete("report-1", artifact, verify)
    allocation = VCGPayments(CombinatorialAuction(["gpu", "dataset"])).clear(
        {"team": {("gpu", "dataset"): 10}, "gpu-only": {("gpu",): 4}, "data-only": {("dataset",): 5}}
    )
    repeated = RepeatedGame(NormalFormGame([[[3, 3], [0, 5]], [[5, 0], [1, 1]]]))
    reciprocity = repeated.run([tit_for_tat, fixed(1)], rounds=5)
    return {
        "awarded_team": award["team"],
        "verified_and_paid": paid,
        "balances": ledger.balances,
        "bundle_welfare": allocation["welfare"],
        "vcg_payments": allocation["payments"],
        "repeated_utility": reciprocity["utility"].tolist(),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
