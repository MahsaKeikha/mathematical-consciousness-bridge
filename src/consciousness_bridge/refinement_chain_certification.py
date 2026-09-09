"""Simultaneous finite-sample certification for Proposition 22.

Proposition 22 combines the P20 finite-alphabet confidence construction with
the P21 descriptor-refinement theorem.  When every tested descriptor is a
predeclared deterministic function of the same sampled physical state, one
confidence event for the empirical ``(Omega, E)`` distribution controls every
residual and every refinement gain in the chain simultaneously.

The resulting guarantee does not require a separate union-bound allocation over
descriptor levels.  This is because all level-specific distributions are
deterministic pushforwards of the same base distribution.  The result remains a
finite-alphabet IID baseline and does not establish physical completeness.
"""

from collections.abc import Hashable, Iterable, Sequence
from dataclasses import dataclass

from consciousness_bridge.descriptor_refinement_residual import (
    descriptor_refinement_violations,
    is_descriptor_refinement,
)
from consciousness_bridge.finite_sample_residual_certification import (
    conditional_information_continuity_bound,
    hoeffding_joint_tv_radius,
    maximum_conditional_mutual_information,
)
from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    empirical_joint_from_records,
)


@dataclass(frozen=True)
class SimultaneousCMIInterval:
    """One CMI interval controlled by the shared Proposition 22 event."""

    estimate: float
    lower: float
    upper: float
    continuity_radius: float
    certified_positive: bool


@dataclass(frozen=True)
class RefinementGainInterval:
    """Certified interval for one P21 refinement gain."""

    estimate: float
    lower: float
    upper: float
    direct_lower: float
    direct_upper: float
    difference_lower: float
    difference_upper: float
    continuity_radius: float
    certified_positive: bool


@dataclass(frozen=True)
class RefinementChainConfidenceCertificate:
    """Simultaneous finite-sample certificate for a nested descriptor chain."""

    residual_intervals: tuple[SimultaneousCMIInterval, ...]
    gain_intervals: tuple[RefinementGainInterval, ...]
    base_tv_radius: float
    alpha: float
    simultaneous_coverage: float
    sample_size: int
    empirical_chain_rule_error: float
    terminal_residual_certified_positive: bool


def _validate_positive_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def _bounded_interval(
    estimate: float, radius: float, maximum: float
) -> SimultaneousCMIInterval:
    estimate = min(maximum, max(0.0, estimate))
    lower = max(0.0, estimate - radius)
    upper = min(maximum, estimate + radius)
    return SimultaneousCMIInterval(
        estimate=estimate,
        lower=lower,
        upper=upper,
        continuity_radius=radius,
        certified_positive=lower > 0.0,
    )


def _validate_records_and_chain(
    records: Sequence[tuple[Hashable, Sequence[Hashable], Hashable]],
    omega_size: int,
    descriptor_sizes: Sequence[int],
    target_size: int,
) -> tuple[list[Hashable], list[list[Hashable]], list[Hashable]]:
    _validate_positive_integer(omega_size, "omega_size")
    _validate_positive_integer(target_size, "target_size")
    if not descriptor_sizes:
        raise ValueError("descriptor_sizes must contain at least one level")
    for level, size in enumerate(descriptor_sizes):
        _validate_positive_integer(size, f"descriptor_sizes[{level}]")

    if not records:
        raise ValueError("records must contain at least one sample")
    if any(len(record) != 3 for record in records):
        raise ValueError("each record must contain omega, descriptors, target")

    level_count = len(records[0][1])
    if level_count != len(descriptor_sizes):
        raise ValueError("descriptor_sizes must match the number of descriptor levels")
    if any(len(record[1]) != level_count for record in records):
        raise ValueError("all descriptor chains must have the same length")

    omega_labels = [record[0] for record in records]
    target_labels = [record[2] for record in records]
    levels = [
        [record[1][level] for record in records]
        for level in range(level_count)
    ]

    if len(set(omega_labels)) > omega_size:
        raise ValueError("observed omega labels exceed omega_size")
    if len(set(target_labels)) > target_size:
        raise ValueError("observed target labels exceed target_size")
    for level, (labels, declared_size) in enumerate(zip(levels, descriptor_sizes)):
        if len(set(labels)) > declared_size:
            raise ValueError(
                f"observed descriptor labels exceed descriptor_sizes[{level}]"
            )
        violations = descriptor_refinement_violations(labels, omega_labels)
        if violations:
            raise ValueError(
                f"descriptor level {level} must be a deterministic function of omega"
            )

    for level in range(1, level_count):
        if not is_descriptor_refinement(levels[level - 1], levels[level]):
            raise ValueError(
                f"descriptor level {level} does not refine level {level - 1}"
            )

    return omega_labels, levels, target_labels


def certify_refinement_chain_from_records(
    records: Iterable[tuple[Hashable, Sequence[Hashable], Hashable]],
    *,
    omega_size: int,
    descriptor_sizes: Sequence[int],
    target_size: int,
    alpha: float = 0.05,
    tolerance: float = 1e-10,
) -> RefinementChainConfidenceCertificate:
    """Return the simultaneous Proposition 22 certificate.

    Records are ``(omega, descriptors, target)`` with descriptor levels ordered
    from coarsest to finest.  The descriptors must be predeclared deterministic
    functions of ``omega`` and form a nested refinement chain on the observed
    support.

    A single Hoeffding/union-bound event is built for the base ``(omega,target)``
    empirical law.  Total-variation contraction then controls all deterministic
    pushforwards needed for residual and refinement-gain estimates at once.
    """
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between 0 and 1")
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative")

    materialized = list(records)
    omega_labels, levels, target_labels = _validate_records_and_chain(
        materialized,
        omega_size=omega_size,
        descriptor_sizes=descriptor_sizes,
        target_size=target_size,
    )

    sample_size = len(materialized)
    base_alphabet_size = omega_size * target_size
    base_tv_radius = hoeffding_joint_tv_radius(
        sample_size=sample_size,
        alphabet_size=base_alphabet_size,
        alpha=alpha,
    )

    residual_intervals: list[SimultaneousCMIInterval] = []
    for labels, physical_size in zip(levels, descriptor_sizes):
        empirical_joint = empirical_joint_from_records(
            (omega, physical, target)
            for omega, physical, target in zip(
                omega_labels, labels, target_labels
            )
        )
        estimate = conditional_mutual_information(empirical_joint)
        continuity_radius = conditional_information_continuity_bound(
            base_tv_radius,
            omega_size=omega_size,
            physical_size=physical_size,
            target_size=target_size,
        )
        maximum = maximum_conditional_mutual_information(
            omega_size=omega_size,
            target_size=target_size,
        )
        residual_intervals.append(
            _bounded_interval(estimate, continuity_radius, maximum)
        )

    gain_intervals: list[RefinementGainInterval] = []
    chain_rule_errors: list[float] = []
    for level in range(1, len(levels)):
        coarse_labels = levels[level - 1]
        fine_labels = levels[level]
        empirical_joint = empirical_joint_from_records(
            (fine, coarse, target)
            for fine, coarse, target in zip(
                fine_labels, coarse_labels, target_labels
            )
        )
        estimate = conditional_mutual_information(empirical_joint)
        continuity_radius = conditional_information_continuity_bound(
            base_tv_radius,
            omega_size=descriptor_sizes[level],
            physical_size=descriptor_sizes[level - 1],
            target_size=target_size,
        )
        maximum = maximum_conditional_mutual_information(
            omega_size=descriptor_sizes[level],
            target_size=target_size,
        )

        direct_lower = max(0.0, estimate - continuity_radius)
        direct_upper = min(maximum, estimate + continuity_radius)

        previous_residual = residual_intervals[level - 1]
        current_residual = residual_intervals[level]
        difference_lower = max(
            0.0, previous_residual.lower - current_residual.upper
        )
        difference_upper = min(
            maximum, previous_residual.upper - current_residual.lower
        )
        difference_upper = max(0.0, difference_upper)

        lower = max(direct_lower, difference_lower)
        upper = min(direct_upper, difference_upper)
        if lower > upper + tolerance:
            raise AssertionError("certified refinement-gain intervals do not intersect")
        if lower > upper:
            midpoint = 0.5 * (lower + upper)
            lower = midpoint
            upper = midpoint

        empirical_difference = (
            residual_intervals[level - 1].estimate
            - residual_intervals[level].estimate
        )
        chain_rule_errors.append(abs(empirical_difference - estimate))

        gain_intervals.append(
            RefinementGainInterval(
                estimate=estimate,
                lower=lower,
                upper=upper,
                direct_lower=direct_lower,
                direct_upper=direct_upper,
                difference_lower=difference_lower,
                difference_upper=difference_upper,
                continuity_radius=continuity_radius,
                certified_positive=lower > 0.0,
            )
        )

    empirical_chain_rule_error = max(chain_rule_errors, default=0.0)
    if empirical_chain_rule_error > tolerance:
        raise AssertionError("empirical P21 chain-rule identity did not close")

    residual_tuple = tuple(residual_intervals)
    return RefinementChainConfidenceCertificate(
        residual_intervals=residual_tuple,
        gain_intervals=tuple(gain_intervals),
        base_tv_radius=base_tv_radius,
        alpha=alpha,
        simultaneous_coverage=1.0 - alpha,
        sample_size=sample_size,
        empirical_chain_rule_error=empirical_chain_rule_error,
        terminal_residual_certified_positive=residual_tuple[-1].certified_positive,
    )
