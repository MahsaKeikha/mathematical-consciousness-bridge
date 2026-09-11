import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs" / "detailed_proposition_record.md"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


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
    p75 = text.index("## 1.9 P75: identifiability does not by itself validate the target model")
    p76 = text.index("## 1.10 P76: finite data must separate model failure from sampling noise")
    p77 = text.index("## 1.11 P77: full-law confidence regions can reject the complete declared model set")
    p78 = text.index("## 1.12 P78: certified continuous separation for the P75 model family")
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
    assert formulation < p71 < p72 < p73 < p74 < p75 < p76 < p77 < p78 < operational < scale < finite < fundamental
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
        "P75 asks whether successful recovery also validates the measurement model itself",
        "generically just-identified",
        "A fourth binary view creates additional observable constraints",
        "P76 asks the next practical question",
        "finite data are strong enough to demonstrate that one of those requirements has genuinely failed",
        "P77 closes the next logical gap",
        "any distribution allowed by the entire declared measurement model",
        "finding one imperfect best-fitting model is not enough",
        "P78 addresses the computational problem that P77 deliberately leaves open",
        "continuous family generated by nine parameters",
        "mathematically guaranteed lower bound for every box",
        "any explicit candidate model supplies an upper bound",
        "exact rational arithmetic",
        "separately valid upper bound on the P77 sampling radius",
        "does not turn failure to reject into model validation",
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

    assert len(section.split()) >= 1000


def test_research_at_a_glance_covers_the_full_scientific_program():
    text = README.read_text(encoding="utf-8")
    start = text.index("# Research at a glance")
    end = text.index("# 1. Mathematical formulation of the bridge problem")
    section = text[start:end]
    frontier = _frontier()
    required = [
        "P1-P10",
        "P11-P18",
        f"P19-P24, P71-P{frontier}",
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


def test_detailed_record_preserves_full_chronology_off_main_page():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()

    assert "docs/detailed_proposition_record.md" in readme
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in detail
    assert "**P71** returns from the downstream calibration branch" in detail
    assert "**P72** adds the next target-side obligation" in detail
    assert "**P73** closes the population identifiability step" in detail
    assert "**P74** converts the P73 population inversion into a finite-sample confidence certificate" in detail
    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail
    assert "**P76** converts the tracked P75 population adequacy restrictions" in detail
    assert "**P77** closes the finite-data full-law gap left explicit by P76" in detail
    assert "**P78** supplies the continuous-family optimization certificate required by P77" in detail
    assert f"Open the complete P1 to P{frontier} chronology" not in readme


def test_front_page_has_current_research_record_counts():
    text = README.read_text(encoding="utf-8")
    frontier = _frontier()
    assert "proposition-level results | **45**" not in text
    assert "total equation-driven quantitative figures | **58**" not in text
    assert f"{frontier} proposition-level results" in text
    assert f"The theorem frontier is P{frontier}." in text

    match = re.search(r"\| Equation-driven quantitative figures \| \*\*(\d+)\*\* \|", text)
    assert match is not None
    assert int(match.group(1)) >= 64
