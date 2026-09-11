from fractions import Fraction
from pathlib import Path

import pytest

from consciousness_bridge.joint_statistical_computational_power import (
    certified_joint_power_margin,
    certified_three_way_full_law_decision,
    joint_linf_required_population_separation,
    numerical_joint_power_plan,
    sufficient_joint_linf_sample_size,
)


def test_three_way_decision_rejects_only_with_strict_certified_separation() -> None:
    rejected = certified_three_way_full_law_decision(
        distance_lower_bound=Fraction(21, 100),
        candidate_distance_upper_bound=Fraction(23, 100),
        rejection_radius_upper=Fraction(1, 5),
    )
    assert rejected.status == "reject"

    boundary = certified_three_way_full_law_decision(
        distance_lower_bound=Fraction(1, 5),
        candidate_distance_upper_bound=Fraction(23, 100),
        rejection_radius_upper=Fraction(1, 5),
    )
    assert boundary.status == "unresolved"


def test_three_way_decision_can_supply_explicit_overlap_witness() -> None:
    overlap = certified_three_way_full_law_decision(
        distance_lower_bound=Fraction(3, 20),
        candidate_distance_upper_bound=Fraction(1, 5),
        rejection_radius_upper=Fraction(1, 5),
    )
    assert overlap.status == "overlap_witness"
    assert "closed P77 confidence ball" in overlap.conclusion

    unresolved = certified_three_way_full_law_decision(
        distance_lower_bound=Fraction(3, 20),
        candidate_distance_upper_bound=Fraction(21, 100),
        rejection_radius_upper=Fraction(1, 5),
    )
    assert unresolved.status == "unresolved"


def test_exact_joint_power_margin_uses_strict_sum_of_three_error_budgets() -> None:
    certificate = certified_joint_power_margin(
        population_separation_lower=Fraction(1, 4),
        rejection_radius_upper=Fraction(2, 25),
        alternative_radius_upper=Fraction(7, 100),
        optimization_gap_upper=Fraction(1, 50),
    )
    assert certificate.required_separation == Fraction(17, 100)
    assert certificate.slack == Fraction(2, 25)
    assert certificate.certified

    equality = certified_joint_power_margin(
        population_separation_lower=Fraction(17, 100),
        rejection_radius_upper=Fraction(2, 25),
        alternative_radius_upper=Fraction(7, 100),
        optimization_gap_upper=Fraction(1, 50),
    )
    assert equality.slack == 0
    assert not equality.certified


def test_joint_sample_size_matches_alpha_beta_mesh_margin_example() -> None:
    sample_size = sufficient_joint_linf_sample_size(
        population_separation_margin=0.20,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.02,
    )
    assert sample_size == 355

    required_at_n = joint_linf_required_population_separation(
        sample_size=sample_size,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.02,
    )
    required_before = joint_linf_required_population_separation(
        sample_size=sample_size - 1,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.02,
    )
    assert required_at_n < 0.20
    assert required_before >= 0.20


def test_optimization_gap_consumes_power_budget_and_increases_sample_burden() -> None:
    exact_optimization = sufficient_joint_linf_sample_size(
        population_separation_margin=0.20,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.0,
    )
    approximate_optimization = sufficient_joint_linf_sample_size(
        population_separation_margin=0.20,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.02,
    )
    assert approximate_optimization > exact_optimization


def test_numerical_plan_reports_declared_power_floor_and_strict_margin() -> None:
    plan = numerical_joint_power_plan(
        population_separation_margin=0.20,
        alphabet_size=16,
        alpha=0.05,
        beta=0.20,
        optimization_gap_upper=0.02,
    )
    assert plan.sample_size == 355
    assert plan.power_lower_bound == pytest.approx(0.80)
    assert plan.required_separation < plan.population_separation_margin


def test_p79_input_validation_rejects_invalid_certification_contracts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        certified_three_way_full_law_decision(
            distance_lower_bound=Fraction(3, 10),
            candidate_distance_upper_bound=Fraction(1, 5),
            rejection_radius_upper=Fraction(1, 10),
        )

    with pytest.raises(TypeError, match="Fraction"):
        certified_joint_power_margin(
            population_separation_lower=0.2,  # type: ignore[arg-type]
            rejection_radius_upper=Fraction(1, 20),
            alternative_radius_upper=Fraction(1, 20),
            optimization_gap_upper=Fraction(1, 100),
        )

    with pytest.raises(ValueError, match="smaller than"):
        sufficient_joint_linf_sample_size(
            population_separation_margin=0.20,
            alphabet_size=16,
            optimization_gap_upper=0.20,
        )

    with pytest.raises(ValueError, match="beta"):
        joint_linf_required_population_separation(
            sample_size=100,
            alphabet_size=16,
            alpha=0.05,
            beta=1.0,
        )


def test_p79_source_preserves_scientific_and_certification_boundaries() -> None:
    source = Path(
        "src/consciousness_bridge/joint_statistical_computational_power.py"
    ).read_text(encoding="utf-8")
    required = (
        "eps_alpha + eps_beta + eta",
        "planning margin Delta_0 must be prespecified or justified independently",
        "numerical Hoeffding helper below is a planning calculation, not a formal",
        "does not validate the P75 target-measurement model when rejection fails",
        "does not identify any latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in required:
        assert token in source, token
