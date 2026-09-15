"""Repair exact generated P94 migration contracts before finalization.

Temporary helper for PR #156. Delete it after the promoted P94 publication head
is validated and before merge.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_PATH = ROOT / "tests" / "test_p94_reader_surface_coherence.py"
BIB_PATH = ROOT / "CITATION.bib"
CITATION_PATH = ROOT / "CITATION.md"
CFF_PATH = ROOT / "CITATION.cff"


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


def repair_intermediate_bib_frontier() -> None:
    text = BIB_PATH.read_text(encoding="utf-8")
    p89 = "Current documented theorem frontier: P89."
    p93 = "Current documented theorem frontier: P93."
    if p93 in text:
        text = text.replace(p93, p89, 1)
        BIB_PATH.write_text(text, encoding="utf-8")
        print("[P94] normalized intermediate BibTeX frontier for legacy finalizer compatibility")
        return
    if p89 in text:
        return
    raise RuntimeError("CITATION.bib is neither at the legacy P89 nor intermediate P93 marker")


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


def main() -> None:
    verify_pre_promotion_citations()
    repair_intermediate_bib_frontier()
    repair_generated_test_escape()


if __name__ == "__main__":
    main()
