from math import isclose

from consciousness_bridge.sequential_witness_graph import (
    EdgeMarginInterval,
    allocate_error_budget,
    basel_alpha_spend,
    edge_margin_interval,
    prunable_vertices,
    sequential_witness_decision,
    simultaneous_edge_intervals,
)


def test_basel_alpha_spending_has_expected_partial_sum():
    alpha = 0.05
    partial = sum(basel_alpha_spend(n, alpha) for n in range(1, 20000))
    assert partial < alpha
    assert isclose(partial, alpha, rel_tol=0.0, abs_tol=2e-6)


def test_weighted_error_budget_uses_total_alpha_exactly():
    allocation = allocate_error_budget(
        ("a", "b", "c"),
        0.06,
        weights={"a": 1.0, "b": 2.0, "c": 3.0},
    )
    assert isclose(sum(allocation.values()), 0.06)
    assert allocation["b"] == 2.0 * allocation["a"]
    assert allocation["c"] == 3.0 * allocation["a"]


def test_edge_margin_interval_contains_compatible_population_margin():
    interval = edge_margin_interval(
        empirical_target_distance=0.62,
        empirical_quantum_distance=0.21,
        target_radius_first=0.03,
        target_radius_second=0.02,
        quantum_radius_first=0.01,
        quantum_radius_second=0.02,
        lipschitz_constant=1.5,
    )

    true_target_distance = 0.60
    true_quantum_distance = 0.20
    true_margin = true_target_distance - 1.5 * true_quantum_distance
    assert interval.lower <= true_margin <= interval.upper


def test_simultaneous_intervals_use_shared_vertex_radii():
    edges = (("a", "b"), ("a", "c"))
    intervals = simultaneous_edge_intervals(
        edges,
        empirical_target_distances={
            ("a", "b"): 0.7,
            ("a", "c"): 0.4,
        },
        empirical_quantum_distances={
            ("a", "b"): 0.2,
            ("a", "c"): 0.2,
        },
        target_radii={"a": 0.02, "b": 0.03, "c": 0.05},
        quantum_radii={"a": 0.01, "b": 0.02, "c": 0.04},
        lipschitz_constants={
            ("a", "b"): 1.0,
            ("a", "c"): 1.0,
        },
    )
    assert intervals[("a", "b")].lower > intervals[("a", "c")].lower


def test_positive_lower_bound_triggers_anytime_valid_stop_decision():
    intervals = {
        ("a", "b"): EdgeMarginInterval(lower=-0.03, upper=0.10),
        ("b", "c"): EdgeMarginInterval(lower=0.04, upper=0.16),
    }
    decision = sequential_witness_decision(intervals)
    assert decision.status == "certified-positive"
    assert decision.selected_edge == ("b", "c")
    assert decision.selected_interval == intervals[("b", "c")]


def test_all_negative_upper_bounds_certify_no_positive_edge():
    intervals = {
        ("a", "b"): EdgeMarginInterval(lower=-0.30, upper=-0.02),
        ("b", "c"): EdgeMarginInterval(lower=-0.20, upper=-0.01),
    }
    decision = sequential_witness_decision(intervals)
    assert decision.status == "certified-no-positive-edge"


def test_unresolved_family_does_not_overclaim():
    intervals = {
        ("a", "b"): EdgeMarginInterval(lower=-0.02, upper=0.08),
        ("b", "c"): EdgeMarginInterval(lower=-0.04, upper=0.02),
    }
    decision = sequential_witness_decision(intervals)
    assert decision.status == "unresolved"


def test_vertex_pruning_requires_all_incident_edges_negative():
    vertices = ("a", "b", "c", "d")
    edges = (("a", "b"), ("b", "c"), ("c", "d"))
    intervals = {
        ("a", "b"): EdgeMarginInterval(lower=-0.2, upper=-0.1),
        ("b", "c"): EdgeMarginInterval(lower=-0.1, upper=0.05),
        ("c", "d"): EdgeMarginInterval(lower=-0.3, upper=-0.02),
    }
    assert prunable_vertices(vertices, edges, intervals) == ("a", "d")


def test_duplicate_undirected_edges_are_rejected():
    try:
        simultaneous_edge_intervals(
            (("a", "b"), ("b", "a")),
            empirical_target_distances={
                ("a", "b"): 0.2,
                ("b", "a"): 0.2,
            },
            empirical_quantum_distances={
                ("a", "b"): 0.1,
                ("b", "a"): 0.1,
            },
            target_radii={"a": 0.01, "b": 0.01},
            quantum_radii={"a": 0.01, "b": 0.01},
            lipschitz_constants={
                ("a", "b"): 1.0,
                ("b", "a"): 1.0,
            },
        )
    except ValueError as exc:
        assert "undirected edge" in str(exc)
    else:
        raise AssertionError("duplicate undirected edge should be rejected")
