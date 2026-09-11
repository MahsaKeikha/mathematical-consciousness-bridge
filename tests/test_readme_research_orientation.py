from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs" / "detailed_proposition_record.md"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def test_readme_follows_reader_first_scientific_order():
    text = README.read_text(encoding="utf-8")
    plain = text.index("# What this project is trying to achieve, in plain language")
    abstract = text.index("# Abstract")
    status = text.index("# Scientific status discipline")
    reading = text.index("# How to read this study")
    glance = text.index("# Research at a glance")
    formulation = text.index("# 1. Mathematical formulation of the bridge problem")
    p71 = text.index("## 1.5 P71: target provenance cannot be circular")
    p72 = text.index("## 1.6 P72: noisy target observation is a separate scientific layer")
    p73 = text.index("## 1.7 P73: target-channel reliability can sometimes be identified")
    p74 = text.index("## 1.8 P74: finite samples must certify target-channel recovery")
    operational = text.index("# 2. From physical dynamics to operational structure")
    scale = text.index("# 3. Time, composition, and scale cannot be ignored")
    finite = text.index("# 4. Turning a population theorem into a finite experiment")
    fundamental = text.index("# 4.4 Fundamental theory / Theory-of-Everything interface")
    quantum = text.index("# 5. Quantum mechanics enters as a physical description")
    adaptive = text.index("# 6. Adaptive experiment design")
    calibration = text.index("# 7. Calibration and optimization as a downstream experimental layer")
    established = text.index("# What has actually been established")
    open_section = text.index("# What remains open")
    falsification = text.index("# Falsification logic")
    evidence = text.index("# Evidence, references, and provenance")
    visuals = text.index("# Complete visual evidence without front-page overload")
    validation = text.index("# Numerical validation facts")
    reproducibility = text.index("# Reproducibility and audit path")
    detail = text.index("# Detailed proposition record")
    current = text.index("# Current scientific status")
    navigation = text.index("# Navigation")

    assert plain < abstract < status < reading < glance < formulation
    assert formulation < p71 < p72 < p73 < p74 < operational < scale < finite < fundamental
    assert fundamental < quantum < adaptive < calibration
    assert calibration < established < open_section < falsification < evidence
    assert evidence < visuals < validation < reproducibility < detail < current < navigation


def test_plain_language_section_explains_full_program_without_equations():
    text = README.read_text(encoding="utf-8")
    section = _plain_language_section(text)

    required = (
        "would that description also be enough to determine what, if anything, is experienced",
        "physical-to-experiential bridge",
        "without assuming the answer in advance",
        "define the physical side clearly",
        "define the experiential target independently",
        "P71 formalizes this circularity problem",
        "P72 therefore separates the underlying target from the way it is observed",
        "P73 asks when that reliability can be learned",
        "its reliability must itself be identifiable, independently calibrated, or honestly left uncertain",
        "P74 asks the practical follow-up",
        "available finite data justify trusting that recovery",
        "does the physical description actually contain enough information",
        "would not automatically prove that consciousness lies outside physics",
        "finite data",
        "complete quantum description",
        "attempts to expose these alternatives",
        "capable of proving that rule wrong if it is false",
        "physical-to-experiential bridge itself remains open",
    )
    for phrase in required:
        assert phrase in section, phrase

    for forbidden in (
        "$$",
        "\\boxed",
        "\\begin",
        "\\frac",
        "I(E;",
        "E=B",
        "\\Omega",
        "\\gamma",
    ):
        assert forbidden not in section, forbidden

    assert len(section.split()) >= 900


def test_research_at_a_glance_covers_the_full_scientific_program():
    text = README.read_text(encoding="utf-8")
    start = text.index("# Research at a glance")
    end = text.index("# 1. Mathematical formulation of the bridge problem")
    section = text[start:end]
    required = [
        "P1-P10",
        "P11-P18",
        "P19-P24, P71-P74",
        "P25-P37",
        "P38-P44",
        "P45-P60",
        "P61-P70",
        "docs/calibration_optimization_frontier_p61_p70.md",
        "Proved / implemented / tested",
        "docs/theorem_roadmap.md",
        "docs/research_navigation.md",
        "docs/equation_and_citation_map.md",
    ]
    for token in required:
        assert token in section, token


def test_detailed_record_preserves_full_p1_to_p74_chronology_off_main_page():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")

    assert "docs/detailed_proposition_record.md" in readme
    assert "Complete P1 to P74 chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in detail
    assert "**P71** returns from the downstream calibration branch" in detail
    assert "**P72** adds the next target-side obligation" in detail
    assert "**P73** closes the population identifiability step" in detail
    assert "**P74** adds finite-sample certification" in detail
    assert "Open the complete P1 to P74 chronology" not in readme


def test_front_page_has_current_research_record_counts():
    text = README.read_text(encoding="utf-8")
    assert "proposition-level results | **45**" not in text
    assert "total equation-driven quantitative figures | **58**" not in text
    assert "74 proposition-level results" in text
    assert "**P74**" in text
    assert "**62**" in text
