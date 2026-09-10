from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_50_bounded_starvation_asynchronous_sampling.md"
FIGURE = ROOT / "docs" / "figures" / "p50_bounded_starvation_asynchronous_sampling.svg"


def test_p50_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 50A",
        "Proposition 50B",
        "Proposition 50C",
        "Bounded-starvation condition",
        "Dynamic pruning is compatible",
        "Scientific interpretation boundary",
    ):
        assert phrase in text


def test_p50_visual_and_proof_to_code_path_are_public():
    assert FIGURE.exists()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "p50_bounded_starvation_asynchronous_sampling.svg",
        "bounded_starvation_sampling.py",
        "test_bounded_starvation_sampling.py",
        "P50 - bounded-starvation asynchronous sampling",
    ):
        assert token in readme
