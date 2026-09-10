"""Proposition 69: certified optimization of the P68 Lagrangian dual.

P68 gives a valid lower bound on the unrestricted P63 integer optimum for every
positive Lagrange multiplier. P69 optimizes that one-dimensional dual family
without turning dual optimality into a claim of primal exactness.

The dual is concave. At a multiplier, each edge has one or two exact minimizing
integer counts. Their minimum and maximum total spends define the full
supergradient interval. A zero-containing interval certifies a global dual
maximizer. Otherwise the interval sign directs a monotone bracket search.
Supporting-line bounds then certify how close the best evaluated dual value is
to the strongest possible P68 lower bound.

This module concerns a declared experimental resource-allocation surrogate. It
makes no experiential or quantum-ontological claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import isfinite
from typing import TypeVar

from consciousness_bridge.lagrangian_optimality_gap import (
    EdgeLagrangianMinimum,
    lagrangian_dual_lower_bound,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class DualEvaluation:
    """Exact P68 dual value and supergradient interval at one multiplier."""

    lambda_value: float
    dual_value: float
    minimum_spend: int
    maximum_spend: int
    supergradient_lower: int
    supergradient_upper: int
    edge_minima: dict[Hashable, EdgeLagrangianMinimum]


@dataclass(frozen=True)
class DualOptimalMultiplierCertificate:
    """Certified approximation to the strongest P68 Lagrangian lower bound."""

    lambda_value: float
    dual_lower_bound: float
    dual_optimum_upper_bound: float
    dual_value_error_bound: float
    exact_dual_maximizer: bool
    lambda_lower: float
    lambda_upper: float
    iterations: int
    evaluation: DualEvaluation
    baseline_budget_case: bool


def evaluate_dual_with_supergradient(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    lambda_value: float,
) -> DualEvaluation:
    """Evaluate q(lambda) and its full one-dimensional supergradient interval.

    If M_e(lambda) is the set of exact minimizing counts for edge e, then the
    concave dual superdifferential is

        [sum_e c_e min M_e - B, sum_e c_e max M_e - B].

    The interval is exact because the edge minimizers combine independently.
    """
    dual_value, minima = lagrangian_dual_lower_bound(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        lambda_value,
    )
    minimum_spend = sum(
        unit_costs[edge] * min(minimum.minimizing_counts)
        for edge, minimum in minima.items()
    )
    maximum_spend = sum(
        unit_costs[edge] * max(minimum.minimizing_counts)
        for edge, minimum in minima.items()
    )
    return DualEvaluation(
        lambda_value=lambda_value,
        dual_value=dual_value,
        minimum_spend=minimum_spend,
        maximum_spend=maximum_spend,
        supergradient_lower=minimum_spend - total_budget,
        supergradient_upper=maximum_spend - total_budget,
        edge_minima=dict(minima),
    )


def certified_dual_optimal_multiplier(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    *,
    dual_tolerance: float = 1e-10,
    max_iterations: int = 200,
) -> DualOptimalMultiplierCertificate:
    """Certify the strongest P68 dual value to a declared additive tolerance.

    The search first brackets a dual maximizer using the sign of the exact
    supergradient interval. It then bisects that bracket. If zero enters a
    supergradient interval, the corresponding multiplier is an exact global
    dual maximizer. Otherwise concave supporting lines at the two bracket
    endpoints provide a rigorous upper bound on the unknown dual optimum.

    The routine stops only when the supporting-line upper bound minus the best
    evaluated dual value is at most ``dual_tolerance``. This certifies dual
    value quality; it does not claim zero primal-dual gap.
    """
    _validate_search_parameters(dual_tolerance, max_iterations)

    # This first evaluation delegates all problem validation to P68 before the
    # P69 search inspects the baseline or any mapping values.
    initial = evaluate_dual_with_supergradient(
        coefficients, sensitivities, unit_costs, total_budget, 1.0
    )
    baseline = sum(unit_costs.values())
    if total_budget == baseline:
        return _baseline_certificate(
            coefficients,
            sensitivities,
            unit_costs,
            total_budget,
        )

    left = initial

    # Find a point with strictly positive supergradient interval to the left.
    while left.supergradient_lower <= 0:
        if left.supergradient_lower <= 0 <= left.supergradient_upper:
            return _exact_certificate(left, baseline_budget_case=False)
        next_lambda = left.lambda_value / 2.0
        if next_lambda == 0.0:
            raise RuntimeError("failed to bracket dual maximizer away from zero")
        left = evaluate_dual_with_supergradient(
            coefficients, sensitivities, unit_costs, total_budget, next_lambda
        )

    # Find a point with strictly negative supergradient interval to the right.
    right = initial
    while right.supergradient_upper >= 0:
        if right.supergradient_lower <= 0 <= right.supergradient_upper:
            return _exact_certificate(right, baseline_budget_case=False)
        next_lambda = right.lambda_value * 2.0
        if not isfinite(next_lambda):
            raise RuntimeError("failed to bracket dual maximizer at finite lambda")
        right = evaluate_dual_with_supergradient(
            coefficients, sensitivities, unit_costs, total_budget, next_lambda
        )

    if left.lambda_value >= right.lambda_value:
        raise RuntimeError("invalid dual search bracket")

    best = left if left.dual_value >= right.dual_value else right
    for iteration in range(1, max_iterations + 1):
        upper = _supporting_line_upper_bound(left, right)
        error = max(0.0, upper - best.dual_value)
        if error <= dual_tolerance:
            return _certificate_from_bracket(
                best,
                left,
                right,
                upper,
                error,
                iteration - 1,
            )

        midpoint_lambda = 0.5 * (left.lambda_value + right.lambda_value)
        if midpoint_lambda in {left.lambda_value, right.lambda_value}:
            raise RuntimeError(
                "floating-point bracket stalled before dual-value tolerance; "
                f"remaining certified error is {error}"
            )
        midpoint = evaluate_dual_with_supergradient(
            coefficients,
            sensitivities,
            unit_costs,
            total_budget,
            midpoint_lambda,
        )
        if midpoint.dual_value > best.dual_value:
            best = midpoint
        if midpoint.supergradient_lower <= 0 <= midpoint.supergradient_upper:
            return _exact_certificate(midpoint, baseline_budget_case=False, iterations=iteration)
        if midpoint.supergradient_lower > 0:
            left = midpoint
        elif midpoint.supergradient_upper < 0:
            right = midpoint
        else:
            raise RuntimeError("inconsistent P69 supergradient interval")

    upper = _supporting_line_upper_bound(left, right)
    error = max(0.0, upper - best.dual_value)
    if error > dual_tolerance:
        raise RuntimeError(
            "dual-value tolerance not reached within max_iterations; "
            f"remaining certified error is {error}"
        )
    return _certificate_from_bracket(
        best,
        left,
        right,
        upper,
        error,
        max_iterations,
    )


def _supporting_line_upper_bound(left: DualEvaluation, right: DualEvaluation) -> float:
    """Upper-bound the concave maximum inside a sign-changing bracket."""
    g_left = left.supergradient_lower
    g_right = right.supergradient_upper
    if g_left <= 0 or g_right >= 0:
        raise ValueError("supporting-line bracket must have positive/negative signs")

    # For concave q, every supergradient gives a global affine upper support.
    # The maximum of the minimum of the increasing left support and decreasing
    # right support occurs at their intersection, clipped to the bracket.
    numerator = (
        right.dual_value
        - g_right * right.lambda_value
        - left.dual_value
        + g_left * left.lambda_value
    )
    denominator = g_left - g_right
    crossing = numerator / denominator
    crossing = min(right.lambda_value, max(left.lambda_value, crossing))
    left_support = left.dual_value + g_left * (crossing - left.lambda_value)
    right_support = right.dual_value + g_right * (crossing - right.lambda_value)
    return min(left_support, right_support)


def _baseline_certificate(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
) -> DualOptimalMultiplierCertificate:
    # Once lambda exceeds every first marginal reduction per cost, count one is
    # an edgewise minimizer. With B equal to baseline spend, q then equals the
    # only feasible primal objective exactly.
    from consciousness_bridge.global_integer_optimality_certificate import (
        marginal_reduction,
    )

    threshold = max(
        marginal_reduction(coefficients[e] * sensitivities[e], 1) / unit_costs[e]
        for e in coefficients
    )
    lambda_value = max(1.0, threshold * 2.0)
    evaluation = evaluate_dual_with_supergradient(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        lambda_value,
    )
    if evaluation.supergradient_lower > 0 or evaluation.supergradient_upper < 0:
        raise RuntimeError("baseline multiplier did not produce zero-containing slope")
    return _exact_certificate(evaluation, baseline_budget_case=True)


def _exact_certificate(
    evaluation: DualEvaluation,
    *,
    baseline_budget_case: bool,
    iterations: int = 0,
) -> DualOptimalMultiplierCertificate:
    return DualOptimalMultiplierCertificate(
        lambda_value=evaluation.lambda_value,
        dual_lower_bound=evaluation.dual_value,
        dual_optimum_upper_bound=evaluation.dual_value,
        dual_value_error_bound=0.0,
        exact_dual_maximizer=True,
        lambda_lower=evaluation.lambda_value,
        lambda_upper=evaluation.lambda_value,
        iterations=iterations,
        evaluation=evaluation,
        baseline_budget_case=baseline_budget_case,
    )


def _certificate_from_bracket(
    best: DualEvaluation,
    left: DualEvaluation,
    right: DualEvaluation,
    upper: float,
    error: float,
    iterations: int,
) -> DualOptimalMultiplierCertificate:
    return DualOptimalMultiplierCertificate(
        lambda_value=best.lambda_value,
        dual_lower_bound=best.dual_value,
        dual_optimum_upper_bound=max(upper, best.dual_value),
        dual_value_error_bound=error,
        exact_dual_maximizer=False,
        lambda_lower=left.lambda_value,
        lambda_upper=right.lambda_value,
        iterations=iterations,
        evaluation=best,
        baseline_budget_case=False,
    )


def _validate_search_parameters(dual_tolerance: float, max_iterations: int) -> None:
    if not isfinite(dual_tolerance) or dual_tolerance <= 0.0:
        raise ValueError("dual_tolerance must be positive and finite")
    if not isinstance(max_iterations, int) or isinstance(max_iterations, bool):
        raise TypeError("max_iterations must be an integer")
    if max_iterations < 1:
        raise ValueError("max_iterations must be positive")
