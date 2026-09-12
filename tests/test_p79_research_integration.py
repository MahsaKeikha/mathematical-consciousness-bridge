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


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def _project_version() -> str:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_p79_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_79_certified_sampling_radius.md",
        DOCS / "p79_equation_provenance.md",
        DOCS / "figures" / "p79_certified_sampling_radius.svg",
        ROOT / "src" / "consciousness_bridge" / "certified_sampling_radius.py",
        ROOT / "tests" / "test_certified_sampling_radius.py",
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

    assert "## 1.13 P79: certified rational sampling-radius envelope" in readme
    assert "proposition_79_certified_sampling_radius.md" in readme
    assert "p79_equation_provenance.md" in readme
    assert "p79_certified_sampling_radius.svg" in readme

    assert "### P79: certified rational sampling-radius envelope" in roadmap
    assert "proposition_79_certified_sampling_radius.md" in roadmap
    assert "| [P79]" in roadmap

    assert "P79 certified rational sampling-radius envelope" in navigation
    assert "| P79 |" in navigation
    assert "**P79** closes the numerical-direction gap" in detail
    assert "# P79 certified rational sampling-radius envelope" in equation_map

    assert "p79_certified_sampling_radius.svg" in website
    assert "P79: Certified rational sampling-radius envelope" in research_map
    assert "p79_certified_sampling_radius.svg" in atlas


def test_p79_plain_language_explains_why_rounding_direction_matters() -> None:
    plain = _plain_language_section(README.read_text(encoding="utf-8"))
    required = (
        "P79 closes a smaller but important numerical-certification gap",
        "ordinary floating-point evaluation",
        "exact rational upper bound",
        "positive convergent series",
        "integer arithmetic",
        "P78 lower bound is strictly larger than the P79 upper bound",
        "does not make non-rejection into model acceptance",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in plain, token

    for forbidden in ("$$", "\\boxed", "\\mathcal", "\\widehat", "\\theta"):
        assert forbidden not in plain, forbidden


def test_p79_release_history_survives_later_frontiers() -> None:
    readme = README.read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    frontier = _frontier()
    version = _project_version()

    # Current release metadata and the current theorem frontier are separate
    # concepts. During theorem development the frontier may advance before the
    # next formal release version is cut, but all public metadata must agree on
    # each concept independently.
    assert f"version: {version}" in cff
    assert f"version      = {{{version}}}" in bib
    assert f"v{version}" in readme
    assert f"Current documented theorem frontier: P{frontier}" in cff
    assert f"{frontier} proposition-level results" in readme
    assert f"The theorem frontier is P{frontier}." in readme
    assert f"| Public theorem frontier | **P{frontier}** |" in readme
    assert f"Read the complete P1 to P{frontier} detailed proposition record" in readme

    figure_match = re.search(
        r"(\d+) equation-driven quantitative figures",
        readme,
    )
    assert figure_match is not None
    assert int(figure_match.group(1)) >= 69

    # P79 and intervening formal releases remain part of the permanent citable
    # history after the theorem frontier advances.
    assert "Proposition 79" in citation
    assert "# 0.79.0 - 2026-09-11" in changelog
    assert "# 0.81.0 - 2026-09-11" in changelog
    assert "Proposition 79" in changelog

    match = re.search(r"P1 through P(\d+) with explicit dependency branches", readme)
    assert match is not None
    assert int(match.group(1)) == frontier


def test_p79_preserves_one_sided_certification_logic() -> None:
    readme = README.read_text(encoding="utf-8")
    proof = (DOCS / "proposition_79_certified_sampling_radius.md").read_text(
        encoding="utf-8"
    )
    source = (
        ROOT / "src" / "consciousness_bridge" / "certified_sampling_radius.py"
    ).read_text(encoding="utf-8")

    for token in (
        "mathematically valid *upper bound*",
        "ordinary floating-point approximation",
        "exact rational arithmetic",
        "does not identify any latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    ):
        assert token in source, token

    for token in (
        "mathematically valid upper bound",
        "Converting an ordinary floating-point evaluation",
        "P79 supplies an **upper** bound on sampling uncertainty",
        "does not validate a model when rejection fails",
        "The physical-to-experiential bridge remains open.",
    ):
        assert token in proof, token

    assert "P78 lower-bounds model distance" in readme
    assert "P79 upper-bounds the P77 sampling radius" in readme


def test_p78_release_history_survives_p79_frontier() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    assert "# 0.78.0 - 2026-09-10" in changelog
    assert "Proposition 78" in changelog
    assert "## 1.12 P78: certified continuous separation for the P75 model family" in readme
    assert "| [P78]" in roadmap


def test_p79_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p79-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p79_publication_patch.py").exists()
