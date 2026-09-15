"""Repair the last full-suite contracts during the one-run P94 promotion.

This helper is temporary. It runs after the P94 publication finalizer and before
canonical figure regeneration. Delete it with the other P94 migration helpers
after the exact promoted head is validated.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one {old!r}, found {count}")
    return text.replace(old, new, 1)


def normalize_latex_controls() -> None:
    replacements = (
        ("\x0barepsilon", r"\varepsilon"),
        ("\x0crac", r"\frac"),
        ("\x07lpha", r"\alpha"),
    )
    for path in ("docs/theorem_roadmap.md", "CITATION.md"):
        text = read(path)
        for old, new in replacements:
            text = text.replace(old, new)
        for control in ("\x0c", "\x0b", "\x07"):
            if control in text:
                raise RuntimeError(f"{path}: residual LaTeX control character {control!r}")
        write(path, text)


def repair_website_residue() -> None:
    path = "website/implementation.html"
    text = read(path)
    if "P73-P93" in text:
        text = text.replace("P73-P93", "P73-P94")
    if "Stage 06 · P73-P94" not in text:
        raise RuntimeError(f"{path}: Stage 06 range did not advance to P94")
    text = text.replace("index.html#p93-frontier", "index.html#p94-frontier")
    text = text.replace(">current P92 frontier</a>", ">current P94 frontier</a>")
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = text.replace("index.html#p93-frontier", "index.html#p94-frontier")
    if "index.html#p93-frontier" in text:
        raise RuntimeError(f"{path}: stale P93 homepage frontier link remains")
    write(path, text)


def repair_p92_reader_regression() -> None:
    path = "tests/test_p92_reader_surface_coherence.py"
    text = read(path)
    if "import json\n" not in text:
        text = text.replace("from pathlib import Path\n", "import json\nfrom pathlib import Path\n", 1)
    old = '''def test_p92_is_historical_while_p93_owns_the_homepage() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    assert 'id="p93-frontier"' in home
    assert 'id="p92-frontier"' not in home
    p93 = atlas.index('id="p93-frontier"')
    p92 = atlas.index('id="p92-frontier"')
    assert p93 < p92
    historical = atlas[p92:]
    assert "Previous theorem frontier · P92" in historical
    assert "p92_exact_global_mixed_prevalence_distance.svg" in historical
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in historical
    assert "p92_equation_provenance.md" in historical
'''
    new = '''def test_p92_is_historical_beneath_the_declared_homepage_frontier() -> None:
    manifest = json.loads(_read("figures/manifest.json"))
    current = str(manifest["current_frontier"]).lower()
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    assert f'id="{current}-frontier"' in home
    assert 'id="p92-frontier"' not in home
    current_position = atlas.index(f'id="{current}-frontier"')
    p92 = atlas.index('id="p92-frontier"')
    assert current_position < p92
    historical = atlas[p92:]
    assert "Previous theorem frontier · P92" in historical
    assert "p92_exact_global_mixed_prevalence_distance.svg" in historical
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in historical
    assert "p92_equation_provenance.md" in historical
'''
    text = replace_required(text, old, new, label=path)
    write(path, text)


def repair_reader_experience_regressions() -> None:
    path = "tests/test_reader_experience.py"
    text = read(path)
    if "import json\n" not in text:
        text = text.replace("import ast\n", "import ast\nimport json\n", 1)

    old = '''def test_repository_verifier_tracks_p93_and_all_93_propositions() -> None:
    verifier = _text("scripts/verify_repository.py")
    assert 'CURRENT_FRONTIER = "P93"' in verifier
    assert "covered: set[int] = set()" in verifier
    assert "range(1, 94)" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert '"docs/proposition_92_exact_global_mixed_prevalence_distance.md"' in verifier
'''
    new = '''def test_repository_verifier_tracks_declared_frontier_and_all_propositions() -> None:
    manifest = json.loads(_text("figures/manifest.json"))
    frontier = str(manifest["current_frontier"])
    verifier = _text("scripts/verify_repository.py")
    assert f'CURRENT_FRONTIER = "{frontier}"' in verifier
    assert "covered: set[int] = set()" in verifier
    assert 'frontier_number = int(CURRENT_FRONTIER.removeprefix("P"))' in verifier
    assert "range(1, frontier_number + 1)" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert '"docs/proposition_92_exact_global_mixed_prevalence_distance.md"' in verifier
'''
    text = replace_required(text, old, new, label=path)

    old = '''def test_overview_orients_first_time_reader_before_theorem_frontier() -> None:
    overview = _text("website/index.html")
    assert overview.count('id="project-journey"') == 1
    assert overview.index('id="project-journey"') < overview.index('id="p93-frontier"')
    assert "The whole research program in three stages" in overview
    assert "<span>Research I</span>" in overview
    assert "<span>Research II</span>" in overview
    assert "<span>Research III</span>" in overview
    assert "Research I identifies a physical subsystem candidate" in overview
    assert "None of these stages by itself establishes the final physical-to-experiential bridge." in overview
'''
    new = '''def test_overview_orients_first_time_reader_before_theorem_frontier() -> None:
    manifest = json.loads(_text("figures/manifest.json"))
    frontier_id = f'id="{str(manifest["current_frontier"]).lower()}-frontier"'
    overview = _text("website/index.html")
    assert overview.count('id="project-journey"') == 1
    assert overview.index('id="project-journey"') < overview.index(frontier_id)
    assert "The whole research program in three stages" in overview
    assert "<span>Research I</span>" in overview
    assert "<span>Research II</span>" in overview
    assert "<span>Research III</span>" in overview
    assert "Research I identifies a physical subsystem candidate" in overview
    assert "None of these stages by itself establishes the final physical-to-experiential bridge." in overview
'''
    text = replace_required(text, old, new, label=path)
    write(path, text)


def normalize_research_navigation_eof() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    normalized = text.rstrip("\n") + "\n"
    write(path, normalized)
    if read(path).endswith("\n\n"):
        raise RuntimeError(f"{path}: extra blank line remains at EOF")


def verify() -> None:
    roadmap = read("docs/theorem_roadmap.md")
    if any(control in roadmap for control in ("\x0c", "\x0b", "\x07")):
        raise RuntimeError("docs/theorem_roadmap.md still contains control characters")
    implementation = read("website/implementation.html")
    if "Stage 06 · P73-P94" not in implementation:
        raise RuntimeError("implementation Stage 06 is not promoted through P94")
    for path in ("website/implementation.html", "website/research-map.html"):
        if "index.html#p93-frontier" in read(path):
            raise RuntimeError(f"{path}: stale P93 homepage link remains")
    if "test_p92_is_historical_while_p93_owns_the_homepage" in read(
        "tests/test_p92_reader_surface_coherence.py"
    ):
        raise RuntimeError("P92 reader regression still hard-codes P93 as current")
    reader_test = read("tests/test_reader_experience.py")
    if 'overview.index(\'id="p93-frontier"\')' in reader_test:
        raise RuntimeError("reader experience still hard-codes the P93 homepage anchor")
    if 'CURRENT_FRONTIER = "P93"' in reader_test:
        raise RuntimeError("reader experience still hard-codes P93 verifier state")
    if read("docs/research_navigation.md").endswith("\n\n"):
        raise RuntimeError("research navigation has an extra blank line at EOF")


def main() -> None:
    normalize_latex_controls()
    repair_website_residue()
    repair_p92_reader_regression()
    repair_reader_experience_regressions()
    normalize_research_navigation_eof()
    verify()
    print("[P94] full-suite migration residue repaired")


if __name__ == "__main__":
    main()
