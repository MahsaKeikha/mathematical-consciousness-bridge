from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def test_readme_opens_with_plain_language_abstract_and_research_map():
    text = README.read_text(encoding="utf-8")
    plain = text.index("# What this project is trying to achieve, in plain language")
    abstract = text.index("# Abstract")
    glance = text.index("# Research at a glance")
    detailed = text.index("# Detailed proposition record")
    assert plain < abstract < glance < detailed


def test_research_at_a_glance_covers_the_full_scientific_program():
    text = README.read_text(encoding="utf-8")
    start = text.index("# Research at a glance")
    end = text.index("# Detailed proposition record")
    section = text[start:end]
    required = [
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P25-P37",
        "P38-P44",
        "P45-P58",
        "P59-P70",
        "Proved / implemented / tested",
        "Open physical-to-experiential bridge",
        "docs/theorem_roadmap.md",
        "docs/research_navigation.md",
        "docs/equation_and_citation_map.md",
        "website/index.html",
    ]
    for token in required:
        assert token in section, token


def test_detailed_record_preserves_full_p1_to_p70_chronology():
    text = README.read_text(encoding="utf-8")
    start = text.index("# Detailed proposition record")
    section = text[start:]
    assert "P1 to P70 chronology" in section
    assert "Propositions **P1-P10**" in section
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in section


def test_front_page_has_no_stale_pre_p70_research_record_counts():
    text = README.read_text(encoding="utf-8")
    assert "proposition-level results | **45**" not in text
    assert "total equation-driven quantitative figures | **58**" not in text
