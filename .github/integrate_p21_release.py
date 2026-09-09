from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"expected one marker for {label} in {path}, found {count}"
        )
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def require(path: str, token: str, label: str) -> None:
    text = Path(path).read_text(encoding="utf-8")
    if token not in text:
        raise RuntimeError(f"missing post-integration requirement {label} in {path}")


# ---------------------------------------------------------------------------
# README: make the main page expose P21 as part of the paper itself.
# ---------------------------------------------------------------------------
replace_once(
    "README.md",
    "version-0.20.0-2563eb",
    "version-0.21.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P20** converts the P19 stochastic population residual into an explicit finite-sample confidence certificate under a declared finite-alphabet IID model.",
    "**P20** converts the P19 stochastic population residual into an explicit finite-sample confidence certificate under a declared finite-alphabet IID model. **P21** then proves how that residual behaves under nested physical-descriptor refinement: unresolved deterministic collisions can only disappear, while the stochastic residual decreases by exactly the target-relevant information supplied by the added physical detail.",
    "README abstract P21 summary",
)
replace_once(
    "README.md",
    "**20 proposition-level results, 58 equation-driven quantitative figures",
    "**21 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P20 in dependency order",
    "P1 through P21 in dependency order",
    "README navigation theorem range",
)
replace_once(
    "README.md",
    "| implementation of P20 | [finite_sample_residual_certification.py](src/consciousness_bridge/finite_sample_residual_certification.py) | executable finite-sample residual confidence certificate |",
    "| implementation of P20 | [finite_sample_residual_certification.py](src/consciousness_bridge/finite_sample_residual_certification.py) | executable finite-sample residual confidence certificate |\n| implementation of P21 | [descriptor_refinement_residual.py](src/consciousness_bridge/descriptor_refinement_residual.py) | executable omitted-physics refinement and residual-persistence audit |",
    "README P21 implementation navigation",
)
replace_once(
    "README.md",
    "| **4.6 P20 finite-sample residual certification** | What can finite data certify about the P19 population residual? |",
    "| **4.6 P20 finite-sample residual certification** | What can finite data certify about the P19 population residual? |\n| **4.7 P21 descriptor refinement** | Does a residual survive systematic enrichment of the declared physical description? |",
    "README paper map P21 row",
)
replace_once(
    "README.md",
    "| proposition-level results | **20** |",
    "| proposition-level results | **21** |",
    "README research-record proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.20.0** |",
    "| research-software version | **0.21.0** |",
    "README research-software version",
)

p20_end = """[Read Proposition 20](docs/proposition_20_finite_sample_residual_certification.md). The [P20 theorem map](docs/figures/p20_finite_sample_residual_certificate.svg), [implementation](src/consciousness_bridge/finite_sample_residual_certification.py), [tests](tests/test_finite_sample_residual_certification.py), [equation provenance](docs/equation_and_citation_map.md), and [falsification requirements](docs/falsification_program.md) are linked directly.

---

# 5. Probability, distinguishability, and information geometry"""

p21_readme = r"""[Read Proposition 20](docs/proposition_20_finite_sample_residual_certification.md). The [P20 theorem map](docs/figures/p20_finite_sample_residual_certificate.svg), [implementation](src/consciousness_bridge/finite_sample_residual_certification.py), [tests](tests/test_finite_sample_residual_certification.py), [equation provenance](docs/equation_and_citation_map.md), and [falsification requirements](docs/falsification_program.md) are linked directly.

# 4.7 P21 - physical-descriptor refinement and residual persistence

![P21 physical-descriptor refinement and residual persistence](docs/figures/p21_descriptor_refinement_residual_persistence.svg)

P19 asks whether a declared physical descriptor is sufficient, and P20 asks whether a positive residual can be certified from finite data. P21 addresses the next necessary scientific objection: **could the residual simply reflect omitted physical detail?**

Let the fine physical descriptor be a deterministic function of the sampled physical state,

\[
T_f=f(\Omega),
\]

and let the coarse descriptor be obtained from the fine descriptor,

\[
\boxed{T_c=c(T_f).}
\]

For a deterministic target audit, define the unresolved collision set

\[
\mathcal C(T,E)
=
\{(\omega,\omega'):
T(\omega)=T(\omega'),\ E(\omega)\ne E(\omega')\}.
\]

P21 proves

\[
\boxed{
\mathcal C(T_f,E)
\subseteq
\mathcal C(T_c,E).
}
\]

A valid refinement can therefore resolve a collision produced by a coarse description, but it cannot create a new unresolved collision that was absent at the coarse level.

For finite stochastic variables define the descriptor-relative residual

\[
\boxed{R(T):=I(E;\Omega\mid T).}
\]

The conditional-information chain rule gives the exact refinement decomposition

\[
\boxed{
R(T_c)
=
I(E;T_f\mid T_c)
+
R(T_f).
}
\]

Hence

\[
\boxed{R(T_f)\le R(T_c),}
\]

and the decrease is not an unspecified effect:

\[
\boxed{
R(T_c)-R(T_f)
=
I(E;T_f\mid T_c).
}
\]

It is exactly the target-relevant information supplied by the added physical detail.

For a nested descriptor chain

\[
T_0\preceq T_1\preceq\cdots\preceq T_m,
\]

P21 yields

\[
\boxed{
R_0\ge R_1\ge\cdots\ge R_m\ge0
}
\]

and the telescoping identity

\[
\boxed{
R_0-R_m
=
\sum_{k=1}^{m}I(E;T_k\mid T_{k-1}).
}
\]

This turns omitted physics into an explicit audit trajectory. Each refinement must state which physical variables were added, how the nesting relation is established, how much residual was removed, and how much remains.

The interpretation boundary is essential. A positive residual at the finest **declared and measured** level challenges that descriptor; it does not establish that no richer physical description exists. In particular, if the chain reaches the identity descriptor \(T_m=\Omega\), then

\[
\boxed{I(E;\Omega\mid\Omega)=0}
\]

by definition. Conditional screening-off therefore cannot by itself prove that a target lies outside physics. P21 is an omitted-physics control theorem, not an argument for a nonphysical substance or an extra spacetime dimension.

[Read Proposition 21](docs/proposition_21_descriptor_refinement_residual_persistence.md). The [P21 theorem map](docs/figures/p21_descriptor_refinement_residual_persistence.svg), [implementation](src/consciousness_bridge/descriptor_refinement_residual.py), and [tests](tests/test_descriptor_refinement_residual.py) expose the complete proof-to-code audit path.

---

# 5. Probability, distinguishability, and information geometry"""
replace_once(
    "README.md",
    p20_end,
    p21_readme,
    "README P21 theorem section",
)
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P20",
    "# 7. Theorem roadmap - P1 through P21",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P20** | finite-sample confidence interval for the P19 conditional-information residual | proved | [P20](docs/proposition_20_finite_sample_residual_certification.md) |",
    "| **P20** | finite-sample confidence interval for the P19 conditional-information residual | proved | [P20](docs/proposition_20_finite_sample_residual_certification.md) |\n| **P21** | descriptor refinement makes deterministic collisions and stochastic residuals monotone, with exact information-gain decomposition | proved | [P21](docs/proposition_21_descriptor_refinement_residual_persistence.md) |",
    "README P21 proposition table row",
)

# ---------------------------------------------------------------------------
# Theorem-roadmap prose.
# ---------------------------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P20 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P21 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P20](proposition_20_finite_sample_residual_certification.md) | Hoeffding joint-TV concentration plus finite-alphabet entropy continuity | finite-sample confidence interval for the P19 conditional-information residual | proved finite-sample certification theorem |",
    "| [P20](proposition_20_finite_sample_residual_certification.md) | Hoeffding joint-TV concentration plus finite-alphabet entropy continuity | finite-sample confidence interval for the P19 conditional-information residual | proved finite-sample certification theorem |\n| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | nested descriptor factorization and conditional-information chain rule | explicit omitted-physics audit and residual-persistence trajectory | proved descriptor-refinement theorem |",
    "roadmap P21 proposition row",
)

roadmap_marker = """Direct proof: [Proposition 20](proposition_20_finite_sample_residual_certification.md). Implementation: [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py). Tests: [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py).

---

# 10. Dependency chain"""
roadmap_insert = r"""Direct proof: [Proposition 20](proposition_20_finite_sample_residual_certification.md). Implementation: [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py). Tests: [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py).

---

# 10. Descriptor refinement and omitted-physics control: P21

Let \(T_f=f(\Omega)\) refine \(T_c\) through

\[
\boxed{T_c=c(T_f).}
\]

For deterministic target collisions, P21 proves

\[
\boxed{
\mathcal C(T_f,E)
\subseteq
\mathcal C(T_c,E).
}
\]

For the P19 stochastic residual

\[
R(T)=I(E;\Omega\mid T),
\]

the conditional-information chain rule gives

\[
\boxed{
R(T_c)
=
I(E;T_f\mid T_c)
+
R(T_f).
}
\]

Therefore

\[
\boxed{R(T_f)\le R(T_c).}
\]

For a nested chain \(T_0\preceq\cdots\preceq T_m\),

\[
\boxed{
R_0-R_m
=
\sum_{k=1}^{m}I(E;T_k\mid T_{k-1}),
}
\]

so every residual decrease is assigned exactly to target-relevant information added by one physical refinement step. A positive terminal residual remains descriptor relative; it does not establish physical completeness or a nonphysical ontology.

Direct proof: [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md). Implementation: [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py). Tests: [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py).

---

# 11. Dependency chain"""
replace_once(
    "docs/theorem_roadmap.md",
    roadmap_marker,
    roadmap_insert,
    "roadmap P21 theorem section",
)
replace_once(
    "docs/theorem_roadmap.md",
    r"""&\text{P20: finite-sample residual certification}.
\end{aligned}""",
    r"""&\text{P20: finite-sample residual certification}\\
&\Downarrow\\
&\text{P21: physical-descriptor refinement + residual persistence}.
\end{aligned}""",
    "roadmap P21 dependency tail",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 11. Current frontier",
    "# 12. Current frontier",
    "roadmap frontier numbering",
)
replace_once(
    "docs/theorem_roadmap.md",
    "3. sharpen P20 beyond the conservative finite-alphabet IID baseline using structured, multinomial, non-IID, and quantum confidence methods with explicit coverage;",
    "3. derive simultaneous finite-sample confidence accounting across P21 refinement chains, including adaptive refinement and principled stopping rules for physical-completeness audits;",
    "roadmap P21 finite-data frontier",
)

# ---------------------------------------------------------------------------
# Reader navigation.
# ---------------------------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "for the dependency structure from P1 through P20.",
    "for the dependency structure from P1 through P21.",
    "navigation theorem range",
)
old_reading = """5. [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) for the population physical-sufficiency theorem.
6. [Proposition 20](proposition_20_finite_sample_residual_certification.md) for finite-sample certification of the P19 stochastic residual.
7. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
8. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
9. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
10. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
new_reading = """5. [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) for the population physical-sufficiency theorem.
6. [Proposition 20](proposition_20_finite_sample_residual_certification.md) for finite-sample certification of the P19 stochastic residual.
7. [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md) for the omitted-physics refinement audit and residual-persistence theorem.
8. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
9. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
10. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
11. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
replace_once(
    "docs/research_navigation.md",
    old_reading,
    new_reading,
    "navigation P21 reading order",
)
replace_once(
    "docs/research_navigation.md",
    "| P20 | [Finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |",
    "| P20 | [Finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |\n| P21 | [Descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | omitted-physics audit, residual monotonicity, and exact refinement gain |",
    "navigation P21 proposition row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | finite-data confidence certificate for the P19 stochastic residual |",
    "| [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | finite-data confidence certificate for the P19 stochastic residual |\n| [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | nested physical-description audit that quantifies how added physical detail removes or fails to remove the residual |",
    "navigation P21 fundamental interface row",
)
replace_once(
    "docs/research_navigation.md",
    "The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg). The P20 finite-sample layer is implemented in [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py), tested in [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py), and summarized by [p20_finite_sample_residual_certificate.svg](figures/p20_finite_sample_residual_certificate.svg).",
    "The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg). The P20 finite-sample layer is implemented in [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py), tested in [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py), and summarized by [p20_finite_sample_residual_certificate.svg](figures/p20_finite_sample_residual_certificate.svg). The P21 omitted-physics audit is implemented in [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py), tested in [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py), and summarized by [p21_descriptor_refinement_residual_persistence.svg](figures/p21_descriptor_refinement_residual_persistence.svg).",
    "navigation P21 implementation paragraph",
)

# ---------------------------------------------------------------------------
# Equation provenance.
# ---------------------------------------------------------------------------
p21_provenance = r"""# 15. P21 - physical-descriptor refinement and residual persistence

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(T_c=c\circ T_f\) with \(T_f=f(\Omega)\) | declares a nested deterministic physical-description relation | repository modeling assumption using standard function composition | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(\mathcal C(T_f,E)\subseteq\mathcal C(T_c,E)\) | deterministic target-collision monotonicity under valid refinement | proved | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T)=I(E;\Omega\mid T)\) | descriptor-relative stochastic residual inherited from P19 | repository diagnostic built from standard conditional mutual information | [P19](proposition_19_fundamental_physical_sufficiency.md); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T_c)=I(E;T_f\mid T_c)+R(T_f)\) | exact decomposition of the coarse residual into refinement capture plus remaining residual | proved from the conditional-mutual-information chain rule and deterministic nesting | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T_f)\le R(T_c)\) | residual monotonicity under valid physical refinement | proved | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R_0-R_m=\sum_{k=1}^{m}I(E;T_k\mid T_{k-1})\) | exact telescoping accounting for a nested descriptor chain | proved by repeated P21 decomposition | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(I(E;\Omega\mid\Omega)=0\) | identity-descriptor boundary preventing ontological overinterpretation of screening-off residuals | standard conditional-information identity used here as an interpretation guard | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |

P21 formalizes an omitted-physics control. Persistence of a residual through a finite declared refinement chain is evidence only relative to that chain. Physical completeness requires an independent scientific argument; the conditional-information residual cannot supply that argument by itself.

---

# 16. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    "# 15. Candidate consciousness-theory feature families",
    p21_provenance,
    "equation map P21 provenance",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 16. Citation discipline",
    "# 17. Citation discipline",
    "equation map citation section number",
)

# ---------------------------------------------------------------------------
# Machine guards for the public paper.
# ---------------------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p20_finite_sample_residual_certificate.svg",',
    '    "p20_finite_sample_residual_certificate.svg",\n    "p21_descriptor_refinement_residual_persistence.svg",',
    "main-page P21 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 21):",
    "for index in range(1, 22):",
    "main-page P21 proposition guard",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 21):",
    "for number in range(1, 22):",
    "navigation P21 theorem-chain guard",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p20_finite_sample_residual_certificate.svg",',
    '    "p20_finite_sample_residual_certificate.svg",\n    "p21_descriptor_refinement_residual_persistence.svg",',
    "canonical P21 figure guard",
)

# Fix the one roadmap line that exceeded the publication line-length guard.
replace_once(
    "docs/figures/theorem_roadmap.svg",
    "The proof chain separates representation, recovery, causal structure, time, composition, scale, sufficiency, finite data, and physical-refinement controls.",
    "The chain separates representation, recovery, causal structure, time, composition, scale, sufficiency, finite data, and refinement controls.",
    "roadmap subtitle length",
)

# ---------------------------------------------------------------------------
# Release metadata.
# ---------------------------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.20.0"',
    'version = "0.21.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "fundamental physical-sufficiency and residual tests, finite-sample residual certification, recoverability, and falsifiable experiment design.",
    "fundamental physical-sufficiency and residual tests, finite-sample residual certification, descriptor-refinement residual-persistence audits, recoverability, and falsifiable experiment design.",
    "pyproject P21 description",
)
replace_once(
    "CITATION.cff",
    "version: 0.20.0",
    "version: 0.21.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "fundamental physical-sufficiency factorization and residual tests, finite-sample residual certification, robust experiment design",
    "fundamental physical-sufficiency factorization and residual tests, finite-sample residual certification, descriptor-refinement residual-persistence audits, robust experiment design",
    "citation P21 abstract",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.20.0"',
    '__version__ = "0.21.0"',
    "runtime version",
)

changelog_marker = """## 0.20.0 - 2026-09-09"""
changelog_release = r"""## 0.21.0 - 2026-09-09

### Proposition 21 - physical-descriptor refinement and residual persistence

- Formalized nested deterministic physical descriptors through \(T_c=c\circ T_f\) with \(T_f=f(\Omega)\).
- Proved deterministic collision monotonicity \(\mathcal C(T_f,E)\subseteq\mathcal C(T_c,E)\), so valid physical refinement can remove unresolved target collisions but cannot create new ones.
- Defined the descriptor-relative stochastic residual \(R(T)=I(E;\Omega\mid T)\).
- Proved the exact refinement identity \(R(T_c)=I(E;T_f\mid T_c)+R(T_f)\) and therefore \(R(T_f)\le R(T_c)\).
- Extended the result to nested refinement chains with exact telescoping \(R_0-R_m=\sum_k I(E;T_k\mid T_{k-1})\).
- Added executable refinement validation, collision audits, pairwise residual decomposition, nested residual trajectories, and twelve regression tests.
- Added a publication-style P21 theorem map and extended the public theorem roadmap through P21.
- Added the identity-descriptor boundary \(I(E;\Omega\mid\Omega)=0\) as an explicit guard against treating conditional screening-off as a proof of nonphysical ontology.
- Integrated P21 into the README paper, reader navigation, equation provenance, visual guards, theorem-chain guards, changelog, and release metadata.

## 0.20.0 - 2026-09-09"""
replace_once(
    "CHANGELOG.md",
    changelog_marker,
    changelog_release,
    "P21 changelog release",
)

# ---------------------------------------------------------------------------
# Final assertions before CI is allowed to validate the release state.
# ---------------------------------------------------------------------------
requirements = (
    ("README.md", "# 4.7 P21 - physical-descriptor refinement and residual persistence", "README P21 section"),
    ("README.md", "# 7. Theorem roadmap - P1 through P21", "README P1-P21 heading"),
    ("README.md", "p21_descriptor_refinement_residual_persistence.svg", "README P21 figure"),
    ("docs/theorem_roadmap.md", "# 10. Descriptor refinement and omitted-physics control: P21", "roadmap P21 section"),
    ("docs/research_navigation.md", "proposition_21_descriptor_refinement_residual_persistence.md", "navigation P21 link"),
    ("docs/equation_and_citation_map.md", "# 15. P21 - physical-descriptor refinement and residual persistence", "P21 provenance section"),
    ("pyproject.toml", 'version = "0.21.0"', "pyproject release version"),
    ("CITATION.cff", "version: 0.21.0", "citation release version"),
    ("src/consciousness_bridge/__init__.py", '__version__ = "0.21.0"', "runtime release version"),
)
for path, token, label in requirements:
    require(path, token, label)

print("P21 release integration markers verified.")
