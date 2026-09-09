import itertools

import pytest

from consciousness_bridge.partition_lattice_node_aggregation import (
    aggregation_compatible_coarse_map,
    canonical_partition,
    descend_partition,
    is_aggregation_saturated,
    lift_partition,
    node_aggregation_partition_certificate,
    partition_join,
    partition_meet,
    partition_refines,
)

FINE_NODES = ("a", "b", "c", "d", "e")
AGGREGATION = {
    "a": "X",
    "b": "X",
    "c": "Y",
    "d": "Z",
    "e": "Z",
}
COARSE_NODES = ("X", "Y", "Z")


def test_saturation_is_exact_descent_criterion():
    saturated = (("a", "b", "c"), ("d", "e"))
    nonsaturated = (("a", "c"), ("b", "d", "e"))

    assert is_aggregation_saturated(saturated, AGGREGATION)
    assert not is_aggregation_saturated(nonsaturated, AGGREGATION)
    assert descend_partition(saturated, AGGREGATION) == canonical_partition(
        (("X", "Y"), ("Z",)),
        COARSE_NODES,
    )

    with pytest.raises(ValueError, match="no coarse descent"):
        descend_partition(nonsaturated, AGGREGATION)


def test_lift_and_descent_are_inverse_on_coarse_partitions():
    coarse = (("X", "Y"), ("Z",))
    lifted = lift_partition(coarse, AGGREGATION)
    descended = descend_partition(lifted, AGGREGATION)
    assert descended == canonical_partition(coarse, COARSE_NODES)


def test_saturated_fine_partition_round_trip_is_exact():
    fine = (("a", "b"), ("c", "d", "e"))
    descended = descend_partition(fine, AGGREGATION)
    lifted = lift_partition(descended, AGGREGATION)
    assert lifted == canonical_partition(fine, FINE_NODES)


def test_lift_preserves_refinement_order():
    coarse_fine = (("X",), ("Y",), ("Z",))
    coarse_coarse = (("X", "Y"), ("Z",))
    assert partition_refines(coarse_fine, coarse_coarse, COARSE_NODES)

    lifted_fine = lift_partition(coarse_fine, AGGREGATION)
    lifted_coarse = lift_partition(coarse_coarse, AGGREGATION)
    assert partition_refines(lifted_fine, lifted_coarse, FINE_NODES)


def test_lift_preserves_meet_and_join():
    first = (("X", "Y"), ("Z",))
    second = (("X",), ("Y", "Z"))

    coarse_meet = partition_meet(first, second, COARSE_NODES)
    coarse_join = partition_join(first, second, COARSE_NODES)

    lifted_first = lift_partition(first, AGGREGATION)
    lifted_second = lift_partition(second, AGGREGATION)

    assert lift_partition(coarse_meet, AGGREGATION) == partition_meet(
        lifted_first,
        lifted_second,
        FINE_NODES,
    )
    assert lift_partition(coarse_join, AGGREGATION) == partition_join(
        lifted_first,
        lifted_second,
        FINE_NODES,
    )


def _three_bit_distribution():
    return {
        (0, 0, 0): 0.20,
        (0, 0, 1): 0.05,
        (0, 1, 0): 0.05,
        (0, 1, 1): 0.20,
        (1, 0, 0): 0.05,
        (1, 0, 1): 0.20,
        (1, 1, 0): 0.20,
        (1, 1, 1): 0.05,
    }


def _fine_support():
    return tuple(itertools.product((0, 1), repeat=3))


def _aggregation_three_nodes():
    return {0: "A", 1: "A", 2: "B"}


def _lossless_aggregate_map():
    pair_states = tuple(itertools.product((0, 1), repeat=2))
    return aggregation_compatible_coarse_map(
        _fine_support(),
        (0, 1, 2),
        ("A", "B"),
        _aggregation_three_nodes(),
        {
            "A": {state: state for state in pair_states},
            "B": {(0,): 0, (1,): 1},
        },
    )


def _lossless_decoder(coarse_map):
    return {coarse: {fine: 1.0} for fine, coarse in coarse_map.items()}


def test_lossless_node_aggregation_preserves_partition_irreducibility():
    distribution = _three_bit_distribution()
    coarse_map = _lossless_aggregate_map()
    certificate = node_aggregation_partition_certificate(
        distribution,
        (0, 1, 2),
        ((0, 1), (2,)),
        _aggregation_three_nodes(),
        ("A", "B"),
        coarse_map,
        _lossless_decoder(coarse_map),
    )

    assert certificate.product_commutation_error < 1e-12
    assert abs(
        certificate.fine_irreducibility - certificate.coarse_irreducibility
    ) < 1e-12
    assert certificate.additive_loss_bound < 1e-12
    assert certificate.exact_preservation_certified


def test_information_destroying_aggregate_can_erase_irreducibility():
    distribution = _three_bit_distribution()
    coarse_map = aggregation_compatible_coarse_map(
        _fine_support(),
        (0, 1, 2),
        ("A", "B"),
        _aggregation_three_nodes(),
        {
            "A": {state: "*" for state in itertools.product((0, 1), repeat=2)},
            "B": {(0,): 0, (1,): 1},
        },
    )
    decoder = {
        ("*", 0): {
            (0, 0, 0): 0.25,
            (0, 1, 0): 0.25,
            (1, 0, 0): 0.25,
            (1, 1, 0): 0.25,
        },
        ("*", 1): {
            (0, 0, 1): 0.25,
            (0, 1, 1): 0.25,
            (1, 0, 1): 0.25,
            (1, 1, 1): 0.25,
        },
    }
    certificate = node_aggregation_partition_certificate(
        distribution,
        (0, 1, 2),
        ((0, 1), (2,)),
        _aggregation_three_nodes(),
        ("A", "B"),
        coarse_map,
        decoder,
    )

    assert certificate.fine_irreducibility > 0.0
    assert certificate.coarse_irreducibility < 1e-12
    loss = certificate.fine_irreducibility - certificate.coarse_irreducibility
    assert loss <= certificate.additive_loss_bound + 1e-12


def test_certificate_rejects_partition_that_splits_aggregation_fiber():
    distribution = _three_bit_distribution()
    coarse_map = _lossless_aggregate_map()
    with pytest.raises(ValueError, match="no coarse descent"):
        node_aggregation_partition_certificate(
            distribution,
            (0, 1, 2),
            ((0,), (1, 2)),
            _aggregation_three_nodes(),
            ("A", "B"),
            coarse_map,
            _lossless_decoder(coarse_map),
        )


def test_coarse_map_requires_surjective_node_aggregation():
    with pytest.raises(ValueError, match="surjective"):
        aggregation_compatible_coarse_map(
            _fine_support(),
            (0, 1, 2),
            ("A", "B", "C"),
            _aggregation_three_nodes(),
            {
                "A": {state: state for state in itertools.product((0, 1), repeat=2)},
                "B": {(0,): 0, (1,): 1},
                "C": {(0,): 0},
            },
        )
