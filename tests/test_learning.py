import numpy as np
import pytest

from swarmkit.learning import (
    CollaborativeReward,
    ParallelReward,
    SoftmaxPolicy,
    counterfactual_message_credit,
)
from swarmkit.types import Message, SwarmState


def test_reinforce_learns_a_policy_and_seeded_sampling():
    policy = SoftmaxPolicy(2, 2, learning_rate=0.1)
    for _ in range(80):
        policy.update([1, 0], 1, 1)
        policy.update([0, 1], 0, 1)
    assert policy.probabilities([1, 0])[1] > 0.9
    assert policy.probabilities([0, 1])[0] > 0.9
    a, b = SwarmState(seed=4), SwarmState(seed=4)
    assert [policy.sample([1, 0], a) for _ in range(20)] == [policy.sample([1, 0], b) for _ in range(20)]


@pytest.mark.parametrize(
    "advantage,old_probability,clipped", [(1, 0.2, True), (-1, 0.9, True), (-1, 0.2, False), (1, 0.9, False)]
)
def test_ppo_clipping_depends_on_advantage_sign(advantage, old_probability, clipped):
    policy = SoftmaxPolicy(1, 2, learning_rate=0.1)
    old_weights = policy.weights.copy()
    result = policy.update([1], 0, advantage, old_log_probability=np.log(old_probability))
    assert (result["coefficient"] == 0) == clipped
    if clipped:
        assert np.array_equal(old_weights, policy.weights)
    else:
        assert np.sign(policy.weights[0, 0]) == np.sign(advantage)


def test_entropy_bonus_moves_nonuniform_policy_towards_uniform():
    policy = SoftmaxPolicy(1, 2, learning_rate=0.1)
    policy.weights[:] = [2, -2]
    before = policy.probabilities([1])[0]
    policy.update([1], 0, 0, entropy_weight=1)
    assert policy.probabilities([1])[0] < before


def test_invalid_and_overflow_updates_leave_weights_intact():
    policy = SoftmaxPolicy(1, 2, learning_rate=1e308)
    before = policy.weights.copy()
    with pytest.raises(ValueError, match="numerical range"):
        policy.update([1e100], 0, 1e100)
    assert np.array_equal(policy.weights, before)
    for features, action, advantage in (([np.nan], 0, 1), ([1], 0.5, 1), ([1], 0, np.inf)):
        with pytest.raises(ValueError):
            policy.update(features, action, advantage)
    with pytest.raises(ValueError):
        SoftmaxPolicy(1.5, 2)
    policy.weights[:] = np.inf
    with pytest.raises(ValueError):
        policy.probabilities([1])


def test_collaborative_reward_uses_verified_changes_and_costs():
    reward = CollaborativeReward(influence_weight=2, cost_weight=0.5)
    result = reward(1, {"a": 0.2, "b": 0.8}, {"a": 0.6, "b": 0.6}, cost=0.4)
    assert result.utility == pytest.approx(1)
    assert result.per_agent == pytest.approx({"a": 0.4, "b": -0.2})
    with pytest.raises(ValueError):
        reward(1, {"a": 0}, {"b": 1})
    with pytest.raises(ValueError):
        CollaborativeReward(cost_weight=-1)


def test_parallel_annealing_keeps_task_performance_and_path_cost():
    reward = ParallelReward(parallel_weight=1, completion_weight=1, critical_path_weight=0.1, anneal_steps=10)
    early = reward(2, spawned=4, completed=4, critical_path_steps=3, training_step=0)
    late = reward(2, spawned=4, completed=4, critical_path_steps=3, training_step=10)
    assert early.utility == pytest.approx(3.45)
    assert late.utility == pytest.approx(1.7)
    assert reward(2, spawned=100, completed=0, critical_path_steps=0, training_step=0).utility == 2
    assert reward(2, spawned=0, completed=0, critical_path_steps=0, training_step=0).utility == 2
    with pytest.raises(ValueError):
        reward(2, spawned=1.5, completed=1, critical_path_steps=0, training_step=0)


def test_counterfactual_credit_measures_marginal_harm_and_help():
    messages = [Message("a", "", id="good"), Message("b", "", id="bad")]
    credit = counterfactual_message_credit(messages, lambda ms: sum(2 if m.id == "good" else -1 for m in ms))
    assert credit == {"good": 2, "bad": -1}
    with pytest.raises(ValueError):
        counterfactual_message_credit([messages[0], messages[0]], lambda _: 0)


def test_ppo_reports_actual_importance_ratio_and_rejects_unrepresentable_ratio():
    policy = SoftmaxPolicy(1, 2)
    result = policy.update([1], 0, 1, old_log_probability=-100)
    assert result["ratio"] == pytest.approx(0.5 * np.exp(100))
    assert result["coefficient"] == 0
    before = policy.weights.copy()
    with pytest.raises(ValueError, match="importance ratio"):
        policy.update([1], 0, 1, old_log_probability=-1e300)
    assert np.array_equal(policy.weights, before)
