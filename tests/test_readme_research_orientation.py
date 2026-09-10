from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs" / "detailed_proposition_record.md"


def test_readme_follows_reader_first_scientific_order():
    text = README.read_text(encoding="utf-8")
    plain = text.index("# What this project is trying to achieve, in plain language")
    abstract = text.index("# Abstract")
    status = text.index("# Scientific status discipline")
    glance = text.index("# Research at a glance")
    formulation = text.index("# 1. Mathematical formulation of the bridge problem")
    open_section = text.index("# What remains open")
    detail = text.index("# Detailed proposition record")

    assert plain < abstract < status < glance < formulation < open_section < detail


def test_research_at_a_glance_covers_the_full_scientific_program():
    text = README.read_text(encoding="utf-8")
    start = text.index("# Research at a glance")
    end = text.index("# 1. Mathematical formulation of the bridge problem")
    section = text[start:end]
    required = [
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P25-P37",
        "P38-P44",
        "P45-P58",
        "Calibration and integer optimization",
        "docs/calibration_optimization_frontier_p61_p70.md",
        "Proved / implemented / tested",
        "docs/theorem_roadmap.md",
        "docs/research_navigation.md",
        "docs/equation_and_citation_map.md",
    ]
    for token in required:
        assert token in section, token


def test_detailed_record_preserves_full_p1_to_p70_chronology_off_main_page():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")

    assert "docs/detailed_proposition_record.md" in readme
    assert "Complete P1 to P70 chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in detail
    assert "Open the complete P1 to P70 chronology" not in readme


def test_front_page_has_no_stale_pre_p70_research_record_counts():
    text = README.read_text(encoding="utf-8")
    assert "proposition-level results | **45**" not in text
    assert "total equation-driven quantitative figures | **58**" not in text
    assert "70 proposition-level results" in text
    assert "**P70**" in text
