from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "website" / "research-map.html"
TEST = ROOT / "tests" / "test_complete_research_map_proposition_navigator.py"

NAV_START = "<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->"
NAV_END = "<!-- END COMPLETE PROPOSITION NAVIGATOR -->"

REPLACEMENTS = [
    (
        "and P96 separates pilot-selected regime design from independent holdout certification.</p>",
        "and P96 separates pilot-selected regime design from independent holdout certification, "
        "P97 protects same-data selection over a finite predeclared candidate family, P98 rotates "
        "selection-valid holdout certification across independent blocks, P99 aggregates distributed "
        "cross-fitted evidence with e-values, and P100 makes fresh P99 rounds anytime-valid under "
        "predictable reserve stakes.</p>",
    ),
    (
        "Recover and test the declared target model, then strengthen one-sided rejection through exact global, parity, linear-duality, and nonlinear algebraic constraints, culminating in P92 exact global mixed-prevalence distance, the P93 IID finite-sample handoff, P94 finite-range dependent rejection, and P95 drift-aware stratified rejection.",
        "Recover and test the declared target model, then strengthen one-sided rejection through exact global, parity, linear-duality, nonlinear, selection-valid, and sequential inference, culminating in P100 anytime-valid repeated inspection and stopping across fresh P99 rounds.",
    ),
    (
        "<h2>P19 and P71-P100: from sufficiency to finite-range dependent target-model falsification</h2>",
        "<h2>P19 and P71-P100: from sufficiency to selection-valid and anytime-valid target-model falsification</h2>",
    ),
    (
        "P77-P100 move from full-law confidence-region separation to exact continuous-family lower bounds, stronger observable constraints, complete real-linear closure, nonlinear model-image separation, and localized finite-sample rejection under IID and declared finite-range dependence.",
        "P77-P100 move from full-law confidence-region separation to exact continuous-family lower bounds, stronger observable constraints, complete real-linear closure, nonlinear model-image separation, localized finite-sample rejection, selection-valid certification, distributed e-value aggregation, and anytime-valid sequential stopping.",
    ),
    (
        "<h2>P77-P100: from full-law rejection to finite-range dependent localized nonlinear certification</h2>",
        "<h2>P77-P100: from full-law rejection to anytime-valid sequential certification</h2>",
    ),
    (
        "P93 adds localized IID finite-sample sign preservation, P94 extends that rejection gate to declared finite-range dependence under one common marginal law, P95 adds predeclared regime-level drift handling without pooling, and P96 permits pilot-selected regime plans under a frozen-plan independent-holdout design.</p>",
        "P93 adds localized IID finite-sample sign preservation, P94 extends that rejection gate to declared finite-range dependence under one common marginal law, P95 adds predeclared regime-level drift handling without pooling, P96 permits pilot-selected regime plans under a frozen-plan independent-holdout design, P97 protects finite predeclared same-data candidate selection, P98 cross-fits frozen plans across independent blocks, P99 combines distributed fold evidence with exact e-values, and P100 adds anytime-valid sequential evidence accumulation across fresh rounds.</p>",
    ),
    (
        "<p>P99 remains a conditional model-rejection theorem under its declared independent-block, own-fold-exclusion, frozen-plan, and exact error-budget assumptions. P95 remains the immediate drift-aware predecessor under its declared finite-range dependence and common-marginal assumptions. It does not identify the latent state with consciousness, establish nonphysicality, validate a replacement theory, or close the physical-to-experiential bridge. The current mathematics narrows what a declared model can explain; it does not convert model rejection into an ontological conclusion.</p>",
        "<p>P100 remains a conditional sequential model-rejection theorem under its declared fresh-round, conditional e-value validity, and predictable reserve-stake assumptions. P99 remains its immediate distributed-evidence predecessor under independent-block, own-fold-exclusion, frozen-plan, and exact calibration conditions. P95 remains the drift-aware predecessor under declared finite-range dependence and common-marginal assumptions. None of these results identifies the latent state with consciousness, establishes nonphysicality, validates a replacement theory, or closes the physical-to-experiential bridge. The current mathematics narrows what a declared model can explain; it does not convert model rejection into an ontological conclusion.</p>",
    ),
]


def replace_exact_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one exact Research Map phrase, found {count}: {old[:90]!r}")
    return text.replace(old, new, 1)


def clean_inline_markdown(value: str, *, sentence_case: bool = False) -> str:
    cleaned = value.replace("`", "")
    if sentence_case and cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned


def polish_navigator(page: str) -> str:
    before, rest = page.split(NAV_START, 1)
    navigator, after = rest.split(NAV_END, 1)

    navigator = re.sub(
        r"<strong>(.*?)</strong>",
        lambda match: f"<strong>{clean_inline_markdown(match.group(1), sentence_case=True)}</strong>",
        navigator,
    )
    navigator = re.sub(
        r'<span class="proposition-nav-object">(.*?)</span>',
        lambda match: (
            '<span class="proposition-nav-object">'
            f"{clean_inline_markdown(match.group(1))}</span>"
        ),
        navigator,
    )
    navigator = re.sub(
        r'<span class="proposition-nav-status">(.*?)</span>',
        lambda match: (
            '<span class="proposition-nav-status">'
            f"{clean_inline_markdown(match.group(1))}</span>"
        ),
        navigator,
    )
    return before + NAV_START + navigator + NAV_END + after


def append_regression_test(test_text: str) -> str:
    marker = "def test_research_map_p100_frontier_copy_is_current() -> None:"
    if marker in test_text:
        return test_text
    return test_text.rstrip() + '''\n\n\ndef test_research_map_p100_frontier_copy_is_current() -> None:\n    page = PAGE.read_text(encoding="utf-8")\n    assert "P19 and P71-P100: from sufficiency to selection-valid and anytime-valid target-model falsification" in page\n    assert "P77-P100: from full-law rejection to anytime-valid sequential certification" in page\n    assert "P100 remains a conditional sequential model-rejection theorem" in page\n    assert "P97 protects same-data selection over a finite predeclared candidate family" in page\n    assert "P99 aggregates distributed cross-fitted evidence with e-values" in page\n    assert "P100 makes fresh P99 rounds anytime-valid under predictable reserve stakes" in page\n    assert "P77-P100: from full-law rejection to finite-range dependent localized nonlinear certification" not in page\n    assert "P99 remains a conditional model-rejection theorem under its declared independent-block" not in page\n\n\ndef test_navigator_cards_render_plain_reader_text() -> None:\n    page = PAGE.read_text(encoding="utf-8")\n    block = page.split("<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->", 1)[1].split(\n        "<!-- END COMPLETE PROPOSITION NAVIGATOR -->", 1\n    )[0]\n    assert "`" not in block\n    assert "<strong>Representation-independent bridge objects</strong>" in block\n    assert "<strong>Full mixed-prevalence P75 separation bracket" in block\n'''


def main() -> None:
    page = PAGE.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        page = replace_exact_once(page, old, new)
    page = polish_navigator(page)
    PAGE.write_text(page, encoding="utf-8")

    test_text = TEST.read_text(encoding="utf-8")
    TEST.write_text(append_regression_test(test_text), encoding="utf-8")

    navigator = page.split(NAV_START, 1)[1].split(NAV_END, 1)[0]
    if navigator.count('class="proposition-nav-card"') != 100:
        raise RuntimeError("Polish pass changed the 100-card navigator contract")
    if "`" in navigator:
        raise RuntimeError("Raw Markdown code ticks remain in the static navigator")


if __name__ == "__main__":
    main()
