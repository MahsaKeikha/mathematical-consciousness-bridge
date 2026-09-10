from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P49 publication marker: {label}")
    return text.replace(old, new, 1)


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.22 P49 - dyadic certification schedules" in text:
        return

    text = replace_once(
        text,
        "version-0.48.0-2563eb",
        "version-0.49.0-2563eb",
        "README version",
    )

    p48 = (
        "**P48** converts that qualitative eventual-detection result into an "
        "explicit gap-dependent stopping bound under a declared logarithmic "
        "confidence-sequence envelope, including positive-witness, all-negative, "
        "zero-gap, and acquisition-cost cases."
    )
    p49 = (
        p48
        + " **P49** proves that full graph certification need only be evaluated at "
        "dyadic sample counts: the first checkpoint above any finite P48 threshold "
        "is strictly below twice that threshold, while the number of complete "
        "certification looks grows only logarithmically."
    )
    text = replace_once(text, p48, p49, "README abstract")

    text = replace_once(
        text,
        "The public research record now contains **48 proposition-level results",
        "The public research record now contains **49 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P48", "P1 through P49")

    p48_row = (
        "| gap-dependent sequential stopping complexity | "
        "[Proposition 48](docs/proposition_48_gap_dependent_stopping_complexity.md) | "
        "explicit nonzero-margin local sample bound, positive/all-negative stopping "
        "epochs, zero-gap boundary, and pruning-aware acquisition-cost control |"
    )
    p49_row = (
        p48_row
        + "\n| dyadic certification schedule | "
        "[Proposition 49](docs/proposition_49_dyadic_stopping_overhead.md) | "
        "logarithmic full-graph certification looks with strictly less than twofold "
        "sample-threshold and linear-cost overhead |"
    )
    text = replace_once(text, p48_row, p49_row, "README navigation")

    section = r'''
## 13.22 P49 - dyadic certification schedules

![P49 dyadic stopping overhead](docs/figures/p49_dyadic_stopping_overhead.svg)

P48 provides an explicit sufficient local sample threshold \(N_e\) for every declared nonzero-margin edge. P49 asks a different practical question: **must the complete P47 witness graph be re-evaluated after every new sample?**

The answer is no. Define the dyadic checkpoint map

\[
\boxed{
D(N)=2^{\lceil\log_2N\rceil}.
}
\]

This is the first sample count in

\[
1,2,4,8,16,\ldots
\]

that is at least \(N\).

For every positive integer \(N\), P49 proves the exact deterministic bound

\[
\boxed{
N\le D(N)<2N.
}
\]

Thus an experiment that recomputes the full certificate only at dyadic counts reaches a valid P48 sign-certification checkpoint with strictly less than a factor of two sample-count overhead.

The number of full certification looks through that point is

\[
\boxed{
L(N)=\lceil\log_2N\rceil+1,
}
\]

so complete graph evaluation drops from at most \(O(N)\) per-sample looks to

\[
\boxed{O(\log N)}.
\]

If the P48 positive-witness stopping bound is

\[
K_+=\min_{e:M_e>0}N_e,
\]

then the dyadic procedure stops no later than

\[
\boxed{
\widetilde K_+=D(K_+)<2K_+.
}
\]

If every declared edge is strictly negative and P48 gives

\[
K_-=\max_eN_e,
\]

then dyadic all-negative certification occurs no later than

\[
\boxed{
\widetilde K_-=D(K_-)<2K_-.
}
\]

The P48 zero-gap boundary is unchanged. If a required population margin is exactly zero, P48 supplies no generic finite sign-separation threshold, and P49 cannot manufacture one by changing the checkpoint schedule.

P47 validity also requires no new correction: dyadic checkpoints are merely a deterministic subset of the times already covered by the P47 simultaneous confidence event.

For any full-family acquisition cost linear in epoch count,

\[
C_{\rm full}(K)=K\sum_{i\in V}c_i,
\]

the corresponding dyadic reference satisfies

\[
\boxed{
C_{\rm full}(K)
\le
C_{\rm dyad}(K)
<
2C_{\rm full}(K).
}
\]

P49 therefore separates **certification-computation frequency** from **sample acquisition**: the number of complete statistical evaluations becomes logarithmic, while the stopping-threshold overshoot remains strictly bounded below twofold.

The theorem is intentionally narrow. It does not prove dyadic scheduling is optimal, does not improve the underlying P48 population gap, and does not establish quantum incompleteness, an extra physical dimension, or consciousness.

[Read Proposition 49](docs/proposition_49_dyadic_stopping_overhead.md). The [P49 theorem map](docs/figures/p49_dyadic_stopping_overhead.svg), [implementation](src/consciousness_bridge/dyadic_stopping_overhead.py), and [tests](tests/test_dyadic_stopping_overhead.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P49 section")
    write("README.md", text)


def integrate_roadmap() -> None:
    text = read("docs/theorem_roadmap.md")
    if "[P49](proposition_49_dyadic_stopping_overhead.md)" in text:
        return

    visual = "![P48 gap-dependent stopping complexity](figures/p48_gap_dependent_stopping_complexity.svg)"
    text = replace_once(
        text,
        visual,
        visual + "\n\n![P49 dyadic stopping overhead](figures/p49_dyadic_stopping_overhead.svg)",
        "roadmap visual",
    )

    row = (
        "| [P48](proposition_48_gap_dependent_stopping_complexity.md) | explicit "
        "inversion of a logarithmic confidence-sequence envelope plus margin "
        "perturbation bounds | gap-dependent positive/all-negative stopping epochs "
        "and pruning-aware acquisition-cost upper bound | proved sequential "
        "stopping-complexity theorem |"
    )
    row49 = (
        row
        + "\n| [P49](proposition_49_dyadic_stopping_overhead.md) | dyadic ceiling "
        "geometry and deterministic checkpoint-count bound | logarithmic complete "
        "certification looks with strictly less than twofold stopping-threshold and "
        "linear-cost overhead | proved sequential scheduling theorem |"
    )
    text = replace_once(text, row, row49, "roadmap row")
    write("docs/theorem_roadmap.md", text)


def integrate_navigation() -> None:
    text = read("docs/research_navigation.md")
    if "| P49 | [Dyadic certification schedule]" in text:
        return
    text = text.replace("P1 through P48", "P1 through P49")

    row = (
        "| P48 | [Gap-dependent stopping complexity]"
        "(proposition_48_gap_dependent_stopping_complexity.md) | explicit "
        "nonzero-margin sequential stopping counts, all-negative certification, "
        "zero-gap boundary, and acquisition-cost control |"
    )
    row49 = (
        row
        + "\n| P49 | [Dyadic certification schedule]"
        "(proposition_49_dyadic_stopping_overhead.md) | logarithmic certification "
        "looks with strictly less than twofold stopping-threshold overhead |"
    )
    text = replace_once(text, row, row49, "navigation row")
    write("docs/research_navigation.md", text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 38. P49 dyadic certification schedules" in text:
        return
    addition = r'''

---

# 38. P49 dyadic certification schedules

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D(N)=2^{\lceil\log_2N\rceil}\) | first dyadic checkpoint at or above a finite P48 threshold | repository definition | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(N\le D(N)<2N\) | exact sample-threshold overhead bound | proved integer scheduling theorem | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(L(N)=\lceil\log_2N\rceil+1\) | complete certification-look count through the dyadic threshold | proved counting identity | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(\widetilde K_+=D(K_+)<2K_+\) | positive-witness dyadic stopping bound | proved from P48 plus monotonicity of \(D\) | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(\widetilde K_-=D(K_-)<2K_-\) | all-negative dyadic stopping bound | proved from P48 plus monotonicity of \(D\) | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(C_{\rm dyad}(K)<2C_{\rm full}(K)\) | linear acquisition-cost overhead | proved by multiplying the dyadic epoch inequality by positive per-epoch cost | [P49](proposition_49_dyadic_stopping_overhead.md) |

P49 changes checkpoint frequency only. Statistical validity remains inherited from P47 and finite sign separation remains inherited from P48.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    text = read("pyproject.toml")
    text = replace_once(text, 'version = "0.48.0"', 'version = "0.49.0"', "pyproject version")
    text = replace_once(
        text,
        "gap-dependent sequential stopping complexity, robust experiment design",
        "gap-dependent sequential stopping complexity, dyadic certification scheduling, robust experiment design",
        "pyproject description",
    )
    write("pyproject.toml", text)

    text = read("CITATION.cff")
    text = replace_once(text, "version: 0.48.0", "version: 0.49.0", "citation version")
    text = replace_once(
        text,
        "gap-dependent sequential stopping complexity, robust experiment design",
        "gap-dependent sequential stopping complexity, dyadic certification scheduling, robust experiment design",
        "citation abstract",
    )
    write("CITATION.cff", text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.49.0 - 2026-09-10"):
        entry = """# 0.49.0 - 2026-09-10

- Add P49 dyadic certification schedules for P48 stopping thresholds.
- Prove the exact dyadic ceiling bound N <= D(N) < 2N.
- Reduce complete certification evaluations to ceil(log2 N)+1 looks.
- Prove less-than-two positive-witness and all-negative stopping overhead.
- Preserve the P48 zero-gap boundary and P47 simultaneous-validity guarantee.
- Extend the less-than-two factor to linear full-family acquisition-cost bounds.
- Add implementation, regression tests, theorem visual, and equation-map provenance.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p48_gap_dependent_stopping_complexity.svg",',
        '    "p48_gap_dependent_stopping_complexity.svg",\n    "p49_dyadic_stopping_overhead.svg",',
        "main figure guard",
    )
    text = text.replace("for index in range(1, 49):", "for index in range(1, 50):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.48.0-2563eb", "version-0.49.0-2563eb")
    text = text.replace('version = "0\\.48\\.0"', 'version = "0\\.49\\.0"')
    text = text.replace("version: 0\\.48\\.0", "version: 0\\.49\\.0")

    marker = (
        '        "Proposition 48",\n'
        '        "p48_gap_dependent_stopping_complexity.svg",\n'
        '        "gap_stopping_complexity.py",\n'
        '        "test_gap_stopping_complexity.py",\n'
    )
    replacement = marker + (
        '        "Proposition 49",\n'
        '        "p49_dyadic_stopping_overhead.svg",\n'
        '        "dyadic_stopping_overhead.py",\n'
        '        "test_dyadic_stopping_overhead.py",\n'
    )
    text = replace_once(text, marker, replacement, "release path guards")
    write(path, text)

    write(
        "tests/test_dyadic_stopping_overhead_documentation.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_49_dyadic_stopping_overhead.md"\nFIGURE = ROOT / "docs" / "figures" / "p49_dyadic_stopping_overhead.svg"\n\n\ndef test_p49_documentation_exposes_core_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 49A",\n        "Proposition 49B",\n        "Proposition 49C",\n        "Zero-gap boundary is preserved",\n        "Certification-look complexity",\n        "Scientific boundary",\n    ):\n        assert phrase in text\n\n\ndef test_p49_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "p49_dyadic_stopping_overhead.svg",\n        "dyadic_stopping_overhead.py",\n        "test_dyadic_stopping_overhead.py",\n        "P49 - dyadic certification schedules",\n    ):\n        assert token in readme\n''',
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
