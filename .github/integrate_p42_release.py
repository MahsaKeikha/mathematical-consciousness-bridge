from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.41.0-2563eb", "version-0.42.0-2563eb", "README version")
text = replace_once(
    text,
    "**P41** makes that continuous-region theorem directly computable for trace-distance tomography balls, converting per-preparation quantum and target confidence radii into an end-to-end regularity obstruction and an explicit uncertainty budget.",
    "**P41** makes that continuous-region theorem directly computable for trace-distance tomography balls, converting per-preparation quantum and target confidence radii into an end-to-end regularity obstruction and an explicit uncertainty budget. **P42** derives explicit finite-sample radii for a fixed informationally complete measurement and categorical target model, then solves for sufficient quantum and target sample sizes needed to resolve a positive population regularity gap.",
    "README abstract P42",
)
text = replace_once(text, "**41 proposition-level results", "**42 proposition-level results", "README proposition count")
text = text.replace("P1 through P41", "P1 through P42")
text = replace_once(
    text,
    "| trace-ball quantum envelope | [Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md) | analytic pairwise quantum envelope and end-to-end Lipschitz obstruction from simultaneous trace-distance and target-TV balls |",
    "| trace-ball quantum envelope | [Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md) | analytic pairwise quantum envelope and end-to-end Lipschitz obstruction from simultaneous trace-distance and target-TV balls |\n| quantum regular-bridge sample complexity | [Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md) | explicit IC-tomography and categorical-target sample sizes for resolving a positive Lipschitz regularity gap |",
    "README navigation P42",
)
text = replace_once(
    text,
    "| **11.17 P41 trace-ball quantum envelope** | How can per-preparation trace-distance and target-TV confidence balls yield a directly computable P40 obstruction? |",
    "| **11.17 P41 trace-ball quantum envelope** | How can per-preparation trace-distance and target-TV confidence balls yield a directly computable P40 obstruction? |\n| **11.18 P42 quantum regular-bridge sample complexity** | How many IC quantum measurements and categorical target observations are sufficient to resolve a declared positive regularity gap? |",
    "README paper map P42",
)
text = replace_once(text, "| proposition-level results | **41** |", "| proposition-level results | **42** |", "README record count")
text = replace_once(text, "| research-software version | **0.41.0** |", "| research-software version | **0.42.0** |", "README record version")

p42 = r'''## 13.15 P42 - quantum regular-bridge sample complexity

![P42 quantum regular-bridge sample complexity](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg)

P41 states its uncertainty budget in terms of abstract quantum and target confidence radii. P42 derives those radii for one explicit experimental design and solves the resulting sufficient sample-size inequalities.

Let there be \(K\) preparations. For each preparation, measure one fixed informationally complete POVM with \(m\) outcomes. Let \(p_x\) be the true measurement distribution and \(\widehat p_x\) the empirical distribution from \(n_Q\) IID repetitions. Let the fixed linear reconstruction map \(R\) satisfy \(R(p_x)=\rho_x\) and

\[
\boxed{
\frac12\|R(v)\|_1\le\kappa_R\|v\|_1.
}
\]

A coordinate Hoeffding bound plus a union bound over all \(Km\) coordinates gives

\[
\boxed{
t_Q=\sqrt{\frac{\log(2Km/\alpha_Q)}{2n_Q}}}
\]

and therefore the simultaneous raw-reconstruction trace-norm radius

\[
\boxed{
r_Q=\kappa_Rm\sqrt{\frac{\log(2Km/\alpha_Q)}{2n_Q}}.
}
\]

The raw linear reconstruction \(\widetilde\rho_x=R(\widehat p_x)\) need not be positive semidefinite, so P42 treats it only as a Hermitian reconstruction. It does not silently relabel it as a physical density operator.

For an independently defined categorical target with alphabet size \(k\), \(n_Y\) IID observations per preparation give the simultaneous total-variation radius

\[
\boxed{
\varepsilon_Y
=\frac{k}{2}
\sqrt{\frac{\log(2Kk/\alpha_Y)}{2n_Y}}.
}
\]

For one preparation pair define

\[
d_Q=D(\rho_x,\rho_{x'}),
\qquad
d_Y=\|P_x-P_{x'}\|_{\mathrm{TV}},
\]

and the population Lipschitz regularity gap

\[
\boxed{\Delta=d_Y-Ld_Q.}
\]

P42 proves that on the simultaneous concentration event, the empirical P41 obstruction margin obeys

\[
\boxed{
\widehat M_{xx'}
\ge
\Delta-4\varepsilon_Y-4Lr_Q.
}
\]

The factor four is not decorative. The empirical pair distances can deviate from their population values, and the final certificate then consumes a second uncertainty allowance when it forms its lower and upper confidence envelopes.

Choose \(\lambda\in(0,1)\) and require

\[
4\varepsilon_Y\le\lambda\Delta,
\qquad
4Lr_Q\le(1-\lambda)\Delta.
\]

Solving gives the sufficient per-preparation sample sizes

\[
\boxed{
n_Y
\ge
\frac{2k^2}{\lambda^2\Delta^2}
\log\frac{2Kk}{\alpha_Y}
}
\]

and

\[
\boxed{
n_Q
\ge
\frac{8L^2\kappa_R^2m^2}{(1-\lambda)^2\Delta^2}
\log\frac{2Km}{\alpha_Q}.
}
\]

For balanced allocation \(\lambda=1/2\),

\[
\boxed{
n_Y\ge\frac{8k^2}{\Delta^2}\log\frac{2Kk}{\alpha_Y}}
\]

and

\[
\boxed{
n_Q\ge\frac{32L^2\kappa_R^2m^2}{\Delta^2}\log\frac{2Km}{\alpha_Q}.}
\]

The theorem therefore exposes the experimental scaling directly: both sample requirements grow as \(\Delta^{-2}\), while the quantum requirement grows as \(L^2\kappa_R^2\). Poor tomography conditioning is not hidden inside an unspecified error bar.

With these sufficient sample sizes, a positive empirical obstruction is certified with confidence at least

\[
\boxed{\max\{0,1-\alpha_Q-\alpha_Y\}.}
\]

The result is conservative because it uses coordinate Hoeffding bounds and union bounds. Better tomography or multinomial confidence regions may improve the constants and dimension dependence without changing the logical structure.

The scientific boundary remains strict:

\[
\boxed{
\text{sufficient samples to reject one declared regular bridge class}
\neq
\text{quantum mechanics is incomplete}.
}
\]

P42 is conditional on the fixed IC measurement, reconstruction map, IID sampling model, system boundary, independent target definition, and declared Lipschitz bridge class. It does not identify the target with consciousness.

[Read Proposition 42](docs/proposition_42_quantum_regular_bridge_sample_complexity.md). The [P42 theorem map](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg), [implementation](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py), and [tests](tests/test_quantum_regular_bridge_sample_complexity.py) expose the complete proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md). The [P41 theorem map](docs/figures/p41_trace_ball_quantum_envelope.svg), [implementation](src/consciousness_bridge/trace_ball_quantum_envelope.py), and [tests](tests/test_trace_ball_quantum_envelope.py) expose the complete proof-to-code path.\n\n---",
    "[Read Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md). The [P41 theorem map](docs/figures/p41_trace_ball_quantum_envelope.svg), [implementation](src/consciousness_bridge/trace_ball_quantum_envelope.py), and [tests](tests/test_trace_ball_quantum_envelope.py) expose the complete proof-to-code path.\n\n" + p42 + "---",
    "README P42 section",
)
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)",
    "![P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)\n\n![P42 quantum regular-bridge sample complexity](figures/p42_quantum_regular_bridge_sample_complexity.svg)",
    "roadmap P42 figure",
)
row = "| [P41](proposition_41_trace_ball_quantum_envelope.md) | trace-distance triangle inequality plus simultaneous quantum and target confidence balls | analytic P40 envelope and end-to-end regularity obstruction | proved confidence-envelope theorem |"
text = replace_once(
    text,
    row,
    row + "\n| [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) | IC-measurement Hoeffding concentration plus linear-reconstruction stability | explicit sufficient quantum and target samples for a positive regularity obstruction | proved finite-sample design theorem |",
    "roadmap P42 row",
)
p42_road = r'''## P42 - explicit regular-bridge sample complexity

For a fixed IC measurement with \(m\) outcomes and reconstruction stability \(\kappa_R\), P42 obtains

\[
r_Q=\kappa_Rm\sqrt{\frac{\log(2Km/\alpha_Q)}{2n_Q}}.
\]

For a categorical target with \(k\) outcomes,

\[
\varepsilon_Y=\frac{k}{2}\sqrt{\frac{\log(2Kk/\alpha_Y)}{2n_Y}}.
\]

If \(\Delta=d_Y-Ld_Q>0\), then

\[
\boxed{\widehat M\ge\Delta-4\varepsilon_Y-4Lr_Q.}
\]

Allocating fractions \(\lambda\) and \(1-\lambda\) of the gap gives explicit sufficient \(n_Y\) and \(n_Q\), both scaling as \(\Delta^{-2}\). This is a theorem for one declared tomography design and bridge regularity class, not a quantum-incompleteness claim.

Direct proof: [Proposition 42](proposition_42_quantum_regular_bridge_sample_complexity.md). Implementation: [quantum_regular_bridge_sample_complexity.py](../src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py). Tests: [test_quantum_regular_bridge_sample_complexity.py](../tests/test_quantum_regular_bridge_sample_complexity.py).

---

'''
text = replace_once(text, "# 8. Fundamental physical sufficiency: P19", p42_road + "# 8. Fundamental physical sufficiency: P19", "roadmap P42 section")
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = text.replace("from P1 through P41", "from P1 through P42")
row = "| P41 | [Trace-ball quantum envelope](proposition_41_trace_ball_quantum_envelope.md) | analytic continuous-region envelope and end-to-end Lipschitz certificate |"
text = replace_once(
    text,
    row,
    row + "\n| P42 | [Quantum regular-bridge sample complexity](proposition_42_quantum_regular_bridge_sample_complexity.md) | explicit fixed-IC quantum and categorical-target sample-size theorem |",
    "navigation P42 row",
)
path.write_text(text, encoding="utf-8")

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
p42_eq = r'''# 31. P42 quantum regular-bridge sample complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\frac12\|R(v)\|_1\le\kappa_R\|v\|_1\) | conditioning bound for the declared linear IC reconstruction | declared tomography-design assumption | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(t_Q=\sqrt{\log(2Km/\alpha_Q)/(2n_Q)}\) | simultaneous coordinate-frequency radius over the IC experiment | Hoeffding plus union bound | standard concentration; [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(r_Q=\kappa_Rmt_Q\) | simultaneous raw-reconstruction half-trace-norm radius | proved from reconstruction stability and the frequency bound | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\varepsilon_Y=\frac{k}{2}\sqrt{\log(2Kk/\alpha_Y)/(2n_Y)}\) | simultaneous categorical target-TV radius | Hoeffding plus union bound | standard concentration; [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\Delta=d_Y-Ld_Q\) | population regularity gap for one preparation pair | repository design quantity | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\widehat M\ge\Delta-4\varepsilon_Y-4Lr_Q\) | finite-data lower bound on the empirical P41 obstruction margin | proved | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(n_Y\ge2k^2\log(2Kk/\alpha_Y)/(\lambda^2\Delta^2)\) | sufficient target samples per preparation | proved by uncertainty-budget allocation | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(n_Q\ge8L^2\kappa_R^2m^2\log(2Km/\alpha_Q)/((1-\lambda)^2\Delta^2)\) | sufficient quantum samples per preparation | proved by uncertainty-budget allocation | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |

P42 uses a fixed informationally complete measurement, a declared linear reconstruction stability constant, and IID categorical sampling. The coordinate Hoeffding construction is conservative. The raw linear reconstruction need not be a physical density operator. The theorem does not establish quantum incompleteness or consciousness.

---

'''
text = replace_once(text, "# 31. Candidate consciousness-theory feature families", p42_eq + "# 32. Candidate consciousness-theory feature families", "equation map P42")
text = replace_once(text, "# 32. Citation discipline", "# 33. Citation discipline", "equation map citation renumber")
path.write_text(text, encoding="utf-8")

# Main-page guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p41_trace_ball_quantum_envelope.svg",', '    "p41_trace_ball_quantum_envelope.svg",\n    "p42_quantum_regular_bridge_sample_complexity.svg",', "main-page P42 figure")
text = replace_once(text, "for index in range(1, 42):", "for index in range(1, 43):", "main-page P42 proposition range")
path.write_text(text, encoding="utf-8")

# Release metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.41.0"', 'version = "0.42.0"', "pyproject version")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.41.0", "version: 0.42.0", "citation version")
text = replace_once(
    text,
    "trace-ball quantum envelope certification,",
    "trace-ball quantum envelope certification, fixed-IC quantum regular-bridge sample complexity,",
    "citation P42 abstract",
)
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.42.0 - 2026-09-09

### Added
- Proposition 42: quantum regular-bridge sample complexity for a fixed informationally complete measurement and categorical IID target model.
- Explicit simultaneous quantum reconstruction radius controlled by the linear reconstruction stability constant \(\kappa_R\).
- Explicit simultaneous categorical target total-variation radius.
- Population regularity-gap theorem \(\widehat M\ge\Delta-4\varepsilon_Y-4Lr_Q\).
- General gap-allocation sample-size formulas and balanced-allocation corollary.
- Executable sample-complexity utilities, dedicated regression tests, and a publication theorem map.

### Corrected
- Repaired two malformed LaTeX escape sequences in the published P41 proof.
- Clarified that raw linear tomography reconstructions need not be physical density operators and their trace-norm reconstruction radius is not restricted to the unit interval.

### Scientific boundary
- P42 is conditional on the declared IC measurement, linear reconstruction map, IID sampling model, system boundary, independent target definition, and Lipschitz bridge class.
- The theorem supplies a sufficient experimental sample size for one declared regularity obstruction. It does not establish quantum incompleteness or consciousness.

'''
text = replace_once(text, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog P42")
path.write_text(text, encoding="utf-8")
