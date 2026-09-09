"""Finite-sample certification for Proposition 20.

The functions in this module certify a population conditional-mutual-information
residual from finite IID categorical data. The result is deliberately
conservative. A certified positive residual shows that the declared physical
descriptor does not screen off the target under the stated finite-alphabet
model. It does not identify the missing information as nonphysical.
"""

from collections.abc import Iterable
from dataclasses import dataclass
from math import log, sqrt

from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    empirical_joint_from_records,
)


@dataclass(frozen=True)
class CMIConfidenceCertificate:
    """Finite-sample confidence certificate for conditional mutual information."""

    estimate: float
    lower: float
    upper: float
    tv_radius: float
    continuity_radius: float
    alpha: float
    sample_size: int
    certified_positive: bool


def _validate_alphabet_size(size: int, name: str) -> None:
    if isinstance(size, bool) or not isinstance(size, int) or size < 1:
        raise ValueError(f"{name} must be a positive integer")


def binary_entropy(probability: float) -> float:
    """Binary entropy in nats."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1]")
    if probability in (0.0, 1.0):
        return 0.0
    return -probability * log(probability) - (1.0 - probability) * log(
        1.0 - probability
    )


def entropy_continuity_bound(tv_radius: float, alphabet_size: int) -> float:
    """Bound entropy change when TV distance is at most ``tv_radius``.

    For alphabet size ``d``, the sharp finite-alphabet expression

        h_2(delta) + delta log(d - 1)

    increases up to ``delta = 1 - 1/d``. When only an upper radius is known,
    the safe uniform bound is therefore this expression below that threshold
    and the trivial entropy range ``log(d)`` above it. The result is in nats.
    """
    _validate_alphabet_size(alphabet_size, "alphabet_size")
    if not 0.0 <= tv_radius <= 1.0:
        raise ValueError("tv_radius must lie in [0, 1]")
    if alphabet_size == 1:
        return 0.0

    threshold = 1.0 - 1.0 / alphabet_size
    if tv_radius >= threshold:
        return log(alphabet_size)
    return binary_entropy(tv_radius) + tv_radius * log(alphabet_size - 1)


def hoeffding_joint_tv_radius(
    sample_size: int, alphabet_size: int, alpha: float
) -> float:
    """Return a simultaneous TV radius from cellwise Hoeffding bounds.

    For ``d`` declared joint categories and ``n`` IID samples, a union bound over
    empirical cell frequencies gives, with probability at least ``1 - alpha``,

        TV(P_hat, P) <= (d / 2) sqrt(log(2d/alpha) / (2n)).

    The returned radius is clipped at one.
    """
    invalid_sample_size = (
        isinstance(sample_size, bool)
        or not isinstance(sample_size, int)
        or sample_size < 1
    )
    if invalid_sample_size:
        raise ValueError("sample_size must be a positive integer")
    _validate_alphabet_size(alphabet_size, "alphabet_size")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between 0 and 1")

    cell_radius = sqrt(log(2.0 * alphabet_size / alpha) / (2.0 * sample_size))
    return min(1.0, 0.5 * alphabet_size * cell_radius)


def maximum_conditional_mutual_information(
    omega_size: int, target_size: int
) -> float:
    """Return the universal finite-alphabet upper bound for I(E;Omega|T)."""
    _validate_alphabet_size(omega_size, "omega_size")
    _validate_alphabet_size(target_size, "target_size")
    return min(log(omega_size), log(target_size))


def conditional_information_continuity_bound(
    tv_radius: float,
    omega_size: int,
    physical_size: int,
    target_size: int,
) -> float:
    """Bound CMI change induced by a joint-distribution TV perturbation.

    The identity

        I(E;Omega|T) = H(E,T) + H(Omega,T) - H(T) - H(E,Omega,T)

    is combined with TV contraction under marginalization and the finite-alphabet
    entropy continuity bound. The result is capped by the full possible range of
    conditional mutual information.
    """
    if not 0.0 <= tv_radius <= 1.0:
        raise ValueError("tv_radius must lie in [0, 1]")
    _validate_alphabet_size(omega_size, "omega_size")
    _validate_alphabet_size(physical_size, "physical_size")
    _validate_alphabet_size(target_size, "target_size")

    dimensions = (
        target_size * physical_size,
        omega_size * physical_size,
        physical_size,
        target_size * omega_size * physical_size,
    )
    raw_bound = sum(
        entropy_continuity_bound(tv_radius, dimension) for dimension in dimensions
    )
    full_range = maximum_conditional_mutual_information(omega_size, target_size)
    return min(full_range, raw_bound)


def finite_sample_cmi_certificate(
    estimate: float,
    sample_size: int,
    omega_size: int,
    physical_size: int,
    target_size: int,
    alpha: float = 0.05,
) -> CMIConfidenceCertificate:
    """Certify a finite-sample interval for population I(E;Omega|T), in nats."""
    max_cmi = maximum_conditional_mutual_information(omega_size, target_size)
    _validate_alphabet_size(physical_size, "physical_size")
    if estimate < -1e-12 or estimate > max_cmi + 1e-12:
        raise ValueError("estimate must lie in the valid conditional-information range")
    estimate = min(max_cmi, max(0.0, estimate))

    joint_size = omega_size * physical_size * target_size
    tv_radius = hoeffding_joint_tv_radius(sample_size, joint_size, alpha)
    continuity_radius = conditional_information_continuity_bound(
        tv_radius,
        omega_size=omega_size,
        physical_size=physical_size,
        target_size=target_size,
    )

    lower = max(0.0, estimate - continuity_radius)
    upper = min(max_cmi, estimate + continuity_radius)
    return CMIConfidenceCertificate(
        estimate=estimate,
        lower=lower,
        upper=upper,
        tv_radius=tv_radius,
        continuity_radius=continuity_radius,
        alpha=alpha,
        sample_size=sample_size,
        certified_positive=lower > 0.0,
    )


def certify_cmi_from_records(
    records: Iterable[tuple[object, object, object]],
    omega_size: int,
    physical_size: int,
    target_size: int,
    alpha: float = 0.05,
) -> CMIConfidenceCertificate:
    """Estimate CMI from records and return the Proposition 20 certificate."""
    _validate_alphabet_size(omega_size, "omega_size")
    _validate_alphabet_size(physical_size, "physical_size")
    _validate_alphabet_size(target_size, "target_size")

    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    if any(len(record) != 3 for record in materialized):
        raise ValueError("each record must contain omega, physical, target")

    observed_sizes = (
        len({record[0] for record in materialized}),
        len({record[1] for record in materialized}),
        len({record[2] for record in materialized}),
    )
    declared_sizes = (omega_size, physical_size, target_size)
    if any(
        observed > declared
        for observed, declared in zip(observed_sizes, declared_sizes)
    ):
        raise ValueError("observed labels exceed the declared alphabet sizes")

    weights = empirical_joint_from_records(materialized)
    estimate = conditional_mutual_information(weights)
    return finite_sample_cmi_certificate(
        estimate=estimate,
        sample_size=len(materialized),
        omega_size=omega_size,
        physical_size=physical_size,
        target_size=target_size,
        alpha=alpha,
    )
