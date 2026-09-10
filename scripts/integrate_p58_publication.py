from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P58 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P58 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.31 P58 - finite-data switching-metric uncertainty" in text:
        return

    text = replace_once(text, "version-0.57.0-2563eb", "version-0.58.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **57 proposition-level results, 58 equation-driven quantitative figures",
        "The public research record now contains **58 proposition-level results, 59 equation-driven quantitative figures",
        "README proposition/figure count",
    )
    text = text.replace("P1 through P57", "P1 through P58")

    p57 = (
        "**P57** removes the fixed-metric restriction: if two declared switching metrics differ uniformly by at most delta, "
        "the exact P54 route optimum changes by at most q(S;s) delta, and this sharp perturbation term composes with P55 residual release "
        "and P56 setup motion into one strict-decrease certificate."
    )
    p58 = (
        p57
        + " **P58** removes the known-metric restriction: bounded noisy pairwise transition measurements generate simultaneous edge-confidence intervals, "
        "whose lower and upper route envelopes bracket the unknown true P54 optimum without requiring the empirical center itself to satisfy the triangle inequality. "
        "The upper-envelope minimizer is a robust route, and the envelope width certifies its worst-case regret on the shared confidence event."
    )
    text = replace_once(text, p57, p58, "README abstract P57 sentence")

    text = insert_after_line(
        text,
        "[Proposition 57](docs/proposition_57_switching_metric_perturbation.md)",
        "| finite-data switching-metric uncertainty | [Proposition 58](docs/proposition_58_finite_data_metric_uncertainty.md) | simultaneous pairwise confidence envelopes, robust route optimization, route-regret control, and robust old/new cost comparison |",
        "README proposition navigation",
    )

    section = r'''
## 13.31 P58 - finite-data switching-metric uncertainty

![P58 finite-data switching-metric uncertainty](docs/figures/p58_finite_data_metric_uncertainty.svg)

P57 treats the transition geometry as known. P58 moves the scheduling chain into a finite-data setting where the unknown true switching cost is a metric but its pairwise entries are measured with noise.

For every unordered transition pair \(e\), let \(\widehat c_e\) be a sample mean based on \(n_e\) bounded observations with range width \(B_e\). Allocate pairwise failure probabilities \(\alpha_e\) with \(\sum_e\alpha_e\le\alpha\), and define

\[
\boxed{
\rho_e
=
B_e\sqrt{\frac{1}{2n_e}\log\frac{2}{\alpha_e}}.
}
\]

Hoeffding concentration plus a finite-family union bound gives the simultaneous event

\[
\boxed{
|\widehat c_e-c_e|\le\rho_e
\quad\forall e
}
\]

with probability at least \(1-\alpha\).

A central methodological point is that the empirical table \(\widehat c\) is **not required to be a metric**. Sampling noise may violate triangle inequalities even when the unknown physical transition cost \(c\) is metric. P58 therefore avoids an unjustified projection step and works directly with pairwise confidence intervals.

Define edgewise envelopes

\[
\underline c_e=\max\{0,\widehat c_e-\rho_e\},
\qquad
\overline c_e=\widehat c_e+\rho_e.
\]

For every candidate block route \(\pi\), these induce route envelopes \(\underline\ell(\pi;s)\) and \(\overline\ell(\pi;s)\). Their exact Held-Karp minima are

\[
\boxed{
L^-(S;s)=\min_\pi\underline\ell(\pi;s),
\qquad
L^+(S;s)=\min_\pi\overline\ell(\pi;s).
}
\]

On the simultaneous confidence event,

\[
\boxed{
L^-(S;s)
\le
L_c^*(S;s)
\le
L^+(S;s).
}
\]

Adding the deterministic acquisition term gives a complete finite-data interval for the unknown true residual execution cost.

P58 also defines the robust route

\[
\boxed{
\pi^{\rm rob}\in\arg\min_\pi\overline\ell(\pi;s)
}
\]

and proves

\[
\boxed{
0\le
\ell_c(\pi^{\rm rob};s)-L_c^*(S;s)
\le
L^+(S;s)-L^-(S;s).
}
\]

Thus the route-envelope width is not merely an uncertainty bar. It is a certified upper bound on the regret of executing the robust route instead of the unknown true optimum.

For two sequential states with simultaneous total-cost intervals \([C_0^-,C_0^+]\) and \([C_1^-,C_1^+]\), P58 gives the direct strict-improvement certificate

\[
\boxed{
C_0^->C_1^+
\Longrightarrow
C_{c_0}^*(r_0;s_0)>C_{c_1}^*(r_1;s_1).
}
\]

Under a common pairwise confidence radius \(\eta\), the rectangular route interval satisfies

\[
\boxed{
L^+-L^-
\le
2q_{\rm rect}\eta.
}
\]

With equal pairwise sample counts \(n\), common observation range width \(B\), \(M\) calibrated unordered pairs, and equal error spending, a sufficient condition for route-interval width at most \(\varepsilon\) is

\[
\boxed{
n
\ge
\frac{2B^2q_{\rm rect}^2}{\varepsilon^2}
\log\frac{2M}{\alpha}.
}
\]

This is a transparent sufficient calibration law, not a minimax lower bound.

The sequential experimental-scheduling chain is now

\[
\boxed{
\text{P53 residual demand}
\to
\text{P54 exact metric scheduling}
\to
\text{P55 support release}
\to
\text{P56 start motion}
\to
\text{P57 deterministic metric drift}
\to
\text{P58 finite-data metric uncertainty}.
}
\]

The scientific boundary remains explicit. P58 is a finite-data experimental scheduling theorem. It does not infer an experiential variable from route geometry, does not validate pruning by itself, does not prove minimax adaptive calibration, and does not claim that quantum mechanics is incomplete.

[Read Proposition 58](docs/proposition_58_finite_data_metric_uncertainty.md). The [P58 theorem map](docs/figures/p58_finite_data_metric_uncertainty.svg), [implementation](src/consciousness_bridge/finite_data_metric_uncertainty.py), and [tests](tests/test_finite_data_metric_uncertainty.py) provide the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P58 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P58](proposition_58_finite_data_metric_uncertainty.md)" in text:
        return
    text = insert_after_line(
        text,
        "![P57 switching-metric perturbation stability]",
        "![P58 finite-data switching-metric uncertainty](figures/p58_finite_data_metric_uncertainty.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P57](proposition_57_switching_metric_perturbation.md)",
        "| [P58](proposition_58_finite_data_metric_uncertainty.md) | pairwise Hoeffding confidence intervals plus exact lower/upper route-envelope dynamic programs | finite-data bracket for the unknown true switching optimum, robust route-regret certificate, and robust old/new comparison | proved finite-data confidence-envelope theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P58 | [Finite-data switching-metric uncertainty]" in text:
        return
    text = text.replace("P1 through P57", "P1 through P58")
    text = insert_after_line(
        text,
        "| P57 | [Switching-metric perturbation stability]",
        "| P58 | [Finite-data switching-metric uncertainty](proposition_58_finite_data_metric_uncertainty.md) | simultaneous pairwise transition confidence intervals, exact robust route envelopes, route-regret bound, and finite-data strict-improvement certificate |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 47. P58 finite-data switching-metric uncertainty" in text:
        return
    addition = r'''

---

# 47. P58 finite-data switching-metric uncertainty

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\rho_e=B_e\sqrt{\log(2/\alpha_e)/(2n_e)}\) | two-sided bounded-mean transition-cost confidence radius | standard Hoeffding consequence under declared pairwise sampling assumptions | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\Pr(|\widehat c_e-c_e|\le\rho_e\ \forall e)\ge1-\alpha\) | simultaneous finite transition-family coverage | finite-family union-bound theorem | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\underline c_e=\max\{0,\widehat c_e-\rho_e\},\ \overline c_e=\widehat c_e+\rho_e\) | rectangular pairwise transition envelope | repository definition | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(L^-=\min_\pi\underline\ell(\pi;s),\ L^+=\min_\pi\overline\ell(\pi;s)\) | exact lower and upper route-envelope optima | repository definition plus Held-Karp computation | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(L^-\le L_c^*\le L^+\) | finite-data confidence bracket for the unknown true P54 switching optimum | proved confidence-envelope theorem | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\ell_c(\pi^{\rm rob};s)-L_c^*\le L^+-L^-\) | robust-route regret certificate | proved deterministic consequence on the shared confidence event | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(C_0^->C_1^+\Rightarrow C_{c_0}^*>C_{c_1}^*\) | robust strict reoptimization comparison | proved interval-separation certificate | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(n\ge 2B^2q_{\rm rect}^2\varepsilon^{-2}\log(2M/\alpha)\) | sufficient common pairwise calibration count for route-envelope width at most \(\varepsilon\) | derived sufficient design inequality, not minimax | [P58](proposition_58_finite_data_metric_uncertainty.md) |

P58 assumes an unknown true metric and a valid finite-data observation model. The empirical center itself need not satisfy the triangle inequality.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.57.0"', 'version = "0.58.0"', "pyproject version")
    text = replace_once(
        text,
        "switching-metric perturbation stability, robust experiment design",
        "switching-metric perturbation stability, finite-data switching-metric uncertainty, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.57.0", "version: 0.58.0", "citation version")
    text = replace_once(
        text,
        "switching-metric perturbation stability, robust experiment design",
        "switching-metric perturbation stability, finite-data switching-metric uncertainty, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.58.0 - 2026-09-10"):
        entry = """# 0.58.0 - 2026-09-10

- Add P58 finite-data switching-metric uncertainty and robust reoptimization.
- Derive simultaneous pairwise Hoeffding confidence intervals for bounded transition-cost observations under finite-family error spending.
- Allow the empirical transition table to be nonmetric while retaining the declared unknown true-metric premise needed by P54.
- Compute exact lower and upper route envelopes over the P54 block-route family using Held-Karp dynamic programming.
- Add a robust upper-envelope route and certify its true-route regret by the envelope width.
- Add robust old/new total-cost interval comparison and a sufficient common-sample calibration law.
- Add implementation, tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p57_switching_metric_perturbation.svg",',
        '    "p57_switching_metric_perturbation.svg",\n    "p58_finite_data_metric_uncertainty.svg",',
        "main-page P58 figure guard",
    )
    text = text.replace("for index in range(1, 58):", "for index in range(1, 59):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.57.0-2563eb", "version-0.58.0-2563eb")
    text = text.replace('version = "0\\.57\\.0"', 'version = "0\\.58\\.0"')
    text = text.replace("version: 0\\.57\\.0", "version: 0\\.58\\.0")
    marker = (
        '        "Proposition 57",\n'
        '        "p57_switching_metric_perturbation.svg",\n'
        '        "switching_metric_perturbation.py",\n'
        '        "test_switching_metric_perturbation.py",\n'
    )
    replacement = marker + (
        '        "Proposition 58",\n'
        '        "p58_finite_data_metric_uncertainty.svg",\n'
        '        "finite_data_metric_uncertainty.py",\n'
        '        "test_finite_data_metric_uncertainty.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P58 path guards")
    write(path, text)

    write(
        "tests/test_finite_data_metric_uncertainty_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p58_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P58 - finite-data switching-metric uncertainty",\n        "p58_finite_data_metric_uncertainty.svg",\n        "finite_data_metric_uncertainty.py",\n        "test_finite_data_metric_uncertainty.py",\n    ):\n        assert token in text\n\n\ndef test_p58_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P58](proposition_58_finite_data_metric_uncertainty.md)" in roadmap\n    assert "| P58 | [Finite-data switching-metric uncertainty]" in navigation\n    assert "# 47. P58 finite-data switching-metric uncertainty" in equations\n''',
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
