import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"


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


def test_p79_is_auditable_from_deep_reader_surfaces() -> None:
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    traceability = (DOCS / "research_traceability_index.md").read_text(encoding="utf-8")
    detail = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    equation_map = (DOCS / "equation_and_citation_map.md").read_text(encoding="utf-8")
    website_map = (ROOT / "website" / "research-map.html").read_text(encoding="utf-8")
    atlas = (ROOT / "website" / "visual-atlas.html").read_text(encoding="utf-8")

    assert "proposition_79_certified_sampling_radius.md" in roadmap
    assert "P79 certified rational sampling-radius envelope" in navigation
    assert "proposition_79_certified_sampling_radius.md" in traceability
    assert "p79_equation_provenance.md" in traceability
    assert "p79_certified_sampling_radius.svg" in traceability
    assert "**P79** closes the numerical-direction gap" in detail
    assert "# P79 certified rational sampling-radius envelope" in equation_map
    assert "proposition_79_certified_sampling_radius.md" in website_map
    assert "p79_certified_sampling_radius.svg" in atlas


def test_landing_page_routes_to_traceability_instead_of_repeating_p79_derivation() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/research_traceability_index.md" in readme
    assert "docs/theorem_roadmap.md" in readme
    assert "docs/reproducibility.md" in readme
    assert "## 1.13 P79: certified rational sampling-radius envelope" not in readme
    assert "p79_certified_sampling_radius.svg" not in readme


def test_p79_proof_explains_why_rounding_direction_matters() -> None:
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


def test_p79_release_history_survives_later_frontiers() -> None:
    readme = README.read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    frontier = _frontier()
    version = _project_version()

    assert f"version: {version}" in cff
    assert f"version      = {{{version}}}" in bib
    assert f"v{version}" in readme
    assert f"Current documented theorem frontier: P{frontier}" in cff
    assert f"{frontier} proposition-level results" in readme
    assert f"The theorem frontier is P{frontier}." in readme
    assert f"| Public theorem frontier | **P{frontier}** |" in readme
    assert f"Read the complete P1 to P{frontier} detailed proposition record" in readme

    figure_match = re.search(r"(\d+) equation-driven quantitative figures", readme)
    assert figure_match is not None
    assert int(figure_match.group(1)) >= 69

    assert "Proposition 79" in citation
    assert "# 0.79.0 - 2026-09-11" in changelog
    assert "# 0.81.0 - 2026-09-11" in changelog
    assert "Proposition 79" in changelog

    match = re.search(r"P1 through P(\d+) with explicit dependency branches", readme)
    assert match is not None
    assert int(match.group(1)) == frontier


def test_p79_preserves_one_sided_certification_logic() -> None:
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


def test_p78_release_history_survives_later_frontier() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    assert "# 0.78.0 - 2026-09-10" in changelog
    assert "Proposition 78" in changelog
    assert "| [P78]" in roadmap


def test_p79_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p79-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p79_publication_patch.py").exists()
