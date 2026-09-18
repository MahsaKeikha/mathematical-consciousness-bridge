from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_plain_language_is_conceptual_not_a_theorem_changelog() -> None:
    page = (ROOT / "website/plain-language.html").read_text(encoding="utf-8")

    assert "If you remember only three things" in page
    assert "100 linked results · technical endpoint P100" in page
    assert "A note about proposition numbers" in page
    assert "P93 is the current checkpoint" not in page
    assert re.search(r'id="p\\d+-reader-frontier"', page) is None


def test_plain_language_keeps_the_three_programs_distinct() -> None:
    page = (ROOT / "website/plain-language.html").read_text(encoding="utf-8")

    research_i = page.index("<span>Research I</span>")
    research_ii = page.index("<span>Research II</span>")
    research_iii = page.index("<span>Research III</span>")

    assert research_i < research_ii < research_iii
    assert "Finding a physical system is not the same as finding consciousness" in page
    assert "A failed bridge test has a limited meaning" in page
    assert "Uncertainty is a valid scientific result" in page
