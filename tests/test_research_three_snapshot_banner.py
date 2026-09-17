from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "64b2bc47461fe110b135080f8dc70883552d6fd9"


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_is_audit_metadata_not_a_reader_card() -> None:
    page = _read("website/measurement-science.html")

    assert "Verified repository snapshot" not in page
    assert "This page is pinned to the corrected V1-V10 Research III record" not in page
    assert f"<!-- research-three-snapshot: {PIN} -->" in page
    assert f"/commit/{PIN}" in page
    assert "Formal validation V1-V10" in page
    assert "81</strong><span>tests in each CI job" in page
    assert "19</strong><span>scientific visuals: 9 architecture + 10 validation" in page


def test_research_three_page_no_longer_uses_governance_as_a_major_section() -> None:
    page = _read("website/measurement-science.html")

    assert '<p class="eyebrow">Implemented now versus not yet established</p>' not in page
    assert "Resolution-aware abstention" in page
    assert "Audit the Research III source and reproducibility record" in page


def test_homepage_orientation_promotes_engineering_validation() -> None:
    script = _read("website/research-orientation.js")

    assert "function enhanceHomepageResearchIII()" in script
    assert "Measurement engineering and formal validation" in script
    assert "V1-V10 formal validation" in script
    assert "81</strong><span>tests in each CI job" in script
    assert "10 result figures" in script
    assert "machine-readable outputs" in script
    assert "enhanceHomepageResearchIII();" in script


def test_homepage_engineering_summary_preserves_scientific_boundary() -> None:
    script = _read("website/research-orientation.js")

    assert "does not yet provide human empirical calibration" in script
    assert "analytic and synthetic validation" in script
    assert "does not turn successful analytic and synthetic validation" in script
