import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"
VERIFIER = ROOT / "scripts" / "verify_repository.py"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontier() -> int:
    verifier = _read(VERIFIER)
    match = re.search(r'^CURRENT_FRONTIER = "P(\d+)"$', verifier, flags=re.MULTILINE)
    assert match is not None
    return int(match.group(1))


def _frontier_proof(frontier: int) -> Path:
    matches = list(DOCS.glob(f"proposition_{frontier}_*.md"))
    assert len(matches) == 1
    return matches[0]


def test_first_reader_surfaces_are_layered_not_archives() -> None:
    frontier = _frontier()
    readme = _read(ROOT / "README.md")
    start = _read(ROOT / "START_HERE.md")
    navigation = _read(DOCS / "research_navigation.md")

    assert len(readme) < 16_000
    assert len(start) < 18_000
    for path in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
    ):
        assert path in readme
    assert str(frontier) in start
    assert f"the full {frontier} proposition index" in navigation
    assert "Detailed Proposition Record" in navigation
    assert "Theorem Roadmap" in navigation


def test_current_frontier_release_and_open_boundary_are_consistent() -> None:
    frontier = _frontier()
    label = f"P{frontier}"
    readme = _read(ROOT / "README.md")
    start = _read(ROOT / "START_HERE.md")
    roadmap = _read(DOCS / "theorem_roadmap.md")
    navigation = _read(DOCS / "research_navigation.md")
    citation = _read(ROOT / "CITATION.md")
    glossary = _read(DOCS / "glossary.md")

    for text in (readme, start, roadmap, navigation, citation, glossary):
        assert label in text
    assert "v0.82.0" in readme
    assert "v0.82.0" in start
    assert "physical-to-experiential bridge" in readme
    assert "Final bridge from physical description to experience:** open" in readme
    assert f"## Current theorem frontier: {label}" in citation
    assert "P91" in citation
    assert "P90" in citation
    assert "## Historical theorem frontier: P89" in citation
    assert "## Current theorem frontier: P91" not in citation
    assert label in glossary


def test_complete_proposition_record_is_canonical_archive() -> None:
    frontier = _frontier()
    detail = _read(DOCS / "detailed_proposition_record.md")
    roadmap = _read(DOCS / "theorem_roadmap.md")
    assert f"P1 through P{frontier} with explicit dependency branches" in roadmap
    for number in range(1, frontier + 1):
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
        "P88",
        "P89",
        "P90",
        "P91",
        "P93",
        f"P{frontier}",
    ):
        assert marker in detail, f"{marker} branch missing from detailed record"


def test_specialist_surfaces_own_specialist_detail() -> None:
    frontier = _frontier()
    figures = _read(DOCS / "figure_catalog.md")
    equations = _read(DOCS / "equation_and_citation_map.md")
    fundamental = _read(DOCS / "fundamental_theory_consciousness_program.md")
    calibration = _read(DOCS / "calibration_optimization_frontier_p61_p70.md")

    assert "Complete Figure Catalog" in figures
    assert f"P{frontier}" in figures
    assert f"p{frontier}_" in figures
    assert "# Equation and Citation Map" in equations
    assert f"p{frontier}_equation_provenance.md" in equations
    assert "bridge hypotheses" in equations
    assert "no experimentally established Theory of Everything" in fundamental
    assert "Proposition 70" in calibration


def test_current_frontier_has_proof_code_test_provenance_and_figure() -> None:
    frontier = _frontier()
    proof = _frontier_proof(frontier)
    sources = _read(WEBSITE / "sources.html")
    assert f'id="p{frontier}-source"' in sources
    assert f"P{frontier}" in sources
    assert proof.name in sources
    assert f"p{frontier}_equation_provenance.md" in sources
    assert f'id="p{frontier - 3}-source"' in sources or 'id="p91-source"' in sources


def test_overview_orients_to_all_three_research_programs_before_current_frontier() -> None:
    frontier = _frontier()
    overview = _read(WEBSITE / "index.html")
    dashboard = overview.index('class="research-dashboard"')
    journey = overview.index('id="project-journey"')
    current = overview.index(f'id="p{frontier}-frontier"')
    assert dashboard < journey < current
    for token in (
        "The whole research program in three stages",
        "Research I · Physical-system identification",
        "58</strong><span>proposition-level statements",
        "Research II · Bridge sufficiency and falsification",
        f"{frontier}</strong><span>proposition-level results",
        f"P{frontier} current theorem frontier · v0.82.0",
        f"Explore all {frontier} results",
        "research-map.html",
        "Research III · Consciousness measurement science",
        "measurement-science.html",
        "Open</strong><span>physical-to-experiential bridge",
        "None of these stages by itself establishes the final physical-to-experiential bridge.",
    ):
        assert token in overview


def test_plain_language_and_start_here_are_three_stage_reader_entries() -> None:
    frontier = _frontier()
    plain = _read(WEBSITE / "plain-language.html")
    start = _read(WEBSITE / "start-here.html")

    for source in (plain, start):
        for token in ("Research I", "Research II", "Research III"):
            assert token in source
        assert "physical-to-experiential bridge" in source

    assert f"{frontier} linked results · technical endpoint P{frontier}" in plain
    assert 'id="project-journey"' in plain
    assert "If you remember only three things" in plain
    assert re.search(r'id="p\\d+-reader-frontier"', plain) is None
    assert f"{frontier} results · current frontier P{frontier}" in start
    assert 'id="program-stages"' in start
    assert f"The {frontier} Research II propositions by scientific role" in start
    assert "Inside Research II" in start


def test_research_lineage_preserves_counts_and_scientific_boundaries() -> None:
    frontier = _frontier()
    lineage = _read(WEBSITE / "research-lineage.html")
    for token in (
        "58</strong><span>proposition-level statements",
        "45</strong><span>reproducible experiments",
        "33</strong><span>scientific result figures",
        "223</strong><span>claim-level tests",
        f"{frontier}</strong><span>proposition-level results",
        f"P{frontier}</strong><span>current theorem frontier",
        "Research III · consciousness measurement science",
        "V1-V55</strong><span>formal validation stages",
        "200</strong><span>tests in each CI job",
        "22</strong><span>code-generated validation figures",
        "11</strong><span>reproducible validation runners",
        "V36-V40 · finite-sample electromagnetic inference",
        "V41-V45 · multiplicity and selection-safe inference",
        "V46-V50 · cross-site replication inference and stability",
        "v46_v50_electromagnetic_replication_validation.svg",
        "V51-V55 · transportability across sensor systems, hardware, and states",
        "v51_v55_transportability_validation.svg",
        "A recovered subsystem is not automatically a conscious subject",
        "Bridge remains an independently testable open problem",
    ):
        assert token in lineage


def test_research_map_and_plain_language_use_current_state() -> None:
    frontier = _frontier()
    research_map = _read(WEBSITE / "research-map.html")
    plain = _read(WEBSITE / "plain-language.html")
    assert f"P{frontier}" in research_map
    assert f'id="p{frontier}-research-map"' in research_map
    assert "Research II" in plain
    assert f"{frontier} linked results · technical endpoint P{frontier}" in plain
    assert "A note about proposition numbers" in plain
    assert "Research III" in plain


def test_citation_surface_is_professional_and_current() -> None:
    frontier = _frontier()
    label = f"P{frontier}"
    citation = _read(ROOT / "CITATION.md")
    bib = _read(ROOT / "CITATION.bib")
    cff = _read(ROOT / "CITATION.cff")
    readme = _read(ROOT / "README.md")
    marker = f"Current documented theorem frontier: {label}."

    assert "## Preferred scholarly citation" in citation
    assert "CITATION.md" in readme
    assert "CITATION.bib" in citation
    assert "CITATION.cff" in readme
    assert "Version 0.82.0" in citation
    assert f"## Current theorem frontier: {label}" in citation
    assert marker in bib
    assert marker in cff


def test_changelog_tracks_declared_current_frontier() -> None:
    frontier = _frontier()
    changelog = _read(ROOT / "CHANGELOG.md")
    assert changelog.startswith(f"# Unreleased research frontier - P{frontier}\n")
