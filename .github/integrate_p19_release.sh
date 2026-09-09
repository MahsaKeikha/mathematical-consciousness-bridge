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

reader_nav = r'''# Reader navigation

A reader should not need to search the repository to understand the argument. The [Research Navigation](docs/research_navigation.md) page provides the complete reading order and direct links to every proposition. The most important paths are also available here:

| What you want to inspect | Direct link | What is there |
| --- | --- | --- |
| complete theorem chain | [Theorem Roadmap](docs/theorem_roadmap.md) | P1 through P19 in dependency order |
| equation provenance | [Equation and Citation Map](docs/equation_and_citation_map.md) | standard results, repository definitions, proofs, and external sources separated explicitly |
| current frontier theorem | [Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md) | deterministic factorization, stochastic sufficiency, and local rank obstruction |
| fundamental-theory program | [Fundamental Theory to Consciousness](docs/fundamental_theory_consciousness_program.md) | candidate fundamental state, physical quotients, experiential quotient, and falsifiable bridge program |
| stochastic extension | [Stochastic Fundamental Bridge](docs/stochastic_fundamental_bridge.md) | Markov-kernel and conditional-information formulation |
| empirical falsification | [Falsification Program](docs/falsification_program.md) | conditions that would weaken or defeat a bridge claim |
| source standards | [Citation and Reference Policy](docs/citation_and_reference_policy.md) | citation, DOI, attribution, evidence-class, and prose rules |
| high-impact source audit | [Reference Audit](docs/reference_audit.md) | publication metadata and evidential role of major sources |
| quantitative physics | [Quantitative Physics and Mathematics Atlas](docs/quantitative_physics_mathematics_atlas.md) | Q01 through Q40 with equations and reproducible figures |
| implementation of P19 | [fundamental_physical_sufficiency.py](src/consciousness_bridge/fundamental_physical_sufficiency.py) | executable factorization and conditional-information utilities |

Every local documentation and figure link is checked by automated tests. Broken internal links therefore fail CI instead of remaining silently in the public research record.

---

'''
text = replace_once(text, "# Paper map", reader_nav + "# Paper map", "README reader navigation")
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
    "| automated tests | **120+ and expanding** |",
    "| automated tests | **150+ and expanding** |",
    "README test count",
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

The interpretation is deliberately conservative. A residual first challenges the completeness of the declared physical descriptor. Measurement error, omitted physical variables, system boundaries, timescale, and intervention coverage must be tested before introducing a new primitive.

[Read Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md). See the [Equation and Citation Map](docs/equation_and_citation_map.md) for the provenance of each mathematical ingredient and the [Falsification Program](docs/falsification_program.md) for the empirical burden.

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

A positive rank residual is therefore a sufficient local no-factorization certificate. Neither a positive information residual nor a positive rank residual establishes a nonphysical ontology. Both first challenge the completeness of the declared physical descriptor.

Direct proof: [Proposition 19](proposition_19_fundamental_physical_sufficiency.md). Provenance: [Equation and Citation Map](equation_and_citation_map.md). Empirical burden: [Falsification Program](falsification_program.md).

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

# Extend the equation-level provenance map through P19.
eq_path = Path("docs/equation_and_citation_map.md")
eq_text = eq_path.read_text(encoding="utf-8")
new_sections = r'''# 11. P17 - coarse-graining and refinement

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C:\Omega_f\to\Omega_c\) | deterministic coarse-graining map | repository modeling definition | P17 |
| \(C_\#P(y)=\sum_{x:C(x)=y}P(x)\) | pushforward of a fine response law | standard pushforward construction applied here | P17; standard probability |
| \(\|C_\#P-C_\#Q\|_{\mathrm{TV}}\le\|P-Q\|_{\mathrm{TV}}\) | data-processing contraction under deterministic coarse-graining | proved for the declared response laws | P17; standard TV contraction principle |
| fine-scale collision with identical coarse pushforwards | exact refinement non-recoverability witness | repository counterexample | P17 |
| bijective reparameterization preserves TV exactly | representation-preserving special case | proved | P17 |

P17 is a physical information-loss theorem. It does not identify a privileged biological scale and does not attach an experiential interpretation to coarse-graining.

---

# 12. P18 - scale sufficiency by approximate reconstruction

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D=R_\#C_\#\) | reconstruction operator induced by a coarse map and declared decoder | repository construction using standard pushforwards | P18 |
| \(\rho(P)=\|P-R_\#C_\#P\|_{\mathrm{TV}}\) | response-law reconstruction defect | repository definition | P18 |
| \(\rho_{\mathcal F}=\sup_{P\in\mathcal F}\rho(P)\) | uniform family reconstruction defect | repository definition | P18 |
| \(0\le d_f-d_c\le\rho(P)+\rho(Q)\le2\rho_{\mathcal F}\) | pairwise response-geometry distortion certificate | proved | P18 |
| \(\delta_c\ge\delta_f-2\rho_{\mathcal F}\) | finite-family separation guarantee | proved | P18 |
| \(\rho_{\mathcal F}=0\Rightarrow d_c=d_f\) on the declared family | exact family scale sufficiency | proved | P18 |

The pushforward, total variation, and triangle inequality are standard mathematics. The reconstruction-defect certificate and its role as a scale-sufficiency criterion are repository results.

---

# 13. P19 - fundamental physical sufficiency and residual tests

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(T:\mathcal M\to\mathcal Q_T\) | declared physical descriptor on a candidate fundamental state space | repository abstraction | P19 |
| \(E:\mathcal M\to\mathcal Q_E\) | independently defined target descriptor | repository abstraction; experiential instantiation remains open | P19 |
| \(E=B_T\circ T\) iff \(E\) is constant on every fiber of \(T\) | exact deterministic physical-sufficiency criterion | proved | P19; standard quotient and factorization logic |
| \(T(\Omega)=T(\Omega')\) and \(E(\Omega)\ne E(\Omega')\) | exact no-factorization witness relative to the declared \(T\) | proved | P19 |
| \(E\perp\!\!\!\perp\Omega\mid T\) | stochastic physical-sufficiency condition | standard conditional-independence form applied here | P19; Cover and Thomas 2006 |
| \(I(E;\Omega\mid T)=0\) | finite-alphabet information criterion equivalent to conditional independence | standard information-theoretic identity applied here | Cover and Thomas 2006; P19 |
| \(I(E;\Omega\mid T)=H(E\mid T)\) for deterministic \(E=E(\Omega)\) | deterministic-target corollary | proved from standard entropy identities | P19; Cover and Thomas 2006 |
| \(\operatorname{rank}D(T,E)=\operatorname{rank}DT\) under local smooth factorization | necessary differential condition | proved by the chain rule | P19; standard differential calculus |
| \(d_\perp=\operatorname{rank}D(T,E)-\operatorname{rank}DT>0\) | sufficient local no-factorization witness | proved | P19 |

P19 is a theorem about sufficiency relative to a declared physical descriptor. A residual first indicates that the declared descriptor may be incomplete. It is not by itself evidence for a nonphysical substance, a new spacetime dimension, or a failure of quantum mechanics.

---

'''
eq_text = replace_once(
    eq_text,
    "# 11. Candidate consciousness-theory feature families",
    new_sections + "# 14. Candidate consciousness-theory feature families",
    "equation map P17-P19 insertion",
)
eq_text = replace_once(
    eq_text,
    "# 12. Citation discipline",
    "# 15. Citation discipline",
    "equation map citation section number",
)
eq_path.write_text(eq_text, encoding="utf-8")

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

- Proved the exact factorization criterion \(E=B_T\circ T\) if and only if the target is constant on every fiber of the declared physical descriptor.
- Added exact collision witnesses that rule out deterministic factorization through an incomplete descriptor.
- Proved the finite stochastic equivalence between physical screening-off and \(I(E;\Omega\mid T)=0\).
- Added the deterministic-target corollary \(I(E;\Omega\mid T)=H(E\mid T)\).
- Added a differential no-go criterion based on \(\operatorname{rank}D(T,E)-\operatorname{rank}DT\).
- Added executable factorization and conditional-information utilities with regression tests.
- Added a P19 theorem map and synchronized the public P1-P19 dependency map.
- Added a complete reader-navigation index and automated internal-link integrity checks.
- Extended the equation and citation map through P19 so standard mathematics, repository results, and interpretation boundaries remain explicit.

'''
chtext = replace_once(chtext, "## 0.18.0 - 2026-09-09", entry + "## 0.18.0 - 2026-09-09", "changelog insertion")
changelog.write_text(chtext, encoding="utf-8")

main_test = Path("tests/test_main_page_visual_paper.py")
mtext = main_test.read_text(encoding="utf-8")
mtext = replace_once(mtext, "range(1, 19)", "range(1, 20)", "P19 main-page guard")
mtext = replace_once(
    mtext,
    '    "p18_scale_sufficiency_certificate.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p18_scale_sufficiency_certificate.svg",\n    "p19_fundamental_physical_sufficiency.svg",\n    "observer_to_bridge_handoff.svg",',
    "P19 main-page figure guard",
)
main_test.write_text(mtext, encoding="utf-8")

visual_test = Path("tests/test_visual_and_terminology_quality.py")
vtext = visual_test.read_text(encoding="utf-8")
vtext = replace_once(
    vtext,
    '    "p18_scale_sufficiency_certificate.svg",\n    "universal_proof_ladder.svg",',
    '    "p18_scale_sufficiency_certificate.svg",\n    "p19_fundamental_physical_sufficiency.svg",\n    "universal_proof_ladder.svg",',
    "P19 visual guard",
)
visual_test.write_text(vtext, encoding="utf-8")

policy = Path("docs/citation_and_reference_policy.md")
policy_text = policy.read_text(encoding="utf-8")
policy_text = replace_once(
    policy_text,
    "8. The wording of a source's scientific role must not exceed what the cited source establishes.",
    "8. The wording of a source's scientific role must not exceed what the cited source establishes.\n"
    "9. Local theorem, figure, code, and documentation links are checked automatically in CI so the public research path remains navigable.",
    "citation policy link integrity",
)
policy_text = replace_once(
    policy_text,
    "## Reference layers",
    "## Reference layers\n\n- [Research Navigation](research_navigation.md): complete reading order and direct theorem, evidence, figure, and implementation paths.",
    "citation policy navigation",
)
policy.write_text(policy_text, encoding="utf-8")
PY