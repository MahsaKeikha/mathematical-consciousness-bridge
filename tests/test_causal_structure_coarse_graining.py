import pytest

from consciousness_bridge.causal_structure_coarse_graining import (
    collapsed_fiber_witness,
    is_injective_on_observed_support,
    pushforward_distribution,
    pushforward_response_table,
    pushforward_tv_pair,
)


def test_pushforward_distribution_aggregates_fine_states():
    distribution = {"a": 0.2, "b": 0.3, "c": 0.5}
    coarse_map = {"a": "x", "b": "x", "c": "y"}

    assert pushforward_distribution(distribution, coarse_map) == pytest.approx(
        {"x": 0.5, "y": 0.5}
    )


def test_total_variation_contracts_under_many_to_one_coarse_graining():
    first = {"a": 1.0}
    second = {"b": 1.0}
    coarse_map = {"a": "x", "b": "x"}

    fine, coarse = pushforward_tv_pair(first, second, coarse_map)

    assert fine == pytest.approx(1.0)
    assert coarse == pytest.approx(0.0)
    assert coarse <= fine


def test_bijective_relabeling_preserves_total_variation():
    first = {"a": 0.8, "b": 0.2}
    second = {"a": 0.3, "b": 0.7}
    relabeling = {"a": "left", "b": "right"}

    fine, coarse = pushforward_tv_pair(first, second, relabeling)

    assert fine == pytest.approx(0.5)
    assert coarse == pytest.approx(fine)


def test_response_geometry_can_collapse_after_coarse_graining():
    responses = {
        "u0": {0: {"a": 1.0}},
        "u1": {0: {"b": 1.0}},
    }
    coarse_map = {"a": "x", "b": "x"}

    coarse = pushforward_response_table(responses, coarse_map)

    assert coarse["u0"][0] == pytest.approx({"x": 1.0})
    assert coarse["u1"][0] == pytest.approx({"x": 1.0})


def test_noninjective_map_returns_collapsed_fiber_witness():
    coarse_map = {"a": "x", "b": "x", "c": "y"}
    witness = collapsed_fiber_witness(coarse_map)

    assert witness is not None
    assert witness[0] != witness[1]
    assert coarse_map[witness[0]] == coarse_map[witness[1]]


def test_injectivity_is_checked_on_declared_support():
    coarse_map = {"a": "x", "b": "x", "c": "y"}

    assert is_injective_on_observed_support(coarse_map, {"a", "c"})
    assert not is_injective_on_observed_support(coarse_map, {"a", "b"})


def test_missing_coarse_map_entries_are_rejected():
    with pytest.raises(ValueError):
        pushforward_distribution({"a": 1.0}, {})
    with pytest.raises(ValueError):
        is_injective_on_observed_support({"a": "x"}, {"a", "b"})
