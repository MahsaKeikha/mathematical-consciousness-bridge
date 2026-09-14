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

    assert len(readme) < 14_000
    assert len(start) < 15_000
    for path in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
    ):
        assert path in readme
    assert "89" in start
    assert "does **not** duplicate the full 89 proposition index" in navigation
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
        assert "P89" in text
    assert "v0.82.0" in readme
    assert "v0.82.0" in start
    assert "physical-to-experiential bridge" in readme
    assert "Final bridge from physical description to experience:** open" in readme
    assert "## Current theorem frontier: P89" in citation
    assert "## Historical theorem frontier: P88" in citation
    assert "## Historical theorem frontier: P87" in citation
    assert "## Current theorem frontier: P88" not in citation
    assert "current public frontier is **P89**" in glossary


def test_complete_proposition_record_is_canonical_archive() -> None:
    detail = _read(DOCS / "detailed_proposition_record.md")
    roadmap = _read(DOCS / "theorem_roadmap.md")
    assert "Complete P1 to P89 chronology" in detail
    assert "P1 through P89 with explicit dependency branches" in roadmap
    for number in range(1, 90):
        assert list(DOCS.glob(f"proposition_{number}_*.md")), (
            f"missing P{number} proposition document"
        )
    for marker in (
        "P1-P10",
        "P11",
        "P19",
        "P25-P30",
        "P38",
        "P45",
        "P54",
        "P59",
        "P71",
        "P72",
        "P73",
        "P88",
        "P89",
    ):
        assert marker in detail, f"{marker} branch missing from detailed record"


def test_specialist_surfaces_own_specialist_detail() -> None:
    figures = _read(DOCS / "figure_catalog.md")
    equations = _read(DOCS / "equation_and_citation_map.md")
    fundamental = _read(DOCS / "fundamental_theory_consciousness_program.md")
    calibration = _read(DOCS / "calibration_optimization_frontier_p61_p70.md")

    assert "Complete Figure Catalog" in figures
    assert "P89" in figures
    assert "p89_complete_linear_parity_duality.svg" in figures
    assert "# Equation and Citation Map" in equations
    assert "p89_equation_provenance.md" in equations
    assert "bridge hypotheses" in equations
    assert "no experimentally established Theory of Everything" in fundamental
    assert "Proposition 70" in calibration


def test_current_frontier_has_proof_code_test_provenance_and_figure() -> None:
    sources = _read(WEBSITE / "sources.html")
    assert 'id="p89-source"' in sources
    assert "Current theorem source · P89" in sources
    for token in (
        "proposition_89_complete_linear_parity_duality.md",
        "p89_equation_provenance.md",
        "complete_linear_parity_duality.py",
        "test_complete_linear_parity_duality.py",
        "p89_complete_linear_parity_duality.svg",
    ):
        assert token in sources
    assert "Previous theorem source · P88" in sources


def test_overview_orients_to_all_three_research_programs_before_p89() -> None:
    overview = _read(WEBSITE / "index.html")
    dashboard = overview.index('class="research-dashboard"')
    journey = overview.index('id="project-journey"')
    p89 = overview.index('id="p89-frontier"')
    assert dashboard < journey < p89
    for token in (
        "The whole research program in three stages",
        "Research I · Physical-system identification",
        "58</strong><span>proposition-level statements",
        "45 experiments · 33 figures · 223 claim-level tests",
        "spatiotemporal-observer-math",
        "Research II · Bridge sufficiency and falsification",
        "89</strong><span>proposition-level results",
        "P89 current theorem frontier · v0.82.0",
        "research-map.html",
        "Research III · Consciousness measurement science",
        "34</strong><span>tests in each CI job",
        "5 targets · 2 research arms · M0-M7 claim ladder",
        "measurement-science.html",
        "Open</strong><span>physical-to-experiential bridge",
        "None of these stages by itself establishes the final physical-to-experiential bridge.",
    ):
        assert token in overview


def test_plain_language_and_start_here_are_three_stage_reader_entries() -> None:
    plain = _read(WEBSITE / "plain-language.html")
    start = _read(WEBSITE / "start-here.html")

    for source in (plain, start):
        for token in ("Research I", "Research II", "Research III"):
            assert token in source
        assert "89 results · current frontier P89" in source
        assert "physical-to-experiential bridge" in source

    assert 'id="three-stage-progress"' in plain
    assert "What the whole research program is doing" in plain
    assert "The proposition sequence belongs to Research II. It is one stage of a larger program" in plain
    assert 'id="program-stages"' in start
    assert "Start with the three stages before entering the proposition chronology" in start
    assert "The 89 Research II propositions by scientific role" in start
    assert "Inside Research II" in start


def test_research_lineage_preserves_counts_and_scientific_boundaries() -> None:
    lineage = _read(WEBSITE / "research-lineage.html")
    for token in (
        "58</strong><span>proposition-level statements",
        "45</strong><span>reproducible experiments",
        "33</strong><span>scientific result figures",
        "223</strong><span>claim-level tests",
        "89</strong><span>proposition-level results",
        "P89</strong><span>current theorem frontier",
        "Research III · consciousness measurement science",
        "A recovered subsystem is not automatically a conscious subject",
        "Bridge remains an independently testable open problem",
    ):
        assert token in lineage


def test_research_map_and_plain_language_use_current_p89_state() -> None:
    research_map = _read(WEBSITE / "research-map.html")
    plain = _read(WEBSITE / "plain-language.html")
    assert "P89" in research_map
    assert "P75-P89" in research_map or "P73-P89" in research_map
    assert 'id="p89-research-map"' in research_map
    assert "5/168" in research_map
    assert "Research II" in plain
    assert "current frontier P89" in plain
    assert "Research III" in plain


def test_citation_surface_is_professional_and_current() -> None:
    citation = _read(ROOT / "CITATION.md")
    readme = _read(ROOT / "README.md")
    assert "## Preferred scholarly citation" in citation
    assert "CITATION.md" in readme
    assert "CITATION.cff" in readme
    assert "Version 0.82.0" in citation
    assert "current documented frontier, P89" in citation
