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


def test_sitewide_card_affordance_contract_is_explicit() -> None:
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    for selector in (
        ".result",
        ".flow-node",
        ".figure-card",
        ".card",
        ".frontier-summary-card",
        ".evidence-card",
        ".reader-primer-card",
        ".reader-step-card",
        ".source-grid > a",
        ".research-program-card",
        ".lineage-mini-card",
        ".trail-card",
        ".theorem-figure-shell",
    ):
        assert selector in script

    assert "function classifyCardAffordances()" in script
    assert "function neutralizeAmbiguousWholeCard(card)" in script
    assert "uniqueTargets.size > 1" in script
    assert "card-affordance-actionable" in script
    assert "card-affordance-static" in script
    assert "card-affordance-multi" in script
    assert "event.stopImmediatePropagation()" in script
    assert "card-action-hint" in script
    assert "Open →" in script
    assert "interactive-card::after" in script
    assert "content: none !important" in script
    assert "classifyCardAffordances();" in script


def test_p100_overview_cards_have_exact_theorem_destinations() -> None:
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")
    proof = (ROOT / "docs" / "proposition_100_anytime_sequential_eprocess.md").read_text(
        encoding="utf-8"
    )

    expected = (
        (
            "Collect certification data that were not used to choose their own test",
            "#p100b-conditional-p99-round-validity",
            "## P100B. Conditional P99 round validity",
        ),
        (
            "Turn each valid round into evidence that can be multiplied safely",
            "#p100d-product-process-is-a-nonnegative-supermartingale",
            "## P100D. Product process is a nonnegative supermartingale",
        ),
        (
            "Inspect after every round without paying a new error penalty for every look",
            "#p100e-anytime-valid-rejection-by-villes-inequality",
            "## P100E. Anytime-valid rejection by Ville's inequality",
        ),
        (
            "Predictable reserve stake",
            "#p100c-predictable-reserve-stake-factor",
            "## P100C. Predictable reserve-stake factor",
        ),
        (
            "Exact two-round checkpoint",
            "#p100g-exact-95-percent-moderate-evidence-checkpoint",
            "## P100G. Exact 95 percent moderate-evidence checkpoint",
        ),
    )
    for heading, fragment, theorem_heading in expected:
        assert heading in script
        assert fragment in script
        assert theorem_heading in proof


def test_p100_full_technical_figure_control_is_replaced_by_real_link() -> None:
    overview = (WEBSITE / "index.html").read_text(encoding="utf-8")
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    assert '<details class="technical-figure-details">' in overview
    assert "function fixP100TechnicalFigureControl()" in script
    assert "details.replaceWith(link)" in script
    assert "visual-atlas.html#p100-frontier" in script
    assert "Open the full technical P100 theorem figure →" in script
    assert 'id="p100-frontier"' in atlas


def test_about_page_uses_measurement_science_language_for_human_signals() -> None:
    about = (WEBSITE / "about.html").read_text(encoding="utf-8")

    assert (
        "What can observable human signals legitimately tell us about an underlying conscious "
        "or experiential target, and what remains non-identifiable?"
    ) in about
    assert "A physiological signal is not consciousness." in about
    assert "A neural measurement is not experience." in about
    assert "Measurement, latent human state, and the limits of inference" in about
    assert "separately defined experiential or consciousness-related target" in about
    assert "identity, experience, and dignity" not in about
    assert "Measurement, dignity" not in about
