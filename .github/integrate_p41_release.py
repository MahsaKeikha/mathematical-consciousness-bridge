from pathlib import Path


def one(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def maybe(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1) if old in text else text


# README
p = Path("README.md")
s = p.read_text(encoding="utf-8")
s = one(s, "version-0.40.0-2563eb", "version-0.41.0-2563eb", "badge")
s = one(
    s,
    "**P40** proves the corresponding continuous-region limitation: an injective finite quantum descriptor always permits unrestricted factorization on the sampled preparations, while a valid continuous-region obstruction requires an explicit bridge regularity class and compares target separation against the largest quantum separation allowed anywhere in the confidence region.",
    "**P40** proves the corresponding continuous-region limitation: an injective finite quantum descriptor always permits unrestricted factorization on the sampled preparations, while a valid continuous-region obstruction requires an explicit bridge regularity class and compares target separation against the largest quantum separation allowed anywhere in the confidence region. **P41** makes that continuous-region theorem directly computable for trace-distance tomography balls, converting per-preparation quantum and target confidence radii into an end-to-end regularity obstruction and an explicit uncertainty budget.",
    "abstract",
)
s = one(s, "**40 proposition-level results", "**41 proposition-level results", "count")
s = maybe(s, "P1 through P40 with explicit dependency branches", "P1 through P41 with explicit dependency branches")
s = maybe(s, "| proposition-level results | **40** |", "| proposition-level results | **41** |")
s = maybe(s, "| research-software version | **0.40.0** |", "| research-software version | **0.41.0** |")
s = maybe(s, "# 7. Theorem roadmap - P1 through P40", "# 7. Theorem roadmap - P1 through P41")
row = "| continuous quantum-region regularity | [Proposition 40](docs/proposition_40_continuous_quantum_region_regularity.md) | injective-descriptor no-go plus modulus-of-continuity obstruction over a continuous confidence region |"
s = one(s, row, row + "\n| trace-ball quantum envelope | [Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md) | analytic pairwise quantum envelope and end-to-end Lipschitz obstruction from simultaneous trace-distance and target-TV balls |", "nav")
row = "| implementation of P40 | [continuous_quantum_region_regularity.py](src/consciousness_bridge/continuous_quantum_region_regularity.py) | continuous-region bridge-regularity obstruction and injective-descriptor audit |"
s = one(s, row, row + "\n| implementation of P41 | [trace_ball_quantum_envelope.py](src/consciousness_bridge/trace_ball_quantum_envelope.py) | trace-ball quantum envelope and global Lipschitz obstruction certificate |", "impl")
row = "| **11.16 P40 continuous quantum-region regularity** | What can finite data rule out when tomography leaves a continuous set of distinct quantum descriptors? |"
s = one(s, row, row + "\n| **11.17 P41 trace-ball quantum envelope** | How can per-preparation trace-distance and target-TV confidence balls yield a directly computable P40 obstruction? |", "paper map")
row = "| **P40** | injective finite descriptors always admit unrestricted factorization on the sampled image; with a declared modulus of continuity, target separation exceeding the confidence-region quantum envelope yields a robust obstruction | proved no-go plus regularity theorem | [P40](docs/proposition_40_continuous_quantum_region_regularity.md) |"
s = one(s, row, row + "\n| **P41** | simultaneous trace-distance balls imply a pairwise quantum upper envelope; combining it with target-TV lower confidence and a declared bridge modulus yields an end-to-end obstruction | proved confidence-envelope theorem | [P41](docs/proposition_41_trace_ball_quantum_envelope.md) |", "theorem table")
section = r'''## 13.14 P41 - trace-ball quantum envelope and end-to-end certification

![P41 trace-ball quantum envelope](docs/figures/p41_trace_ball_quantum_envelope.svg)

P40 defines the continuous-region quantity

\[
U_{xx'}=
\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q),
\]

but computing that supremum may require a difficult optimization over the complete tomography confidence region. P41 gives a direct analytic bound when tomography supplies simultaneous trace-distance balls

\[
D(\rho_x,\widehat\rho_x)\le r_x.
\]

For each preparation pair, triangle inequality gives

\[
\boxed{
D(\rho_x,\rho_{x'})
\le
U^{\mathrm{ball}}_{xx'}
:=
\min\left\{1,
D(\widehat\rho_x,\widehat\rho_{x'})+r_x+r_{x'}
\right\}.
}
\]

Therefore the exact P40 region supremum satisfies

\[
\boxed{U_{xx'}\le U^{\mathrm{ball}}_{xx'}.}
\]

For independently estimated target laws with simultaneous TV radii \(\varepsilon_x\), P41 also gives

\[
\boxed{
L^{\mathrm{ball}}_{xx'}
=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-\varepsilon_x-\varepsilon_{x'}
\right]_+
\le
\|P_x-P_{x'}\|_{\mathrm{TV}}.
}
\]

For a declared bridge modulus \(\omega\), the fully computable sufficient obstruction becomes

\[
\boxed{
L^{\mathrm{ball}}_{xx'}
>
\omega(U^{\mathrm{ball}}_{xx'}).
}
\]

For an \(L\)-Lipschitz bridge,

\[
\boxed{
M^{\mathrm{ball}}_{xx'}
=
L^{\mathrm{ball}}_{xx'}
-LU^{\mathrm{ball}}_{xx'}.
}
\]

A positive maximum over preparation pairs rules out the declared Lipschitz bridge class throughout the complete trace-ball quantum confidence region, on the joint confidence event.

In the unsaturated symmetric-error regime, a conservative design inequality is

\[
\boxed{
d_Y-Ld_Q>2\varepsilon+2Lr.}
\]

The left side is the population regularity gap. The right side is the combined uncertainty cost. This decomposition tells an experimentalist whether the current limitation is quantum-state precision, target precision, or the assumed bridge regularity.

If the simultaneous quantum and target confidence events have failure probabilities \(\alpha_Q\) and \(\alpha_Y\), respectively, the P41 certificate has confidence at least

\[
\boxed{\max\{0,1-\alpha_Q-\alpha_Y\}.}
\]

The scientific boundary remains unchanged:

\[
\boxed{
\text{positive trace-ball regularity obstruction}
\neq
\text{proof that quantum mechanics is incomplete}.
}
\]

P41 applies only to the declared trace-ball confidence region, independent target confidence bounds, and bridge regularity class. The next theorem burden is to insert explicit sample-size-dependent tomography and target radii into the design inequality and solve for sufficient experiment sizes.

[Read Proposition 41](docs/proposition_41_trace_ball_quantum_envelope.md). The [P41 theorem map](docs/figures/p41_trace_ball_quantum_envelope.svg), [implementation](src/consciousness_bridge/trace_ball_quantum_envelope.py), and [tests](tests/test_trace_ball_quantum_envelope.py) expose the complete proof-to-code path.

'''
marker = "[Read Proposition 40](docs/proposition_40_continuous_quantum_region_regularity.md). The [P40 theorem map](docs/figures/p40_continuous_quantum_region_regularity.svg), [implementation](src/consciousness_bridge/continuous_quantum_region_regularity.py), and [tests](tests/test_continuous_quantum_region_regularity.py) expose the complete proof-to-code path.\n\n---"
s = one(s, marker, marker[:-3] + section + "---", "P41 section")
s = maybe(s, "the P1-P40 proposition chain", "the P1-P41 proposition chain")
p.write_text(s, encoding="utf-8")

# theorem roadmap
p = Path("docs/theorem_roadmap.md")
s = p.read_text(encoding="utf-8")
s = one(s, "![P40 continuous quantum-region regularity](figures/p40_continuous_quantum_region_regularity.svg)", "![P40 continuous quantum-region regularity](figures/p40_continuous_quantum_region_regularity.svg)\n\n![P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)", "roadmap figure")
row = "| [P40](proposition_40_continuous_quantum_region_regularity.md) | injective-image factorization plus confidence-region distance envelopes and bridge moduli | unrestricted-bridge no-go and continuous-region regularity obstruction | proved no-go plus regularity theorem |"
s = one(s, row, row + "\n| [P41](proposition_41_trace_ball_quantum_envelope.md) | trace-distance triangle inequality plus simultaneous quantum and target confidence balls | analytic P40 envelope and end-to-end regularity obstruction | proved confidence-envelope theorem |", "roadmap row")
block = r'''## P41 - trace-ball quantum envelope

If tomography gives simultaneous trace-distance balls

\[
D(\rho_x,\widehat\rho_x)\le r_x,
\]

then

\[
\boxed{
U_{xx'}
\le
U^{\mathrm{ball}}_{xx'}
=
\min\{1,D(\widehat\rho_x,\widehat\rho_{x'})+r_x+r_{x'}\}.
}
\]

Combining this with target-TV confidence gives a direct P40 obstruction

\[
\boxed{
L^{\mathrm{ball}}_{xx'}>
\omega(U^{\mathrm{ball}}_{xx'}).
}
\]

For an \(L\)-Lipschitz bridge and symmetric uncertainty, the design inequality is

\[
\boxed{d_Y-Ld_Q>2\varepsilon+2Lr.}
\]

Direct proof: [Proposition 41](proposition_41_trace_ball_quantum_envelope.md). Implementation: [trace_ball_quantum_envelope.py](../src/consciousness_bridge/trace_ball_quantum_envelope.py). Tests: [test_trace_ball_quantum_envelope.py](../tests/test_trace_ball_quantum_envelope.py).

---

'''
s = one(s, "# 8. Fundamental physical sufficiency: P19", block + "# 8. Fundamental physical sufficiency: P19", "roadmap block")
p.write_text(s, encoding="utf-8")

# research navigation
p = Path("docs/research_navigation.md")
s = p.read_text(encoding="utf-8")
s = maybe(s, "from P1 through P40", "from P1 through P41")
row = "| P40 | [Continuous quantum-region regularity](proposition_40_continuous_quantum_region_regularity.md) | injective-descriptor no-go and continuous-region regularity obstruction |"
s = one(s, row, row + "\n| P41 | [Trace-ball quantum envelope](proposition_41_trace_ball_quantum_envelope.md) | analytic continuous-region envelope and end-to-end Lipschitz certificate |", "navigation")
p.write_text(s, encoding="utf-8")

# equation provenance
p = Path("docs/equation_and_citation_map.md")
s = p.read_text(encoding="utf-8")
block = r'''# 30. P41 trace-ball quantum envelope

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D(\rho_x,\rho_{x'})\le D(\widehat\rho_x,\widehat\rho_{x'})+r_x+r_{x'}\) | true quantum pairwise distance control from simultaneous trace balls | standard triangle inequality applied here | standard trace distance; [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(U^{\mathrm{ball}}_{xx'}=\min\{1,\widehat D^Q_{xx'}+r_x+r_{x'}\}\) | analytic outer bound on the P40 confidence-region envelope | repository construction | [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(L^{\mathrm{ball}}_{xx'}=[\widehat D^Y_{xx'}-\varepsilon_x-\varepsilon_{x'}]_+\) | target-law lower confidence separation | triangle inequality | [P39](proposition_39_finite_data_quantum_nonfactorization.md); [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(L^{\mathrm{ball}}_{xx'}>\omega(U^{\mathrm{ball}}_{xx'})\) | end-to-end continuous-region regularity obstruction | proved | [P40](proposition_40_continuous_quantum_region_regularity.md); [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(M^{\mathrm{ball}}=L^{\mathrm{ball}}-LU^{\mathrm{ball}}\) | Lipschitz obstruction margin | repository definition | [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(d_Y-Ld_Q>2\varepsilon+2Lr\) | symmetric unsaturated experimental design condition | derived sufficient inequality | [P41](proposition_41_trace_ball_quantum_envelope.md) |

P41 assumes valid simultaneous confidence balls. It does not itself derive their statistical radii.

---

'''
s = one(s, "# 30. Candidate consciousness-theory feature families", block + "# 31. Candidate consciousness-theory feature families", "citation P41")
s = one(s, "# 31. Citation discipline", "# 32. Citation discipline", "citation renumber")
p.write_text(s, encoding="utf-8")

# metadata
p = Path("pyproject.toml")
s = p.read_text(encoding="utf-8")
s = one(s, 'version = "0.40.0"', 'version = "0.41.0"', "pyproject version")
s = one(s, "continuous quantum-region regularity obstruction, recoverability", "continuous quantum-region regularity obstruction, trace-ball quantum envelope certification, recoverability", "pyproject description")
p.write_text(s, encoding="utf-8")

p = Path("CITATION.cff")
s = p.read_text(encoding="utf-8")
s = one(s, "version: 0.40.0", "version: 0.41.0", "citation version")
s = one(s, "continuous quantum-region regularity obstruction, robust experiment design", "continuous quantum-region regularity obstruction, trace-ball quantum envelope certification, robust experiment design", "citation abstract")
p.write_text(s, encoding="utf-8")

p = Path("CHANGELOG.md")
s = p.read_text(encoding="utf-8")
entry = '''## 0.41.0 - 2026-09-09\n\n### Added\n- Proposition 41: trace-ball quantum envelopes and end-to-end regularity certification.\n- Analytic upper bounds on the P40 continuous quantum confidence-region envelope.\n- Target-TV lower confidence envelopes and a direct Lipschitz obstruction margin.\n- A symmetric finite-error experiment-design inequality.\n- Executable implementation, regression tests, publication map, and public-paper integration.\n\n### Scientific boundary\n- P41 assumes the declared quantum and target confidence balls have valid simultaneous coverage.\n- A positive P41 obstruction rejects only the declared trace-ball region together with the declared bridge regularity class.\n\n'''
s = one(s, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog")
p.write_text(s, encoding="utf-8")

# visibility and release guards
p = Path("tests/test_main_page_visual_paper.py")
s = p.read_text(encoding="utf-8")
s = one(s, '    "p40_continuous_quantum_region_regularity.svg",', '    "p40_continuous_quantum_region_regularity.svg",\n    "p41_trace_ball_quantum_envelope.svg",', "figure guard")
s = one(s, "for index in range(1, 41):", "for index in range(1, 42):", "proposition guard")
p.write_text(s, encoding="utf-8")

p = Path("tests/test_release_metadata_consistency.py")
s = p.read_text(encoding="utf-8")
s = s.replace("0.40.0", "0.41.0")
s = s.replace(r"0\.40\.0", r"0\.41\.0")
s = one(s, '        "test_continuous_quantum_region_regularity.py",', '        "test_continuous_quantum_region_regularity.py",\n        "Proposition 41",\n        "p41_trace_ball_quantum_envelope.svg",\n        "trace_ball_quantum_envelope.py",\n        "test_trace_ball_quantum_envelope.py",', "release guard P41")
p.write_text(s, encoding="utf-8")
