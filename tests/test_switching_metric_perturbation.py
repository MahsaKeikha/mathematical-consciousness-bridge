from math import isclose

from consciousness_bridge.switching_metric_perturbation import (
    metric_drift_reoptimization_certificate,
    metric_perturbation_certificate,
    metric_sup_distance,
    rooted_route_edge_count,
    route_reuse_certificate,
)


def line_metric(coordinates):
    return {
        (first, second): abs(coordinates[first] - coordinates[second])
        for first in coordinates
        for second in coordinates
    }


def shifted_metric(costs, delta):
    return {
        edge: (value if edge[0] == edge[1] else value + delta)
        for edge, value in costs.items()
    }


def test_metric_sup_distance_matches_uniform_off_diagonal_shift():
    points = ("s", "a", "b")
    old = line_metric({"s": 0.0, "a": 1.0, "b": 3.0})
    new = shifted_metric(old, 0.25)
    assert isclose(metric_sup_distance(points, old, new), 0.25)


def test_rooted_route_edge_count_is_sharp_for_external_start():
    assert rooted_route_edge_count(("a", "b"), start="s") == 2
    assert rooted_route_edge_count(("a", "b", "c"), start=None) == 2
    assert rooted_route_edge_count(("a", "b", "c"), start="a") == 2


def test_metric_perturbation_bound_is_attained_by_uniform_shift():
    old = line_metric({"s": 0.0, "a": 1.0, "b": 3.0})
    new = shifted_metric(old, 0.5)
    certificate = metric_perturbation_certificate(
        {"a": 1, "b": 1},
        old,
        new,
        start="s",
    )
    assert certificate.route_edge_count == 2
    assert isclose(certificate.metric_sup_distance, 0.5)
    assert isclose(certificate.absolute_switching_change, 1.0)
    assert isclose(certificate.uniform_bound, 1.0)
    assert certificate.bound_holds


def test_metric_perturbation_total_cost_change_is_only_switching_change():
    old = line_metric({"s": 0.0, "a": 2.0, "b": 5.0})
    new = shifted_metric(old, 0.2)
    certificate = metric_perturbation_certificate(
        {"a": 3, "b": 4},
        old,
        new,
        start="s",
        sample_cost=7.0,
    )
    assert isclose(certificate.absolute_switching_change, 0.4)
    assert certificate.bound_holds


def test_route_reuse_is_valid_one_sided_upper_bound():
    old = line_metric({"s": 0.0, "t": 0.5, "a": 1.0, "b": 3.0, "c": 4.0})
    new = shifted_metric(old, 0.3)
    certificate = route_reuse_certificate(
        {"a": 1, "b": 1, "c": 1},
        old,
        new,
        old_start="s",
        new_start="t",
    )
    assert certificate.bound_holds
    assert certificate.actual_change <= certificate.one_sided_change_upper_bound + 1e-12


def test_combined_residual_start_and_metric_drift_bound_holds():
    coordinates = {
        "s": 0.0,
        "t": 0.5,
        "a": 1.0,
        "b": 3.0,
        "c": 4.0,
    }
    old = line_metric(coordinates)
    new = shifted_metric(old, 0.2)
    certificate = metric_drift_reoptimization_certificate(
        {"a": 2, "b": 2, "c": 2},
        {"a": 0, "b": 1, "c": 1},
        old,
        new,
        old_start="s",
        new_start="t",
        sample_cost=1.5,
    )
    assert certificate.fixed_geometry_release >= 0.0
    assert certificate.perturbation_penalty >= 0.0
    assert certificate.lower_bound_holds
    assert certificate.actual_release + 1e-12 >= certificate.guaranteed_release_lower_bound


def test_strict_decrease_certificate_can_survive_geometry_drift():
    coordinates = {
        "s": 0.0,
        "t": 0.1,
        "a": 1.0,
        "b": 3.0,
        "c": 5.0,
    }
    old = line_metric(coordinates)
    new = shifted_metric(old, 0.05)
    certificate = metric_drift_reoptimization_certificate(
        {"a": 5, "b": 5, "c": 5},
        {"a": 0, "b": 1, "c": 1},
        old,
        new,
        old_start="s",
        new_start="t",
        sample_cost=2.0,
    )
    assert certificate.strict_decrease_certified
    assert certificate.actual_release > 0.0


def test_zero_remaining_support_has_no_metric_drift_penalty():
    old = line_metric({"s": 0.0, "t": 2.0, "a": 1.0})
    new = shifted_metric(old, 0.4)
    certificate = metric_drift_reoptimization_certificate(
        {"a": 3},
        {"a": 0},
        old,
        new,
        old_start="s",
        new_start="t",
    )
    assert certificate.metric_sup_distance == 0.0
    assert certificate.perturbation_penalty == 0.0
    assert certificate.lower_bound_holds
