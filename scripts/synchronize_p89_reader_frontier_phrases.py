"""Synchronize canonical documentation to the P89 theorem frontier.

The formal package release remains v0.82.0; the documented theorem frontier can
advance independently. Historical P88 material remains part of the audit trail,
while current-frontier labels, navigation, reproducibility, and proposition
counts move to P89.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

P89_PROOF = "proposition_89_complete_linear_parity_duality.md"
P89_PROVENANCE = "p89_equation_provenance.md"
P89_FIGURE = "figures/p89_complete_linear_parity_duality.svg"
P89_SOURCE = "../src/consciousness_bridge/complete_linear_parity_duality.py"
P89_TEST = "../tests/test_complete_linear_parity_duality.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str, changed: list[str]) -> None:
    original = read(path)
    if original != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def replace_many(text: str, replacements: tuple[tuple[str, str], ...]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def sync_readme(changed: list[str]) -> None:
    path = ROOT / "README.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current public theorem frontier is **P88**.", "The current public theorem frontier is **P89**."),
            ("**Public theorem frontier:** P88", "**Public theorem frontier:** P89"),
            ("[Read the current frontier](docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)", f"[Read the current frontier](docs/{P89_PROOF})"),
            ("88 proposition-level results", "89 proposition-level results"),
            ("P1 through P88", "P1 through P89"),
            ("P71-P88", "P71-P89"),
            ("P75-P88", "P75-P89"),
        ),
    )
    current_section = re.compile(
        r"### Current theorem frontier\n\n!\[P88 .*?\n\n(?=##|###|$)",
        re.DOTALL,
    )
    replacement = f'''### Current theorem frontier\n\n![P89 Complete Linear Parity-Functional Duality Certificate](docs/figures/p89_complete_linear_parity_duality.svg)\n\n**Figure 2. P89 exact complete linear parity-functional duality certificate.** P89 removes the finite coefficient-radius and four-observable support restrictions of P88. On the established exact-rational witness, one real eleven-coordinate functional gives a normalized lower bound of `5/168`; a matching rational convex-vertex plus zero-mass perturbation certificate gives the same universal upper bound. Therefore the complete real linear parity-functional optimum is exactly `5/168`, strictly stronger than `L88 = 1/64`. This remains a conditional model-separation theorem for the declared P75 family and does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.\n\n'''
    text, count = current_section.subn(replacement, text, count=1)
    if count == 0 and "P89 Complete Linear Parity-Functional Duality Certificate" not in text:
        raise RuntimeError("README current frontier section was not found")
    write_if_changed(path, text, changed)


def sync_start_here_markdown(changed: list[str]) -> None:
    path = ROOT / "START_HERE.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The public theorem frontier is **P88**.", "The public theorem frontier is **P89**."),
            ("P75 through P88", "P75 through P89"),
            ("P71 through P88", "P71 through P89"),
            ("P1 through P88", "P1 through P89"),
            ("88 proposition", "89 proposition"),
        ),
    )
    write_if_changed(path, text, changed)


def sync_theorem_roadmap(changed: list[str]) -> None:
    path = DOCS / "theorem_roadmap.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P88**. The proposition record runs from **P1 through P88 with explicit dependency branches**.",
        "The current documented theorem frontier is **P89**. The proposition record runs from **P1 through P89 with explicit dependency branches**.",
    )
    p88_line = r"&\text{P88: radius-three bounded primitive four-event parity functionals extend the exact coefficient box to |c_i| <= 3}"
    p89_line = r"&\text{P89: complete linear parity-functional duality closes all real linear directions on the eleven canonical parity coordinates}"
    if p89_line not in text:
        if p88_line not in text:
            raise RuntimeError("theorem roadmap P88 dependency line is missing")
        text = text.replace(p88_line, p88_line + r"\\" + "\n" + r"&\Downarrow\\" + "\n" + p89_line, 1)

    p88_row = "| [P88](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md) | radius-three bounded primitive four-event parity functionals | exact coefficient-radius extension that strictly strengthens P87 on the declared witness | proved conditional computational theorem |"
    p89_row = "| [P89](proposition_89_complete_linear_parity_duality.md) | complete real linear parity-functional duality | removes coefficient-radius/support cutoffs and gives matching exact lower/upper certificates | proved conditional computational theorem |"
    if p89_row not in text:
        if p88_row not in text:
            raise RuntimeError("theorem roadmap P88 proposition row is missing")
        text = text.replace(p88_row, p88_row + "\n" + p89_row, 1)

    p89_section = r'''## P89: complete linear parity-functional duality

P89 closes a different gap from P88. Rather than increasing the integer coefficient radius again, it removes both the coefficient-radius restriction and the exactly-four-observable support restriction. Let \(y(p)\in\mathbb R^{11}\) be the vector of the eleven canonical P83 even-parity probabilities and let \(c\in\mathbb R^{11}\setminus\{0\}\). The scalar functional

\[
Q_c(p)=c^\top y(p)
\]

is multi-affine in the P75 parameters, so its exact range on a rational parameter box is determined by the finite parity vectors at box vertices. With the centered full-law transfer norm

\[
D(c)=\min_a\sum_x |(Ac)_x-a|,
\]

P89 defines the complete linear certificate

\[
L_{\mathrm{lin}}(B)=\sup_{c\ne0}\frac{\operatorname{dist}(c^\top y(\widehat p),I_B(c))}{D(c)}.
\]

A finite LP duality shows that this supremum equals the minimum signed full-law perturbation radius needed to write the empirical parity vector as a convex combination of P75 box-vertex parity vectors plus \(A^\top\delta\) with \(\mathbf1^\top\delta=0\). On the established rational witness, the exact lower functional

```text
(0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)
```

has empirical value `-13/6`, exact P75 interval `[-51/8,-3]`, gap `5/6`, centered norm `28`, and therefore lower bound `5/168`. A matching rational convex-vertex plus zero-mass perturbation certificate has `||delta||_infinity = 5/168`, proving

\[
\boxed{L_{\mathrm{lin}}(B)=L_{89}(B)=\frac5{168}>\frac1{64}=L_{88}(B).}
\]

No larger coefficient radius, denser support, or other real linear combination of the same eleven parity coordinates can improve this value on the stated box. Nonlinear P75 constraints and observables outside this eleven-coordinate family remain open directions.

- Proof: [P89](proposition_89_complete_linear_parity_duality.md)
- Provenance: [p89_equation_provenance.md](p89_equation_provenance.md)
- Figure: [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg)
- Source: [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py)
- Tests: [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py)

P89 remains a conditional model-separation theorem for the declared P75 target-measurement family. It does not identify the latent state with consciousness, establish nonphysicality, validate an alternative model, or close the physical-to-experiential bridge.

## After P89

P89 closes the complete **linear** parity-functional class on the eleven declared parity coordinates. A future P90 claim should therefore address a different gap, such as nonlinear joint parity constraints, additional observable families, or a tighter use of the nonlinear P75 image, and must include a certificate not already implied by P89.'''

    pattern = re.compile(r"## After P88\n\n.*?(?=\n## |\Z)", re.DOTALL)
    if "## P89: complete linear parity-functional duality" not in text:
        match = pattern.search(text)
        if match is None:
            raise RuntimeError("theorem roadmap After P88 block is missing")
        text = text[: match.start()] + p89_section + text[match.end() :]
    else:
        text = text.replace("## After P88", "## After P89")
    text = text.replace("After P88, the target-side chain", "After P89, the target-side chain")
    text = text.replace("continuation beyond P88", "continuation beyond P89")
    write_if_changed(path, text, changed)


def sync_detailed_record(changed: list[str]) -> None:
    path = DOCS / "detailed_proposition_record.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("## Complete P1 to P88 chronology", "## Complete P1 to P89 chronology"),
            ("88 disconnected proposition-level results", "89 disconnected proposition-level results"),
        ),
    )
    if "## Proposition 89: Complete Linear Parity-Functional Duality Certificate" not in text:
        text += '''\n\n## Proposition 89: Complete Linear Parity-Functional Duality Certificate\n\nP89 removes P88's finite coefficient-radius and four-observable support restrictions and studies every real linear functional of all eleven canonical P83 parity coordinates. Finite-dimensional duality matches a functional lower certificate to a convex P75 box-vertex plus zero-mass signed-perturbation upper certificate. On the established exact rational witness both sides equal `5/168`, strictly strengthening `L88 = 1/64`.\n\nThe result is complete for the declared **linear parity-functional class** only. It does not claim complete separation from the nonlinear P75 model image, identify the latent variable with experience, establish nonphysicality, or close the physical-to-experiential bridge.\n\n- [Proof](proposition_89_complete_linear_parity_duality.md)\n- [Equation provenance](p89_equation_provenance.md)\n- Implementation: `src/consciousness_bridge/complete_linear_parity_duality.py`\n- Tests: `tests/test_complete_linear_parity_duality.py`\n- Figure: `docs/figures/p89_complete_linear_parity_duality.svg`\n'''
    write_if_changed(path, text, changed)


def sync_navigation(changed: list[str]) -> None:
    path = DOCS / "research_navigation.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current documented theorem frontier is **P88**.", "The current documented theorem frontier is **P89**."),
            ("**Results:** P75 through P88", "**Results:** P75 through P89"),
            ("P74 through P88", "P74 through P89"),
            ("P71 through P88", "P71 through P89"),
            ("the full 88 proposition index", "the full 89 proposition index"),
        ),
    )
    current_pattern = re.compile(r"\*\*Current frontier:\*\* \[P88:[^\]]+\]\([^\)]+\)")
    text = current_pattern.sub(
        "**Current frontier:** [P89: Complete Linear Parity Functional Duality Certificate](proposition_89_complete_linear_parity_duality.md)",
        text,
        count=1,
    )
    audit_pattern = re.compile(r"For P88:\n\n\| Audit surface \| Canonical route \|\n\| --- \| --- \|\n.*?(?=\n\n|\Z)", re.DOTALL)
    audit = '''For P89:\n\n| Audit surface | Canonical route |\n| --- | --- |\n| Direct theorem | [P89 proposition](proposition_89_complete_linear_parity_duality.md) |\n| Equation and method provenance | [P89 provenance](p89_equation_provenance.md) |\n| Implementation | [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py) |\n| Regression tests | [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py) |\n| Theorem figure | [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg) |'''
    text, count = audit_pattern.subn(audit, text, count=1)
    if count == 0 and "For P89:" not in text:
        raise RuntimeError("research navigation P88 audit block was not found")
    text = text.replace(
        "P88 is a conditional model separation result for the declared P75 target-measurement family. It does not identify the latent state with consciousness, establish nonphysicality, or close the final bridge from physical description to experience.",
        "P89 is a conditional model-separation result for the declared P75 target-measurement family. It closes the declared real linear parity-functional class only; it does not identify the latent state with consciousness, establish nonphysicality, exhaust nonlinear model constraints, or close the final bridge from physical description to experience.",
    )
    write_if_changed(path, text, changed)


def sync_reproducibility(changed: list[str]) -> None:
    path = DOCS / "reproducibility.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current public theorem frontier is **P88**.", "The current public theorem frontier is **P89**."),
            ("| Run only the current P88 theorem checks | focused P88 commands below |", "| Run only the current P89 theorem checks | focused P89 commands below |"),
        ),
    )
    section = r'''## 5. Focused audit of the current P89 frontier

The current theorem frontier is **P89**.

Its direct technical record is:

```text
docs/proposition_89_complete_linear_parity_duality.md
docs/p89_equation_provenance.md
src/consciousness_bridge/complete_linear_parity_duality.py
tests/test_complete_linear_parity_duality.py
docs/figures/p89_complete_linear_parity_duality.svg
figures/manifest.json
```

Run the focused theorem and figure-publication checks with:

```bash
python -m pytest \
  tests/test_complete_linear_parity_duality.py \
  tests/test_figure_publication_sync.py \
  tests/test_p89_reader_surface_coherence.py
```

P89 considers every real linear functional of the eleven canonical P83 parity coordinates. On the published strict witness, the exact functional coefficient vector is

```text
(0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)
```

with empirical value `-13/6`, exact P75 interval `[-51/8,-3]`, interval gap `5/6`, centering constant `-3`, and centered transfer norm `28`. The normalized lower certificate is therefore

\[
\frac5{168}.
\]

A matching rational convex-vertex plus zero-mass perturbation certificate has exact infinity radius `5/168`. The equality of the lower and upper certificates proves that `5/168` is the exact optimum over the complete real linear parity-functional class on the stated box. Thus

\[
L_{88}=\frac1{64}<L_{89}=\frac5{168}.
\]

This completeness statement is limited to the declared linear parity-functional class. It does not exhaust nonlinear P75 constraints or close the physical-to-experiential bridge.
'''
    pattern = re.compile(r"## 5\. Focused audit of the current P88 frontier\n.*?\n---\n\n## 6\.", re.DOTALL)
    if pattern.search(text):
        text = pattern.sub(section + "\n---\n\n## 6.", text, count=1)
    elif "## 5. Focused audit of the current P89 frontier" not in text:
        raise RuntimeError("reproducibility P88 focused section was not found")
    write_if_changed(path, text, changed)


def sync_research_map(changed: list[str]) -> None:
    path = DOCS / "research_map.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The public theorem frontier is **P88**", "The public theorem frontier is **P89**"),
            ("P75-P88", "P75-P89"),
            ("P71-P88", "P71-P89"),
            ("P1-P88", "P1-P89"),
        ),
    )
    if "P89 closes the complete real linear parity-functional class" not in text:
        text += "\n\n### P89 complete linear parity-functional closure\n\nP89 closes the complete real linear parity-functional class on the eleven canonical P83 parity coordinates for a fixed rational P75 parameter box. Matching exact rational lower and upper certificates give `L89 = 5/168` on the published strict witness, strictly above `L88 = 1/64`. Nonlinear model constraints and the physical-to-experiential bridge remain open.\n"
    write_if_changed(path, text, changed)


def sync_catalogs(changed: list[str]) -> None:
    figure_catalog = DOCS / "figure_catalog.md"
    text = read(figure_catalog)
    if "p89_complete_linear_parity_duality.svg" not in text:
        row = "| [P89 Complete Linear Parity-Functional Duality Certificate](figures/p89_complete_linear_parity_duality.svg) | What this figure shows: Proposition 89 removes the finite coefficient-radius and four-observable support restrictions of P88 and closes the complete real linear-functional class on all eleven canonical parity coordinates. How to read it: follow the three panels from unrestricted coefficient space, through matching lower/upper dual certificates, to the exact witness `1/64 < 5/168`. Main takeaway: matching rational certificates prove the exact complete-linear optimum on the stated P75 box. | Conditional exact model-separation theorem; complete for the declared linear parity-functional class only. | [Proposition 89](proposition_89_complete_linear_parity_duality.md) |\n"
        text += "\n" + row
    write_if_changed(figure_catalog, text, changed)

    equation_map = DOCS / "equation_and_citation_map.md"
    if equation_map.is_file():
        text = read(equation_map)
        if "p89_equation_provenance.md" not in text:
            text += "\n\n## P89 complete linear parity-functional duality\n\n- Theorem: [Proposition 89](proposition_89_complete_linear_parity_duality.md)\n- Equation provenance: [P89 equation record](p89_equation_provenance.md)\n- Implementation: [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py)\n- Tests: [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py)\n- Figure: [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg)\n"
        write_if_changed(equation_map, text, changed)

    claim_matrix = DOCS / "claim_source_matrix.md"
    if claim_matrix.is_file():
        text = read(claim_matrix).replace("P75-P88", "P75-P89")
        if "| P89 complete linear parity duality |" not in text:
            text += "\n| P89 complete linear parity duality | Every real linear functional of the eleven canonical parity coordinates is bounded by the finite P89 primal/dual certificate; the strict witness optimum is exactly 5/168 | repository theorem | [P89 proof](proposition_89_complete_linear_parity_duality.md), [P89 provenance](p89_equation_provenance.md), implementation/tests, [P89 figure](figures/p89_complete_linear_parity_duality.svg) | Complete only for the declared linear parity-functional class; no consciousness identification or nonphysicality claim |\n"
        write_if_changed(claim_matrix, text, changed)


def sync_glossary(changed: list[str]) -> None:
    path = DOCS / "glossary.md"
    text = read(path)
    text = text.replace("P88", "P89") if "**Theorem frontier**" in text and "P88" in text else text
    write_if_changed(path, text, changed)


def assert_state() -> None:
    roadmap = read(DOCS / "theorem_roadmap.md")
    navigation = read(DOCS / "research_navigation.md")
    reproducibility = read(DOCS / "reproducibility.md")
    detailed = read(DOCS / "detailed_proposition_record.md")
    required = (
        (roadmap, "The current documented theorem frontier is **P89**."),
        (roadmap, r"\text{P89:"),
        (roadmap, "## P89: complete linear parity-functional duality"),
        (roadmap, "## After P89"),
        (navigation, "The current documented theorem frontier is **P89**."),
        (navigation, "**Results:** P75 through P89"),
        (navigation, "For P89:"),
        (reproducibility, "The current public theorem frontier is **P89**."),
        (reproducibility, "## 5. Focused audit of the current P89 frontier"),
        (detailed, "## Proposition 89: Complete Linear Parity-Functional Duality Certificate"),
    )
    for source, marker in required:
        if marker not in source:
            raise RuntimeError(f"missing P89 documentation marker {marker!r}")


def main() -> None:
    changed: list[str] = []
    sync_readme(changed)
    sync_start_here_markdown(changed)
    sync_theorem_roadmap(changed)
    sync_detailed_record(changed)
    sync_navigation(changed)
    sync_reproducibility(changed)
    sync_research_map(changed)
    sync_catalogs(changed)
    sync_glossary(changed)
    assert_state()
    print("[P89 docs] synchronized:", ", ".join(changed) if changed else "already current")


if __name__ == "__main__":
    main()
