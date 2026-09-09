#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing integration marker: {label}")
    return text.replace(old, new, 1)


readme_path = Path("README.md")
text = readme_path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.18.0", "version-0.19.0", "README badge")
text = replace_once(
    text,
    "**P18** proves a quantitative scale-sufficiency certificate based on approximate reconstruction.",
    "**P18** proves a quantitative scale-sufficiency certificate based on approximate reconstruction. "
    "**P19** proves exact deterministic and stochastic criteria for whether an independently defined "
    "target factors through a declared physical descriptor, together with a differential no-go test.",
    "README abstract P18 sentence",
)
text = replace_once(
    text,
    "The public research record now contains **18 proposition-level results,",
    "The public research record now contains **19 proposition-level results,",
    "README research record prose",
)
text = replace_once(
    text,
    "| **4.4 Fundamental-theory interface** | Can spacetime, quantum, causal, and experiential structure be tested as quotients of one candidate fundamental state? |",
    "| **4.4 Fundamental-theory interface** | Can spacetime, quantum, causal, and experiential structure be tested as quotients of one candidate fundamental state? |\n"
    "| **4.5 P19 physical sufficiency** | Does an independently defined target factor through the declared physical descriptor? |",
    "README paper map",
)
text = replace_once(
    text,
    "| proposition-level results | **18** |",
    "| proposition-level results | **19** |",
    "README proposition count",
)
text = replace_once(
    text,
    "| research-software version | **0.18.0** |",
    "| research-software version | **0.19.0** |",
    "README software version",
)
text = replace_once(
    text,
    "# 7. Theorem roadmap - P1 through P18",
    "# 7. Theorem roadmap - P1 through P19",
    "README theorem heading",
)
p18_row = (
    "| **P18** | approximate reconstruction gives a quantitative scale-sufficiency certificate | "
    "proved | [P18](docs/proposition_18_scale_sufficiency_certification.md) |"
)
p19_row = (
    "| **P19** | exact physical-sufficiency factorization, conditional-information residual, and "
    "differential no-go criterion | proved | "
    "[P19](docs/proposition_19_fundamental_physical_sufficiency.md) |"
)
text = replace_once(text, p18_row, p18_row + "\n" + p19_row, "README P19 theorem row")

p19_section = r'''# 4.5 P19 - fundamental physical sufficiency and residual tests

![P19 fundamental physical sufficiency](docs/figures/p19_fundamental_physical_sufficiency.svg)

P19 turns the fundamental-theory interface into an exact theorem. Let

\[
T:\mathcal M\to\mathcal Q_T
\]

be the declared physical descriptor and let

\[
E:\mathcal M\to\mathcal Q_E
\]

be an independently defined target descriptor. There exists a unique bridge on the physical image,

\[
\boxed{E=B_T\circ T,}
\]

if and only if the target is constant on every physical fiber:

\[
\boxed{
T(\Omega)=T(\Omega')
\Longrightarrow
E(\Omega)=E(\Omega').
}
\]

Thus a single exact collision

\[
\boxed{
T(\Omega)=T(\Omega')
\quad\text{but}\quad
E(\Omega)\ne E(\Omega')
}
\]

rules out every deterministic bridge through that declared physical descriptor.

The stochastic extension replaces deterministic factorization by conditional independence,

\[
\boxed{E\perp\!\!\!\perp\Omega\mid T.}
\]

For finite alphabets this is equivalent to

\[
\boxed{
\mathcal I_{\perp}^{\mathrm{fund}}
:=I(E;\Omega\mid T)=0.
}
\]

For smooth local coordinates, any differentiable factorization requires

\[
\boxed{
\operatorname{rank}D(T,E)=\operatorname{rank}DT.
}
\]

Therefore

\[
\boxed{
d_{\perp}
:=\operatorname{rank}D(T,E)-\operatorname{rank}DT>0
}
\]

is a sufficient local no-factorization certificate.

The interpretation is deliberately conservative: a residual first challenges the completeness of the declared physical descriptor. Measurement error, omitted physical variables, system boundaries, timescale, and intervention coverage must be tested before introducing a new primitive.

[Read Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md).

---

'''
marker = "# 5. Probability, distinguishability, and information geometry"
text = replace_once(text, marker, p19_section + marker, "README P19 section insertion")
readme_path.write_text(text, encoding="utf-8")

roadmap_path = Path("docs/theorem_roadmap.md")
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = replace_once(
    roadmap,
    "![P1-P18 theorem roadmap]",
    "![P1-P19 theorem roadmap]",
    "roadmap figure alt text",
)
p18_doc_row = (
    "| [P18](proposition_18_scale_sufficiency_certification.md) | approximate reconstruction and "
    "separation margin | certifies when a coarse scale preserves a declared response family | "
    "proved scale-sufficiency theorem |"
)
p19_doc_row = (
    "| [P19](proposition_19_fundamental_physical_sufficiency.md) | quotient factorization, conditional "
    "mutual information, and differential rank obstruction | tests whether an independent target is "
    "fixed by the declared physical descriptor | proved physical-sufficiency theorem |"
)
roadmap = replace_once(
    roadmap,
    p18_doc_row,
    p18_doc_row + "\n" + p19_doc_row,
    "roadmap P19 row",
)
p19_doc_section = r'''# 8. Fundamental physical sufficiency: P19

P19 asks whether an independently defined target descriptor \(E\) is already fixed by the declared physical descriptor \(T\).

The deterministic criterion is

\[
\boxed{
E=B_T\circ T
\iff
T(\Omega)=T(\Omega')\Rightarrow E(\Omega)=E(\Omega').
}
\]

For finite stochastic variables, physical sufficiency is equivalent to

\[
\boxed{
I(E;\Omega\mid T)=0.
}
\]

For differentiable local coordinates, any smooth factorization requires

\[
\boxed{
\operatorname{rank}D(T,E)=\operatorname{rank}DT.
}
\]

A positive rank residual is therefore a sufficient local no-factorization certificate. Neither a positive information residual nor a positive rank residual establishes a nonphysical ontology; both first challenge the completeness of the declared physical descriptor.

---

'''
roadmap = replace_once(
    roadmap,
    "# 8. Dependency chain",
    p19_doc_section + "# 9. Dependency chain",
    "roadmap P19 section",
)
roadmap = replace_once(roadmap, "# 9. Current frontier", "# 10. Current frontier", "roadmap frontier")
roadmap_path.write_text(roadmap, encoding="utf-8")

pyproject = Path("pyproject.toml")
ptext = pyproject.read_text(encoding="utf-8")
ptext = replace_once(ptext, 'version = "0.18.0"', 'version = "0.19.0"', "pyproject version")
ptext = replace_once(
    ptext,
    "scale-sufficiency certification, recoverability, and falsifiable experiment design",
    "scale-sufficiency certification, fundamental physical-sufficiency and residual tests, "
    "recoverability, and falsifiable experiment design",
    "pyproject description",
)
pyproject.write_text(ptext, encoding="utf-8")

citation = Path("CITATION.cff")
ctext = citation.read_text(encoding="utf-8")
ctext = replace_once(ctext, "version: 0.18.0", "version: 0.19.0", "citation version")
ctext = replace_once(
    ctext,
    "quantitative scale-sufficiency certification by approximate reconstruction, robust experiment design",
    "quantitative scale-sufficiency certification by approximate reconstruction, fundamental "
    "physical-sufficiency factorization and residual tests, robust experiment design",
    "citation abstract",
)
citation.write_text(ctext, encoding="utf-8")

changelog = Path("CHANGELOG.md")
chtext = changelog.read_text(encoding="utf-8")
entry = r'''## 0.19.0 - 2026-09-09

### Proposition 19 - fundamental physical sufficiency and residual tests

- Proved the exact factorization criterion \(E=B_T\circ T\) iff the target is constant on every fiber of the declared physical descriptor.
- Added exact collision witnesses that rule out deterministic factorization through an incomplete descriptor.
- Proved the finite stochastic equivalence between physical screening-off and \(I(E;\Omega\mid T)=0\).
- Added the deterministic-target corollary \(I(E;\Omega\mid T)=H(E\mid T)\).
- Added a differential no-go criterion based on \(\operatorname{rank}D(T,E)-\operatorname{rank}DT\).
- Added executable factorization and conditional-information utilities with regression tests.
- Added a P19 theorem map and rebuilt the roadmap as a compact P1-P19 dependency map.
- Reduced the quantitative visual scale and rebuilt the state-space map for main-page readability.

'''
chtext = replace_once(chtext, "## 0.18.0 - 2026-09-09", entry + "## 0.18.0 - 2026-09-09", "changelog insertion")
changelog.write_text(chtext, encoding="utf-8")

main_test = Path("tests/test_main_page_visual_paper.py")
mtext = main_test.read_text(encoding="utf-8")
mtext = replace_once(mtext, "range(1, 19)", "range(1, 20)", "P19 main-page guard")
main_test.write_text(mtext, encoding="utf-8")

visual_test = Path("tests/test_visual_and_terminology_quality.py")
vtext = visual_test.read_text(encoding="utf-8")
vtext = replace_once(
    vtext,
    '    "p18_scale_sufficiency_certificate.svg",',
    '    "p18_scale_sufficiency_certificate.svg",\n    "p19_fundamental_physical_sufficiency.svg",',
    "P19 visual guard",
)
visual_test.write_text(vtext, encoding="utf-8")
PY
