from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P54 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_matching_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P54 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.27 P54 - metric switching-cost residual scheduling" in text:
        return

    text = replace_once(text, "version-0.53.0-2563eb", "version-0.54.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **53 proposition-level results",
        "The public research record now contains **54 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P53", "P1 through P54")

    p53_sentence = (
        "**P53** makes that optimum sequential: after additional samples or P47-safe edge pruning, "
        "the residual vertex demands decrease componentwise, and the exact optimal remaining time "
        "decreases by the released total residual demand divided by capacity."
    )
    p54_sentence = (
        p53_sentence
        + " **P54** adds metric preparation-switching costs and proves that an optimal residual "
        "schedule can batch every positive-demand preparation into one contiguous block, reducing "
        "the switching term exactly to a shortest Hamiltonian path problem."
    )
    text = replace_once(text, p53_sentence, p54_sentence, "README abstract P53 sentence")

    p54_row = (
        "| metric switching-cost residual scheduling | "
        "[Proposition 54](docs/proposition_54_metric_switching_cost_residual_scheduling.md) | "
        "metric batching, exact acquisition-routing decomposition, and Held-Karp shortest-path audit |"
    )
    text = insert_after_matching_line(
        text,
        "[Proposition 53](docs/proposition_53_residual_demand_reoptimization.md)",
        p54_row,
        "README proposition navigation",
    )

    section = r'''
## 13.27 P54 - metric switching-cost residual scheduling

![P54 metric switching-cost residual scheduling](docs/figures/p54_metric_switching_cost_residual_scheduling.svg)

P53 gives the exact remaining deterministic sample burden after additional acquisition and valid safe pruning. P54 adds another experimental resource that is invisible to a sample-count-only analysis: the cost of changing the physical preparation or apparatus configuration.

Let

\[
V_+=\{i:r_i>0\}
\]

be the currently positive-demand preparations, let \(a>0\) be deterministic per-sample acquisition cost, and let \(c(u,v)\) be a declared finite metric over the relevant preparation/setup points. For any feasible expanded schedule \(\sigma\),

\[
C_{\rm total}(\sigma)
=
a\sum_i r_i+C_{\rm sw}(\sigma).
\]

The acquisition term is fixed. The nontrivial part is switching.

P54 proves that repeated preparation visits are never required under a metric. Delete every occurrence of a preparation after its first visit. Every resulting shortcut is no longer than the deleted route segment by repeated triangle inequality. Expanding each retained preparation back into one contiguous block adds only zero-cost self transitions. Hence

\[
\boxed{
C_{\rm sw}(\bar\sigma)\le C_{\rm sw}(\sigma).
}
\]

There is therefore always an optimal schedule that visits every member of \(V_+\) exactly once as a block. The exact deterministic optimization becomes

\[
\boxed{
C_{\rm total}^*
=
a\sum_{i\in V_+}r_i
+
L^*(V_+;s),
}
\]

where \(L^*(V_+;s)\) is the shortest Hamiltonian path through the positive-demand preparations, optionally rooted at the current setup \(s\), with no return-to-start requirement.

For exact small-instance auditing, the implementation uses the Held-Karp recurrence

\[
\boxed{
D(S,j)=\min_{k\in S\setminus\{j\}}
\left[D(S\setminus\{j\},k)+c(k,j)\right],
}
\]

with time complexity \(O(m^2 2^m)\) and state complexity \(O(m2^m)\) for \(m=|V_+|\).

The metric assumption is essential. Without triangle inequality, a repeated visit may be a cheaper intermediate route than a direct transition, so the batching theorem and Hamiltonian-path reduction need not hold.

This produces the scheduling chain

\[
\boxed{
\text{P48 local thresholds}
\to
\text{P52 static allocation}
\to
\text{P53 residual reoptimization}
\to
\text{P54 metric switching-cost routing}.
}
\]

P54 is a deterministic scheduling theorem conditional on declared residual demands and a declared metric switching cost. It does not claim that P48 thresholds are statistically minimax, does not independently validate pruning, and makes no ontological claim about consciousness or quantum mechanics.

[Read Proposition 54](docs/proposition_54_metric_switching_cost_residual_scheduling.md). The [P54 theorem map](docs/figures/p54_metric_switching_cost_residual_scheduling.svg), [implementation](src/consciousness_bridge/metric_switching_residual_schedule.py), and [tests](tests/test_metric_switching_residual_schedule.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P54 section boundary")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P54](proposition_54_metric_switching_cost_residual_scheduling.md)" in text:
        return
    text = insert_after_matching_line(
        text,
        "p53_residual_demand_reoptimization.svg",
        "![P54 metric switching-cost residual scheduling](figures/p54_metric_switching_cost_residual_scheduling.svg)",
        "roadmap figure",
    )
    text = insert_after_matching_line(
        text,
        "| [P53](proposition_53_residual_demand_reoptimization.md)",
        "| [P54](proposition_54_metric_switching_cost_residual_scheduling.md) | metric shortcutting plus Hamiltonian-path reduction and Held-Karp recurrence | exact residual execution cost with preparation switching overhead | proved deterministic scheduling theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P54 | [Metric switching-cost residual scheduling]" in text:
        return
    text = text.replace("P1 through P53", "P1 through P54")
    text = insert_after_matching_line(
        text,
        "| P53 | [Residual-demand reoptimization]",
        "| P54 | [Metric switching-cost residual scheduling](proposition_54_metric_switching_cost_residual_scheduling.md) | one-block metric batching, exact acquisition-routing decomposition, and Held-Karp shortest Hamiltonian path audit |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 43. P54 metric switching-cost residual scheduling" in text:
        return
    addition = r'''

---

# 43. P54 metric switching-cost residual scheduling

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C_{\rm total}(\sigma)=a\sum_i r_i+C_{\rm sw}(\sigma)\) | deterministic acquisition and switching-cost decomposition | repository scheduling definition | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(C_{\rm sw}(\bar\sigma)\le C_{\rm sw}(\sigma)\) | first-visit metric batching inequality | proved by repeated triangle inequality | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(C_{\rm total}^*=a\sum_i r_i+L^*(V_+;s)\) | exact optimum after batching | proved Hamiltonian-path reduction | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(D(S,j)=\min_{k\in S\setminus\{j\}}[D(S\setminus\{j\},k)+c(k,j)]\) | exact finite-instance Held-Karp recurrence | standard subset-DP construction applied here | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |

The metric assumption is structural: without triangle inequality the batching inequality and Hamiltonian-path reduction need not hold.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.53.0"', 'version = "0.54.0"', "pyproject version")
    if "metric switching-cost residual scheduling" not in text:
        text = replace_once(
            text,
            "residual-demand reoptimization after safe pruning, robust experiment design",
            "residual-demand reoptimization after safe pruning, metric switching-cost residual scheduling, robust experiment design",
            "pyproject description",
        )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.53.0", "version: 0.54.0", "citation version")
    if "metric switching-cost residual scheduling" not in text:
        text = replace_once(
            text,
            "residual-demand reoptimization after safe pruning, robust experiment design",
            "residual-demand reoptimization after safe pruning, metric switching-cost residual scheduling, robust experiment design",
            "citation abstract",
        )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.54.0 - 2026-09-10"):
        entry = """# 0.54.0 - 2026-09-10

- Add P54 metric switching-cost residual scheduling.
- Prove that repeated preparation visits can be removed without increasing metric switching cost.
- Reduce exact residual execution cost to fixed acquisition burden plus a shortest Hamiltonian path.
- Add a Held-Karp exact solver for small preparation sets.
- Make the triangle-inequality boundary explicit and test zero-demand support reduction.
- Add theorem documentation, publication visual, proof-to-code guards, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p53_residual_demand_reoptimization.svg",',
        '    "p53_residual_demand_reoptimization.svg",\n    "p54_metric_switching_cost_residual_scheduling.svg",',
        "main-page P54 figure guard",
    )
    text = text.replace("for index in range(1, 54):", "for index in range(1, 55):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.53.0-2563eb", "version-0.54.0-2563eb")
    text = text.replace('version = "0\\.53\\.0"', 'version = "0\\.54\\.0"')
    text = text.replace("version: 0\\.53\\.0", "version: 0\\.54\\.0")
    marker = (
        '        "Proposition 53",\n'
        '        "p53_residual_demand_reoptimization.svg",\n'
        '        "residual_demand_reoptimization.py",\n'
        '        "test_residual_demand_reoptimization.py",\n'
    )
    replacement = marker + (
        '        "Proposition 54",\n'
        '        "p54_metric_switching_cost_residual_scheduling.svg",\n'
        '        "metric_switching_residual_schedule.py",\n'
        '        "test_metric_switching_residual_schedule.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P54 path guards")
    write(path, text)

    write(
        "tests/test_metric_switching_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p54_is_visible_on_main_research_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P54 - metric switching-cost residual scheduling",\n        "p54_metric_switching_cost_residual_scheduling.svg",\n        "metric_switching_residual_schedule.py",\n        "test_metric_switching_residual_schedule.py",\n        "**54 proposition-level results",\n    ):\n        assert token in text\n\n\ndef test_p54_is_in_roadmap_navigation_and_equation_map():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P54](proposition_54_metric_switching_cost_residual_scheduling.md)" in roadmap\n    assert "| P54 | [Metric switching-cost residual scheduling]" in navigation\n    assert "# 43. P54 metric switching-cost residual scheduling" in equations\n''',
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
