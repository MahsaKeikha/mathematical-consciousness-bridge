from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_p64_publication_surface():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "P64 fast certified integer approximation" in readme
    assert "p64_fast_heterogeneous_integer_approximation.svg" in readme
    assert "fast_heterogeneous_integer_approximation.py" in readme
    assert "[P64](proposition_64_fast_heterogeneous_integer_approximation.md)" in (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    assert "| P64 | [Fast certified heterogeneous integer approximation]" in (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    assert "# 53. P64 fast certified heterogeneous integer approximation" in (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
