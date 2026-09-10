from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P51 publication marker: {label}")
    return text.replace(old, new, 1)


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.24 P51 - heterogeneous finite-window service-rate stopping" in text:
        return

    text = replace_once(text, "version-0.50.0-2563eb", "version-0.51.0-2563eb", "README version")
    p50 = (
        "**P50** converts P48 local thresholds into finite global-round bounds for "
        "asynchronous priority sampling under an explicit bounded-starvation "
        "condition, while proving that no finite global-time guarantee follows from "
        "P47 validity alone if a required preparation can be ignored indefinitely."
    )
    p51 = (
        p50
        + " **P51** sharpens the common starvation factor into preparation-specific "
        "finite-window service guarantees, producing an exact endpoint bottleneck "
        "time and instance-dependent positive/all-negative global stopping bounds."
    )
    text = replace_once(text, p50, p51, "README abstract")
    text = replace_once(
        text,
        "The public research record now contains **50 proposition-level results",
        "The public research record now contains **51 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P50", "P1 through P51")

    section = r'''

## 13.24 P51 - heterogeneous finite-window service-rate stopping

![P51 heterogeneous finite-window service-rate stopping](docs/figures/p51_heterogeneous_service_rate_stopping.svg)

P50 uses one common starvation horizon \(H\). P51 replaces that worst-case factor with a preparation-specific finite-window guarantee

\[
(W_i,q_i),
\qquad
1\le q_i\le W_i,
\]

meaning that preparation \(i\), whenever active throughout any \(W_i\)-round window, is sampled at least \(q_i\) times in that window.

For a preparation active throughout the first \(T\) rounds,

\[
\boxed{
N_i(T)
\ge
q_i\left\lfloor\frac{T}{W_i}\right\rfloor.
}
\]

Therefore \(N\) local samples are guaranteed by

\[
\boxed{
T_i(N)
=
W_i\left\lceil\frac{N}{q_i}\right\rceil.
}
\]

For edge \(e=\{i,j\}\) with P48 threshold \(N_e\), both endpoints must reach that threshold, so the exact service bottleneck bound is

\[
\boxed{
T_e
=
\max\left\{
W_i\left\lceil\frac{N_e}{q_i}\right\rceil,
W_j\left\lceil\frac{N_e}{q_j}\right\rceil
\right\}.
}
\]

If positive-margin edges exist, then on the P47 simultaneous good event

\[
\boxed{
\tau_+
\le
T_+
=
\min_{e:M_e>0}T_e.
}
\]

If every declared edge is strictly negative,

\[
\boxed{
\tau_0
\le
T_-
=
\max_{e\in E}T_e.
}
\]

Both inherit the P47 probability guarantee \(1-\alpha_Y-\alpha_Q\).

P50 is recovered exactly by setting

\[
W_i=H,
\qquad q_i=1,
\]

which gives \(T_i(N)=HN\).

Writing \(\pi_i=q_i/W_i\) is useful for interpretation, but P51 deliberately retains the exact finite-window integer theorem. An asymptotic frequency condition alone can allow arbitrarily long finite starvation intervals and therefore cannot support the same deterministic stopping guarantee.

Dynamic P47 safe pruning remains compatible: once a preparation is no longer active, future windows impose no service obligation on it.

P51 is a scheduling theorem, not an optimality theorem. It does not strengthen the regularity witness into an ontological conclusion and does not establish quantum incompleteness, an extra physical dimension, or consciousness.

[Read Proposition 51](docs/proposition_51_heterogeneous_service_rate_stopping.md). The [P51 theorem map](docs/figures/p51_heterogeneous_service_rate_stopping.svg), [implementation](src/consciousness_bridge/heterogeneous_service_stopping.py), and [tests](tests/test_heterogeneous_service_stopping.py) expose the proof-to-code path.
'''
    marker = "\n---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P51 section")
    write("README.md", text)


def integrate_roadmap() -> None:
    text = read("docs/theorem_roadmap.md")
    if "[P51](proposition_51_heterogeneous_service_rate_stopping.md)" in text:
        return
    visual = "![P50 bounded-starvation asynchronous sampling](figures/p50_bounded_starvation_asynchronous_sampling.svg)"
    text = replace_once(text, visual, visual + "\n\n![P51 heterogeneous finite-window service-rate stopping](figures/p51_heterogeneous_service_rate_stopping.svg)", "roadmap visual")
    row = "| [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) | finite-window H-fair service guarantee plus P48 local stopping thresholds | finite global-round stopping for asynchronous priority sampling and a no-progress impossibility result without fairness | proved asynchronous scheduling theorem |"
    row51 = row + "\n| [P51](proposition_51_heterogeneous_service_rate_stopping.md) | preparation-specific finite-window quotas and exact endpoint service bottlenecks | instance-dependent positive/all-negative global stopping bounds with P50 as a special case | proved heterogeneous scheduling theorem |"
    text = replace_once(text, row, row51, "roadmap row")
    write("docs/theorem_roadmap.md", text)


def integrate_navigation() -> None:
    text = read("docs/research_navigation.md")
    if "| P51 | [Heterogeneous finite-window service-rate stopping]" in text:
        return
    text = text.replace("P1 through P50", "P1 through P51")
    row = "| P50 | [Bounded-starvation asynchronous sampling](proposition_50_bounded_starvation_asynchronous_sampling.md) | H-fair priority sampling with finite global-round stopping and explicit no-starvation necessity |"
    row51 = row + "\n| P51 | [Heterogeneous finite-window service-rate stopping](proposition_51_heterogeneous_service_rate_stopping.md) | preparation-specific service windows and quotas with endpoint-bottleneck global stopping bounds |"
    text = replace_once(text, row, row51, "navigation row")
    write("docs/research_navigation.md", text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 40. P51 heterogeneous finite-window service-rate stopping" in text:
        return
    addition = r'''

---

# 40. P51 heterogeneous finite-window service-rate stopping

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \((W_i,q_i)\) | preparation-specific finite-window service guarantee | repository definition | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(N_i(T)\ge q_i\lfloor T/W_i\rfloor\) | finite-time local-count growth | proved block-counting theorem | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_i(N)=W_i\lceil N/q_i\rceil\) | sufficient global rounds for endpoint local threshold | proved inversion of the service bound | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_e=\max\{T_i(N_e),T_j(N_e)\}\) | edge service bottleneck | proved endpoint assembly | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_+=\min_{M_e>0}T_e\) | positive-witness global stopping bound | proved from P47-P48 plus P51 service | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_-=\max_eT_e\) | all-negative global stopping bound | proved from P47-P48 plus P51 service | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    text = read("pyproject.toml")
    text = replace_once(text, 'version = "0.50.0"', 'version = "0.51.0"', "pyproject version")
    text = replace_once(text, "bounded-starvation asynchronous sampling, robust experiment design", "bounded-starvation asynchronous sampling, heterogeneous finite-window service-rate stopping, robust experiment design", "pyproject description")
    write("pyproject.toml", text)

    text = read("CITATION.cff")
    text = replace_once(text, "version: 0.50.0", "version: 0.51.0", "citation version")
    text = replace_once(text, "bounded-starvation asynchronous sampling, robust experiment design", "bounded-starvation asynchronous sampling, heterogeneous finite-window service-rate stopping, robust experiment design", "citation abstract")
    write("CITATION.cff", text)

    text = read("CHANGELOG.md")
    if not text.startswith("# 0.51.0 - 2026-09-10"):
        entry = """# 0.51.0 - 2026-09-10

- Add P51 heterogeneous finite-window service-rate stopping.
- Replace one common P50 starvation horizon with preparation-specific windows and quotas.
- Prove exact finite-time local-count growth and endpoint threshold inversion.
- Derive edge bottleneck times and instance-dependent positive/all-negative global stopping bounds.
- Recover P50 exactly as the quota-one common-window special case.
- Preserve dynamic pruning and distinguish finite-window guarantees from asymptotic service-rate heuristics.
- Add implementation, regression tests, theorem visual, and equation-map provenance.

"""
        write("CHANGELOG.md", entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(text, '    "p50_bounded_starvation_asynchronous_sampling.svg",', '    "p50_bounded_starvation_asynchronous_sampling.svg",\n    "p51_heterogeneous_service_rate_stopping.svg",', "main figure guard")
    text = text.replace("for index in range(1, 51):", "for index in range(1, 52):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.50.0-2563eb", "version-0.51.0-2563eb")
    text = text.replace('version = "0\\.50\\.0"', 'version = "0\\.51\\.0"')
    text = text.replace("version: 0\\.50\\.0", "version: 0\\.51\\.0")
    marker = '        "Proposition 50",\n        "p50_bounded_starvation_asynchronous_sampling.svg",\n        "bounded_starvation_sampling.py",\n        "test_bounded_starvation_sampling.py",\n'
    replacement = marker + '        "Proposition 51",\n        "p51_heterogeneous_service_rate_stopping.svg",\n        "heterogeneous_service_stopping.py",\n        "test_heterogeneous_service_stopping.py",\n'
    text = replace_once(text, marker, replacement, "release path guards")
    write(path, text)

    write("tests/test_heterogeneous_service_stopping_documentation.py", '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_51_heterogeneous_service_rate_stopping.md"\nFIGURE = ROOT / "docs" / "figures" / "p51_heterogeneous_service_rate_stopping.svg"\n\n\ndef test_p51_documentation_exposes_core_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in ("Proposition 51A", "Proposition 51B", "Proposition 51C", "P50 is an exact special case", "Finite-window rate interpretation", "Scientific boundary"):\n        assert phrase in text\n\n\ndef test_p51_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in ("p51_heterogeneous_service_rate_stopping.svg", "heterogeneous_service_stopping.py", "test_heterogeneous_service_stopping.py", "P51 - heterogeneous finite-window service-rate stopping"):\n        assert token in readme\n''')


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equation_map()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
