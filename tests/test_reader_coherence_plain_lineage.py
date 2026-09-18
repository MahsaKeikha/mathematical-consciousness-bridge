from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_plain_language_is_p100_current_and_reader_first() -> None:
    page = _read("website/plain-language.html")
    assert "P93 is the current checkpoint" not in page
    assert "all 99 Research II results" not in page
    assert "Current Research II frontier: P100" in page
    assert "You can understand the project without reading the proposition archive" in page
    assert 'id="technical-frontier-history"' in page
    assert 'id="p100-reader-frontier"' in page
    assert 'id="p93-reader-frontier"' in page


def test_research_lineage_is_ordered_by_research_stage() -> None:
    page = _read("website/research-lineage.html")
    i = page.index('id="research-i"')
    ii = page.index('id="research-ii"')
    iii = page.index('id="research-iii"')
    assert i < ii < iii

    research_i = page[i:ii]
    research_ii = page[ii:iii]
    research_iii = page[iii:]

    assert "V46-V50" not in research_i
    assert "consciousness-measurement-science" not in research_i
    assert "Research II · current frontier · P100" in research_ii
    assert "V1-V50" in research_iii
    assert "V46-V50 · cross-site replication inference and stability" in research_iii


def test_research_three_lineage_exposes_assumptions_without_claiming_theory_neutrality() -> None:
    page = _read("website/research-lineage.html")
    assert "theory-neutral" not in page
    assert "makes its scientific commitments explicit rather than claiming theory neutrality" in page
    assert "Target choice, evidence channels, validation domains, and claim ceilings" in page
