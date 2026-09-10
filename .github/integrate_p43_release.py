from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.42.0-2563eb", "version-0.43.0-2563eb", "README version")
text = replace_once(
    text,
    "**P42** derives explicit finite-sample radii for a fixed informationally complete measurement and categorical target model, then solves for sufficient quantum and target sample sizes needed to resolve a positive population regularity gap.",
    "**P42** derives explicit finite-sample radii for a fixed informationally complete measurement and categorical target model, then solves for sufficient quantum and target sample sizes needed to resolve a positive population regularity gap. **P43** removes the arbitrary P42 quantum-versus-target uncertainty split and proves the unique cube-root allocation that minimizes a declared weighted sampling cost, including an explicit integer-rounding overhead bound.",
    "README abstract P43",
)
text = replace_once(text, "**42 proposition-level results", "**43 proposition-level results", "README proposition count")
text = text.replace("P1 through P42", "P1 through P43")
text = replace_once(
    text,
    "| quantum regular-bridge sample complexity | [Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md) | explicit IC-tomography and categorical-target sample sizes for resolving a positive Lipschitz regularity gap |",
    "| quantum regular-bridge sample complexity | [Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md) | explicit IC-tomography and categorical-target sample sizes for resolving a positive Lipschitz regularity gap |\n| optimal quantum-target allocation | [Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md) | closed-form cube-root allocation minimizing weighted P42 sampling cost with integer-rounding control |",
    "README navigation P43",
)
text = replace_once(
    text,
    "| **11.18 P42 quantum regular-bridge sample complexity** | How many IC quantum measurements and categorical target observations are sufficient to resolve a declared positive regularity gap? |",
    "| **11.18 P42 quantum regular-bridge sample complexity** | How many IC quantum measurements and categorical target observations are sufficient to resolve a declared positive regularity gap? |\n| **11.19 P43 optimal quantum-target allocation** | How should the P42 uncertainty budget be divided to minimize declared weighted sampling cost? |",
    "README paper map P43",
)
text = replace_once(text, "| proposition-level results | **42** |", "| proposition-level results | **43** |", "README record count")
text = replace_once(text, "| research-software version | **0.42.0** |", "| research-software version | **0.43.0** |", "README record version")

p43 = r'''## 13.16 P43 - optimal quantum-target uncertainty allocation

![P43 optimal quantum-target uncertainty allocation](docs/figures/p43_optimal_quantum_target_allocation.svg)

P42 leaves one design choice free: the fraction \(\lambda\in(0,1)\) of the population regularity gap assigned to target uncertainty. P43 solves that design problem exactly for a declared weighted sampling cost.

Write the P42 sufficient sample sizes as

\[
n_Y\ge\frac{A_Y}{\lambda^2},
\qquad
n_Q\ge\frac{A_Q}{(1-\lambda)^2},
\]

with

\[
A_Y=\frac{2k^2}{\Delta^2}\log\frac{2Kk}{\alpha_Y},
\qquad
A_Q=\frac{8L^2\kappa_R^2m^2}{\Delta^2}\log\frac{2Km}{\alpha_Q}.
\]

Let \(c_Y>0\) and \(c_Q>0\) be declared costs per target and quantum sample. The continuous weighted per-preparation cost is

\[
\boxed{
C(\lambda)
=c_Y\frac{A_Y}{\lambda^2}
+c_Q\frac{A_Q}{(1-\lambda)^2}.
}
\]

Because

\[
C''(\lambda)
=\frac{6c_YA_Y}{\lambda^4}
+\frac{6c_QA_Q}{(1-\lambda)^4}>0,
\]

the objective is strictly convex. P43 therefore has one global optimum:

\[
\boxed{
\lambda_*
=
\frac{(c_YA_Y)^{1/3}}
{(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}}.
}
\]

The exact minimum continuous cost is

\[
\boxed{
C_*
=\left[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}\right]^3.
}
\]

Using sufficient integer sample sizes

\[
N_Y=\left\lceil\frac{A_Y}{\lambda_*^2}\right\rceil,
\qquad
N_Q=\left\lceil\frac{A_Q}{(1-\lambda_*)^2}\right\rceil,
\]

P43 gives the rounding guarantee

\[
\boxed{
C_*
\le c_YN_Y+c_QN_Q
\le C_*+c_Y+c_Q.
}
\]

Balanced allocation \(\lambda=1/2\) is optimal exactly when

\[
\boxed{c_YA_Y=c_QA_Q.}
\]

More generally its continuous cost is within a factor four of the optimum:

\[
\boxed{
1\le\frac{C_{1/2}}{C_*}\le4.
}
\]

P43 replaces that generic baseline with the exact cost-minimizing design. The cube-root law also exposes how tomography conditioning, bridge regularity, measurement outcome count, target alphabet size, and monetary or operational sample costs shift the optimal precision budget.

No additional confidence penalty is introduced when the design quantities are fixed before data collection. The P42 confidence lower bound remains

\[
\boxed{\max\{0,1-\alpha_Q-\alpha_Y\}.}
\]

The scientific boundary is unchanged:

\[
\boxed{
\text{optimal resource allocation inside P42}
\neq
\text{evidence that quantum mechanics is incomplete}.
}
\]

The costs are design weights, not physical observables. P43 optimizes a declared experiment and does not establish physical completeness or experiential interpretation.

[Read Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md). The [P43 theorem map](docs/figures/p43_optimal_quantum_target_allocation.svg), [implementation](src/consciousness_bridge/optimal_quantum_target_allocation.py), and [tests](tests/test_optimal_quantum_target_allocation.py) expose the complete proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md). The [P42 theorem map](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg), [implementation](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py), and [tests](tests/test_quantum_regular_bridge_sample_complexity.py) expose the complete proof-to-code path.\n\n---",
    "[Read Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md). The [P42 theorem map](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg), [implementation](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py), and [tests](tests/test_quantum_regular_bridge_sample_complexity.py) expose the complete proof-to-code path.\n\n" + p43 + "---",
    "README P43 section",
)
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P42 quantum regular-bridge sample complexity](figures/p42_quantum_regular_bridge_sample_complexity.svg)",
    "![P42 quantum regular-bridge sample complexity](figures/p42_quantum_regular_bridge_sample_complexity.svg)\n\n![P43 optimal quantum-target allocation](figures/p43_optimal_quantum_target_allocation.svg)",
    "roadmap P43 figure",
)
row = "| [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) | IC-measurement Hoeffding concentration plus linear-reconstruction stability | explicit sufficient quantum and target samples for a positive regularity obstruction | proved finite-sample design theorem |"
text = replace_once(
    text,
    row,
    row + "\n| [P43](proposition_43_optimal_quantum_target_allocation.md) | strict convexity and closed-form weighted allocation | unique minimum-cost split of the P42 quantum and target uncertainty budget | proved resource-allocation theorem |",
    "roadmap P43 row",
)
p43_road = r'''## P43 - optimal quantum-target allocation

For the P42 coefficients \(A_Y,A_Q>0\) and declared sample costs \(c_Y,c_Q>0\), P43 minimizes

\[
C(\lambda)=c_YA_Y/\lambda^2+c_QA_Q/(1-\lambda)^2.
\]

Strict convexity gives the unique optimum

\[
\boxed{
\lambda_*=\frac{(c_YA_Y)^{1/3}}{(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}}
}
\]

and

\[
\boxed{C_*=[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}]^3.}
\]

Upward integer rounding adds at most \(c_Y+c_Q\) weighted cost per preparation. This is a pre-data resource optimization within P42, not a physical-completeness theorem.

Direct proof: [Proposition 43](proposition_43_optimal_quantum_target_allocation.md). Implementation: [optimal_quantum_target_allocation.py](../src/consciousness_bridge/optimal_quantum_target_allocation.py). Tests: [test_optimal_quantum_target_allocation.py](../tests/test_optimal_quantum_target_allocation.py).

---

'''
text = replace_once(text, "# 8. Fundamental physical sufficiency: P19", p43_road + "# 8. Fundamental physical sufficiency: P19", "roadmap P43 section")
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = text.replace("from P1 through P42", "from P1 through P43")
row = "| P42 | [Quantum regular-bridge sample complexity](proposition_42_quantum_regular_bridge_sample_complexity.md) | explicit fixed-IC quantum and categorical-target sample-size theorem |"
text = replace_once(
    text,
    row,
    row + "\n| P43 | [Optimal quantum-target allocation](proposition_43_optimal_quantum_target_allocation.md) | cube-root minimum-cost allocation of the P42 uncertainty budget |",
    "navigation P43 row",
)
path.write_text(text, encoding="utf-8")

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
p43_eq = r'''# 32. P43 optimal quantum-target uncertainty allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C(\lambda)=c_YA_Y/\lambda^2+c_QA_Q/(1-\lambda)^2\) | weighted P42 sampling cost | repository design objective | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C''(\lambda)>0\) on \((0,1)\) | strict convexity and uniqueness of the optimizer | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(\lambda_*=(c_YA_Y)^{1/3}/[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}]\) | exact optimal target-side gap fraction | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C_*=[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}]^3\) | exact minimum continuous weighted cost | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C_*\le C_{int}\le C_*+c_Y+c_Q\) | sufficient integer-rounding overhead bound | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(1\le C_{1/2}/C_*\le4\) | universal balanced-allocation approximation bound | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |

P43 optimizes a declared P42 resource objective with design weights fixed before data collection. It does not add evidence for physical completeness, quantum incompleteness, or consciousness.

---

'''
text = replace_once(text, "# 32. Candidate consciousness-theory feature families", p43_eq + "# 33. Candidate consciousness-theory feature families", "equation map P43")
text = replace_once(text, "# 33. Citation discipline", "# 34. Citation discipline", "equation map citation renumber")
path.write_text(text, encoding="utf-8")

# Main-page and release guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p42_quantum_regular_bridge_sample_complexity.svg",', '    "p42_quantum_regular_bridge_sample_complexity.svg",\n    "p43_optimal_quantum_target_allocation.svg",', "main-page P43 figure")
text = replace_once(text, "for index in range(1, 43):", "for index in range(1, 44):", "main-page P43 range")
path.write_text(text, encoding="utf-8")

path = Path("tests/test_release_metadata_consistency.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.42.0-2563eb", "version-0.43.0-2563eb", "release guard README")
text = replace_once(text, 'r\'^version = "0\\.42\\.0"$\'', 'r\'^version = "0\\.43\\.0"$\'', "release guard pyproject")
text = replace_once(text, "r'^version: 0\\.42\\.0$'", "r'^version: 0\\.43\\.0$'", "release guard citation")
text = replace_once(
    text,
    '        "test_quantum_regular_bridge_sample_complexity.py",',
    '        "test_quantum_regular_bridge_sample_complexity.py",\n        "Proposition 43",\n        "p43_optimal_quantum_target_allocation.svg",\n        "optimal_quantum_target_allocation.py",\n        "test_optimal_quantum_target_allocation.py",',
    "release guard P43 paths",
)
path.write_text(text, encoding="utf-8")

# Release metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.42.0"', 'version = "0.43.0"', "pyproject version")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.42.0", "version: 0.43.0", "citation version")
text = replace_once(
    text,
    "fixed-IC quantum regular-bridge sample complexity,",
    "fixed-IC quantum regular-bridge sample complexity, optimal quantum-target resource allocation,",
    "citation P43 abstract",
)
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.43.0 - 2026-09-09

### Added
- Proposition 43: exact minimum-cost allocation of the P42 quantum and target uncertainty budget.
- Strict-convexity proof and closed-form cube-root allocation law.
- Exact minimum continuous weighted sampling cost.
- Sufficient integer sample counts with at most one weighted sample of rounding overhead per modality and preparation.
- Universal factor-four upper bound for the balanced P42 allocation relative to the exact continuous optimum.
- Executable optimizer, dedicated regression tests, theorem map, and full public-paper integration.

### Scientific boundary
- P43 optimizes declared experimental resources under P42 assumptions and fixed pre-data design weights.
- The result does not establish physical completeness, quantum incompleteness, or consciousness.

'''
text = replace_once(text, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog P43")
path.write_text(text, encoding="utf-8")
