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
s = one(s, "version-0.39.0-2563eb", "version-0.40.0-2563eb", "badge")
s = one(
    s,
    "**P39** converts that exact population criterion into a finite-data model-set certificate that carries tomography-model uncertainty and target-distribution uncertainty without treating numerical closeness as exact quantum-state equality.",
    "**P39** converts that exact population criterion into a finite-data model-set certificate that carries tomography-model uncertainty and target-distribution uncertainty without treating numerical closeness as exact quantum-state equality. **P40** proves the corresponding continuous-region limitation: an injective finite quantum descriptor always permits unrestricted factorization on the sampled preparations, while a valid continuous-region obstruction requires an explicit bridge regularity class and compares target separation against the largest quantum separation allowed anywhere in the confidence region.",
    "abstract",
)
s = one(s, "**39 proposition-level results", "**40 proposition-level results", "count")
s = maybe(s, "P1 through P39 with explicit dependency branches", "P1 through P40 with explicit dependency branches")
s = maybe(s, "| proposition-level results | **39** |", "| proposition-level results | **40** |")
s = maybe(s, "| research-software version | **0.39.0** |", "| research-software version | **0.40.0** |")
s = maybe(s, "# 7. Theorem roadmap - P1 through P39", "# 7. Theorem roadmap - P1 through P40")
row = "| finite-data quantum non-factorization | [Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md) | confidence-set rejection of declared quantum state-fiber models with explicit target uncertainty |"
s = one(s, row, row + "\n| continuous quantum-region regularity | [Proposition 40](docs/proposition_40_continuous_quantum_region_regularity.md) | injective-descriptor no-go plus modulus-of-continuity obstruction over a continuous confidence region |", "nav")
row = "| implementation of P39 | [finite_data_quantum_nonfactorization.py](src/consciousness_bridge/finite_data_quantum_nonfactorization.py) | finite-data quantum model-set non-factorization certificate |"
s = one(s, row, row + "\n| implementation of P40 | [continuous_quantum_region_regularity.py](src/consciousness_bridge/continuous_quantum_region_regularity.py) | continuous-region bridge-regularity obstruction and injective-descriptor audit |", "impl")
row = "| **11.15 P39 finite-data quantum non-factorization** | Can finite data reject every quantum state-fiber hypothesis that survives the declared tomography analysis? |"
s = one(s, row, row + "\n| **11.16 P40 continuous quantum-region regularity** | What can finite data rule out when tomography leaves a continuous set of distinct quantum descriptors? |", "paper map")
row = "| **P39** | simultaneous target-TV lower bounds are checked against every exact state-fiber hypothesis in a tomography confidence set; a positive worst-model margin certifies P38 non-factorization for the true declared model | proved finite-data model-set theorem | [P39](docs/proposition_39_finite_data_quantum_nonfactorization.md) |"
s = one(s, row, row + "\n| **P40** | injective finite descriptors always admit unrestricted factorization on the sampled image; with a declared modulus of continuity, target separation exceeding the confidence-region quantum envelope yields a robust obstruction | proved no-go plus regularity theorem | [P40](docs/proposition_40_continuous_quantum_region_regularity.md) |", "theorem table")
section = r'''## 13.13 P40 - continuous quantum confidence regions and bridge regularity

![P40 continuous quantum confidence-region regularity](docs/figures/p40_continuous_quantum_region_regularity.svg)

P39 handles a finite family of exact state-fiber hypotheses. P40 asks what remains possible when tomography instead leaves a continuous set of admissible quantum descriptor assignments.

The first result is a no-go theorem. If a candidate descriptor \(Q:x\mapsto\rho_x\) is injective on the finite preparation set, then any target assignment can be written as

\[
\boxed{y=g\circ Q}
\]

for some unrestricted map \(g\) defined on the finite image of \(Q\). The same is true for arbitrary target distributions. Therefore

\[
\boxed{
\text{injective finite quantum descriptor}
+
\text{unrestricted bridge}
\Longrightarrow
\text{factorization is always possible on the sampled preparations}.
}
\]

This means small but nonzero trace distance cannot become a non-factorization witness by itself.

To obtain a continuous-region obstruction, P40 requires a declared bridge regularity class. Let \(\omega\) be a nondecreasing modulus with \(\omega(0)=0\) and require

\[
\boxed{
\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}
\le
\omega(D(\rho,\sigma)).
}
\]

For a quantum confidence region \(\mathcal C_Q\), define the largest pairwise state separation still allowed anywhere in that region:

\[
\boxed{
U_{xx'}=
\sup_{Q\in\mathcal C_Q}
D(\rho_x^Q,\rho_{x'}^Q).
}
\]

If simultaneous target analysis supplies

\[
L_{xx'}\le\|P_x-P_{x'}\|_{\mathrm{TV}},
\]

define

\[
\boxed{
M_{xx'}=L_{xx'}-\omega(U_{xx'}),
\qquad
M_*=\max_{x\ne x'}M_{xx'}.
}
\]

P40 proves

\[
\boxed{
M_*>0
\Longrightarrow
\text{no descriptor in }\mathcal C_Q
\text{ supports a bridge in the declared regularity class}.
}
\]

For an \(L\)-Lipschitz bridge, \(\omega(r)=Lr\), so one pair is obstructed whenever

\[
\boxed{L_{xx'}>L\,U_{xx'}.}
\]

This also gives a lower bound on the effective Lipschitz constant required by any bridge that could fit the pair.

The scientific boundary is essential:

\[
\boxed{
\text{no regular bridge in the declared quantum confidence region}
\neq
\text{no quantum explanation}.
}
\]

The regularity class is an additional bridge-model assumption, not a consequence of quantum mechanics. A positive obstruction may instead expose an inadequate system boundary, an overly narrow quantum confidence region, invalid target confidence bounds, omitted environmental variables, or an unjustified regularity assumption.

The next theorem target is end-to-end quantum tomography control: derive certified bounds on \(U_{xx'}\) directly from trace-norm or measurement-frequency confidence regions and propagate them into sample-complexity conditions for \(M_*>0\).

[Read Proposition 40](docs/proposition_40_continuous_quantum_region_regularity.md). The [P40 theorem map](docs/figures/p40_continuous_quantum_region_regularity.svg), [implementation](src/consciousness_bridge/continuous_quantum_region_regularity.py), and [tests](tests/test_continuous_quantum_region_regularity.py) expose the complete proof-to-code path.

'''
marker = "[Read Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md). The [P39 theorem map](docs/figures/p39_finite_data_quantum_nonfactorization.svg), [implementation](src/consciousness_bridge/finite_data_quantum_nonfactorization.py), and [tests](tests/test_finite_data_quantum_nonfactorization.py) expose the complete proof-to-code path.\n\n---"
s = one(s, marker, marker[:-3] + section + "---", "P40 section")
s = maybe(s, "the P1-P39 proposition chain", "the P1-P40 proposition chain")
p.write_text(s, encoding="utf-8")

# theorem roadmap
p = Path("docs/theorem_roadmap.md")
s = p.read_text(encoding="utf-8")
s = one(s, "![P39 finite-data quantum non-factorization](figures/p39_finite_data_quantum_nonfactorization.svg)", "![P39 finite-data quantum non-factorization](figures/p39_finite_data_quantum_nonfactorization.svg)\n\n![P40 continuous quantum-region regularity](figures/p40_continuous_quantum_region_regularity.svg)", "roadmap figure")
row = "| [P39](proposition_39_finite_data_quantum_nonfactorization.md) | target-TV confidence bounds plus tomography model-set coverage | finite-data rejection of every surviving exact quantum-state-fiber hypothesis | proved finite-data model-set theorem |"
s = one(s, row, row + "\n| [P40](proposition_40_continuous_quantum_region_regularity.md) | injective-image factorization plus confidence-region distance envelopes and bridge moduli | unrestricted-bridge no-go and continuous-region regularity obstruction | proved no-go plus regularity theorem |", "roadmap row")
block = r'''## P40 - continuous quantum-region regularity obstruction

If a finite quantum descriptor \(Q\) is injective on the sampled preparation set, then any target assignment factors through some unrestricted map on \(\operatorname{Im}(Q)\). Thus continuous quantum-state closeness alone cannot rule out unrestricted factorization.

For a declared bridge modulus \(\omega\), define

\[
U_{xx'}=\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q),
\qquad
M_{xx'}=L_{xx'}-\omega(U_{xx'}).
\]

Then

\[
\boxed{
M_*:=\max_{x\ne x'}M_{xx'}>0
}
\]

rules out every descriptor in the declared quantum confidence region for every bridge satisfying that modulus, on the joint confidence event.

Direct proof: [Proposition 40](proposition_40_continuous_quantum_region_regularity.md). Implementation: [continuous_quantum_region_regularity.py](../src/consciousness_bridge/continuous_quantum_region_regularity.py). Tests: [test_continuous_quantum_region_regularity.py](../tests/test_continuous_quantum_region_regularity.py).

---

'''
s = one(s, "# 8. Fundamental physical sufficiency: P19", block + "# 8. Fundamental physical sufficiency: P19", "roadmap block")
p.write_text(s, encoding="utf-8")

# research navigation
p = Path("docs/research_navigation.md")
s = p.read_text(encoding="utf-8")
s = maybe(s, "from P1 through P39", "from P1 through P40")
row = "| P39 | [Finite-data quantum non-factorization](proposition_39_finite_data_quantum_nonfactorization.md) | model-set confidence certificate for quantum descriptor non-factorization |"
s = one(s, row, row + "\n| P40 | [Continuous quantum-region regularity](proposition_40_continuous_quantum_region_regularity.md) | injective-descriptor no-go and continuous-region regularity obstruction |", "navigation")
p.write_text(s, encoding="utf-8")

# equation provenance
p = Path("docs/equation_and_citation_map.md")
s = p.read_text(encoding="utf-8")
block = r'''# 29. P40 continuous quantum-region regularity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| injective \(Q\) on finite \(\mathcal X\Rightarrow y=g\circ Q\) for arbitrary \(y\) | unrestricted-factorization no-go | proved by defining \(g\) on the finite image | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}\le\omega(D(\rho,\sigma))\) | declared bridge regularity class | explicit additional assumption | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(U_{xx'}=\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q)\) | worst allowed quantum separation over the continuous confidence region | repository definition | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(M_{xx'}=L_{xx'}-\omega(U_{xx'})\) | pairwise regularity obstruction margin | repository definition | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(M_*>0\) | robust incompatibility of the whole region with the declared bridge class | proved | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(\omega(r)=Lr\) | Lipschitz special case | standard regularity model specialized here | [P40](proposition_40_continuous_quantum_region_regularity.md) |

P40 does not infer bridge regularity from quantum mechanics. The modulus is an independently declared model restriction.

---

'''
s = one(s, "# 29. Candidate consciousness-theory feature families", block + "# 30. Candidate consciousness-theory feature families", "citation P40")
s = one(s, "# 30. Citation discipline", "# 31. Citation discipline", "citation renumber")
p.write_text(s, encoding="utf-8")

# metadata
p = Path("pyproject.toml")
s = p.read_text(encoding="utf-8")
s = one(s, 'version = "0.39.0"', 'version = "0.40.0"', "pyproject version")
s = one(s, "finite-data quantum model-set non-factorization, recoverability", "finite-data quantum model-set non-factorization, continuous quantum-region regularity obstruction, recoverability", "pyproject description")
p.write_text(s, encoding="utf-8")

p = Path("CITATION.cff")
s = p.read_text(encoding="utf-8")
s = one(s, "version: 0.39.0", "version: 0.40.0", "citation version")
s = one(s, "finite-data quantum model-set non-factorization, robust experiment design", "finite-data quantum model-set non-factorization, continuous quantum-region regularity obstruction, robust experiment design", "citation abstract")
p.write_text(s, encoding="utf-8")

p = Path("CHANGELOG.md")
s = p.read_text(encoding="utf-8")
entry = '''## 0.40.0 - 2026-09-09\n\n### Added\n- Proposition 40: continuous quantum confidence regions and bridge-regularity obstructions.\n- A no-go theorem showing that injective finite descriptors always permit unrestricted factorization on the sampled image.\n- A continuous confidence-region quantum-distance envelope.\n- A modulus-of-continuity obstruction and Lipschitz corollary.\n- Executable implementation, regression tests, publication map, and public-paper integration.\n\n### Scientific boundary\n- Bridge regularity is an additional modeling assumption and is not derived from quantum mechanics.\n- A positive P40 obstruction rules out only the declared quantum confidence region together with the declared bridge-regularity class.\n\n'''
s = one(s, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog")
p.write_text(s, encoding="utf-8")

# visibility and release guards
p = Path("tests/test_main_page_visual_paper.py")
s = p.read_text(encoding="utf-8")
s = one(s, '    "p39_finite_data_quantum_nonfactorization.svg",', '    "p39_finite_data_quantum_nonfactorization.svg",\n    "p40_continuous_quantum_region_regularity.svg",', "figure guard")
s = one(s, "for index in range(1, 40):", "for index in range(1, 41):", "proposition guard")
p.write_text(s, encoding="utf-8")

p = Path("tests/test_release_metadata_consistency.py")
s = p.read_text(encoding="utf-8")
s = s.replace("0.39.0", "0.40.0")
s = one(s, '        "test_finite_data_quantum_nonfactorization.py",', '        "test_finite_data_quantum_nonfactorization.py",\n        "Proposition 40",\n        "p40_continuous_quantum_region_regularity.svg",\n        "continuous_quantum_region_regularity.py",\n        "test_continuous_quantum_region_regularity.py",', "release guard P40")
p.write_text(s, encoding="utf-8")
