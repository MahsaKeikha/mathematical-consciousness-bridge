"""Finalize the P90 publication state before merge.

This is a temporary migration helper. It repairs the canonical P90 promoter and
publication-contract migrator, runs them, closes the remaining publication
residuals, and leaves the repository in a deterministic P90 state for CI.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def repair_promoter() -> None:
    path = ROOT / "scripts" / "promote_p90_public_frontier.py"
    text = path.read_text(encoding="utf-8")

    append_anchor = '    text = append_once(text, "## P90: exact nonlinear rank-one slice separation",'
    dep_code = (
        '    p89_dependency = "&\\\\text{P89: complete linear parity-functional duality closes all real linear directions on the eleven canonical parity coordinates}"\n'
        '    p90_dependency = "&\\\\text{P90: exact nonlinear rank-one slice separation exploits product-law image structure beyond the complete P89 linear envelope}"\n'
        '    if p90_dependency not in text:\n'
        '        if p89_dependency not in text:\n'
        '            raise RuntimeError("P89 dependency-map anchor missing")\n'
        '        text = text.replace(p89_dependency, p89_dependency + "\\\\\\\\n&\\\\Downarrow\\\\\\\\n" + p90_dependency, 1)\n\n'
    )
    if 'p90_dependency = "&\\\\text{P90:' not in text:
        if append_anchor not in text:
            raise RuntimeError("P90 roadmap append anchor missing")
        text = text.replace(append_anchor, dep_code + append_anchor, 1)

    index_anchor = '        ("Current theorem frontier · P89", "Current theorem frontier · P90"),\n'
    if '("The 89 results form several dependency branches.", "The 90 results form several dependency branches.")' not in text:
        if index_anchor not in text:
            raise RuntimeError("homepage replacement anchor missing")
        text = text.replace(
            index_anchor,
            index_anchor
            + '        ("The 89 results form several dependency branches.", "The 90 results form several dependency branches."),\n'
            + '        ("all 89 propositions", "all 90 propositions"),\n',
            1,
        )

    readme_anchor = '        ("The current public theorem frontier is **P89**.", "The current public theorem frontier is **P90**."),\n'
    if '"**Public theorem frontier:** P89", "**Public theorem frontier:** P90"' not in text:
        if readme_anchor not in text:
            raise RuntimeError("README frontier anchor missing")
        text = text.replace(
            readme_anchor,
            readme_anchor
            + '        ("**Public theorem frontier:** P89", "**Public theorem frontier:** P90"),\n',
            1,
        )

    links_old = (
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/'
        'blob/main/docs/{PROVENANCE_NAME}">{PROVENANCE_NAME}</a></p>'
    )
    links_new = (
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/'
        'blob/main/docs/{PROVENANCE_NAME}">{PROVENANCE_NAME}</a> · '
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/'
        'blob/main/src/consciousness_bridge/{SOURCE_NAME}">{SOURCE_NAME}</a> · '
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/'
        'blob/main/tests/{TEST_NAME}">{TEST_NAME}</a></p>'
    )
    if 'blob/main/src/consciousness_bridge/{SOURCE_NAME}' not in text:
        if links_old not in text:
            raise RuntimeError("P90 homepage links anchor missing")
        text = text.replace(links_old, links_new, 1)

    roadmap_anchor = '        ("## After P89", "## After P90"),\n'
    if '("continuation beyond P89", "continuation beyond P90")' not in text:
        if roadmap_anchor not in text:
            raise RuntimeError("roadmap future-work anchor missing")
        text = text.replace(
            roadmap_anchor,
            roadmap_anchor
            + '        ("continuation beyond P89", "continuation beyond P90"),\n'
            + '        ("A future P90 claim", "A future P91 claim"),\n',
            1,
        )

    old = 'append_once(text, "## P90: exact nonlinear rank-one slice separation", f\'\'\''
    new = 'append_once(text, "## P90: exact nonlinear rank-one slice separation", fr\'\'\''
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def repair_contract_migrator() -> None:
    path = ROOT / "scripts" / "advance_p90_publication_contracts.py"
    text = path.read_text(encoding="utf-8")

    old = '            ("Previous theorem frontier · P88", "Previous theorem frontier · P89"),\n'
    if '("text[p88:p87]", "text[p89:p88]")' not in text:
        if old not in text:
            raise RuntimeError("historical atlas assertion anchor missing")
        text = text.replace(
            old,
            old + '            ("text[p88:p87]", "text[p89:p88]"),\n',
            1,
        )

    marker = '    patch(\n        ".github/workflows/figures.yml",\n'
    repair = (
        '    target = ROOT / "tests/test_figure_publication_sync.py"\n'
        '    test_text = target.read_text(encoding="utf-8")\n'
        '    old = "    p90 = text.index(\\\'id=\\\"p90-frontier\\\"\\\')\\n    p88 = text.index(\\\'id=\\\"p88-frontier\\\"\\\')"\n'
        '    new = "    p90 = text.index(\\\'id=\\\"p90-frontier\\\"\\\')\\n    p89 = text.index(\\\'id=\\\"p89-frontier\\\"\\\')\\n    p88 = text.index(\\\'id=\\\"p88-frontier\\\"\\\')"\n'
        '    if old in test_text:\n'
        '        test_text = test_text.replace(old, new, 1)\n'
        '    test_text = test_text.replace("text[p88:p87]", "text[p89:p88]", 1)\n'
        '    target.write_text(test_text, encoding="utf-8")\n\n'
    )
    if 'test_text = test_text.replace("text[p88:p87]", "text[p89:p88]", 1)' not in text:
        if marker not in text:
            raise RuntimeError("figure-test repair insertion anchor missing")
        text = text.replace(marker, repair + marker, 1)

    path.write_text(text, encoding="utf-8")


def close_residuals() -> None:
    repro = ROOT / "docs" / "reproducibility.md"
    text = repro.read_text(encoding="utf-8")
    start = text.find("## 5. Focused audit of the current P89 frontier")
    if start == -1:
        start = text.find("## 5. Focused audit of the current P90 frontier")
    if start == -1:
        raise RuntimeError("focused audit section not found")
    end = text.find("\n---\n", start)
    if end == -1:
        end = len(text)
    block = r'''## 5. Focused audit of the current P90 frontier

The current theorem frontier is **P90**.

Its direct technical record is:

```text
docs/proposition_90_exact_nonlinear_rank_one_separation.md
docs/proposition_90_equation_provenance.md
src/consciousness_bridge/exact_nonlinear_rank_one_separation.py
tests/test_exact_nonlinear_rank_one_separation.py
docs/figures/p90_exact_nonlinear_rank_one_separation.svg
figures/manifest.json
```

Run the focused theorem and figure-publication checks with:

```bash
python -m pytest \
  tests/test_exact_nonlinear_rank_one_separation.py \
  tests/test_figure_publication_sync.py \
  tests/test_frontier_publication_consistency.py
```

P90 uses a genuinely nonlinear constraint of the declared strict P75 model image. Because prevalence is fixed at zero, the active observable law is one product Bernoulli component, and the canonical two-by-two slice must satisfy `ad = bc`. For the established empirical slice,

```text
q1000 = 1/8
q1001 = 1/24
q1010 = 0
q1011 = 5/24
```

the determinant residual is `5/192` and the slice mass is `3/8`. Therefore every rank-one slice within L-infinity radius `epsilon` must satisfy

\[
\epsilon \ge \frac{5/192}{3/8} = \frac5{72}.
\]

The rational P75 parameter point

```text
(0, 3/5, 1/2, 3/8, 3/4, 5/9, 1/2, 2/3, 3/4)
```

attains full-law L-infinity distance exactly `5/72`, so the lower and upper certificates match:

\[
L_{90}=\frac5{72}=\frac73L_{89},\qquad L_{89}=\frac5{168}.
\]

P90 is exact only for the declared strict P75 box and its fixed extreme-prevalence product-law image. It does not identify consciousness, establish nonphysicality, exhaust more general nonlinear mixture constraints, or close the physical-to-experiential bridge.
'''
    repro.write_text(text[:start] + block + text[end:], encoding="utf-8")

    prepare = ROOT / "scripts" / "prepare_website.py"
    text = prepare.read_text(encoding="utf-8")
    replacements = (
        (
            '<strong>89</strong><span>proposition-level results</span>',
            '<strong>90</strong><span>proposition-level results</span>',
        ),
        (
            '<strong>P89</strong><span>current theorem frontier</span>',
            '<strong>P90</strong><span>current theorem frontier</span>',
        ),
    )
    for old, new in replacements:
        text = text.replace(old, new)
        if new not in text:
            raise RuntimeError(f"P90 Research Lineage validator token missing: {new}")
    prepare.write_text(text, encoding="utf-8")


def main() -> None:
    repair_promoter()
    repair_contract_migrator()
    run("python", "scripts/promote_p90_public_frontier.py")
    run("python", "scripts/advance_p90_publication_contracts.py")
    close_residuals()
    run("python", "scripts/normalize_documentation_punctuation.py")
    run("python", "scripts/sync_figure_publication.py")
    print("P90 publication state finalized")


if __name__ == "__main__":
    main()
