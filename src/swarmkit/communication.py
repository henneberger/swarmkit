"""Information gating and numerical channels for swarm communication.

Entropy gating: https://arxiv.org/abs/2605.06988
Latent memory: https://arxiv.org/abs/2511.20639
Geometric alignment: https://arxiv.org/abs/2608.13317
Learned cache translation: https://arxiv.org/abs/2606.13594

These are model-neutral mechanisms, not pretrained LatentMAS/Interlat/StateBridge
releases. Real hidden states and aligned calibration examples must be supplied by
an adapter with access to a model's internals. No method invents hidden states
from text or assumes that arbitrary models share a representation space.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from dataclasses import replace

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .types import KVCache, LatentPayload, Message, probability


def _matrix(value: ArrayLike, name: str) -> NDArray[np.float64]:
    result = np.asarray(value, dtype=float)
    if result.ndim != 2 or 0 in result.shape or not np.isfinite(result).all():
        raise ValueError(f"{name} must be a nonempty finite matrix")
    return result


def _distribution(values: Sequence[float]) -> NDArray[np.float64]:
    p = np.asarray(values, dtype=float)
    if p.ndim != 1 or not len(p) or not np.isfinite(p).all() or (p < 0).any() or p.max() <= 0:
        raise ValueError("expected nonnegative finite probabilities with positive mass")
    # Scale before summation: finite masses can otherwise overflow their sum.
    p = p / p.max()
    return p / p.sum()


def entropy(values: Sequence[float]) -> float:
    p = _distribution(values)
    return float(-np.sum(p[p > 0] * np.log(p[p > 0])))


def jensen_shannon(left: Sequence[float], right: Sequence[float]) -> float:
    p, q = _distribution(left), _distribution(right)
    if p.shape != q.shape:
        raise ValueError("belief vectors must have the same shape")
    mean = (p + q) / 2

    def divergence(a: NDArray[np.float64]) -> float:
        take = a > 0
        return float(np.sum(a[take] * np.log(a[take] / mean[take])))

    return (divergence(p) + divergence(q)) / 2


class InformationGate:
    """Publish on changed beliefs, new evidence, or a maximum silence interval.

    Default Jensen–Shannon divergence catches equal-entropy hypothesis switches;
    metric='entropy' exposes the original entropy-only gate's blind spot. State
    updates only when publication is accepted. Supply stable candidate ordering.
    """

    def __init__(self, threshold: float = 0.2, *, metric: str = "js", max_silence: int | None = None):
        if not math.isfinite(threshold) or threshold < 0:
            raise ValueError("threshold must be finite and nonnegative")
        if metric not in ("js", "entropy") or (
            max_silence is not None and (not isinstance(max_silence, int) or max_silence < 1)
        ):
            raise ValueError("invalid metric or silence interval")
        self.threshold, self.metric, self.max_silence = threshold, metric, max_silence
        self._last: dict[str, tuple[NDArray[np.float64], int]] = {}
        self._evidence: dict[str, set[str]] = {}
        self._steps: dict[str, int] = {}
        self._labels: dict[str, tuple[str, ...]] = {}

    def accept(
        self, sender: str, beliefs: Sequence[float], *, step: int = 0, evidence_ids: Sequence[str] = ()
    ) -> bool:
        current = _distribution(beliefs)
        if not isinstance(step, int) or step < 0 or step < self._steps.get(sender, 0):
            raise ValueError("steps must be nonnegative integers and cannot move backwards")
        last = self._last.get(sender)
        if last is not None and current.shape != last[0].shape:
            raise ValueError("belief vectors must have the same shape")
        novel = set(evidence_ids) - self._evidence.get(sender, set())
        accept = last is None or bool(novel)
        if last is not None:
            if step < last[1]:
                raise ValueError("steps cannot move backwards")
            change = (
                jensen_shannon(current, last[0])
                if self.metric == "js"
                else abs(entropy(current) - entropy(last[0]))
            )
            accept |= change >= self.threshold
            accept |= self.max_silence is not None and step - last[1] >= self.max_silence
        self._steps[sender] = step
        if accept:
            self._last[sender] = current.copy(), step
            self._evidence.setdefault(sender, set()).update(evidence_ids)
        return bool(accept)

    def __call__(self, message: Message) -> bool:
        beliefs = message.metadata.get("beliefs")
        if beliefs is None:
            return True
        if isinstance(beliefs, Mapping):
            labels = tuple(sorted(beliefs))
            if message.sender in self._labels and labels != self._labels[message.sender]:
                raise ValueError("candidate identities must remain stable for a sender")
            result = self.accept(
                message.sender,
                [beliefs[key] for key in labels],
                step=message.step,
                evidence_ids=[e.id for e in message.evidence],
            )
            self._labels[message.sender] = labels
            return result
        return self.accept(
            message.sender, beliefs, step=message.step, evidence_ids=[e.id for e in message.evidence]
        )


class EvidenceCompressor:
    """Select bounded evidence cards; prioritize novelty and counterevidence.

    Selection preserves complete structured Evidence objects and their provenance.
    This bounds card count, not bytes/tokens; a provider summarizer can be injected
    separately without pretending a character cutoff preserves all information.
    """

    def __init__(self, max_cards: int = 2):
        if not isinstance(max_cards, int) or max_cards < 1:
            raise ValueError("max_cards must be positive")
        self.max_cards = max_cards

    def compress(
        self, message: Message, *, seen_ids: Sequence[str] = (), leading_answer: str | None = None
    ) -> Message:
        seen = set(seen_ids)
        unique = {e.id: e for e in message.evidence}
        ranked = sorted(
            unique.values(),
            key=lambda e: (
                e.id not in seen,
                leading_answer in e.contradicts if leading_answer else False,
                e.confidence,
                e.id,
            ),
            reverse=True,
        )
        selected = tuple(ranked[: self.max_cards])
        return replace(
            message,
            evidence=selected,
            content="\n".join(f"[{e.id}] {e.claim}" for e in selected),
            metadata={
                **message.metadata,
                "omitted_evidence_ids": tuple(e.id for e in ranked[self.max_cards :]),
            },
        )


class LatentMemory:
    """Bounded hidden-state FIFO; latest packet metadata describes the buffer.

    Token rows are retained, but segment boundaries and earlier metadata are not.
    """

    def __init__(self, max_tokens: int = 1024):
        if not isinstance(max_tokens, int) or max_tokens < 1:
            raise ValueError("max_tokens must be positive")
        self.max_tokens = max_tokens
        self._packet: LatentPayload | None = None

    def append(self, packet: LatentPayload) -> None:
        values = _matrix(packet.values, "latent values")
        if self._packet is not None:
            if packet.model_id != self._packet.model_id or packet.layer != self._packet.layer:
                raise ValueError("align model and layer before appending latent states")
            if values.shape[1] != self._packet.values.shape[1]:
                raise ValueError("latent feature dimensions differ")
            values = np.concatenate((self._packet.values, values), axis=0)
        self._packet = LatentPayload(
            values[-self.max_tokens :].copy(), packet.model_id, packet.layer, dict(packet.metadata)
        )

    def read(self) -> LatentPayload | None:
        if self._packet is None:
            return None
        return replace(self._packet, values=self._packet.values.copy())


class GeometricAlignment:
    """Centered, optionally whitened rectangular Procrustes feature alignment.

    Paired rows must represent aligned meanings/tokens. Whitening is regularized;
    rectangular source/target dimensions are supported. This implements the
    geometric component, not a reproduction of a full model-specific pipeline.
    """

    def __init__(
        self, source_model: str, target_model: str, *, whiten: bool = True, regularization: float = 1e-6
    ):
        if not math.isfinite(regularization) or regularization <= 0:
            raise ValueError("regularization must be positive and finite")
        self.source_model, self.target_model = source_model, target_model
        self.whiten, self.regularization = whiten, regularization
        self._fitted = False

    def fit(self, source: ArrayLike, target: ArrayLike) -> GeometricAlignment:
        x, y = _matrix(source, "source"), _matrix(target, "target")
        if x.shape[0] != y.shape[0] or x.shape[0] < 2:
            raise ValueError("at least two paired calibration rows required")
        source_mean, target_mean = x.mean(axis=0), y.mean(axis=0)
        x, y = x - source_mean, y - target_mean
        if not np.isfinite(x).all() or not np.isfinite(y).all():
            raise ValueError("calibration magnitudes exceed numerical range")

        def roots(a: NDArray[np.float64]) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
            with np.errstate(over="ignore", invalid="ignore"):
                covariance = a.T @ a / max(1, len(a) - 1)
            if not np.isfinite(covariance).all():
                raise ValueError("calibration covariance exceeds numerical range")
            eigen, vectors = np.linalg.eigh(covariance)
            root = np.sqrt(np.maximum(eigen, 0) + self.regularization)
            return (vectors / root) @ vectors.T, (vectors * root) @ vectors.T

        if self.whiten:
            wx, _ = roots(x)
            wy, cy = roots(y)
        else:
            wx, wy, cy = np.eye(x.shape[1]), np.eye(y.shape[1]), np.eye(y.shape[1])
        with np.errstate(over="ignore", invalid="ignore"):
            cross = (x @ wx).T @ (y @ wy)
        if not np.isfinite(cross).all():
            raise ValueError("calibration cross product exceeds numerical range")
        u, _, vt = np.linalg.svd(cross, full_matrices=False)
        mapping = wx @ (u @ vt) @ cy
        if not np.isfinite(mapping).all():
            raise ValueError("alignment exceeds numerical range")
        self.source_mean, self.target_mean, self.mapping = source_mean, target_mean, mapping
        self._fitted = True
        return self

    def transform(self, packet: LatentPayload) -> LatentPayload:
        if not self._fitted:
            raise RuntimeError("fit calibration pairs before transforming")
        x = _matrix(packet.values, "latent values")
        if packet.model_id != self.source_model or x.shape[1] != len(self.source_mean):
            raise ValueError("source model or hidden dimension does not match calibration")
        mapped = (x - self.source_mean) @ self.mapping + self.target_mean
        if not np.isfinite(mapped).all():
            raise ValueError("mapped states exceed numerical range")
        return LatentPayload(
            mapped, self.target_model, packet.layer, {**packet.metadata, "alignment": "centered_procrustes"}
        )


class VocabularyAnchor:
    """Blend mapped states with top-k target-token embedding neighborhoods."""

    def __init__(
        self,
        embeddings: ArrayLike,
        *,
        model_id: str,
        weight: float = 0.25,
        top_k: int = 4,
        temperature: float = 1.0,
    ):
        self.embeddings = _matrix(embeddings, "embeddings").copy()
        probability(weight, "weight")
        if not isinstance(top_k, int) or top_k < 1 or not math.isfinite(temperature) or temperature <= 0:
            raise ValueError("top_k and temperature must be positive")
        self.model_id, self.weight, self.top_k, self.temperature = model_id, weight, top_k, temperature

    def transform(self, packet: LatentPayload) -> LatentPayload:
        x = _matrix(packet.values, "latent values")
        if packet.model_id != self.model_id or x.shape[1] != self.embeddings.shape[1]:
            raise ValueError("embedding model or dimension mismatch")

        def unit_rows(values: NDArray[np.float64]) -> NDArray[np.float64]:
            scale = np.max(np.abs(values), axis=1, keepdims=True)
            scaled = values / np.where(scale > 0, scale, 1)
            norm = np.linalg.norm(scaled, axis=1, keepdims=True)
            return scaled / np.where(norm > 0, norm, 1)

        similarities = unit_rows(x) @ unit_rows(self.embeddings).T
        ids = np.argsort(-similarities, axis=1)[:, : min(self.top_k, len(self.embeddings))]
        scores = np.take_along_axis(similarities, ids, axis=1)
        with np.errstate(over="ignore", under="ignore"):
            scores = np.exp((scores - scores.max(axis=1, keepdims=True)) / self.temperature)
        scores /= scores.sum(axis=1, keepdims=True)
        anchors = np.sum(self.embeddings[ids] * scores[..., None], axis=1)
        mapped = (1 - self.weight) * x + self.weight * anchors
        if not np.isfinite(mapped).all():
            raise ValueError("anchored states exceed numerical range")
        return LatentPayload(mapped, packet.model_id, packet.layer, {**packet.metadata, "anchored": True})


class LinearLatentCodec:
    """Learn a regularized linear communication adapter from paired states.

    This provides an executable reconstruction baseline for learned latent/KV
    channels, not Interlat's contrastive/generative neural training recipe.
    """

    def __init__(self, source_model: str, target_model: str, *, regularization: float = 1e-4):
        if not math.isfinite(regularization) or regularization <= 0:
            raise ValueError("regularization must be positive and finite")
        self.source_model, self.target_model = source_model, target_model
        self.regularization, self._weights = regularization, None

    def fit(self, source: ArrayLike, target: ArrayLike) -> LinearLatentCodec:
        x, y = _matrix(source, "source"), _matrix(target, "target")
        if len(x) != len(y) or len(x) < 2:
            raise ValueError("at least two paired calibration rows required")
        source_mean, target_mean = x.mean(axis=0), y.mean(axis=0)
        x, y = x - source_mean, y - target_mean
        with np.errstate(over="ignore", invalid="ignore"):
            gram = x.T @ x + self.regularization * np.eye(x.shape[1])
            cross = x.T @ y
        if not np.isfinite(gram).all() or not np.isfinite(cross).all():
            raise ValueError("calibration exceeds numerical range")
        weights = np.linalg.solve(gram, cross)
        if not np.isfinite(weights).all():
            raise ValueError("adapter exceeds numerical range")
        self.source_mean, self.target_mean, self._weights = source_mean, target_mean, weights
        return self

    def transform(self, packet: LatentPayload) -> LatentPayload:
        if self._weights is None:
            raise RuntimeError("fit before transform")
        x = _matrix(packet.values, "latent values")
        if packet.model_id != self.source_model or x.shape[1] != self._weights.shape[0]:
            raise ValueError("source model or dimension mismatch")
        mapped = (x - self.source_mean) @ self._weights + self.target_mean
        if not np.isfinite(mapped).all():
            raise ValueError("mapped states exceed numerical range")
        return LatentPayload(mapped, self.target_model, packet.layer, dict(packet.metadata))


class KVCacheTranslator:
    """Separate learned linear maps for keys and values; preserve leading axes."""

    def __init__(self, source_model: str, target_model: str, *, regularization: float = 1e-4):
        self.keys = LinearLatentCodec(source_model, target_model, regularization=regularization)
        self.values = LinearLatentCodec(source_model, target_model, regularization=regularization)
        self.source_model, self.target_model = source_model, target_model

    @staticmethod
    def _flatten(value: ArrayLike) -> tuple[NDArray[np.float64], tuple[int, ...]]:
        a = np.asarray(value, dtype=float)
        if a.ndim < 2 or 0 in a.shape or not np.isfinite(a).all():
            raise ValueError("cache requires finite arrays with token and feature axes")
        return a.reshape(-1, a.shape[-1]), a.shape[:-1]

    def fit(self, source: KVCache, target: KVCache) -> KVCacheTranslator:
        if source.model_id != self.source_model or target.model_id != self.target_model:
            raise ValueError("cache model does not match codec")
        sk, sk_shape = self._flatten(source.keys)
        sv, sv_shape = self._flatten(source.values)
        tk, tk_shape = self._flatten(target.keys)
        tv, tv_shape = self._flatten(target.values)
        if not sk_shape == sv_shape == tk_shape == tv_shape:
            raise ValueError("paired cache leading axes must match")
        keys = LinearLatentCodec(
            self.source_model, self.target_model, regularization=self.keys.regularization
        ).fit(sk, tk)
        values = LinearLatentCodec(
            self.source_model, self.target_model, regularization=self.values.regularization
        ).fit(sv, tv)
        self.keys, self.values = keys, values
        return self

    def transform(self, cache: KVCache) -> KVCache:
        k, kshape = self._flatten(cache.keys)
        v, vshape = self._flatten(cache.values)
        if kshape != vshape:
            raise ValueError("key/value leading axes differ")
        mapped_k = self.keys.transform(LatentPayload(k, cache.model_id)).values
        mapped_v = self.values.transform(LatentPayload(v, cache.model_id)).values
        return KVCache(
            mapped_k.reshape(*kshape, mapped_k.shape[-1]),
            mapped_v.reshape(*vshape, mapped_v.shape[-1]),
            self.target_model,
            dict(cache.metadata),
        )
