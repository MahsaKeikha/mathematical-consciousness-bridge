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


def _project_version(pyproject: str) -> tuple[int, int, int]:
    match = re.search(r'^version = "(\d+)\.(\d+)\.(\d+)"$', pyproject, re.MULTILINE)
    assert match is not None
    return tuple(int(value) for value in match.groups())


def test_p77_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_77_full_law_model_set_separation.md",
        DOCS / "p77_equation_provenance.md",
        DOCS / "figures" / "p77_full_law_model_set_separation.svg",
        ROOT / "src" / "consciousness_bridge" / "full_law_model_set_separation.py",
        ROOT / "tests" / "test_full_law_model_set_separation.py",
        ROOT / "tests" / "test_p77_figure_geometry.py",
    )
    for path in required:
        assert path.exists(), path


def test_p77_is_exposed_across_public_research_surfaces() -> None:
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    detail = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    equation_map = (DOCS / "equation_and_citation_map.md").read_text(encoding="utf-8")
    website = (WEBSITE / "index.html").read_text(encoding="utf-8")
    research_map = (WEBSITE / "research-map.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    assert "## 1.11 P77: full-law confidence regions can reject the complete declared model set" in readme
    assert "proposition_77_full_law_model_set_separation.md" in readme
    assert "p77_equation_provenance.md" in readme
    assert "p77_full_law_model_set_separation.svg" in readme

    assert "### P77: finite-sample full-law model-set separation" in roadmap
    assert "proposition_77_full_law_model_set_separation.md" in roadmap
    assert "| P77 |" in navigation
    assert "P77 finite-sample full-law model-set separation" in navigation
    assert "**P77** closes the finite-data full-law gap left explicit by P76" in detail
    assert "# P77 finite-sample full-law model-set separation" in equation_map
    assert "p77_full_law_model_set_separation.svg" in website
    assert "P77" in research_map
    assert "p77_full_law_model_set_separation.svg" in atlas


def test_p77_plain_language_explains_full_law_logic_without_equations() -> None:
    readme = README.read_text(encoding="utf-8")
    plain = _plain_language_section(readme)

    required = (
        "P77 closes the next logical gap",
        "any distribution allowed by the entire declared measurement model",
        "whole confidence region around the observed distribution",
        "finding one imperfect best-fitting model is not enough",
        "mathematically certified lower bound",
        "equivalent certified proof",
        "stronger full-distribution standard",
        "physical-to-experiential bridge itself remains open",
    )
    for token in required:
        assert token in plain, token

    forbidden = (
        "$$",
        "\\boxed",
        "\\begin",
        "\\frac",
        "\\mathcal",
        "\\widehat",
    )
    for token in forbidden:
        assert token not in plain, token


def test_p77_release_history_survives_later_frontiers() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

    assert _project_version(pyproject) >= (0, 77, 0)
    assert "P77" in cff
    assert "P77" in bib
    assert "P77" in citation
    assert "# 0.77.0 - 2026-09-10" in changelog
    assert "Proposition 77" in changelog


def test_p77_certification_boundary_is_preserved() -> None:
    readme = README.read_text(encoding="utf-8")
    proof = (DOCS / "proposition_77_full_law_model_set_separation.md").read_text(
        encoding="utf-8"
    )
    source = (
        ROOT / "src" / "consciousness_bridge" / "full_law_model_set_separation.py"
    ).read_text(encoding="utf-8")

    source_required = (
        "certified *lower* bound",
        "upper bound on distance",
        "cannot by itself certify rejection",
        "non-rejection is not model acceptance",
        "does not identify a latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in source_required:
        assert token in source, token

    proof_required = (
        "confidence-region inversion",
        "upper bound",
        "cannot be used as though it were a lower bound",
        "non-rejection means model acceptance",
        "physical-to-experiential bridge has been solved",
        "The physical-to-experiential bridge remains open.",
    )
    for token in proof_required:
        assert token in proof, token

    assert "A candidate best-fit model" in readme
    assert "It cannot by itself certify rejection" in readme


def test_p77_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p77-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p77_publication_patch.py").exists()
