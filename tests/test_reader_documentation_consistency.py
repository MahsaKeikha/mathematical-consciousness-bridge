import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def _frontier() -> int:
    numbers: list[int] = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def _project_version() -> str:
    text = _read("pyproject.toml")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_start_here_matches_current_release_and_theorem_frontier() -> None:
    source = _read("START_HERE.md")
    frontier = _frontier()
    version = _project_version()

    assert f"v{version}" in source
    assert f"{frontier} proposition-level results" in source
    assert f"P{frontier}" in source
    assert "physical-to-experiential bridge itself remains open" in source
    assert f"docs/proposition_{frontier}_" in source


def test_reader_entry_points_are_linked_from_main_surfaces() -> None:
    readme = _read("README.md")
    navigation = _read("docs/research_navigation.md")
    website = _read("website/index.html")

    assert "START_HERE.md" in readme
    assert "START_HERE.md" in navigation
    assert "start-here.html" in website


def test_navigation_and_roadmap_report_current_frontier() -> None:
    navigation = _read("docs/research_navigation.md")
    roadmap = _read("docs/theorem_roadmap.md")
    frontier = _frontier()

    assert f"current documented theorem frontier is **P{frontier}**" in navigation
    assert f"current documented theorem frontier is **P{frontier}**" in roadmap
    assert f"P{frontier}" in navigation
    assert f"P{frontier}" in roadmap
    assert f"P71-P{frontier}" in navigation
    assert f"P71-P{frontier}" in roadmap


def test_public_start_page_is_reader_oriented_and_scientifically_bounded() -> None:
    source = _read("website/start-here.html")
    frontier = _frontier()
    version = _project_version()

    assert str(frontier) in source
    assert f"P{frontier}" in source
    assert f"v{version}" in source
    assert "physical-to-experiential bridge" in source
    assert "does not claim that consciousness has been derived from physics" in source
    assert "research-map.html" in source
    assert "visual-atlas.html" in source
