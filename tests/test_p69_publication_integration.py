from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p69_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_69_dual_optimal_multiplier.md",
        "docs/figures/p69_dual_optimal_multiplier.svg",
        "src/consciousness_bridge/dual_optimal_multiplier.py",
        "tests/test_dual_optimal_multiplier.py",
        "tests/test_p69_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p69_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p69.py").exists()
    assert not (ROOT / ".github/workflows/publish-p69.yml").exists()


def test_p69_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_69_dual_optimal_multiplier.md"
    figure = root / "docs" / "figures" / "p69_dual_optimal_multiplier.svg"
    source = root / "src" / "consciousness_bridge" / "dual_optimal_multiplier.py"
    algorithm_test = root / "tests" / "test_dual_optimal_multiplier.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme

    calibration = root / "docs" / "calibration_optimization_frontier_p61_p70.md"
    calibration_text = calibration.read_text(encoding="utf-8")
    assert proof.name in calibration_text
    assert figure.name in calibration_text
