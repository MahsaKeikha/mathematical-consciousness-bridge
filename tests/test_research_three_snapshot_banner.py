from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "7a2a1a3a60263e48b7a268642eecc6941e84d1b4"


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_is_audit_metadata_not_a_reader_card() -> None:
    page = _read("website/measurement-science.html")

    assert "Verified repository snapshot" not in page
    assert "This page is pinned to the corrected V1-V10 Research III record" not in page
    assert '<p class="eyebrow">Implemented now versus not yet established</p>' not in page


def test_research_three_v15_public_layer_uses_verified_snapshot() -> None:
    refresh = _read("website/research-iii-atlas-refresh.js")
    orientation = _read("website/research-orientation.js")

    assert PIN in refresh
    assert PIN in orientation
    assert "V1-V15 result record" in refresh
    assert "14 / 14 visible" in refresh
    assert "98</strong><span>tests in each CI job" in orientation
    assert "23 scientific visuals" in orientation


def test_research_three_page_keeps_reproducibility_and_scientific_boundary() -> None:
    page = _read("website/measurement-science.html")
    refresh = _read("website/research-iii-atlas-refresh.js")

    assert "Resolution-aware abstention" in page
    assert "Scientific boundary" in page
    assert "formal-validation-v11-v15" in refresh
    assert "run_identification_design_validation.py" in refresh


def test_homepage_orientation_promotes_engineering_validation() -> None:
    script = _read("website/research-orientation.js")

    assert "function enhanceHomepageResearchIII()" in script
    assert "V1-V15 formal validation" in script
    assert "98</strong><span>tests in each CI job" in script
    assert "23 scientific visuals" in script
    assert "3 deterministic runners" in script
    assert "enhanceHomepageResearchIII();" in script


def test_research_three_orientation_preserves_empirical_boundary() -> None:
    script = _read("website/research-orientation.js")

    assert "do not establish empirical calibration for consciousness" in script
    assert "analytic or synthetic validation is not human or clinical validation" in script
