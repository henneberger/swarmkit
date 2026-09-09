"""Trainable contrastive channels and low-rank message bottlenecks.

Mechanism-level adapters motivated by Interlat (https://arxiv.org/abs/2511.09149).
These explicitly train a small numerical interface, not the paper's full neural
encoder/decoder/generative stages. Aligned calibration rows are caller-supplied.
"""

from __future__ import annotations

import hashlib
import math

import numpy as np
from numpy.typing import ArrayLike

from .types import LatentPayload


def _rows(value: ArrayLike) -> np.ndarray:
    x = np.asarray(value, dtype=float)
    if x.ndim != 2 or min(x.shape) < 1 or not np.isfinite(x).all():
        raise ValueError("expected a nonempty finite matrix")
    return x


def _unit(x: np.ndarray) -> np.ndarray:
    scale = np.max(np.abs(x), axis=1, keepdims=True)
    if (scale == 0).any():
        raise ValueError("zero vectors have no contrastive direction")
    stable = x / scale
    return stable / np.linalg.norm(stable, axis=1, keepdims=True)


class ContrastiveLatentCodec:
    """Paired InfoNCE linear adapter with mismatched rows as negative examples.

    Training minimizes cross-entropy of source-to-target pair retrieval. Returned
    states are in target feature coordinates, but successful pair retrieval does
    not establish preserved facts or downstream generation quality.
    """

    def __init__(
        self,
        source_model: str,
        target_model: str,
        *,
        temperature: float = 0.2,
        learning_rate: float = 0.1,
        weight_decay: float = 1e-4,
        seed: int = 0,
    ):
        if any(not math.isfinite(v) or v <= 0 for v in (temperature, learning_rate)):
            raise ValueError("temperature and learning rate must be positive")
        if not math.isfinite(weight_decay) or weight_decay < 0:
            raise ValueError("weight decay must be nonnegative")
        self.source_model, self.target_model = source_model, target_model
        self.temperature, self.learning_rate = temperature, learning_rate
        self.weight_decay, self.seed = weight_decay, seed
        self.weights = None
        self.losses: tuple[float, ...] = ()

    def fit(self, source: ArrayLike, target: ArrayLike, *, epochs: int = 200) -> ContrastiveLatentCodec:
        x, y = _unit(_rows(source)), _unit(_rows(target))
        if len(x) != len(y) or len(x) < 2 or type(epochs) is not int or epochs < 1:
            raise ValueError("need at least two paired rows and positive integer epochs")
        rng = np.random.default_rng(self.seed)
        weights = rng.normal(0, 0.01, (x.shape[1], y.shape[1]))
        losses = []
        for _ in range(epochs):
            with np.errstate(over="ignore", invalid="ignore"):
                scores = (x @ weights) @ y.T / self.temperature
                scores -= scores.max(axis=1, keepdims=True)
            if not np.isfinite(scores).all():
                raise ValueError("contrastive logits exceed numerical range")
            probabilities = np.exp(scores)
            normalizer = probabilities.sum(axis=1, keepdims=True)
            probabilities /= normalizer
            loss = np.mean(np.log(normalizer[:, 0]) - np.diag(scores))
            loss += 0.5 * self.weight_decay * float(np.sum(weights * weights))
            losses.append(float(loss))
            residual = probabilities - np.eye(len(x))
            gradient = x.T @ residual @ y / (len(x) * self.temperature) + self.weight_decay * weights
            updated = weights - self.learning_rate * gradient
            if not np.isfinite(updated).all() or not math.isfinite(loss):
                raise ValueError("training diverged; lower learning rate or rescale calibration data")
            weights = updated
        self.weights, self.losses = weights, tuple(losses)
        return self

    def transform(self, packet: LatentPayload) -> LatentPayload:
        if self.weights is None:
            raise RuntimeError("fit before transform")
        x = _unit(_rows(packet.values))
        if packet.model_id != self.source_model or x.shape[1] != self.weights.shape[0]:
            raise ValueError("source model or feature dimension mismatch")
        mapped = x @ self.weights
        if not np.isfinite(mapped).all():
            raise ValueError("non-finite transformed states")
        return LatentPayload(
            mapped, self.target_model, packet.layer, {**packet.metadata, "codec": "linear_infonce"}
        )


class LatentBottleneck:
    """Fitted PCA communication bottleneck with explicit decode/reconstruction.

    Rank and model identity are checked; compression error is observable. This is
    a low-rank baseline, not a promise that decisive private information survives.
    """

    def __init__(self, model_id: str, rank: int):
        if type(rank) is not int or rank < 1:
            raise ValueError("rank must be a positive integer")
        self.model_id, self.rank = model_id, rank
        self.components = None

    def fit(self, values: ArrayLike) -> LatentBottleneck:
        x = _rows(values)
        if self.rank > min(x.shape) or len(x) < 2:
            raise ValueError("rank exceeds calibration dimensions or insufficient rows")
        mean = (x / len(x)).sum(axis=0)
        if not np.isfinite(mean).all():
            raise ValueError("calibration mean overflow")
        with np.errstate(over="ignore", invalid="ignore"):
            centered = x - mean
        if not np.isfinite(centered).all():
            raise ValueError("centered states exceed numerical range")
        _, _, vt = np.linalg.svd(centered, full_matrices=False)
        self.mean, self.components = mean, vt[: self.rank].copy()
        self.identity = hashlib.sha256(
            self.model_id.encode() + self.mean.tobytes() + self.components.tobytes()
        ).hexdigest()
        return self

    def encode(self, packet: LatentPayload) -> LatentPayload:
        if self.components is None:
            raise RuntimeError("fit before encoding")
        x = _rows(packet.values)
        if packet.model_id != self.model_id or x.shape[1] != len(self.mean):
            raise ValueError("source model or feature dimension mismatch")
        if packet.metadata.get("bottleneck"):
            raise ValueError("packet is already compressed")
        with np.errstate(over="ignore", invalid="ignore"):
            encoded = (x - self.mean) @ self.components.T
        if not np.isfinite(encoded).all():
            raise ValueError("compressed states exceed numerical range")
        return LatentPayload(
            encoded,
            self.model_id,
            packet.layer,
            {
                **packet.metadata,
                "bottleneck": True,
                "original_dimension": len(self.mean),
                "bottleneck_id": self.identity,
            },
        )

    def decode(self, packet: LatentPayload) -> LatentPayload:
        if self.components is None:
            raise RuntimeError("fit before decoding")
        x = _rows(packet.values)
        if (
            packet.model_id != self.model_id
            or x.shape[1] != self.rank
            or not packet.metadata.get("bottleneck")
            or packet.metadata.get("bottleneck_id") != self.identity
            or packet.metadata.get("original_dimension") != len(self.mean)
        ):
            raise ValueError("packet is not compatible compressed data")
        metadata = dict(packet.metadata)
        metadata.pop("bottleneck", None)
        metadata.pop("original_dimension", None)
        metadata.pop("bottleneck_id", None)
        with np.errstate(over="ignore", invalid="ignore"):
            decoded = x @ self.components + self.mean
        if not np.isfinite(decoded).all():
            raise ValueError("reconstructed states exceed numerical range")
        return LatentPayload(decoded, self.model_id, packet.layer, metadata)
