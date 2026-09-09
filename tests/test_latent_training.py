import numpy as np
import pytest

from swarmkit.latent_training import ContrastiveLatentCodec, LatentBottleneck
from swarmkit.types import LatentPayload


def test_contrastive_training_learns_actual_pair_retrieval():
    rng = np.random.default_rng(9)
    x = rng.normal(size=(12, 12))
    rotation, _ = np.linalg.qr(rng.normal(size=(12, 12)))
    y = x @ rotation
    codec = ContrastiveLatentCodec("a", "b", seed=3).fit(x, y, epochs=250)
    output = codec.transform(LatentPayload(x, "a"))
    normalized = y / np.linalg.norm(y, axis=1, keepdims=True)
    assert np.array_equal(np.argmax(output.values @ normalized.T, axis=1), np.arange(len(x)))
    assert codec.losses[-1] < codec.losses[0] * 0.25
    with pytest.raises(ValueError):
        codec.transform(LatentPayload(x, "wrong"))


def test_compression_reconstruction_of_low_rank_signal():
    rng = np.random.default_rng(2)
    data = rng.normal(size=(100, 2)) @ rng.normal(size=(2, 8)) + 3
    codec = LatentBottleneck("a", 2).fit(data)
    compressed = codec.encode(LatentPayload(data, "a"))
    assert compressed.values.shape == (100, 2)
    np.testing.assert_allclose(codec.decode(compressed).values, data, atol=1e-10)
    with pytest.raises(ValueError):
        codec.encode(compressed)
    with pytest.raises(ValueError):
        codec.decode(LatentPayload(np.zeros((4, 2)), "a"))


def test_bottleneck_rejects_other_calibration_and_stale_packets_after_refit():
    x = np.random.default_rng(3).normal(size=(20, 4))
    left, right = LatentBottleneck("a", 2).fit(x), LatentBottleneck("a", 2).fit(x + 10)
    packet = left.encode(LatentPayload(x, "a"))
    with pytest.raises(ValueError, match="compatible"):
        right.decode(packet)
    left.fit(x + 10)
    with pytest.raises(ValueError, match="compatible"):
        left.decode(packet)


def test_contrastive_rejects_zero_unpaired_and_preserves_fit_on_failure():
    codec = ContrastiveLatentCodec("a", "b")
    x = np.eye(3)
    codec.fit(x, x, epochs=10)
    weights = codec.weights.copy()
    with pytest.raises(ValueError):
        codec.fit(x, x[:-1])
    assert np.array_equal(codec.weights, weights)
    with pytest.raises(ValueError, match="zero"):
        codec.fit(np.zeros((3, 3)), x)
    with pytest.raises(ValueError):
        ContrastiveLatentCodec("a", "b", temperature=5e-324).fit(x, x, epochs=1)
