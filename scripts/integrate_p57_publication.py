from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P57 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P57 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.30 P57 - switching-metric perturbation reoptimization stability" in text:
        return

    text = replace_once(text, "version-0.56.0-2563eb", "version-0.57.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **56 proposition-level results",
        "The public research record now contains **57 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P56", "P1 through P57")

    p56 = (
        "**P56** removes the fixed-start restriction: the optimal metric route is 1-Lipschitz "
        "in the setup origin, so moving the apparatus from s to s' can erode a P55 saving by "
        "at most the metric displacement c(s,s')."
    )
    p57 = (
        p56
        + " **P57** removes the fixed-metric restriction: if two declared switching metrics "
        "differ uniformly by at most delta, the exact P54 route optimum changes by at most "
        "q(S;s) delta, and this sharp perturbation term composes with P55 residual release and "
        "P56 setup motion into one strict-decrease certificate."
    )
    text = replace_once(text, p56, p57, "README abstract P56 sentence")

    text = insert_after_line(
        text,
        "[Proposition 56](docs/proposition_56_moving_start_metric_reoptimization_stability.md)",
        "| switching-metric perturbation stability | [Proposition 57](docs/proposition_57_switching_metric_perturbation.md) | sharp sup-norm metric-drift bound, combined residual/start/geometry certificate, and old-route reuse bound |",
        "README proposition navigation",
    )

    section = r'''
## 13.30 P57 - switching-metric perturbation reoptimization stability

![P57 switching-metric perturbation stability](docs/figures/p57_switching_metric_perturbation.svg)

P56 controls movement of the current apparatus setup while holding one metric switching geometry fixed. P57 removes that fixed-metric restriction and asks how much the exact P54 optimum can change when the transition geometry itself changes between sequential reoptimization steps.

Let \(c\) and \(c'\) be two declared finite metrics on the relevant preparation and setup points. Define their uniform separation

\[
\boxed{
\delta
=
\max_{x,y}|c(x,y)-c'(x,y)|.
}
\]

For active support \(S\), define the number of nontrivial route edges

\[
\boxed{
q(S;s)
=
\begin{cases}
|S|-1,&s\text{ absent or }s\in S,\\
|S|,&s\notin S.
\end{cases}
}
\]

P57 proves the sharp deterministic stability bound

\[
\boxed{
|L_c^*(S;s)-L_{c'}^*(S;s)|
\le
q(S;s)\,\delta.
}
\]

The coefficient is tight: adding the same positive perturbation to every off-diagonal distance of a metric can increase every nontrivial route edge by exactly that amount.

P57 then composes all three changes that can occur during sequential experimental reoptimization. For \(r'\le r\), define the P55 release under the old geometry

\[
\Delta_{\rm fixed}
=
C_c^*(r;s)-C_c^*(r';s)\ge0.
\]

With \(S'=S(r')\), the joint start-and-metric perturbation penalty is

\[
\boxed{
P_{57}
=
\min\left\{
c(s,s')+q(S';s')\delta,
q(S';s)\delta+c'(s,s')
\right\}.
}
\]

Therefore

\[
\boxed{
C_c^*(r;s)-C_{c'}^*(r';s')
\ge
\Delta_{\rm fixed}-P_{57}.
}
\]

A directly checkable strict-improvement certificate follows:

\[
\boxed{
\Delta_{\rm fixed}>P_{57}
\Longrightarrow
C_{c'}^*(r';s')<C_c^*(r;s).
}
\]

P57 also gives a tighter instance-specific bound by taking the old optimal route and evaluating that exact order under the new metric and start. Since the new optimum cannot cost more than any feasible reused route, this route-reuse certificate can be much sharper than the worst-case \(q\delta\) envelope.

The deterministic scheduling chain is now

\[
\boxed{
\text{P53 residual demand}
\to
\text{P54 metric scheduling}
\to
\text{P55 support release}
\to
\text{P56 start motion}
\to
\text{P57 metric drift}.
}
\]

The scientific boundary remains strict. P57 assumes two valid declared metrics. It does not estimate a metric from noisy data, justify pruning, establish sequential minimaxity, imply hidden physics, identify any scheduling quantity with consciousness, or claim that quantum mechanics is incomplete.

[Read Proposition 57](docs/proposition_57_switching_metric_perturbation.md). The [P57 theorem map](docs/figures/p57_switching_metric_perturbation.svg), [implementation](src/consciousness_bridge/switching_metric_perturbation.py), and [tests](tests/test_switching_metric_perturbation.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P57 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P57](proposition_57_switching_metric_perturbation.md)" in text:
        return
    text = insert_after_line(
        text,
        "p56_moving_start_metric_reoptimization_stability.svg",
        "![P57 switching-metric perturbation stability](figures/p57_switching_metric_perturbation.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P56](proposition_56_moving_start_metric_reoptimization_stability.md)",
        "| [P57](proposition_57_switching_metric_perturbation.md) | uniform finite-metric perturbation, route reuse, and P55-P56 composition | sharp q-delta route stability plus residual/start/geometry reoptimization certificate | proved deterministic perturbation theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P57 | [Switching-metric perturbation stability]" in text:
        return
    text = text.replace("P1 through P56", "P1 through P57")
    text = insert_after_line(
        text,
        "| P56 | [Moving-start metric reoptimization stability]",
        "| P57 | [Switching-metric perturbation stability](proposition_57_switching_metric_perturbation.md) | sharp sup-norm metric-drift control, combined residual/start/metric strict-decrease certificate, and route-reuse upper bound |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 46. P57 switching-metric perturbation stability" in text:
        return
    addition = r'''

---

# 46. P57 switching-metric perturbation stability

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\delta=\max_{x,y}|c(x,y)-c'(x,y)|\) | common-point sup distance between two declared finite switching metrics | repository definition | [P57](proposition_57_switching_metric_perturbation.md) |
| \(q(S;s)\in\{|S|-1,|S|\}\) | exact maximum number of nontrivial metric edges required by the rooted P54 route | repository definition with metric shortcut justification | [P57](proposition_57_switching_metric_perturbation.md) |
| \(|L_c^*(S;s)-L_{c'}^*(S;s)|\le q(S;s)\delta\) | stability of the exact switching optimum under metric drift | proved sharp perturbation theorem | [P57](proposition_57_switching_metric_perturbation.md) |
| \(P_{57}=\min\{c(s,s')+q(S';s')\delta,\ q(S';s)\delta+c'(s,s')\}\) | combined start-motion and metric-drift penalty | proved by two valid perturbation orders | [P57](proposition_57_switching_metric_perturbation.md) |
| \(C_c^*(r;s)-C_{c'}^*(r';s')\ge\Delta_{\rm fixed}-P_{57}\) | full residual/start/metric reoptimization lower bound | proved P55-P56-P57 composition | [P57](proposition_57_switching_metric_perturbation.md) |
| \(L_{c'}^*(S;s')\le\ell_{c'}(\pi_c^*;s')\) | old-optimal-route reuse certificate under the new geometry | proved feasibility upper bound | [P57](proposition_57_switching_metric_perturbation.md) |

P57 is a deterministic experimental-scheduling robustness theorem. Uncertain or statistically estimated switching metrics require a separate confidence-set analysis.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.56.0"', 'version = "0.57.0"', "pyproject version")
    text = replace_once(
        text,
        "moving-start metric reoptimization stability, robust experiment design",
        "moving-start metric reoptimization stability, switching-metric perturbation stability, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.56.0", "version: 0.57.0", "citation version")
    text = replace_once(
        text,
        "moving-start metric reoptimization stability, robust experiment design",
        "moving-start metric reoptimization stability, switching-metric perturbation stability, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.57.0 - 2026-09-10"):
        entry = """# 0.57.0 - 2026-09-10

- Add P57 switching-metric perturbation reoptimization stability.
- Prove the exact P54 route optimum is sharply q-Lipschitz under sup-norm perturbations of the declared finite metric.
- Compose P55 residual release, P56 setup motion, and P57 metric drift into one deterministic lower bound and strict-decrease certificate.
- Add a tighter instance-specific old-route reuse upper bound.
- Make the known-metric boundary explicit and identify finite-data metric uncertainty as the next theorem target.
- Add implementation, tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p56_moving_start_metric_reoptimization_stability.svg",',
        '    "p56_moving_start_metric_reoptimization_stability.svg",\n    "p57_switching_metric_perturbation.svg",',
        "main-page P57 figure guard",
    )
    text = text.replace("for index in range(1, 57):", "for index in range(1, 58):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.56.0-2563eb", "version-0.57.0-2563eb")
    text = text.replace('version = "0\\.56\\.0"', 'version = "0\\.57\\.0"')
    text = text.replace("version: 0\\.56\\.0", "version: 0\\.57\\.0")
    marker = (
        '        "Proposition 56",\n'
        '        "p56_moving_start_metric_reoptimization_stability.svg",\n'
        '        "moving_start_metric_reoptimization.py",\n'
        '        "test_moving_start_metric_reoptimization.py",\n'
    )
    replacement = marker + (
        '        "Proposition 57",\n'
        '        "p57_switching_metric_perturbation.svg",\n'
        '        "switching_metric_perturbation.py",\n'
        '        "test_switching_metric_perturbation.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P57 path guards")
    write(path, text)

    write(
        "tests/test_switching_metric_perturbation_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p57_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P57 - switching-metric perturbation reoptimization stability",\n        "p57_switching_metric_perturbation.svg",\n        "switching_metric_perturbation.py",\n        "test_switching_metric_perturbation.py",\n    ):\n        assert token in text\n\n\ndef test_p57_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P57](proposition_57_switching_metric_perturbation.md)" in roadmap\n    assert "| P57 | [Switching-metric perturbation stability]" in navigation\n    assert "# 46. P57 switching-metric perturbation stability" in equations\n''',
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
