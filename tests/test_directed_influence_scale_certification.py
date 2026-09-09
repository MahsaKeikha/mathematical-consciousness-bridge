import pytest

from consciousness_bridge.directed_influence_scale_certification import (
    directed_influence_scale_certificate,
)


def responses():
    return {
        "u0": {
            "t": {
                (0, 0): 0.45,
                (1, 0): 0.45,
                (0, 1): 0.05,
                (1, 1): 0.05,
            }
        },
        "u1": {
            "t": {
                (0, 0): 0.05,
                (1, 0): 0.05,
                (0, 1): 0.45,
                (1, 1): 0.45,
            }
        },
    }


SOURCE_PAIRS = {0: (("u0", "u1"),)}
IDENTITY_MAP = {(0,): "zero", (1,): "one"}
IDENTITY_DECODER = {"zero": {(0,): 1.0}, "one": {(1,): 1.0}}
CONSTANT_MAP = {(0,): "all", (1,): "all"}
BALANCED_DECODER = {"all": {(0,): 0.5, (1,): 0.5}}


def certificate(*, coarse_map=IDENTITY_MAP, decoder=IDENTITY_DECODER, threshold=0.0):
    return directed_influence_scale_certificate(
        responses(),
        SOURCE_PAIRS,
        source=0,
        target=1,
        delay="t",
        coarse_map=coarse_map,
        decoder=decoder,
        threshold=threshold,
    )


def test_identity_coarse_map_exactly_preserves_directed_influence():
    result = certificate()

    assert result.fine_influence == pytest.approx(0.8)
    assert result.coarse_influence == pytest.approx(0.8)
    assert result.reconstruction_defect == pytest.approx(0.0)
    assert result.distortion_bound == pytest.approx(0.0)
    assert result.guaranteed_coarse_influence == pytest.approx(0.8)


def test_many_to_one_map_can_erase_influence_but_obeys_p25_bound():
    result = certificate(coarse_map=CONSTANT_MAP, decoder=BALANCED_DECODER)

    assert result.fine_influence == pytest.approx(0.8)
    assert result.coarse_influence == pytest.approx(0.0)
    assert result.reconstruction_defect == pytest.approx(0.4)
    assert result.distortion_bound == pytest.approx(0.8)
    assert result.fine_influence - result.coarse_influence <= (
        result.distortion_bound + 1e-12
    )


def test_deterministic_coarse_observation_cannot_create_an_influence_edge():
    result = certificate(coarse_map=CONSTANT_MAP, decoder=BALANCED_DECODER)

    assert result.coarse_influence <= result.fine_influence
    assert result.no_false_positive_certified


def test_margin_above_two_rho_certifies_threshold_edge_preservation():
    result = certificate(threshold=0.5)

    assert result.fine_edge_present
    assert result.coarse_edge_present
    assert result.edge_preservation_certified


def test_insufficient_reconstruction_margin_does_not_claim_preservation():
    result = certificate(
        coarse_map=CONSTANT_MAP,
        decoder=BALANCED_DECODER,
        threshold=0.2,
    )

    assert result.fine_edge_present
    assert not result.coarse_edge_present
    assert not result.edge_preservation_certified


def test_coarse_positive_edge_implies_fine_positive_edge_at_same_threshold():
    result = certificate(threshold=0.7)

    assert result.coarse_edge_present
    assert result.fine_edge_present


def test_coarse_map_must_cover_every_observed_target_outcome():
    with pytest.raises(ValueError, match="cover every observed target outcome"):
        certificate(
            coarse_map={(0,): "zero"},
            decoder={"zero": {(0,): 1.0}},
        )


def test_decoder_must_remain_inside_declared_coarse_fibers():
    invalid_decoder = {
        "zero": {(1,): 1.0},
        "one": {(1,): 1.0},
    }
    with pytest.raises(ValueError, match="corresponding coarse fiber"):
        certificate(decoder=invalid_decoder)


def test_source_must_have_at_least_one_matched_pair():
    with pytest.raises(ValueError, match="matched intervention pair"):
        directed_influence_scale_certificate(
            responses(),
            {},
            source=0,
            target=1,
            delay="t",
            coarse_map=IDENTITY_MAP,
            decoder=IDENTITY_DECODER,
        )


def test_pair_interventions_must_exist_in_response_table():
    with pytest.raises(ValueError, match="declared response"):
        directed_influence_scale_certificate(
            responses(),
            {0: (("u0", "missing"),)},
            source=0,
            target=1,
            delay="t",
            coarse_map=IDENTITY_MAP,
            decoder=IDENTITY_DECODER,
        )


def test_delay_must_exist_for_every_referenced_intervention():
    with pytest.raises(ValueError, match="delay must be available"):
        directed_influence_scale_certificate(
            responses(),
            SOURCE_PAIRS,
            source=0,
            target=1,
            delay="missing",
            coarse_map=IDENTITY_MAP,
            decoder=IDENTITY_DECODER,
        )


def test_invalid_source_target_and_threshold_are_rejected():
    with pytest.raises(ValueError, match="source must be nonnegative"):
        directed_influence_scale_certificate(
            responses(),
            SOURCE_PAIRS,
            source=-1,
            target=1,
            delay="t",
            coarse_map=IDENTITY_MAP,
            decoder=IDENTITY_DECODER,
        )

    with pytest.raises(ValueError, match="target must be nonnegative"):
        directed_influence_scale_certificate(
            responses(),
            SOURCE_PAIRS,
            source=0,
            target=-1,
            delay="t",
            coarse_map=IDENTITY_MAP,
            decoder=IDENTITY_DECODER,
        )

    with pytest.raises(ValueError, match="threshold"):
        certificate(threshold=-0.1)
    with pytest.raises(ValueError, match="threshold"):
        certificate(threshold=1.1)
