from consciousness_bridge.bounded_starvation_sampling import (
    asynchronous_stopping_bound,
    fairness_violations,
    is_h_fair_schedule,
    minimum_samples_under_fairness,
    prefix_local_sample_counts,
    rounds_for_local_samples,
    starvation_counterexample_length,
)
from consciousness_bridge.gap_stopping_complexity import EdgeStoppingComplexity


def _bound(edge, margin, samples):
    return EdgeStoppingComplexity(
        edge=edge,
        margin=margin,
        gap=abs(margin),
        amplitude=0.3,
        log_factor=4.0,
        local_samples=samples,
    )


def test_round_robin_schedule_is_h_fair():
    active = (("a", "b", "c"),) * 6
    selections = ("a", "b", "c", "a", "b", "c")
    assert is_h_fair_schedule(active, selections, 3)


def test_starved_active_vertex_is_detected():
    active = (("a", "b"),) * 4
    selections = ("a", "a", "a", "a")
    violations = fairness_violations(active, selections, 2)
    assert violations
    assert any(v.vertex == "b" for v in violations)


def test_pruned_vertex_does_not_create_future_fairness_obligation():
    active = (
        ("a", "b"),
        ("a", "b"),
        ("a",),
        ("a",),
    )
    selections = ("a", "b", "a", "a")
    assert is_h_fair_schedule(active, selections, 2)


def test_fairness_implies_floor_rounds_over_h_samples():
    assert minimum_samples_under_fairness(0, 4) == 0
    assert minimum_samples_under_fairness(3, 4) == 0
    assert minimum_samples_under_fairness(4, 4) == 1
    assert minimum_samples_under_fairness(17, 4) == 4
    assert rounds_for_local_samples(5, 4) == 20


def test_positive_witness_global_time_bound_is_h_times_local_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 50),
        ("b", "c"): _bound(("b", "c"), 0.2, 18),
        ("c", "d"): _bound(("c", "d"), 0.08, 41),
    }
    result = asynchronous_stopping_bound(bounds, fairness_horizon=5)
    assert result.status == "positive-witness"
    assert result.local_epoch_bound == 18
    assert result.global_round_bound == 90
    assert result.controlling_edges == (("b", "c"),)


def test_all_negative_global_time_bound_is_h_times_slowest_edge():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 12),
        ("b", "c"): _bound(("b", "c"), -0.02, 75),
        ("c", "d"): _bound(("c", "d"), -0.2, 20),
    }
    result = asynchronous_stopping_bound(bounds, fairness_horizon=4)
    assert result.status == "certified-no-positive-edge"
    assert result.local_epoch_bound == 75
    assert result.global_round_bound == 300


def test_zero_margin_preserves_no_finite_global_time_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 12),
        ("b", "c"): EdgeStoppingComplexity(
            edge=("b", "c"),
            margin=0.0,
            gap=0.0,
            amplitude=0.3,
            log_factor=4.0,
            local_samples=None,
        ),
    }
    result = asynchronous_stopping_bound(bounds, fairness_horizon=4)
    assert result.status == "no-finite-sign-gap-bound"
    assert result.global_round_bound is None


def test_prefix_counts_track_asynchronous_schedule():
    history = prefix_local_sample_counts(
        ("a", "a", "b", "c", "a"),
        ("a", "b", "c"),
    )
    assert history[-1] == {"a": 3, "b": 1, "c": 1}


def test_without_fairness_required_endpoint_can_be_delayed_arbitrarily():
    schedule = starvation_counterexample_length(1000)
    assert len(schedule) == 1000
    assert "needed" not in schedule


def test_selected_vertex_must_be_active():
    try:
        fairness_violations((("a",),), ("b",), 1)
    except ValueError as exc:
        assert "not active" in str(exc)
    else:
        raise AssertionError("inactive selection should be rejected")
