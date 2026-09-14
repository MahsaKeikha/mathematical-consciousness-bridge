from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"
CHANGELOG = ROOT / "CHANGELOG.md"


def test_p75_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_75_target_model_adequacy_overidentification.md",
        DOCS / "p75_equation_provenance.md",
        DOCS / "figures" / "p75_target_model_adequacy_overidentification.svg",
        ROOT / "src" / "consciousness_bridge" / "target_model_adequacy.py",
        ROOT / "tests" / "test_target_model_adequacy.py",
    )
    for path in required:
        assert path.exists(), path
