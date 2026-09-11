"""P77 finite-sample full-law model-set separation.

P76 propagates one simultaneous finite-sample event into selected polynomial
adequacy constraints. P77 states the stronger full-law confidence-set inversion
principle: if the entire confidence region around the empirical law is disjoint
from a declared model set, the model is rejected with the same coverage level.

For a finite alphabet of size K, Hoeffding plus a union bound gives

    eps_n(alpha) = sqrt(log(2 K / alpha) / (2 n)).

On that event, ||P_hat-P||_inf <= eps_n and
||P_hat-P||_1 <= min(2, K eps_n). Distance to any nonempty model set is
1-Lipschitz in the same norm. Therefore a certified lower bound on empirical
distance that exceeds the corresponding sampling radius is enough to reject.

This module deliberately distinguishes a certified *lower* bound on distance
from an ordinary optimizer value. A numerical candidate model provides an
upper bound on distance and cannot by itself certify rejection of a continuous
model family.

The theorem is generic finite-alphabet statistics. Its repository-specific role
is to close the logical gap between P75 full-law model membership and P76
partial finite-sample polynomial rejection without assuming a chi-square null
law. It does not identify a latent state with consciousness. It does not solve
the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class FullLawSeparationCertificate:
    """Finite-sample P77 certificate from certified model-distance lower bounds."""

    confidence: float
    sample_size: int
    alphabet_size: int
    cell_linf_radius: float
    joint_l1_radius: float
    linf_distance_lower_bound: float | None
    l1_distance_lower_bound: float | None
    certified_incompatible_linf: bool
    certified_incompatible_l1: bool
    certified_incompatible: bool
    conclusion: str


def finite_alphabet_cell_linf_radius(
    sample_size: int,
    alphabet_size: int,
    alpha: float,
) -> float:
    """Return the simultaneous Hoeffding radius over K categorical cells."""

    if isinstance(sample_size, bool) or int(sample_size) != sample_size:
        raise ValueError("sample_size must be a positive integer")
    if isinstance(alphabet_size, bool) or int(alphabet_size) != alphabet_size:
        raise ValueError("alphabet_size must be a positive integer")
    sample_size = int(sample_size)
    alphabet_size = int(alphabet_size)
    if sample_size <= 0:
        raise ValueError("sample_size must be positive")
    if alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    return sqrt(log(2.0 * alphabet_size / alpha) / (2.0 * sample_size))


def finite_alphabet_joint_l1_radius(
    sample_size: int,
    alphabet_size: int,
    alpha: float,
) -> float:
    """Return the induced conservative L1 radius from the same cell event."""

    eps = finite_alphabet_cell_linf_radius(sample_size, alphabet_size, alpha)
    return min(2.0, alphabet_size * eps)


def _validate_probability_vector(probabilities: Sequence[float]) -> np.ndarray:
    array = np.asarray(probabilities, dtype=float)
    if array.ndim != 1 or array.size == 0:
        raise ValueError("probabilities must be a nonempty one-dimensional vector")
    if not np.all(np.isfinite(array)):
        raise ValueError("probabilities must be finite")
    if np.any(array < 0.0):
        raise ValueError("probabilities must be nonnegative")
    total = float(array.sum())
    if total <= 0.0:
        raise ValueError("probabilities must have positive total mass")
    return array / total


def finite_model_family_distances(
    empirical_law: Sequence[float],
    model_family: Iterable[Sequence[float]],
) -> tuple[float, float]:
    """Return exact empirical distances to a finite declared model family.

    The result is exact up to ordinary floating-point evaluation for the finite
    list supplied to the function. It is *not* a lower bound for a larger
    continuous family that happens to contain those points.
    """

    empirical = _validate_probability_vector(empirical_law)
    candidates = [_validate_probability_vector(candidate) for candidate in model_family]
    if not candidates:
        raise ValueError("model_family must contain at least one probability vector")
    if any(candidate.shape != empirical.shape for candidate in candidates):
        raise ValueError("every model law must have the same alphabet as empirical_law")

    linf = min(float(np.max(np.abs(empirical - candidate))) for candidate in candidates)
    l1 = min(float(np.sum(np.abs(empirical - candidate))) for candidate in candidates)
    return linf, l1


def _validate_distance_lower_bound(value: float | None, name: str) -> float | None:
    if value is None:
        return None
    value = float(value)
    if not np.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def full_law_separation_certificate(
    *,
    sample_size: int,
    alphabet_size: int,
    alpha: float = 0.05,
    linf_distance_lower_bound: float | None = None,
    l1_distance_lower_bound: float | None = None,
) -> FullLawSeparationCertificate:
    """Certify full-law model incompatibility from sound distance lower bounds.

    A supplied lower bound L_inf must satisfy

        L_inf <= inf_{Q in M} ||P_hat-Q||_inf,

    and similarly for L1. If the lower bound exceeds the sampling radius, the
    P77 confidence region cannot intersect M.

    An optimizer's best-fit value is generally an *upper* bound on the infimum
    and must not be passed here as though it were a certified lower bound.
    """

    linf_lower = _validate_distance_lower_bound(
        linf_distance_lower_bound,
        "linf_distance_lower_bound",
    )
    l1_lower = _validate_distance_lower_bound(
        l1_distance_lower_bound,
        "l1_distance_lower_bound",
    )
    if linf_lower is None and l1_lower is None:
        raise ValueError("at least one certified distance lower bound is required")

    eps = finite_alphabet_cell_linf_radius(sample_size, alphabet_size, alpha)
    l1_radius = finite_alphabet_joint_l1_radius(sample_size, alphabet_size, alpha)

    reject_linf = linf_lower is not None and linf_lower > eps
    reject_l1 = l1_lower is not None and l1_lower > l1_radius
    reject = bool(reject_linf or reject_l1)

    if reject:
        witnesses = []
        if reject_linf:
            witnesses.append("L-infinity")
        if reject_l1:
            witnesses.append("L1")
        conclusion = (
            "certified incompatible with the declared model set by "
            + " and ".join(witnesses)
            + " confidence-region separation"
        )
    else:
        conclusion = (
            "not rejected by the supplied P77 distance lower bounds; "
            "non-rejection is not model acceptance"
        )

    return FullLawSeparationCertificate(
        confidence=1.0 - alpha,
        sample_size=int(sample_size),
        alphabet_size=int(alphabet_size),
        cell_linf_radius=float(eps),
        joint_l1_radius=float(l1_radius),
        linf_distance_lower_bound=linf_lower,
        l1_distance_lower_bound=l1_lower,
        certified_incompatible_linf=bool(reject_linf),
        certified_incompatible_l1=bool(reject_l1),
        certified_incompatible=reject,
        conclusion=conclusion,
    )


def exact_finite_family_separation_certificate(
    empirical_law: Sequence[float],
    model_family: Iterable[Sequence[float]],
    *,
    sample_size: int,
    alpha: float = 0.05,
) -> FullLawSeparationCertificate:
    """Apply P77 exactly when the declared model family itself is finite."""

    empirical = _validate_probability_vector(empirical_law)
    linf_distance, l1_distance = finite_model_family_distances(empirical, model_family)
    return full_law_separation_certificate(
        sample_size=sample_size,
        alphabet_size=int(empirical.size),
        alpha=alpha,
        linf_distance_lower_bound=linf_distance,
        l1_distance_lower_bound=l1_distance,
    )


def population_model_distance_interval(
    empirical_distance: float,
    sampling_radius: float,
    *,
    maximum_distance: float | None = None,
) -> tuple[float, float]:
    """Transport an exact empirical distance-to-set through a sampling ball.

    Distance to a nonempty set is 1-Lipschitz in any metric induced by a norm,
    hence |d(P_hat,M)-d(P,M)| is at most ||P_hat-P||.
    """

    empirical_distance = float(empirical_distance)
    sampling_radius = float(sampling_radius)
    if not np.isfinite(empirical_distance) or empirical_distance < 0.0:
        raise ValueError("empirical_distance must be finite and nonnegative")
    if not np.isfinite(sampling_radius) or sampling_radius < 0.0:
        raise ValueError("sampling_radius must be finite and nonnegative")
    if maximum_distance is not None:
        maximum_distance = float(maximum_distance)
        if not np.isfinite(maximum_distance) or maximum_distance < 0.0:
            raise ValueError("maximum_distance must be finite and nonnegative")

    lower = max(0.0, empirical_distance - sampling_radius)
    upper = empirical_distance + sampling_radius
    if maximum_distance is not None:
        upper = min(upper, maximum_distance)
    return float(lower), float(upper)


def sufficient_linf_separation_sample_size(
    population_distance_margin: float,
    alphabet_size: int,
    alpha: float = 0.05,
) -> int:
    """Sufficient n for eventual P77 L-infinity rejection at margin tau.

    If d_inf(P,M) >= tau and eps_n < tau/2, then on the simultaneous
    confidence event

        d_inf(P_hat,M) >= tau-eps_n > eps_n,

    so exact or certified empirical model-set distance rejects M.
    """

    tau = float(population_distance_margin)
    if not 0.0 < tau <= 1.0:
        raise ValueError("population_distance_margin must lie in (0, 1]")
    if isinstance(alphabet_size, bool) or int(alphabet_size) != alphabet_size:
        raise ValueError("alphabet_size must be a positive integer")
    alphabet_size = int(alphabet_size)
    if alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")

    threshold = 2.0 * log(2.0 * alphabet_size / alpha) / tau**2
    return int(np.floor(threshold)) + 1


def sufficient_l1_separation_sample_size(
    population_distance_margin: float,
    alphabet_size: int,
    alpha: float = 0.05,
) -> int:
    """Sufficient n for eventual P77 L1 rejection at margin tau.

    The formula uses the uncapped radius K eps_n and the sufficient condition
    K eps_n < tau/2.
    """

    tau = float(population_distance_margin)
    if not 0.0 < tau <= 2.0:
        raise ValueError("population_distance_margin must lie in (0, 2]")
    if isinstance(alphabet_size, bool) or int(alphabet_size) != alphabet_size:
        raise ValueError("alphabet_size must be a positive integer")
    alphabet_size = int(alphabet_size)
    if alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")

    threshold = (
        2.0 * alphabet_size**2 * log(2.0 * alphabet_size / alpha) / tau**2
    )
    return int(np.floor(threshold)) + 1
