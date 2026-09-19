from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "8de006a11d09d290fa3a45d144f8b024012fac3d"


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_is_audit_metadata_not_a_reader_card() -> None:
    page = _read("website/measurement-science.html")

    assert "Verified repository snapshot" not in page
    assert "This page is pinned to the corrected V1-V10 Research III record" not in page
    assert '<p class="eyebrow">Implemented now versus not yet established</p>' not in page


def test_research_three_v50_public_layer_uses_verified_snapshot() -> None:
    refresh = _read("website/research-iii-atlas-refresh.js")
    orientation = _read("website/research-orientation.js")

    assert PIN in refresh
    assert PIN in orientation
    assert "V1-V55 result record" in refresh
    assert "22 / 22 visible" in refresh
    assert "196</strong><span>tests in each CI job" in orientation
    assert "31 scientific visuals" in orientation


def test_research_three_page_has_visual_v1_v55_reproducibility_map() -> None:
    page = _read("website/measurement-science.html")
    styles = _read("website/styles.css")
    refresh = _read("website/research-iii-atlas-refresh.js")

    assert "Eleven validation programs move from identifiability to robustness, study design, electromagnetic measurement, source identifiability, resolution and information limits, design and spatial specificity, finite-sample inference, selection-safe inference, cross-site replication inference, and transportability" in page
    for stage in ("V1-V5", "V6-V10", "V11-V15", "V16-V20", "V21-V25", "V26-V30", "V31-V35", "V36-V40", "V41-V45", "V46-V50", "V51-V55"):
        assert stage in page
    for label in ("Derivation", "Code", "Results", "Figures"):
        assert page.count(f">{label}<") >= 3
    for label in ("Research program", "Figure"):
        assert f">{label}<" in page
    for node in range(1, 56):
        assert f"<span>V{node}</span>" in page
    for seed in ("20260917", "20260918", "20260919"):
        assert seed in page
    for runner in (
        "run_validation_program.py",
        "run_robustness_validation.py",
        "run_identification_design_validation.py",
        "run_electromagnetic_validation.py",
        "run_electromagnetic_inverse_validation.py",
        "run_electromagnetic_resolution_validation.py",
        "run_electromagnetic_design_validation.py",
        "run_electromagnetic_finite_sample_validation.py",
        "run_electromagnetic_selection_validation.py",
        "run_electromagnetic_replication_validation.py",
        "run_transportability_validation.py",
    ):
        assert runner in page

    assert 'class="validation-flow"' in page
    assert page.count('class="validation-node"') == 55
    assert ".validation-flow::before" in styles
    assert "grid-template-columns: repeat(5, minmax(0, 1fr))" in styles
    assert "Two deterministic runners regenerate" not in page
    assert "data-v11-v15-runner" not in refresh
    assert "What V1-V55 establishes, and what it does not" in page
    assert "v16_v20_electromagnetic_validation.svg" in page
    assert "electromagnetic_validation_summary.json" in page
    assert "electromagnetic-field-program.md" in page
    assert "Claim ceiling today:" in page
    assert "universal electromagnetic consciousness signature" in page
    assert "Scientific boundary" in page
    assert "Electromagnetic measurement arm" in page
    assert "v16_v20_electromagnetic_validation.svg" in page
    assert "electromagnetic_validation_summary.json" in page
    assert "v21_v25_electromagnetic_inverse_validation.svg" in page
    assert "electromagnetic_inverse_validation_summary.json" in page
    assert "electromagnetic-source-identifiability.md" in page
    assert "v21-v25-electromagnetic-source-identifiability" in page
    assert "v26_v30_electromagnetic_resolution_validation.svg" in page
    assert "electromagnetic_resolution_validation_summary.json" in page
    assert "electromagnetic-resolution-program.md" in page
    assert "v26-v30-electromagnetic-resolution-information" in page
    assert "v31_v35_electromagnetic_design_validation.svg" in page
    assert "electromagnetic_design_validation_summary.json" in page
    assert "electromagnetic-design-spatial-specificity.md" in page
    assert "v31-v35-electromagnetic-design-spatial-specificity" in page
    assert "v36_v40_electromagnetic_finite_sample_validation.svg" in page
    assert "electromagnetic_finite_sample_validation_summary.json" in page
    assert "electromagnetic-finite-sample-inference.md" in page
    assert "v36-v40-electromagnetic-finite-sample-inference" in page
    assert "v41_v45_electromagnetic_selection_validation.svg" in page
    assert "electromagnetic_selection_validation_summary.json" in page
    assert "electromagnetic-selection-safe-inference.md" in page
    assert "v41-v45-electromagnetic-selection-safe-inference" in page
    assert "v46_v50_electromagnetic_replication_validation.svg" in page
    assert "v51_v55_transportability_validation.svg" in page
    assert "transportability_validation_summary.json" in page
    assert "transportability-program.md" in page
    assert "electromagnetic_replication_validation_summary.json" in page
    assert "electromagnetic-replication-inference.md" in page
    assert "v46-v50-electromagnetic-replication-inference" in page


def test_homepage_orientation_promotes_engineering_validation() -> None:
    script = _read("website/research-orientation.js")

    assert "function enhanceHomepageResearchIII()" in script
    assert "V1-V55 formal validation" in script
    assert "196</strong><span>tests in each CI job" in script
    assert "31 scientific visuals" in script
    assert "11 reproducible validation runners" in script
    assert "enhanceHomepageResearchIII();" in script


def test_research_three_orientation_preserves_empirical_boundary() -> None:
    script = _read("website/research-orientation.js")

    assert "source reconstructions remain model- and prior-dependent inferences" in script
    assert "No current result establishes a universal electromagnetic consciousness signature" in script
    assert "analytic or synthetic validation is not human or clinical validation" in script


def test_research_lineage_exposes_current_research_three_v50_record() -> None:
    lineage = _read("website/research-lineage.html")

    assert PIN in lineage
    assert "<strong>V1-V55</strong><span>formal validation stages</span>" in lineage
    assert "<strong>22</strong><span>code-generated validation figures</span>" in lineage
    assert "<strong>196</strong><span>tests in each CI job</span>" in lineage
    assert "<strong>11</strong><span>reproducible validation runners</span>" in lineage
    assert "v41_v45_electromagnetic_selection_validation.svg" in lineage
    assert "V41-V45 selection-safe inference" in lineage
    assert "electromagnetic-selection-safe-inference.md" in lineage
    assert "v46_v50_electromagnetic_replication_validation.svg" in lineage
    assert "V46-V50 replication inference" in lineage
    assert "electromagnetic-replication-inference.md" in lineage
    assert "statistically valid source inference is still not direct evidence" in lineage


def test_research_three_page_uses_editorial_full_width_result_stages() -> None:
    page = _read("website/measurement-science.html")
    styles = _read("website/styles.css")

    assert '<body class="research-iii-page">' in page
    assert "Research III editorial research experience" in styles
    assert 'class="research-iii-stage-nav"' in page
    assert "Follow the result journey" in page
    assert "Open the V1-V55 validation record" in page
    assert 'section[id^="v31-"]' in styles
    assert 'section[id^="v51-"]' in styles
    assert "max-width: none !important" in styles
    assert "height: auto !important" in styles
    assert "max-height: none !important" in styles
    assert "grid-template-columns: minmax(0, 1.04fr) minmax(430px, 0.96fr)" not in styles
    assert "order: 2;" in styles
    assert "order: 4;" in styles
    assert "grid-template-columns: repeat(4, minmax(0, 1fr)) !important" in styles
    assert "linear-gradient(135deg, #111827 0%, #17233a 48%, #1d2e5c 100%)" in styles


def test_research_three_runtime_renderer_cannot_restore_narrow_figure_cards() -> None:
    refresh = _read("website/research-iii-atlas-refresh.js")

    assert "body.research-iii-page .r3-stage-extension>.measurement-figure-grid" in refresh
    assert "display:block!important" in refresh
    assert "grid-template-columns:none!important" in refresh
    assert "body.research-iii-page .r3-stage-extension .measurement-figure-grid>.figure-card" in refresh
    assert "max-width:none!important" in refresh
    assert "max-height:none!important" in refresh
    assert "object-fit:initial!important" in refresh
    assert "order:2!important" in refresh
    assert "order:4!important" in refresh
