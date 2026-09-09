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
    if token not in Path(path).read_text(encoding="utf-8"):
        raise RuntimeError(f"missing post-integration requirement {label} in {path}")


# ---------------------------------------------------------------------------
# README: expose P22 directly in the public research paper.
# ---------------------------------------------------------------------------
replace_once(
    "README.md",
    "version-0.21.0-2563eb",
    "version-0.22.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P21** then proves how that residual behaves under nested physical-descriptor refinement: unresolved deterministic collisions can only disappear, while the stochastic residual decreases by exactly the target-relevant information supplied by the added physical detail.",
    "**P21** then proves how that residual behaves under nested physical-descriptor refinement: unresolved deterministic collisions can only disappear, while the stochastic residual decreases by exactly the target-relevant information supplied by the added physical detail. **P22** gives a simultaneous finite-sample certificate for the entire declared refinement chain from one shared confidence event on the empirical physical-target law.",
    "README abstract P22 summary",
)
replace_once(
    "README.md",
    "**21 proposition-level results, 58 equation-driven quantitative figures",
    "**22 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P21 in dependency order",
    "P1 through P22 in dependency order",
    "README theorem navigation range",
)
replace_once(
    "README.md",
    "| finite-sample residual theorem | [Proposition 20](docs/proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |",
    "| finite-sample residual theorem | [Proposition 20](docs/proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |\n| physical-refinement theorem | [Proposition 21](docs/proposition_21_descriptor_refinement_residual_persistence.md) | omitted-physics residual trajectory and exact refinement gain |\n| simultaneous refinement-chain theorem | [Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md) | one confidence event controlling the full residual-and-gain trajectory |",
    "README P21-P22 theorem navigation",
)
replace_once(
    "README.md",
    "| implementation of P21 | [descriptor_refinement_residual.py](src/consciousness_bridge/descriptor_refinement_residual.py) | executable omitted-physics refinement and residual-persistence audit |",
    "| implementation of P21 | [descriptor_refinement_residual.py](src/consciousness_bridge/descriptor_refinement_residual.py) | executable omitted-physics refinement and residual-persistence audit |\n| implementation of P22 | [refinement_chain_certification.py](src/consciousness_bridge/refinement_chain_certification.py) | simultaneous finite-sample refinement-chain confidence certificate |",
    "README P22 implementation navigation",
)
replace_once(
    "README.md",
    "| **4.7 P21 descriptor refinement** | Does a residual survive systematic enrichment of the declared physical description? |",
    "| **4.7 P21 descriptor refinement** | Does a residual survive systematic enrichment of the declared physical description? |\n| **4.8 P22 simultaneous refinement certification** | Can one finite data set certify the full declared residual-and-gain trajectory at once? |",
    "README P22 paper-map row",
)
replace_once(
    "README.md",
    "| proposition-level results | **21** |",
    "| proposition-level results | **22** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.21.0** |",
    "| research-software version | **0.22.0** |",
    "README software version",
)

p21_end = """[Read Proposition 21](docs/proposition_21_descriptor_refinement_residual_persistence.md). The [P21 theorem map](docs/figures/p21_descriptor_refinement_residual_persistence.svg), [implementation](src/consciousness_bridge/descriptor_refinement_residual.py), and [tests](tests/test_descriptor_refinement_residual.py) expose the complete proof-to-code audit path.

---

# 5. Probability, distinguishability, and information geometry"""

p22_readme = r"""[Read Proposition 21](docs/proposition_21_descriptor_refinement_residual_persistence.md). The [P21 theorem map](docs/figures/p21_descriptor_refinement_residual_persistence.svg), [implementation](src/consciousness_bridge/descriptor_refinement_residual.py), and [tests](tests/test_descriptor_refinement_residual.py) expose the complete proof-to-code audit path.

# 4.8 P22 - simultaneous finite-sample refinement-chain certification

![P22 simultaneous refinement-chain certification](docs/figures/p22_simultaneous_refinement_chain_certification.svg)

P21 gives the exact population trajectory of a nested physical-descriptor audit. P22 asks whether the **entire trajectory** can be certified from one finite data set without treating every descriptor level as a separately sampled statistical experiment.

Let

\[
Z=(\Omega,E)
\]

have a finite declared alphabet, and suppose

\[
Z_1,\ldots,Z_n\overset{\mathrm{IID}}{\sim}P_{\Omega E}.
\]

For predeclared deterministic nested descriptors

\[
T_k=f_k(\Omega),
\qquad
T_{k-1}=c_k(T_k),
\]

P22 first certifies one base event

\[
\boxed{
\mathcal A_n
=
\left\{
\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\right\}
}
\]

with

\[
\Pr(\mathcal A_n)\ge1-\alpha.
\]

Every level-specific residual law is a deterministic pushforward of \(P_{\Omega E}\):

\[
\phi_k(\omega,e)
=
(\omega,T_k(\omega),e).
\]

Every refinement-gain law is also a deterministic pushforward:

\[
\psi_k(\omega,e)
=
(T_k(\omega),T_{k-1}(\omega),e).
\]

Total-variation contraction therefore transfers the **same** base confidence event to every residual and every gain distribution in the chain.

For

\[
R_k=I(E;\Omega\mid T_k),
\]

P22 obtains simultaneous intervals satisfying

\[
\boxed{
|R_k-\widehat R_k|
\le
\Delta_k(\tau_n(\alpha))
\qquad
\forall k.
}
\]

For the P21 refinement gains

\[
G_k=I(E;T_k\mid T_{k-1}),
\]

it likewise obtains

\[
\boxed{
|G_k-\widehat G_k|
\le
\Gamma_k(\tau_n(\alpha))
\qquad
\forall k.
}
\]

P21 also gives

\[
G_k=R_{k-1}-R_k,
\qquad
\widehat G_k=\widehat R_{k-1}-\widehat R_k,
\]

so P22 intersects the direct gain interval with the difference-based interval implied by the residual bounds.

The main simultaneous statement is

\[
\boxed{
\Pr\left(
R_k\in\mathcal I_k^R\ \forall k,
\quad
G_k\in\mathcal I_k^G\ \forall k
\right)
\ge1-\alpha.
}
\]

This construction does **not** replace \(\alpha\) by \(\alpha/(2m+1)\). There is one probabilistic event for the shared base law, and all level-specific bounds follow deterministically from that event. This is different from running independently calibrated confidence procedures at each level.

The absence of a level-count penalty does not make long chains statistically free. The base radius depends on the declared physical-target alphabet \(d_\Omega d_E\), and the entropy-continuity radii depend on the descriptor alphabet sizes. High-dimensional alphabets can make the finite-data certificate numerically weak.

If the terminal lower bound satisfies

\[
\boxed{L_m^R>0,}
\]

then residual persistence at the finest tested descriptor is certified with simultaneous confidence at least \(1-\alpha\) under the declared finite-alphabet IID model. The conclusion remains descriptor relative. P22 does not establish physical completeness, nonphysical ontology, or an additional spacetime dimension, and the P21 identity boundary

\[
I(E;\Omega\mid\Omega)=0
\]

remains unchanged.

[Read Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md). The [P22 theorem map](docs/figures/p22_simultaneous_refinement_chain_certification.svg), [implementation](src/consciousness_bridge/refinement_chain_certification.py), and [tests](tests/test_refinement_chain_certification.py) expose the full proof-to-code path.

---

# 5. Probability, distinguishability, and information geometry"""
replace_once(
    "README.md",
    p21_end,
    p22_readme,
    "README P22 theorem section",
)
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P21",
    "# 7. Theorem roadmap - P1 through P22",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P21** | descriptor refinement makes deterministic collisions and stochastic residuals monotone, with exact information-gain decomposition | proved | [P21](docs/proposition_21_descriptor_refinement_residual_persistence.md) |",
    "| **P21** | descriptor refinement makes deterministic collisions and stochastic residuals monotone, with exact information-gain decomposition | proved | [P21](docs/proposition_21_descriptor_refinement_residual_persistence.md) |\n| **P22** | one base confidence event simultaneously certifies the declared residual-and-refinement-gain chain | proved finite-sample theorem | [P22](docs/proposition_22_simultaneous_refinement_chain_certification.md) |",
    "README P22 theorem table row",
)

# ---------------------------------------------------------------------------
# Theorem-roadmap prose.
# ---------------------------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P21 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P22 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | nested descriptor factorization and conditional-information chain rule | explicit omitted-physics audit and residual-persistence trajectory | proved descriptor-refinement theorem |",
    "| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | nested descriptor factorization and conditional-information chain rule | explicit omitted-physics audit and residual-persistence trajectory | proved descriptor-refinement theorem |\n| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared base-TV confidence event plus deterministic pushforward contraction | simultaneous finite-data confidence family for P21 residuals and gains | proved simultaneous-certification theorem |",
    "roadmap P22 proposition row",
)

roadmap_marker = """Direct proof: [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md). Implementation: [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py). Tests: [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py).

---

# 11. Dependency chain"""
roadmap_insert = r"""Direct proof: [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md). Implementation: [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py). Tests: [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py).

---

# 11. Simultaneous finite-sample refinement certification: P22

Let the finite-alphabet IID base law be \(P_{\Omega E}\), and let every descriptor \(T_k=f_k(\Omega)\) be predeclared and nested.

P22 constructs one base event

\[
\boxed{
\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
}
\]

with probability at least \(1-\alpha\). Because every residual and gain law is a deterministic pushforward of this base law, the same event implies

\[
\boxed{
|R_k-\widehat R_k|
\le
\Delta_k(\tau_n)
\qquad
\forall k
}
\]

and

\[
\boxed{
|G_k-\widehat G_k|
\le
\Gamma_k(\tau_n)
\qquad
\forall k.
}
\]

Using the P21 identity \(G_k=R_{k-1}-R_k\), P22 also intersects each direct gain interval with the difference interval implied by adjacent residual bounds.

Therefore

\[
\boxed{
\Pr\left(
R_k\in\mathcal I_k^R\ \forall k,
\quad
G_k\in\mathcal I_k^G\ \forall k
\right)
\ge1-\alpha.
}
\]

No additional confidence split over the number of descriptor levels is required for this shared-base-event construction. The bound can nevertheless become weak as the declared physical-target and descriptor alphabets grow.

Direct proof: [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md). Implementation: [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py). Tests: [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py).

---

# 12. Dependency chain"""
replace_once(
    "docs/theorem_roadmap.md",
    roadmap_marker,
    roadmap_insert,
    "roadmap P22 theorem section",
)
replace_once(
    "docs/theorem_roadmap.md",
    r"""&\text{P21: physical-descriptor refinement + residual persistence}.
\end{aligned}""",
    r"""&\text{P21: physical-descriptor refinement + residual persistence}\\
&\Downarrow\\
&\text{P22: simultaneous finite-sample refinement certification}.
\end{aligned}""",
    "roadmap dependency tail",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 12. Current frontier",
    "# 13. Current frontier",
    "roadmap frontier numbering",
)
replace_once(
    "docs/theorem_roadmap.md",
    "3. derive simultaneous finite-sample confidence accounting across P21 refinement chains, including adaptive refinement and principled stopping rules for physical-completeness audits;",
    "3. extend P22 beyond fixed finite-alphabet IID chains to continuous, dependent, hidden-state, noisy-descriptor, and adaptive-refinement settings with valid coverage;",
    "roadmap post-P22 frontier",
)

# ---------------------------------------------------------------------------
# Reader navigation.
# ---------------------------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "for the dependency structure from P1 through P21.",
    "for the dependency structure from P1 through P22.",
    "navigation theorem range",
)
old_reading = """7. [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md) for the omitted-physics refinement audit and residual-persistence theorem.
8. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
9. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
10. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
11. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
new_reading = """7. [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md) for the omitted-physics refinement audit and residual-persistence theorem.
8. [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md) for simultaneous finite-data certification of the full P21 refinement trajectory.
9. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
10. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
11. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
12. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
replace_once(
    "docs/research_navigation.md",
    old_reading,
    new_reading,
    "navigation P22 reading order",
)
replace_once(
    "docs/research_navigation.md",
    "| P21 | [Descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | omitted-physics audit, residual monotonicity, and exact refinement gain |",
    "| P21 | [Descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | omitted-physics audit, residual monotonicity, and exact refinement gain |\n| P22 | [Simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | one shared finite-sample confidence event for all P21 residuals and gains |",
    "navigation P22 proposition row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | nested physical-description audit that quantifies how added physical detail removes or fails to remove the residual |",
    "| [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | nested physical-description audit that quantifies how added physical detail removes or fails to remove the residual |\n| [P22 simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | simultaneous finite-sample confidence family for the full declared refinement trajectory |",
    "navigation P22 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "The P21 omitted-physics audit is implemented in [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py), tested in [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py), and summarized by [p21_descriptor_refinement_residual_persistence.svg](figures/p21_descriptor_refinement_residual_persistence.svg).",
    "The P21 omitted-physics audit is implemented in [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py), tested in [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py), and summarized by [p21_descriptor_refinement_residual_persistence.svg](figures/p21_descriptor_refinement_residual_persistence.svg). The P22 simultaneous finite-data layer is implemented in [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py), tested in [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py), and summarized by [p22_simultaneous_refinement_chain_certification.svg](figures/p22_simultaneous_refinement_chain_certification.svg).",
    "navigation P22 implementation paragraph",
)

# ---------------------------------------------------------------------------
# Equation and citation provenance.
# ---------------------------------------------------------------------------
p22_provenance = r"""# 16. P22 - simultaneous finite-sample refinement-chain certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(M=d_\Omega d_E\) | alphabet size of the common sampled base law \((\Omega,E)\) | repository sampling-model definition | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}\le\tau_n(\alpha)\) | one finite-sample confidence event shared by the whole descriptor chain | Hoeffding plus union bound applied to the base categorical law | [Hoeffding 1963](https://doi.org/10.1080/01621459.1963.10500830); [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(P_k=(\phi_k)_\#P_{\Omega E}\) and \(Q_k=(\psi_k)_\#P_{\Omega E}\) | expresses residual and gain distributions as deterministic pushforwards of one base law | repository construction using standard pushforward probability | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\|P_k-\widehat P_k\|_{\mathrm{TV}}\le\tau_n\) and \(\|Q_k-\widehat Q_k\|_{\mathrm{TV}}\le\tau_n\) for all \(k\) | transfers one base confidence event to every level by TV contraction | standard data-processing property applied here | [P17](proposition_17_coarse_graining_and_refinement.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(|R_k-\widehat R_k|\le\Delta_k(\tau_n)\) simultaneously for all \(k\) | finite-sample confidence family for the P21 residual trajectory | proved from shared TV event plus P20 continuity | [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(|G_k-\widehat G_k|\le\Gamma_k(\tau_n)\) simultaneously for all \(k\) | finite-sample confidence family for target information captured by each refinement | proved from the same shared event | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(G_k=R_{k-1}-R_k\) and \(\widehat G_k=\widehat R_{k-1}-\widehat R_k\) | population and empirical chain-rule identity used to sharpen gain intervals | proved in P21 and inherited by P22 | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\Pr(R_k\in\mathcal I_k^R\ \forall k,\ G_k\in\mathcal I_k^G\ \forall k)\ge1-\alpha\) | simultaneous residual-and-gain coverage | proved | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| no \(\alpha/(2m+1)\) replacement is required | one base-TV event deterministically implies every level-specific bound in this construction | theorem consequence, not a generic multiple-testing exemption | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |

P22 is a finite-data theorem for a fixed declared deterministic refinement chain. It does not justify post hoc adaptive descriptor selection using the same confidence statement, and it does not establish physical completeness.

---

# 17. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    "# 16. Candidate consciousness-theory feature families",
    p22_provenance,
    "equation map P22 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 17. Citation discipline",
    "# 18. Citation discipline",
    "equation map citation numbering",
)

# ---------------------------------------------------------------------------
# Public paper and visual guards.
# ---------------------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p21_descriptor_refinement_residual_persistence.svg",',
    '    "p21_descriptor_refinement_residual_persistence.svg",\n    "p22_simultaneous_refinement_chain_certification.svg",',
    "main-page P22 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 22):",
    "for index in range(1, 23):",
    "main-page P22 proposition guard",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 22):",
    "for number in range(1, 23):",
    "navigation P22 theorem guard",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p21_descriptor_refinement_residual_persistence.svg",',
    '    "p21_descriptor_refinement_residual_persistence.svg",\n    "p22_simultaneous_refinement_chain_certification.svg",',
    "canonical P22 figure guard",
)

# ---------------------------------------------------------------------------
# Release metadata.
# ---------------------------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.21.0"',
    'version = "0.22.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "descriptor-refinement residual-persistence audits, recoverability",
    "descriptor-refinement residual-persistence audits, simultaneous refinement-chain certification, recoverability",
    "pyproject P22 description",
)
replace_once(
    "CITATION.cff",
    "version: 0.21.0",
    "version: 0.22.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "descriptor-refinement residual-persistence audits, robust experiment design",
    "descriptor-refinement residual-persistence audits, simultaneous refinement-chain certification, robust experiment design",
    "citation P22 abstract",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.21.0"',
    '__version__ = "0.22.0"',
    "runtime version",
)

changelog_release = r"""## 0.22.0 - 2026-09-09

### Proposition 22 - simultaneous finite-sample certification of physical-refinement chains

- Rebased P20 finite-sample concentration on one declared base law \((\Omega,E)\) for a fixed nested physical-descriptor chain.
- Proved that deterministic pushforward contraction transfers one base total-variation confidence event to every residual law and every refinement-gain law simultaneously.
- Derived simultaneous confidence intervals for the complete P21 residual trajectory \(R_k=I(E;\Omega\mid T_k)\).
- Derived simultaneous confidence intervals for every refinement gain \(G_k=I(E;T_k\mid T_{k-1})\).
- Used the P21 identity \(G_k=R_{k-1}-R_k\) to intersect direct and difference-based gain certificates without weakening coverage.
- Proved joint coverage \(\Pr(R_k\in\mathcal I_k^R\ \forall k,\ G_k\in\mathcal I_k^G\ \forall k)\ge1-\alpha\).
- Established that this shared-base-event construction requires no separate \(\alpha/(2m+1)\) confidence split over descriptor levels, while preserving the alphabet-size limitations of the conservative finite-alphabet bound.
- Added executable simultaneous chain certification and twelve regression tests.
- Added a publication-style P22 theorem map and extended the global theorem roadmap through P22.
- Integrated P22 into the README paper, reader navigation, equation provenance, release metadata, proposition guards, and figure-quality guards.

## 0.21.0 - 2026-09-09"""
replace_once(
    "CHANGELOG.md",
    "## 0.21.0 - 2026-09-09",
    changelog_release,
    "P22 changelog release",
)

# ---------------------------------------------------------------------------
# Final fail-fast release assertions.
# ---------------------------------------------------------------------------
requirements = (
    ("README.md", "# 4.8 P22 - simultaneous finite-sample refinement-chain certification", "README P22 section"),
    ("README.md", "# 7. Theorem roadmap - P1 through P22", "README P1-P22 heading"),
    ("README.md", "p22_simultaneous_refinement_chain_certification.svg", "README P22 figure"),
    ("docs/theorem_roadmap.md", "# 11. Simultaneous finite-sample refinement certification: P22", "roadmap P22 section"),
    ("docs/figures/theorem_roadmap.svg", "Theorem Roadmap - P1 through P22", "visual roadmap P22"),
    ("docs/research_navigation.md", "proposition_22_simultaneous_refinement_chain_certification.md", "navigation P22 link"),
    ("docs/equation_and_citation_map.md", "# 16. P22 - simultaneous finite-sample refinement-chain certification", "P22 provenance"),
    ("pyproject.toml", 'version = "0.22.0"', "pyproject P22 version"),
    ("CITATION.cff", "version: 0.22.0", "citation P22 version"),
    ("src/consciousness_bridge/__init__.py", '__version__ = "0.22.0"', "runtime P22 version"),
)
for path, token, label in requirements:
    require(path, token, label)

print("P22 release integration markers verified.")
