import pytest

from consciousness_bridge.intervention_causal_geometry import (
    aggregate_directed_influence_matrix,
    has_directed_cycle,
    partition_response_irreducibility,
    productized_partition_distribution,
    relabel_joint_responses,
    response_diameter,
    response_geometry,
)


def _correlated_responses():
    return {
        "base": {
            "early": {("0", "0"): 0.80, ("1", "1"): 0.20},
            "late": {("0", "0"): 0.70, ("1", "1"): 0.30},
        },
        "push0": {
            "early": {("0", "0"): 0.20, ("1", "1"): 0.80},
            "late": {("0", "0"): 0.35, ("1", "1"): 0.65},
        },
        "push1": {
            "early": {("0", "0"): 0.30, ("1", "1"): 0.70},
            "late": {("0", "0"): 0.40, ("1", "1"): 0.60},
        },
    }


def test_response_geometry_is_invariant_under_bijective_outcome_relabeling():
    responses = _correlated_responses()
    relabeling = {
        ("0", "0"): ("A", "A"),
        ("0", "1"): ("A", "B"),
        ("1", "0"): ("B", "A"),
        ("1", "1"): ("B", "B"),
    }

    transformed = relabel_joint_responses(responses, relabeling)

    assert response_geometry(responses, "early") == pytest.approx(
        response_geometry(transformed, "early")
    )
    assert response_diameter(responses, "late") == pytest.approx(
        response_diameter(transformed, "late")
    )


def test_correlated_joint_response_has_positive_partition_irreducibility():
    value = partition_response_irreducibility(
        _correlated_responses(),
        partition=((0,), (1,)),
        delay="early",
    )

    assert value > 0.0


def test_independent_joint_response_factorizes_exactly():
    distribution = {
        ("0", "0"): 0.25,
        ("0", "1"): 0.25,
        ("1", "0"): 0.25,
        ("1", "1"): 0.25,
    }
    productized = productized_partition_distribution(
        distribution,
        partition=((0,), (1,)),
    )
    responses = {"base": {"early": distribution}}

    assert productized == pytest.approx(distribution)
    assert partition_response_irreducibility(
        responses,
        partition=((0,), (1,)),
        delay="early",
    ) == pytest.approx(0.0)


def test_feedforward_influence_graph_has_no_return_cycle():
    responses = {
        "base": {"t1": {("0", "0"): 1.0}},
        "flip0": {"t1": {("1", "1"): 1.0}},
        "flip1": {"t1": {("0", "1"): 1.0}},
    }
    source_pairs = {
        0: (("base", "flip0"),),
        1: (("base", "flip1"),),
    }

    matrix = aggregate_directed_influence_matrix(
        responses,
        source_pairs,
        delays=("t1",),
        block_count=2,
    )

    assert matrix[0][1] == pytest.approx(1.0)
    assert matrix[1][0] == pytest.approx(0.0)
    assert not has_directed_cycle(matrix)


def test_recurrent_influence_graph_contains_return_cycle():
    responses = {
        "base": {"t1": {("0", "0"): 1.0}},
        "flip0": {"t1": {("1", "1"): 1.0}},
        "flip1": {"t1": {("1", "1"): 1.0}},
    }
    source_pairs = {
        0: (("base", "flip0"),),
        1: (("base", "flip1"),),
    }

    matrix = aggregate_directed_influence_matrix(
        responses,
        source_pairs,
        delays=("t1",),
        block_count=2,
    )

    assert matrix[0][1] == pytest.approx(1.0)
    assert matrix[1][0] == pytest.approx(1.0)
    assert has_directed_cycle(matrix)


def test_partition_must_cover_every_block_exactly_once():
    distribution = {
        ("0", "0"): 0.5,
        ("1", "1"): 0.5,
    }

    with pytest.raises(ValueError):
        productized_partition_distribution(distribution, partition=((0,), (0, 1)))
