from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P53 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, marker: str, line: str, label: str) -> str:
    lines = text.splitlines()
    if line in lines:
        return text
    for index, current in enumerate(lines):
        if marker in current:
            lines.insert(index + 1, line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P53 line marker: {label}")


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.26 P53 - residual-demand reoptimization after safe pruning" in text:
        return
    text = replace_once(text, "version-0.52.0-2563eb", "version-0.53.0-2563eb", "README version")
    p52 = (
        "**P52** then solves the downstream capacity-allocation problem exactly: "
        "once finite local demands are declared, the unique minimax continuous "
        "service shares are proportional to those demands, with a matching exact "
        "unit-capacity discrete quota bound."
    )
    p53 = (
        p52
        + " **P53** makes that optimum sequential: after additional samples or "
        "P47-safe edge pruning, the residual vertex demands decrease componentwise, "
        "and the exact optimal remaining time decreases by the released total "
        "residual demand divided by capacity."
    )
    text = replace_once(text, p52, p53, "README P52 abstract")
    text = replace_once(
        text,
        "The public research record now contains **52 proposition-level results",
        "The public research record now contains **53 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P52", "P1 through P53")
    text = insert_after_line(
        text,
        "[Proposition 52](docs/proposition_52_capacity_optimal_service_allocation.md)",
        "| residual-demand reoptimization | [Proposition 53](docs/proposition_53_residual_demand_reoptimization.md) | exact remaining threshold demand after sampling and safe pruning, monotonicity, and released-time identity |",
        "README compact navigation",
    )
    section = r'''
## 13.26 P53 - residual-demand reoptimization after safe pruning

![P53 residual-demand reoptimization](docs/figures/p53_residual_demand_reoptimization.svg)

P52 solves the capacity allocation problem for a fixed vector of local sampling demands. A sequential experiment is not fixed: samples accumulate and P47 may safely remove edges whose upper regularity margin is already certified negative. P53 gives the exact dynamic reoptimization law after either kind of progress.

For active witness graph \(G_t=(V,E_t)\), P48 edge thresholds \(N_e\), and collected local counts \(n_i(t)\), define

\[
\boxed{
r_i(t)=\max_{e\in E_t:e\ni i}(N_e-n_i(t))_+.
}
\]

The total residual burden is

\[
R(t)=\sum_i r_i(t).
\]

Reapplying P52 to the residual vector gives

\[
\boxed{
T_{\rm rem}^*(t)=\frac{R(t)}{C},
\qquad
\pi_i^*(t)=C\frac{r_i(t)}{R(t)}
}
\]

whenever \(R(t)>0\).

Now compare two valid sequential states with

\[
E_b\subseteq E_a,
\qquad
n_i(b)\ge n_i(a)\quad\forall i.
\]

Every retained threshold deficit can only shrink, and the maximum is taken over a subset of the earlier incident-edge family. Therefore

\[
\boxed{
r_i(b)\le r_i(a)\quad\forall i,}
\]

which immediately yields

\[
R(b)\le R(a),
\qquad
T_{\rm rem}^*(b)\le T_{\rm rem}^*(a).
\]

More strongly, because the P52 remaining optimum is exact at both states,

\[
\boxed{
T_{\rm rem}^*(a)-T_{\rm rem}^*(b)
=
\frac{R(a)-R(b)}{C}.
}
\]

This turns safe pruning into a quantitatively auditable scheduling benefit. Removing an edge releases capacity only where that edge contributes to an endpoint's current maximum unsatisfied threshold. A nonbinding edge may disappear with zero immediate service release; a uniquely binding edge can release a strict amount at one or both endpoints.

The statistical and scheduling roles remain separate. P47 supplies the validity of pruning. P53 does not create permission to remove an edge; it computes the deterministic capacity consequence after a valid removal has occurred.

P53 also does not claim that the P48 thresholds are information-theoretically minimal or that residual proportional allocation minimizes every realized random stopping time. It makes no ontological claim about consciousness or quantum theory.

[Read Proposition 53](docs/proposition_53_residual_demand_reoptimization.md). The [P53 theorem map](docs/figures/p53_residual_demand_reoptimization.svg), [implementation](src/consciousness_bridge/residual_demand_reoptimization.py), and [tests](tests/test_residual_demand_reoptimization.py) expose the proof-to-code path.

'''
    text = replace_once(text, "---\n\n# 14. Observer-to-bridge handoff", section + "---\n\n# 14. Observer-to-bridge handoff", "README section insertion")
    write("README.md", text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P53](proposition_53_residual_demand_reoptimization.md)" in text:
        return
    text = insert_after_line(
        text,
        "p52_capacity_optimal_service_allocation.svg",
        "![P53 residual-demand reoptimization](figures/p53_residual_demand_reoptimization.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P52](proposition_52_capacity_optimal_service_allocation.md)",
        "| [P53](proposition_53_residual_demand_reoptimization.md) | residual max-envelope demands plus repeated exact P52 optimization | monotone optimal remaining time and exact capacity release after sampling or P47-safe pruning | proved dynamic scheduling theorem |",
        "roadmap row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P53 | [Residual-demand reoptimization]" in text:
        return
    text = text.replace("P1 through P52", "P1 through P53")
    text = insert_after_line(
        text,
        "| P52 | [Capacity-optimal service allocation]",
        "| P53 | [Residual-demand reoptimization](proposition_53_residual_demand_reoptimization.md) | dynamic P52 reoptimization after sampling and safe edge pruning, with exact released-capacity identity |",
        "navigation row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 42. P53 residual-demand reoptimization" in text:
        return
    addition = r'''

---

# 42. P53 residual-demand reoptimization

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(r_i(t)=\max_{e\in E_t:e\ni i}(N_e-n_i(t))_+\) | componentwise-minimal current vertex demand | proved residual reduction | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(R(t)=\sum_i r_i(t)\) | total residual threshold burden | repository definition | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(T_{\rm rem}^*(t)=R(t)/C\) | exact optimal remaining deterministic completion time | P52 applied to residual demands | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(E_b\subseteq E_a,\ n_i(b)\ge n_i(a)\Rightarrow r_i(b)\le r_i(a)\) | residual monotonicity under sampling and safe pruning | proved max-envelope monotonicity | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(T_{\rm rem}^*(a)-T_{\rm rem}^*(b)=[R(a)-R(b)]/C\) | exact released optimal time | proved identity | [P53](proposition_53_residual_demand_reoptimization.md) |

P53 quantifies deterministic threshold burden after valid pruning; it does not itself justify the statistical pruning decision.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.52.0"', 'version = "0.53.0"', "pyproject version")
    text = replace_once(
        text,
        "capacity-optimal service allocation, robust experiment design",
        "capacity-optimal service allocation, residual-demand reoptimization, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.52.0", "version: 0.53.0", "citation version")
    text = replace_once(
        text,
        "capacity-optimal service allocation, robust experiment design",
        "capacity-optimal service allocation, residual-demand reoptimization, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.53.0 - 2026-09-10"):
        entry = """# 0.53.0 - 2026-09-10

- Add P53 residual-demand reoptimization after additional sampling and P47-safe pruning.
- Define the exact max-envelope residual demand at each preparation.
- Prove componentwise residual monotonicity under nondecreasing counts and edge removal.
- Prove the exact optimal remaining time R(t)/C by dynamic reuse of P52.
- Prove the exact released-time identity [R(a)-R(b)]/C.
- Add sampling-only and pruning-only release accounting, implementation, tests, theorem visual, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p52_capacity_optimal_service_allocation.svg",',
        '    "p52_capacity_optimal_service_allocation.svg",\n    "p53_residual_demand_reoptimization.svg",',
        "main page figure guard",
    )
    text = text.replace("for index in range(1, 53):", "for index in range(1, 54):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.52.0-2563eb", "version-0.53.0-2563eb")
    text = text.replace('version = "0\\.52\\.0"', 'version = "0\\.53\\.0"')
    text = text.replace("version: 0\\.52\\.0", "version: 0\\.53\\.0")
    marker = (
        '        "Proposition 52",\n'
        '        "p52_capacity_optimal_service_allocation.svg",\n'
        '        "capacity_optimal_service_allocation.py",\n'
        '        "test_capacity_optimal_service_allocation.py",\n'
    )
    replacement = marker + (
        '        "Proposition 53",\n'
        '        "p53_residual_demand_reoptimization.svg",\n'
        '        "residual_demand_reoptimization.py",\n'
        '        "test_residual_demand_reoptimization.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P53 guards")
    write(path, text)

    write(
        "tests/test_residual_demand_reoptimization_documentation.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_53_residual_demand_reoptimization.md"\nFIGURE = ROOT / "docs" / "figures" / "p53_residual_demand_reoptimization.svg"\n\n\ndef test_p53_documentation_exposes_core_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 53A",\n        "Proposition 53B",\n        "Proposition 53C",\n        "Pruning-only release",\n        "Dynamic reallocation law",\n        "What P53 does not prove",\n    ):\n        assert phrase in text\n\n\ndef test_p53_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "p53_residual_demand_reoptimization.svg",\n        "residual_demand_reoptimization.py",\n        "test_residual_demand_reoptimization.py",\n        "P53 - residual-demand reoptimization after safe pruning",\n    ):\n        assert token in readme\n''',
    )


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equation_map()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
