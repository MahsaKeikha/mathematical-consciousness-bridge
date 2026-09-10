import re
from pathlib import Path


def test_release_versions_are_synchronized():
    readme = Path("README.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    citation = Path("CITATION.cff").read_text(encoding="utf-8")
    assert "version-0.39.0-2563eb" in readme
    assert re.search(r'^version = "0\.39\.0"$', pyproject, re.MULTILINE)
    assert re.search(r'^version: 0\.39\.0$', citation, re.MULTILINE)


def test_p39_publication_paths_are_visible():
    readme = Path("README.md").read_text(encoding="utf-8")
    for token in (
        "Proposition 39",
        "p39_finite_data_quantum_nonfactorization.svg",
        "finite_data_quantum_nonfactorization.py",
        "test_finite_data_quantum_nonfactorization.py",
    ):
        assert token in readme
