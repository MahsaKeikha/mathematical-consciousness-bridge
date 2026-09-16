import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "theorem_roadmap.svg"
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"
CATALOG = ROOT / "docs" / "figure_catalog.md"
MANIFEST = ROOT / "figures" / "manifest.json"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
RESEARCH_MAP = ROOT / "website" / "research-map.html"


def _frontier() -> int:
    numbers: list[int] = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def _figure_nodes() -> list[int]:
    text = FIGURE.read_text(encoding="utf-8")
    return sorted(int(value) for value in re.findall(r'data-proposition="P(\d+)"', text))


def _roadmap_index_numbers() -> list[int]:
    text = ROADMAP.read_text(encoding="utf-8")
    block = text.split("## 3. Complete proposition index", 1)[1].split(
        "## 4. Calibration branch remains separate", 1
    )[0]
    return [int(value) for value in re.findall(r"^\| \[P(\d+)\]", block, flags=re.MULTILINE)]


def test_theorem_roadmap_figure_has_exact_p1_through_current_frontier_nodes():
    text = FIGURE.read_text(encoding="utf-8")
    frontier = _frontier()
    nodes = _figure_nodes()
    assert frontier == 100
    assert nodes == list(range(1, frontier + 1))
    assert len(nodes) == len(set(nodes)) == 100
    assert "Complete theorem dependency map for P1-P100" in text
    assert "Every proposition P1 through P100 appears explicitly" in text
    assert "P71-P100 returns to the P19 bridge-sufficiency lineage" in text
    assert 'class="chip current" data-proposition="P100"' in text
    assert "P1-P31" not in text


def test_roadmap_table_and_roadmap_figure_have_identical_p1_p100_coverage():
    assert _roadmap_index_numbers() == list(range(1, 101))
    assert _figure_nodes() == _roadmap_index_numbers()


def test_figure_catalog_and_manifest_publish_complete_roadmap_metadata():
    catalog = CATALOG.read_text(encoding="utf-8")
    assert "Complete theorem dependency map for P1-P100" in catalog
    assert "complete theorem roadmap for Propositions 1 through 100" in catalog
    assert "P1-P31" not in catalog

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    record = next(
        item
        for item in manifest["figures"]
        if item["path"] == "docs/figures/theorem_roadmap.svg"
    )
    assert record["title"] == "Complete theorem dependency map for P1-P100"
    assert record["bytes"] == FIGURE.stat().st_size


def test_repository_and_website_use_the_same_complete_p1_p100_roadmap():
    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")
    research = RESEARCH_MAP.read_text(encoding="utf-8")
    canonical_name = "theorem_roadmap.svg"
    for page in (atlas, research):
        assert canonical_name in page
        assert "Complete theorem roadmap: P1-P100" in page
        assert "Complete theorem roadmap P1-P100" in page
    assert 'id="complete-theorem-roadmap-figure"' in research
    assert "Every proposition from P1 through P100 appears as an individual labeled node" in research
