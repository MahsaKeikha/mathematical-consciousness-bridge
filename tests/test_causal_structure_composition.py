import pytest

from consciousness_bridge.causal_structure_composition import (
    compose_independent_response_tables,
    composed_response_distance_bounds,
    coupling_defect,
    maximum_response_factorization_defect,
    response_factorization_defect_direct,
    subsystem_partition,
    tensor_product_distribution,
)
from consciousness_bridge.intervention_causal_structure import (
    directed_influence_matrix,
    response_distance,
)


def _left_responses():
    return {
        "a0": {0: {(0,): 1.0}},
        "a1": {0: {(1,): 1.0}},
    }


def _right_responses():
    return {
        "b0": {0: {(0,): 0.75, (1,): 0.25}},
        "b1": {0: {(0,): 0.25, (1,): 0.75}},
    }


def test_tensor_product_distribution_forms_normalized_concatenated_law():
    result = tensor_product_distribution(
        {(0,): 0.25, (1,): 0.75},
        {("x",): 0.4, ("y",): 0.6},
    )
    assert sum(result.values()) == pytest.approx(1.0)
    assert result[(0, "x")] == pytest.approx(0.1)
    assert result[(1, "y")] == pytest.approx(0.45)


def test_independent_composition_has_zero_subsystem_partition_defect():
    composed = compose_independent_response_tables(_left_responses(), _right_responses())
    assert coupling_defect(composed, 1, 1, 0) == pytest.approx(0.0)
    assert maximum_response_factorization_defect(composed, 1, 1, 0) == pytest.approx(
        0.0
    )


def test_one_factor_intervention_distance_is_preserved_exactly():
    composed = compose_independent_response_tables(_left_responses(), _right_responses())
    left_distance = response_distance(_left_responses(), "a0", "a1", 0)
    joint_distance = response_distance(composed, ("a0", "b0"), ("a1", "b0"), 0)
    assert joint_distance == pytest.approx(left_distance)


def test_composed_response_distance_lies_between_theorem_bounds():
    left = {
        "a0": {0: {(0,): 0.8, (1,): 0.2}},
        "a1": {0: {(0,): 0.3, (1,): 0.7}},
    }
    right = _right_responses()
    composed = compose_independent_response_tables(left, right)

    d_left = response_distance(left, "a0", "a1", 0)
    d_right = response_distance(right, "b0", "b1", 0)
    d_joint = response_distance(composed, ("a0", "b0"), ("a1", "b1"), 0)
    lower, upper = composed_response_distance_bounds(d_left, d_right)

    assert lower <= d_joint <= upper
    assert lower == pytest.approx(0.5)
    assert upper == pytest.approx(0.75)


def test_independent_composition_has_zero_cross_system_directed_influence():
    composed = compose_independent_response_tables(_left_responses(), _right_responses())
    source_pairs = {
        0: ((('a0', 'b0'), ('a1', 'b0')),),
        1: ((('a0', 'b0'), ('a0', 'b1')),),
    }
    matrix = directed_influence_matrix(composed, source_pairs, 0, block_count=2)

    assert matrix[0][1] == pytest.approx(0.0)
    assert matrix[1][0] == pytest.approx(0.0)
    assert matrix[0][0] > 0.0
    assert matrix[1][1] > 0.0


def test_correlated_joint_response_has_positive_coupling_defect():
    correlated = {(0, 0): 0.5, (1, 1): 0.5}
    defect = response_factorization_defect_direct(correlated, 1, 1)
    assert defect == pytest.approx(0.5)


def test_subsystem_partition_uses_disjoint_contiguous_blocks():
    assert subsystem_partition(2, 3) == ((0, 1), (2, 3, 4))


def test_invalid_composition_inputs_are_rejected():
    with pytest.raises(ValueError):
        compose_independent_response_tables({}, _right_responses())
    with pytest.raises(ValueError):
        composed_response_distance_bounds(-0.1, 0.2)
    with pytest.raises(ValueError):
        subsystem_partition(0, 1)
    with pytest.raises(ValueError):
        response_factorization_defect_direct({(0, 0): 1.0}, 1, 2)
