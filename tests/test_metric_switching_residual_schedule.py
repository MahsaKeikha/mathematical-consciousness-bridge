from itertools import permutations
from math import isclose

from consciousness_bridge.metric_switching_residual_schedule import (
    batching_certificate,
    block_expanded_schedule,
    expanded_schedule_cost,
    first_visit_order,
    shortest_block_schedule,
    switching_path_cost,
    validate_metric_costs,
)


def _line_metric(points):
    coordinates = {point: index for index, point in enumerate(points)}
    return {
        (u, v): float(abs(coordinates[u] - coordinates[v]))
        for u in points
        for v in points
    }


def test_metric_validation_accepts_line_metric():
    points = ("s", "a", "b", "c")
    validate_metric_costs(points, _line_metric(points))


def test_metric_validation_rejects_triangle_violation():
    points = ("a", "b", "c")
    costs = {
        ("a", "a"): 0.0,
        ("b", "b"): 0.0,
        ("c", "c"): 0.0,
        ("a", "b"): 1.0,
        ("b", "a"): 1.0,
        ("b", "c"): 1.0,
        ("c", "b"): 1.0,
        ("a", "c"): 3.0,
        ("c", "a"): 3.0,
    }
    try:
        validate_metric_costs(points, costs)
    except ValueError as exc:
        assert "triangle" in str(exc)
    else:
        raise AssertionError("triangle inequality violation should be rejected")


def test_first_visit_batching_never_increases_metric_switching_cost():
    points = ("s", "a", "b", "c")
    costs = _line_metric(points)
    schedule = ("a", "b", "a", "c", "b", "c")
    certificate = batching_certificate(schedule, costs, start="s")
    assert certificate.batched_order == ("a", "b", "c")
    assert certificate.switching_nonincreasing
    assert certificate.batched_switching_cost <= certificate.original_switching_cost


def test_shortest_block_schedule_matches_bruteforce_small_instance():
    points = ("s", "a", "b", "c")
    coordinates = {"s": 0.0, "a": 2.0, "b": 5.0, "c": 3.0}
    costs = {
        (u, v): abs(coordinates[u] - coordinates[v])
        for u in points
        for v in points
    }
    demands = {"a": 2, "b": 1, "c": 3}
    result = shortest_block_schedule(demands, costs, start="s")

    brute = min(
        switching_path_cost(order, costs, start="s")
        for order in permutations(demands)
    )
    assert isclose(result.switching_cost, brute)
    assert isclose(result.acquisition_cost, 6.0)
    assert isclose(result.total_cost, 6.0 + brute)


def test_demands_change_acquisition_cost_but_not_optimal_switch_order_objective():
    points = ("s", "a", "b", "c")
    costs = _line_metric(points)
    first = shortest_block_schedule({"a": 1, "b": 1, "c": 1}, costs, start="s")
    second = shortest_block_schedule({"a": 10, "b": 2, "c": 7}, costs, start="s")
    assert first.order == second.order
    assert first.switching_cost == second.switching_cost
    assert first.acquisition_cost == 3.0
    assert second.acquisition_cost == 19.0


def test_block_expansion_meets_exact_residual_demands():
    demands = {"a": 3, "b": 1, "c": 2}
    expanded = block_expanded_schedule(("b", "a", "c"), demands)
    assert expanded == ("b", "a", "a", "a", "c", "c")
    assert first_visit_order(expanded) == ("b", "a", "c")


def test_single_required_vertex_costs_only_start_transition_plus_acquisition():
    costs = {("s", "s"): 0.0, ("a", "a"): 0.0, ("s", "a"): 4.0, ("a", "s"): 4.0}
    result = shortest_block_schedule({"a": 5}, costs, start="s", sample_cost=2.0)
    assert result.order == ("a",)
    assert result.acquisition_cost == 10.0
    assert result.switching_cost == 4.0
    assert result.total_cost == 14.0


def test_zero_demand_vertices_are_not_visited():
    points = ("s", "a", "b")
    costs = _line_metric(points)
    result = shortest_block_schedule({"a": 3, "b": 0}, costs, start="s")
    assert result.order == ("a",)


def test_all_zero_demands_need_no_schedule():
    # No switching-cost map is needed because no preparation must be visited.
    result = shortest_block_schedule({"a": 0, "b": 0}, {}, start="s")
    assert result.order == ()
    assert result.total_cost == 0.0


def test_expanded_switching_cost_counts_revisits():
    points = ("s", "a", "b")
    costs = _line_metric(points)
    schedule = ("a", "b", "a")
    assert expanded_schedule_cost(schedule, costs, start="s") == 3.0


def test_incomplete_metric_is_rejected():
    try:
        shortest_block_schedule(
            {"a": 1, "b": 1},
            {("a", "a"): 0.0, ("b", "b"): 0.0},
        )
    except ValueError as exc:
        assert "every ordered pair" in str(exc)
    else:
        raise AssertionError("incomplete metric should be rejected")
