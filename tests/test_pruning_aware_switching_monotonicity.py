from math import isclose

import pytest

from consciousness_bridge.pruning_aware_switching_monotonicity import (
    componentwise_nonincreasing,
    positive_support,
    pruning_monotonicity_certificate,
    shortcut_certificate_from_old_optimum,
    support_preserving_release,
)


def _line_metric(points):
    coordinates = {point: index for index, point in enumerate(points)}
    return {
        (u, v): float(abs(coordinates[u] - coordinates[v]))
        for u in points
        for v in points
    }


def test_positive_support_ignores_zero_demands():
    assert positive_support({"a": 3, "b": 0, "c": 1}) == ("a", "c")


def test_componentwise_nonincreasing_allows_missing_new_vertices_as_zero():
    assert componentwise_nonincreasing({"a": 3, "b": 2}, {"a": 1})
    assert not componentwise_nonincreasing({"a": 1}, {"a": 2})


def test_support_preserving_reduction_changes_only_acquisition_term():
    release = support_preserving_release(
        {"a": 5, "b": 4, "c": 2},
        {"a": 3, "b": 1, "c": 1},
        sample_cost=2.0,
    )
    assert release == 12.0


def test_pruning_can_reduce_both_acquisition_and_switching_cost():
    points = ("s", "a", "b", "c")
    costs = _line_metric(points)
    certificate = pruning_monotonicity_certificate(
        {"a": 3, "b": 2, "c": 4},
        {"a": 2, "b": 0, "c": 1},
        costs,
        start="s",
        sample_cost=1.5,
    )
    assert certificate.support_nested
    assert certificate.cost_nonincreasing
    assert certificate.acquisition_release == 9.0
    assert certificate.route_release >= 0.0
    assert isclose(
        certificate.total_release,
        certificate.acquisition_release + certificate.route_release,
    )


def test_support_unchanged_gives_zero_optimal_route_release():
    points = ("s", "a", "b", "c")
    costs = _line_metric(points)
    certificate = pruning_monotonicity_certificate(
        {"a": 4, "b": 3, "c": 2},
        {"a": 1, "b": 1, "c": 1},
        costs,
        start="s",
    )
    assert certificate.old_support == certificate.new_support
    assert certificate.route_release == 0.0
    assert certificate.total_release == certificate.acquisition_release


def test_shortcut_from_old_optimum_certifies_nonnegative_route_release():
    points = ("s", "a", "b", "c", "d")
    costs = _line_metric(points)
    shortcut = shortcut_certificate_from_old_optimum(
        {"a": 1, "b": 1, "c": 1, "d": 1},
        {"a": 1, "b": 0, "c": 1, "d": 0},
        costs,
        start="s",
    )
    assert shortcut.retained_order == ("a", "c")
    assert shortcut.certified_route_release >= 0.0
    assert shortcut.shortcut_path_cost <= shortcut.old_path_cost


def test_actual_optimal_route_release_dominates_old_route_shortcut_release():
    points = ("s", "a", "b", "c", "d")
    costs = _line_metric(points)
    old = {"a": 1, "b": 1, "c": 1, "d": 1}
    new = {"a": 1, "b": 0, "c": 1, "d": 0}
    exact = pruning_monotonicity_certificate(old, new, costs, start="s")
    shortcut = shortcut_certificate_from_old_optimum(old, new, costs, start="s")
    assert exact.route_release + 1e-12 >= shortcut.certified_route_release


def test_all_residual_demand_can_disappear():
    points = ("s", "a", "b")
    costs = _line_metric(points)
    certificate = pruning_monotonicity_certificate(
        {"a": 2, "b": 1},
        {"a": 0, "b": 0},
        costs,
        start="s",
    )
    assert certificate.new_support == ()
    assert certificate.new_acquisition_cost == 0.0
    assert certificate.new_switching_cost == 0.0
    assert certificate.cost_nonincreasing


def test_increasing_residual_demand_is_rejected():
    points = ("s", "a")
    costs = _line_metric(points)
    with pytest.raises(ValueError, match="componentwise nonincreasing"):
        pruning_monotonicity_certificate(
            {"a": 1},
            {"a": 2},
            costs,
            start="s",
        )


def test_support_preserving_helper_rejects_support_change():
    with pytest.raises(ValueError, match="support must be unchanged"):
        support_preserving_release({"a": 2, "b": 1}, {"a": 1, "b": 0})
