from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.drift_aware_stratified_sign_coherence import P95RegimeInput
from consciousness_bridge.simultaneous_candidate_family_selection import (
    P97CandidatePlan,
    certify_p97_balanced_candidate_family_95_threshold_exact,
    certify_p97_same_data_candidate_family_exact,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _point_mass_law() -> tuple[Fraction, ...]:
    return (Fraction(1),) + (Fraction(0),) * 15


def _candidate(
    name: str,
    first_law: tuple[Fraction, ...],
) -> P97CandidatePlan:
    return P97CandidatePlan(
        name=name,
        description=f"predeclared candidate {name}",
        familywise_alpha=Fraction(1, 40),
        regimes=(
            P95RegimeInput(
                name=f"{name}-a",
                empirical_law=first_law,
                sample_size=4056,
                dependence_range=1,
                alpha_budget=Fraction(1, 80),
            ),
            P95RegimeInput(
                name=f"{name}-b",
                empirical_law=_point_mass_law(),
                sample_size=4056,
                dependence_range=1,
                alpha_budget=Fraction(1, 80),
            ),
        ),
    )


def test_p97_two_candidate_two_regime_threshold_is_4045():
    threshold = certify_p97_balanced_candidate_family_95_threshold_exact(
        candidate_count=2,
        regime_count=2,
        dependence_range=1,
    )
    assert threshold.global_alpha == Fraction(1, 20)
    assert threshold.candidate_alpha_budget == Fraction(1, 40)
    assert threshold.local_alpha_budget == Fraction(1, 80)
    assert threshold.last_noncertifying_sample_size == 4044
    assert threshold.first_certifying_sample_size == 4045
    assert threshold.first_exact_replication_sample_size == 4056
    assert threshold.first_balanced_dataset_observations == 8090
    assert threshold.first_exact_balanced_dataset_observations == 8112
    target_squared = Fraction(1, 24) ** 2
    assert threshold.last_radius.squared_radius_lower >= target_squared
    assert threshold.first_radius.squared_radius_upper < target_squared


def test_p97_same_data_selection_can_choose_rejecting_candidate_after_inspection():
    certificate = certify_p97_same_data_candidate_family_exact(
        (
            _candidate("witness-plan", _witness_law()),
            _candidate("control-plan", _point_mass_law()),
        ),
        global_alpha=Fraction(1, 20),
        selected_candidate_name="witness-plan",
        candidate_family_predeclared=True,
    )
    assert certificate.candidate_count == 2
    assert certificate.allocated_candidate_alpha == Fraction(1, 20)
    assert certificate.simultaneous_confidence_lower == Fraction(19, 20)
    assert certificate.rejecting_candidates == ("witness-plan",)
    assert certificate.rejects_selected_joint_p75_null
    assert certificate.candidate_certificates[0].nested_p95_certificate.rejects_joint_p75_null
    assert not certificate.candidate_certificates[1].nested_p95_certificate.rejects_joint_p75_null


def test_p97_same_data_selection_can_choose_nonrejecting_candidate_after_inspection():
    certificate = certify_p97_same_data_candidate_family_exact(
        (
            _candidate("witness-plan", _witness_law()),
            _candidate("control-plan", _point_mass_law()),
        ),
        global_alpha=Fraction(1, 20),
        selected_candidate_name="control-plan",
        candidate_family_predeclared=True,
    )
    assert certificate.rejecting_candidates == ("witness-plan",)
    assert not certificate.rejects_selected_joint_p75_null


def test_p97_requires_predeclared_finite_family_and_exact_budget_accounting():
    candidates = (
        _candidate("a", _point_mass_law()),
        _candidate("b", _point_mass_law()),
    )
    with pytest.raises(ValueError, match="fixed before"):
        certify_p97_same_data_candidate_family_exact(
            candidates,
            global_alpha=Fraction(1, 20),
            selected_candidate_name="a",
            candidate_family_predeclared=False,
        )
    with pytest.raises(ValueError, match="predeclared candidate"):
        certify_p97_same_data_candidate_family_exact(
            candidates,
            global_alpha=Fraction(1, 20),
            selected_candidate_name="not-in-family",
            candidate_family_predeclared=True,
        )


def test_p97_rejects_candidate_alpha_overspend_and_duplicate_names():
    candidate = _candidate("same", _point_mass_law())
    with pytest.raises(ValueError, match="unique"):
        certify_p97_same_data_candidate_family_exact(
            (candidate, candidate),
            global_alpha=Fraction(1, 20),
            selected_candidate_name="same",
            candidate_family_predeclared=True,
        )

    oversized = P97CandidatePlan(
        name="large",
        description="oversized candidate budget",
        familywise_alpha=Fraction(3, 50),
        regimes=(
            P95RegimeInput(
                name="only",
                empirical_law=_point_mass_law(),
                sample_size=100,
                dependence_range=0,
                alpha_budget=Fraction(1, 100),
            ),
        ),
    )
    with pytest.raises(ValueError, match="exceed"):
        certify_p97_same_data_candidate_family_exact(
            (oversized,),
            global_alpha=Fraction(1, 20),
            selected_candidate_name="large",
            candidate_family_predeclared=True,
        )


def test_p97_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.simultaneous_candidate_family_selection",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "same data" in source
    assert "finite family" in source
    assert "multiplicity cost" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
