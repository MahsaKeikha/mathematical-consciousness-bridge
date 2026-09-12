from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_start_here_matches_current_release_frontier() -> None:
    source = _read("START_HERE.md")

    assert "v0.81.0" in source
    assert "81 proposition-level results" in source
    assert "current theorem frontier is **P81**" in source
    assert "physical-to-experiential bridge itself remains open" in source
    assert "docs/proposition_81_projection_event_model_separation.md" in source


def test_reader_entry_points_are_linked_from_main_surfaces() -> None:
    readme = _read("README.md")
    navigation = _read("docs/research_navigation.md")
    website = _read("website/index.html")

    assert "START_HERE.md" in readme
    assert "START_HERE.md" in navigation
    assert "start-here.html" in website


def test_navigation_and_roadmap_report_p81_frontier() -> None:
    navigation = _read("docs/research_navigation.md")
    roadmap = _read("docs/theorem_roadmap.md")

    assert "current documented theorem frontier is **P81**" in navigation
    assert "current documented theorem frontier is **P81**" in roadmap
    assert "P81" in navigation
    assert "P81" in roadmap
    assert "P71-P81" in navigation
    assert "P71-P81" in roadmap


def test_public_start_page_is_reader_oriented_and_scientifically_bounded() -> None:
    source = _read("website/start-here.html")

    assert "81" in source
    assert "P81" in source
    assert "v0.81.0" in source
    assert "physical-to-experiential bridge" in source
    assert "does not claim that consciousness has been derived from physics" in source
    assert "research-map.html" in source
    assert "visual-atlas.html" in source
