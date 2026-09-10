"""Proposition 42: sample complexity for the P41 regularity obstruction.

This module solves the P41 symmetric uncertainty inequality under declared
square-root confidence-radius laws. The concentration constants are inputs. They
must come from a separately justified tomography and target-estimation analysis.

Nothing in this module supplies a universal quantum tomography rate, establishes
quantum incompleteness, or identifies any target with consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log, sqrt


@dataclass(frozen=True)
class SampleComplexityCertificate:
    """Sufficient sample sizes for a positive P41 Lipschitz obstruction margin."""

    population_regularity_gap: float
    allocation_fraction_target: float
    minimum_target_samples: int
    minimum_quantum_samples: int
    target_radius_at_minimum: float
    quantum_radius_at_minimum: float
    uncertainty_budget_at_minimum: float
    certified_by_bound: bool


@dataclass(frozen=True)
class OptimalAllocation:
    """Continuous allocation minimizing a declared weighted sample objective."""

    allocation_fraction_target: float
    target_weighted_term: float
    quantum_weighted_term: float


def square_root_radius(
    sample_count: int,
    alpha: float,
    constant: float,
    log_factor: float,
) -> float:
    """Return c sqrt(log(A/alpha)/n) for declared c and A.

    ``log_factor`` is the declared positive factor A. This function does not claim
    that any particular choice of c or A is valid for a tomography protocol.
    """
    if sample_count < 1:
        raise ValueError("sample_count must be positive")
    _validate_alpha(alpha)
    if constant < 0.0:
        raise ValueError("constant must be nonnegative")
    if log_factor <= alpha:
        raise ValueError("log_factor must exceed alpha so log(A/alpha) is positive")
    return constant * sqrt(log(log_factor / alpha) / sample_count)


def population_regularity_gap(
    target_distance: float,
    quantum_trace_distance: float,
    lipschitz_constant: float,
) -> float:
    """Return Gamma = d_Y - L d_Q."""
    _unit_interval(target_distance, "target_distance")
    _unit_interval(quantum_trace_distance, "quantum_trace_distance")
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    return target_distance - lipschitz_constant * quantum_trace_distance


def sufficient_sample_complexity(
    target_distance: float,
    quantum_trace_distance: float,
    lipschitz_constant: float,
    *,
    target_radius_constant: float,
    quantum_radius_constant: float,
    target_log_factor: float,
    quantum_log_factor: float,
    alpha_target: float,
    alpha_quantum: float,
    allocation_fraction_target: float = 0.5,
) -> SampleComplexityCertificate:
    """Solve a sufficient P41 sample-size condition.

    Let Gamma = d_Y - L d_Q. Under declared simultaneous radius laws

        epsilon_Y(n) = c_Y sqrt(log(A_Y/alpha_Y)/n)
        r_Q(n)       = c_Q sqrt(log(A_Q/alpha_Q)/n),

    P41 is guaranteed when

        2 epsilon_Y + 2 L r_Q < Gamma.

    We allocate a fraction lambda of the population gap to target uncertainty and
    the remainder to quantum uncertainty. The returned integer counts enforce the
    non-strict component inequalities

        2 epsilon_Y <= lambda Gamma,
        2 L r_Q <= (1-lambda) Gamma.

    To provide a strict final P41 obstruction in an implementation, an experiment
    should verify the observed P41 margin is positive rather than rely on equality
    at a planning boundary.
    """
    gap = population_regularity_gap(
        target_distance, quantum_trace_distance, lipschitz_constant
    )
    if gap <= 0.0:
        raise ValueError("population regularity gap must be positive")
    if not 0.0 < allocation_fraction_target < 1.0:
        raise ValueError("allocation_fraction_target must lie in (0, 1)")
    _validate_alpha(alpha_target)
    _validate_alpha(alpha_quantum)
    if target_radius_constant < 0.0 or quantum_radius_constant < 0.0:
        raise ValueError("radius constants must be nonnegative")
    if target_log_factor <= alpha_target or quantum_log_factor <= alpha_quantum:
        raise ValueError("each log factor must exceed its alpha")

    lam = allocation_fraction_target
    target_n_real = (
        4.0
        * target_radius_constant**2
        * log(target_log_factor / alpha_target)
        / (lam**2 * gap**2)
    )
    quantum_n_real = (
        4.0
        * lipschitz_constant**2
        * quantum_radius_constant**2
        * log(quantum_log_factor / alpha_quantum)
        / ((1.0 - lam) ** 2 * gap**2)
    )

    target_n = max(1, ceil(target_n_real))
    quantum_n = max(1, ceil(quantum_n_real))
    target_radius = square_root_radius(
        target_n,
        alpha_target,
        target_radius_constant,
        target_log_factor,
    )
    quantum_radius = square_root_radius(
        quantum_n,
        alpha_quantum,
        quantum_radius_constant,
        quantum_log_factor,
    )
    budget = 2.0 * target_radius + 2.0 * lipschitz_constant * quantum_radius

    return SampleComplexityCertificate(
        population_regularity_gap=gap,
        allocation_fraction_target=lam,
        minimum_target_samples=target_n,
        minimum_quantum_samples=quantum_n,
        target_radius_at_minimum=target_radius,
        quantum_radius_at_minimum=quantum_radius,
        uncertainty_budget_at_minimum=budget,
        certified_by_bound=budget <= gap + 1e-12,
    )


def optimal_continuous_allocation(
    *,
    lipschitz_constant: float,
    target_radius_constant: float,
    quantum_radius_constant: float,
    target_log_factor: float,
    quantum_log_factor: float,
    alpha_target: float,
    alpha_quantum: float,
    target_sample_cost: float = 1.0,
    quantum_sample_cost: float = 1.0,
) -> OptimalAllocation:
    """Minimize the continuous weighted sufficient-sample objective over lambda.

    Ignoring integer ceilings and the common positive factor 4/Gamma^2, the
    weighted objective has form

        a/lambda^2 + b/(1-lambda)^2.

    Its unique interior minimizer is

        lambda* = a^(1/3) / (a^(1/3) + b^(1/3)).
    """
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    if target_radius_constant <= 0.0 or quantum_radius_constant <= 0.0:
        raise ValueError("radius constants must be positive for allocation optimization")
    if target_sample_cost <= 0.0 or quantum_sample_cost <= 0.0:
        raise ValueError("sample costs must be positive")
    _validate_alpha(alpha_target)
    _validate_alpha(alpha_quantum)
    if target_log_factor <= alpha_target or quantum_log_factor <= alpha_quantum:
        raise ValueError("each log factor must exceed its alpha")

    a = (
        target_sample_cost
        * target_radius_constant**2
        * log(target_log_factor / alpha_target)
    )
    b = (
        quantum_sample_cost
        * lipschitz_constant**2
        * quantum_radius_constant**2
        * log(quantum_log_factor / alpha_quantum)
    )
    if b == 0.0:
        return OptimalAllocation(
            allocation_fraction_target=1.0,
            target_weighted_term=a,
            quantum_weighted_term=b,
        )

    a13 = a ** (1.0 / 3.0)
    b13 = b ** (1.0 / 3.0)
    lam = a13 / (a13 + b13)
    return OptimalAllocation(
        allocation_fraction_target=lam,
        target_weighted_term=a,
        quantum_weighted_term=b,
    )


def _validate_alpha(alpha: float) -> None:
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie in (0, 1)")


def _unit_interval(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")
