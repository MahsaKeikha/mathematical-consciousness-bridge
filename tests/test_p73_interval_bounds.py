from consciousness_bridge.three_view_target_channel_identifiability import (
    finite_three_view_stability_certificate,
)


def test_p73_finite_intervals_remain_inside_unit_interval_for_noisy_data():
    observations = (
        [(1, 1, 1)] * 45
        + [(1, 1, -1)] * 5
        + [(1, -1, 1)] * 5
        + [(-1, 1, 1)] * 5
    )
    certificate = finite_three_view_stability_certificate(observations, alpha=0.05)
    for interval in (
        certificate.stability_1,
        certificate.stability_2,
        certificate.stability_3,
    ):
        assert 0.0 <= interval.lower <= interval.upper <= 1.0
