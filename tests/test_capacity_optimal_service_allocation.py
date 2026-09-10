from math import isclose, isinf

from consciousness_bridge.capacity_optimal_service_allocation import (
    capacity_feasible,
    completion_time,
    exact_quota_schedule,
    optimal_service_allocation,
    schedule_counts,
    threshold_saturation_lower_bound,
    vertex_threshold_demands,
)


def test_vertex_demands_are_maximum_incident_edge_thresholds():
    vertices = ("a", "b", "c", "d")
    edges = (("a", "b"), ("b", "c"), ("c", "d"))
    demands = vertex_threshold_demands(
        vertices,
        edges,
        {
            ("a", "b"): 5,
            ("b", "c"): 9,
            ("c", "d"): 4,
        },
    )
    assert demands == {"a": 5, "b": 9, "c": 9, "d": 4}


def test_isolated_vertex_has_zero_threshold_demand():
    demands = vertex_threshold_demands(
        ("a", "b", "isolated"),
        (("a", "b"),),
        {("a", "b"): 7},
    )
    assert demands["isolated"] == 0


def test_optimal_service_shares_are_proportional_to_demand():
    result = optimal_service_allocation({"a": 2.0, "b": 3.0, "c": 5.0})
    assert isclose(result.shares["a"], 0.2)
    assert isclose(result.shares["b"], 0.3)
    assert isclose(result.shares["c"], 0.5)
    assert isclose(result.completion_time, 10.0)
    assert capacity_feasible(result.shares)


def test_capacity_scales_optimal_completion_time_exactly():
    result = optimal_service_allocation(
        {"a": 2.0, "b": 6.0},
        capacity=2.0,
    )
    assert isclose(result.completion_time, 4.0)
    assert isclose(sum(result.shares.values()), 2.0)
    assert isclose(completion_time({"a": 2.0, "b": 6.0}, result.shares), 4.0)


def test_optimal_completion_matches_universal_lower_bound():
    demands = {"a": 4.0, "b": 1.0, "c": 7.0}
    optimum = optimal_service_allocation(demands)
    lower = threshold_saturation_lower_bound(demands)
    assert isclose(optimum.completion_time, lower)


def test_nonproportional_feasible_shares_cannot_beat_optimum():
    demands = {"a": 2.0, "b": 3.0, "c": 5.0}
    optimum = optimal_service_allocation(demands)
    candidate = {"a": 0.25, "b": 0.25, "c": 0.50}
    assert capacity_feasible(candidate)
    assert completion_time(demands, candidate) >= optimum.completion_time


def test_unserved_positive_demand_has_infinite_completion_time():
    assert isinf(
        completion_time(
            {"a": 1.0, "b": 2.0},
            {"a": 1.0, "b": 0.0},
        )
    )


def test_zero_demand_vertices_receive_zero_optimal_share():
    result = optimal_service_allocation({"a": 2.0, "b": 0.0})
    assert result.shares["a"] == 1.0
    assert result.shares["b"] == 0.0
    assert result.completion_time == 2.0


def test_all_zero_demands_have_zero_completion_time():
    result = optimal_service_allocation({"a": 0.0, "b": 0.0})
    assert result.completion_time == 0.0
    assert result.total_demand == 0.0
    assert result.shares == {"a": 0.0, "b": 0.0}


def test_exact_integer_quota_schedule_meets_demands_at_lower_bound_length():
    demands = {"a": 3, "b": 1, "c": 4}
    certificate = exact_quota_schedule(demands)
    assert certificate.length == 8
    assert certificate.optimal_length == 8
    assert certificate.is_optimal
    assert schedule_counts(certificate.schedule) == demands


def test_custom_quota_order_preserves_exact_optimality():
    certificate = exact_quota_schedule(
        {"a": 2, "b": 3},
        order=("b", "a"),
    )
    assert certificate.schedule[:2] == ("b", "a")
    assert schedule_counts(certificate.schedule) == {"a": 2, "b": 3}
    assert certificate.is_optimal


def test_invalid_duplicate_undirected_edges_are_rejected():
    try:
        vertex_threshold_demands(
            ("a", "b"),
            (("a", "b"), ("b", "a")),
            {("a", "b"): 2, ("b", "a"): 2},
        )
    except ValueError as exc:
        assert "undirected edge" in str(exc)
    else:
        raise AssertionError("duplicate undirected edge should be rejected")
