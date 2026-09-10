"""Proposition 42: finite-sample IC-POVM obstruction sample complexity.

The module instantiates the corrected P41 population design inequality with an
explicit finite-outcome informationally complete measurement model. Quantum-state
confidence radii are derived from coordinatewise Hoeffding concentration and a
declared linear-reconstruction trace-norm stability constant. Target-law radii use
the same concentration argument on a finite target alphabet.

The result is conditional on IID sampling, the declared IC reconstruction model,
and the Lipschitz bridge class. It does not establish quantum incompleteness or
identify any target with consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log, sqrt


@dataclass(frozen=True)
class P42SampleComplexityCertificate:
    population_gap: float
    target_sample_size: int
    quantum_sample_size: int
    target_radius: float
    quantum_radius: float
    uncertainty_budget: float
    certified_by_bound: bool


def simultaneous_target_tv_radius(
    sample_size: int,
    preparation_count: int,
    target_outcome_count: int,
    alpha_target: float,
) -> float:
    """Return the P42 simultaneous categorical target-TV radius.

    Coordinatewise Hoeffding plus a union bound over every preparation and target
    outcome gives ||P_x - P_hat_x||_TV <= epsilon simultaneously.
    """
    _positive_int(sample_size, "sample_size")
    _positive_int(preparation_count, "preparation_count")
    _positive_int(target_outcome_count, "target_outcome_count")
    _alpha(alpha_target, "alpha_target")
    term = log(2.0 * preparation_count * target_outcome_count / alpha_target)
    return min(
        1.0,
        0.5
        * target_outcome_count
        * sqrt(term / (2.0 * sample_size)),
    )


def simultaneous_ic_povm_trace_radius(
    sample_size: int,
    preparation_count: int,
    povm_outcome_count: int,
    reconstruction_stability: float,
    alpha_quantum: float,
) -> float:
    """Return the P42 simultaneous physical-state trace-distance radius.

    Let A be a linear IC reconstruction map satisfying
    ||A(v)||_1 <= kappa ||v||_1. Linear inversion followed by trace-norm projection
    onto the density operators gives D(rho_x, rho_hat_x) <=
    kappa * m_Q * sqrt(log(2 N m_Q / alpha_Q)/(2 n_Q)).
    """
    _positive_int(sample_size, "sample_size")
    _positive_int(preparation_count, "preparation_count")
    _positive_int(povm_outcome_count, "povm_outcome_count")
    if reconstruction_stability <= 0.0:
        raise ValueError("reconstruction_stability must be positive")
    _alpha(alpha_quantum, "alpha_quantum")
    term = log(2.0 * preparation_count * povm_outcome_count / alpha_quantum)
    return min(
        1.0,
        reconstruction_stability
        * povm_outcome_count
        * sqrt(term / (2.0 * sample_size)),
    )


def sufficient_target_sample_size(
    population_gap: float,
    preparation_count: int,
    target_outcome_count: int,
    alpha_target: float,
    *,
    target_budget_fraction: float = 0.5,
) -> int:
    """Return sufficient per-preparation target trials for a chosen gap budget."""
    _positive_gap(population_gap)
    _budget_fraction(target_budget_fraction)
    _positive_int(preparation_count, "preparation_count")
    _positive_int(target_outcome_count, "target_outcome_count")
    _alpha(alpha_target, "alpha_target")
    term = log(2.0 * preparation_count * target_outcome_count / alpha_target)
    numerator = 2.0 * target_outcome_count**2 * term
    denominator = target_budget_fraction**2 * population_gap**2
    return max(1, ceil(numerator / denominator))


def sufficient_quantum_sample_size(
    population_gap: float,
    lipschitz_constant: float,
    preparation_count: int,
    povm_outcome_count: int,
    reconstruction_stability: float,
    alpha_quantum: float,
    *,
    target_budget_fraction: float = 0.5,
) -> int:
    """Return sufficient per-preparation IC-POVM trials for the quantum budget."""
    _positive_gap(population_gap)
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    if lipschitz_constant == 0.0:
        return 1
    _budget_fraction(target_budget_fraction)
    _positive_int(preparation_count, "preparation_count")
    _positive_int(povm_outcome_count, "povm_outcome_count")
    if reconstruction_stability <= 0.0:
        raise ValueError("reconstruction_stability must be positive")
    _alpha(alpha_quantum, "alpha_quantum")
    quantum_fraction = 1.0 - target_budget_fraction
    term = log(2.0 * preparation_count * povm_outcome_count / alpha_quantum)
    numerator = (
        8.0
        * lipschitz_constant**2
        * reconstruction_stability**2
        * povm_outcome_count**2
        * term
    )
    denominator = quantum_fraction**2 * population_gap**2
    return max(1, ceil(numerator / denominator))


def p42_sample_complexity_certificate(
    target_population_distance: float,
    quantum_population_distance: float,
    lipschitz_constant: float,
    preparation_count: int,
    target_outcome_count: int,
    povm_outcome_count: int,
    reconstruction_stability: float,
    alpha_target: float,
    alpha_quantum: float,
    *,
    target_budget_fraction: float = 0.5,
) -> P42SampleComplexityCertificate:
    """Construct the explicit P42 sufficient sample-size certificate.

    The population regularity gap is Delta = d_Y - L d_Q. If Delta <= 0, no
    finite sample size can force the P41 Lipschitz obstruction from this bound.
    Otherwise the gap is split between target and quantum uncertainty budgets.
    """
    _unit_interval(target_population_distance, "target_population_distance")
    _unit_interval(quantum_population_distance, "quantum_population_distance")
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    gap = target_population_distance - lipschitz_constant * quantum_population_distance
    _positive_gap(gap)
    _budget_fraction(target_budget_fraction)

    n_target = sufficient_target_sample_size(
        gap,
        preparation_count,
        target_outcome_count,
        alpha_target,
        target_budget_fraction=target_budget_fraction,
    )
    n_quantum = sufficient_quantum_sample_size(
        gap,
        lipschitz_constant,
        preparation_count,
        povm_outcome_count,
        reconstruction_stability,
        alpha_quantum,
        target_budget_fraction=target_budget_fraction,
    )
    epsilon = simultaneous_target_tv_radius(
        n_target,
        preparation_count,
        target_outcome_count,
        alpha_target,
    )
    radius = simultaneous_ic_povm_trace_radius(
        n_quantum,
        preparation_count,
        povm_outcome_count,
        reconstruction_stability,
        alpha_quantum,
    )
    budget = 4.0 * epsilon + 4.0 * lipschitz_constant * radius
    return P42SampleComplexityCertificate(
        population_gap=gap,
        target_sample_size=n_target,
        quantum_sample_size=n_quantum,
        target_radius=epsilon,
        quantum_radius=radius,
        uncertainty_budget=budget,
        certified_by_bound=budget <= gap,
    )


def _positive_int(value: int, name: str) -> None:
    if value < 1:
        raise ValueError(f"{name} must be positive")


def _alpha(value: float, name: str) -> None:
    if not 0.0 < value < 1.0:
        raise ValueError(f"{name} must lie in (0, 1)")


def _unit_interval(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")


def _positive_gap(value: float) -> None:
    if value <= 0.0:
        raise ValueError("population regularity gap must be positive")


def _budget_fraction(value: float) -> None:
    if not 0.0 < value < 1.0:
        raise ValueError("target_budget_fraction must lie in (0, 1)")
