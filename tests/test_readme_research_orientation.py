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
