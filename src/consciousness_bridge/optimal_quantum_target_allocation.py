"""Proposition 43: optimal quantum-target uncertainty allocation.

The module optimizes the P42 gap-allocation parameter for a declared weighted
sampling cost. It supplies a closed-form cube-root allocation law, integer sample
sizes, and a rounding overhead bound.

The result optimizes resources within the P42 experimental assumptions. It does
not establish physical completeness, quantum incompleteness, or consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log


@dataclass(frozen=True)
class OptimalQuantumTargetAllocation:
    """Closed-form P43 allocation and sufficient integer sample sizes."""

    target_gap_fraction: float
    quantum_gap_fraction: float
    target_samples_per_preparation: int
    quantum_samples_per_preparation: int
    continuous_weighted_cost: float
    integer_weighted_cost: float
    integer_rounding_overhead_bound: float
    balanced_to_optimal_continuous_cost_ratio: float


def p42_target_coefficient(
    *,
    preparation_count: int,
    target_outcomes: int,
    population_regularity_gap: float,
    alpha_target: float,
) -> float:
    """Return A_Y in n_Y >= A_Y / lambda^2."""
    _positive_integer(preparation_count, "preparation_count")
    _positive_integer(target_outcomes, "target_outcomes")
    _positive(population_regularity_gap, "population_regularity_gap")
    _alpha(alpha_target, "alpha_target")
    return (
        2.0
        * target_outcomes**2
        * log(2.0 * preparation_count * target_outcomes / alpha_target)
        / population_regularity_gap**2
    )


def p42_quantum_coefficient(
    *,
    preparation_count: int,
    measurement_outcomes: int,
    population_regularity_gap: float,
    lipschitz_constant: float,
    reconstruction_stability: float,
    alpha_quantum: float,
) -> float:
    """Return A_Q in n_Q >= A_Q / (1-lambda)^2."""
    _positive_integer(preparation_count, "preparation_count")
    _positive_integer(measurement_outcomes, "measurement_outcomes")
    _positive(population_regularity_gap, "population_regularity_gap")
    _positive(lipschitz_constant, "lipschitz_constant")
    _positive(reconstruction_stability, "reconstruction_stability")
    _alpha(alpha_quantum, "alpha_quantum")
    return (
        8.0
        * lipschitz_constant**2
        * reconstruction_stability**2
        * measurement_outcomes**2
        * log(2.0 * preparation_count * measurement_outcomes / alpha_quantum)
        / population_regularity_gap**2
    )


def optimal_gap_fraction(
    *,
    target_coefficient: float,
    quantum_coefficient: float,
    target_sample_cost: float = 1.0,
    quantum_sample_cost: float = 1.0,
) -> float:
    """Return the unique cost-minimizing P42 target gap fraction.

    For weighted cost

        C(lambda) = c_Y A_Y/lambda^2 + c_Q A_Q/(1-lambda)^2,

    the minimizer is

        lambda* = (c_Y A_Y)^(1/3)
                  / ((c_Y A_Y)^(1/3) + (c_Q A_Q)^(1/3)).
    """
    _positive(target_coefficient, "target_coefficient")
    _positive(quantum_coefficient, "quantum_coefficient")
    _positive(target_sample_cost, "target_sample_cost")
    _positive(quantum_sample_cost, "quantum_sample_cost")
    target_weighted = target_sample_cost * target_coefficient
    quantum_weighted = quantum_sample_cost * quantum_coefficient
    target_root = target_weighted ** (1.0 / 3.0)
    quantum_root = quantum_weighted ** (1.0 / 3.0)
    return target_root / (target_root + quantum_root)


def continuous_weighted_cost(
    *,
    target_coefficient: float,
    quantum_coefficient: float,
    target_gap_fraction: float,
    target_sample_cost: float = 1.0,
    quantum_sample_cost: float = 1.0,
) -> float:
    """Evaluate the continuous P42 weighted sample cost."""
    _positive(target_coefficient, "target_coefficient")
    _positive(quantum_coefficient, "quantum_coefficient")
    _positive(target_sample_cost, "target_sample_cost")
    _positive(quantum_sample_cost, "quantum_sample_cost")
    _open_unit_interval(target_gap_fraction, "target_gap_fraction")
    lam = target_gap_fraction
    return (
        target_sample_cost * target_coefficient / lam**2
        + quantum_sample_cost * quantum_coefficient / (1.0 - lam) ** 2
    )


def minimum_continuous_weighted_cost(
    *,
    target_coefficient: float,
    quantum_coefficient: float,
    target_sample_cost: float = 1.0,
    quantum_sample_cost: float = 1.0,
) -> float:
    """Return the exact minimum continuous weighted sample cost."""
    _positive(target_coefficient, "target_coefficient")
    _positive(quantum_coefficient, "quantum_coefficient")
    _positive(target_sample_cost, "target_sample_cost")
    _positive(quantum_sample_cost, "quantum_sample_cost")
    target_root = (target_sample_cost * target_coefficient) ** (1.0 / 3.0)
    quantum_root = (quantum_sample_cost * quantum_coefficient) ** (1.0 / 3.0)
    return (target_root + quantum_root) ** 3


def optimal_quantum_target_allocation(
    *,
    preparation_count: int,
    measurement_outcomes: int,
    target_outcomes: int,
    population_regularity_gap: float,
    lipschitz_constant: float,
    reconstruction_stability: float,
    alpha_quantum: float,
    alpha_target: float,
    target_sample_cost: float = 1.0,
    quantum_sample_cost: float = 1.0,
) -> OptimalQuantumTargetAllocation:
    """Return the P43 optimal continuous allocation and sufficient integers."""
    target_coefficient = p42_target_coefficient(
        preparation_count=preparation_count,
        target_outcomes=target_outcomes,
        population_regularity_gap=population_regularity_gap,
        alpha_target=alpha_target,
    )
    quantum_coefficient = p42_quantum_coefficient(
        preparation_count=preparation_count,
        measurement_outcomes=measurement_outcomes,
        population_regularity_gap=population_regularity_gap,
        lipschitz_constant=lipschitz_constant,
        reconstruction_stability=reconstruction_stability,
        alpha_quantum=alpha_quantum,
    )
    lam = optimal_gap_fraction(
        target_coefficient=target_coefficient,
        quantum_coefficient=quantum_coefficient,
        target_sample_cost=target_sample_cost,
        quantum_sample_cost=quantum_sample_cost,
    )
    target_continuous = target_coefficient / lam**2
    quantum_continuous = quantum_coefficient / (1.0 - lam) ** 2
    target_integer = ceil(target_continuous)
    quantum_integer = ceil(quantum_continuous)
    optimum = minimum_continuous_weighted_cost(
        target_coefficient=target_coefficient,
        quantum_coefficient=quantum_coefficient,
        target_sample_cost=target_sample_cost,
        quantum_sample_cost=quantum_sample_cost,
    )
    integer_cost = (
        target_sample_cost * target_integer
        + quantum_sample_cost * quantum_integer
    )
    balanced = continuous_weighted_cost(
        target_coefficient=target_coefficient,
        quantum_coefficient=quantum_coefficient,
        target_gap_fraction=0.5,
        target_sample_cost=target_sample_cost,
        quantum_sample_cost=quantum_sample_cost,
    )
    return OptimalQuantumTargetAllocation(
        target_gap_fraction=lam,
        quantum_gap_fraction=1.0 - lam,
        target_samples_per_preparation=target_integer,
        quantum_samples_per_preparation=quantum_integer,
        continuous_weighted_cost=optimum,
        integer_weighted_cost=integer_cost,
        integer_rounding_overhead_bound=target_sample_cost + quantum_sample_cost,
        balanced_to_optimal_continuous_cost_ratio=balanced / optimum,
    )


def _positive_integer(value: int, name: str) -> None:
    if value < 1:
        raise ValueError(f"{name} must be positive")


def _positive(value: float, name: str) -> None:
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _alpha(value: float, name: str) -> None:
    if not 0.0 < value < 1.0:
        raise ValueError(f"{name} must lie in (0, 1)")


def _open_unit_interval(value: float, name: str) -> None:
    if not 0.0 < value < 1.0:
        raise ValueError(f"{name} must lie in (0, 1)")
