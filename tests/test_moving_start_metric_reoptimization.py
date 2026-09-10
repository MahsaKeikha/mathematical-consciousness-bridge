from math import isclose

import pytest

from consciousness_bridge.moving_start_metric_reoptimization import (
    fixed_support_start_change,
    moving_start_reoptimization_certificate,
    release_identity_check,
    start_lipschitz_certificate,
)


def _line_metric(points):
    coordinates = {point: index for index, point in enumerate(points)}
    return {
        (u, v): float(abs(coordinates[u] - coordinates[v]))
        for u in points
        for v in points
    }


def test_start_lipschitz_bound_holds_on_line_metric():
    points = ("s", "t", "a", "b", "c")
    costs = _line_metric(points)
    certificate = start_lipschitz_certificate(
        ("a", "b", "c"),
        costs,
        first_start="s",
        second_start="t",
    )
    assert certificate.bound_holds
    assert certificate.absolute_route_change <= certificate.start_distance


def test_start_lipschitz_can_be_tight():
    points = ("s", "t", "a")
    coordinates = {"s": 0.0, "t": 1.0, "a": 3.0}
    costs = {
        (u, v): abs(coordinates[u] - coordinates[v])
        for u in points
        for v in points
    }
    certificate = start_lipschitz_certificate(
        ("a",),
        costs,
        first_start="s",
        second_start="t",
    )
    assert isclose(certificate.absolute_route_change, certificate.start_distance)


def test_fixed_support_total_cost_is_start_lipschitz():
    points = ("s", "t", "a", "b")
    costs = _line_metric(points)
    change, bound = fixed_support_start_change(
        {"a": 4, "b": 3},
        costs,
        first_start="s",
        second_start="t",
        sample_cost=2.0,
    )
    assert change <= bound


def test_moving_start_can_erode_fixed_start_savings_by_at_most_distance():
    points = ("s", "t", "a", "b", "c")
    costs = _line_metric(points)
    certificate = moving_start_reoptimization_certificate(
        {"a": 5, "b": 4, "c": 3},
        {"a": 2, "b": 0, "c": 1},
        costs,
        old_start="s",
        new_start="t",
        sample_cost=1.0,
    )
    assert certificate.lower_bound_holds
    assert certificate.actual_release >= certificate.guaranteed_release_lower_bound
    assert release_identity_check(certificate)


def test_large_fixed_start_release_certifies_strict_decrease_despite_start_move():
    points = ("s", "t", "a", "b")
    costs = _line_metric(points)
    certificate = moving_start_reoptimization_certificate(
        {"a": 10, "b": 10},
        {"a": 1, "b": 1},
        costs,
        old_start="s",
        new_start="t",
        sample_cost=1.0,
    )
    assert certificate.fixed_start_release > certificate.start_distance
    assert certificate.strict_decrease_certified
    assert certificate.actual_release > 0.0


def test_start_move_bound_can_be_negative_without_claiming_increase():
    points = ("s", "t", "a")
    coordinates = {"s": 0.0, "t": 10.0, "a": 1.0}
    costs = {
        (u, v): abs(coordinates[u] - coordinates[v])
        for u in points
        for v in points
    }
    certificate = moving_start_reoptimization_certificate(
        {"a": 2},
        {"a": 1},
        costs,
        old_start="s",
        new_start="t",
    )
    assert certificate.guaranteed_release_lower_bound < 0.0
    assert not certificate.strict_decrease_certified
    assert certificate.lower_bound_holds


def test_same_start_recovers_p55_fixed_start_release():
    points = ("s", "a", "b")
    costs = _line_metric(points)
    certificate = moving_start_reoptimization_certificate(
        {"a": 4, "b": 2},
        {"a": 1, "b": 1},
        costs,
        old_start="s",
        new_start="s",
    )
    assert certificate.start_distance == 0.0
    assert isclose(certificate.actual_release, certificate.fixed_start_release)
    assert isclose(
        certificate.guaranteed_release_lower_bound,
        certificate.fixed_start_release,
    )


def test_increasing_residual_demands_are_rejected():
    points = ("s", "t", "a")
    costs = _line_metric(points)
    with pytest.raises(ValueError, match="componentwise nonincreasing"):
        moving_start_reoptimization_certificate(
            {"a": 1},
            {"a": 2},
            costs,
            old_start="s",
            new_start="t",
        )


def test_empty_support_is_rejected_for_route_lipschitz_certificate():
    points = ("s", "t")
    costs = _line_metric(points)
    with pytest.raises(ValueError, match="support must be nonempty"):
        start_lipschitz_certificate(
            (),
            costs,
            first_start="s",
            second_start="t",
        )
