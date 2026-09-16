from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def test_sources_resource_and_audit_cards_have_destinations() -> None:
    source = (WEBSITE / "sources.html").read_text(encoding="utf-8")
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    headings = (
        "Proof documents",
        "Implementations",
        "Regression tests",
        "Figures",
        "Release metadata",
        "Version history",
        "Read assumptions",
        "Check dependencies",
        "Inspect proof",
        "Run implementation",
        "Run tests",
        "Check scientific boundary",
    )
    for heading in headings:
        assert f"<h3>{heading}</h3>" in source
        assert heading in script

    assert "function wireSourceCards()" in script
    assert "resource-card-overlay" in script
    assert "research-map.html#proposition-atlas" in script
    assert "docs/equation_and_citation_map.md" in script
    assert "docs/claim_evidence_standard.md" in script


def test_sources_page_is_runtime_synchronized_to_p100_frontier() -> None:
    source = (WEBSITE / "sources.html").read_text(encoding="utf-8")
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    assert 'id="p99-source"' in source
    assert "function syncSourcesFrontier()" in script
    assert "Current theorem source · P100" in script
    assert "Immediate predecessor theorem source · P99" in script
    assert "proposition_100_anytime_sequential_eprocess.md" in script
    assert "p100_equation_provenance.md" in script
    assert "anytime_sequential_eprocess.py" in script
    assert "test_anytime_sequential_eprocess.py" in script
    assert "p100_anytime_sequential_eprocess.svg" in script
    assert "P100 is a sequential inference theorem" in script
    assert "syncSourcesFrontier();" in script


def test_research_map_milestones_link_to_real_canonical_proofs() -> None:
    guide = (WEBSITE / "research-map-guide.js").read_text(encoding="utf-8")

    milestones = (
        (1, "representation_invariance"),
        (11, "intervention_resolved_causal_structure"),
        (19, "fundamental_physical_sufficiency"),
        (38, "quantum_operational_sufficiency"),
        (71, "target_provenance_noncircularity"),
        (75, "target_model_adequacy_overidentification"),
        (92, "exact_global_mixed_prevalence_distance"),
        (100, "anytime_sequential_eprocess"),
    )
    for number, slug in milestones:
        assert f"number: {number}," in guide
        assert f"slug: '{slug}'" in guide
        assert (ROOT / "docs" / f"proposition_{number}_{slug}.md").is_file()

    assert "Eight orientation checkpoints through the P1-P100 program" in guide
    assert "not a claim that the full theorem graph is a single linear dependency chain" in guide
    assert "P100 is the current Research II theorem frontier" in guide


def test_footer_loads_research_map_guide_only_on_research_map() -> None:
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")
    assert "function loadResearchMapGuide()" in script
    assert "currentFile() !== 'research-map.html'" in script
    assert "script.src = 'research-map-guide.js'" in script
    assert "loadResearchMapGuide();" in script
