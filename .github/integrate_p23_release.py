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
# README: expose P23 in the public research paper.
# ---------------------------------------------------------------------------
replace_once(
    "README.md",
    "version-0.22.0-2563eb",
    "version-0.23.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P22** gives a simultaneous finite-sample certificate for the entire declared refinement chain from one shared confidence event on the empirical physical-target law.",
    "**P22** gives a simultaneous finite-sample certificate for the entire declared refinement chain from one shared confidence event on the empirical physical-target law. **P23** proves that the same shared base confidence event also supports fixed-sample data-dependent selection among admissible deterministic refinements, together with an explicit near-optimality bound for the selected refinement.",
    "README abstract P23 summary",
)
replace_once(
    "README.md",
    "**22 proposition-level results, 58 equation-driven quantitative figures",
    "**23 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P22 in dependency order",
    "P1 through P23 in dependency order",
    "README theorem navigation range",
)
replace_once(
    "README.md",
    "| simultaneous refinement-chain theorem | [Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md) | one confidence event controlling the full residual-and-gain trajectory |",
    "| simultaneous refinement-chain theorem | [Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md) | one confidence event controlling the full residual-and-gain trajectory |\n| adaptive refinement-selection theorem | [Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and refinement-regret control |",
    "README P23 theorem navigation",
)
replace_once(
    "README.md",
    "| implementation of P22 | [refinement_chain_certification.py](src/consciousness_bridge/refinement_chain_certification.py) | simultaneous finite-sample refinement-chain confidence certificate |",
    "| implementation of P22 | [refinement_chain_certification.py](src/consciousness_bridge/refinement_chain_certification.py) | simultaneous finite-sample refinement-chain confidence certificate |\n| implementation of P23 | [adaptive_descriptor_selection.py](src/consciousness_bridge/adaptive_descriptor_selection.py) | adaptive fixed-sample descriptor-selection and regret certificate |",
    "README P23 implementation navigation",
)
replace_once(
    "README.md",
    "| **4.8 P22 simultaneous refinement certification** | Can one finite data set certify the full declared residual-and-gain trajectory at once? |",
    "| **4.8 P22 simultaneous refinement certification** | Can one finite data set certify the full declared residual-and-gain trajectory at once? |\n| **4.9 P23 adaptive descriptor selection** | Does finite-sample validity survive choosing the physical refinement after inspecting the same data? |",
    "README P23 paper-map row",
)
replace_once(
    "README.md",
    "| proposition-level results | **22** |",
    "| proposition-level results | **23** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.22.0** |",
    "| research-software version | **0.23.0** |",
    "README software version",
)

p22_end = """[Read Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md). The [P22 theorem map](docs/figures/p22_simultaneous_refinement_chain_certification.svg), [implementation](src/consciousness_bridge/refinement_chain_certification.py), and [tests](tests/test_refinement_chain_certification.py) expose the full proof-to-code path.

---

# 5. Probability, distinguishability, and information geometry"""

p23_section = r"""[Read Proposition 22](docs/proposition_22_simultaneous_refinement_chain_certification.md). The [P22 theorem map](docs/figures/p22_simultaneous_refinement_chain_certification.svg), [implementation](src/consciousness_bridge/refinement_chain_certification.py), and [tests](tests/test_refinement_chain_certification.py) expose the full proof-to-code path.

# 4.9 P23 - adaptive physical-descriptor selection certification

![P23 adaptive physical-descriptor selection certification](docs/figures/p23_adaptive_descriptor_selection_certification.svg)

P22 certifies a fixed declared refinement chain. P23 addresses the next statistical question: **what happens when the next physical refinement is selected after inspecting the same finite data?**

Let the sampled base law be

\[
Z=(\Omega,E)\sim P,
\]

with empirical law \(\widehat P_n\), and let a common coarse physical descriptor be

\[
T_c=c(\Omega).
\]

For every admissible candidate \(f\), define a finer deterministic descriptor

\[
T_f=f(\Omega)
\]

that refines \(T_c\). The P21 refinement gain and remaining residual are

\[
\boxed{
G_f=I(E;T_f\mid T_c),
\qquad
R_f=I(E;\Omega\mid T_f).
}
\]

P21 gives

\[
\boxed{R_c-R_f=G_f.}
\]

P23 starts from the same one-event finite-sample certificate used by P22:

\[
\boxed{
\mathcal A_n
=
\left\{
\|P-\widehat P_n\|_{\mathrm{TV}}
\le\tau_n(\alpha)
\right\},
\qquad
\Pr(\mathcal A_n)\ge1-\alpha.
}
\]

For **every** deterministic map \(h\), total variation contracts pathwise:

\[
\boxed{
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\|P-\widehat P_n\|_{\mathrm{TV}}.
}
\]

Therefore, once \(\mathcal A_n\) occurs, all admissible residual and gain pushforwards are controlled simultaneously. In particular,

\[
\boxed{
|G_f-\widehat G_f|
\le
\Gamma_f(\tau_n),
\qquad
|R_f-\widehat R_f|
\le
\Delta_f(\tau_n)
\quad
\forall f.
}
\]

Now choose the refinement from the same data:

\[
\boxed{
\widehat f
\in
\operatorname*{arg\,max}_{f}\widehat G_f.
}
\]

Because the candidate inequalities already hold simultaneously on one base event, they remain valid for the selected candidate. P23 therefore proves fixed-sample post-selection coverage without a separate candidate-count confidence split.

The theorem also quantifies selection regret. If

\[
G^*=\max_f G_f
\]

and \(L_f^G,U_f^G\) are simultaneous candidate gain bounds, then

\[
\boxed{
0
\le
G^*-G_{\widehat f}
\le
\max_f U_f^G-L_{\widehat f}^G
\le
2\Gamma_{\max}.
}
\]

Since all candidates refine the same coarse descriptor,

\[
\boxed{
R_{\widehat f}-\min_fR_f
=
G^*-G_{\widehat f}.
}
\]

Thus the same certificate bounds how far the selected physical refinement can be from the smallest population residual available in the declared admissible class.

The absence of a direct candidate-count penalty is structural, not a general statement that model selection is free. The confidence ball controls the **base distribution itself**, and candidate laws are deterministic pushforwards of that same law. The finite-data cost still depends strongly on the declared physical-state alphabet and on the descriptor alphabet sizes.

P23 also draws a strict boundary between statistical validity and scientific interpretation:

\[
\boxed{
\text{post-selection statistical validity}
\neq
\text{physical admissibility}.
}
\]

A descriptor engineered from target labels can still be a mathematical function of \(\Omega\) after construction. P23's probability theorem does not make such a map a physically explanatory variable. Physical admissibility still requires independent justification of variables, system boundaries, measurement models, intervention semantics, and scale.

Finally, P23 is **fixed-sample**. Repeatedly collecting more data, inspecting the certificate, and stopping when a desired result appears is an optional-stopping problem and is not covered by this theorem.

[Read Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md). The [P23 theorem map](docs/figures/p23_adaptive_descriptor_selection_certification.svg), [implementation](src/consciousness_bridge/adaptive_descriptor_selection.py), and [tests](tests/test_adaptive_descriptor_selection.py) expose the full proof-to-code path.

---

# 5. Probability, distinguishability, and information geometry"""
replace_once(
    "README.md",
    p22_end,
    p23_section,
    "README P23 theorem section",
)
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P22",
    "# 7. Theorem roadmap - P1 through P23",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P22** | one base confidence event simultaneously certifies the declared residual-and-refinement-gain chain | proved finite-sample theorem | [P22](docs/proposition_22_simultaneous_refinement_chain_certification.md) |",
    "| **P22** | one base confidence event simultaneously certifies the declared residual-and-refinement-gain chain | proved finite-sample theorem | [P22](docs/proposition_22_simultaneous_refinement_chain_certification.md) |\n| **P23** | fixed-sample adaptive descriptor selection retains simultaneous coverage and admits explicit refinement-regret bounds | proved post-selection theorem | [P23](docs/proposition_23_adaptive_descriptor_selection_certification.md) |",
    "README P23 theorem table row",
)

# ---------------------------------------------------------------------------
# Theorem roadmap prose.
# ---------------------------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P22 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P23 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared base-TV confidence event plus deterministic pushforward contraction | simultaneous finite-data confidence family for P21 residuals and gains | proved simultaneous-certification theorem |",
    "| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared base-TV confidence event plus deterministic pushforward contraction | simultaneous finite-data confidence family for P21 residuals and gains | proved simultaneous-certification theorem |\n| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | universal pushforward control plus post-selection regret analysis | adaptive fixed-sample physical-refinement selection with valid coverage | proved post-selection theorem |",
    "roadmap P23 proposition row",
)

roadmap_marker = """Direct proof: [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md). Implementation: [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py). Tests: [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py).

---

# 12. Dependency chain"""
roadmap_insert = r"""Direct proof: [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md). Implementation: [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py). Tests: [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py).

---

# 12. Adaptive physical-descriptor selection: P23

Let \(T_c=c(\Omega)\) be a common coarse physical descriptor and let every admissible \(T_f=f(\Omega)\) refine \(T_c\).

On the one P22 base confidence event,

\[
\boxed{
\|P-\widehat P\|_{\mathrm{TV}}
\le\tau_n(\alpha),
}
\]

total-variation contraction implies uniform control for every deterministic candidate pushforward. Hence the simultaneous gain and residual bounds remain valid even after selecting

\[
\boxed{
\widehat f\in\operatorname*{arg\,max}_f\widehat G_f.
}
\]

If \(G^*=\max_fG_f\), then P23 proves

\[
\boxed{
0\le G^*-G_{\widehat f}
\le\max_fU_f^G-L_{\widehat f}^G
\le2\Gamma_{\max}.
}
\]

By P21,

\[
\boxed{
R_{\widehat f}-\min_fR_f
=G^*-G_{\widehat f}.
}
\]

Thus fixed-sample adaptive selection retains coverage and receives a quantitative near-optimality certificate relative to the declared admissible descriptor class.

P23 does not cover optional stopping across sample sizes, and statistical post-selection validity does not by itself establish that a selected map is a scientifically meaningful physical descriptor.

Direct proof: [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md). Implementation: [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py). Tests: [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py).

---

# 13. Dependency chain"""
replace_once(
    "docs/theorem_roadmap.md",
    roadmap_marker,
    roadmap_insert,
    "roadmap P23 theorem section",
)
replace_once(
    "docs/theorem_roadmap.md",
    r"""&\text{P22: simultaneous finite-sample refinement certification}.
\end{aligned}""",
    r"""&\text{P22: simultaneous finite-sample refinement certification}\\
&\Downarrow\\
&\text{P23: fixed-sample adaptive descriptor selection}.
\end{aligned}""",
    "roadmap dependency tail",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 13. Current frontier",
    "# 14. Current frontier",
    "roadmap frontier numbering",
)
replace_once(
    "docs/theorem_roadmap.md",
    "3. extend P22 beyond fixed finite-alphabet IID chains to continuous, dependent, hidden-state, noisy-descriptor, and adaptive-refinement settings with valid coverage;",
    "3. extend P23 from fixed-sample post-selection validity to anytime-valid adaptive refinement with optional stopping, then address continuous, dependent, hidden-state, and noisy-descriptor settings;",
    "roadmap post-P23 frontier",
)

# ---------------------------------------------------------------------------
# Reader navigation.
# ---------------------------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "for the dependency structure from P1 through P22.",
    "for the dependency structure from P1 through P23.",
    "navigation theorem range",
)
old_reading = """8. [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md) for simultaneous finite-data certification of the full P21 refinement trajectory.
9. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
10. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
11. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
12. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
new_reading = """8. [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md) for simultaneous finite-data certification of the full P21 refinement trajectory.
9. [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md) for fixed-sample adaptive descriptor selection and post-selection regret certification.
10. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
11. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
12. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
13. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
replace_once(
    "docs/research_navigation.md",
    old_reading,
    new_reading,
    "navigation P23 reading order",
)
replace_once(
    "docs/research_navigation.md",
    "| P22 | [Simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | one shared finite-sample confidence event for all P21 residuals and gains |",
    "| P22 | [Simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | one shared finite-sample confidence event for all P21 residuals and gains |\n| P23 | [Adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and near-optimal refinement selection |",
    "navigation P23 proposition row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P22 simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | simultaneous finite-sample confidence family for the full declared refinement trajectory |",
    "| [P22 simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md) | simultaneous finite-sample confidence family for the full declared refinement trajectory |\n| [P23 adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | post-selection coverage and refinement-regret bounds for adaptive fixed-sample physical descriptor choice |",
    "navigation P23 fundamental-theory row",
)
replace_once(
    "docs/research_navigation.md",
    "The P22 simultaneous finite-data layer is implemented in [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py), tested in [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py), and summarized by [p22_simultaneous_refinement_chain_certification.svg](figures/p22_simultaneous_refinement_chain_certification.svg).",
    "The P22 simultaneous finite-data layer is implemented in [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py), tested in [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py), and summarized by [p22_simultaneous_refinement_chain_certification.svg](figures/p22_simultaneous_refinement_chain_certification.svg). The P23 adaptive-selection layer is implemented in [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py), tested in [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py), and summarized by [p23_adaptive_descriptor_selection_certification.svg](figures/p23_adaptive_descriptor_selection_certification.svg).",
    "navigation P23 implementation",
)

# ---------------------------------------------------------------------------
# Equation and citation provenance.
# ---------------------------------------------------------------------------
p23_equation_section = r"""# 17. P23 - adaptive physical-descriptor selection certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\|h_\#P-h_\#\widehat P\|_{\mathrm{TV}}\le\|P-\widehat P\|_{\mathrm{TV}}\) for every deterministic \(h\) | pathwise pushforward contraction supporting uniform candidate control | standard total-variation data processing applied here | standard probability; [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(G_f=I(E;T_f\mid T_c)\) | target-relevant information captured by candidate refinement \(f\) | P21 refinement gain used as P23 selection objective | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(\widehat f\in\operatorname*{arg\,max}_f\widehat G_f\) | fixed-sample data-dependent descriptor-selection rule | repository selection construction | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(|G_f-\widehat G_f|\le\Gamma_f(\tau_n)\) for all candidates on one base event | simultaneous gain confidence family before and after selection | proved from P22 base event, TV contraction, and P20 entropy continuity | [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(0\le G^*-G_{\widehat f}\le2\Gamma_{\max}\) | generic post-selection refinement-regret bound | proved | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(G^*-G_{\widehat f}\le\max_fU_f^G-L_{\widehat f}^G\) | data-dependent regret certificate from simultaneous candidate intervals | proved | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(R_{\widehat f}-\min_fR_f=G^*-G_{\widehat f}\) | converts gain regret into excess remaining residual under a common coarse descriptor | proved from P21 identity | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |

P23 is a fixed-sample post-selection theorem. The shared base confidence event supports data-dependent candidate choice because all candidate laws are deterministic pushforwards of the same finite base law. This does not provide optional-stopping validity across sample sizes and does not establish the physical admissibility or completeness of the selected descriptor.

---

# 18. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    "# 17. Candidate consciousness-theory feature families",
    p23_equation_section,
    "equation map P23 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 18. Citation discipline",
    "# 19. Citation discipline",
    "equation map citation numbering",
)

# ---------------------------------------------------------------------------
# Release metadata.
# ---------------------------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.22.0"',
    'version = "0.23.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "simultaneous refinement-chain certification, recoverability",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, recoverability",
    "pyproject P23 description",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.22.0"',
    '__version__ = "0.23.0"',
    "package version",
)
replace_once(
    "CITATION.cff",
    "version: 0.22.0",
    "version: 0.23.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "simultaneous refinement-chain certification, robust experiment design",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, robust experiment design",
    "citation P23 abstract",
)

changelog_marker = """This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.22.0 - 2026-09-09"""
changelog_insert = r"""This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.23.0 - 2026-09-09

### Proposition 23 - adaptive physical-descriptor selection certification

- Extended the P22 shared-base-law confidence event from fixed refinement chains to fixed-sample data-dependent selection among admissible deterministic refinements.
- Used pathwise total-variation contraction to show that one base confidence event controls every deterministic candidate pushforward simultaneously.
- Proved that the residual and refinement-gain confidence intervals remain valid for the descriptor selected from the same finite sample.
- Proved the generic post-selection regret bound \(0\le G^*-G_{\widehat f}\le2\Gamma_{\max}\).
- Added the sharper observable certificate \(G^*-G_{\widehat f}\le\max_fU_f^G-L_{\widehat f}^G\).
- Used P21 to identify the same quantity with selected residual excess: \(R_{\widehat f}-\min_fR_f=G^*-G_{\widehat f}\).
- Made the distinction between statistical post-selection validity and physical admissibility explicit.
- Preserved the fixed-sample boundary: optional stopping across growing sample sizes remains outside P23.
- Added executable adaptive-selection certification, fourteen dedicated regression tests, and a publication-style P23 theorem map.
- Extended the README paper, global theorem roadmap, research navigation, equation provenance, release metadata, proposition guards, and figure-quality guards through P23.

## 0.22.0 - 2026-09-09"""
replace_once(
    "CHANGELOG.md",
    changelog_marker,
    changelog_insert,
    "P23 changelog release",
)

# ---------------------------------------------------------------------------
# Machine guards: P1-P23 and the P23 public figure are now mandatory.
# ---------------------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p22_simultaneous_refinement_chain_certification.svg",\n',
    '    "p22_simultaneous_refinement_chain_certification.svg",\n    "p23_adaptive_descriptor_selection_certification.svg",\n',
    "main-page P23 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 23):",
    "for index in range(1, 24):",
    "main-page P23 proposition range",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 23):",
    "for number in range(1, 24):",
    "navigation P23 proposition range",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p22_simultaneous_refinement_chain_certification.svg",\n',
    '    "p22_simultaneous_refinement_chain_certification.svg",\n    "p23_adaptive_descriptor_selection_certification.svg",\n',
    "visual P23 figure guard",
)

# ---------------------------------------------------------------------------
# Final fail-fast requirements.
# ---------------------------------------------------------------------------
requirements = (
    ("README.md", "version-0.23.0-2563eb", "README version"),
    ("README.md", "# 4.9 P23 - adaptive physical-descriptor selection certification", "README P23 section"),
    ("README.md", "p23_adaptive_descriptor_selection_certification.svg", "README P23 figure"),
    ("README.md", "| **P23** |", "README P23 theorem row"),
    ("docs/theorem_roadmap.md", "P1-P23 theorem roadmap", "roadmap P23 range"),
    ("docs/theorem_roadmap.md", "# 12. Adaptive physical-descriptor selection: P23", "roadmap P23 section"),
    ("docs/research_navigation.md", "proposition_23_adaptive_descriptor_selection_certification.md", "navigation P23 link"),
    ("docs/equation_and_citation_map.md", "# 17. P23 - adaptive physical-descriptor selection certification", "equation-map P23 section"),
    ("docs/figures/theorem_roadmap.svg", "P1 through P23", "visual roadmap P23 title"),
    ("docs/figures/p23_adaptive_descriptor_selection_certification.svg", "POST-SELECTION NEAR-OPTIMALITY", "P23 figure theorem block"),
    ("pyproject.toml", 'version = "0.23.0"', "pyproject version"),
    ("src/consciousness_bridge/__init__.py", '__version__ = "0.23.0"', "package version"),
    ("CITATION.cff", "version: 0.23.0", "citation version"),
    ("CHANGELOG.md", "## 0.23.0 - 2026-09-09", "P23 changelog"),
    ("tests/test_main_page_visual_paper.py", '"p23_adaptive_descriptor_selection_certification.svg"', "main-page P23 figure guard"),
    ("tests/test_main_page_visual_paper.py", "range(1, 24)", "main-page P23 range"),
    ("tests/test_document_link_integrity.py", "range(1, 24)", "navigation P23 range"),
    ("tests/test_visual_and_terminology_quality.py", '"p23_adaptive_descriptor_selection_certification.svg"', "visual P23 guard"),
)
for path, token, label in requirements:
    require(path, token, label)

print("P23 release integration applied and verified")
