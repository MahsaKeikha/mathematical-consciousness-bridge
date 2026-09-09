from math import log

import pytest

from consciousness_bridge.adaptive_descriptor_selection import (
    certify_adaptive_descriptor_selection_from_records,
)


OMEGA = (0, 1, 2, 3)
COARSE = {state: 0 for state in OMEGA}
GOOD = {0: 0, 1: 1, 2: 0, 3: 1}
PARTIAL = {0: 0, 1: 1, 2: 1, 3: 1}
BAD = {state: 0 for state in OMEGA}


def balanced_records(repetitions: int = 100) -> list[tuple[int, int]]:
    return [
        (omega, omega % 2)
        for _ in range(repetitions)
        for omega in OMEGA
    ]


def certificate(
    *,
    records=None,
    candidates=None,
    candidate_sizes=None,
    coarse=COARSE,
    coarse_size=1,
    omega_states=OMEGA,
    target_size=2,
    alpha=0.05,
):
    if records is None:
        records = balanced_records()
    if candidates is None:
        candidates = {"good": GOOD, "partial": PARTIAL, "bad": BAD}
    if candidate_sizes is None:
        candidate_sizes = {"good": 2, "partial": 2, "bad": 1}
    return certify_adaptive_descriptor_selection_from_records(
        records,
        omega_states=omega_states,
        coarse_descriptor=coarse,
        coarse_size=coarse_size,
        candidate_descriptors=candidates,
        candidate_sizes=candidate_sizes,
        target_size=target_size,
        alpha=alpha,
    )


def test_empirical_gain_selection_finds_target_relevant_refinement():
    result = certificate(records=balanced_records(25_000))

    assert result.selected_name == "good"
    selected = result.candidates[result.selected_index]
    assert selected.gain_estimate == pytest.approx(log(2.0), abs=1e-12)
    assert selected.residual_estimate == pytest.approx(0.0, abs=1e-12)
    assert result.selected_gain_certified_positive


def test_one_base_radius_has_no_candidate_count_penalty():
    single = certificate(
        candidates={"good": GOOD},
        candidate_sizes={"good": 2},
    )
    many = certificate()

    assert many.base_tv_radius == pytest.approx(single.base_tv_radius)
    assert many.candidate_count == 3
    assert many.candidate_count_penalty_applied is False


def test_all_candidate_intervals_are_simultaneously_exposed():
    result = certificate()

    assert {item.name for item in result.candidates} == {
        "bad",
        "good",
        "partial",
    }
    for item in result.candidates:
        assert item.gain_lower <= item.gain_estimate <= item.gain_upper
        assert item.residual_lower <= item.residual_estimate <= item.residual_upper


def test_empirical_p21_identity_closes_for_every_candidate():
    result = certificate()

    assert max(
        item.empirical_chain_rule_error for item in result.candidates
    ) < 1e-12


def test_post_selection_regret_certificate_is_bounded_by_generic_result():
    result = certificate(records=balanced_records(25_000))

    assert result.data_dependent_selection_regret_bound >= 0.0
    assert (
        result.data_dependent_selection_regret_bound
        <= result.generic_selection_regret_bound + 1e-12
    )
    assert result.selected_residual_excess_bound == pytest.approx(
        result.data_dependent_selection_regret_bound
    )


def test_duplicate_candidate_copies_do_not_change_selected_good_interval():
    base = certificate(
        candidates={"good": GOOD, "bad": BAD},
        candidate_sizes={"good": 2, "bad": 1},
    )
    expanded = certificate(
        candidates={
            "good": GOOD,
            "bad": BAD,
            "bad_copy_1": BAD,
            "bad_copy_2": BAD,
            "bad_copy_3": BAD,
        },
        candidate_sizes={
            "good": 2,
            "bad": 1,
            "bad_copy_1": 1,
            "bad_copy_2": 1,
            "bad_copy_3": 1,
        },
    )

    base_good = next(item for item in base.candidates if item.name == "good")
    expanded_good = next(
        item for item in expanded.candidates if item.name == "good"
    )
    assert expanded.base_tv_radius == pytest.approx(base.base_tv_radius)
    assert expanded_good.gain_lower == pytest.approx(base_good.gain_lower)
    assert expanded_good.gain_upper == pytest.approx(base_good.gain_upper)


def test_candidate_must_be_defined_on_full_declared_omega_alphabet():
    incomplete = {0: 0, 1: 1, 2: 0}

    with pytest.raises(ValueError, match="every declared omega state"):
        certificate(
            candidates={"incomplete": incomplete},
            candidate_sizes={"incomplete": 2},
        )


def test_candidate_must_refine_the_common_coarse_descriptor():
    coarse = {0: 0, 1: 1, 2: 0, 3: 1}

    with pytest.raises(ValueError, match="does not refine"):
        certificate(
            coarse=coarse,
            coarse_size=2,
            candidates={"constant": BAD},
            candidate_sizes={"constant": 1},
        )


def test_candidate_size_declaration_is_enforced():
    with pytest.raises(ValueError, match="declared alphabet size"):
        certificate(
            candidates={"good": GOOD},
            candidate_sizes={"good": 1},
        )


def test_candidate_size_names_must_match_candidate_names():
    with pytest.raises(ValueError, match="exactly the candidate names"):
        certificate(
            candidates={"good": GOOD},
            candidate_sizes={"other": 2},
        )


def test_records_must_stay_inside_declared_omega_alphabet():
    records = balanced_records() + [(99, 1)]

    with pytest.raises(ValueError, match="outside omega_states"):
        certificate(records=records)


def test_target_alphabet_declaration_is_enforced():
    records = balanced_records() + [(0, 2)]

    with pytest.raises(ValueError, match="target labels exceed"):
        certificate(records=records, target_size=2)


def test_duplicate_declared_omega_states_are_rejected():
    with pytest.raises(ValueError, match="must not contain duplicates"):
        certificate(omega_states=(0, 1, 2, 3, 3))


def test_invalid_alpha_and_empty_records_are_rejected():
    with pytest.raises(ValueError, match="alpha"):
        certificate(alpha=0.0)
    with pytest.raises(ValueError, match="at least one sample"):
        certificate(records=[])
