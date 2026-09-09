import itertools

import pytest

from consciousness_bridge.response_geometry_node_aggregation import (
    declared_response_family,
    geometry_threshold_preserved,
    response_geometry_distortion,
    response_geometry_node_aggregation_certificate,
    response_geometry_over_grid,
)

FINE_NODES = (0, 1, 2)
COARSE_NODES = ("A", "B")
AGGREGATION = {0: "A", 1: "A", 2: "B"}
INTERVENTIONS = ("u0", "u1", "u2")
DELAYS = ("t1", "t2")


def _product_distribution(parameters):
    result = {}
    for outcome in itertools.product((0, 1), repeat=3):
        probability = 1.0
        for value, parameter in zip(outcome, parameters, strict=True):
            probability *= parameter if value else 1.0 - parameter
        result[outcome] = probability
    return result


def _responses():
    return {
        "u0": {
            "t1": _product_distribution((0.2, 0.3, 0.2)),
            "t2": _product_distribution((0.3, 0.4, 0.3)),
        },
        "u1": {
            "t1": _product_distribution((0.7, 0.3, 0.6)),
            "t2": _product_distribution((0.6, 0.4, 0.5)),
        },
        "u2": {
            "t1": _product_distribution((0.2, 0.8, 0.8)),
            "t2": _product_distribution((0.3, 0.7, 0.7)),
        },
    }


def _lossless_aggregate_maps():
    return {
        "A": {state: state for state in itertools.product((0, 1), repeat=2)},
        "B": {(0,): 0, (1,): 1},
    }


def _lossless_decoder():
    decoder = {}
    for fine in itertools.product((0, 1), repeat=3):
        coarse = ((fine[0], fine[1]), fine[2])
        decoder[coarse] = {fine: 1.0}
    return decoder


def test_declared_family_requires_complete_intervention_delay_grid():
    responses = _responses()
    del responses["u2"]["t2"]
    with pytest.raises(ValueError, match="intervention-delay cell"):
        declared_response_family(responses, INTERVENTIONS, DELAYS)


def test_geometry_contains_every_intervention_pair_at_every_delay():
    family = declared_response_family(_responses(), INTERVENTIONS, DELAYS)
    geometry = response_geometry_over_grid(family, INTERVENTIONS, DELAYS)
    assert len(geometry) == 6
    assert set(key[2] for key in geometry) == set(DELAYS)


def test_lossless_node_aggregation_preserves_complete_response_geometry():
    certificate = response_geometry_node_aggregation_certificate(
        _responses(),
        interventions=INTERVENTIONS,
        delays=DELAYS,
        fine_nodes=FINE_NODES,
        coarse_nodes=COARSE_NODES,
        aggregation=AGGREGATION,
        aggregate_maps=_lossless_aggregate_maps(),
        decoder=_lossless_decoder(),
    )
    assert certificate.pair_count == 3
    assert certificate.delay_count == 2
    assert certificate.max_geometry_loss < 1e-12
    assert certificate.reconstruction_defect < 1e-12
    assert certificate.fine_diameter == pytest.approx(certificate.coarse_diameter)
    assert certificate.exact_geometry_preservation_certified


def test_information_destroying_node_aggregation_contracts_geometry():
    aggregate_maps = {
        "A": {state: "*" for state in itertools.product((0, 1), repeat=2)},
        "B": {(0,): 0, (1,): 1},
    }
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
    certificate = response_geometry_node_aggregation_certificate(
        _responses(),
        interventions=INTERVENTIONS,
        delays=DELAYS,
        fine_nodes=FINE_NODES,
        coarse_nodes=COARSE_NODES,
        aggregation=AGGREGATION,
        aggregate_maps=aggregate_maps,
        decoder=decoder,
    )
    assert certificate.max_geometry_loss > 0.0
    assert certificate.coarse_diameter <= certificate.fine_diameter + 1e-12
    assert certificate.max_geometry_loss <= certificate.uniform_distortion_bound + 1e-12


def test_geometry_distortion_rejects_mismatched_index_sets():
    with pytest.raises(ValueError, match="same indexed grid"):
        response_geometry_distortion(
            {("u0", "u1", "t1"): 0.2},
            {("u0", "u2", "t1"): 0.1},
        )


def test_threshold_certificate_uses_two_reconstruction_defects():
    assert geometry_threshold_preserved(0.7, 0.1, 0.4)
    assert not geometry_threshold_preserved(0.5, 0.1, 0.4)


def test_threshold_certificate_rejects_invalid_probability_scale_values():
    with pytest.raises(ValueError, match="threshold"):
        geometry_threshold_preserved(0.5, 0.1, 1.1)


def test_duplicate_intervention_labels_are_rejected():
    with pytest.raises(ValueError, match="Intervention labels must be unique"):
        declared_response_family(_responses(), ("u0", "u0"), DELAYS)


def test_duplicate_delay_labels_are_rejected():
    with pytest.raises(ValueError, match="Delay labels must be unique"):
        declared_response_family(_responses(), INTERVENTIONS, ("t1", "t1"))
