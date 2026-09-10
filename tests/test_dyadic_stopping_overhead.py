from consciousness_bridge.dyadic_stopping_overhead import (
    analytic_checkpoint_bound,
    dyadic_checkpoint_count,
    dyadic_edge_bound,
    dyadic_overhead_ratio,
    dyadic_stopping_epoch_bound,
    first_dyadic_at_or_above,
    geometric_cost_upper_bound,
    logarithmic_look_bound,
)
from consciousness_bridge.gap_stopping_complexity import EdgeStoppingComplexity


def _bound(edge, margin, samples):
    return EdgeStoppingComplexity(
        edge=edge,
        margin=margin,
        gap=abs(margin),
        amplitude=0.4,
        log_factor=5.0,
        local_samples=samples,
    )


def test_first_dyadic_checkpoint_is_smallest_power_of_two_above_threshold():
    expected = {
        1: 1,
        2: 2,
        3: 4,
        4: 4,
        5: 8,
        8: 8,
        9: 16,
        31: 32,
        32: 32,
        33: 64,
    }
    for samples, checkpoint in expected.items():
        assert first_dyadic_at_or_above(samples) == checkpoint


def test_dyadic_sample_overhead_is_always_less_than_two():
    for samples in range(1, 5000):
        ratio = dyadic_overhead_ratio(samples)
        assert 1.0 <= ratio < 2.0


def test_number_of_certification_looks_is_logarithmic():
    for samples in (1, 2, 3, 8, 9, 100, 1024, 1025):
        looks = dyadic_checkpoint_count(samples)
        assert looks == logarithmic_look_bound(samples)
        assert looks < analytic_checkpoint_bound(samples)


def test_zero_gap_edge_preserves_no_finite_bound():
    bound = EdgeStoppingComplexity(
        edge=("a", "b"),
        margin=0.0,
        gap=0.0,
        amplitude=0.4,
        log_factor=5.0,
        local_samples=None,
    )
    result = dyadic_edge_bound(bound)
    assert result.dyadic_samples is None
    assert result.overhead_ratio is None


def test_positive_family_has_less_than_factor_two_epoch_overhead():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 55),
        ("b", "c"): _bound(("b", "c"), 0.12, 65),
        ("c", "d"): _bound(("c", "d"), 0.2, 33),
    }
    result = dyadic_stopping_epoch_bound(bounds)
    assert result.status == "positive-witness"
    assert result.p48_epochs == 33
    assert result.dyadic_epochs == 64
    assert result.dyadic_epochs < 2 * result.p48_epochs
    assert result.certification_looks == 7


def test_all_negative_family_has_less_than_factor_two_epoch_overhead():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 17),
        ("b", "c"): _bound(("b", "c"), -0.12, 70),
        ("c", "d"): _bound(("c", "d"), -0.2, 63),
    }
    result = dyadic_stopping_epoch_bound(bounds)
    assert result.status == "certified-no-positive-edge"
    assert result.p48_epochs == 70
    assert result.dyadic_epochs == 128
    assert result.dyadic_epochs < 2 * result.p48_epochs


def test_zero_margin_blocks_all_negative_dyadic_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 17),
        ("b", "c"): EdgeStoppingComplexity(
            edge=("b", "c"),
            margin=0.0,
            gap=0.0,
            amplitude=0.4,
            log_factor=5.0,
            local_samples=None,
        ),
    }
    result = dyadic_stopping_epoch_bound(bounds)
    assert result.status == "no-finite-sign-gap-bound"
    assert result.dyadic_epochs is None


def test_linear_cost_bound_inherits_same_less_than_two_overhead():
    p48_cost = 700.0
    p48_epochs = 70
    dyadic_epochs = first_dyadic_at_or_above(p48_epochs)
    dyadic_cost = geometric_cost_upper_bound(
        p48_cost,
        p48_epochs,
        dyadic_epochs,
    )
    assert dyadic_cost == 1280.0
    assert dyadic_cost < 2.0 * p48_cost


def test_invalid_sample_threshold_is_rejected():
    try:
        first_dyadic_at_or_above(0)
    except ValueError as exc:
        assert "positive integer" in str(exc)
    else:
        raise AssertionError("zero threshold should be rejected")
