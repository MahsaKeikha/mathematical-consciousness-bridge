from math import log

import pytest

from consciousness_bridge.refinement_chain_certification import (
    certify_refinement_chain_from_records,
)


def _balanced_binary_records(repeats: int, descriptor_mode: str):
    records = []
    for _ in range(repeats):
        for omega in (0, 1):
            if descriptor_mode == "resolved":
                descriptors = ("all", omega)
            elif descriptor_mode == "persistent":
                descriptors = ("all", "all")
            else:
                raise ValueError("unknown descriptor mode")
            records.append((omega, descriptors, omega))
    return records


def test_single_base_event_controls_all_levels_without_level_penalty():
    short = certify_refinement_chain_from_records(
        [(0, ("all",), 0), (1, ("all",), 1)] * 500,
        omega_size=2,
        descriptor_sizes=(1,),
        target_size=2,
        alpha=0.05,
    )
    long = certify_refinement_chain_from_records(
        [(0, ("all", "all", "all"), 0), (1, ("all", "all", "all"), 1)]
        * 500,
        omega_size=2,
        descriptor_sizes=(1, 1, 1),
        target_size=2,
        alpha=0.05,
    )

    assert short.base_tv_radius == pytest.approx(long.base_tv_radius)
    assert short.simultaneous_coverage == pytest.approx(0.95)
    assert long.simultaneous_coverage == pytest.approx(0.95)


def test_empirical_chain_rule_closes_for_exact_refinement():
    certificate = certify_refinement_chain_from_records(
        _balanced_binary_records(100, "resolved"),
        omega_size=2,
        descriptor_sizes=(1, 2),
        target_size=2,
    )

    residuals = certificate.residual_intervals
    gain = certificate.gain_intervals[0]
    assert residuals[0].estimate == pytest.approx(log(2.0))
    assert residuals[1].estimate == pytest.approx(0.0, abs=1e-12)
    assert gain.estimate == pytest.approx(log(2.0))
    assert certificate.empirical_chain_rule_error < 1e-12


def test_large_sample_certifies_refinement_gain():
    certificate = certify_refinement_chain_from_records(
        _balanced_binary_records(6000, "resolved"),
        omega_size=2,
        descriptor_sizes=(1, 2),
        target_size=2,
        alpha=0.05,
    )

    gain = certificate.gain_intervals[0]
    assert gain.certified_positive
    assert gain.lower > 0.0
    assert gain.lower <= gain.estimate <= gain.upper
    assert gain.lower >= gain.direct_lower
    assert gain.lower >= gain.difference_lower
    assert gain.upper <= gain.direct_upper
    assert gain.upper <= gain.difference_upper


def test_large_sample_certifies_terminal_residual_persistence():
    certificate = certify_refinement_chain_from_records(
        _balanced_binary_records(6000, "persistent"),
        omega_size=2,
        descriptor_sizes=(1, 1),
        target_size=2,
        alpha=0.05,
    )

    terminal = certificate.residual_intervals[-1]
    assert terminal.estimate == pytest.approx(log(2.0))
    assert terminal.certified_positive
    assert certificate.terminal_residual_certified_positive
    assert certificate.gain_intervals[0].estimate == pytest.approx(0.0, abs=1e-12)


def test_refinement_that_fully_resolves_target_does_not_certify_terminal_residual():
    certificate = certify_refinement_chain_from_records(
        _balanced_binary_records(6000, "resolved"),
        omega_size=2,
        descriptor_sizes=(1, 2),
        target_size=2,
        alpha=0.05,
    )

    terminal = certificate.residual_intervals[-1]
    assert terminal.estimate == pytest.approx(0.0, abs=1e-12)
    assert terminal.lower == 0.0
    assert not certificate.terminal_residual_certified_positive


def test_single_level_chain_has_no_refinement_gain_intervals():
    certificate = certify_refinement_chain_from_records(
        [(0, ("all",), 0), (1, ("all",), 1)] * 20,
        omega_size=2,
        descriptor_sizes=(1,),
        target_size=2,
    )

    assert len(certificate.residual_intervals) == 1
    assert certificate.gain_intervals == ()
    assert certificate.empirical_chain_rule_error == 0.0


def test_non_nested_descriptor_chain_is_rejected():
    records = [
        (0, ("left", "same"), 0),
        (1, ("right", "same"), 1),
    ]

    with pytest.raises(ValueError, match="does not refine"):
        certify_refinement_chain_from_records(
            records,
            omega_size=2,
            descriptor_sizes=(2, 1),
            target_size=2,
        )


def test_descriptor_must_be_deterministic_function_of_omega():
    records = [
        (0, ("a",), 0),
        (0, ("b",), 1),
    ]

    with pytest.raises(ValueError, match="deterministic function of omega"):
        certify_refinement_chain_from_records(
            records,
            omega_size=1,
            descriptor_sizes=(2,),
            target_size=2,
        )


def test_declared_alphabet_sizes_are_enforced():
    records = [(0, ("a",), 0), (1, ("b",), 1)]

    with pytest.raises(ValueError, match="omega labels exceed"):
        certify_refinement_chain_from_records(
            records,
            omega_size=1,
            descriptor_sizes=(2,),
            target_size=2,
        )

    with pytest.raises(ValueError, match="descriptor labels exceed"):
        certify_refinement_chain_from_records(
            records,
            omega_size=2,
            descriptor_sizes=(1,),
            target_size=2,
        )

    with pytest.raises(ValueError, match="target labels exceed"):
        certify_refinement_chain_from_records(
            records,
            omega_size=2,
            descriptor_sizes=(2,),
            target_size=1,
        )


def test_descriptor_size_vector_must_match_chain_length():
    records = [(0, ("a", "b"), 0)]

    with pytest.raises(ValueError, match="match the number"):
        certify_refinement_chain_from_records(
            records,
            omega_size=1,
            descriptor_sizes=(1,),
            target_size=1,
        )


def test_empty_records_and_empty_descriptor_sizes_are_rejected():
    with pytest.raises(ValueError, match="descriptor_sizes"):
        certify_refinement_chain_from_records(
            [(0, ("a",), 0)],
            omega_size=1,
            descriptor_sizes=(),
            target_size=1,
        )

    with pytest.raises(ValueError, match="at least one sample"):
        certify_refinement_chain_from_records(
            [],
            omega_size=1,
            descriptor_sizes=(1,),
            target_size=1,
        )


def test_invalid_alpha_and_tolerance_are_rejected():
    records = [(0, ("a",), 0)]

    with pytest.raises(ValueError, match="alpha"):
        certify_refinement_chain_from_records(
            records,
            omega_size=1,
            descriptor_sizes=(1,),
            target_size=1,
            alpha=1.0,
        )

    with pytest.raises(ValueError, match="tolerance"):
        certify_refinement_chain_from_records(
            records,
            omega_size=1,
            descriptor_sizes=(1,),
            target_size=1,
            tolerance=-1.0,
        )
