from consciousness_bridge.partition_irreducibility_scale_certification import (
    block_compatible_coarse_map,
    coarse_partition_irreducibility,
    partition_irreducibility,
    partition_scale_certificate,
    partition_scale_loss,
    product_decoder_from_coordinate_decoders,
    threshold_irreducibility_preserved,
)


def binary_correlated_distribution():
    return {
        (0, 0): 0.45,
        (0, 1): 0.05,
        (1, 0): 0.05,
        (1, 1): 0.45,
    }


def identity_map():
    support = [(0, 0), (0, 1), (1, 0), (1, 1)]
    return block_compatible_coarse_map(
        support,
        ({0: 0, 1: 1}, {0: 0, 1: 1}),
    )


def identity_decoder():
    return {
        (0, 0): {(0, 0): 1.0},
        (0, 1): {(0, 1): 1.0},
        (1, 0): {(1, 0): 1.0},
        (1, 1): {(1, 1): 1.0},
    }


def test_partition_irreducibility_matches_known_binary_value():
    value = partition_irreducibility(binary_correlated_distribution(), ((0,), (1,)))
    assert abs(value - 0.4) < 1e-12


def test_identity_observation_preserves_irreducibility_exactly():
    distribution = binary_correlated_distribution()
    fine, coarse, loss = partition_scale_loss(
        distribution,
        ((0,), (1,)),
        identity_map(),
    )
    assert abs(fine - 0.4) < 1e-12
    assert abs(coarse - fine) < 1e-12
    assert abs(loss) < 1e-12


def test_collapsing_one_coordinate_can_destroy_partition_irreducibility():
    distribution = binary_correlated_distribution()
    support = list(distribution)
    coarse_map = block_compatible_coarse_map(
        support,
        ({0: 0, 1: 0}, {0: 0, 1: 1}),
    )
    fine = partition_irreducibility(distribution, ((0,), (1,)))
    coarse = coarse_partition_irreducibility(
        distribution,
        ((0,), (1,)),
        coarse_map,
    )
    assert fine > 0.0
    assert abs(coarse) < 1e-12
    assert coarse <= fine


def test_p26_reconstruction_bound_controls_partition_loss():
    distribution = binary_correlated_distribution()
    certificate = partition_scale_certificate(
        distribution,
        ((0,), (1,)),
        identity_map(),
        identity_decoder(),
    )
    loss = certificate.fine_irreducibility - certificate.coarse_irreducibility
    assert loss >= -1e-12
    assert loss <= certificate.additive_loss_bound + 1e-12
    assert certificate.exact_preservation_certified


def test_threshold_margin_certificate():
    distribution = binary_correlated_distribution()
    certificate = partition_scale_certificate(
        distribution,
        ((0,), (1,)),
        identity_map(),
        identity_decoder(),
    )
    assert threshold_irreducibility_preserved(certificate, 0.2)
    assert not threshold_irreducibility_preserved(certificate, 0.5)


def test_product_decoder_builds_normalized_joint_conditionals():
    decoder = product_decoder_from_coordinate_decoders(
        ((0, 0),),
        (
            {0: {0: 0.5, 1: 0.5}},
            {0: {0: 0.25, 1: 0.75}},
        ),
    )
    conditional = decoder[(0, 0)]
    assert abs(sum(conditional.values()) - 1.0) < 1e-12
    assert abs(conditional[(1, 1)] - 0.375) < 1e-12


def test_block_compatible_map_rejects_missing_coordinate_values():
    try:
        block_compatible_coarse_map(
            [(0, 0), (1, 1)],
            ({0: 0}, {0: 0, 1: 1}),
        )
    except ValueError as exc:
        assert "cover every fine support value" in str(exc)
    else:
        raise AssertionError("Expected ValueError")


def test_negative_threshold_is_rejected():
    certificate = partition_scale_certificate(
        binary_correlated_distribution(),
        ((0,), (1,)),
        identity_map(),
        identity_decoder(),
    )
    try:
        threshold_irreducibility_preserved(certificate, -0.1)
    except ValueError as exc:
        assert "nonnegative" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
