import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_complete_proposition_index_is_one_contiguous_p1_p100_table() -> None:
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    block = roadmap.split("## 3. Complete proposition index", 1)[1].split(
        "## 4. Calibration branch remains separate", 1
    )[0]
    rows = re.findall(r"^\| \[P(\d+)\]\(", block, flags=re.MULTILINE)
    assert rows == [str(number) for number in range(1, 101)]
    assert "\n\n| [P90]" not in block
    assert "\n\n| [P96]" not in block


def test_p100_roadmap_frontier_language_is_current() -> None:
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    assert "## 5. Current frontier and remaining scientific boundary" in roadmap
    assert "None of P71-P100 identifies a latent variable with consciousness." in roadmap
    assert "After P89, the target-side chain" not in roadmap
    assert "None of P71-P95" not in roadmap


def test_static_reader_sources_are_p100_current() -> None:
    research_map = (ROOT / "website" / "research-map.html").read_text(encoding="utf-8")
    plain = (ROOT / "website" / "plain-language.html").read_text(encoding="utf-8")
    assert "through Proposition 100" in research_map
    assert "through Proposition 99" not in research_map
    assert "A 100-result sufficiency and falsification architecture" in plain
    assert "The 100-result proposition program asks" in plain
    assert "The current theorem frontier is P100." in plain
    assert "A 99-result sufficiency and falsification architecture" not in plain
    assert "The 99-result proposition program asks" not in plain
    assert "The current theorem frontier is P99." not in plain
