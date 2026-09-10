from consciousness_bridge.gap_stopping_complexity import EdgeStoppingComplexity
from consciousness_bridge.heterogeneous_service_stopping import (
    ServiceGuarantee,
    edge_service_stopping_bound,
    guaranteed_samples,
    heterogeneous_stopping_bound,
    is_service_compliant_schedule,
    p50_special_case_bound,
    rounds_for_samples,
    service_violations,
)


def _bound(edge, margin, samples):
    return EdgeStoppingComplexity(
        edge=edge,
        margin=margin,
        gap=abs(margin),
        amplitude=0.35,
        log_factor=4.0,
        local_samples=samples,
    )


def test_service_guarantee_rate_and_round_conversion():
    guarantee = ServiceGuarantee(window=10, quota=4)
    assert guarantee.service_rate == 0.4
    assert guaranteed_samples(0, guarantee) == 0
    assert guaranteed_samples(9, guarantee) == 0
    assert guaranteed_samples(10, guarantee) == 4
    assert guaranteed_samples(27, guarantee) == 8
    assert rounds_for_samples(1, guarantee) == 10
    assert rounds_for_samples(4, guarantee) == 10
    assert rounds_for_samples(5, guarantee) == 20
    assert rounds_for_samples(9, guarantee) == 30


def test_p50_is_quota_one_special_case():
    assert p50_special_case_bound(17, 5) == 85


def test_heterogeneous_schedule_compliance_and_violation_detection():
    active = (("a", "b"),) * 6
    selections = ("a", "b", "a", "a", "b", "a")
    guarantees = {
        "a": ServiceGuarantee(window=3, quota=2),
        "b": ServiceGuarantee(window=3, quota=1),
    }
    assert is_service_compliant_schedule(active, selections, guarantees)

    bad = ("a", "a", "a", "a", "b", "a")
    violations = service_violations(active, bad, guarantees)
    assert any(v.vertex == "b" and v.start_round == 1 for v in violations)


def test_pruned_vertex_has_no_service_obligation_after_removal():
    active = (("a", "b"), ("a", "b"), ("a",), ("a",))
    selections = ("a", "b", "a", "a")
    guarantees = {
        "a": ServiceGuarantee(window=2, quota=1),
        "b": ServiceGuarantee(window=2, quota=1),
    }
    assert is_service_compliant_schedule(active, selections, guarantees)


def test_edge_bound_is_controlled_by_slower_endpoint():
    bound = _bound(("a", "b"), 0.2, 13)
    guarantees = {
        "a": ServiceGuarantee(window=4, quota=2),
        "b": ServiceGuarantee(window=5, quota=1),
    }
    result = edge_service_stopping_bound(bound, guarantees)
    assert result.endpoint_rounds == (28, 65)
    assert result.global_rounds == 65
    assert result.bottleneck_vertices == ("b",)


def test_positive_family_uses_fastest_positive_edge_global_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), 0.1, 20),
        ("b", "c"): _bound(("b", "c"), 0.2, 15),
        ("c", "d"): _bound(("c", "d"), -0.1, 12),
    }
    guarantees = {
        "a": ServiceGuarantee(window=5, quota=1),
        "b": ServiceGuarantee(window=4, quota=2),
        "c": ServiceGuarantee(window=3, quota=1),
        "d": ServiceGuarantee(window=6, quota=1),
    }
    result = heterogeneous_stopping_bound(bounds, guarantees)
    assert result.status == "positive-witness"
    # (a,b): max(100, 40)=100; (b,c): max(32,45)=45.
    assert result.global_round_bound == 45
    assert result.controlling_edges == (("b", "c"),)


def test_all_negative_family_uses_slowest_edge_global_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 10),
        ("b", "c"): _bound(("b", "c"), -0.2, 20),
    }
    guarantees = {
        "a": ServiceGuarantee(window=3, quota=1),
        "b": ServiceGuarantee(window=4, quota=2),
        "c": ServiceGuarantee(window=5, quota=1),
    }
    result = heterogeneous_stopping_bound(bounds, guarantees)
    # (a,b): max(30,20)=30; (b,c): max(40,100)=100.
    assert result.status == "certified-no-positive-edge"
    assert result.global_round_bound == 100
    assert result.controlling_edges == (("b", "c"),)


def test_zero_margin_preserves_no_finite_bound():
    bounds = {
        ("a", "b"): _bound(("a", "b"), -0.1, 10),
        ("b", "c"): EdgeStoppingComplexity(
            edge=("b", "c"),
            margin=0.0,
            gap=0.0,
            amplitude=0.35,
            log_factor=4.0,
            local_samples=None,
        ),
    }
    guarantees = {
        "a": ServiceGuarantee(window=3, quota=1),
        "b": ServiceGuarantee(window=4, quota=1),
        "c": ServiceGuarantee(window=5, quota=1),
    }
    result = heterogeneous_stopping_bound(bounds, guarantees)
    assert result.status == "no-finite-sign-gap-bound"
    assert result.global_round_bound is None


def test_invalid_service_guarantee_is_rejected():
    for window, quota in ((0, 1), (3, 0), (2, 3)):
        try:
            ServiceGuarantee(window=window, quota=quota)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid service guarantee should be rejected")
