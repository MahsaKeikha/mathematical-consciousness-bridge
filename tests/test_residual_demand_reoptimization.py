from math import isclose

from consciousness_bridge.residual_demand_reoptimization import (
    pruning_release_by_vertex,
    reoptimization_certificate,
    residual_state,
    residual_vertex_demands,
    sample_release_by_vertex,
)


def test_residual_demands_use_largest_unsatisfied_incident_threshold():
    vertices = ("a", "b", "c")
    edges = (("a", "b"), ("b", "c"))
    residual = residual_vertex_demands(
        vertices,
        edges,
        {("a", "b"): 8.0, ("b", "c"): 12.0},
        {"a": 3.0, "b": 5.0, "c": 9.0},
    )
    assert residual == {"a": 5.0, "b": 7.0, "c": 3.0}


def test_completed_endpoint_has_zero_residual_even_if_edge_remains_active():
    residual = residual_vertex_demands(
        ("a", "b"),
        (("a", "b"),),
        {("a", "b"): 5.0},
        {"a": 7.0, "b": 2.0},
    )
    assert residual == {"a": 0.0, "b": 3.0}


def test_residual_state_reoptimizes_exactly_by_p52():
    state = residual_state(
        ("a", "b", "c"),
        (("a", "b"), ("b", "c")),
        {("a", "b"): 6.0, ("b", "c"): 10.0},
        {"a": 1.0, "b": 4.0, "c": 5.0},
        capacity=2.0,
    )
    assert state.residual_demands == {"a": 5.0, "b": 6.0, "c": 5.0}
    assert isclose(state.total_residual_demand, 16.0)
    assert isclose(state.optimal_remaining_time, 8.0)
    assert isclose(sum(state.optimal_service_shares.values()), 2.0)


def test_sampling_and_safe_pruning_cannot_increase_residual_demands():
    certificate = reoptimization_certificate(
        ("a", "b", "c", "d"),
        (("a", "b"), ("b", "c"), ("c", "d")),
        (("a", "b"), ("c", "d")),
        {
            ("a", "b"): 8.0,
            ("b", "c"): 12.0,
            ("c", "d"): 7.0,
        },
        {"a": 2.0, "b": 4.0, "c": 3.0, "d": 2.0},
        {"a": 4.0, "b": 6.0, "c": 5.0, "d": 3.0},
        capacity=1.0,
    )
    assert certificate.componentwise_nonincreasing
    assert certificate.released_residual_demand >= 0.0
    assert certificate.released_optimal_time >= 0.0
    assert isclose(
        certificate.released_optimal_time,
        certificate.released_residual_demand,
    )


def test_released_time_equals_released_demand_divided_by_capacity():
    certificate = reoptimization_certificate(
        ("a", "b", "c"),
        (("a", "b"), ("b", "c")),
        (("a", "b"),),
        {("a", "b"): 8.0, ("b", "c"): 12.0},
        {"a": 2.0, "b": 3.0, "c": 4.0},
        {"a": 4.0, "b": 5.0, "c": 5.0},
        capacity=2.5,
    )
    assert isclose(
        certificate.released_optimal_time,
        certificate.released_residual_demand / 2.5,
    )


def test_pruning_release_detects_edge_that_was_unique_bottleneck():
    release = pruning_release_by_vertex(
        ("a", "b", "c"),
        (("a", "b"), ("b", "c")),
        (("a", "b"),),
        {("a", "b"): 5.0, ("b", "c"): 11.0},
        {"a": 1.0, "b": 2.0, "c": 3.0},
    )
    assert release["a"] == 0.0
    assert release["b"] == 6.0
    assert release["c"] == 8.0


def test_pruning_nonbinding_edge_releases_no_vertex_demand():
    release = pruning_release_by_vertex(
        ("a", "b", "c"),
        (("a", "b"), ("b", "c")),
        (("b", "c"),),
        {("a", "b"): 4.0, ("b", "c"): 10.0},
        {"a": 5.0, "b": 2.0, "c": 3.0},
    )
    assert release == {"a": 0.0, "b": 0.0, "c": 0.0}


def test_sample_release_is_componentwise_nonnegative():
    release = sample_release_by_vertex(
        ("a", "b", "c"),
        (("a", "b"), ("b", "c")),
        {("a", "b"): 8.0, ("b", "c"): 9.0},
        {"a": 2.0, "b": 2.0, "c": 3.0},
        {"a": 5.0, "b": 4.0, "c": 7.0},
    )
    assert all(value >= 0.0 for value in release.values())
    assert release["a"] == 3.0
    assert release["b"] == 2.0
    assert release["c"] == 4.0


def test_removing_all_edges_releases_all_remaining_demand():
    certificate = reoptimization_certificate(
        ("a", "b"),
        (("a", "b"),),
        (),
        {("a", "b"): 6.0},
        {"a": 2.0, "b": 1.0},
        {"a": 2.0, "b": 1.0},
    )
    assert certificate.after.total_residual_demand == 0.0
    assert certificate.after.optimal_remaining_time == 0.0
    assert certificate.released_residual_demand == 9.0


def test_counts_may_not_move_backward():
    try:
        reoptimization_certificate(
            ("a", "b"),
            (("a", "b"),),
            (("a", "b"),),
            {("a", "b"): 5.0},
            {"a": 2.0, "b": 2.0},
            {"a": 1.0, "b": 3.0},
        )
    except ValueError as exc:
        assert "nondecreasing" in str(exc)
    else:
        raise AssertionError("decreasing local count should be rejected")
