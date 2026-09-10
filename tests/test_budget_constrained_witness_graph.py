from consciousness_bridge.budget_constrained_witness_graph import (
    exact_budgeted_witness_selection,
    fractional_degree_upper_bound,
    induced_edge_value,
    weighted_degrees,
)


def test_induced_edge_value_counts_only_fully_selected_edges():
    edges = {("a", "b"): 2.0, ("b", "c"): 3.0, ("a", "c"): 5.0}
    assert induced_edge_value(("a", "b"), edges) == 2.0
    assert induced_edge_value(("a", "b", "c"), edges) == 10.0


def test_weighted_degrees_match_edge_incidence():
    edges = {("a", "b"): 2.0, ("b", "c"): 3.0, ("a", "c"): 5.0}
    degree = weighted_degrees(("a", "b", "c"), edges)
    assert degree == {"a": 7.0, "b": 5.0, "c": 8.0}


def test_fractional_degree_relaxation_is_an_upper_bound():
    vertices = ("a", "b", "c", "d")
    costs = {vertex: 1.0 for vertex in vertices}
    edges = {
        ("a", "b"): 4.0,
        ("a", "c"): 2.0,
        ("b", "c"): 2.0,
        ("c", "d"): 1.0,
    }
    exact = exact_budgeted_witness_selection(vertices, costs, edges, budget=2.0)
    upper = fractional_degree_upper_bound(vertices, costs, edges, budget=2.0)
    assert exact.induced_edge_value == 4.0
    assert upper >= exact.induced_edge_value
    assert exact.degree_relaxation_upper_bound == upper


def test_exact_solver_uses_shared_vertex_structure():
    vertices = ("a", "b", "c", "d")
    costs = {vertex: 1.0 for vertex in vertices}
    edges = {
        ("a", "b"): 3.0,
        ("a", "c"): 3.0,
        ("b", "c"): 3.0,
        ("c", "d"): 7.0,
    }
    result = exact_budgeted_witness_selection(vertices, costs, edges, budget=3.0)
    assert set(result.selected_vertices) == {"a", "b", "c"}
    assert result.induced_edge_value == 9.0
    assert result.selected_cost == 3.0
    assert result.optimality_gap_upper_bound >= 0.0


def test_zero_budget_selects_nothing():
    result = exact_budgeted_witness_selection(
        ("a", "b"),
        {"a": 1.0, "b": 1.0},
        {("a", "b"): 1.0},
        budget=0.0,
    )
    assert result.selected_vertices == ()
    assert result.induced_edge_value == 0.0
    assert result.degree_relaxation_upper_bound == 0.0


def test_invalid_duplicate_undirected_edge_is_rejected():
    try:
        weighted_degrees(
            ("a", "b"),
            {("a", "b"): 1.0, ("b", "a"): 1.0},
        )
    except ValueError as exc:
        assert "undirected edge once" in str(exc)
    else:
        raise AssertionError("duplicate undirected edge should be rejected")


def test_exact_solver_has_vertex_guard():
    vertices = tuple(range(4))
    costs = {vertex: 1.0 for vertex in vertices}
    try:
        exact_budgeted_witness_selection(
            vertices,
            costs,
            {},
            budget=2.0,
            max_vertices=3,
        )
    except ValueError as exc:
        assert "max_vertices" in str(exc)
    else:
        raise AssertionError("large exact instance should be rejected")
