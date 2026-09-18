from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_visual_atlas_has_all_three_programs_with_distinct_status() -> None:
    atlas = _read("website/visual-atlas.html")

    for section_id in (
        "research-i-visual-program",
        "research-ii-visual-program",
        "research-iii-visual-program",
        "research-ii-frontier-archive",
    ):
        assert f'id="{section_id}"' in atlas

    assert "58" in atlas and "45" in atlas and "33" in atlas and "223" in atlas
    assert "100" in atlas and "158" in atlas and "P100" in atlas
    assert "V1-V25" in atlas and "16" in atlas and "121" in atlas and "M0-M7" in atlas
    assert "V21-V25 electromagnetic source-identifiability layers" in atlas
    assert "not an empirically or clinically validated consciousness instrument" in atlas
    assert "physical world-tube" in atlas
    assert "does not by itself identify that subsystem as a conscious subject" in atlas


def test_visual_atlas_uses_canonical_figures_from_all_three_programs() -> None:
    atlas = _read("website/visual-atlas.html")

    for figure in (
        "physics_pipeline.svg",
        "worldtube_baseline.png",
        "observer_bridge_dimension_audit.svg",
        "theorem_roadmap.svg",
        "p100_anytime_sequential_eprocess.svg",
        "equation_evidence_map.svg",
        "measurement_architecture.svg",
        "structural_measurement_pipeline.svg",
        "claim_ladder.svg",
    ):
        assert figure in atlas

    assert atlas.count('class="program-visual-card"') == 9
    assert atlas.index('id="research-i-visual-program"') < atlas.index('id="research-ii-visual-program"')
    assert atlas.index('id="research-ii-visual-program"') < atlas.index('id="research-iii-visual-program"')
    assert atlas.index('id="research-iii-visual-program"') < atlas.index('id="research-ii-frontier-archive"')
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')


def test_sources_has_three_program_audit_sections_before_research_two_sequence() -> None:
    sources = _read("website/sources.html")

    for section_id in (
        "research-i-source-program",
        "research-ii-source-program",
        "research-iii-source-program",
        "complete-source-sequence",
    ):
        assert f'id="{section_id}"' in sources

    assert sources.index('id="research-i-source-program"') < sources.index('id="research-ii-source-program"')
    assert sources.index('id="research-ii-source-program"') < sources.index('id="research-iii-source-program"')
    assert sources.index('id="research-iii-source-program"') < sources.index('id="complete-source-sequence"')
    assert "Research II · Complete theorem source sequence" in sources
    assert "full Research II proposition record" in sources
    assert 'data-proposition="P1"' in sources
    assert 'data-proposition="P100"' in sources


def test_sources_links_each_program_to_its_real_audit_record() -> None:
    sources = _read("website/sources.html")

    for token in (
        "spatiotemporal-observer-math/blob/main/docs/research_index.md",
        "spatiotemporal-observer-math/blob/main/docs/assumption_ledger.md",
        "spatiotemporal-observer-math/blob/main/docs/proposition_58_observer_bridge.md",
        "mathematical-consciousness-bridge/blob/main/docs/theorem_roadmap.md",
        "mathematical-consciousness-bridge/blob/main/figures/manifest.json",
        "mathematical-consciousness-bridge/tree/main/tests",
        "consciousness-measurement-science/blob/main/docs/epistemic-boundaries.md",
        "consciousness-measurement-science/blob/main/docs/measurement-framework.md",
        "consciousness-measurement-science/blob/main/docs/statistical-validation.md",
        "consciousness-measurement-science/blob/main/docs/reproducibility.md",
        "consciousness-measurement-science/blob/main/docs/electromagnetic-field-program.md",
        "consciousness-measurement-science/blob/main/docs/electromagnetic-source-identifiability.md",
        "consciousness-measurement-science/blob/main/docs/electromagnetic-source-identifiability.md",
        "consciousness-measurement-science/tree/main/schemas",
    ):
        assert token in sources

    assert sources.count('class="program-source-card"') == 24
    assert "analytic and synthetic validation, specification, and software scaffolding are not empirical consciousness evidence" in sources
    assert "external validation" in sources
    assert "clinical validation" in sources
    assert "V16-V20 electromagnetic field program" in sources
    assert "docs/electromagnetic-field-program.md" in sources
    assert "V21-V25 electromagnetic source-identifiability program" in sources
    assert "docs/electromagnetic-source-identifiability.md" in sources
    assert "V21-V25 electromagnetic source-identifiability program" in sources
    assert "docs/electromagnetic-source-identifiability.md" in sources


def test_sitewide_orientation_describes_atlas_and_sources_as_three_program_surfaces() -> None:
    orientation = _read("website/research-orientation.js")

    assert "Three-program visual evidence record" in orientation
    assert "Research I exposes its scientific-result figures" in orientation
    assert "Research II renders its canonical theorem and architecture record" in orientation
    assert "Research III exposes 9 foundational architecture visuals plus 16 code-generated V1-V25 validation-result figures" in orientation
    assert "Three-program provenance and reproducibility" in orientation
    assert "Research I physical-system provenance" in orientation
    assert "Research II P1-P100 theorem provenance" in orientation
    assert "Research III architecture from its V1-V25 executable validation record" in orientation


def test_three_program_cards_are_native_links_and_static_metrics_do_not_mimic_links() -> None:
    atlas = _read("website/visual-atlas.html")
    sources = _read("website/sources.html")
    css = _read("website/styles.css")

    assert atlas.count('<a class="program-index-card"') == 3
    assert sources.count('<a class="program-index-card"') == 3
    assert atlas.count('<a class="program-visual-card"') == 9
    assert sources.count('<a class="program-source-card"') == 24
    assert ".program-record-metric" in css
    assert ".program-visual-card::after" in css
    assert ".program-source-card::after" in css
    assert "Open record" in css


def test_three_program_reader_surfaces_respect_dash_policy() -> None:
    for path in (
        "website/visual-atlas.html",
        "website/sources.html",
        "website/research-orientation.js",
        "website/styles.css",
    ):
        text = _read(path)
        assert "\u2013" not in text
        assert "\u2014" not in text
