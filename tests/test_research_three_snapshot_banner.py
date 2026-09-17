from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee"


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_is_now_a_visible_validation_record() -> None:
    page = _read("website/measurement-science.html")

    assert "Verified repository snapshot" in page
    assert "Formal validation V1-V10" in page
    assert "81</strong><span>tests in each CI job" in page
    assert "19</strong><span>scientific visuals: 9 architecture + 10 validation" in page
    assert PIN in page


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
