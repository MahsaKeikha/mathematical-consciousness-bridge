import pytest

from consciousness_bridge import causal_structure_minimality, intervention_causal_geometry

DELAY = ("t",)
INTERVENTIONS = ("u0", "u1")
PARTITIONS = (((0,), (1,)),)
SOURCE_PAIRS = {
    0: (("u0", "u1"),),
    1: (("u0", "u1"),),
}


def _correlation_swap():
    return {
        "u0": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
        "u1": {"t": {("0", "1"): 0.5, ("1", "0"): 0.5}},
    }


def _product_shift():
    return {
        "u0": {"t": {("0", "0"): 0.5, ("0", "1"): 0.5}},
        "u1": {"t": {("1", "0"): 0.5, ("1", "1"): 0.5}},
    }


def _differentiated_product():
    return {
        "u0": {"t": {("0", "0"): 1.0}},
        "u1": {"t": {("1", "1"): 1.0}},
    }


def _stereotyped_product():
    return {
        "u0": {"t": {("0", "0"): 1.0}},
        "u1": {"t": {("0", "0"): 1.0}},
    }


def _identical_correlated():
    return {
        "u0": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
        "u1": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
    }


def _full(responses):
    return causal_structure_minimality.labeled_causal_structure_fingerprint(
        responses,
        INTERVENTIONS,
        DELAY,
        SOURCE_PAIRS,
        PARTITIONS,
        block_count=2,
    )


def test_same_response_geometry_can_hide_different_partition_structure():
    correlated = _correlation_swap()
    product = _product_shift()

    geometry_correlated = causal_structure_minimality.geometry_fingerprint(
        correlated, INTERVENTIONS, DELAY
    )
    geometry_product = causal_structure_minimality.geometry_fingerprint(
        product, INTERVENTIONS, DELAY
    )
    partition_correlated = causal_structure_minimality.partition_fingerprint(
        correlated, PARTITIONS, DELAY
    )
    partition_product = causal_structure_minimality.partition_fingerprint(
        product, PARTITIONS, DELAY
    )

    assert geometry_correlated == pytest.approx((1.0,))
    assert geometry_product == pytest.approx((1.0,))
    assert partition_correlated == pytest.approx((0.5,))
    assert partition_product == pytest.approx((0.0,))
    assert _full(correlated) != _full(product)


def test_same_partition_landscape_can_hide_different_response_geometry():
    differentiated = _differentiated_product()
    stereotyped = _stereotyped_product()

    partition_differentiated = causal_structure_minimality.partition_fingerprint(
        differentiated, PARTITIONS, DELAY
    )
    partition_stereotyped = causal_structure_minimality.partition_fingerprint(
        stereotyped, PARTITIONS, DELAY
    )
    geometry_differentiated = causal_structure_minimality.geometry_fingerprint(
        differentiated, INTERVENTIONS, DELAY
    )
    geometry_stereotyped = causal_structure_minimality.geometry_fingerprint(
        stereotyped, INTERVENTIONS, DELAY
    )

    assert partition_differentiated == pytest.approx((0.0,))
    assert partition_stereotyped == pytest.approx((0.0,))
    assert geometry_differentiated == pytest.approx((1.0,))
    assert geometry_stereotyped == pytest.approx((0.0,))
    assert _full(differentiated) != _full(stereotyped)


def test_same_directed_influence_can_hide_joint_response_difference():
    swap = _correlation_swap()
    identical = _identical_correlated()

    influence_swap = causal_structure_minimality.influence_fingerprint(
        swap, SOURCE_PAIRS, DELAY, block_count=2
    )
    influence_identical = causal_structure_minimality.influence_fingerprint(
        identical, SOURCE_PAIRS, DELAY, block_count=2
    )
    geometry_swap = causal_structure_minimality.geometry_fingerprint(
        swap, INTERVENTIONS, DELAY
    )
    geometry_identical = causal_structure_minimality.geometry_fingerprint(
        identical, INTERVENTIONS, DELAY
    )

    assert influence_swap == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert influence_identical == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert geometry_swap == pytest.approx((1.0,))
    assert geometry_identical == pytest.approx((0.0,))
    assert _full(swap) != _full(identical)


def test_response_diameter_collision_does_not_imply_equal_geometry():
    system_a = {
        "u0": {"t": {("0", "0"): 1.0}},
        "u1": {"t": {("1", "1"): 1.0}},
        "u2": {"t": {("0", "0"): 1.0}},
    }
    system_b = {
        "u0": {"t": {("0", "0"): 1.0}},
        "u1": {"t": {("1", "1"): 1.0}},
        "u2": {"t": {("0", "0"): 0.5, ("1", "1"): 0.5}},
    }
    interventions = ("u0", "u1", "u2")

    assert intervention_causal_geometry.response_diameter(
        system_a, "t"
    ) == pytest.approx(1.0)
    assert intervention_causal_geometry.response_diameter(
        system_b, "t"
    ) == pytest.approx(1.0)
    assert causal_structure_minimality.geometry_fingerprint(
        system_a, interventions, DELAY
    ) != pytest.approx(
        causal_structure_minimality.geometry_fingerprint(
            system_b, interventions, DELAY
        )
    )


def test_same_minimum_irreducibility_scalar_can_hide_geometry_difference():
    swap = _correlation_swap()
    identical = _identical_correlated()

    kappa_swap = intervention_causal_geometry.partition_response_irreducibility(
        swap, PARTITIONS[0], "t"
    )
    kappa_identical = intervention_causal_geometry.partition_response_irreducibility(
        identical, PARTITIONS[0], "t"
    )

    assert kappa_swap == pytest.approx(0.5)
    assert kappa_identical == pytest.approx(0.5)
    assert causal_structure_minimality.geometry_fingerprint(
        swap, INTERVENTIONS, DELAY
    ) != pytest.approx(
        causal_structure_minimality.geometry_fingerprint(
            identical, INTERVENTIONS, DELAY
        )
    )


def test_boolean_recurrence_is_not_complete_for_influence_strength():
    strong_cycle = ((0.0, 1.0), (1.0, 0.0))
    weak_cycle = ((0.0, 0.2), (0.2, 0.0))

    assert intervention_causal_geometry.has_directed_cycle(strong_cycle)
    assert intervention_causal_geometry.has_directed_cycle(weak_cycle)
    assert strong_cycle != weak_cycle


def test_projection_collision_detects_non_reconstructibility():
    correlated = _correlation_swap()
    product = _product_shift()
    full = {
        "correlated": _full(correlated),
        "product": _full(product),
    }
    projected = {
        "correlated": causal_structure_minimality.geometry_fingerprint(
            correlated, INTERVENTIONS, DELAY
        ),
        "product": causal_structure_minimality.geometry_fingerprint(
            product, INTERVENTIONS, DELAY
        ),
    }

    assert causal_structure_minimality.projection_collision(full, projected) == (
        "correlated",
        "product",
    )
    assert not causal_structure_minimality.projection_is_complete(full, projected)


def test_injective_projection_is_complete_on_declared_domain():
    full = {"a": (1, 2), "b": (3, 4)}
    projected = {"a": "x", "b": "y"}

    assert causal_structure_minimality.projection_collision(full, projected) is None
    assert causal_structure_minimality.projection_is_complete(full, projected)
