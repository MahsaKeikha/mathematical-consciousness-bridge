from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_all(path: Path, old: str, new: str, minimum: int, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count < minimum:
        raise RuntimeError(f"{label}: expected at least {minimum} markers, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")


readme = ROOT / "README.md"
replace_once(
    readme,
    "version-0.45.0-2563eb",
    "version-0.46.0-2563eb",
    "README version badge",
)
replace_once(
    readme,
    "The public research record now contains **45 proposition-level results",
    "The public research record now contains **46 proposition-level results",
    "README proposition count",
)
replace_once(
    readme,
    "P1 through P45 with explicit dependency branches",
    "P1 through P46 with explicit dependency branches",
    "README theorem navigation count",
)
replace_once(
    readme,
    "**P45** then moves the resource-allocation problem from independent candidate pairs to a shared preparation graph: one preparation-level sample stream can tighten every incident candidate edge, the resulting inverse-square design problem is strictly convex, and the unique optimum obeys an incidence-weighted cube-root KKT law.",
    "**P45** then moves the resource-allocation problem from independent candidate pairs to a shared preparation graph: one preparation-level sample stream can tighten every incident candidate edge, the resulting inverse-square design problem is strictly convex, and the unique optimum obeys an incidence-weighted cube-root KKT law. **P46** adds the hard-budget discrete layer: it proves the induced witness value is monotone and supermodular, proves the general budgeted selection problem is NP-hard by reduction from CLIQUE, and gives a computable weighted-degree relaxation that certifies an upper bound on the unknown optimum.",
    "README abstract P46",
)
replace_once(
    readme,
    "| shared-preparation graph allocation | [Proposition 45](docs/proposition_45_shared_preparation_graph_allocation.md) | unique minimum-cost preparation-level allocation for overlapping candidate edges with an incidence-weighted KKT characterization |",
    "| shared-preparation graph allocation | [Proposition 45](docs/proposition_45_shared_preparation_graph_allocation.md) | unique minimum-cost preparation-level allocation for overlapping candidate edges with an incidence-weighted KKT characterization |\n| budget-constrained witness graph | [Proposition 46](docs/proposition_46_budget_constrained_witness_graph.md) | hard-budget preparation selection, NP-hardness, weighted-degree upper bound, and exact small-instance solver |",
    "README P46 navigation row",
)
p46_section = r'''## 13.19 P46 - budget-constrained witness-graph selection

![P46 budget-constrained witness graph](docs/figures/p46_budget_constrained_witness_graph.svg)

P45 solves a continuous shared-precision problem after the witness graph has already been declared. P46 addresses the discrete problem that appears when the total budget is too small to measure every preparation.

For a selected preparation set \(S\subseteq V\), define the total value of candidate witness edges whose two endpoints are both available:

\[
\boxed{
F(S)=\sum_{\{i,j\}\in E}w_{ij}\mathbf 1\{i,j\in S\}.
}
\]

The hard-budget design problem is

\[
\boxed{
\max_{S\subseteq V}F(S)
\quad\text{subject to}\quad
\sum_{i\in S}c_i\le B.
}
\]

P46 first proves that \(F\) is monotone and supermodular. Adding a preparation can become more valuable after neighboring preparations are already selected because more candidate witness edges become complete.

The general optimization problem is NP-hard. With unit costs and unit edge weights, the decision question of whether one can obtain value \(\binom{k}{2}\) using budget \(k\) is equivalent to asking whether the graph contains a \(k\)-clique.

P46 also gives a computable upper bound. If

\[
d_i=\sum_{j:\{i,j\}\in E}w_{ij}
\]

is the full weighted degree, then every feasible set satisfies

\[
\boxed{
2F(S)\le\sum_{i\in S}d_i.
}
\]

Relaxing the resulting degree-weighted 0-1 knapsack to fractional vertex selection gives

\[
\boxed{
F^*(B)
\le
U_{\rm deg}(B)
:=
\min\left\{
\sum_{e\in E}w_e,
\frac12K_{\rm frac}(B)
\right\}.
}
\]

Therefore any feasible design \(S\) has the certified optimality interval

\[
\boxed{
F(S)\le F^*(B)\le U_{\rm deg}(B),
}
\]

and

\[
\boxed{
F^*(B)-F(S)
\le
U_{\rm deg}(B)-F(S).
}
\]

For small graphs the repository implementation enumerates every budget-feasible subset and returns the exact optimum together with the independent degree-relaxation cross-check.

The design pipeline is now

\[
\boxed{
\text{hard budget}
\longrightarrow
\text{P46 preparation subset}
\longrightarrow
\text{induced witness graph}
\longrightarrow
\text{P45 continuous precision allocation}.
}
\]

The scientific boundary remains strict. P46 is an experimental resource-selection theorem. It does not establish that a selected witness is physically real, that a quantum descriptor is complete, that quantum mechanics is incomplete, or that the independently defined target is consciousness.

[Read Proposition 46](docs/proposition_46_budget_constrained_witness_graph.md). The [P46 theorem map](docs/figures/p46_budget_constrained_witness_graph.svg), [implementation](src/consciousness_bridge/budget_constrained_witness_graph.py), and [tests](tests/test_budget_constrained_witness_graph.py) expose the proof-to-code path.

'''
replace_once(
    readme,
    "---\n\n# 14. Observer-to-bridge handoff",
    p46_section + "---\n\n# 14. Observer-to-bridge handoff",
    "README P46 theorem section",
)

roadmap = ROOT / "docs" / "theorem_roadmap.md"
replace_once(
    roadmap,
    "![P45 shared-preparation graph allocation](figures/p45_shared_preparation_graph_allocation.svg)\n",
    "![P45 shared-preparation graph allocation](figures/p45_shared_preparation_graph_allocation.svg)\n\n![P46 budget-constrained witness graph](figures/p46_budget_constrained_witness_graph.svg)\n",
    "roadmap P46 figure",
)
replace_once(
    roadmap,
    "| [P45](proposition_45_shared_preparation_graph_allocation.md) | strictly convex shared-vertex allocation plus incidence-weighted KKT conditions | unique preparation-level sample design for overlapping candidate witness pairs | proved resource-allocation theorem |",
    "| [P45](proposition_45_shared_preparation_graph_allocation.md) | strictly convex shared-vertex allocation plus incidence-weighted KKT conditions | unique preparation-level sample design for overlapping candidate witness pairs | proved resource-allocation theorem |\n| [P46](proposition_46_budget_constrained_witness_graph.md) | monotone supermodular induced-edge objective, CLIQUE reduction, and fractional degree-knapsack bound | hard-budget preparation selection with certified optimality gap | proved combinatorial design theorem |",
    "roadmap P46 index row",
)
roadmap_add = r'''

---

# 21. P46 budget-constrained witness-graph selection

P45 optimizes continuous preparation-level precision on a fixed candidate graph. P46 asks which preparations should be measured when a hard budget prevents full graph coverage.

For selected preparations \(S\),

\[
F(S)=\sum_{\{i,j\}\in E}w_{ij}\mathbf 1\{i,j\in S\}.
\]

P46 proves that \(F\) is monotone and supermodular, and that maximizing \(F\) subject to \(\sum_{i\in S}c_i\le B\) is NP-hard even for unit costs and unit weights. The reduction is from CLIQUE.

The full weighted degree

\[
d_i=\sum_{j:\{i,j\}\in E}w_{ij}
\]

gives

\[
2F(S)\le\sum_{i\in S}d_i.
\]

A fractional knapsack relaxation therefore gives the certified upper bound

\[
F^*(B)\le U_{\rm deg}(B).
\]

Together with any feasible design value \(F(S)\), this yields an explicit a posteriori optimality-gap certificate. Small instances are solved exactly by subset enumeration in the reference implementation.

P46 remains a discrete experimental-design theorem and makes no ontological claim about quantum mechanics or consciousness.
'''
text = roadmap.read_text(encoding="utf-8")
if "# 21. P46 budget-constrained witness-graph selection" in text:
    raise RuntimeError("roadmap P46 section already exists")
roadmap.write_text(text.rstrip() + roadmap_add + "\n", encoding="utf-8")

nav = ROOT / "docs" / "research_navigation.md"
replace_once(
    nav,
    "P1 through P45",
    "P1 through P46",
    "navigation theorem count",
)
replace_once(
    nav,
    "| P45 | [Shared-preparation graph allocation](proposition_45_shared_preparation_graph_allocation.md) | shared preparation-level precision allocation for overlapping candidate witness edges |",
    "| P45 | [Shared-preparation graph allocation](proposition_45_shared_preparation_graph_allocation.md) | shared preparation-level precision allocation for overlapping candidate witness edges |\n| P46 | [Budget-constrained witness graph](proposition_46_budget_constrained_witness_graph.md) | discrete preparation selection, NP-hardness, relaxation upper bound, and exact small-instance certification |",
    "navigation P46 row",
)

citation_map = ROOT / "docs" / "equation_and_citation_map.md"
p46_citations = r'''

---

# 35. P46 budget-constrained witness graph

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(F(S)=\sum_{\{i,j\}\in E}w_{ij}\mathbf 1\{i,j\in S\}\) | total value of candidate witness edges induced by measured preparations | repository definition | [P46](proposition_46_budget_constrained_witness_graph.md) |
| monotonicity and supermodularity of \(F\) | formalizes preparation complementarity | proved from nonnegative edge weights | [P46](proposition_46_budget_constrained_witness_graph.md) |
| unit-cost, unit-weight threshold \(\binom{k}{2}\) | reduction from CLIQUE | proves NP-hardness of optimization and NP-completeness of decision form | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(2F(S)\le\sum_{i\in S}d_i\) | weighted-degree relaxation | proved by comparing internal and full weighted degrees | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(F^*(B)\le U_{\rm deg}(B)\) | fractional degree-knapsack upper bound | proved relaxation bound | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(F^*(B)-F(S)\le U_{\rm deg}(B)-F(S)\) | a posteriori optimality-gap certificate | proved | [P46](proposition_46_budget_constrained_witness_graph.md) |

P46 is a combinatorial experimental-design result. Its graph weights are declared design values, not consciousness scores or evidence of quantum incompleteness.
'''
text = citation_map.read_text(encoding="utf-8")
if "# 35. P46 budget-constrained witness graph" in text:
    raise RuntimeError("citation map P46 section already exists")
citation_map.write_text(text.rstrip() + p46_citations + "\n", encoding="utf-8")

pyproject = ROOT / "pyproject.toml"
replace_once(pyproject, 'version = "0.45.0"', 'version = "0.46.0"', "pyproject version")

citation = ROOT / "CITATION.cff"
replace_once(citation, "version: 0.45.0", "version: 0.46.0", "citation version")
replace_once(
    citation,
    "shared-preparation graph allocation",
    "shared-preparation graph allocation, budget-constrained witness-graph selection",
    "citation P46 abstract",
)

changelog = ROOT / "CHANGELOG.md"
text = changelog.read_text(encoding="utf-8")
entry = """# 0.46.0 - 2026-09-10\n\n- Add P46 budget-constrained witness-graph selection.\n- Prove monotonicity and supermodularity of the induced-edge design value.\n- Prove NP-hardness by reduction from CLIQUE, even for unit costs and weights.\n- Add a fractional weighted-degree knapsack upper bound and certified optimality gap.\n- Add exact small-instance enumeration, theorem map, proof documentation, and regression tests.\n- Preserve the explicit boundary that this is an experimental-design theorem, not evidence of quantum incompleteness or consciousness.\n\n"""
if text.startswith("# 0.46.0"):
    raise RuntimeError("changelog already contains 0.46.0")
changelog.write_text(entry + text, encoding="utf-8")

release_test = ROOT / "tests" / "test_release_metadata_consistency.py"
replace_all(release_test, "0.45.0", "0.46.0", 3, "release test version")
replace_once(
    release_test,
    '        "test_shared_preparation_graph_allocation.py",\n',
    '        "test_shared_preparation_graph_allocation.py",\n        "Proposition 46",\n        "p46_budget_constrained_witness_graph.svg",\n        "budget_constrained_witness_graph.py",\n        "test_budget_constrained_witness_graph.py",\n',
    "release test P46 tokens",
)

main_page_test = ROOT / "tests" / "test_main_page_visual_paper.py"
replace_once(
    main_page_test,
    '    "p45_shared_preparation_graph_allocation.svg",\n',
    '    "p45_shared_preparation_graph_allocation.svg",\n    "p46_budget_constrained_witness_graph.svg",\n',
    "main page P46 figure",
)
replace_once(
    main_page_test,
    "for index in range(1, 46):",
    "for index in range(1, 47):",
    "main page proposition range",
)

for path in (readme, roadmap, nav, citation_map, pyproject, citation, changelog, release_test, main_page_test):
    text = path.read_text(encoding="utf-8")
    if "\u2013" in text or "\u2014" in text:
        raise RuntimeError(f"forbidden dash character in {path}")

print("P46 release integration complete")
