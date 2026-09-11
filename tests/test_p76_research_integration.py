from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def test_p76_is_exposed_across_public_research_surfaces() -> None:
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    detail = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    site = (WEBSITE / "index.html").read_text(encoding="utf-8")
    research_map = (WEBSITE / "research-map.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    assert "## 1.10 P76: finite data must separate model failure from sampling noise" in readme
    assert "docs/figures/p76_finite_sample_target_model_adequacy.svg" in readme
    assert "P1 through P76 with explicit dependency branches" in readme
    assert "76 proposition-level results" in readme
    assert "64 equation-driven quantitative figures" in readme

    assert "current documented theorem frontier is **P76**" in roadmap
    assert "P76: finite data must separate adequacy failure from sampling noise" in roadmap
    assert "proposition_76_finite_sample_target_model_adequacy.md" in roadmap

    assert "current documented theorem frontier is **P76**" in navigation
    assert "P76 finite-sample target-model adequacy rejection" in navigation
    assert "p76_equation_provenance.md" in navigation

    assert "Complete P1 to P76 chronology" in detail
    assert "**P76** converts the tracked P75 population adequacy restrictions" in detail

    assert "<strong>76</strong><span>proposition-level results</span>" in site
    assert "p76_finite_sample_target_model_adequacy.svg" in site
    assert "proposition_76_finite_sample_target_model_adequacy.md" in site
    assert "P76" in research_map
    assert "p76_finite_sample_target_model_adequacy.svg" in research_map
    assert "p76_finite_sample_target_model_adequacy.svg" in atlas


def test_p76_release_and_provenance_surfaces_are_synchronized() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    equation_map = (DOCS / "equation_and_citation_map.md").read_text(encoding="utf-8")
    provenance = (DOCS / "p76_equation_provenance.md").read_text(encoding="utf-8")

    assert 'version = "0.76.0"' in pyproject
    assert "version: 0.76.0" in cff
    assert "Current documented theorem frontier: P76" in cff
    assert "version      = {0.76.0}" in bib
    assert "Current documented theorem frontier: P76" in bib
    assert "Version **0.76.0** and theorem frontier **P76**" in citation
    assert changelog.startswith("# 0.76.0 - 2026-09-10")
    assert "# P76 finite-sample target-model adequacy rejection" in equation_map
    assert "## Repository-specific contribution" in provenance


def test_p76_plain_language_and_scientific_boundaries_remain_explicit() -> None:
    readme = README.read_text(encoding="utf-8")
    source = (
        ROOT / "src" / "consciousness_bridge" / "finite_sample_target_model_adequacy.py"
    ).read_text(encoding="utf-8")
    proof = (DOCS / "proposition_76_finite_sample_target_model_adequacy.md").read_text(
        encoding="utf-8"
    )

    plain_start = readme.index("# What this project is trying to achieve, in plain language")
    plain_end = readme.index("# Abstract", plain_start)
    plain = readme[plain_start:plain_end]

    assert "P76 asks the next practical question" in plain
    assert "ordinary sampling noise" in plain
    assert "non-rejection is not model acceptance" in plain
    assert "finite data are strong enough to demonstrate that one of those requirements has genuinely failed" in plain
    assert "physical-to-experiential bridge itself remains open" in plain

    assert "one shared sixteen-cell Hoeffding event" in source
    assert "not an acceptance test" in source
    assert "does not identify any latent state with consciousness" in source

    assert "does not establish the converse" in proof
    assert "not rejected by the current P76 certificate" in proof
    assert "The physical-to-experiential bridge remains open." in proof


def test_p76_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p76-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p76_publication_patch.py").exists()
