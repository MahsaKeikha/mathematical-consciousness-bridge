import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _project_version() -> str:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', pyproject, re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_release_versions_are_synchronized():
    version = _project_version()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert f"version-{version}-2563eb" in readme
    assert re.search(rf"^version: {re.escape(version)}$", citation, re.MULTILINE)


def test_historical_theorem_artifacts_live_on_authoritative_archive_layers():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    record = (ROOT / "docs/detailed_proposition_record.md").read_text(encoding="utf-8")
    calibration = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")

    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/calibration_optimization_frontier_p61_p70.md" in readme
    for proposition in range(39, 61):
        proofs = list((ROOT / "docs").glob(f"proposition_{proposition}_*.md"))
        figures = list((ROOT / "docs/figures").glob(f"p{proposition}_*.svg"))
        assert len(proofs) == 1
        assert figures
    assert "Complete P1 to P88 chronology" in record
    for proposition in range(61, 71):
        proofs = list((ROOT / "docs").glob(f"proposition_{proposition}_*.md"))
        figures = list((ROOT / "docs/figures").glob(f"p{proposition}_*.svg"))
        assert len(proofs) == 1
        assert figures
        assert proofs[0].name in calibration
        assert figures[0].name in calibration
