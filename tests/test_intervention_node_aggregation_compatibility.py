import itertools

import pytest

from consciousness_bridge.intervention_node_aggregation_compatibility import (
    aggregated_directed_influence_certificate,
    descend_source_pairs,
    pair_source_images,
    source_pair_families_are_aggregation_compatible,
)

FINE_NODES = (0, 1, 2)
COARSE_NODES = ("A", "B")
AGGREGATION = {0: "A", 1: "A", 2: "B"}
DELAY = "t1"


def _distribution(p0: float, p1: float, p2: float):
    distribution = {}
    for outcome in itertools.product((0, 1), repeat=3):
        probability = 1.0
        for value, parameter in zip(outcome, (p0, p1, p2), strict=True):
            probability *= parameter if value else 1.0 - parameter
        distribution[outcome] = probability
    return distribution


def _responses():
    return {
        "baseline": {DELAY: _distribution(0.2, 0.3, 0.2)},
        "stim0": {DELAY: _distribution(0.8, 0.3, 0.7)},
        "stim1": {DELAY: _distribution(0.2, 0.8, 0.6)},
        "stim2": {DELAY: _distribution(0.2, 0.3, 0.9)},
    }


def _source_pairs():
    return {
        0: (("baseline", "stim0"),),
        1: (("baseline", "stim1"),),
        2: (("baseline", "stim2"),),
    }


def test_pair_source_images_records_aggregate_source_labels():
    images = pair_source_images(_source_pairs(), AGGREGATION)
    assert images[("baseline", "stim0")] == frozenset({"A"})
    assert images[("baseline", "stim1")] == frozenset({"A"})
    assert images[("baseline", "stim2")] == frozenset({"B"})


def test_source_pair_families_descend_by_fiber_union():
    assert source_pair_families_are_aggregation_compatible(
        _source_pairs(),
        AGGREGATION,
    )
    descended = descend_source_pairs(
        FINE_NODES,
        COARSE_NODES,
        AGGREGATION,
        _source_pairs(),
    )
    assert descended["A"] == (
        ("baseline", "stim0"),
        ("baseline", "stim1"),
    )
    assert descended["B"] == (("baseline", "stim2"),)


def test_same_pair_may_be_shared_inside_one_aggregate_source():
    pairs = {
        0: (("baseline", "stim0"),),
        1: (("baseline", "stim0"),),
        2: (("baseline", "stim2"),),
    }
    assert source_pair_families_are_aggregation_compatible(pairs, AGGREGATION)
    descended = descend_source_pairs(
        FINE_NODES,
        COARSE_NODES,
        AGGREGATION,
        pairs,
    )
    assert descended["A"] == (("baseline", "stim0"),)


def test_pair_crossing_aggregate_source_labels_is_rejected():
    pairs = {
        0: (("baseline", "stim0"),),
        2: (("baseline", "stim0"),),
    }
    assert not source_pair_families_are_aggregation_compatible(pairs, AGGREGATION)
    with pytest.raises(ValueError, match="different aggregate-source fibers"):
        descend_source_pairs(
            FINE_NODES,
            COARSE_NODES,
            AGGREGATION,
            pairs,
        )


def test_lossless_target_block_aggregation_preserves_influence():
    target_state_map = {(0,): 0, (1,): 1}
    decoder = {0: {(0,): 1.0}, 1: {(1,): 1.0}}
    certificate = aggregated_directed_influence_certificate(
        _responses(),
        _source_pairs(),
        fine_nodes=FINE_NODES,
        coarse_nodes=COARSE_NODES,
        aggregation=AGGREGATION,
        coarse_source="A",
        coarse_target="B",
        delay=DELAY,
        target_state_map=target_state_map,
        target_decoder=decoder,
        threshold=0.2,
    )
    assert certificate.pair_count == 2
    assert certificate.fine_block_influence > 0.0
    assert abs(
        certificate.fine_block_influence - certificate.coarse_influence
    ) < 1e-12
    assert certificate.reconstruction_defect < 1e-12
    assert certificate.edge_preservation_certified


def test_lossy_target_aggregation_obeys_p18_bound():
    target_state_map = {(0,): "*", (1,): "*"}
    decoder = {"*": {(0,): 0.5, (1,): 0.5}}
    certificate = aggregated_directed_influence_certificate(
        _responses(),
        _source_pairs(),
        fine_nodes=FINE_NODES,
        coarse_nodes=COARSE_NODES,
        aggregation=AGGREGATION,
        coarse_source="A",
        coarse_target="B",
        delay=DELAY,
        target_state_map=target_state_map,
        target_decoder=decoder,
    )
    assert certificate.fine_block_influence > 0.0
    assert certificate.coarse_influence < 1e-12
    loss = certificate.fine_block_influence - certificate.coarse_influence
    assert loss <= certificate.distortion_bound + 1e-12


def test_coarse_source_pool_can_exceed_each_named_constituent_pair_only_by_supremum():
    certificate = aggregated_directed_influence_certificate(
        _responses(),
        _source_pairs(),
        fine_nodes=FINE_NODES,
        coarse_nodes=COARSE_NODES,
        aggregation=AGGREGATION,
        coarse_source="A",
        coarse_target="B",
        delay=DELAY,
        target_state_map={(0,): 0, (1,): 1},
        target_decoder={0: {(0,): 1.0}, 1: {(1,): 1.0}},
    )
    # Aggregate-source influence is the maximum over the inherited pair family.
    # It is not a new simultaneous perturbation of fine sources 0 and 1.
    assert certificate.pair_count == 2
    assert certificate.fine_block_influence == pytest.approx(0.5)


def test_missing_source_response_is_rejected():
    responses = _responses()
    pairs = {0: (("baseline", "missing",),)}
    with pytest.raises(ValueError, match="declared response"):
        aggregated_directed_influence_certificate(
            responses,
            pairs,
            fine_nodes=FINE_NODES,
            coarse_nodes=COARSE_NODES,
            aggregation=AGGREGATION,
            coarse_source="A",
            coarse_target="B",
            delay=DELAY,
            target_state_map={(0,): 0, (1,): 1},
            target_decoder={0: {(0,): 1.0}, 1: {(1,): 1.0}},
        )


def test_non_surjective_node_map_is_rejected():
    with pytest.raises(ValueError, match="surjective"):
        descend_source_pairs(
            FINE_NODES,
            ("A", "B", "C"),
            AGGREGATION,
            _source_pairs(),
        )
