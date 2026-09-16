import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = ROOT / "website" / "start-here.html"


def _start_here() -> str:
    return START.read_text(encoding="utf-8")


def test_start_here_separates_model_adequacy_from_inference_validity() -> None:
    text = _start_here()

    assert "P75-P92 test the declared target-measurement model itself" in text
    assert "P93-P100 carry population separation into IID finite data" in text
    assert "P75-P100 test the declared target-measurement model itself" not in text

    for token in (
        "finite-range dependence",
        "declared drift",
        "selection-valid holdout",
        "candidate selection",
        "cross-fitting",
        "e-value aggregation",
        "anytime-valid sequential evidence",
    ):
        assert token in text


def test_scientific_role_grid_is_gap_free_from_p1_through_p100() -> None:
    text = _start_here()
    section = text.split("<h2>The 100 Research II propositions by scientific role</h2>", 1)[1]
    section = section.split("</section>", 1)[0]

    ranges = [
        (int(start), int(end))
        for start, end in re.findall(r"<span>P(\d+)-P(\d+)</span>", section)
    ]
    covered = [number for start, end in ranges for number in range(start, end + 1)]

    assert ranges == [
        (1, 10),
        (11, 18),
        (19, 24),
        (25, 37),
        (38, 44),
        (45, 60),
        (61, 70),
        (71, 74),
        (75, 92),
        (93, 100),
    ]
    assert covered == list(range(1, 101))


def test_late_research_ii_role_descriptions_match_theorem_progression() -> None:
    text = _start_here()

    assert "<span>P75-P92</span><h3>Target-model adequacy and separation</h3>" in text
    assert "<span>P93-P100</span><h3>Finite-data and adaptive inference</h3>" in text
    assert text.index("<span>P75-P92</span>") < text.index("<span>P93-P100</span>")
    assert "The physical-to-experiential step remains open" in text


def test_start_here_role_fix_respects_reader_punctuation_policy() -> None:
    text = _start_here()
    assert "\u2013" not in text
    assert "\u2014" not in text
