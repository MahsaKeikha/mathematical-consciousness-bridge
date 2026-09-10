import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _project_version() -> str:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.MULTILINE)
    assert match
    return match.group(1)


def _citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version: ([0-9]+\.[0-9]+\.[0-9]+)$', text, re.MULTILINE)
    assert match
    return match.group(1)


def test_release_version_is_synchronized_across_public_surfaces():
    version = _project_version()
    assert _citation_version() == version
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert f"version-{version}-2563eb" in readme
    assert f"| research-software version | **{version}** |" in readme


def test_public_proposition_count_matches_released_chain():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "**32 proposition-level results" in readme
    assert "| proposition-level results | **32** |" in readme
