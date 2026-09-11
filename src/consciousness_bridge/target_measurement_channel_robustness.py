"""Proposition 72: noisy target measurement and witness transfer.

P71 requires target provenance to be independent enough that the bridge test is
not true by construction. P72 addresses a different problem: the independently
declared target may be latent and observed through a noisy measurement channel.

Under the declared nondifferential measurement condition

    Y independent of Omega given (E_star, T),

the conditional data-processing inequality gives

    I(Y; Omega | T) <= I(E_star; Omega | T).

Thus a population-level positive residual in the observed target transfers to
the latent target under the stated measurement model. The converse fails: an
erasing measurement channel can hide a positive latent residual.

The module also implements total-variation contraction through a target channel,
the exact binary-symmetric attenuation factor, and a conservative finite-sample
lower confidence bound for an observed target-distribution separation.

E_star is a declared latent target variable. This module does not establish that
it is consciousness, ground truth experience, or an ontological primitive.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import floor, isfinite, log, sqrt
from typing import TypeVar

from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
)

Omega = TypeVar("Omega", bound=Hashable)
Physical = TypeVar("Physical", bound=Hashable)
LatentTarget = TypeVar("LatentTarget", bound=Hashable)
ObservedTarget = TypeVar("ObservedTarget", bound=Hashable)
Label = TypeVar("Label", bound=Hashable)


@dataclass(frozen=True)
class TargetMeasurementResidualCertificate:
    """Population residual comparison under a declared target channel."""

    latent_joint_distribution: dict[tuple[Hashable, Hashable, Hashable], float]
    observed_joint_distribution: dict[tuple[Hashable, Hashable, Hashable], float]
    latent_residual_nats: float
    observed_residual_nats: float
    data_processing_gap_nats: float
    data_processing_verified: bool


@dataclass(frozen=True)
class TargetTVTransfer:
    """Total-variation separation before and after a target channel."""

    latent_tv: float
    observed_tv: float
    contraction_gap: float


@dataclass(frozen=True)
class BinarySymmetricTargetTransfer:
    """Exact TV attenuation for a binary symmetric target channel."""

    noise_rate: float
    attenuation_factor: float
    latent_tv: float
    observed_tv: float


@dataclass(frozen=True)
class ObservedTVLowerBound:
    """Finite-sample lower confidence bound on observed target separation."""

    confidence_level: float
    alphabet_size: int
    sample_size_a: int
    sample_size_b: int
    empirical_tv: float
    coordinate_radius_a: float
    coordinate_radius_b: float
    tv_radius_a: float
    tv_radius_b: float
    lower_bound: float


def target_measurement_residual_certificate(
    latent_joint_weights: Mapping[tuple[Omega, Physical, LatentTarget], float],
    measurement_channel_weights: Mapping[
        tuple[Physical, LatentTarget, ObservedTarget], float
    ],
) -> TargetMeasurementResidualCertificate:
    """Verify P72 conditional data processing for a finite declared channel.

    ``latent_joint_weights`` describe a finite measure on ``(Omega, T, E_star)``.
    ``measurement_channel_weights`` describe a nonnegative channel on
    ``(T, E_star, Y)`` and are normalized separately for every latent ``(T,E)``
    pair that occurs with positive probability.

    The construction enforces the P72 measurement premise

        P(y | omega, t, e) = K(y | t, e),

    which is equivalent to ``Y independent of Omega given (E_star, T)`` on the
    declared finite support. Conditional data processing then requires

        I(Y; Omega | T) <= I(E_star; Omega | T).
    """
    latent = _normalize_joint(latent_joint_weights, "latent_joint_weights")
    observed_pairs = {(physical, target) for _, physical, target in latent}
    channel = _normalize_conditional_channel(
        measurement_channel_weights,
        required_pairs=observed_pairs,
    )

    observed: dict[tuple[Hashable, Hashable, Hashable], float] = defaultdict(float)
    for (omega, physical, latent_target), probability in latent.items():
        for (channel_physical, channel_target, measured), conditional in channel.items():
            if channel_physical == physical and channel_target == latent_target:
                observed[(omega, physical, measured)] += probability * conditional

    latent_residual = conditional_mutual_information(latent)
    observed_residual = conditional_mutual_information(observed)
    tolerance = 1e-11 * max(1.0, abs(latent_residual), abs(observed_residual))
    if observed_residual > latent_residual + tolerance:
        raise RuntimeError("P72 conditional data-processing inequality failed")

    latent_residual = max(0.0, latent_residual)
    observed_residual = max(0.0, observed_residual)
    return TargetMeasurementResidualCertificate(
        latent_joint_distribution=dict(latent),
        observed_joint_distribution=dict(observed),
        latent_residual_nats=latent_residual,
        observed_residual_nats=observed_residual,
        data_processing_gap_nats=max(0.0, latent_residual - observed_residual),
        data_processing_verified=True,
    )


def apply_target_channel(
    target_weights: Mapping[LatentTarget, float],
    channel_weights: Mapping[tuple[LatentTarget, ObservedTarget], float],
) -> dict[Hashable, float]:
    """Push one finite target distribution through a declared channel."""
    target = _normalize_distribution(target_weights, "target_weights")
    channel = _normalize_simple_channel(
        channel_weights,
        required_inputs=set(target),
    )
    observed: dict[Hashable, float] = defaultdict(float)
    for latent_target, probability in target.items():
        for (channel_target, measured), conditional in channel.items():
            if channel_target == latent_target:
                observed[measured] += probability * conditional
    return dict(observed)


def total_variation(
    weights_a: Mapping[Label, float],
    weights_b: Mapping[Label, float],
) -> float:
    """Total variation between two normalized finite distributions."""
    distribution_a = _normalize_distribution(weights_a, "weights_a")
    distribution_b = _normalize_distribution(weights_b, "weights_b")
    support = set(distribution_a) | set(distribution_b)
    return 0.5 * sum(
        abs(distribution_a.get(label, 0.0) - distribution_b.get(label, 0.0))
        for label in support
    )


def target_channel_tv_transfer(
    target_weights_a: Mapping[LatentTarget, float],
    target_weights_b: Mapping[LatentTarget, float],
    channel_weights: Mapping[tuple[LatentTarget, ObservedTarget], float],
) -> TargetTVTransfer:
    """Apply one target channel and verify total-variation contraction."""
    latent_tv = total_variation(target_weights_a, target_weights_b)
    observed_a = apply_target_channel(target_weights_a, channel_weights)
    observed_b = apply_target_channel(target_weights_b, channel_weights)
    observed_tv = total_variation(observed_a, observed_b)
    tolerance = 1e-12
    if observed_tv > latent_tv + tolerance:
        raise RuntimeError("target channel increased total variation")
    return TargetTVTransfer(
        latent_tv=latent_tv,
        observed_tv=observed_tv,
        contraction_gap=max(0.0, latent_tv - observed_tv),
    )


def binary_symmetric_target_transfer(
    probability_one_a: float,
    probability_one_b: float,
    noise_rate: float,
) -> BinarySymmetricTargetTransfer:
    """Exact binary-symmetric target-channel attenuation.

    For ``Y = E_star xor N`` with ``N ~ Bernoulli(eta)``, the TV separation of
    two Bernoulli latent targets is multiplied exactly by ``abs(1 - 2*eta)``.
    """
    _probability(probability_one_a, "probability_one_a")
    _probability(probability_one_b, "probability_one_b")
    _probability(noise_rate, "noise_rate")

    latent_tv = abs(probability_one_a - probability_one_b)
    attenuation = abs(1.0 - 2.0 * noise_rate)
    observed_tv = attenuation * latent_tv
    return BinarySymmetricTargetTransfer(
        noise_rate=noise_rate,
        attenuation_factor=attenuation,
        latent_tv=latent_tv,
        observed_tv=observed_tv,
    )


def finite_observed_tv_lower_bound(
    counts_a: Mapping[Label, int],
    counts_b: Mapping[Label, int],
    declared_alphabet: Sequence[Label],
    alpha: float,
) -> ObservedTVLowerBound:
    """Conservative lower confidence bound for two categorical target laws.

    Coordinate-wise Hoeffding bounds and a union bound across both samples and
    all declared categories give, with probability at least ``1-alpha``,

        TV(P_a, P_b)
        >= TV(P_hat_a, P_hat_b) - tau_a - tau_b,

    where ``tau_s = d/2 * sqrt(log(4d/alpha)/(2 n_s))`` capped at one.
    The alphabet must be declared independently of the observed counts so that
    unseen categories are not silently removed from the confidence statement.
    """
    _open_probability(alpha, "alpha")
    alphabet = tuple(declared_alphabet)
    if not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("declared_alphabet must contain unique labels")
    allowed = set(alphabet)
    if not set(counts_a).issubset(allowed) or not set(counts_b).issubset(allowed):
        raise ValueError("count labels must belong to declared_alphabet")

    sample_size_a = _validate_counts(counts_a, "counts_a")
    sample_size_b = _validate_counts(counts_b, "counts_b")
    empirical_a = {label: counts_a.get(label, 0) / sample_size_a for label in alphabet}
    empirical_b = {label: counts_b.get(label, 0) / sample_size_b for label in alphabet}
    empirical_tv = 0.5 * sum(
        abs(empirical_a[label] - empirical_b[label]) for label in alphabet
    )

    d = len(alphabet)
    log_term = log(4.0 * d / alpha)
    coordinate_a = sqrt(log_term / (2.0 * sample_size_a))
    coordinate_b = sqrt(log_term / (2.0 * sample_size_b))
    tv_radius_a = min(1.0, 0.5 * d * coordinate_a)
    tv_radius_b = min(1.0, 0.5 * d * coordinate_b)
    lower = max(0.0, empirical_tv - tv_radius_a - tv_radius_b)

    return ObservedTVLowerBound(
        confidence_level=1.0 - alpha,
        alphabet_size=d,
        sample_size_a=sample_size_a,
        sample_size_b=sample_size_b,
        empirical_tv=empirical_tv,
        coordinate_radius_a=coordinate_a,
        coordinate_radius_b=coordinate_b,
        tv_radius_a=tv_radius_a,
        tv_radius_b=tv_radius_b,
        lower_bound=lower,
    )


def sufficient_equal_sample_size_for_latent_gap(
    alphabet_size: int,
    alpha: float,
    latent_tv_gap: float,
    channel_stability_lower_bound: float,
) -> int:
    """Sufficient equal per-group sample size for a positive observed TV LCB.

    Assume a declared latent separation at least ``latent_tv_gap`` and a target
    channel satisfying

        TV(Kp, Kq) >= gamma * TV(p, q)

    with ``gamma >= channel_stability_lower_bound > 0``. Under the P72
    coordinate-Hoeffding certificate, a sufficient strict condition is

        n > 2 d^2 log(4d/alpha) / (gamma^2 * latent_tv_gap^2).

    The returned integer is the smallest integer strictly above that bound.
    This is a sufficient design bound, not a necessary sample complexity.
    """
    if not isinstance(alphabet_size, int) or isinstance(alphabet_size, bool):
        raise TypeError("alphabet_size must be an integer")
    if alphabet_size < 1:
        raise ValueError("alphabet_size must be positive")
    _open_probability(alpha, "alpha")
    _positive_unit_interval(latent_tv_gap, "latent_tv_gap")
    _positive_unit_interval(
        channel_stability_lower_bound,
        "channel_stability_lower_bound",
    )

    numerator = 2.0 * alphabet_size**2 * log(4.0 * alphabet_size / alpha)
    denominator = (channel_stability_lower_bound * latent_tv_gap) ** 2
    real_bound = numerator / denominator
    return floor(real_bound) + 1


def _normalize_joint(
    weights: Mapping[tuple[Omega, Physical, LatentTarget], float],
    name: str,
) -> dict[tuple[Omega, Physical, LatentTarget], float]:
    if not weights:
        raise ValueError(f"{name} must be nonempty")
    total = 0.0
    for value in weights.values():
        _nonnegative_finite(value, name)
        total += value
    if total <= 0.0:
        raise ValueError(f"{name} must have positive total mass")
    return {key: value / total for key, value in weights.items() if value > 0.0}


def _normalize_distribution(
    weights: Mapping[Label, float],
    name: str,
) -> dict[Label, float]:
    if not weights:
        raise ValueError(f"{name} must be nonempty")
    total = 0.0
    for value in weights.values():
        _nonnegative_finite(value, name)
        total += value
    if total <= 0.0:
        raise ValueError(f"{name} must have positive total mass")
    return {key: value / total for key, value in weights.items() if value > 0.0}


def _normalize_conditional_channel(
    weights: Mapping[tuple[Physical, LatentTarget, ObservedTarget], float],
    *,
    required_pairs: set[tuple[Physical, LatentTarget]],
) -> dict[tuple[Physical, LatentTarget, ObservedTarget], float]:
    if not weights:
        raise ValueError("measurement_channel_weights must be nonempty")
    totals: dict[tuple[Physical, LatentTarget], float] = defaultdict(float)
    for (physical, target, _), value in weights.items():
        _nonnegative_finite(value, "measurement_channel_weights")
        totals[(physical, target)] += value
    missing = required_pairs.difference(pair for pair, total in totals.items() if total > 0.0)
    if missing:
        raise ValueError("measurement channel must cover every observed (T,E_star) pair")
    return {
        key: value / totals[(key[0], key[1])]
        for key, value in weights.items()
        if value > 0.0 and (key[0], key[1]) in required_pairs
    }


def _normalize_simple_channel(
    weights: Mapping[tuple[LatentTarget, ObservedTarget], float],
    *,
    required_inputs: set[LatentTarget],
) -> dict[tuple[LatentTarget, ObservedTarget], float]:
    if not weights:
        raise ValueError("channel_weights must be nonempty")
    totals: dict[LatentTarget, float] = defaultdict(float)
    for (target, _), value in weights.items():
        _nonnegative_finite(value, "channel_weights")
        totals[target] += value
    missing = required_inputs.difference(target for target, total in totals.items() if total > 0.0)
    if missing:
        raise ValueError("channel must cover every target value with positive mass")
    return {
        key: value / totals[key[0]]
        for key, value in weights.items()
        if value > 0.0 and key[0] in required_inputs
    }


def _validate_counts(counts: Mapping[Label, int], name: str) -> int:
    total = 0
    for count in counts.values():
        if not isinstance(count, int) or isinstance(count, bool):
            raise TypeError(f"{name} must contain integer counts")
        if count < 0:
            raise ValueError(f"{name} counts must be nonnegative")
        total += count
    if total < 1:
        raise ValueError(f"{name} must contain at least one observation")
    return total


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must contain finite nonnegative values")


def _probability(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")


def _open_probability(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0 or value >= 1.0:
        raise ValueError(f"{name} must lie strictly between zero and one")


def _positive_unit_interval(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0 or value > 1.0:
        raise ValueError(f"{name} must lie in (0, 1]")
