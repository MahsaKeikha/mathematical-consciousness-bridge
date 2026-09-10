from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def require_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P52 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, contains: str, new_line: str, label: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if contains in line:
            if new_line in lines:
                return text
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P52 line marker: {label}")


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.25 P52 - capacity-optimal service allocation" in text:
        return

    text = require_replace(
        text,
        "version-0.51.0-2563eb",
        "version-0.52.0-2563eb",
        "README version",
    )
    p51 = (
        "**P51** sharpens the common starvation factor into preparation-specific "
        "finite-window service guarantees, producing an exact endpoint bottleneck "
        "time and instance-dependent positive/all-negative global stopping bounds."
    )
    p52 = (
        p51
        + " **P52** then solves the downstream capacity-allocation problem exactly: "
        "once finite local demands are declared, the unique minimax continuous "
        "service shares are proportional to those demands, with a matching exact "
        "unit-capacity discrete quota bound."
    )
    text = require_replace(text, p51, p52, "README abstract P51 sentence")
    text = require_replace(
        text,
        "The public research record now contains **51 proposition-level results",
        "The public research record now contains **52 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P51", "P1 through P52")

    p51_nav = "| heterogeneous finite-window service-rate stopping | [Proposition 51](docs/proposition_51_heterogeneous_service_rate_stopping.md) | preparation-specific service windows and quotas with endpoint-bottleneck global stopping bounds |"
    p52_nav = "| capacity-optimal service allocation | [Proposition 52](docs/proposition_52_capacity_optimal_service_allocation.md) | exact minimax service shares for finite vertex demands, capacity lower bound, uniqueness, and discrete quota optimality |"
    lines = text.splitlines()
    if p51_nav not in lines:
        for index, line in enumerate(lines):
            if "[Proposition 50](docs/proposition_50_bounded_starvation_asynchronous_sampling.md)" in line:
                lines.insert(index + 1, p51_nav)
                break
        else:
            raise RuntimeError("missing P52 line marker: README P50 proposition navigation")
    if p52_nav not in lines:
        p51_index = lines.index(p51_nav)
        lines.insert(p51_index + 1, p52_nav)
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    section = r'''
## 13.25 P52 - capacity-optimal service allocation

![P52 capacity-optimal service allocation](docs/figures/p52_capacity_optimal_service_allocation.svg)

P51 converts local sample thresholds into global-time guarantees once finite-window service rates are specified. P52 asks the inverse design question: **how should a fixed total sampling capacity be divided among preparations so the complete declared threshold task finishes as early as possible in the worst case?**

For a finite witness graph, let P48 supply a finite threshold \(N_e\) for every edge. The componentwise-minimal preparation demand sufficient to place every incident edge above threshold is

\[
\boxed{
d_i=\max\{N_e:e\ni i\},
}
\]

with \(d_i=0\) for isolated vertices.

Let \(C>0\) be total preparation-level sampling capacity and let \(\pi_i\ge0\) be the continuous service share assigned to preparation \(i\), subject to

\[
\sum_i\pi_i\le C.
\]

The deterministic threshold-saturation time is

\[
\boxed{
T(\pi)=\max_{i:d_i>0}\frac{d_i}{\pi_i}.
}
\]

For every feasible allocation with finite completion time \(T\), the inequalities \(d_i\le T\pi_i\) imply

\[
\sum_i d_i\le T\sum_i\pi_i\le TC.
\]

Therefore every policy obeys the capacity lower bound

\[
\boxed{
T(\pi)\ge\frac{\sum_i d_i}{C}.
}
\]

P52 then exhibits an allocation that attains the bound exactly:

\[
\boxed{
\pi_i^*=C\frac{d_i}{\sum_jd_j}.
}
\]

Every positive-demand preparation has the same completion bottleneck,

\[
\frac{d_i}{\pi_i^*}
=
\frac{\sum_jd_j}{C},
\]

so

\[
\boxed{
T^*=\frac{\sum_i d_i}{C}.
}
\]

The optimum is unique on the positive-demand support: any allocation attaining the same makespan must satisfy \(\pi_i\ge C d_i/\sum_jd_j\) for every required preparation, and capacity feasibility forces equality for all of them.

For integer demands under unit global capacity, the discrete result is exact as well. Any schedule needs at least \(\sum_i d_i\) rounds because each round contributes at most one sample toward the total outstanding demand. Selecting each preparation exactly \(d_i\) times attains that lower bound, giving

\[
\boxed{
T_{\rm discrete}^*=\sum_i d_i.
}
\]

This closes a clean optimization loop:

\[
\boxed{
\text{P48 local thresholds}
\to
\text{P50-P51 global service guarantees}
\to
\text{P52 capacity-optimal service shares}.
}
\]

P52 is an exact threshold-scheduling theorem. It does **not** claim that the conservative P48 thresholds are minimax statistical sample complexities, and it does not claim that proportional service minimizes every realized data-dependent stopping time. It also makes no ontological claim about quantum mechanics or consciousness.

[Read Proposition 52](docs/proposition_52_capacity_optimal_service_allocation.md). The [P52 theorem map](docs/figures/p52_capacity_optimal_service_allocation.svg), [implementation](src/consciousness_bridge/capacity_optimal_service_allocation.py), and [tests](tests/test_capacity_optimal_service_allocation.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = require_replace(text, marker, section + marker, "README P52 section")
    write("README.md", text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P52](proposition_52_capacity_optimal_service_allocation.md)" in text:
        return
    text = insert_after_line(
        text,
        "p51_heterogeneous_service_rate_stopping.svg",
        "![P52 capacity-optimal service allocation](figures/p52_capacity_optimal_service_allocation.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P51](proposition_51_heterogeneous_service_rate_stopping.md)",
        "| [P52](proposition_52_capacity_optimal_service_allocation.md) | capacity-conservation lower bound plus proportional-demand minimax construction | unique capacity-optimal service shares and exact unit-capacity quota completion | proved deterministic scheduling theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P52 | [Capacity-optimal service allocation]" in text:
        return
    text = text.replace("P1 through P51", "P1 through P52")
    text = insert_after_line(
        text,
        "| P51 | [Heterogeneous finite-window service-rate stopping]",
        "| P52 | [Capacity-optimal service allocation](proposition_52_capacity_optimal_service_allocation.md) | exact proportional-demand minimax service shares, capacity lower bound, uniqueness, and discrete quota optimum |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 41. P52 capacity-optimal service allocation" in text:
        return
    addition = r'''

---

# 41. P52 capacity-optimal service allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(d_i=\max\{N_e:e\ni i\}\) | componentwise-minimal vertex demand sufficient for all incident P48 thresholds | proved threshold reduction | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T(\pi)=\max_i d_i/\pi_i\) | continuous capacity-constrained threshold makespan | repository optimization definition | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T\ge(\sum_i d_i)/C\) | universal capacity lower bound | proved by summing \(d_i\le T\pi_i\) | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(\pi_i^*=C d_i/\sum_jd_j\) | unique minimax service allocation on positive demand support | proved exact optimum | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T^*=(\sum_i d_i)/C\) | exact optimal continuous completion time | proved by lower-bound attainment | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T_{\rm discrete}^*=\sum_i d_i\) for unit capacity | exact integer quota-saturation length | proved counting lower bound plus construction | [P52](proposition_52_capacity_optimal_service_allocation.md) |

P52 optimizes deterministic saturation of declared sufficient thresholds; it is not an information-theoretic lower bound on the underlying statistical problem.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = require_replace(text, 'version = "0.51.0"', 'version = "0.52.0"', "pyproject version")
    text = require_replace(
        text,
        "heterogeneous finite-window service-rate stopping, robust experiment design",
        "heterogeneous finite-window service-rate stopping, capacity-optimal service allocation, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = require_replace(text, "version: 0.51.0", "version: 0.52.0", "citation version")
    text = require_replace(
        text,
        "heterogeneous finite-window service-rate stopping, robust experiment design",
        "heterogeneous finite-window service-rate stopping, capacity-optimal service allocation, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.52.0 - 2026-09-10"):
        entry = """# 0.52.0 - 2026-09-10

- Add P52 capacity-optimal service allocation for finite witness-graph threshold demands.
- Reduce edge thresholds to the componentwise-minimal vertex demand vector.
- Prove the universal capacity-conservation lower bound.
- Prove the unique proportional-demand minimax continuous service allocation.
- Prove the exact unit-capacity integer quota-saturation optimum.
- Add implementation, regression tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = require_replace(
        text,
        '    "p51_heterogeneous_service_rate_stopping.svg",',
        '    "p51_heterogeneous_service_rate_stopping.svg",\n    "p52_capacity_optimal_service_allocation.svg",',
        "main-page figure guard",
    )
    text = text.replace("for index in range(1, 52):", "for index in range(1, 53):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.51.0-2563eb", "version-0.52.0-2563eb")
    text = text.replace('version = "0\\.51\\.0"', 'version = "0\\.52\\.0"')
    text = text.replace("version: 0\\.51\\.0", "version: 0\\.52\\.0")
    marker = (
        '        "Proposition 51",\n'
        '        "p51_heterogeneous_service_rate_stopping.svg",\n'
        '        "heterogeneous_service_stopping.py",\n'
        '        "test_heterogeneous_service_stopping.py",\n'
    )
    replacement = marker + (
        '        "Proposition 52",\n'
        '        "p52_capacity_optimal_service_allocation.svg",\n'
        '        "capacity_optimal_service_allocation.py",\n'
        '        "test_capacity_optimal_service_allocation.py",\n'
    )
    text = require_replace(text, marker, replacement, "release P52 path guards")
    write(path, text)

    write(
        "tests/test_capacity_optimal_service_allocation_documentation.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_52_capacity_optimal_service_allocation.md"\nFIGURE = ROOT / "docs" / "figures" / "p52_capacity_optimal_service_allocation.svg"\n\n\ndef test_p52_documentation_exposes_exact_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 52A",\n        "Proposition 52B",\n        "Proposition 52C",\n        "Exact discrete unit-capacity result",\n        "Scientific boundary",\n    ):\n        assert phrase in text\n\n\ndef test_p52_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "p52_capacity_optimal_service_allocation.svg",\n        "capacity_optimal_service_allocation.py",\n        "test_capacity_optimal_service_allocation.py",\n        "P52 - capacity-optimal service allocation",\n    ):\n        assert token in readme\n''',
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
