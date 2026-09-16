from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_start_here_points_to_p100_frontier() -> None:
    text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    assert "The public theorem frontier is **P100**." in text
    assert "You do not need to read 100 propositions" in text
    assert "[P100](docs/proposition_100_anytime_sequential_eprocess.md)" in text
    assert "The public theorem frontier is **P99**." not in text


def test_reproducibility_route_names_p100_as_current() -> None:
    text = (ROOT / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    assert "Run only the current P100 theorem checks" in text
    assert "focused P100 commands below" in text
    assert "Run only the current P99 theorem checks" not in text


def test_citation_guide_has_one_current_p100_frontier() -> None:
    text = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    assert "current documented frontier, P100" in text
    assert "Current documented theorem frontier: P100" in text
    assert "theorem frontier **P100**" in text
    assert "## Current theorem frontier: P100" in text
    assert "## Immediate predecessor theorem frontier: P99" in text
    assert "At the preceding stage, the documented theorem frontier was **P99**." in text
    assert "## Earlier theorem frontier: P98" in text
    assert "At that stage, the documented theorem frontier was **P98**." in text
    assert "## Earlier theorem frontier: P97" in text
    assert "At that stage, the documented theorem frontier was **P97**." in text
    assert "current documented frontier, P99" not in text
    assert "theorem frontier **P99**" not in text
