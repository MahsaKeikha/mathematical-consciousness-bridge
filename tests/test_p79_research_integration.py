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
        DOCS / "proposition_79_bounded_target_view_dependence.md",
        DOCS / "p79_equation_provenance.md",
        DOCS / "figures" / "p79_bounded_target_view_dependence.svg",
        ROOT / "src" / "consciousness_bridge" / "bounded_target_view_dependence.py",
        ROOT / "tests" / "test_bounded_target_view_dependence.py",
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

    assert "## 1.13 P79: bounded target-view dependence does not automatically erase rejection" in readme
    assert "proposition_79_bounded_target_view_dependence.md" in readme
    assert "p79_equation_provenance.md" in readme
    assert "p79_bounded_target_view_dependence.svg" in readme
    assert "### P79: robust rejection under bounded target-view dependence" in roadmap
    assert "proposition_79_bounded_target_view_dependence.md" in roadmap
    assert "| P79 |" in navigation
    assert "P79 bounded target-view dependence" in navigation
    assert "**P79** weakens the exact conditional-independence assumption" in detail
    assert "# P79 bounded target-view dependence robustness" in equation_map
    assert "p79_bounded_target_view_dependence.svg" in website
    assert "P79: Bounded target-view dependence robustness" in research_map
    assert "p79_bounded_target_view_dependence.svg" in atlas


def test_p79_plain_language_is_complete_and_equation_free() -> None:
    plain = _plain_language_section(README.read_text(encoding="utf-8"))
    required = (
        "P79 addresses another assumption behind that target-measurement model",
        "residual dependence even after conditioning on the latent target state",
        "declare or independently calibrate a quantitative dependence allowance",
        "ordinary sampling uncertainty and the allowed residual dependence",
        "must not be chosen from the same discrepancy merely to avoid rejection",
        "independent scientific justification",
        "physical-to-experiential bridge itself remains open",
    )
    for token in required:
        assert token in plain, token
    for token in ("$$", "\\boxed", "\\mathcal", "\\rho", "\\varepsilon"):
        assert token not in plain, token


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


def test_p79_certification_boundary_is_preserved() -> None:
    readme = README.read_text(encoding="utf-8")
    proof = (DOCS / "proposition_79_bounded_target_view_dependence.md").read_text(
        encoding="utf-8"
    )
    source = (
        ROOT / "src" / "consciousness_bridge" / "bounded_target_view_dependence.py"
    ).read_text(encoding="utf-8")

    source_required = (
        "must be justified independently or declared before the rejection test",
        "must not be tuned from the same observed discrepancy merely to avoid rejection",
        "L > eps + rho",
        "non-rejection is inconclusive and is not model validation",
        "does not identify a latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in source_required:
        assert token in source, token

    proof_required = (
        "independently justified upper bound",
        "must not be tuned from the same data merely to force rejection",
        "L_p>\\varepsilon_p+\\bar\\rho_p",
        "A failure to reject under the enlarged dependence allowance is inconclusive",
        "The physical-to-experiential bridge remains open.",
    )
    for token in proof_required:
        assert token in proof, token

    assert "must not be chosen from the same discrepancy merely to avoid rejection" in readme
    assert "independently justified dependence allowance" in readme


def test_p79_navigation_has_one_contiguous_reader_item_and_current_frontier() -> None:
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    assert "15. [P79 bounded target-view dependence]" in navigation
    assert "The current theorem frontier is P79" in navigation
    assert "| Bounded target-view dependence robustness | P79 |" in navigation
    assert "[P79 figure](figures/p79_bounded_target_view_dependence.svg)" in navigation
    assert "[P79 provenance record](p79_equation_provenance.md)" in navigation


def test_p79_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p79-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p79_publication_patch.py").exists()
