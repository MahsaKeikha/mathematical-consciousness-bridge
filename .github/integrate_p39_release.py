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
s = one(s, "version-0.38.0-2563eb", "version-0.39.0-2563eb", "badge")
s = one(
    s,
    "**P38** then specializes the physical-sufficiency program to a tomographically complete finite-dimensional quantum state descriptor and states the exact quantum non-factorization witness.",
    "**P38** then specializes the physical-sufficiency program to a tomographically complete finite-dimensional quantum state descriptor and states the exact quantum non-factorization witness. **P39** converts that exact population criterion into a finite-data model-set certificate that carries tomography-model uncertainty and target-distribution uncertainty without treating numerical closeness as exact quantum-state equality.",
    "abstract",
)
s = one(s, "**38 proposition-level results", "**39 proposition-level results", "count")
s = maybe(s, "P1 through P38 with explicit dependency branches", "P1 through P39 with explicit dependency branches")
s = maybe(s, "| proposition-level results | **38** |", "| proposition-level results | **39** |")
s = maybe(s, "| research-software version | **0.38.0** |", "| research-software version | **0.39.0** |")
s = maybe(s, "# 7. Theorem roadmap - P1 through P38", "# 7. Theorem roadmap - P1 through P39")
row = "| quantum operational sufficiency | [Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md) | exact factorization and non-factorization criterion for a tomographically complete quantum descriptor |"
s = one(s, row, row + "\n| finite-data quantum non-factorization | [Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md) | confidence-set rejection of declared quantum state-fiber models with explicit target uncertainty |", "nav")
row = "| implementation of P38 | [quantum_operational_sufficiency.py](src/consciousness_bridge/quantum_operational_sufficiency.py) | quantum operational factorization and residual utilities |"
s = one(s, row, row + "\n| implementation of P39 | [finite_data_quantum_nonfactorization.py](src/consciousness_bridge/finite_data_quantum_nonfactorization.py) | finite-data quantum model-set non-factorization certificate |", "impl")
row = "| **11.14 P38 quantum operational sufficiency** | Does an independently defined target factor through a tomographically complete quantum state descriptor? |"
s = one(s, row, row + "\n| **11.15 P39 finite-data quantum non-factorization** | Can finite data reject every quantum state-fiber hypothesis that survives the declared tomography analysis? |", "paper map")
row = "| **P38** | an independently defined target factors through a tomographically complete quantum state iff it is constant on quantum-state fibers; an exact collision proves non-factorization through that declared descriptor | proved quantum sufficiency theorem | [P38](docs/proposition_38_quantum_operational_sufficiency.md) |"
s = one(s, row, row + "\n| **P39** | simultaneous target-TV lower bounds are checked against every exact state-fiber hypothesis in a tomography confidence set; a positive worst-model margin certifies P38 non-factorization for the true declared model | proved finite-data model-set theorem | [P39](docs/proposition_39_finite_data_quantum_nonfactorization.md) |", "theorem table")
section = r'''## 13.12 P39 - finite-data quantum model-set non-factorization

![P39 finite-data quantum model-set non-factorization](docs/figures/p39_finite_data_quantum_nonfactorization.svg)

P38 is exact, but finite noisy tomography does not justify replacing equality of quantum states by a numerical closeness threshold. Distinct density operators can have arbitrarily small trace distance, so

\[
\boxed{
\text{small tomography distance}
\not\Rightarrow
\text{exact quantum-state equality}.
}
\]

P39 therefore uses a declared finite quantum hypothesis family \(\mathfrak H_Q\). Each hypothesis \(h\) explicitly specifies exact operational-state fibers through \(q_h\). A tomography analysis returns a confidence set \(\mathcal C_Q\) with

\[
\boxed{\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q.}
\]

For independently defined target laws, let simultaneous total-variation confidence radii satisfy

\[
\Pr\left(\|P_x-\widehat P_x\|_{\mathrm{TV}}\le\varepsilon_x\ \forall x\right)
\ge1-\alpha_Y.
\]

Define

\[
\boxed{
L_{xx'}=
\left[\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}-\varepsilon_x-\varepsilon_{x'}\right]_+.
}
\]

For one candidate quantum hypothesis,

\[
\boxed{V(h)=\max_{q_h(x)=q_h(x')}L_{xx'}.}
\]

A positive \(V(h)\) certifies a same-state pair whose true target laws differ on the target-confidence event. Over the complete tomography confidence set define

\[
\boxed{V_*=\min_{h\in\mathcal C_Q}V(h).}
\]

P39 proves

\[
\boxed{
V_*>0
\Longrightarrow
\text{the true declared quantum hypothesis fails P38 stochastic factorization}
}
\]

with confidence at least

\[
\boxed{1-\alpha_Q-\alpha_Y.}
\]

An injective surviving hypothesis has no same-state collision and therefore gives \(V(h)=0\), correctly blocking this certificate. The theorem therefore cannot manufacture non-factorization merely from target differences.

The interpretation boundary is strict:

\[
\boxed{
\text{all models in the declared quantum confidence set fail target factorization}
\neq
\text{quantum mechanics is incomplete}.
}
\]

A positive certificate can still reflect an overly narrow model family, an incorrect system boundary, omitted environmental degrees of freedom, preparation misspecification, target-measurement error, or nonstationarity. For an experiential application, the target must additionally be justified independently of the physical variables under test.

The next theorem target is continuous-region robust quantum sufficiency, replacing the finite hypothesis set by a physically admissible continuous confidence region and minimizing a factorization discrepancy over that entire region.

[Read Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md). The [P39 theorem map](docs/figures/p39_finite_data_quantum_nonfactorization.svg), [implementation](src/consciousness_bridge/finite_data_quantum_nonfactorization.py), and [tests](tests/test_finite_data_quantum_nonfactorization.py) expose the complete proof-to-code path.

'''
marker = "[Read Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md). The [P38 theorem map](docs/figures/p38_quantum_operational_sufficiency.svg), [implementation](src/consciousness_bridge/quantum_operational_sufficiency.py), and [tests](tests/test_quantum_operational_sufficiency.py) expose the proof-to-code path.\n\n---"
s = one(s, marker, marker[:-3] + section + "---", "P39 main section")
s = maybe(s, "the P1-P29 proposition chain", "the P1-P39 proposition chain")
p.write_text(s, encoding="utf-8")

# theorem roadmap
p = Path("docs/theorem_roadmap.md")
s = p.read_text(encoding="utf-8")
s = one(s, "![P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)", "![P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)\n\n![P39 finite-data quantum non-factorization](figures/p39_finite_data_quantum_nonfactorization.svg)", "roadmap figure")
row = "| [P38](proposition_38_quantum_operational_sufficiency.md) | factorization through tomographically complete density-operator fibers | exact quantum descriptor sufficiency and non-factorization witness | proved quantum sufficiency theorem |"
s = one(s, row, row + "\n| [P39](proposition_39_finite_data_quantum_nonfactorization.md) | target-TV confidence bounds plus tomography model-set coverage | finite-data rejection of every surviving exact quantum-state-fiber hypothesis | proved finite-data model-set theorem |", "roadmap row")
block = r'''## P39 - finite-data quantum model-set non-factorization

For simultaneous target-TV radii \(\varepsilon_x\),

\[
L_{xx'}=
\left[\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}-\varepsilon_x-\varepsilon_{x'}\right]_+.
\]

For each declared quantum hypothesis \(h\),

\[
V(h)=\max_{q_h(x)=q_h(x')}L_{xx'},
\qquad
V_*=\min_{h\in\mathcal C_Q}V(h).
\]

If the true quantum hypothesis belongs to \(\mathcal C_Q\) with probability at least \(1-\alpha_Q\), the target confidence event has probability at least \(1-\alpha_Y\), and \(V_*>0\), then the true declared quantum hypothesis fails P38 stochastic factorization with confidence at least \(1-\alpha_Q-\alpha_Y\).

The theorem never substitutes numerical state closeness for exact state equality. An injective surviving quantum model correctly blocks the collision-based certificate.

Direct proof: [Proposition 39](proposition_39_finite_data_quantum_nonfactorization.md). Implementation: [finite_data_quantum_nonfactorization.py](../src/consciousness_bridge/finite_data_quantum_nonfactorization.py). Tests: [test_finite_data_quantum_nonfactorization.py](../tests/test_finite_data_quantum_nonfactorization.py).

---

'''
s = one(s, "# 8. Fundamental physical sufficiency: P19", block + "# 8. Fundamental physical sufficiency: P19", "roadmap block")
p.write_text(s, encoding="utf-8")

# research navigation
p = Path("docs/research_navigation.md")
s = p.read_text(encoding="utf-8")
s = maybe(s, "from P1 through P38", "from P1 through P39")
row = "| P38 | [Quantum operational sufficiency](proposition_38_quantum_operational_sufficiency.md) | quantum factorization and non-factorization criterion |"
s = one(s, row, row + "\n| P39 | [Finite-data quantum non-factorization](proposition_39_finite_data_quantum_nonfactorization.md) | model-set confidence certificate for quantum descriptor non-factorization |", "navigation")
p.write_text(s, encoding="utf-8")

# equation and citation map
p = Path("docs/equation_and_citation_map.md")
s = p.read_text(encoding="utf-8")
block = r'''# 26. P32-P37 operational-scale closure

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\eta_{a\times b}\le\eta_a+\eta_b\) | joint intervention-delay ambiguity budget | proved | [P33](proposition_33_joint_operational_quotient.md) |
| \(D_G^{\mathrm{full}}\le2\rho_G^*+2\eta_{a\times b}\) | complete geometry-scale bound | proved | [P34](proposition_34_joint_p11_operational_scale.md) |
| \(D_A^{\mathrm{full}}\le2\rho_A^*+2\eta_{a\times b}\) | complete directed-influence bound | proved | [P35](proposition_35_approximate_directed_influence_operational_quotient.md) |
| \(|\kappa_\pi(P)-\kappa_\pi(Q)|\le(m+1)\|P-Q\|_{\mathrm{TV}}\) | partition-product perturbation bound | proved | [P36](proposition_36_partition_irreducibility_operational_quotient.md) |
| complete P11 max-norm distortion budget | simultaneous G/A/K scale certificate | proved | [P37](proposition_37_complete_approximate_p11_operational_scale.md) |

---

# 27. P38 quantum operational sufficiency

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(x\mapsto\rho_x\in\mathcal D(\mathcal H)\) | declared finite-dimensional quantum operational descriptor | repository specialization of standard density-operator formalism | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(\rho_x=\rho_{x'}\Rightarrow y(x)=y(x')\) | deterministic quantum sufficiency criterion | necessary and sufficient for factorization through the declared descriptor | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(I(Y;X\mid\rho_X)=0\) | stochastic quantum sufficiency criterion | population criterion | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(\rho_x=\rho_{x'}\) but \(y(x)\ne y(x')\) | exact descriptor-relative non-factorization witness | proved sufficient | [P38](proposition_38_quantum_operational_sufficiency.md) |

---

# 28. P39 finite-data quantum model-set non-factorization

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q\) | tomography model-set coverage assumption | declared input | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(L_{xx'}=[\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}-\varepsilon_x-\varepsilon_{x'}]_+\) | lower confidence bound on true target-law separation | proved by triangle inequality | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V(h)=\max_{q_h(x)=q_h(x')}L_{xx'}\) | model-specific P38 violation margin | repository definition | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V_*=\min_{h\in\mathcal C_Q}V(h)\) | worst surviving quantum-model margin | repository definition | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V_*>0\Rightarrow\) P38 non-factorization for the true declared model with confidence \(\ge1-\alpha_Q-\alpha_Y\) | finite-data robust model-set theorem | proved by simultaneous target bound plus union bound | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| small trace distance \(\not\Rightarrow\) exact state equality | blocks false collision certificates from noisy tomography | mathematical boundary | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |

P39 rejects only the declared quantum confidence set as sufficient for the independently defined target. It does not establish that quantum mechanics is incomplete or that the target is nonphysical.

---

'''
s = one(s, "# 26. Candidate consciousness-theory feature families", block + "# 29. Candidate consciousness-theory feature families", "citation insertion")
s = one(s, "# 27. Citation discipline", "# 30. Citation discipline", "citation renumber")
p.write_text(s, encoding="utf-8")

# metadata
p = Path("pyproject.toml")
s = p.read_text(encoding="utf-8")
s = one(s, 'version = "0.38.0"', 'version = "0.39.0"', "pyproject version")
s = one(s, "quantum operational sufficiency, recoverability", "quantum operational sufficiency, finite-data quantum model-set non-factorization, recoverability", "pyproject description")
p.write_text(s, encoding="utf-8")

p = Path("CITATION.cff")
s = p.read_text(encoding="utf-8")
s = one(s, "version: 0.38.0", "version: 0.39.0", "citation version")
s = one(s, "quantum operational sufficiency, robust experiment design", "quantum operational sufficiency, finite-data quantum model-set non-factorization, robust experiment design", "citation abstract")
p.write_text(s, encoding="utf-8")

p = Path("CHANGELOG.md")
s = p.read_text(encoding="utf-8")
entry = '''## 0.39.0 - 2026-09-09\n\n### Added\n- Proposition 39: finite-data quantum model-set non-factorization certification.\n- A target-law separation lower bound with simultaneous total-variation uncertainty.\n- A worst-model violation margin over a tomography-derived quantum confidence set.\n- Explicit proof that numerical quantum-state closeness is not exact state equality.\n- A guard showing that any surviving injective quantum model blocks the collision certificate.\n- Executable implementation, nine regression tests, and a publication theorem map.\n\n### Scientific boundary\n- P39 certifies non-factorization only relative to the declared quantum hypothesis family and its confidence set.\n- It does not prove quantum mechanics incomplete, consciousness nonphysical, or any target experiential without independent justification.\n\n'''
s = one(s, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog")
p.write_text(s, encoding="utf-8")

# public visibility guard
p = Path("tests/test_main_page_visual_paper.py")
s = p.read_text(encoding="utf-8")
s = one(s, '    "p38_quantum_operational_sufficiency.svg",', '    "p38_quantum_operational_sufficiency.svg",\n    "p39_finite_data_quantum_nonfactorization.svg",', "figure guard")
s = one(s, "for index in range(1, 39):", "for index in range(1, 40):", "proposition guard")
p.write_text(s, encoding="utf-8")

# release consistency guard
Path("tests/test_release_metadata_consistency.py").write_text('''import re\nfrom pathlib import Path\n\n\ndef test_release_versions_are_synchronized():\n    readme = Path("README.md").read_text(encoding="utf-8")\n    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")\n    citation = Path("CITATION.cff").read_text(encoding="utf-8")\n    assert "version-0.39.0-2563eb" in readme\n    assert re.search(r'^version = "0\\.39\\.0"$', pyproject, re.MULTILINE)\n    assert re.search(r'^version: 0\\.39\\.0$', citation, re.MULTILINE)\n\n\ndef test_p39_publication_paths_are_visible():\n    readme = Path("README.md").read_text(encoding="utf-8")\n    for token in (\n        "Proposition 39",\n        "p39_finite_data_quantum_nonfactorization.svg",\n        "finite_data_quantum_nonfactorization.py",\n        "test_finite_data_quantum_nonfactorization.py",\n    ):\n        assert token in readme\n''', encoding="utf-8")
