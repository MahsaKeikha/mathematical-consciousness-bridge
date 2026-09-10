import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"


def _max_proposition_number() -> int:
    numbers = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_readme_theorem_roadmap_advertises_current_frontier():
    readme = README.read_text(encoding="utf-8")
    frontier = _max_proposition_number()
    assert f"P1 through P{frontier} with explicit dependency branches" in readme


def test_readme_links_every_proposition_at_current_calibration_frontier():
    readme = README.read_text(encoding="utf-8")
    required = (
        "docs/proposition_61_exact_integer_transition_calibration.md",
        "docs/proposition_62_heterogeneous_cost_transition_calibration.md",
        "docs/proposition_63_exact_heterogeneous_integer_calibration.md",
        "docs/proposition_64_fast_heterogeneous_integer_approximation.md",
    )
    for link in required:
        assert link in readme


def test_public_navigation_documents_agree_on_current_frontier():
    frontier = _max_proposition_number()
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")

    assert f"P1 through P{frontier}" in readme
    assert f"[P{frontier}](proposition_{frontier}_" in roadmap
    assert f"| P{frontier} |" in navigation


def test_public_reader_navigation_uses_no_forbidden_dash_characters():
    readme = README.read_text(encoding="utf-8")
    assert "\u2013" not in readme
    assert "\u2014" not in readme
