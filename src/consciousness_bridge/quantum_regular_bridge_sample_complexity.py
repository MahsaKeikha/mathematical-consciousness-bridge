"""Proposition 42: finite-sample design for quantum regular-bridge obstruction.

The module combines a fixed informationally complete measurement, a declared
linear reconstruction stability constant, categorical target sampling, and the
P40-P41 Lipschitz regularity obstruction.

The bounds use coordinate Hoeffding inequalities plus union bounds. They are
transparent and conservative, not statistically optimal. The result is relative
to the declared tomography design and bridge regularity class and does not imply
quantum incompleteness or identify any target with consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log, sqrt


@dataclass(frozen=True)
class RegularBridgeSampleComplexity:
    """Sufficient per-preparation sample sizes for one positive population gap."""

    quantum_samples_per_preparation: int
    target_samples_per_preparation: int
    population_regularity_gap: float
    target_gap_fraction: float
    quantum_gap_fraction: float
    confidence_lower_bound: float


def coordinate_hoeffding_radius(
    *,
    preparation_count: int,
    outcome_count: int,
    samples_per_preparation: int,
    alpha: float,
) -> float:
    """Return a simultaneous coordinate-frequency Hoeffding radius.

    For K preparations and m outcomes, the returned value t satisfies
    |p_x(j)-p_hat_x(j)| <= t simultaneously for all K*m coordinates with
    probability at least 1-alpha under independent IID repetitions within each
    declared preparation stream.
    """
    _positive_integer(preparation_count, "preparation_count")
    _positive_integer(outcome_count, "outcome_count")
    _positive_integer(samples_per_preparation, "samples_per_preparation")
    _alpha(alpha)
    return sqrt(
        log(2.0 * preparation_count * outcome_count / alpha)
        / (2.0 * samples_per_preparation)
    )


def quantum_linear_inversion_trace_radius(
    *,
    preparation_count: int,
    measurement_outcomes: int,
    samples_per_preparation: int,
    alpha_quantum: float,
    reconstruction_stability: float,
) -> float:
    """Return the P42 trace-norm radius for a fixed linear IC reconstruction.

    The declared reconstruction map R must obey

        0.5 * ||R(v)||_1 <= reconstruction_stability * ||v||_1.

    The raw linear inversion estimate R(p_hat) need not be positive semidefinite.
    The bound is a trace-norm statement around that Hermitian reconstruction, not
    a claim that the raw estimate is itself a physical density operator.
    """
    if reconstruction_stability < 0.0:
        raise ValueError("reconstruction_stability must be nonnegative")
    coordinate = coordinate_hoeffding_radius(
        preparation_count=preparation_count,
        outcome_count=measurement_outcomes,
        samples_per_preparation=samples_per_preparation,
        alpha=alpha_quantum,
    )
    return reconstruction_stability * measurement_outcomes * coordinate


def categorical_target_tv_radius(
    *,
    preparation_count: int,
    target_outcomes: int,
    samples_per_preparation: int,
    alpha_target: float,
) -> float:
    """Return a simultaneous total-variation radius for categorical targets."""
    coordinate = coordinate_hoeffding_radius(
        preparation_count=preparation_count,
        outcome_count=target_outcomes,
        samples_per_preparation=samples_per_preparation,
        alpha=alpha_target,
    )
    return min(1.0, 0.5 * target_outcomes * coordinate)


def empirical_lipschitz_obstruction_margin(
    *,
    estimated_quantum_pair_trace_norm_half: float,
    quantum_radius: float,
    estimated_target_tv: float,
    target_radius: float,
    lipschitz_constant: float,
) -> float:
    """Return the direct P41-style empirical pair obstruction margin.

    The quantum pair input is 0.5*||R(p_hat_x)-R(p_hat_y)||_1 for the raw linear
    reconstructions. It may exceed one because the reconstructions need not be
    physical; the final true-state envelope is clipped at one.
    """
    if estimated_quantum_pair_trace_norm_half < 0.0:
        raise ValueError("estimated_quantum_pair_trace_norm_half must be nonnegative")
    if quantum_radius < 0.0:
        raise ValueError("quantum_radius must be nonnegative")
    _unit_interval(estimated_target_tv, "estimated_target_tv")
    _unit_interval(target_radius, "target_radius")
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")

    quantum_upper = min(
        1.0,
        estimated_quantum_pair_trace_norm_half + 2.0 * quantum_radius,
    )
    target_lower = max(0.0, estimated_target_tv - 2.0 * target_radius)
    return target_lower - lipschitz_constant * quantum_upper


def regularity_gap_sample_sizes(
    *,
    preparation_count: int,
    measurement_outcomes: int,
    target_outcomes: int,
    population_regularity_gap: float,
    lipschitz_constant: float,
    reconstruction_stability: float,
    alpha_quantum: float,
    alpha_target: float,
    target_gap_fraction: float = 0.5,
) -> RegularBridgeSampleComplexity:
    """Return sufficient per-preparation sample sizes for a positive P42 margin.

    Let Delta = d_Y - L*d_Q > 0 be the population regularity gap. On the shared
    confidence event, the empirical certificate obeys

        M_hat >= Delta - 4*epsilon_Y - 4*L*r_Q.

    The requested target_gap_fraction lambda allocates lambda*Delta to the target
    uncertainty and (1-lambda)*Delta to the quantum uncertainty. The returned
    integer sample sizes make each contribution no larger than its allocation.
    """
    _positive_integer(preparation_count, "preparation_count")
    _positive_integer(measurement_outcomes, "measurement_outcomes")
    _positive_integer(target_outcomes, "target_outcomes")
    if population_regularity_gap <= 0.0:
        raise ValueError("population_regularity_gap must be positive")
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    if reconstruction_stability < 0.0:
        raise ValueError("reconstruction_stability must be nonnegative")
    _alpha(alpha_quantum)
    _alpha(alpha_target)
    if not 0.0 < target_gap_fraction < 1.0:
        raise ValueError("target_gap_fraction must lie in (0, 1)")

    delta = population_regularity_gap
    lam = target_gap_fraction
    quantum_fraction = 1.0 - lam

    target_n = ceil(
        2.0
        * target_outcomes**2
        * log(2.0 * preparation_count * target_outcomes / alpha_target)
        / (lam**2 * delta**2)
    )

    if lipschitz_constant == 0.0 or reconstruction_stability == 0.0:
        quantum_n = 1
    else:
        quantum_n = ceil(
            8.0
            * lipschitz_constant**2
            * reconstruction_stability**2
            * measurement_outcomes**2
            * log(2.0 * preparation_count * measurement_outcomes / alpha_quantum)
            / (quantum_fraction**2 * delta**2)
        )

    return RegularBridgeSampleComplexity(
        quantum_samples_per_preparation=quantum_n,
        target_samples_per_preparation=target_n,
        population_regularity_gap=delta,
        target_gap_fraction=lam,
        quantum_gap_fraction=quantum_fraction,
        confidence_lower_bound=max(0.0, 1.0 - alpha_quantum - alpha_target),
    )


def population_margin_lower_bound(
    *,
    population_regularity_gap: float,
    target_radius: float,
    quantum_radius: float,
    lipschitz_constant: float,
) -> float:
    """Return Delta - 4*epsilon_Y - 4*L*r_Q."""
    if population_regularity_gap < 0.0:
        raise ValueError("population_regularity_gap must be nonnegative")
    _unit_interval(target_radius, "target_radius")
    if quantum_radius < 0.0:
        raise ValueError("quantum_radius must be nonnegative")
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    return (
        population_regularity_gap
        - 4.0 * target_radius
        - 4.0 * lipschitz_constant * quantum_radius
    )


def _positive_integer(value: int, name: str) -> None:
    if value < 1:
        raise ValueError(f"{name} must be positive")


def _alpha(value: float) -> None:
    if not 0.0 < value < 1.0:
        raise ValueError("alpha must lie in (0, 1)")


def _unit_interval(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")
