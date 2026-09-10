from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1) if old in text else text


# README main paper
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.38.0-2563eb", "version-0.39.0-2563eb", "README version")
text = replace_once(
    text,
    "**P38** then specializes the physical-sufficiency program to a tomographically complete finite-dimensional quantum state descriptor and states the exact quantum non-factorization witness.",
    "**P38** then specializes the physical-sufficiency program to a tomographically complete finite-dimensional quantum state descriptor and states the exact quantum non-factorization witness. **P39** proves a finite-data model-set certificate that carries both tomography-model uncertainty and target-distribution uncertainty without converting numerical closeness into exact quantum-state equality.",
    "README abstract P39",
)
text = replace_once(text, "**38 proposition-level results", "**39 proposition-level results", "README public count")
text = replace_if_present(text, "P1 through P38 with explicit dependency branches", "P1 through P39 with explicit dependency branches")
text = replace_if_present(text, "| proposition-level results | **38** |", "| proposition-level results | **39** |")
text = replace_if_present(text, "| research-software version | **0.38.0** |", "| research-software version | **0.39.0** |")
text = replace_if_present(text, "# 7. Theorem roadmap - P1 through P38", "# 7. Theorem roadmap - P1 through P39")

nav = "| quantum operational sufficiency | [Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md) | exact factorization and non-factorization criterion for a tomographically complete quantum descriptor |"
text = replace_once(
    text,
    nav,
    nav + "\n| finite-data quantum non-factorization | [Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md) | model-set confidence certificate with explicit target uncertainty and no false exact-equality inference |",
    "README nav P39",
)
impl = "| implementation of P38 | [quantum_operational_sufficiency.py](src/consciousness_bridge/quantum_operational_sufficiency.py) | quantum operational factorization and residual utilities |"
text = replace_once(
    text,
    impl,
    impl + "\n| implementation of P39 | [finite_data_quantum_nonfactorization.py](src/consciousness_bridge/finite_data_quantum_nonfactorization.py) | robust quantum confidence-set non-factorization audit |",
    "README implementation P39",
)
paper = "| **11.14 P38 quantum operational sufficiency** | Does an independently defined target factor through a tomographically complete quantum state descriptor? |"
text = replace_once(
    text,
    paper,
    paper + "\n| **11.15 P39 finite-data quantum non-factorization** | Can finite data reject every quantum operational hypothesis surviving the declared tomography confidence analysis? |",
    "README paper map P39",
)
table = "| **P38** | an independently defined target factors through a tomographically complete quantum state iff it is constant on quantum-state fibers; an exact collision proves non-factorization through that declared descriptor | proved quantum sufficiency theorem | [P38](docs/proposition_38_quantum_operational_sufficiency.md) |"
text = replace_once(
    text,
    table,
    table + "\n| **P39** | target-separation confidence bounds are tested against every exact state-fiber hypothesis in a tomography confidence set; a positive worst-model margin certifies P38 non-factorization for the true declared model with union-bound confidence | proved finite-data model-set theorem | [P39](docs/proposition_39_finite_data_quantum_nonfactorization.md) |",
    "README theorem table P39",
)

p39_section = r'''## 13.12 P39 - finite-data quantum model-set non-factorization

![P39 finite-data quantum model-set non-factorization](docs/figures/p39_finite_data_quantum_nonfactorization.svg)

P38 gives an exact population witness, but noisy tomography creates a crucial finite-data problem: two estimated density operators can be arbitrarily close without being exactly equal. For

\[
\rho_0=\frac{I}{2},
\qquad
\rho_\delta=
\begin{pmatrix}
1/2+\delta&0\\
0&1/2-\delta
\end{pmatrix},
\]

one has

\[
D(\rho_0,\rho_\delta)=\delta
\]

while \(\rho_0\ne\rho_\delta\) for every \(\delta>0\). Therefore

\[
\boxed{
\text{small tomography distance}
\not\Rightarrow
\text{exact quantum-state equality}.
}
\]

P39 avoids that error by working with a declared finite family \(\mathfrak H_Q\) of quantum operational hypotheses. Each hypothesis \(h\) explicitly encodes exact state fibers through a map \(q_h\). A tomography analysis supplies a confidence set \(\mathcal C_Q\) satisfying

\[
\boxed{
\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q.
}
\]

For independently defined target laws \(P_x\), suppose simultaneous total-variation confidence radii satisfy

\[
\Pr\left(
\|P_x-\widehat P_x\|_{\mathrm{TV}}\le\varepsilon_x
\quad\forall x
\right)
\ge1-\alpha_Y.
\]

Define the pairwise true-separation lower bound

\[
\boxed{
L_{xx'}=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-\varepsilon_x-\varepsilon_{x'}
\right]_+.
}
\]

For candidate quantum hypothesis \(h\), define

\[
\boxed{
V(h)
=
\max_{q_h(x)=q_h(x')}L_{xx'}.
}
\]

A positive \(V(h)\) means that hypothesis \(h\) contains an exact same-state pair whose true target laws must differ on the target-confidence event. Hence \(h\) violates the P38 stochastic factorization criterion.

Now define

\[
\boxed{
V_*=\min_{h\in\mathcal C_Q}V(h).
}
\]

P39 proves

\[
\boxed{
V_*>0
\Longrightarrow
\text{the true declared quantum hypothesis fails P38 factorization}
}
\]

with confidence at least

\[
\boxed{1-\alpha_Q-\alpha_Y.}
\]

This uses only the union bound; statistical independence of the tomography and target data sets is not required for this coverage statement.

The theorem also exposes a necessary limitation. If even one surviving hypothesis assigns a distinct quantum operational state to every preparation, then it contains no same-state collision and \(V(h)=0\). Such an injective hypothesis correctly blocks a P39 certificate. Target differences alone cannot refute factorization when the physical model can still encode every preparation distinctly.

The conclusion is therefore deliberately narrow:

\[
\boxed{
\text{all quantum hypotheses in the declared confidence set fail target factorization}
\neq
\text{quantum mechanics is incomplete}.
}
\]

A positive certificate can still indicate a restricted hypothesis class, incorrect system boundary, omitted environment degrees of freedom, preparation misspecification, target-measurement error, or nonstationarity. For an experiential application, the target must additionally be defined independently of the physical variables being tested.

The next theorem target is a continuous-confidence-region version that does not require discrete exact-equality hypotheses. The mathematically natural route is to minimize a factorization discrepancy over every physically admissible quantum descriptor in a continuous confidence region and ask whether that infimum remains strictly positive.

[Read Proposition 39](docs/proposition_39_finite_data_quantum_nonfactorization.md). The [P39 theorem map](docs/figures/p39_finite_data_quantum_nonfactorization.svg), [implementation](src/consciousness_bridge/finite_data_quantum_nonfactorization.py), and [tests](tests/test_finite_data_quantum_nonfactorization.py) expose the proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md). The [P38 theorem map](docs/figures/p38_quantum_operational_sufficiency.svg), [implementation](src/consciousness_bridge/quantum_operational_sufficiency.py), and [tests](tests/test_quantum_operational_sufficiency.py) expose the proof-to-code path.\n\n---",
    "[Read Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md). The [P38 theorem map](docs/figures/p38_quantum_operational_sufficiency.svg), [implementation](src/consciousness_bridge/quantum_operational_sufficiency.py), and [tests](tests/test_quantum_operational_sufficiency.py) expose the proof-to-code path.\n\n" + p39_section + "---",
    "README P39 section",
)
text = replace_if_present(text, "the P1-P29 proposition chain", "the P1-P39 proposition chain")
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)",
    "![P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)\n\n![P39 finite-data quantum non-factorization](figures/p39_finite_data_quantum_nonfactorization.svg)",
    "roadmap P39 figure",
)
row = "| [P38](proposition_38_quantum_operational_sufficiency.md) | factorization through tomographically complete density-operator fibers | exact quantum descriptor sufficiency and non-factorization witness | proved quantum sufficiency theorem |"
text = replace_once(
    text,
    row,
    row + "\n| [P39](proposition_39_finite_data_quantum_nonfactorization.md) | simultaneous target-TV lower bounds plus tomography model-set coverage | finite-data rejection of every surviving exact quantum-state-fiber hypothesis | proved finite-data model-set theorem |",
    "roadmap P39 index",
)
insert = r'''## P39 - finite-data quantum model-set non-factorization

For target estimates \(\widehat P_x\) with simultaneous TV radii \(\varepsilon_x\), define

\[
L_{xx'}=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-\varepsilon_x-\varepsilon_{x'}
\right]_+.
\]

For a declared quantum operational hypothesis \(h\),

\[
\boxed{
V(h)=\max_{q_h(x)=q_h(x')}L_{xx'}.
}
\]

Given a tomography confidence set \(\mathcal C_Q\), define

\[
\boxed{V_*=\min_{h\in\mathcal C_Q}V(h).}
\]

If \(\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q\) and the simultaneous target-confidence event has probability at least \(1-\alpha_Y\), then

\[
\boxed{
V_*>0
\Longrightarrow
h_*\text{ fails P38 stochastic factorization}
}
\]

with confidence at least \(1-\alpha_Q-\alpha_Y\).

P39 also proves why numerical closeness cannot be substituted for exact quantum-state equality: distinct density operators exist at arbitrarily small trace distance. An injective quantum model in the confidence set therefore correctly blocks this collision-based certificate.

Direct proof: [Proposition 39](proposition_39_finite_data_quantum_nonfactorization.md). Implementation: [finite_data_quantum_nonfactorization.py](../src/consciousness_bridge/finite_data_quantum_nonfactorization.py). Tests: [test_finite_data_quantum_nonfactorization.py](../tests/test_finite_data_quantum_nonfactorization.py).

'''
text = replace_once(text, "# 8. Fundamental physical sufficiency: P19", insert + "# 8. Fundamental physical sufficiency: P19", "roadmap P39 section")
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_if_present(text, "from P1 through P38", "from P1 through P39")
row = "| P38 | [Quantum operational sufficiency](proposition_38_quantum_operational_sufficiency.md) | quantum factorization and non-factorization criterion |"
text = replace_once(
    text,
    row,
    row + "\n| P39 | [Finite-data quantum non-factorization](proposition_39_finite_data_quantum_nonfactorization.md) | model-set confidence certificate for quantum descriptor non-factorization |",
    "navigation P39 index",
)
fundamental_row = "| [P31 intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact operational intervention quotient and representative-stability bounds |"
if fundamental_row in text and "[P38 quantum operational sufficiency]" not in text:
    text = text.replace(
        fundamental_row,
        fundamental_row + "\n| [P38 quantum operational sufficiency](proposition_38_quantum_operational_sufficiency.md) | exact factorization criterion for a tomographically complete quantum descriptor |\n| [P39 finite-data quantum non-factorization](proposition_39_finite_data_quantum_nonfactorization.md) | tomography model-set and target-confidence certificate |",
        1,
    )
path.write_text(text, encoding="utf-8")

# Equation provenance: fill the publication gap from P32 through P39.
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")n
