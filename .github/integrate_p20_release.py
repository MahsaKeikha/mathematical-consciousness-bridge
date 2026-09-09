from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"missing integration marker for {label} in {path}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def append_after(path: str, marker: str, addition: str, label: str) -> None:
    replace_once(path, marker, marker + addition, label)


# README release state and reader navigation.
replace_once(
    "README.md",
    "version-0.19.0-2563eb",
    "version-0.20.0-2563eb",
    "README version badge",
)
append_after(
    "README.md",
    "**P19** proves exact deterministic and stochastic criteria for whether an independently defined target factors through a declared physical descriptor, together with a differential no-go test.",
    " **P20** converts the P19 stochastic population residual into an explicit finite-sample confidence certificate under a declared finite-alphabet IID model.",
    "README abstract P20",
)
replace_once(
    "README.md",
    "**19 proposition-level results, 58 equation-driven quantitative figures",
    "**20 proposition-level results, 58 equation-driven quantitative figures",
    "README research-record sentence",
)
replace_once(
    "README.md",
    "| complete theorem chain | [Theorem Roadmap](docs/theorem_roadmap.md) | P1 through P19 in dependency order |",
    "| complete theorem chain | [Theorem Roadmap](docs/theorem_roadmap.md) | P1 through P20 in dependency order |",
    "README theorem navigation",
)
replace_once(
    "README.md",
    "| current frontier theorem | [Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md) | deterministic factorization, stochastic sufficiency, and local rank obstruction |",
    "| population physical-sufficiency theorem | [Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md) | deterministic factorization, stochastic sufficiency, and local rank obstruction |\n| finite-sample residual theorem | [Proposition 20](docs/proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |",
    "README P19-P20 navigation",
)
replace_once(
    "README.md",
    "| implementation of P19 | [fundamental_physical_sufficiency.py](src/consciousness_bridge/fundamental_physical_sufficiency.py) | executable factorization and conditional-information utilities |",
    "| implementation of P19 | [fundamental_physical_sufficiency.py](src/consciousness_bridge/fundamental_physical_sufficiency.py) | executable factorization and population conditional-information utilities |\n| implementation of P20 | [finite_sample_residual_certification.py](src/consciousness_bridge/finite_sample_residual_certification.py) | executable finite-sample residual confidence certificate |",
    "README implementation navigation",
)
append_after(
    "README.md",
    "| **4.5 P19 physical sufficiency** | Does an independently defined target factor through the declared physical descriptor? |",
    "\n| **4.6 P20 finite-sample residual certification** | What can finite data certify about the P19 population residual? |",
    "README paper map P20",
)
replace_once(
    "README.md",
    "| proposition-level results | **19** |",
    "| proposition-level results | **20** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| automated tests | **150+ and expanding** |",
    "| automated tests | **160+ and expanding** |",
    "README test count",
)
replace_once(
    "README.md",
    "| research-software version | **0.19.0** |",
    "| research-software version | **0.20.0** |",
    "README release version",
)
p19_end = """[Read Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md). See the [Equation and Citation Map](docs/equation_and_citation_map.md) for the provenance of each mathematical ingredient and the [Falsification Program](docs/falsification_program.md) for the empirical burden.

---

# 5. Probability, distinguishability, and information geometry
"""
p20_readme = """[Read Proposition 19](docs/proposition_19_fundamental_physical_sufficiency.md). See the [Equation and Citation Map](docs/equation_and_citation_map.md) for the provenance of each mathematical ingredient and the [Falsification Program](docs/falsification_program.md) for the empirical burden.

# 4.6 P20 - finite-sample residual certification

![P20 finite-sample residual certification](docs/figures/p20_finite_sample_residual_certificate.svg)

P19 states a population criterion. P20 asks what finite data can certify. Let

\\[
Z_i=(\\Omega_i,T_i,E_i),\\qquad i=1,\\ldots,n,
\\]

be IID samples on declared finite alphabets of sizes \\(d_\\Omega,d_T,d_E\\), and let

\\[
M=d_\\Omega d_T d_E.
\\]

A simultaneous Hoeffding and union-bound argument gives the conservative joint-distribution radius

\\[
\\boxed{
\\tau_n(\\alpha)
=
\\min\\left\\{
1,
\\frac{M}{2}
\\sqrt{\\frac{1}{2n}\\log\\frac{2M}{\\alpha}}
\\right\\}.
}
\\]

Finite-alphabet entropy continuity then propagates this distributional uncertainty to conditional mutual information. If \\(\\widehat I_n\\) is the empirical residual, P20 proves

\\[
\\boxed{
\\left|
I_P(E;\\Omega\\mid T)-\\widehat I_n
\\right|
\\le
\\Delta_{\\mathrm{CMI}}\\bigl(\\tau_n(\\alpha)\\bigr)
}
\\]

with probability at least \\(1-\\alpha\\). Therefore

\\[
\\boxed{
L_n
=
\\max\\left\\{0,
\\widehat I_n-\\Delta_{\\mathrm{CMI}}(\\tau_n)
\\right\\}
}
\\]

is a valid lower confidence bound, and

\\[
\\boxed{
L_n>0
\\Longrightarrow
I_P(E;\\Omega\\mid T)>0
}
\\]

at confidence at least \\(1-\\alpha\\), under the stated model.

For the synthetic binary checkpoint with \\(n=10{,}000\\), \\(\\alpha=0.05\\), and \\(\\widehat I_n=\\log 2\\), the conservative lower bound is approximately

\\[
\\boxed{L_n\\approx0.234702\\text{ nats}.}
\\]

This is a mathematical calibration, not an empirical consciousness result. A certified positive residual first means that the declared physical descriptor \\(T\\) fails to screen off the declared target \\(E\\) under the sampling assumptions. Omitted physics, measurement error, preprocessing, system boundaries, timescale, and sampling dependence remain alternative explanations that must be tested.

[Read Proposition 20](docs/proposition_20_finite_sample_residual_certification.md). The [P20 theorem map](docs/figures/p20_finite_sample_residual_certificate.svg), [implementation](src/consciousness_bridge/finite_sample_residual_certification.py), [tests](tests/test_finite_sample_residual_certification.py), [equation provenance](docs/equation_and_citation_map.md), and [falsification requirements](docs/falsification_program.md) are linked directly.

---

# 5. Probability, distinguishability, and information geometry
"""
replace_once("README.md", p19_end, p20_readme, "README P20 theorem section")
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P19",
    "# 7. Theorem roadmap - P1 through P20",
    "README roadmap heading",
)
append_after(
    "README.md",
    "| **P19** | exact physical-sufficiency factorization, conditional-information residual, and differential no-go criterion | proved | [P19](docs/proposition_19_fundamental_physical_sufficiency.md) |",
    "\n| **P20** | finite-sample confidence interval for the P19 conditional-information residual | proved | [P20](docs/proposition_20_finite_sample_residual_certification.md) |",
    "README proposition table P20",
)
replace_once(
    "README.md",
    "the P1-P18 proposition chain",
    "the P1-P20 proposition chain",
    "README reproducibility chain",
)
replace_once(
    "README.md",
    "scale sufficiency, quantum normalization",
    "scale sufficiency, fundamental residual certification, quantum normalization",
    "README audit scope",
)
replace_once(
    "README.md",
    "7. **Finite-sample quantum certification.** Derive confidence regions for experimentally reconstructed states/channels and propagate them through the bridge tests.",
    "7. **Finite-sample certification beyond the P20 baseline.** Develop sharper multinomial, structured, non-IID, and quantum confidence methods while preserving explicit coverage guarantees.",
    "README frontier P20",
)
replace_once(
    "README.md",
    "\\text{quantum-completeness test}\n\\longrightarrow\n\\text{bridge or non-reducibility test}.",
    "\\text{quantum-completeness test}\n\\longrightarrow\n\\text{finite-sample residual certification}\n\\longrightarrow\n\\text{bridge or non-reducibility test}.",
    "README final chain",
)
replace_once(
    "README.md",
    "| Follow P1-P18 in proof order | **[Theorem Roadmap](docs/theorem_roadmap.md)** |",
    "| Follow P1-P20 in proof order | **[Theorem Roadmap](docs/theorem_roadmap.md)** |",
    "README start-here roadmap",
)
append_after(
    "README.md",
    "| Read the scale-sufficiency theorem | **[P18 - Scale Sufficiency](docs/proposition_18_scale_sufficiency_certification.md)** |",
    "\n| Read the population physical-sufficiency theorem | **[P19 - Fundamental Physical Sufficiency](docs/proposition_19_fundamental_physical_sufficiency.md)** |\n| Read the finite-sample residual theorem | **[P20 - Finite-Sample Residual Certification](docs/proposition_20_finite_sample_residual_certification.md)** |",
    "README start-here P19-P20",
)

# Theorem roadmap: add P20 and its dependency role.
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P19 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P20 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
append_after(
    "docs/theorem_roadmap.md",
    "| [P19](proposition_19_fundamental_physical_sufficiency.md) | quotient factorization, conditional mutual information, and differential rank obstruction | tests whether an independent target is fixed by the declared physical descriptor | proved physical-sufficiency theorem |",
    "\n| [P20](proposition_20_finite_sample_residual_certification.md) | Hoeffding joint-TV concentration plus finite-alphabet entropy continuity | finite-sample confidence interval for the P19 conditional-information residual | proved finite-sample certification theorem |",
    "roadmap P20 row",
)
roadmap_marker = """Direct proof: [Proposition 19](proposition_19_fundamental_physical_sufficiency.md). Provenance: [Equation and Citation Map](equation_and_citation_map.md). Empirical burden: [Falsification Program](falsification_program.md).

---

# 9. Dependency chain
"""
roadmap_insert = """Direct proof: [Proposition 19](proposition_19_fundamental_physical_sufficiency.md). Provenance: [Equation and Citation Map](equation_and_citation_map.md). Empirical burden: [Falsification Program](falsification_program.md).

---

# 9. Finite-sample residual certification: P20

P20 converts the P19 population condition into a finite-data statement. For IID categorical samples on a declared joint alphabet of size

\\[
M=d_\\Omega d_T d_E,
\\]

it defines the conservative total-variation radius

\\[
\\boxed{
\\tau_n(\\alpha)
=
\\min\\left\\{1,
\\frac M2\\sqrt{\\frac1{2n}\\log\\frac{2M}{\\alpha}}
\\right\\}.
}
\\]

Finite-alphabet entropy continuity gives a deterministic function \\(\\Delta_{\\mathrm{CMI}}\\) such that, with probability at least \\(1-\\alpha\\),

\\[
\\boxed{
|I_P(E;\\Omega\\mid T)-\\widehat I_n|
\\le
\\Delta_{\\mathrm{CMI}}(\\tau_n(\\alpha)).
}
\\]

Thus the lower bound

\\[
L_n=\\max\\{0,\\widehat I_n-\\Delta_{\\mathrm{CMI}}(\\tau_n)\\}
\\]

satisfies

\\[
\\boxed{L_n>0\\Longrightarrow I_P(E;\\Omega\\mid T)>0}
\\]

with the declared confidence. This certifies failure of screening-off by the declared \\(T\\), not a nonphysical ontology.

Direct proof: [Proposition 20](proposition_20_finite_sample_residual_certification.md). Implementation: [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py). Tests: [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py).

---

# 10. Dependency chain
"""
replace_once(
    "docs/theorem_roadmap.md",
    roadmap_marker,
    roadmap_insert,
    "roadmap P20 section",
)
replace_once(
    "docs/theorem_roadmap.md",
    "&\\text{P17-P18: scale loss + scale sufficiency}.\\n\\end{aligned}",
    "&\\text{P17-P18: scale loss + scale sufficiency}\\\\\n&\\Downarrow\\\\\n&\\text{P19: population physical sufficiency}\\\\\n&\\Downarrow\\\\\n&\\text{P20: finite-sample residual certification}.\\n\\end{aligned}",
    "roadmap dependency chain",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 10. Current frontier",
    "# 11. Current frontier",
    "roadmap frontier number",
)
replace_once(
    "docs/theorem_roadmap.md",
    "3. derive estimator-specific finite-sample confidence bounds for \\(\\rho_{\\mathcal F}\\), \\(\\delta_f\\), and the P18 scale margin;",
    "3. sharpen P20 beyond the conservative finite-alphabet IID baseline using structured, multinomial, non-IID, and quantum confidence methods with explicit coverage;",
    "roadmap frontier finite sample",
)

# Reader navigation.
replace_once(
    "docs/research_navigation.md",
    "from P1 through P19.",
    "from P1 through P20.",
    "navigation theorem range",
)
replace_once(
    "docs/research_navigation.md",
    "5. [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) for the current fundamental physical-sufficiency theorem.\n6. [Fundamental Theory to Consciousness program]",
    "5. [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) for the population physical-sufficiency theorem.\n6. [Proposition 20](proposition_20_finite_sample_residual_certification.md) for finite-sample certification of the P19 stochastic residual.\n7. [Fundamental Theory to Consciousness program]",
    "navigation recommended P20",
)
replace_once(
    "docs/research_navigation.md",
    "7. [Stochastic fundamental bridge]",
    "8. [Stochastic fundamental bridge]",
    "navigation numbering 8",
)
replace_once(
    "docs/research_navigation.md",
    "8. [Falsification program]",
    "9. [Falsification program]",
    "navigation numbering 9",
)
replace_once(
    "docs/research_navigation.md",
    "9. [Citation and Reference Policy]",
    "10. [Citation and Reference Policy]",
    "navigation numbering 10",
)
append_after(
    "docs/research_navigation.md",
    "| P19 | [Fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md) | deterministic, stochastic, and differential sufficiency tests |",
    "\n| P20 | [Finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |",
    "navigation P20 row",
)
append_after(
    "docs/research_navigation.md",
    "| [P19 fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md) | exact factorization theorem, stochastic criterion, and local rank obstruction |",
    "\n| [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | finite-data confidence certificate for the P19 stochastic residual |",
    "navigation fundamental P20",
)
replace_once(
    "docs/research_navigation.md",
    "The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg).",
    "The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg). The P20 finite-sample layer is implemented in [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py), tested in [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py), and summarized by [p20_finite_sample_residual_certificate.svg](figures/p20_finite_sample_residual_certificate.svg).",
    "navigation implementation P20",
)

# Equation-level provenance through P20.
eq_marker = """P19 is a theorem about sufficiency relative to a declared physical descriptor. A residual first indicates that the declared descriptor may be incomplete. It is not by itself evidence for a nonphysical substance, a new spacetime dimension, or a failure of quantum mechanics.

---

# 14. Candidate consciousness-theory feature families
"""
eq_p20 = """P19 is a theorem about sufficiency relative to a declared physical descriptor. A residual first indicates that the declared descriptor may be incomplete. It is not by itself evidence for a nonphysical substance, a new spacetime dimension, or a failure of quantum mechanics.

---

# 14. P20 - finite-sample residual certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \\(M=d_\\Omega d_T d_E\\) | declared joint alphabet size | repository sampling-model definition | [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(a_n(\\alpha)=\\sqrt{\\frac1{2n}\\log\\frac{2M}{\\alpha}}\\) | simultaneous cell-frequency radius | standard Hoeffding inequality plus union bound applied here | [Hoeffding 1963](https://doi.org/10.1080/01621459.1963.10500830); [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(\\tau_n(\\alpha)=\\min\\{1,\\frac M2 a_n(\\alpha)\\}\\) | conservative joint total-variation confidence radius | proved from the simultaneous cell bounds | [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(c_d(r)\\) | uniform finite-alphabet entropy-continuity radius for a known TV upper bound | standard finite-alphabet entropy reasoning applied and proved here | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(\\Delta_{\\mathrm{CMI}}(r)\\) | propagates joint-distribution TV error through the four entropy terms of conditional mutual information | repository finite-sample construction | [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(|I_P-\\widehat I_n|\\le\\Delta_{\\mathrm{CMI}}(\\tau_n(\\alpha))\\) | finite-sample population-residual confidence bound | proved under the declared finite-alphabet IID model | [P20](proposition_20_finite_sample_residual_certification.md) |
| \\(L_n>0\\Rightarrow I_P(E;\\Omega\\mid T)>0\\) at confidence \\(1-\\alpha\\) | certified rejection of P19 stochastic screening-off for the declared descriptor | proved finite-sample decision rule | [P20](proposition_20_finite_sample_residual_certification.md) |

P20 is deliberately conservative. A positive lower confidence bound certifies insufficiency of the declared descriptor under the sampling model. It does not identify the residual as nonphysical and does not remove the need to test omitted physical variables, measurement error, system boundaries, timescale, preprocessing, and sampling assumptions.

---

# 15. Candidate consciousness-theory feature families
"""
replace_once(
    "docs/equation_and_citation_map.md",
    eq_marker,
    eq_p20,
    "equation map P20 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 15. Citation discipline",
    "# 16. Citation discipline",
    "equation map citation section number",
)

# Release metadata.
changelog_marker = """This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.19.0 - 2026-09-09
"""
changelog_p20 = """This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.20.0 - 2026-09-09

### Proposition 20 - finite-sample residual certification

- Converted the P19 population condition \\(I(E;\\Omega\\mid T)=0\\) into an explicit finite-sample confidence certificate for declared finite-alphabet IID data.
- Derived a simultaneous joint-distribution total-variation radius from cellwise Hoeffding concentration and a union bound.
- Added a finite-alphabet entropy-continuity lemma that remains valid when only an upper TV radius is known.
- Propagated the joint-distribution confidence radius through the entropy representation of conditional mutual information.
- Proved a confidence interval \\([L_n,U_n]\\) for the population residual and the decision rule \\(L_n>0\\Rightarrow I_P(E;\\Omega\\mid T)>0\\) at confidence at least \\(1-\\alpha\\).
- Added a synthetic binary numerical checkpoint, executable implementation, claim-level regression tests, and a publication-style P20 theorem map.
- Extended the README, theorem roadmap, reader navigation, equation provenance, release metadata, and link-integrity guards through P20.
- Preserved the interpretation boundary that a certified residual first challenges the completeness of the declared physical descriptor and sampling model.

## 0.19.0 - 2026-09-09
"""
replace_once("CHANGELOG.md", changelog_marker, changelog_p20, "P20 changelog")
replace_once("pyproject.toml", 'version = "0.19.0"', 'version = "0.20.0"', "package version")
replace_once(
    "pyproject.toml",
    "fundamental physical-sufficiency and residual tests, recoverability",
    "fundamental physical-sufficiency and residual tests, finite-sample residual certification, recoverability",
    "package description",
)
replace_once("CITATION.cff", "version: 0.19.0", "version: 0.20.0", "citation version")
replace_once(
    "CITATION.cff",
    "fundamental physical-sufficiency factorization and residual tests, robust experiment design",
    "fundamental physical-sufficiency factorization and residual tests, finite-sample residual certification, robust experiment design",
    "citation abstract",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.17.0"',
    '__version__ = "0.20.0"',
    "runtime package version",
)

# Machine-enforced P1-P20 public-document consistency.
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p19_fundamental_physical_sufficiency.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p19_fundamental_physical_sufficiency.svg",\n    "p20_finite_sample_residual_certificate.svg",\n    "observer_to_bridge_handoff.svg",',
    "main-page P20 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 20):\n        assert f\"**P{index}**\" in text",
    "for index in range(1, 21):\n        assert f\"**P{index}**\" in text",
    "main-page P20 proposition guard",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 20):\n        assert f\"proposition_{number}_\" in nav",
    "for number in range(1, 21):\n        assert f\"proposition_{number}_\" in nav",
    "navigation P20 guard",
)

# Critical release assertions: fail rather than silently publish an inconsistent state.
readme = Path("README.md").read_text(encoding="utf-8")
roadmap = Path("docs/theorem_roadmap.md").read_text(encoding="utf-8")
nav = Path("docs/research_navigation.md").read_text(encoding="utf-8")
for token in (
    "version-0.20.0",
    "**20 proposition-level results",
    "# 4.6 P20 - finite-sample residual certification",
    "docs/proposition_20_finite_sample_residual_certification.md",
    "p20_finite_sample_residual_certificate.svg",
):
    if token not in readme:
        raise RuntimeError(f"README integration assertion failed: {token}")
if "P1 through P20" not in roadmap or "proposition_20_" not in nav:
    raise RuntimeError("P20 roadmap/navigation integration assertion failed")
