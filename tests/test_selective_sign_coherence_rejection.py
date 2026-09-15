from fractions import Fraction

import pytest

from consciousness_bridge.certified_sampling_radius import (
    certified_finite_alphabet_sampling_radius,
)
from consciousness_bridge.selective_sign_coherence_rejection import (
    certify_p93_selective_sign_coherence_rejection,
    p93_selected_cells_exact,
    p93_uniform_alpha_allocation,
    p93_witness_alpha_allocation_95,
)

COUNTS = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
EMPIRICAL_LAW = tuple(Fraction(count, 24) for count in COUNTS)
ALPHA_95 = Fraction(1, 20)


def test_p93_selects_exactly_the_seven_p92_cells():
    assert p93_selected_cells_exact(EMPIRICAL_LAW) == {
        "t000": Fraction(1, 8),
        "t001": Fraction(1, 24),
        "t010": Fraction(0),
        "t011": Fraction(5, 24),
        "t100": Fraction(0),
        "t101": Fraction(1, 8),
        "t111": Fraction(1, 8),
    }


def test_p93_witness_allocation_is_fixed_positive_and_exactly_95_percent():
    allocation = p93_witness_alpha_allocation_95()
    assert set(allocation) == {
        "t000",
        "t001",
        "t010",
        "t011",
        "t100",
        "t101",
        "t111",
    }
    assert all(value > 0 for value in allocation.values())
    assert sum(allocation.values(), start=Fraction(0)) == ALPHA_95


def test_p93_refuses_rejection_for_the_actual_n24_table():
    certificate = certify_p93_selective_sign_coherence_rejection(
        EMPIRICAL_LAW,
        sample_size=24,
        alpha_total=ALPHA_95,
        alpha_allocation=p93_witness_alpha_allocation_95(),
    )
    assert certificate.empirical_determinants == (
        Fraction(-1, 48),
        Fraction(1, 64),
        Fraction(5, 192),
    )
    assert certificate.forced_signs == (0, 0, 0)
    assert not certificate.reject_p75


def test_p93_fixed_selective_allocation_certifies_replicated_witness_at_n1464():
    certificate = certify_p93_selective_sign_coherence_rejection(
        EMPIRICAL_LAW,
        sample_size=1464,
        alpha_total=ALPHA_95,
        alpha_allocation=p93_witness_alpha_allocation_95(),
    )
    assert certificate.alpha_spent == ALPHA_95
    assert certificate.forced_signs == (-1, 1, 1)
    assert certificate.reject_p75
    assert certificate.determinant_intervals[0].upper < 0
    assert certificate.determinant_intervals[1].lower > 0
    assert certificate.determinant_intervals[2].lower > 0


def test_p93_same_fixed_allocation_does_not_certify_at_n1440():
    certificate = certify_p93_selective_sign_coherence_rejection(
        EMPIRICAL_LAW,
        sample_size=1440,
        alpha_total=ALPHA_95,
        alpha_allocation=p93_witness_alpha_allocation_95(),
    )
    assert certificate.forced_signs == (0, 1, 1)
    assert not certificate.reject_p75


def test_p93_uniform_seven_cell_allocation_certifies_at_n1632():
    certificate = certify_p93_selective_sign_coherence_rejection(
        EMPIRICAL_LAW,
        sample_size=1632,
        alpha_total=ALPHA_95,
        alpha_allocation=p93_uniform_alpha_allocation(ALPHA_95),
    )
    assert certificate.forced_signs == (-1, 1, 1)
    assert certificate.reject_p75


def test_p93_selective_certificate_beats_full_sixteen_cell_p77_radius_at_n1464():
    full_radius = certified_finite_alphabet_sampling_radius(
        sample_size=1464,
        alphabet_size=16,
        alpha=ALPHA_95,
        series_terms=16,
        sqrt_bits=64,
    )
    assert full_radius.cell_linf_radius_lower > Fraction(1, 24)

    full_radius_at_1872 = certified_finite_alphabet_sampling_radius(
        sample_size=1872,
        alphabet_size=16,
        alpha=ALPHA_95,
        series_terms=16,
        sqrt_bits=64,
    )
    assert full_radius_at_1872.cell_linf_radius_upper < Fraction(1, 24)


def test_p93_rejects_incompatible_empirical_sample_size():
    with pytest.raises(ValueError, match="not an empirical table"):
        certify_p93_selective_sign_coherence_rejection(
            EMPIRICAL_LAW,
            sample_size=1465,
            alpha_total=ALPHA_95,
            alpha_allocation=p93_witness_alpha_allocation_95(),
        )


def test_p93_rejects_error_allocation_above_familywise_budget():
    allocation = p93_uniform_alpha_allocation(ALPHA_95)
    allocation["t000"] += Fraction(1, 100)
    with pytest.raises(ValueError, match="exceeds alpha_total"):
        certify_p93_selective_sign_coherence_rejection(
            EMPIRICAL_LAW,
            sample_size=1464,
            alpha_total=ALPHA_95,
            alpha_allocation=allocation,
        )
