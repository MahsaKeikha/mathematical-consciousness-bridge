from pathlib import Path


def test_research_lineage_connects_both_public_repositories() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    required = (
        "Spatiotemporal Observer Mathematics",
        "Mathematical Consciousness Bridge",
        "https://github.com/MahsaKeikha/spatiotemporal-observer-math",
        "https://github.com/MahsaKeikha/mathematical-consciousness-bridge",
        "Research I repository",
        "Research II",
        "Research Map",
        "physical subsystem identification",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in page


def test_lineage_preserves_scientific_boundary_between_projects() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    required = (
        "A recovered subsystem is not automatically a conscious subject",
        "Bridge remains an independently testable open problem",
        "not a proof chain to consciousness",
        "independently justified experiential target or bridge principle",
    )
    for token in required:
        assert token in page


def test_lineage_exposes_auditable_research_one_entry_points() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    required_paths = (
        "docs/visual_research_guide.md",
        "docs/research_overview.md",
        "docs/research_index.md",
        "docs/physics_guide.md",
        "docs/assumption_ledger.md",
    )
    for path in required_paths:
        assert path in page


def test_global_website_navigation_includes_research_lineage() -> None:
    script = Path("website/app.js").read_text(encoding="utf-8")

    assert "research-lineage.html" in script
    assert "Research Lineage" in script
    assert "spatiotemporal-observer-math" in script
    assert "Research I → Research II" in script
