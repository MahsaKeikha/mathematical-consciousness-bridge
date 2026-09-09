import pytest

from consciousness_bridge.causal_structure_scale_certification import (
    decode_distribution,
    pairwise_scale_distortion,
    reconstruction_error,
    scale_separation_certificate,
    uniform_reconstruction_defect,
)


def test_exact_family_decoder_preserves_response_geometry():
    coarse_map = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    decoder = {
        "A": {"a0": 0.75, "a1": 0.25},
        "B": {"b0": 0.20, "b1": 0.80},
    }
    first = {"a0": 0.075, "a1": 0.025, "b0": 0.18, "b1": 0.72}
    second = {"a0": 0.675, "a1": 0.225, "b0": 0.02, "b1": 0.08}

    fine, coarse, additive_bound = pairwise_scale_distortion(
        first, second, coarse_map, decoder
    )

    assert additive_bound == pytest.approx(0.0, abs=1e-12)
    assert fine == pytest.approx(0.8)
    assert coarse == pytest.approx(fine)


def test_p18_pairwise_distance_loss_is_bounded_by_reconstruction_errors():
    coarse_map = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    decoder = {
        "A": {"a0": 0.6, "a1": 0.4},
        "B": {"b0": 0.5, "b1": 0.5},
    }
    first = {"a0": 0.5, "a1": 0.1, "b0": 0.2, "b1": 0.2}
    second = {"a0": 0.1, "a1": 0.1, "b0": 0.1, "b1": 0.7}

    fine, coarse, additive_bound = pairwise_scale_distortion(
        first, second, coarse_map, decoder
    )

    assert coarse <= fine + 1e-12
    assert fine <= coarse + additive_bound + 1e-12


def test_uniform_defect_yields_two_rho_distortion_certificate():
    coarse_map = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    decoder = {
        "A": {"a0": 0.7, "a1": 0.3},
        "B": {"b0": 0.25, "b1": 0.75},
    }
    family = {
        "p": {"a0": 0.50, "a1": 0.10, "b0": 0.10, "b1": 0.30},
        "q": {"a0": 0.12, "a1": 0.08, "b0": 0.16, "b1": 0.64},
        "r": {"a0": 0.28, "a1": 0.12, "b0": 0.15, "b1": 0.45},
    }

    rho = uniform_reconstruction_defect(family, coarse_map, decoder)

    labels = list(family)
    for index, first_label in enumerate(labels):
        for second_label in labels[index + 1 :]:
            fine, coarse, _ = pairwise_scale_distortion(
                family[first_label], family[second_label], coarse_map, decoder
            )
            loss = fine - coarse
            assert loss >= -1e-12
            assert loss <= 2.0 * rho + 1e-12


def test_collision_family_hits_the_two_rho_bound_exactly():
    coarse_map = {"x0": "A", "x1": "A"}
    decoder = {"A": {"x0": 0.5, "x1": 0.5}}
    family = {
        "left": {"x0": 1.0},
        "right": {"x1": 1.0},
    }

    certificate = scale_separation_certificate(family, coarse_map, decoder)

    assert certificate.fine_min_separation == pytest.approx(1.0)
    assert certificate.coarse_min_separation == pytest.approx(0.0)
    assert certificate.reconstruction_defect == pytest.approx(0.5)
    assert certificate.guaranteed_coarse_separation == pytest.approx(0.0)
    assert not certificate.certified_identifiable


def test_positive_margin_certifies_coarse_family_identifiability():
    coarse_map = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    decoder = {
        "A": {"a0": 0.75, "a1": 0.25},
        "B": {"b0": 0.20, "b1": 0.80},
    }
    family = {
        "low": {"a0": 0.075, "a1": 0.025, "b0": 0.18, "b1": 0.72},
        "mid": {"a0": 0.30, "a1": 0.10, "b0": 0.12, "b1": 0.48},
        "high": {"a0": 0.675, "a1": 0.225, "b0": 0.02, "b1": 0.08},
    }

    certificate = scale_separation_certificate(family, coarse_map, decoder)

    assert certificate.reconstruction_defect == pytest.approx(0.0, abs=1e-12)
    assert certificate.coarse_min_separation == pytest.approx(
        certificate.fine_min_separation
    )
    assert certificate.guaranteed_coarse_separation == pytest.approx(
        certificate.fine_min_separation
    )
    assert certificate.certified_identifiable


def test_decoder_must_stay_inside_declared_coarse_fibers():
    coarse_map = {"a": "A", "b": "B"}
    decoder = {
        "A": {"b": 1.0},
        "B": {"b": 1.0},
    }

    with pytest.raises(ValueError, match="coarse fiber"):
        decode_distribution({"A": 1.0}, decoder, coarse_map)


def test_reconstruction_error_is_zero_for_exact_reconstruction():
    coarse_map = {"a": "A", "b": "B"}
    decoder = {"A": {"a": 1.0}, "B": {"b": 1.0}}
    distribution = {"a": 0.3, "b": 0.7}

    assert reconstruction_error(distribution, coarse_map, decoder) == pytest.approx(0.0)
