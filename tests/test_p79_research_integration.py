import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def test_p79_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_79_joint_statistical_computational_power.md",
        DOCS / "p79_equation_provenance.md",
        DOCS / "figures" / "p79_joint_statistical_computational_power.svg",
        ROOT / "src" / "consciousness_bridge" / "joint_statistical_computational_power.py",
        ROOT / "tests" / "test_joint_statistical_computational_power.py",
        ROOT / "tests" / "test_p79_figure_geometry.py",
    )
    for path in required:
        assert path.exists(), path


def test_p79_is_exposed_across_public_research_surfaces() -> None:
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    detail = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    equation_map = (DOCS / "equation_and_citation_map.md").read_text(encoding="utf-8")
    website = (WEBSITE / "index.html").read_text(encoding="utf-8")
    research_map = (WEBSITE / "research-map.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    assert "## 1.13 P79: joint statistical-computational power for full-law rejection" in readme
    assert "proposition_79_joint_statistical_computational_power.md" in readme
    assert "p79_equation_provenance.md" in readme
    assert "p79_joint_statistical_computational_power.svg" in readme

    assert "### P79: joint statistical-computational power" in roadmap
    assert "proposition_79_joint_statistical_computational_power.md" in roadmap
    assert "| P79 |" in navigation
    assert "P79 joint statistical-computational power" in navigation
    assert "**P79** adds a prospective joint power budget" in detail
    assert "# P79 joint statistical-computational power" in equation_map
    assert "p79_joint_statistical_computational_power.svg" in website
    assert "P79: Joint statistical-computational power" in research_map
    assert "p79_joint_statistical_computational_power.svg" in atlas


def test_p79_plain_language_explains_joint_power_without_equations() -> None:
    readme = README.read_text(encoding="utf-8")
    plain = _plain_language_section(readme)
    required = (
        "P79 asks how much statistical evidence and computational precision are jointly enough",
        "rejection level",
        "desired power",
        "optimization error",
        "explicit overlap witness",
        "unresolved",
        "does not mean the true power is zero",
        "prespecified or justified independently",
        "physical-to-experiential bridge itself remains open",
    )
    for token in required:
        assert token in plain, token

    for forbidden in ("$$", "\\boxed", "\\frac", "\\mathcal", "\\widehat"):
        assert forbidden not in plain, forbidden


def test_p79_release_metadata_and_counts_are_consistent() -> None:
    readme = README.read_text(encoding="utf-8")
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

    assert 'version = "0.79.0"' in pyproject
    assert "version: 0.79.0" in cff
    assert "Current documented theorem frontier: P79" in cff
    assert "version      = {0.79.0}" in bib
    assert "Proposition 79" in citation
    assert "# 0.79.0 - 2026-09-10" in changelog
    assert "79 proposition-level results" in readme
    assert "67 equation-driven quantitative figures" in readme
    assert "The theorem frontier is P79." in readme
    assert "| Public theorem frontier | **P79** |" in readme
    assert "Read the complete P1 to P79 detailed proposition record" in readme

    match = re.search(r"P1 through P(\d+) with explicit dependency branches", readme)
    assert match is not None
    assert int(match.group(1)) == 79


def test_p79_power_and_scientific_boundaries_are_preserved() -> None:
    proof = (DOCS / "proposition_79_joint_statistical_computational_power.md").read_text(
        encoding="utf-8"
    )
    source = (
        ROOT / "src" / "consciousness_bridge" / "joint_statistical_computational_power.py"
    ).read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    source_required = (
        "eps_alpha + eps_beta + eta",
        "planning margin Delta_0 must be prespecified or justified independently",
        "planning calculation, not a formal",
        "does not identify any latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in source_required:
        assert token in source, token

    proof_required = (
        "Type I error at most \\(\\alpha\\)",
        "power at least \\(1-\\beta\\)",
        "Failure of the sufficient power inequality means the test has zero power",
        "This is an overlap witness. It is **not** evidence that the model is true.",
        "The physical-to-experiential bridge remains open.",
    )
    for token in proof_required:
        assert token in proof, token

    assert "failed sufficient power certificate" in readme
    assert "does not imply that actual power is zero" in readme


def test_p79_figure_sequence_is_unique_around_frontier() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "**Figure 13. P78 certified continuous model separation.**" in readme
    assert "**Figure 14. P79 joint statistical-computational power.**" in readme
    assert "**Figure 15. Anatomy of the operational physical candidate.**" in readme
    assert "**Figure 28. Evidence provenance.**" in readme
    figure_numbers = [int(value) for value in re.findall(r"\*\*Figure (\d+)\.", readme)]
    assert len(figure_numbers) == len(set(figure_numbers))


def test_p79_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p79-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p79_publication_patch.py").exists()
