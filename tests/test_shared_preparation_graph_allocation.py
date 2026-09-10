import math

import pytest

from consciousness_bridge.shared_preparation_graph_allocation import (
    GraphEdge,
    edge_uncertainty_budget,
    graph_feasibility,
    kkt_certificate_holds,
    kkt_stationarity_residuals,
    single_edge_optimal_allocation,
    weighted_sampling_cost,
)


def test_nonuniform_edge_budget_reduces_to_p42_uniform_factor_four():
    edge = GraphEdge("a", "b", population_gap=0.5, lipschitz_constant=1.5)
    result = edge_uncertainty_budget(
        edge,
        {"a": 0.02, "b": 0.02},
        {"a": 0.03, "b": 0.03},
    )
    expected_cost = 4.0 * 0.02 + 4.0 * 1.5 * 0.03
    assert result.uncertainty_cost == pytest.approx(expected_cost)
    assert result.slack == pytest.approx(0.5 - expected_cost)
    assert result.feasible


def test_edge_budget_detects_insufficient_precision():
    edge = GraphEdge("a", "b", population_gap=0.1, lipschitz_constant=1.0)
    result = edge_uncertainty_budget(
        edge,
        {"a": 0.03, "b": 0.03},
        {"a": 0.03, "b": 0.03},
    )
    assert result.slack < 0.0
    assert not result.feasible


def test_shared_vertex_allocation_controls_multiple_incident_edges():
    edges = (
        GraphEdge("a", "b", 0.4, 1.0),
        GraphEdge("a", "c", 0.5, 2.0),
    )
    budgets = graph_feasibility(
        edges,
        {"a": 0.02, "b": 0.03, "c": 0.01},
        {"a": 0.02, "b": 0.02, "c": 0.03},
    )
    assert budgets[("a", "b")].feasible
    assert budgets[("a", "c")].feasible
    assert budgets[("a", "c")].uncertainty_cost == pytest.approx(
        2 * (0.02 + 0.01) + 4 * (0.02 + 0.03)
    )


def test_weighted_sampling_cost_matches_inverse_square_model():
    cost = weighted_sampling_cost(
        {"a": 0.2, "b": 0.25},
        {"a": 0.1, "b": 0.2},
        {"a": 2.0, "b": 1.0},
        {"a": 3.0, "b": 4.0},
    )
    expected = 2 / 0.2**2 + 1 / 0.25**2 + 3 / 0.1**2 + 4 / 0.2**2
    assert cost == pytest.approx(expected)


def test_single_edge_closed_form_exhausts_budget():
    edge = GraphEdge("a", "b", population_gap=0.6, lipschitz_constant=1.25)
    allocation = single_edge_optimal_allocation(edge, 1.0, 2.0, 3.0, 4.0)
    consumed = 2 * (
        allocation.first_target_radius + allocation.second_target_radius
    ) + 2 * edge.lipschitz_constant * (
        allocation.first_quantum_radius + allocation.second_quantum_radius
    )
    assert consumed == pytest.approx(edge.population_gap)


def test_single_edge_closed_form_matches_cost_formula():
    edge = GraphEdge("a", "b", population_gap=0.7, lipschitz_constant=1.4)
    weights = (1.2, 0.8, 2.1, 1.7)
    allocation = single_edge_optimal_allocation(edge, *weights)
    direct = (
        weights[0] / allocation.first_target_radius**2
        + weights[1] / allocation.second_target_radius**2
        + weights[2] / allocation.first_quantum_radius**2
        + weights[3] / allocation.second_quantum_radius**2
    )
    assert direct == pytest.approx(allocation.minimum_cost)


def test_single_edge_closed_form_satisfies_kkt_certificate():
    edge = GraphEdge("a", "b", population_gap=0.8, lipschitz_constant=1.3)
    weights = (1.1, 1.7, 2.2, 2.8)
    allocation = single_edge_optimal_allocation(edge, *weights)
    target_radii = {
        "a": allocation.first_target_radius,
        "b": allocation.second_target_radius,
    }
    quantum_radii = {
        "a": allocation.first_quantum_radius,
        "b": allocation.second_quantum_radius,
    }
    target_weights = {"a": weights[0], "b": weights[1]}
    quantum_weights = {"a": weights[2], "b": weights[3]}
    multiplier = weights[0] / allocation.first_target_radius**3

    assert kkt_certificate_holds(
        (edge,),
        target_radii,
        quantum_radii,
        target_weights,
        quantum_weights,
        {("a", "b"): multiplier},
        tolerance=1e-8,
    )


def test_kkt_residual_exposes_nonoptimal_allocation():
    edge = GraphEdge("a", "b", population_gap=1.0, lipschitz_constant=1.0)
    residuals = kkt_stationarity_residuals(
        (edge,),
        {"a": 0.1, "b": 0.2},
        {"a": 0.1, "b": 0.2},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {("a", "b"): 1000.0},
    )
    assert not math.isclose(residuals["b"][0], 0.0)


def test_duplicate_unordered_edges_are_rejected():
    edges = (
        GraphEdge("a", "b", 0.4, 1.0),
        GraphEdge("b", "a", 0.5, 1.0),
    )
    with pytest.raises(ValueError, match="unique"):
        graph_feasibility(
            edges,
            {"a": 0.01, "b": 0.01},
            {"a": 0.01, "b": 0.01},
        )


def test_single_edge_four_stream_formula_requires_positive_lipschitz_constant():
    edge = GraphEdge("a", "b", population_gap=0.5, lipschitz_constant=0.0)
    with pytest.raises(ValueError, match="positive L"):
        single_edge_optimal_allocation(edge, 1.0, 1.0, 1.0, 1.0)
