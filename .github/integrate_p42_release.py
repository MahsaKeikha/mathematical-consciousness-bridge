from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1) if old in text else text


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.41.0-2563eb", "version-0.42.0-2563eb", "README badge")
text = replace_once(
    text,
    "**P41** makes that continuous-region theorem directly computable for trace-distance tomography balls, converting per-preparation quantum and target confidence radii into an end-to-end regularity obstruction and an explicit uncertainty budget.",
    "**P41** makes that continuous-region theorem directly computable for trace-distance tomography balls, converting per-preparation quantum and target confidence radii into an end-to-end regularity obstruction and an explicit uncertainty budget. **P42** supplies an explicit finite-sample theorem for a fixed informationally complete POVM, exposing the reconstruction-conditioning penalty and giving sufficient quantum and target trial counts with inverse-square dependence on the population regularity gap.",
    "README abstract P42",
)
text = replace_once(text, "**41 proposition-level results", "**42 proposition-level results", "README result count")
text = replace_once(text, "P1 through P41 with explicit dependency branches", "P1 through P42 with explicit dependency branches", "README theorem range")
text = replace_once(
    text,
    "| trace-ball quantum envelope | [Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md) | analytic pairwise quantum envelope and end-to-end Lipschitz obstruction from simultaneous trace-distance and target-TV balls |",
    "| trace-ball quantum envelope | [Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md) | analytic pairwise quantum envelope and end-to-end Lipschitz obstruction from simultaneous trace-distance and target-TV balls |\n| IC-POVM sample complexity | [Proposition 42](docs/proposition_42_ic_povm_sample_complexity.md) | explicit sufficient quantum and target trial counts under IID finite-outcome concentration and declared reconstruction stability |",
    "README navigation P42",
)
text = replace_once(
    text,
    "| **11.17 P41 trace-ball quantum envelope** | How can per-preparation trace-distance and target-TV confidence balls yield a directly computable P40 obstruction? |",
    "| **11.17 P41 trace-ball quantum envelope** | How can per-preparation trace-distance and target-TV confidence balls yield a directly computable P40 obstruction? |\n| **11.18 P42 IC-POVM sample complexity** | Under a fixed informationally complete measurement and reconstruction stability constant, how many samples are sufficient to force the P41 obstruction? |",
    "README paper map P42",
)
text = replace_once(text, "| proposition-level results | **41** |", "| proposition-level results | **42** |", "README glance count")
text = replace_once(text, "| research-software version | **0.41.0** |", "| research-software version | **0.42.0** |", "README glance version")
text = replace_once(
    text,
    "In the unsaturated symmetric-error regime, a conservative design inequality is\n\n\\[\n\\boxed{\nd_Y-Ld_Q>2\\varepsilon+2Lr.}\n\\]\n\nThe left side is the population regularity gap. The right side is the combined uncertainty cost. This decomposition tells an experimentalist whether the current limitation is quantum-state precision, target precision, or the assumed bridge regularity.",
    "For a population-level planning calculation, the empirical center distances can themselves deviate from the population distances before the P41 confidence envelopes are applied. Therefore the conservative end-to-end design condition is\n\n\\[\n\\boxed{\nd_Y-Ld_Q>4\\varepsilon+4Lr.}\n\\]\n\nThe left side is the population regularity gap. The right side is the complete finite-error budget needed to guarantee a positive data-dependent P41 margin. This correction is intentionally conservative and prevents the center-estimation error from being counted only once.",
    "README P41 population correction",
)

p42_section = r'''## 13.15 P42 - IC-POVM finite-sample obstruction complexity

![P42 IC-POVM finite-sample obstruction complexity](docs/figures/p42_ic_povm_sample_complexity.svg)

P42 turns the corrected P41 population design inequality into explicit trial counts under one declared finite-outcome tomography model.

Let

\[
\mathcal M=\{M_1,\ldots,M_{m_Q}\}
\]

be a fixed informationally complete POVM and let

\[
p_x(j)=\operatorname{Tr}(M_j\rho_x).
\]

Assume a linear reconstruction map \(A\) with declared trace-norm stability constant \(\kappa\):

\[
\boxed{\|A(v)\|_1\le\kappa\|v\|_1.}
\]

For \(N\) preparations and \(n_Q\) IID POVM outcomes per preparation, coordinatewise Hoeffding concentration and a union bound give the simultaneous trace-distance radius

\[
\boxed{
r_Q(n_Q)
=
\kappa m_Q
\sqrt{
\frac{\log(2Nm_Q/\alpha_Q)}{2n_Q}
}.
}
\]

For an independently defined target alphabet of size \(m_Y\), \(n_Y\) IID target observations per preparation give the simultaneous total-variation radius

\[
\boxed{
\varepsilon_Y(n_Y)
=
\frac{m_Y}{2}
\sqrt{
\frac{\log(2Nm_Y/\alpha_Y)}{2n_Y}
}.
}
\]

For one preparation pair define the population regularity gap

\[
\boxed{\Delta=d_Y-Ld_Q.}
\]

The P41 obstruction is guaranteed by the sufficient condition

\[
\boxed{
\Delta
>
4\varepsilon_Y(n_Y)
+4Lr_Q(n_Q).
}
\]

Choose a budget split \(0<\lambda<1\). It is sufficient that

\[
4\varepsilon_Y(n_Y)\le\lambda\Delta,
\qquad
4Lr_Q(n_Q)\le(1-\lambda)\Delta.
\]

Solving gives

\[
\boxed{
n_Y
\ge
\frac{2m_Y^2\log(2Nm_Y/\alpha_Y)}{\lambda^2\Delta^2}
}
\]

and, for \(L>0\),

\[
\boxed{
n_Q
\ge
\frac{8L^2\kappa^2m_Q^2\log(2Nm_Q/\alpha_Q)}{(1-\lambda)^2\Delta^2}.
}
\]

For the balanced choice \(\lambda=1/2\),

\[
\boxed{
n_Y
\ge
\frac{8m_Y^2\log(2Nm_Y/\alpha_Y)}{\Delta^2},
}
\]

\[
\boxed{
n_Q
\ge
\frac{32L^2\kappa^2m_Q^2\log(2Nm_Q/\alpha_Q)}{\Delta^2}.
}
\]

P42 therefore makes the cost of experimental precision explicit. The target and quantum branches both have inverse-square gap scaling, while tomography pays a quadratic penalty in the declared reconstruction instability \(\kappa\) and bridge Lipschitz constant \(L\).

The scientific boundary remains strict:

\[
\boxed{
\text{finite-sample rejection of one declared IC-POVM and Lipschitz model class}
\neq
\text{quantum incompleteness}.
}
\]

The POVM, IID model, reconstruction stability, system boundary, target validity, and regularity class are all premises. A positive P42 certificate rejects that declared model class only.

The next theorem burden is a lower bound: determine whether order \(\Delta^{-2}\) samples are unavoidable in the declared finite-outcome setting rather than merely sufficient under Hoeffding concentration.

[Read Proposition 42](docs/proposition_42_ic_povm_sample_complexity.md). The [P42 theorem map](docs/figures/p42_ic_povm_sample_complexity.svg), [implementation](src/consciousness_bridge/ic_povm_sample_complexity.py), and [tests](tests/test_ic_povm_sample_complexity.py) expose the complete proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md). The [P41 theorem map](docs/figures/p41_trace_ball_quantum_envelope.svg), [implementation](src/consciousness_bridge/trace_ball_quantum_envelope.py), and [tests](tests/test_trace_ball_quantum_envelope.py) expose the complete proof-to-code path.\n\n---",
    "[Read Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md). The [P41 theorem map](docs/figures/p41_trace_ball_quantum_envelope.svg), [implementation](src/consciousness_bridge/trace_ball_quantum_envelope.py), and [tests](tests/test_trace_ball_quantum_envelope.py) expose the complete proof-to-code path.\n\n" + p42_section + "---",
    "README P42 section",
)
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)",
    "![P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)\n\n![P42 IC-POVM sample complexity](figures/p42_ic_povm_sample_complexity.svg)",
    "roadmap P42 figure",
)
row = "| [P41](proposition_41_trace_ball_quantum_envelope.md) | trace-distance triangle inequality plus simultaneous quantum and target confidence balls | analytic P40 envelope and end-to-end regularity obstruction | proved confidence-envelope theorem |"
text = replace_once(
    text,
    row,
    row + "\n| [P42](proposition_42_ic_povm_sample_complexity.md) | finite-outcome Hoeffding concentration plus IC reconstruction stability | explicit sufficient quantum and target sample sizes for the corrected P41 obstruction | proved finite-sample sample-complexity theorem |",
    "roadmap P42 row",
)
text = replace_once(
    text,
    "For an \\(L\\)-Lipschitz bridge and symmetric uncertainty, the design inequality is\n\n\\[\n\\boxed{d_Y-Ld_Q>2\\varepsilon+2Lr.}\n\\]",
    "For a population-level planning guarantee, center-estimation error must also be carried through the confidence envelopes. The corrected conservative inequality is\n\n\\[\n\\boxed{d_Y-Ld_Q>4\\varepsilon+4Lr.}\n\\]",
    "roadmap P41 correction",
)
roadmap_section = r'''---

## P42 - IC-POVM finite-sample obstruction sample complexity

For a fixed informationally complete POVM with \(m_Q\) outcomes and reconstruction stability

\[
\|A(v)\|_1\le\kappa\|v\|_1,
\]

P42 derives

\[
r_Q(n_Q)=
\kappa m_Q
\sqrt{\frac{\log(2Nm_Q/\alpha_Q)}{2n_Q}}.
\]

For a target alphabet of size \(m_Y\),

\[
\varepsilon_Y(n_Y)=
\frac{m_Y}{2}
\sqrt{\frac{\log(2Nm_Y/\alpha_Y)}{2n_Y}}.
\]

Writing \(\Delta=d_Y-Ld_Q\), a sufficient end-to-end condition is

\[
\boxed{\Delta>4\varepsilon_Y(n_Y)+4Lr_Q(n_Q).}
\]

With budget split \(0<\lambda<1\), sufficient trial counts are

\[
\boxed{
n_Y\ge
\frac{2m_Y^2\log(2Nm_Y/\alpha_Y)}{\lambda^2\Delta^2}
}
\]

and

\[
\boxed{
n_Q\ge
\frac{8L^2\kappa^2m_Q^2\log(2Nm_Q/\alpha_Q)}{(1-\lambda)^2\Delta^2}.
}
\]

The theorem is conditional on the declared IC measurement, reconstruction stability, IID sampling, system boundary, target definition, and Lipschitz bridge class.

Direct proof: [Proposition 42](proposition_42_ic_povm_sample_complexity.md). Implementation: [ic_povm_sample_complexity.py](../src/consciousness_bridge/ic_povm_sample_complexity.py). Tests: [test_ic_povm_sample_complexity.py](../tests/test_ic_povm_sample_complexity.py).
'''
text = replace_once(
    text,
    "Direct proof: [Proposition 41](proposition_41_trace_ball_quantum_envelope.md). Implementation: [trace_ball_quantum_envelope.py](../src/consciousness_bridge/trace_ball_quantum_envelope.py). Tests: [test_trace_ball_quantum_envelope.py](../tests/test_trace_ball_quantum_envelope.py).",
    "Direct proof: [Proposition 41](proposition_41_trace_ball_quantum_envelope.md). Implementation: [trace_ball_quantum_envelope.py](../src/consciousness_bridge/trace_ball_quantum_envelope.py). Tests: [test_trace_ball_quantum_envelope.py](../tests/test_trace_ball_quantum_envelope.py).\n\n" + roadmap_section,
    "roadmap P42 section",
)
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "from P1 through P41", "from P1 through P42", "navigation range")
row = "| P41 | [Trace-ball quantum envelope](proposition_41_trace_ball_quantum_envelope.md) | analytic continuous-region envelope and end-to-end Lipschitz certificate |"
text = replace_once(
    text,
    row,
    row + "\n| P42 | [IC-POVM sample complexity](proposition_42_ic_povm_sample_complexity.md) | explicit finite-sample quantum and target trial requirements for P41 |",
    "navigation P42 row",
)
path.write_text(text, encoding="utf-8")

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "| \\(d_Y-Ld_Q>2\\varepsilon+2Lr\\) | symmetric unsaturated experimental design condition | derived sufficient inequality | [P41](proposition_41_trace_ball_quantum_envelope.md) |",
    "| \\(d_Y-Ld_Q>4\\varepsilon+4Lr\\) | corrected conservative population-level design condition after carrying center-estimation error through the P41 confidence envelopes | derived sufficient inequality | [P41](proposition_41_trace_ball_quantum_envelope.md) |",
    "equation map P41 correction",
)
p42_eq = r'''# 31. P42 IC-POVM finite-sample obstruction sample complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p_x(j)=\operatorname{Tr}(M_j\rho_x)\) | finite-outcome quantum measurement probabilities | standard Born rule specialized to a fixed POVM | standard quantum measurement theory; [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(\|A(v)\|_1\le\kappa\|v\|_1\) | declared stability of the IC linear reconstruction map | explicit model assumption | [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(r_Q(n_Q)=\kappa m_Q\sqrt{\log(2Nm_Q/\alpha_Q)/(2n_Q)}\) | simultaneous trace-distance tomography radius under the declared reconstruction model | proved from coordinatewise Hoeffding, union bound, reconstruction stability, and trace-norm projection | [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(\varepsilon_Y(n_Y)=\frac{m_Y}{2}\sqrt{\log(2Nm_Y/\alpha_Y)/(2n_Y)}\) | simultaneous target-TV radius | proved from coordinatewise Hoeffding and union bound | [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(\Delta=d_Y-Ld_Q\) | population regularity gap for one preparation pair | repository definition | [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(\Delta>4\varepsilon_Y+4Lr_Q\) | sufficient finite-sample condition for a positive P41 obstruction | proved by substitution into corrected P41 population bound | [P41](proposition_41_trace_ball_quantum_envelope.md); [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(n_Y\ge2m_Y^2\log(2Nm_Y/\alpha_Y)/(\lambda^2\Delta^2)\) | sufficient per-preparation target sample size | algebraic consequence | [P42](proposition_42_ic_povm_sample_complexity.md) |
| \(n_Q\ge8L^2\kappa^2m_Q^2\log(2Nm_Q/\alpha_Q)/((1-\lambda)^2\Delta^2)\) | sufficient per-preparation quantum sample size | algebraic consequence | [P42](proposition_42_ic_povm_sample_complexity.md) |

P42 is conditional on IID sampling, a fixed informationally complete POVM, a valid reconstruction stability constant, and a declared Lipschitz bridge class. The inverse-square gap law is a sufficient upper bound here, not yet a minimax lower bound.

---

'''
text = replace_once(text, "# 31. Candidate consciousness-theory feature families", p42_eq + "# 32. Candidate consciousness-theory feature families", "equation map P42 section")
text = replace_once(text, "# 32. Citation discipline", "# 33. Citation discipline", "equation map citation renumber")
path.write_text(text, encoding="utf-8")

# Main page guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p41_trace_ball_quantum_envelope.svg",', '    "p41_trace_ball_quantum_envelope.svg",\n    "p42_ic_povm_sample_complexity.svg",', "main page P42 figure")
text = replace_once(text, "for index in range(1, 42):", "for index in range(1, 43):", "main page P42 proposition")
path.write_text(text, encoding="utf-8")

# Package metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.41.0"', 'version = "0.42.0"', "pyproject version")
text = replace_once(text, "trace-ball quantum envelope certification, recoverability", "trace-ball quantum envelope certification, IC-POVM finite-sample obstruction sample complexity, recoverability", "pyproject description")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.41.0", "version: 0.42.0", "citation version")
text = replace_once(text, "trace-ball quantum envelope certification, robust experiment design", "trace-ball quantum envelope certification, IC-POVM finite-sample obstruction sample complexity, robust experiment design", "citation abstract")
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.42.0 - 2026-09-09

### Added
- Proposition 42: finite-sample obstruction sample complexity for a fixed informationally complete POVM.
- Explicit simultaneous quantum trace-distance radius under a declared linear reconstruction stability constant.
- Explicit simultaneous finite-alphabet target-TV radius.
- Sufficient quantum and target sample-size formulas with inverse-square regularity-gap scaling.
- Executable implementation, regression tests, publication map, and public-paper integration.

### Corrected
- Proposition 41 population-level planning inequality now carries center-estimation error through the confidence envelopes correctly. The conservative sufficient condition is \(d_Y-Ld_Q>4\varepsilon+4Lr\), not the earlier factor-two expression.
- Malformed P41 LaTeX control characters in the target and quantum symbols were removed.

### Scientific boundary
- P42 is conditional on IID sampling, a fixed informationally complete measurement, a declared reconstruction stability constant, and a declared Lipschitz bridge class.
- The theorem gives a sufficient upper bound on sample complexity. It does not yet prove minimax optimality and does not establish quantum incompleteness or consciousness.

'''
text = replace_once(text, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog P42")
path.write_text(text, encoding="utf-8")
