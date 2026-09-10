from consciousness_bridge.gap_stopping_complexity import (
    adaptive_active_cost,
    edge_complexity_bounds,
    edge_uncertainty_parameters,
    full_family_cost_upper_bound,
    required_local_samples,
    sequential_stopping_epoch_bound,
    uncertainty_envelope,
)


def test_explicit_local_sample_bound_certifies_declared_gap():
    for gap, amplitude, log_factor in (
        (0.20, 0.25, 2.0),
        (0.10, 0.40, 10.0),
        (0.35, 0.15, 1.0),
        (0.05, 0.50, 20.0),
    ):
        samples = required_local_samples(gap, amplitude, log_factor)
        assert uncertainty_envelope(samples, amplitude, log_factor) < gap / 2.0
        assert uncertainty_envelope(samples + 100, amplitude, log_factor) < gap / 2.0


def test_smaller_gap_requires_more_samples_for_same_envelope():
    wide_gap = required_local_samples(0.25, 0.3, 4.0)
    narrow_gap = required_local_samples(0.08, 0.3, 4.0)
    assert narrow_gap > wide_gap


def test_edge_parameters_combine_shared_endpoint_uncertainties():
    amplitude, log_factor = edge_uncertainty_parameters(
        ("a", "b"),
        target_amplitudes={"a": 0.10, "b": 0.20},
        quantum_amplitudes={"a": 0.05, "b": 0.08},
        target_log_factors={"a": 2.0, "b": 3.0},
        quantum_log_factors={"a": 5.0, "b": 4.0},
        lipschitz_constant=2.0,
    )
    assert amplitude == 0.10 + 0.20 + 2.0 * (0.05 + 0.08)
    assert log_factor == 5.0


def _family_bounds(margins):
    edges = tuple(margins)
    vertices = {vertex for edge in edges for vertex in edge}
    return edge_complexity_bounds(
        edges,
        margins,
        target_amplitudes={vertex: 0.12 for vertex in vertices},
        quantum_amplitudes={vertex: 0.07 for vertex in vertices},
        target_log_factors={vertex: 3.0 for vertex in vertices},
        quantum_log_factors={vertex: 5.0 for vertex in vertices},
        lipschitz_constants={edge: 1.4 for edge in edges},
    )


def test_positive_family_stops_by_easiest_positive_edge():
    margins = {
        ("a", "b"): -0.05,
        ("b", "c"): 0.08,
        ("c", "d"): 0.20,
    }
    bounds = _family_bounds(margins)
    result = sequential_stopping_epoch_bound(bounds)

    positive_samples = [
        bound.local_samples
        for bound in bounds.values()
        if bound.margin > 0.0
    ]
    assert result.status == "positive-witness"
    assert result.epochs == min(positive_samples)
    assert ("c", "d") in result.controlling_edges


def test_all_negative_family_waits_for_slowest_edge_elimination():
    margins = {
        ("a", "b"): -0.20,
        ("b", "c"): -0.05,
        ("c", "d"): -0.12,
    }
    bounds = _family_bounds(margins)
    result = sequential_stopping_epoch_bound(bounds)

    assert result.status == "certified-no-positive-edge"
    assert result.epochs == max(
        bound.local_samples for bound in bounds.values()
    )
    assert ("b", "c") in result.controlling_edges


def test_zero_margin_blocks_finite_all_negative_sign_bound():
    bounds = _family_bounds(
        {
            ("a", "b"): -0.2,
            ("b", "c"): 0.0,
        }
    )
    result = sequential_stopping_epoch_bound(bounds)
    assert result.status == "no-finite-sign-gap-bound"
    assert result.epochs is None
    assert result.controlling_edges == (("b", "c"),)


def test_positive_edge_still_gives_finite_bound_when_other_edge_has_zero_gap():
    bounds = _family_bounds(
        {
            ("a", "b"): 0.1,
            ("b", "c"): 0.0,
        }
    )
    result = sequential_stopping_epoch_bound(bounds)
    assert result.status == "positive-witness"
    assert result.epochs is not None


def test_round_robin_and_pruned_realized_costs_are_consistent():
    vertices = ("a", "b", "c", "d")
    epochs = 5
    full = full_family_cost_upper_bound(vertices, epochs)
    realized = adaptive_active_cost(
        (
            ("a", "b", "c", "d"),
            ("a", "b", "c", "d"),
            ("a", "b", "c"),
            ("a", "b"),
            ("a", "b"),
        )
    )
    assert full == 40.0
    assert realized == 30.0
    assert realized <= full


def test_zero_uncertainty_amplitude_needs_only_one_local_sample():
    assert required_local_samples(0.1, 0.0, 1.0) == 1
    assert uncertainty_envelope(1, 0.0, 1.0) == 0.0


def test_invalid_log_factor_is_rejected():
    try:
        required_local_samples(0.1, 0.2, 0.5)
    except ValueError as exc:
        assert "log_factor" in str(exc)
    else:
        raise AssertionError("log_factor below one should be rejected")
