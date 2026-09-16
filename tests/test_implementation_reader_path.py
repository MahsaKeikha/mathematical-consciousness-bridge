from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def test_research_path_cards_open_stage_specific_implementation_sections() -> None:
    script = (WEBSITE / "reader-links.js").read_text(encoding="utf-8")

    assert "#program-stages .result-grid" in script
    assert "document.createElement('a')" in script
    assert "card.replaceWith(link)" in script
    for stage in range(1, 11):
        target = f"implementation.html#stage-{stage:02d}"
        assert target in script

    assert "How it works & implementation" in script
    assert "research-path-card" in script
    assert "Open implementation details" in script
    assert "#orientation .result-grid" not in script


def test_research_status_cards_open_exact_stage_pages() -> None:
    script = (WEBSITE / "reader-links.js").read_text(encoding="utf-8")

    required_destinations = {
        "research i": "observer-research.html",
        "research ii": "research-map.html",
        "research iii": "measurement-science.html",
    }
    for label, destination in required_destinations.items():
        assert f"['{label}', '{destination}']" in script

    assert "wireResearchStatusCards();" in script
    assert "research-status-link" in script
    assert "Open research page" in script
    assert "card.replaceWith(link)" in script


def test_implementation_guide_covers_all_ten_research_stages() -> None:
    page = (WEBSITE / "implementation.html").read_text(encoding="utf-8")

    for stage in range(1, 11):
        assert f'id="stage-{stage:02d}"' in page
        assert f'href="#stage-{stage:02d}"' in page


def test_implementation_guide_exposes_real_repository_surfaces() -> None:
    page = (WEBSITE / "implementation.html").read_text(encoding="utf-8")

    required_surfaces = (
        "src/consciousness_bridge/",
        "tree/main/tests",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
        "scripts/reproducibility_audit.py",
        "scripts/generate_all_figures.py",
        "scripts/verify_repository.py",
    )
    for surface in required_surfaces:
        assert surface in page


def test_implementation_guide_preserves_scientific_boundary_language() -> None:
    page = (WEBSITE / "implementation.html").read_text(encoding="utf-8")

    assert "executable mathematics is not evidence" in page
    assert "failure of one descriptor does not prove that experience is nonphysical" in page
    assert "neither one upgrades a conditional theorem into an empirical fact" in page
