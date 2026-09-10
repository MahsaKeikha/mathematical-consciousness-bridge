from math import isclose, log, sqrt

from consciousness_bridge.finite_data_metric_uncertainty import (
    allocate_pair_error,
    canonical_pairs,
    hoeffding_pair_radius,
    pairwise_hoeffding_radii,
    robust_improvement_certificate,
    robust_optimal_switching_certificate,
)
from consciousness_bridge.metric_switching_residual_schedule import (
    shortest_block_schedule,
    switching_path_cost,
)


def line_metric(coordinates):
    return {
        (first, second): abs(coordinates[first] - coordinates[second])
        for first in coordinates
        for second in coordinates
    }


def symmetric_radii(points, radius):
    return {
        (first, second): 0.0 if first == second else radius
        for first in points
        for second in points
    }


def test_hoeffding_pair_radius_matches_two_sided_formula():
    radius = hoeffding_pair_radius(200, 3.0, 0.01)
    expected = 3.0 * sqrt(log(200.0) / 400.0)
    assert isclose(radius, expected)


def test_pair_error_allocation_uses_total_budget():
    points = ("s", "a", "b", "c")
    pairs = canonical_pairs(points)
    allocation = allocate_pair_error(points, 0.06)
    assert set(allocation) == set(pairs)
    assert isclose(sum(allocation.values()), 0.06)


def test_pairwise_radii_are_symmetric_and_zero_on_diagonal():
    points = ("s", "a", "b")
    pairs = canonical_pairs(points)
    radii = pairwise_hoeffding_radii(
        points,
        {pair: 100 for pair in pairs},
        {pair: 2.0 for pair in pairs},
        0.05,
    )
    for point in points:
        assert radii[(point, point)] == 0.0
    for first, second in pairs:
        assert radii[(first, second)] == radii[(second, first)]
        assert radii[(first, second)] > 0.0


def test_robust_interval_contains_unknown_true_metric_optimum():
    points = ("s", "a", "b", "c")
    true_costs = line_metric({"s": 0.0, "a": 1.0, "b": 3.0, "c": 5.0})
    estimates = {
        edge: value + (0.08 if edge[0] != edge[1] else 0.0)
        for edge, value in true_costs.items()
    }
    radii = symmetric_radii(points, 0.1)
    demands = {"a": 2, "b": 1, "c": 3}

    robust = robust_optimal_switching_certificate(
        demands,
        estimates,
        radii,
        start="s",
        sample_cost=2.0,
    )
    true = shortest_block_schedule(
        demands,
        true_costs,
        start="s",
        sample_cost=2.0,
    )
    assert robust.lower_total_cost <= true.total_cost <= robust.upper_total_cost


def test_robust_route_regret_bound_controls_true_route_regret():
    points = ("s", "a", "b", "c")
    true_costs = line_metric({"s": 0.0, "a": 1.0, "b": 4.0, "c": 6.0})
    estimates = dict(true_costs)
    estimates[("a", "c")] = estimates[("c", "a")] = 4.8
    estimates[("a", "b")] = estimates[("b", "a")] = 3.2
    radii = symmetric_radii(points, 0.5)
    demands = {"a": 1, "b": 1, "c": 1}

    robust = robust_optimal_switching_certificate(
        demands,
        estimates,
        radii,
        start="s",
    )
    true = shortest_block_schedule(demands, true_costs, start="s")
    robust_route_true_cost = switching_path_cost(
        robust.robust_order,
        true_costs,
        start="s",
    )
    regret = robust_route_true_cost - true.switching_cost
    assert regret <= robust.robust_route_regret_upper_bound + 1e-12


def test_empirical_center_need_not_be_a_metric():
    points = ("s", "a", "b")
    estimates = {
        ("s", "s"): 0.0,
        ("a", "a"): 0.0,
        ("b", "b"): 0.0,
        ("s", "a"): 1.0,
        ("a", "s"): 1.0,
        ("a", "b"): 1.0,
        ("b", "a"): 1.0,
        ("s", "b"): 3.0,
        ("b", "s"): 3.0,
    }
    radii = symmetric_radii(points, 1.0)
    certificate = robust_optimal_switching_certificate(
        {"a": 1, "b": 1},
        estimates,
        radii,
        start="s",
    )
    assert certificate.lower_switching_cost <= certificate.upper_switching_cost


def test_zero_radii_recover_exact_metric_optimum():
    points = ("s", "a", "b", "c")
    costs = line_metric({"s": 0.0, "a": 2.0, "b": 3.0, "c": 7.0})
    radii = symmetric_radii(points, 0.0)
    demands = {"a": 2, "b": 2, "c": 1}
    robust = robust_optimal_switching_certificate(
        demands,
        costs,
        radii,
        start="s",
        sample_cost=1.5,
    )
    exact = shortest_block_schedule(
        demands,
        costs,
        start="s",
        sample_cost=1.5,
    )
    assert isclose(robust.lower_total_cost, exact.total_cost)
    assert isclose(robust.upper_total_cost, exact.total_cost)
    assert robust.robust_route_regret_upper_bound == 0.0


def test_two_state_intervals_can_certify_strict_improvement():
    points = ("s", "a", "b")
    costs = line_metric({"s": 0.0, "a": 1.0, "b": 3.0})
    radii = symmetric_radii(points, 0.05)
    old = robust_optimal_switching_certificate(
        {"a": 5, "b": 5},
        costs,
        radii,
        start="s",
        sample_cost=2.0,
    )
    new = robust_optimal_switching_certificate(
        {"a": 1, "b": 1},
        costs,
        radii,
        start="s",
        sample_cost=2.0,
    )
    comparison = robust_improvement_certificate(old, new)
    assert comparison.strict_improvement_certified
    assert comparison.guaranteed_release > 0.0


def test_empty_residual_support_has_exact_zero_cost_interval():
    certificate = robust_optimal_switching_certificate(
        {"a": 0, "b": 0},
        {},
        {},
        start="s",
    )
    assert certificate.lower_total_cost == 0.0
    assert certificate.upper_total_cost == 0.0
    assert certificate.robust_order == ()
