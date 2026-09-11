from math import log

import pytest

from consciousness_bridge.fundamental_physical_sufficiency import (
    factorization_collisions,
)
from consciousness_bridge.target_provenance_noncircularity import (
    deterministic_descriptor_target_certificate,
    independently_declared_target_residual,
    stochastic_descriptor_channel_certificate,
)


def test_descriptor_derived_target_is_vacuous_by_construction() -> None:
    omega = (0, 1, 2, 3)
    physical = (0, 1, 0, 1)
    rule = {0: "quiet", 1: "active"}

    result = deterministic_descriptor_target_certificate(omega, physical, rule)

    assert result.target_labels == ("quiet", "active", "quiet", "active")
    assert result.induced_bridge_map == rule
    assert result.factorization_collisions == ()
    assert result.conditional_mutual_information_nats == 0.0
    assert result.structurally_vacuous


def test_independently_declared_synthetic_target_can_expose_a_fiber_collision() -> None:
    omega = (0, 1, 2, 3)
    physical = (0, 1, 0, 1)
    target = (0, 0, 1, 1)

    collisions = factorization_collisions(physical, target)
    residual = independently_declared_target_residual(omega, physical, target)

    assert collisions == [(0, 2), (1, 3)]
    assert residual == pytest.approx(log(2.0))


def test_fixed_learned_rule_still_factors_through_descriptor() -> None:
    omega = ("test-a", "test-b", "test-c", "test-d")
    physical = ("L", "R", "L", "R")
    learned_rule_from_training_artifact = {"L": 0, "R": 1}

    result = deterministic_descriptor_target_certificate(
        omega,
        physical,
        learned_rule_from_training_artifact,
    )

    assert result.induced_bridge_map == learned_rule_from_training_artifact
    assert result.conditional_mutual_information_nats == 0.0
    assert result.structurally_vacuous


def test_descriptor_only_stochastic_channel_has_zero_conditional_residual() -> None:
    state_descriptor_weights = {
        ("omega-0", "A"): 1.0,
        ("omega-1", "A"): 3.0,
        ("omega-2", "B"): 2.0,
        ("omega-3", "B"): 4.0,
    }
    target_channel_weights = {
        ("A", "no"): 3.0,
        ("A", "yes"): 1.0,
        ("B", "no"): 1.0,
        ("B", "yes"): 4.0,
    }

    result = stochastic_descriptor_channel_certificate(
        state_descriptor_weights,
        target_channel_weights,
    )

    assert result.conditional_mutual_information_nats == 0.0
    assert result.structurally_screened_off
    assert sum(result.joint_distribution.values()) == pytest.approx(1.0)


def test_separately_supplied_target_residual_does_not_claim_provenance() -> None:
    omega = (0, 1, 2, 3)
    physical = (0, 1, 0, 1)
    target = (0, 0, 1, 1)

    residual = independently_declared_target_residual(omega, physical, target)

    assert residual > 0.0


def test_deterministic_constructor_rejects_missing_rule_value() -> None:
    with pytest.raises(ValueError, match="every observed physical label"):
        deterministic_descriptor_target_certificate(
            (0, 1),
            ("A", "B"),
            {"A": 0},
        )


def test_stochastic_constructor_requires_channel_for_every_observed_descriptor() -> None:
    with pytest.raises(ValueError, match="every observed descriptor"):
        stochastic_descriptor_channel_certificate(
            {(0, "A"): 1.0, (1, "B"): 1.0},
            {("A", 0): 1.0},
        )


def test_label_sequences_must_align() -> None:
    with pytest.raises(ValueError, match="equal length"):
        independently_declared_target_residual((0, 1), (0,), (0, 1))
