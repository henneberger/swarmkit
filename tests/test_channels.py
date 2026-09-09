import numpy as np
import pytest

from swarmkit.communication import (
    GeometricAlignment,
    InformationGate,
    KVCacheTranslator,
    LatentMemory,
    LinearLatentCodec,
    VocabularyAnchor,
    entropy,
    jensen_shannon,
)
from swarmkit.types import KVCache, LatentPayload, Message


def test_distribution_overflow_and_divergence_invariants():
    assert entropy([1e308, 1e308]) == pytest.approx(np.log(2))
    assert jensen_shannon([1, 0], [0, 1]) == pytest.approx(np.log(2))
    assert jensen_shannon([1, 2], [2, 4]) == pytest.approx(0)
    for value in ([0, 0], [np.nan, 1], [np.inf, 1], [-1, 2], []):
        with pytest.raises(ValueError):
            entropy(value)


def test_equal_entropy_switch_and_novel_evidence():
    gate, original = InformationGate(0.1), InformationGate(0.1, metric="entropy")
    for policy in (gate, original):
        assert policy.accept("a", [0.9, 0.1])
    assert gate.accept("a", [0.1, 0.9], step=1)
    assert not original.accept("a", [0.1, 0.9], step=1)
    assert original.accept("a", [0.1, 0.9], step=2, evidence_ids=["unique"])
    assert not original.accept("a", [0.1, 0.9], step=3, evidence_ids=["unique"])


def test_gate_schema_time_and_last_published_state():
    gate = InformationGate(0.5, metric="entropy", max_silence=5)
    assert gate.accept("a", [1, 1], step=0)
    assert not gate.accept("a", [1, 1], step=4)
    with pytest.raises(ValueError):
        gate.accept("a", [1, 1], step=3)
    assert gate.accept("a", [1, 1], step=5)
    with pytest.raises(ValueError):
        gate.accept("a", [1, 1, 1], step=6)
    mapped = InformationGate()
    assert mapped(Message("a", "", metadata={"beliefs": {"x": 1, "y": 0}}))
    with pytest.raises(ValueError, match="identities"):
        mapped(Message("a", "", metadata={"beliefs": {"x": 1, "z": 0}}))


def test_latent_memory_fifo_copy_and_source_boundaries():
    memory = LatentMemory(max_tokens=3)
    memory.append(LatentPayload(np.array([[1, 2], [3, 4]]), "a", 1))
    memory.append(LatentPayload(np.array([[5, 6], [7, 8]]), "a", 1))
    assert np.array_equal(memory.read().values, [[3, 4], [5, 6], [7, 8]])
    memory.read().values[:] = 99
    assert memory.read().values[0, 0] == 3
    for packet in (
        LatentPayload([[1, 2]], "b", 1),
        LatentPayload([[1, 2]], "a", 2),
        LatentPayload([[1, 2, 3]], "a", 1),
    ):
        with pytest.raises(ValueError):
            memory.append(packet)


@pytest.mark.parametrize("whiten", [False, True])
def test_procrustes_recovers_rotation_translation(whiten):
    rng = np.random.default_rng(4)
    x = rng.normal(size=(200, 3))
    rotation, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    target = x @ rotation + np.array([4, 2, -3])
    alignment = GeometricAlignment("a", "b", whiten=whiten).fit(x, target)
    new = rng.normal(size=(10, 3))
    out = alignment.transform(LatentPayload(new, "a"))
    assert out.model_id == "b"
    assert np.allclose(out.values, new @ rotation + [4, 2, -3], atol=1e-8)


def test_rectangular_alignment_and_ridge_calibration_failures():
    rng = np.random.default_rng(9)
    x = rng.normal(size=(100, 3))
    projection = np.linalg.qr(rng.normal(size=(3, 2)))[0]
    target = x @ projection
    out = GeometricAlignment("a", "b", whiten=False).fit(x, target).transform(LatentPayload(x, "a"))
    assert out.values.shape == (100, 2)
    # Rectangular Procrustes is a constrained approximation, not arbitrary ridge regression.
    for cls in (GeometricAlignment, LinearLatentCodec):
        codec = cls("a", "b")
        with pytest.raises(RuntimeError):
            codec.transform(LatentPayload(x, "a"))
        for left, right in ((x, target[:-1]), ([[1, 2]], [[3, 4]]), ([[np.nan]], [[1]])):
            with pytest.raises(ValueError):
                codec.fit(left, right)
        codec.fit(x, target)
        with pytest.raises(ValueError):
            codec.transform(LatentPayload(x, "wrong"))
        with pytest.raises(ValueError):
            codec.transform(LatentPayload(np.ones((2, 5)), "a"))


def test_ridge_recovers_affine_and_singular_calibration_is_finite():
    rng = np.random.default_rng(5)
    x = rng.normal(size=(150, 4))
    weights = rng.normal(size=(4, 2))
    codec = LinearLatentCodec("a", "b", regularization=1e-8).fit(x, x @ weights + 3)
    heldout = rng.normal(size=(10, 4))
    assert np.allclose(codec.transform(LatentPayload(heldout, "a")).values, heldout @ weights + 3, atol=1e-7)
    codec.fit(np.ones((3, 4)), np.ones((3, 2)) * 7)
    assert np.allclose(codec.transform(LatentPayload(np.ones((2, 4)), "a")).values, 7)


def test_kv_translation_preserves_axes_and_rejects_source_or_pair_mismatch():
    rng = np.random.default_rng(8)
    k, v = rng.normal(size=(2, 3, 4, 5)), rng.normal(size=(2, 3, 4, 5))
    wk, wv = rng.normal(size=(5, 7)), rng.normal(size=(5, 7))
    source = KVCache(k, v, "a")
    target = KVCache(k @ wk + 1, v @ wv - 2, "b")
    codec = KVCacheTranslator("a", "b", regularization=1e-8).fit(source, target)
    output = codec.transform(source)
    assert output.keys.shape == output.values.shape == (2, 3, 4, 7)
    assert np.allclose(output.keys, target.keys, atol=1e-7)
    assert np.allclose(output.values, target.values, atol=1e-7)
    with pytest.raises(ValueError):
        codec.transform(KVCache(k, v, "wrong"))
    with pytest.raises(ValueError):
        codec.fit(source, KVCache(target.keys.reshape(6, 4, 7), target.values.reshape(6, 4, 7), "b"))


def test_anchor_extreme_values_tiny_temperature_and_finite_inputs():
    anchor = VocabularyAnchor([[1e308, 0], [0, 1e308]], model_id="b", weight=1, top_k=1, temperature=1e-300)
    assert np.array_equal(anchor.transform(LatentPayload([[1, 0]], "b")).values, [[1e308, 0]])
    with pytest.raises(ValueError):
        anchor.transform(LatentPayload([[np.inf, 0]], "b"))
    with pytest.raises(ValueError):
        VocabularyAnchor([[1, 0]], model_id="b", top_k=1.5)
