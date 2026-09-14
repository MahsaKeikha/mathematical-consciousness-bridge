import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
FRONTIER = DOCS / "calibration_optimization_frontier_p61_p70.md"


def _max_proposition_number() -> int:
    numbers = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)








def test_public_reader_navigation_uses_no_forbidden_dash_characters():
    readme = README.read_text(encoding="utf-8")
    assert "\u2013" not in readme
    assert "\u2014" not in readme
