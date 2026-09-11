import numpy as np
import pytest

from consciousness_bridge.bounded_target_view_dependence import (
    bounded_dependence_rejection_certificate,
    conditional_dependence_defect,
    conditionally_independent_counterpart,
    observed_distance_to_independent_counterpart,
    observed_mixture_law,
    product_projection_from_conditional_law,
    weighted_conditional_dependence_budget,
)


def _independent_law(probabilities_one: tuple[float, float, float, float]) -> np.ndarray:
    law = []
    for x1 in (0, 1):
        for x2 in (0, 1):
            for x3 in (0, 1):
                for x4 in (0, 1):
                    mass = 1.0
                    for value, probability_one in zip(
                        (x1, x2, x3, x4), probabilities_one, strict=True
                    ):
                        mass *= probability_one if value else 1.0 - probability_one
                    law.append(mass)
    return np.asarray(law, dtype=float)


def _dependent_pair_law() -> np.ndarray:
    """X1=X2 exactly, with X3 and X4 fair and independent."""

    law = np.zeros(16, dtype=float)
    index = 0
    for x1 in (0, 1):
        for x2 in (0, 1):
            for x3 in (0, 1):
                for x4 in (0, 1):
                    if x1 == x2:
                        law[index] = 1.0 / 8.0
                    index += 1
    return law


def test_product_projection_is_identity_for_independent_law() -> None:
    law = _independent_law((0.2, 0.4, 0.7, 0.8))
    projection = product_projection_from_conditional_law(law)
    assert np.allclose(projection, law)
    assert conditional_dependence_defect(law, metric="linf") == pytest.approx(0.0)
    assert conditional_dependence_defect(law, metric="l1") == pytest.approx(0.0)


def test_dependent_pair_has_positive_local_dependence_defect() -> None:
    law = _dependent_pair_law()
    projection = product_projection_from_conditional_law(law)
    assert np.isclose(projection.sum(), 1.0)
    assert conditional_dependence_defect(law, metric="linf") > 0.0
    assert conditional_dependence_defect(law, metric="l1") > 0.0


def test_weighted_defect_bounds_observed_distance_to_p75_counterpart() -> None:
    minus = _dependent_pair_law()
    plus = _independent_law((0.7, 0.6, 0.4, 0.3))
    prevalence = 0.35

    for metric in ("linf", "l1"):
        observed_distance = observed_distance_to_independent_counterpart(
            prevalence,
            minus,
            plus,
            metric=metric,
        )
        budget = weighted_conditional_dependence_budget(
            prevalence,
            minus,
            plus,
            metric=metric,
        )
        assert observed_distance <= budget + 1e-12


def test_constructed_counterpart_is_a_probability_law() -> None:
    minus = _dependent_pair_law()
    plus = _dependent_pair_law()[::-1]
    counterpart = conditionally_independent_counterpart(0.4, minus, plus)
    observed = observed_mixture_law(0.4, minus, plus)

    assert np.all(counterpart >= 0.0)
    assert np.all(observed >= 0.0)
    assert counterpart.sum() == pytest.approx(1.0)
    assert observed.sum() == pytest.approx(1.0)


def test_robust_rejection_requires_distance_beyond_sampling_plus_dependence() -> None:
    certificate = bounded_dependence_rejection_certificate(
        model_distance_lower_bound=0.12,
        sampling_radius_upper_bound=0.03,
        dependence_budget=0.05,
        metric="linf",
    )
    assert certificate.required_threshold == pytest.approx(0.08)
    assert certificate.excess_margin == pytest.approx(0.04)
    assert certificate.certified_incompatible
    assert "dependence allowance" in certificate.conclusion


def test_equality_at_robust_threshold_is_not_rejection() -> None:
    certificate = bounded_dependence_rejection_certificate(
        model_distance_lower_bound=0.08,
        sampling_radius_upper_bound=0.03,
        dependence_budget=0.05,
        metric="linf",
    )
    assert not certificate.certified_incompatible
    assert certificate.excess_margin == pytest.approx(0.0)
    assert "not model validation" in certificate.conclusion


def test_l1_robust_rejection_uses_same_direction() -> None:
    certificate = bounded_dependence_rejection_certificate(
        model_distance_lower_bound=0.45,
        sampling_radius_upper_bound=0.15,
        dependence_budget=0.20,
        metric="l1",
    )
    assert certificate.certified_incompatible
    assert certificate.excess_margin == pytest.approx(0.10)


@pytest.mark.parametrize("metric", ["linf", "l1"])
def test_exact_observed_distance_never_exceeds_weighted_defect(metric: str) -> None:
    minus = np.zeros(16, dtype=float)
    minus[[0, 15]] = 0.5
    plus = _independent_law((0.1, 0.3, 0.6, 0.9))
    prevalence = 0.6

    actual = observed_distance_to_independent_counterpart(
        prevalence,
        minus,
        plus,
        metric=metric,
    )
    bound = weighted_conditional_dependence_budget(
        prevalence,
        minus,
        plus,
        metric=metric,
    )
    assert actual <= bound + 1e-12


def test_validation_errors_are_explicit() -> None:
    with pytest.raises(ValueError, match="sixteen"):
        product_projection_from_conditional_law([1.0, 0.0])
    with pytest.raises(ValueError, match="nonnegative"):
        product_projection_from_conditional_law([1.0] + [-0.1] + [0.0] * 14)
    with pytest.raises(ValueError, match="\[0, 1\]"):
        observed_mixture_law(1.2, [1.0] + [0.0] * 15, [1.0] + [0.0] * 15)
    with pytest.raises(ValueError, match="metric"):
        conditional_dependence_defect([1.0] + [0.0] * 15, metric="tv")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="nonnegative"):
        bounded_dependence_rejection_certificate(
            model_distance_lower_bound=-0.1,
            sampling_radius_upper_bound=0.01,
            dependence_budget=0.01,
        )
