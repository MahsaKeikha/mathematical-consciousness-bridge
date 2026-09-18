from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "771bca04b92cf775eb4f75fb3b576be6f43e0940"


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_is_audit_metadata_not_a_reader_card() -> None:
    page = _read("website/measurement-science.html")

    assert "Verified repository snapshot" not in page
    assert "This page is pinned to the corrected V1-V10 Research III record" not in page
    assert '<p class="eyebrow">Implemented now versus not yet established</p>' not in page


def test_research_three_v25_public_layer_uses_verified_snapshot() -> None:
    refresh = _read("website/research-iii-atlas-refresh.js")
    orientation = _read("website/research-orientation.js")

    assert PIN in refresh
    assert PIN in orientation
    assert "V1-V25 result record" in refresh
    assert "16 / 16 visible" in refresh
    assert "121</strong><span>tests in each CI job" in orientation
    assert "25 scientific visuals" in orientation


def test_research_three_page_has_visual_v1_v25_reproducibility_map() -> None:
    page = _read("website/measurement-science.html")
    styles = _read("website/styles.css")
    refresh = _read("website/research-iii-atlas-refresh.js")

    assert "Five validation programs move from identifiability to robustness, study design, electromagnetic measurement, and source identifiability" in page
    for stage in ("V1-V5", "V6-V10", "V11-V15", "V16-V20", "V21-V25"):
        assert stage in page
    for label in ("Derivation", "Code", "Results", "Figures"):
        assert page.count(f">{label}<") >= 3
    for label in ("Research program", "Figure"):
        assert f">{label}<" in page
    for node in range(1, 26):
        assert f"<span>V{node}</span>" in page
    for seed in ("20260917", "20260918", "20260919"):
        assert seed in page
    for runner in (
        "run_validation_program.py",
        "run_robustness_validation.py",
        "run_identification_design_validation.py",
        "run_electromagnetic_validation.py",
        "run_electromagnetic_inverse_validation.py",
    ):
        assert runner in page

    assert 'class="validation-flow"' in page
    assert page.count('class="validation-node"') == 25
    assert ".validation-flow::before" in styles
    assert "grid-template-columns: repeat(5, minmax(0, 1fr))" in styles
    assert "Two deterministic runners regenerate" not in page
    assert "data-v11-v15-runner" not in refresh
    assert "What V1-V25 establishes, and what it does not" in page
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


def test_homepage_orientation_promotes_engineering_validation() -> None:
    script = _read("website/research-orientation.js")

    assert "function enhanceHomepageResearchIII()" in script
    assert "V1-V25 formal validation" in script
    assert "121</strong><span>tests in each CI job" in script
    assert "25 scientific visuals" in script
    assert "5 reproducible validation runners" in script
    assert "enhanceHomepageResearchIII();" in script


def test_research_three_orientation_preserves_empirical_boundary() -> None:
    script = _read("website/research-orientation.js")

    assert "source reconstructions remain model- and prior-dependent inferences" in script
    assert "No current result establishes a universal electromagnetic consciousness signature" in script
    assert "analytic or synthetic validation is not human or clinical validation" in script
