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
        raise RuntimeError(f"missing requirement {label} in {path}")


# README ---------------------------------------------------------------------
replace_once(
    "README.md",
    "version-0.23.0-2563eb",
    "version-0.24.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P23** proves that the same shared base confidence event also supports fixed-sample data-dependent selection among admissible deterministic refinements, together with an explicit near-optimality bound for the selected refinement.",
    "**P23** proves that the same shared base confidence event also supports fixed-sample data-dependent selection among admissible deterministic refinements, together with an explicit near-optimality bound for the selected refinement. **P24** converts that fixed-sample result into an anytime-valid certificate by allocating the total error budget across all positive sample sizes, giving simultaneous repeated-look and finite stopping-time validity under the declared finite-alphabet IID model.",
    "README abstract P24 summary",
)
replace_once(
    "README.md",
    "**23 proposition-level results, 58 equation-driven quantitative figures",
    "**24 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P23 in dependency order",
    "P1 through P24 in dependency order",
    "README theorem navigation range",
)
replace_once(
    "README.md",
    "| adaptive refinement-selection theorem | [Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and refinement-regret control |",
    "| adaptive refinement-selection theorem | [Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and refinement-regret control |\n| anytime refinement theorem | [Proposition 24](docs/proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look, adaptive-selection, and finite stopping-time validity |",
    "README P24 theorem navigation",
)
replace_once(
    "README.md",
    "| implementation of P23 | [adaptive_descriptor_selection.py](src/consciousness_bridge/adaptive_descriptor_selection.py) | adaptive fixed-sample descriptor-selection and regret certificate |",
    "| implementation of P23 | [adaptive_descriptor_selection.py](src/consciousness_bridge/adaptive_descriptor_selection.py) | adaptive fixed-sample descriptor-selection and regret certificate |\n| implementation of P24 | [anytime_refinement_certification.py](src/consciousness_bridge/anytime_refinement_certification.py) | anytime-valid adaptive refinement and stopping-time certificate |",
    "README P24 implementation navigation",
)
replace_once(
    "README.md",
    "| **4.9 P23 adaptive descriptor selection** | Does finite-sample validity survive choosing the physical refinement after inspecting the same data? |",
    "| **4.9 P23 adaptive descriptor selection** | Does finite-sample validity survive choosing the physical refinement after inspecting the same data? |\n| **4.10 P24 anytime-valid refinement** | Does coverage survive repeated inspection and a data-dependent finite stopping time? |",
    "README P24 paper-map row",
)
replace_once(
    "README.md",
    "| proposition-level results | **23** |",
    "| proposition-level results | **24** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.23.0** |",
    "| research-software version | **0.24.0** |",
    "README software version",
)

p23_end = """[Read Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md). The [P23 theorem map](docs/figures/p23_adaptive_descriptor_selection_certification.svg), [implementation](src/consciousness_bridge/adaptive_descriptor_selection.py), and [tests](tests/test_adaptive_descriptor_selection.py) expose the full proof-to-code path.

---

# 5. Probability, distinguishability, and information geometry"""

p24_section = r"""[Read Proposition 23](docs/proposition_23_adaptive_descriptor_selection_certification.md). The [P23 theorem map](docs/figures/p23_adaptive_descriptor_selection_certification.svg), [implementation](src/consciousness_bridge/adaptive_descriptor_selection.py), and [tests](tests/test_adaptive_descriptor_selection.py) expose the full proof-to-code path.

# 4.10 P24 - anytime-valid adaptive physical-refinement certification

![P24 anytime-valid adaptive physical-refinement certification](docs/figures/p24_anytime_adaptive_refinement_certification.svg)

P23 is a fixed-sample theorem. P24 addresses the remaining repeated-look loophole: **what happens when the same growing data stream is inspected repeatedly and the analysis stops when a desired certificate first appears?**

Let

\[
Z_i=(\Omega_i,E_i),
\qquad
Z_1,Z_2,\ldots\overset{\mathrm{IID}}{\sim}P,
\]

on a finite base alphabet of size \(M\). P24 allocates the total error probability across all positive sample sizes using

\[
\boxed{
\alpha_n
=
\frac{6\alpha}{\pi^2n^2}.
}
\]

Because

\[
\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6},
\]

we obtain the exact budget identity

\[
\boxed{
\sum_{n=1}^{\infty}\alpha_n=\alpha.
}
\]

Applying the P20 finite-alphabet concentration bound at local level \(\alpha_n\) gives

\[
\boxed{
\tau_n^{\mathrm{any}}(\alpha)
=
\min\left\{
1,
\frac M2
\sqrt{
\frac1{2n}
\log\left(
\frac{M\pi^2n^2}{3\alpha}
\right)
}
\right\}.
}
\]

A countable union bound then yields one event valid for all positive times:

\[
\boxed{
\Pr\left(
\forall n\ge1,
\ \|P-\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n^{\mathrm{any}}(\alpha)
\right)
\ge1-\alpha.
}
\]

P23's deterministic-pushforward argument is pathwise, so on this one event the gain and residual intervals remain valid for every admissible deterministic descriptor at every time. If the analysis selects

\[
\widehat f_n=S_n(Z_1,\ldots,Z_n),
\]

then

\[
\boxed{
G_{\widehat f_n}\in\mathcal I^G_{n,\widehat f_n},
\qquad
R_{\widehat f_n}\in\mathcal I^R_{n,\widehat f_n}
\quad\forall n\ge1
}
\]

with simultaneous probability at least \(1-\alpha\).

Let \(\tau\) be a stopping time with respect to the observed-data filtration. If \(\tau<\infty\), the same event is valid at the realized random time, so

\[
\boxed{
\Pr\left(
G_{\widehat f_\tau}\in\mathcal I^G_{\tau,\widehat f_\tau},
\quad
R_{\widehat f_\tau}\in\mathcal I^R_{\tau,\widehat f_\tau}
\right)
\ge1-\alpha.
}
\]

The P23 near-optimality result is also time uniform. With

\[
B_n
=
\max_fU_{f,n}^G-L_{\widehat f_n,n}^G,
\]

P24 gives

\[
\boxed{
0\le G^*-G_{\widehat f_n}\le B_n
\qquad\forall n\ge1,
}
\]

and, by P21,

\[
\boxed{
R_{\widehat f_n}-\min_fR_f
=G^*-G_{\widehat f_n}
\le B_n.
}
\]

This permits statistically valid stopping rules such as the first time the selected gain has a positive lower bound or the first time the refinement-regret certificate falls below a prespecified tolerance.

The construction is deliberately conservative. It is an explicit alpha-spending confidence sequence, not an optimized martingale, e-process, or mixture bound. It assumes a fixed finite alphabet, IID observations, and deterministic admissible descriptor maps.

The interpretation boundary remains strict:

\[
\boxed{
\text{anytime statistical validity}
\neq
\text{physical completeness}
\neq
\text{experiential interpretation}.
}
\]

[Read Proposition 24](docs/proposition_24_anytime_adaptive_refinement_certification.md). The [P24 theorem map](docs/figures/p24_anytime_adaptive_refinement_certification.svg), [implementation](src/consciousness_bridge/anytime_refinement_certification.py), and [tests](tests/test_anytime_refinement_certification.py) expose the full proof-to-code path.

---

# 5. Probability, distinguishability, and information geometry"""
replace_once("README.md", p23_end, p24_section, "README P24 theorem section")
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P23",
    "# 7. Theorem roadmap - P1 through P24",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P23** | fixed-sample adaptive descriptor selection retains simultaneous coverage and admits explicit refinement-regret bounds | proved post-selection theorem | [P23](docs/proposition_23_adaptive_descriptor_selection_certification.md) |",
    "| **P23** | fixed-sample adaptive descriptor selection retains simultaneous coverage and admits explicit refinement-regret bounds | proved post-selection theorem | [P23](docs/proposition_23_adaptive_descriptor_selection_certification.md) |\n| **P24** | summable alpha spending gives time-uniform adaptive-selection and finite stopping-time validity | proved anytime-valid theorem | [P24](docs/proposition_24_anytime_adaptive_refinement_certification.md) |",
    "README P24 theorem row",
)

# Theorem roadmap -----------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P23 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P24 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | universal pushforward control plus post-selection regret analysis | adaptive fixed-sample physical-refinement selection with valid coverage | proved post-selection theorem |",
    "| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | universal pushforward control plus post-selection regret analysis | adaptive fixed-sample physical-refinement selection with valid coverage | proved post-selection theorem |\n| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | summable alpha spending plus countable union control | repeated-look adaptive refinement and finite stopping-time validity | proved anytime-valid theorem |",
    "roadmap P24 proposition row",
)
roadmap_marker = """Direct proof: [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md). Implementation: [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py). Tests: [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py).

---

# 13. Dependency chain"""
roadmap_insert = r"""Direct proof: [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md). Implementation: [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py). Tests: [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py).

---

# 13. Anytime-valid adaptive refinement: P24

P24 distributes the global error budget over all positive sample sizes using

\[
\boxed{
\alpha_n=\frac{6\alpha}{\pi^2n^2},
\qquad
\sum_{n\ge1}\alpha_n=\alpha.
}
\]

The resulting time-indexed P20 radius is

\[
\boxed{
\tau_n^{\mathrm{any}}(\alpha)
=
\min\left\{
1,
\frac M2
\sqrt{\frac1{2n}\log\left(\frac{M\pi^2n^2}{3\alpha}\right)}
\right\}.
}
\]

A countable union bound gives

\[
\boxed{
\Pr\left(
\forall n\ge1:
\|P-\widehat P_n\|_{\mathrm{TV}}
\le\tau_n^{\mathrm{any}}(\alpha)
\right)
\ge1-\alpha.
}
\]

P23's post-selection bounds are deterministic consequences of the base-law event. They therefore hold at every time simultaneously and at any realized finite stopping time.

Direct proof: [Proposition 24](proposition_24_anytime_adaptive_refinement_certification.md). Implementation: [anytime_refinement_certification.py](../src/consciousness_bridge/anytime_refinement_certification.py). Tests: [test_anytime_refinement_certification.py](../tests/test_anytime_refinement_certification.py).

---

# 14. Dependency chain"""
replace_once(
    "docs/theorem_roadmap.md",
    roadmap_marker,
    roadmap_insert,
    "roadmap P24 theorem section",
)
replace_once(
    "docs/theorem_roadmap.md",
    r"""&\text{P23: fixed-sample adaptive descriptor selection}.
\end{aligned}""",
    r"""&\text{P23: fixed-sample adaptive descriptor selection}\\
&\Downarrow\\
&\text{P24: anytime-valid adaptive selection + finite stopping-time control}.
\end{aligned}""",
    "roadmap dependency tail",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 14. Current frontier",
    "# 15. Current frontier",
    "roadmap frontier numbering",
)
replace_once(
    "docs/theorem_roadmap.md",
    "3. extend P23 from fixed-sample post-selection validity to anytime-valid adaptive refinement with optional stopping, then address continuous, dependent, hidden-state, and noisy-descriptor settings;",
    "3. sharpen P24 beyond conservative alpha spending and extend the refinement program to continuous, dependent, hidden-state, noisy-descriptor, and learned-descriptor settings;",
    "roadmap post-P24 frontier",
)

# Reader navigation ---------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "for the dependency structure from P1 through P23.",
    "for the dependency structure from P1 through P24.",
    "navigation theorem range",
)
old_reading = """9. [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md) for fixed-sample adaptive descriptor selection and post-selection regret certification.
10. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
11. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
12. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
13. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
new_reading = """9. [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md) for fixed-sample adaptive descriptor selection and post-selection regret certification.
10. [Proposition 24](proposition_24_anytime_adaptive_refinement_certification.md) for time-uniform repeated-look and finite stopping-time validity.
11. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
12. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
13. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
14. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards."""
replace_once(
    "docs/research_navigation.md",
    old_reading,
    new_reading,
    "navigation P24 reading order",
)
replace_once(
    "docs/research_navigation.md",
    "| P23 | [Adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and near-optimal refinement selection |",
    "| P23 | [Adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | fixed-sample post-selection validity and near-optimal refinement selection |\n| P24 | [Anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look validity, adaptive selection, and finite stopping-time control |",
    "navigation P24 index row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P23 adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | post-selection coverage and refinement-regret bounds for adaptive fixed-sample physical descriptor choice |",
    "| [P23 adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md) | post-selection coverage and refinement-regret bounds for adaptive fixed-sample physical descriptor choice |\n| [P24 anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | time-uniform coverage for repeated inspection and finite stopping times |",
    "navigation P24 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "The P23 adaptive-selection layer is implemented in [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py), tested in [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py), and summarized by [p23_adaptive_descriptor_selection_certification.svg](figures/p23_adaptive_descriptor_selection_certification.svg).",
    "The P23 adaptive-selection layer is implemented in [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py), tested in [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py), and summarized by [p23_adaptive_descriptor_selection_certification.svg](figures/p23_adaptive_descriptor_selection_certification.svg). The P24 anytime-valid layer is implemented in [anytime_refinement_certification.py](../src/consciousness_bridge/anytime_refinement_certification.py), tested in [test_anytime_refinement_certification.py](../tests/test_anytime_refinement_certification.py), and summarized by [p24_anytime_adaptive_refinement_certification.svg](figures/p24_anytime_adaptive_refinement_certification.svg).",
    "navigation P24 implementation",
)

# Equation provenance -------------------------------------------------------
p23_boundary = """P23 is a fixed-sample post-selection theorem. The shared base confidence event supports data-dependent candidate choice because all candidate laws are deterministic pushforwards of the same finite base law. This does not provide optional-stopping validity across sample sizes and does not establish the physical admissibility or completeness of the selected descriptor.

---

# 18. Candidate consciousness-theory feature families"""
p24_provenance = r"""P23 is a fixed-sample post-selection theorem. The shared base confidence event supports data-dependent candidate choice because all candidate laws are deterministic pushforwards of the same finite base law. This does not provide optional-stopping validity across sample sizes and does not establish the physical admissibility or completeness of the selected descriptor.

---

# 18. P24 - anytime-valid adaptive physical-refinement certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\alpha_n=6\alpha/(\pi^2n^2)\) | summable time-indexed failure allocation | repository choice using the standard Basel identity | standard analysis; [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\sum_{n\ge1}\alpha_n=\alpha\) | exact total error-budget identity | follows from \(\sum_{n\ge1}n^{-2}=\pi^2/6\) | standard analysis; [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\tau_n^{\mathrm{any}}(\alpha)\) | time-indexed P20 base-law TV radius evaluated at local level \(\alpha_n\) | repository construction from P20 | [P20](proposition_20_finite_sample_residual_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\Pr(\forall n\ge1:\|P-\widehat P_n\|_{\mathrm{TV}}\le\tau_n^{\mathrm{any}})\ge1-\alpha\) | time-uniform base-law confidence event | proved by countable union bound over P20 failures | [P20](proposition_20_finite_sample_residual_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\widehat f_n=S_n(Z_1,\ldots,Z_n)\) | data-dependent descriptor selected at time \(n\) | repository notation | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| selected gain and residual intervals valid for every \(n\) | repeated-look adaptive-selection coverage | proved from the P24 base event plus P23 pathwise pushforward control | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| stopping-time certificate at finite \(\tau\) | validity after a data-dependent finite stopping rule | proved because the confidence event is simultaneous over all positive times | [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(0\le G^*-G_{\widehat f_n}\le B_n\) for all \(n\) | anytime refinement-regret certificate | proved by applying P23 on the time-uniform event | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |

P24 uses a transparent alpha-spending union-bound construction. It is intentionally conservative and is not claimed to be an optimal confidence sequence. Anytime statistical validity does not establish physical completeness or experiential interpretation.

---

# 19. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    p23_boundary,
    p24_provenance,
    "equation map P24 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 19. Citation discipline",
    "# 20. Citation discipline",
    "equation map citation numbering",
)

# Tests ---------------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p23_adaptive_descriptor_selection_certification.svg",\n',
    '    "p23_adaptive_descriptor_selection_certification.svg",\n    "p24_anytime_adaptive_refinement_certification.svg",\n',
    "main-page P24 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 24):",
    "for index in range(1, 25):",
    "main-page P24 theorem range",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 24):",
    "for number in range(1, 25):",
    "navigation P24 theorem range guard",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p23_adaptive_descriptor_selection_certification.svg",\n',
    '    "p23_adaptive_descriptor_selection_certification.svg",\n    "p24_anytime_adaptive_refinement_certification.svg",\n',
    "visual P24 figure guard",
)

# Release metadata ----------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.23.0"',
    'version = "0.24.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, recoverability, and falsifiable experiment design.",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, anytime-valid refinement certification, recoverability, and falsifiable experiment design.",
    "pyproject P24 description",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.23.0"',
    '__version__ = "0.24.0"',
    "runtime version",
)
replace_once(
    "CITATION.cff",
    "version: 0.23.0",
    "version: 0.24.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, robust experiment design",
    "simultaneous refinement-chain certification, adaptive descriptor-selection certification, anytime-valid refinement certification, robust experiment design",
    "citation P24 abstract",
)

changelog_header = "# Changelog\n\nThis changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
p24_changelog = r"""# Changelog

This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.24.0 - 2026-09-09

### Proposition 24 - anytime-valid adaptive physical-refinement certification

- Converted P23 fixed-sample post-selection validity into a time-uniform certificate for one finite-alphabet IID stream.
- Introduced the explicit summable error schedule \(\alpha_n=6\alpha/(\pi^2n^2)\) with total mass exactly \(\alpha\).
- Derived the anytime base-law radius \(\tau_n^{\mathrm{any}}(\alpha)\) by applying the P20 categorical bound at local level \(\alpha_n\).
- Proved one confidence event valid simultaneously for every positive sample size using a countable union bound.
- Lifted P23 adaptive descriptor-selection coverage to every time on that event.
- Proved validity at any realized finite data-dependent stopping time.
- Extended the P23 refinement-regret and excess-residual certificates to the full time-uniform path.
- Added executable anytime certification, dedicated regression tests, a publication-style P24 theorem map, and a P1-P24 global roadmap.
- Preserved the interpretation boundary that anytime statistical validity does not establish physical completeness or experiential interpretation.
- Integrated P24 into the README paper, reader navigation, equation provenance, release metadata, proposition guards, and visual-quality guards.

"""
replace_once(
    "CHANGELOG.md",
    changelog_header,
    p24_changelog,
    "P24 changelog release",
)

# Fail-fast postconditions ---------------------------------------------------
requirements = {
    "README.md": [
        "version-0.24.0-2563eb",
        "# 4.10 P24 - anytime-valid adaptive physical-refinement certification",
        "# 7. Theorem roadmap - P1 through P24",
        "**24 proposition-level results",
        "p24_anytime_adaptive_refinement_certification.svg",
        "anytime statistical validity",
    ],
    "docs/theorem_roadmap.md": [
        "![P1-P24 theorem roadmap]",
        "# 13. Anytime-valid adaptive refinement: P24",
        "# 14. Dependency chain",
        "# 15. Current frontier",
    ],
    "docs/research_navigation.md": [
        "from P1 through P24",
        "proposition_24_anytime_adaptive_refinement_certification.md",
        "anytime_refinement_certification.py",
    ],
    "docs/equation_and_citation_map.md": [
        "# 18. P24 - anytime-valid adaptive physical-refinement certification",
        "# 19. Candidate consciousness-theory feature families",
        "# 20. Citation discipline",
    ],
    "pyproject.toml": ['version = "0.24.0"'],
    "CITATION.cff": ["version: 0.24.0"],
    "src/consciousness_bridge/__init__.py": ['__version__ = "0.24.0"'],
    "CHANGELOG.md": ["## 0.24.0 - 2026-09-09"],
    "tests/test_main_page_visual_paper.py": [
        "p24_anytime_adaptive_refinement_certification.svg",
        "range(1, 25)",
    ],
    "tests/test_document_link_integrity.py": ["range(1, 25)"],
    "tests/test_visual_and_terminology_quality.py": [
        "p24_anytime_adaptive_refinement_certification.svg"
    ],
}

for path, tokens in requirements.items():
    for token in tokens:
        require(path, token, token)
