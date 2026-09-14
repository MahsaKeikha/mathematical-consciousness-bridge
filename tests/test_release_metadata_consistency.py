import re
from pathlib import Path


def _project_version() -> str:
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', pyproject, re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_release_versions_are_synchronized():
    version = _project_version()
    readme = Path("README.md").read_text(encoding="utf-8")
    citation = Path("CITATION.cff").read_text(encoding="utf-8")
    assert f"version-{version}-2563eb" in readme
    assert re.search(rf"^version: {re.escape(version)}$", citation, re.MULTILINE)
