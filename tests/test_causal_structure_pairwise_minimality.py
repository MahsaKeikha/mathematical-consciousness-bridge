import pytest

from consciousness_bridge import (
    causal_structure_minimality,
    causal_structure_pairwise_minimality,
)

INTERVENTIONS = ("u0", "u1")
DELAYS = ("t",)
PARTITIONS = (((0,), (1,)),)
SOURCE_PAIRS = {0: (("u0", "u1"),), 1: ()}


def _fingerprint(responses):
    return causal_structure_minimality.labeled_causal_structure_fingerprint(
        responses,
        INTERVENTIONS,
        DELAYS,
        SOURCE_PAIRS,
        PARTITIONS,
        block_count=2,
    )


def _uniform_regular_support(size, degree, offset):
    probability = 1.0 / (size * degree)
    distribution = {}
    for row in range(size):
        for step in range(degree):
            column = (row + offset + step) % size
            distribution[(str(row), str(column))] = probability
    return distribution


def _ga_low_irreducibility():
    return {
        "u0": {"t": _uniform_regular_support(4, 2, 0)},
        "u1": {"t": _uniform_regular_support(4, 2, 2)},
    }


def _ga_high_irreducibility():
    diagonal = {(str(index), str(index)): 0.25 for index in range(4)}
    off_diagonal = {
        (str(row), str(column)): 1.0 / 12.0
        for row in range(4)
        for column in range(4)
        if row != column
    }
    return {
        "u0": {"t": diagonal},
        "u1": {"t": off_diagonal},
    }


def _correlation_swap():
    return {
        "u0": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
        "u1": {"t": {("0", "1"): 0.5, ("1", "0"): 0.5}},
    }


def _correlated_plus_deterministic():
    return {
        "u0": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
        "u1": {"t": {("0", "1"): 1.0}},
    }


def _identical_correlated():
    distribution = {("0", "0"): 0.5, ("1", "1"): 0.5}
    return {
        "u0": {"t": distribution},
        "u1": {"t": distribution},
    }


def _audit_domain():
    return {
        "ga_low": _fingerprint(_ga_low_irreducibility()),
        "ga_high": _fingerprint(_ga_high_irreducibility()),
        "gk_zero_influence": _fingerprint(_correlation_swap()),
        "gk_positive_influence": _fingerprint(_correlated_plus_deterministic()),
        "ak_differentiated": _fingerprint(_correlation_swap()),
        "ak_stereotyped": _fingerprint(_identical_correlated()),
    }


def test_geometry_and_influence_can_match_while_partition_landscape_differs():
    low = _fingerprint(_ga_low_irreducibility())
    high = _fingerprint(_ga_high_irreducibility())

    assert low[0] == pytest.approx((1.0,))
    assert high[0] == pytest.approx((1.0,))
    assert low[1] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert high[1] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert low[2] == pytest.approx((0.5,))
    assert high[2] == pytest.approx((0.75,))


def test_geometry_and_partition_can_match_while_influence_differs():
    zero = _fingerprint(_correlation_swap())
    positive = _fingerprint(_correlated_plus_deterministic())

    assert zero[0] == pytest.approx((1.0,))
    assert positive[0] == pytest.approx((1.0,))
    assert zero[2] == pytest.approx((0.5,))
    assert positive[2] == pytest.approx((0.5,))
    assert zero[1] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert positive[1] == pytest.approx((0.5, 0.5, 0.0, 0.0))


def test_influence_and_partition_can_match_while_geometry_differs():
    differentiated = _fingerprint(_correlation_swap())
    stereotyped = _fingerprint(_identical_correlated())

    assert differentiated[1] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert stereotyped[1] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert differentiated[2] == pytest.approx((0.5,))
    assert stereotyped[2] == pytest.approx((0.5,))
    assert differentiated[0] == pytest.approx((1.0,))
    assert stereotyped[0] == pytest.approx((0.0,))


def test_all_pairwise_component_projections_are_incomplete_on_union_domain():
    collisions = causal_structure_pairwise_minimality.pairwise_component_collisions(
        _audit_domain()
    )

    assert collisions[("geometry", "influence")] is not None
    assert collisions[("geometry", "partition")] is not None
    assert collisions[("influence", "partition")] is not None
    assert causal_structure_pairwise_minimality.every_pairwise_projection_is_incomplete(
        _audit_domain()
    )


def test_full_three_component_fingerprint_is_complete_on_itself():
    full = _audit_domain()
    projected = {
        state: causal_structure_pairwise_minimality.component_projection(
            fingerprint,
            ("geometry", "influence", "partition"),
        )
        for state, fingerprint in full.items()
    }

    assert causal_structure_minimality.projection_is_complete(full, projected)


def test_component_projection_validates_requested_components():
    fingerprint = _fingerprint(_correlation_swap())

    with pytest.raises(ValueError, match="At least one component"):
        causal_structure_pairwise_minimality.component_projection(fingerprint, ())
    with pytest.raises(ValueError, match="must be unique"):
        causal_structure_pairwise_minimality.component_projection(
            fingerprint,
            ("geometry", "geometry"),
        )
    with pytest.raises(ValueError, match="Unknown causal-structure component"):
        causal_structure_pairwise_minimality.component_projection(
            fingerprint,
            ("geometry", "unknown"),
        )
