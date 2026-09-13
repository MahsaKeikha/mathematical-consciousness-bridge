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


def test_readme_theorem_roadmap_advertises_current_frontier():
    readme = README.read_text(encoding="utf-8")
    frontier = _max_proposition_number()
    assert f"P1 through P{frontier} with explicit dependency branches" in readme
    assert "docs/theorem_roadmap.md" in readme


def test_calibration_frontier_remains_complete_but_is_not_dumped_on_homepage():
    readme = README.read_text(encoding="utf-8")
    frontier = FRONTIER.read_text(encoding="utf-8")
    required = (
        "proposition_61_exact_integer_transition_calibration.md",
        "proposition_62_heterogeneous_cost_transition_calibration.md",
        "proposition_63_exact_heterogeneous_integer_calibration.md",
        "proposition_64_fast_heterogeneous_integer_approximation.md",
        "proposition_65_lower_bounded_heterogeneous_calibration.md",
        "proposition_66_residual_exact_calibration_augmentation.md",
        "proposition_67_global_integer_optimality_certificate.md",
        "proposition_68_lagrangian_optimality_gap.md",
        "proposition_69_dual_optimal_multiplier.md",
        "proposition_70_primal_dual_gap_decomposition.md",
    )
    for link in required:
        assert link in frontier

    # The landing page should route readers to deeper navigation rather than
    # duplicating the P61-P70 ledger.
    assert "docs/research_traceability_index.md" in readme
    assert sum(link in readme for link in required) <= 1


def test_public_navigation_documents_agree_on_current_frontier():
    frontier = _max_proposition_number()
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    traceability = (DOCS / "research_traceability_index.md").read_text(encoding="utf-8")

    assert f"P1 through P{frontier}" in readme
    assert f"[P{frontier}](proposition_{frontier}_" in roadmap
    assert f"| Held-out validation | P{frontier} |" in navigation
    assert f"**P{frontier} -" in traceability


def test_navigation_is_reader_first_but_preserves_full_audit_routes():
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    assert "Choose by intent" in navigation
    assert "Complete proposition index" in navigation
    assert "theorem_roadmap.md" in navigation
    assert "detailed_proposition_record.md" in navigation
    assert "equation_and_citation_map.md" in navigation
    assert "research_traceability_index.md" in navigation


def test_public_reader_navigation_uses_no_forbidden_dash_characters():
    readme = README.read_text(encoding="utf-8")
    assert "\u2013" not in readme
    assert "\u2014" not in readme
