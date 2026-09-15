"""Exact threshold certification for the P94 finite-range dependence gate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.finite_range_dependent_sign_coherence import (
    P94DependentRadiusCertificate,
    certified_p94_dependent_squared_radius,
)

_WITNESS_RADIUS = Fraction(1, 24)
_ALPHA_95 = Fraction(1, 20)


@dataclass(frozen=True)
class P94WitnessThresholdCertificate:
    dependence_range: int
    color_count: int
    alpha: Fraction
    witness_radius: Fraction
    last_noncertifying_sample_size: int
    first_certifying_sample_size: int
    last_radius: P94DependentRadiusCertificate
    first_radius: P94DependentRadiusCertificate
    base_profile_sample_size: int
    first_exact_replication_sample_size: int


def _validate_dependence_range(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("dependence_range must be a nonnegative integer")
    return value


def certify_p94_witness_95_threshold_exact(
    *,
    dependence_range: int,
    series_terms: int = 20,
) -> P94WitnessThresholdCertificate:
    """Locate the first integer clearing the P94 witness radius at 95 percent.

    P93 certifies that 288 log(280) lies strictly between 1622 and 1623.
    For q=m+1, the P94 threshold is q times that real number. Hence the first
    integer lies between 1622*q and 1623*q. Exact P79 logarithm brackets then
    classify candidates by monotone binary search.
    """

    dependence_range = _validate_dependence_range(dependence_range)
    color_count = dependence_range + 1
    target_squared = _WITNESS_RADIUS * _WITNESS_RADIUS
    low = 1622 * color_count
    high = 1623 * color_count

    def radius(sample_size: int) -> P94DependentRadiusCertificate:
        return certified_p94_dependent_squared_radius(
            sample_size=sample_size,
            dependence_range=dependence_range,
            alpha=_ALPHA_95,
            series_terms=series_terms,
        )

    low_radius = radius(low)
    high_radius = radius(high)
    if low_radius.squared_radius_lower < target_squared:
        raise RuntimeError("log bracket does not certify lower threshold endpoint")
    if high_radius.squared_radius_upper >= target_squared:
        raise RuntimeError("log bracket does not certify upper threshold endpoint")

    while high - low > 1:
        mid = (low + high) // 2
        mid_radius = radius(mid)
        if mid_radius.squared_radius_upper < target_squared:
            high = mid
        elif mid_radius.squared_radius_lower >= target_squared:
            low = mid
        else:
            raise RuntimeError("log bracket is too wide to classify threshold candidate")

    last_radius = radius(low)
    first_radius = radius(high)
    base_sample_size = 24
    first_replication = ((high + base_sample_size - 1) // base_sample_size) * base_sample_size
    return P94WitnessThresholdCertificate(
        dependence_range=dependence_range,
        color_count=color_count,
        alpha=_ALPHA_95,
        witness_radius=_WITNESS_RADIUS,
        last_noncertifying_sample_size=low,
        first_certifying_sample_size=high,
        last_radius=last_radius,
        first_radius=first_radius,
        base_profile_sample_size=base_sample_size,
        first_exact_replication_sample_size=first_replication,
    )
