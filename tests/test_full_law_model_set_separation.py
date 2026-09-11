from math import log
from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.full_law_model_set_separation import (
    exact_finite_family_separation_certificate,
    finite_alphabet_cell_linf_radius,
    finite_alphabet_joint_l1_radius,
    finite_model_family_distances,
    full_law_separation_certificate,
    population_model_distance_interval,
    sufficient_l1_separation_sample_size,
    sufficient_linf_separation_sample_size,
)


def test_finite_alphabet_radii_match_p76_when_k_is_sixteen() -> None:
    n = 20_000
    alpha = 0.05
    eps = finite_alphabet_cell_linf_radius(n, 16, alpha)
    delta = finite_alphabet_joint_l1_radius(n, 16, alpha)

    assert eps == pytest.approx(np.sqrt(log(32.0 / alpha) / (2.0 * n)))
    assert delta == pytest.approx(min(2.0, 16.0 * eps))


def test_finite_model_family_distances_are_exact_for_declared_finite_family() -> None:
    empirical = (0.9, 0.1)
    family = ((0.5, 0.5), (0.4, 0.6))

    linf, l1 = finite_model_family_distances(empirical, family)

    assert linf == pytest.approx(0.4)
    assert l1 == pytest.approx(0.8)


def test_exact_finite_family_certificate_rejects_when_confidence_ball_is_disjoint() -> None:
    certificate = exact_finite_family_separation_certificate(
        (0.9, 0.1),
        ((0.5, 0.5),),
        sample_size=100,
        alpha=0.05,
    )

    assert certificate.certified_incompatible
    assert certificate.certified_incompatible_linf
    assert certificate.certified_incompatible_l1
    assert "confidence-region separation" in certificate.conclusion


def test_nonrejection_remains_inconclusive() -> None:
    certificate = exact_finite_family_separation_certificate(
        (0.9, 0.1),
        ((0.5, 0.5),),
        sample_size=10,
        alpha=0.05,
    )

    assert not certificate.certified_incompatible
    assert "non-rejection is not model acceptance" in certificate.conclusion


def test_one_norm_witness_is_enough_for_rejection() -> None:
    certificate = full_law_separation_certificate(
        sample_size=1000,
        alphabet_size=16,
        alpha=0.05,
        linf_distance_lower_bound=0.2,
        l1_distance_lower_bound=0.0,
    )

    assert certificate.certified_incompatible_linf
    assert not certificate.certified_incompatible_l1
    assert certificate.certified_incompatible


def test_population_distance_interval_is_one_lipschitz_transport() -> None:
    interval = population_model_distance_interval(
        empirical_distance=0.31,
        sampling_radius=0.08,
        maximum_distance=1.0,
    )
    assert interval == pytest.approx((0.23, 0.39))

    clipped = population_model_distance_interval(
        empirical_distance=0.03,
        sampling_radius=0.08,
        maximum_distance=0.09,
    )
    assert clipped == pytest.approx((0.0, 0.09))


def test_sufficient_linf_sample_size_makes_radius_smaller_than_half_margin() -> None:
    tau = 0.12
    alpha = 0.05
    k = 16
    n = sufficient_linf_separation_sample_size(tau, k, alpha)

    assert finite_alphabet_cell_linf_radius(n, k, alpha) < tau / 2.0


def test_sufficient_l1_sample_size_makes_radius_smaller_than_half_margin() -> None:
    tau = 0.4
    alpha = 0.05
    k = 16
    n = sufficient_l1_separation_sample_size(tau, k, alpha)

    assert finite_alphabet_joint_l1_radius(n, k, alpha) < tau / 2.0


def test_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        finite_alphabet_cell_linf_radius(0, 16, 0.05)
    with pytest.raises(ValueError):
        finite_alphabet_cell_linf_radius(10, 0, 0.05)
    with pytest.raises(ValueError):
        finite_alphabet_cell_linf_radius(10, 16, 1.0)
    with pytest.raises(ValueError):
        finite_model_family_distances((0.5, 0.5), ())
    with pytest.raises(ValueError):
        full_law_separation_certificate(sample_size=10, alphabet_size=2)
    with pytest.raises(ValueError):
        population_model_distance_interval(-0.1, 0.1)
    with pytest.raises(ValueError):
        sufficient_linf_separation_sample_size(0.0, 16)
    with pytest.raises(ValueError):
        sufficient_l1_separation_sample_size(2.1, 16)


def test_p77_source_keeps_certification_boundary_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/full_law_model_set_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "certified *lower* bound",
        "upper bound on distance",
        "cannot by itself certify rejection",
        "non-rejection is not model acceptance",
        "does not identify a latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
