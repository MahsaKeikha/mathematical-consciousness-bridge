"""Repair exact generated P94 migration contracts during the one-run promotion.

Temporary helper for PR #156. The promotion workflow invokes its phases around
the generator and finalizer. Delete it after the promoted P94 publication head
is validated and before merge.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_PATH = ROOT / "tests" / "test_p94_reader_surface_coherence.py"
BIB_PATH = ROOT / "CITATION.bib"
CITATION_PATH = ROOT / "CITATION.md"
CFF_PATH = ROOT / "CITATION.cff"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def verify_pre_promotion_citations() -> None:
    marker = "Current documented theorem frontier: P93."
    markdown = CITATION_PATH.read_text(encoding="utf-8")
    bib = BIB_PATH.read_text(encoding="utf-8")
    cff = CFF_PATH.read_text(encoding="utf-8")

    if marker not in markdown:
        raise RuntimeError("CITATION.md is not synchronized to the P93 source frontier")
    if marker not in bib:
        raise RuntimeError("CITATION.bib is not synchronized to the P93 source frontier")
    if marker not in cff:
        raise RuntimeError("CITATION.cff is not synchronized to the P93 source frontier")

    print("[P94] pre-promotion citation metadata agree on P93")


def normalize_bib_for_legacy_finalizer() -> None:
    text = BIB_PATH.read_text(encoding="utf-8")
    p89 = "Current documented theorem frontier: P89."
    p93 = "Current documented theorem frontier: P93."
    if p93 in text:
        text = text.replace(p93, p89, 1)
        BIB_PATH.write_text(text, encoding="utf-8")
        print("[P94] normalized BibTeX input for legacy finalizer compatibility")
        return
    if p89 in text:
        return
    raise RuntimeError("CITATION.bib is neither at the legacy P89 nor synchronized P93 marker")


def repair_generated_test_escape() -> None:
    text = TEST_PATH.read_text(encoding="utf-8")
    old = '    assert "-\\frac{2145}{281474976710656}" in proof\n'
    new = '    assert r"-\\frac{2145}{281474976710656}" in proof\n'
    if old in text:
        if text.count(old) != 1:
            raise RuntimeError("generated P94 determinant-product assertion is duplicated")
        TEST_PATH.write_text(text.replace(old, new, 1), encoding="utf-8")
        print("[P94] generated reader-contract escape repaired")
        return
    if text.count(new) == 1:
        return
    raise RuntimeError("generated P94 determinant-product assertion is missing")


def replace_function(path: str, old_name: str, replacement: str) -> None:
    text = read(path)
    pattern = re.compile(
        rf"def {re.escape(old_name)}\(\) -> None:\n.*?(?=\n\ndef |\Z)",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise RuntimeError(f"{path}: missing function {old_name}")
    write(path, text[: match.start()] + replacement.rstrip() + text[match.end() :])


def repair_generated_latex_controls() -> None:
    replacements = (
        ("\x0barepsilon", r"\varepsilon"),
        ("\x0crac", r"\frac"),
        ("\x07lpha", r"\alpha"),
    )
    for path in ("docs/theorem_roadmap.md", "CITATION.md"):
        text = read(path)
        for old, new in replacements:
            text = text.replace(old, new)
        if any(control in text for control in ("\x07", "\x0b", "\x0c")):
            raise RuntimeError(f"{path}: generated LaTeX control characters remain")
        write(path, text)


def repair_stage_six_and_frontier_links() -> None:
    path = "website/implementation.html"
    text = read(path)
    text = text.replace("P73-P93", "P73-P94")
    text = text.replace("P1-P92 proposition record", "P1-P94 proposition record")
    text = text.replace("index.html#p93-frontier", "index.html#p94-frontier")
    text = text.replace("current P92 frontier", "current P94 frontier")
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = text.replace("index.html#p93-frontier", "index.html#p94-frontier")
    text = text.replace("current P93 frontier", "current P94 frontier")
    write(path, text)


def repair_historical_reader_tests() -> None:
    replace_function(
        "tests/test_p92_reader_surface_coherence.py",
        "test_p92_is_historical_while_p93_owns_the_homepage",
        '''def test_p92_is_historical_while_current_frontier_owns_the_homepage() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    verifier = _read("scripts/verify_repository.py")
    frontier = next(
        line.split('"')[1]
        for line in verifier.splitlines()
        if line.startswith("CURRENT_FRONTIER = ")
    )
    current_marker = f'id="{frontier.lower()}-frontier"'
    assert current_marker in home
    assert 'id="p92-frontier"' not in home
    current = atlas.index(current_marker)
    p92 = atlas.index('id="p92-frontier"')
    assert current < p92
    historical = atlas[p92:]
    assert "Previous theorem frontier · P92" in historical
    assert "p92_exact_global_mixed_prevalence_distance.svg" in historical
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in historical
    assert "p92_equation_provenance.md" in historical''',
    )

    replace_function(
        "tests/test_reader_experience.py",
        "test_repository_verifier_tracks_p93_and_all_93_propositions",
        '''def test_repository_verifier_tracks_declared_frontier_and_all_propositions() -> None:
    verifier = _text("scripts/verify_repository.py")
    frontier = next(
        line.split('"')[1]
        for line in verifier.splitlines()
        if line.startswith("CURRENT_FRONTIER = ")
    )
    frontier_number = int(frontier.removeprefix("P"))
    latest = max(
        int(path.stem.split("_")[1])
        for path in (ROOT / "docs").glob("proposition_*.md")
    )
    assert frontier_number == latest
    assert "covered: set[int] = set()" in verifier
    assert "range(1, frontier_number + 1)" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert '"docs/proposition_92_exact_global_mixed_prevalence_distance.md"' in verifier''',
    )

    replace_function(
        "tests/test_reader_experience.py",
        "test_overview_orients_first_time_reader_before_theorem_frontier",
        '''def test_overview_orients_first_time_reader_before_theorem_frontier() -> None:
    overview = _text("website/index.html")
    verifier = _text("scripts/verify_repository.py")
    frontier = next(
        line.split('"')[1]
        for line in verifier.splitlines()
        if line.startswith("CURRENT_FRONTIER = ")
    )
    current_marker = f'id="{frontier.lower()}-frontier"'
    assert overview.count('id="project-journey"') == 1
    assert overview.index('id="project-journey"') < overview.index(current_marker)
    assert "The whole research program in three stages" in overview
    assert "<span>Research I</span>" in overview
    assert "<span>Research II</span>" in overview
    assert "<span>Research III</span>" in overview
    assert "Research I identifies a physical subsystem candidate" in overview
    assert "None of these stages by itself establishes the final physical-to-experiential bridge." in overview''',
    )


def verify_final_repairs() -> None:
    for path in ("docs/theorem_roadmap.md", "CITATION.md"):
        text = read(path)
        if any(control in text for control in ("\x07", "\x0b", "\x0c")):
            raise RuntimeError(f"{path}: forbidden generated control character remains")

    implementation = read("website/implementation.html")
    if "Stage 06 · P73-P94" not in implementation:
        raise RuntimeError("website/implementation.html: Stage 06 is not promoted to P94")

    for path in ("website/implementation.html", "website/research-map.html"):
        if "index.html#p93-frontier" in read(path):
            raise RuntimeError(f"{path}: stale P93 homepage fragment remains")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("pre", "post", "final"))
    args = parser.parse_args()

    if args.phase == "pre":
        verify_pre_promotion_citations()
        normalize_bib_for_legacy_finalizer()
        return

    if args.phase == "post":
        repair_generated_test_escape()
        return

    repair_generated_latex_controls()
    repair_stage_six_and_frontier_links()
    repair_historical_reader_tests()
    verify_final_repairs()
    print("[P94] residual publication contracts repaired")


if __name__ == "__main__":
    main()
