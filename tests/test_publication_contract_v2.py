from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_first_reader_surfaces_are_layered_not_archives() -> None:
    readme = _read(ROOT / "README.md")
    start = _read(ROOT / "START_HERE.md")
    navigation = _read(DOCS / "research_navigation.md")

    assert len(readme) < 12_000
    assert len(start) < 14_000
    for path in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
    ):
        assert path in readme
    assert "You do not need to read 88 propositions" in start
    assert "does **not** duplicate the full 88 proposition index" in navigation
    assert "Detailed Proposition Record" in navigation
    assert "Theorem Roadmap" in navigation


def test_current_frontier_release_and_open_boundary_are_consistent() -> None:
    readme = _read(ROOT / "README.md")
    start = _read(ROOT / "START_HERE.md")
    roadmap = _read(DOCS / "theorem_roadmap.md")
    navigation = _read(DOCS / "research_navigation.md")
    citation = _read(ROOT / "CITATION.md")
    glossary = _read(DOCS / "glossary.md")

    for text in (readme, start, roadmap, navigation, citation, glossary):
        assert "P88" in text
    assert "v0.82.0" in readme
    assert "v0.82.0" in start
    assert "physical-to-experiential bridge" in readme
    assert "remains open" in readme
    assert "## Current theorem frontier: P88" in citation
    assert "## Historical theorem frontier: P85" in citation
    assert "## Historical theorem frontier: P87" in citation
    assert "## Current theorem frontier: P85" not in citation
    assert "The current documented theorem frontier is **P87**" not in citation
    assert "current public frontier is **P88**" in glossary


def test_complete_proposition_record_is_canonical_archive() -> None:
    detail = _read(DOCS / "detailed_proposition_record.md")
    roadmap = _read(DOCS / "theorem_roadmap.md")
    assert "Complete P1 to P88 chronology" in detail
    assert "P1 through P88 with explicit dependency branches" in roadmap
    for number in range(1, 89):
        assert list(DOCS.glob(f"proposition_{number}_*.md")), (
            f"missing P{number} proposition document"
        )
        assert f"P{number}" in detail, f"P{number} missing from detailed record"


def test_specialist_surfaces_own_specialist_detail() -> None:
    figures = _read(DOCS / "figure_catalog.md")
    equations = _read(DOCS / "equation_and_citation_map.md")
    fundamental = _read(DOCS / "fundamental_theory_consciousness_program.md")
    calibration = _read(DOCS / "calibration_optimization_frontier_p61_p70.md")

    assert "Complete Figure Catalog" in figures
    assert "P88" in figures
    assert "P88" in equations
    assert "no experimentally established Theory of Everything" in fundamental
    assert "Proposition 70" in calibration


def test_current_frontier_has_proof_code_test_provenance_and_figure() -> None:
    sources = _read(WEBSITE / "sources.html")
    assert 'id="p88-source"' in sources
    assert "Current theorem source · P88" in sources
    for token in (
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "p88_equation_provenance.md",
        "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg",
    ):
        assert token in sources
    assert "Previous theorem source · P87" in sources


def test_overview_orients_to_all_three_research_programs_before_p88() -> None:
    overview = _read(WEBSITE / "index.html")
    journey = overview.index('id="project-journey"')
    p88 = overview.index('id="p88-frontier"')
    assert journey < p88
    for token in (
        "The whole research program in three stages",
        "Research I",
        "Research II",
        "Research III",
        "spatiotemporal-observer-math",
        "88 proposition-level results",
        "measurement-science.html",
        "None of these stages by itself establishes the final physical-to-experiential bridge.",
    ):
        assert token in overview


def test_research_lineage_preserves_counts_and_scientific_boundaries() -> None:
    lineage = _read(WEBSITE / "research-lineage.html")
    for token in (
        "58</strong><span>proposition-level statements",
        "45</strong><span>reproducible experiments",
        "33</strong><span>scientific result figures",
        "223</strong><span>claim-level tests",
        "88</strong><span>proposition-level results",
        "Research III · consciousness measurement science",
        "A recovered subsystem is not automatically a conscious subject",
        "Bridge remains an independently testable open problem",
    ):
        assert token in lineage


def test_research_map_and_plain_language_use_current_p88_state() -> None:
    research_map = _read(WEBSITE / "research-map.html")
    plain = _read(WEBSITE / "plain-language.html")
    assert "P88" in research_map
    assert "P73-P88" in research_map
    assert "Research II proposition-level results" in plain
    assert "current Research II theorem frontier" in plain
    assert "P88 is a checkpoint, not the destination" in plain


def test_citation_surface_is_professional_and_current() -> None:
    citation = _read(ROOT / "CITATION.md")
    readme = _read(ROOT / "README.md")
    assert "## Preferred scholarly citation" in citation
    assert "CITATION.md" in readme
    assert "CITATION.cff" in readme
    assert "Version 0.82.0" in citation
    assert "current documented frontier, P88" in citation
