import re
from pathlib import Path


def test_release_versions_are_synchronized():
    readme = Path("README.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    citation = Path("CITATION.cff").read_text(encoding="utf-8")
    assert "version-0.42.0-2563eb" in readme
    assert re.search(r'^version = "0\.42\.0"$', pyproject, re.MULTILINE)
    assert re.search(r'^version: 0\.42\.0$', citation, re.MULTILINE)


def test_p39_publication_paths_are_visible():
    readme = Path("README.md").read_text(encoding="utf-8")
    for token in (
        "Proposition 39",
        "p39_finite_data_quantum_nonfactorization.svg",
        "finite_data_quantum_nonfactorization.py",
        "test_finite_data_quantum_nonfactorization.py",
        "Proposition 40",
        "p40_continuous_quantum_region_regularity.svg",
        "continuous_quantum_region_regularity.py",
        "test_continuous_quantum_region_regularity.py",
        "Proposition 41",
        "p41_trace_ball_quantum_envelope.svg",
        "trace_ball_quantum_envelope.py",
        "test_trace_ball_quantum_envelope.py",
        "Proposition 42",
        "p42_quantum_regular_bridge_sample_complexity.svg",
        "quantum_regular_bridge_sample_complexity.py",
        "test_quantum_regular_bridge_sample_complexity.py",
    ):
        assert token in readme
