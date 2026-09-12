from pathlib import Path

PAGE = Path("website/observer-research.html")


def test_observer_research_has_its_own_dedicated_public_page() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required = (
        "Research I · Previous repository",
        "Spatiotemporal observer mathematics",
        "https://github.com/MahsaKeikha/spatiotemporal-observer-math",
        "v1.9.0",
        "258",
        "54",
        "The core observer object",
        "Physics → observer pipeline",
        "Causal accessibility",
        "Instantaneous and finite-horizon readouts",
        "Comparison geometry",
        "What Research I did not establish",
        "Why Research II exists",
    )
    for token in required:
        assert token in page


def test_observer_research_preserves_physical_to_experiential_boundary() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required = (
        "does <strong>not</strong> insert consciousness",
        "It did not prove that an observer object is conscious",
        "The physical-to-experiential step is a different scientific obligation",
        "is a bridge hypothesis, not a consequence",
    )
    for token in required:
        assert token in page


def test_observer_research_exposes_original_audit_paths() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required_paths = (
        "docs/conceptual_scope.md",
        "docs/scientific_foundations.md",
        "docs/mathematics.md",
        "docs/architecture.md",
        "docs/detailed_proposition_record.md",
        "docs/theorem_roadmap.md",
        "docs/falsification.md",
        "docs/reproducibility.md",
        "docs/conceptual_bridge.md",
    )
    for path in required_paths:
        assert path in page


def test_observer_research_links_forward_without_conflating_programs() -> None:
    page = PAGE.read_text(encoding="utf-8")

    assert 'href="research-lineage.html"' in page
    assert 'href="research-map.html"' in page
    assert "Research I asks what physical observer structure can be identified" in page
    assert "Research II asks what more a testable experiential bridge would require" in page
