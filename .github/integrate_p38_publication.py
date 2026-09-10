from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1) if old in text else text


# Main research paper
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.31.0-2563eb", "version-0.38.0-2563eb", "README badge")
text = replace_once(
    text,
    "**P31** formalizes intervention-label quotienting itself: a many-to-one intervention map defines a unique coarse response law exactly when every retained response law is constant on each intervention fiber, and the quotient ambiguity defect quantifies representative dependence when exact descent fails.",
    "**P31** formalizes intervention-label quotienting itself: a many-to-one intervention map defines a unique coarse response law exactly when every retained response law is constant on each intervention fiber, and the quotient ambiguity defect quantifies representative dependence when exact descent fails. **P32** gives the corresponding exact delay quotient. **P33** proves joint intervention-delay quotient descent and the additive ambiguity bound. **P34** assembles node, state, intervention, and delay scale maps under one declared transformation. **P35** proves approximate directed-influence stability. **P36** propagates response ambiguity through partition-product irreducibility. **P37** combines all three P11 branches into one complete approximate operational-scale certificate. **P38** then specializes the physical-sufficiency program to a tomographically complete finite-dimensional quantum state descriptor and states the exact quantum non-factorization witness.",
    "README abstract P32-P38",
)
text = replace_once(text, "**31 proposition-level results", "**38 proposition-level results", "README public record")
text = replace_if_present(text, "P1 through P31 with explicit dependency branches", "P1 through P38 with explicit dependency branches")
text = replace_if_present(text, "| proposition-level results | **30** |", "| proposition-level results | **38** |")
text = replace_if_present(text, "| proposition-level results | **31** |", "| proposition-level results | **38** |")
text = replace_if_present(text, "| research-software version | **0.30.0** |", "| research-software version | **0.38.0** |")
text = replace_if_present(text, "| research-software version | **0.31.0** |", "| research-software version | **0.38.0** |")
text = replace_if_present(text, "# 7. Theorem roadmap - P1 through P31", "# 7. Theorem roadmap - P1 through P38")

nav_marker = "| intervention-quotient theorem | [Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent, quotient ambiguity defect, and representative-stability bound |"
nav_rows = nav_marker + "\n" + "\n".join([
    "| delay-quotient theorem | [Proposition 32](docs/proposition_32_delay_quotient_compatibility.md) | exact temporal-label descent and delay-fiber ambiguity control |",
    "| joint operational quotient | [Proposition 33](docs/proposition_33_joint_operational_quotient.md) | product-fiber descent and additive intervention-time ambiguity |",
    "| joint P11 operational scale | [Proposition 34](docs/proposition_34_joint_p11_operational_scale.md) | simultaneous node/state/intervention/time scale declaration |",
    "| directed-influence quotient stability | [Proposition 35](docs/proposition_35_approximate_directed_influence_operational_quotient.md) | approximate influence and threshold-edge stability |",
    "| partition quotient stability | [Proposition 36](docs/proposition_36_partition_irreducibility_operational_quotient.md) | product-reference perturbation and irreducibility stability |",
    "| complete approximate P11 scale | [Proposition 37](docs/proposition_37_complete_approximate_p11_operational_scale.md) | one quantitative distortion budget for G, A, and K |",
    "| quantum operational sufficiency | [Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md) | exact factorization and non-factorization criterion for a tomographically complete quantum descriptor |",
])
text = replace_once(text, nav_marker, nav_rows, "README navigation P32-P38")

impl_marker = "| implementation of P31 | [intervention_quotient_compatibility.py](src/consciousness_bridge/intervention_quotient_compatibility.py) | exact intervention-label quotient audit and ambiguity/stability certificate |"
impl_rows = impl_marker + "\n" + "\n".join([
    "| implementation of P32 | [delay_quotient_compatibility.py](src/consciousness_bridge/delay_quotient_compatibility.py) | delay quotient and ambiguity certification |",
    "| implementation of P33 | [joint_operational_quotient.py](src/consciousness_bridge/joint_operational_quotient.py) | joint intervention-delay quotient audit |",
    "| implementation of P34 | [joint_p11_operational_scale.py](src/consciousness_bridge/joint_p11_operational_scale.py) | joint P11 scale assembly |",
    "| implementation of P35 | [directed_influence_operational_quotient.py](src/consciousness_bridge/directed_influence_operational_quotient.py) | directed-influence quotient stability |",
    "| implementation of P37 | [complete_p11_operational_scale.py](src/consciousness_bridge/complete_p11_operational_scale.py) | complete approximate P11 scale budget |",
    "| implementation of P38 | [quantum_operational_sufficiency.py](src/consciousness_bridge/quantum_operational_sufficiency.py) | quantum operational factorization and residual utilities |",
])
text = replace_once(text, impl_marker, impl_rows, "README implementations P32-P38")

paper_marker = "| **11.7 P31 intervention quotient compatibility** | When may several fine intervention labels be represented by one coarse intervention without representative-dependent response laws? |"
paper_rows = paper_marker + "\n" + "\n".join([
    "| **11.8 P32 delay quotient compatibility** | When may several fine delays descend to one coarse temporal label? |",
    "| **11.9 P33 joint operational quotient** | How do intervention and delay ambiguity compose on the experiment grid? |",
    "| **11.10 P34 joint P11 scale** | When can node, state, intervention, and time changes be declared together? |",
    "| **11.11 P35 directed-influence quotient stability** | How much can quotient ambiguity perturb directed influence? |",
    "| **11.12 P36 partition quotient stability** | How does response ambiguity propagate through a partition-product reference? |",
    "| **11.13 P37 complete approximate P11 scale** | What is the full simultaneous distortion budget for G, A, and K? |",
    "| **11.14 P38 quantum operational sufficiency** | Does an independently defined target factor through a tomographically complete quantum state descriptor? |",
])
text = replace_once(text, paper_marker, paper_rows, "README paper map P32-P38")

table_marker = "| **P31** | an intervention quotient descends exactly iff response laws are constant on every intervention fiber; nonzero quotient ambiguity bounds representative-dependent coarse geometry | proved operational quotient theorem | [P31](docs/proposition_31_intervention_quotient_compatibility.md) |"
table_rows = table_marker + "\n" + "\n".join([
    "| **P32** | a delay quotient descends exactly iff response laws are constant on every temporal fiber | proved operational quotient theorem | [P32](docs/proposition_32_delay_quotient_compatibility.md) |",
    "| **P33** | joint intervention-delay ambiguity is the product-fiber diameter and is bounded by the sum of separate ambiguities | proved joint quotient theorem | [P33](docs/proposition_33_joint_operational_quotient.md) |",
    "| **P34** | exact full P11 transport requires one joint scale declaration; response geometry has an additive approximate bound | proved assembly theorem | [P34](docs/proposition_34_joint_p11_operational_scale.md) |",
    "| **P35** | semantically descendable directed influence changes by at most twice the joint operational ambiguity | proved perturbation theorem | [P35](docs/proposition_35_approximate_directed_influence_operational_quotient.md) |",
    "| **P36** | m-block partition irreducibility changes by at most (m+1) times response-law ambiguity | proved product-reference perturbation theorem | [P36](docs/proposition_36_partition_irreducibility_operational_quotient.md) |",
    "| **P37** | response geometry, directed influence, and partition irreducibility admit one complete approximate P11 operational-scale budget | proved complete scale theorem | [P37](docs/proposition_37_complete_approximate_p11_operational_scale.md) |",
    "| **P38** | an independently defined target factors through a tomographically complete quantum state iff it is constant on quantum-state fibers; an exact collision proves non-factorization through that declared descriptor | proved quantum sufficiency theorem | [P38](docs/proposition_38_quantum_operational_sufficiency.md) |",
])
text = replace_once(text, table_marker, table_rows, "README theorem table P32-P38")

extension = r'''## 13.10 P32-P37 - complete operational scale closure

![P30-P37 operational scale theorem map](figures/p30_p37_operational_scale_map.svg)

P32-P37 close the operational-scale assumptions left open by P30-P31. They do not add an experiential variable. They determine when the declared P11 physical candidate remains mathematically meaningful while time labels, intervention labels, nodes, and response states are coarse-grained together.

**P32** introduces a surjective delay quotient \(a:\mathcal T_f\twoheadrightarrow\mathcal T_c\). Exact temporal descent requires

\[
\boxed{
a(\tau)=a(\sigma)\Longrightarrow P^{u,\tau}=P^{u,\sigma}\quad\forall u.}
\]

The temporal ambiguity is the largest total-variation diameter inside one delay fiber.

**P33** combines the intervention quotient \(b\) and delay quotient \(a\). For the product experiment grid,

\[
\boxed{
\eta_{a\times b}
=\sup_{b(u)=b(v),\ a(\tau)=a(\sigma)}
\|P^{u,\tau}-P^{v,\sigma}\|_{\mathrm{TV}}
\le \eta_b+\eta_a.
}
\]

Thus the two independently audited operational ambiguities compose additively in total variation.

**P34** declares the complete scale transformation

\[
\boxed{\Sigma=(q_V,C_V,b,a,R)}
\]

and proves exact full-signature transport only when node, state, intervention-source, temporal, and partition semantics all descend consistently. For response geometry, nonzero joint quotient ambiguity gives

\[
\boxed{D_G^{\mathrm{full}}\le2\rho_G^*+2\eta_{a\times b}.}
\]

**P35** proves the corresponding directed-influence stability, conditional on descended source semantics:

\[
\boxed{D_A^{\mathrm{full}}\le2\rho_A^*+2\eta_{a\times b}.}
\]

**P36** handles the fact that partition irreducibility compares a law with a product of its own moving marginals. For an \(m\)-block partition,

\[
\boxed{
|\kappa_\pi(P)-\kappa_\pi(Q)|\le(m+1)\|P-Q\|_{\mathrm{TV}}.
}
\]

Therefore operational quotient ambiguity contributes at most \((m_{\max}+1)\eta_{a\times b}\) to the declared partition branch.

**P37** assembles all three components. With

\[
\varepsilon_G=2\rho_G^*+2\eta_{a\times b},
\qquad
\varepsilon_A=2\rho_A^*+2\eta_{a\times b},
\]

and

\[
\varepsilon_K=\rho_P^*+\rho_\Pi^*+(m_{\max}+1)\eta_{a\times b},
\]

the complete declared P11 distortion obeys

\[
\boxed{
\|\mathbf D_{P11}^{\mathrm{full}}(\Sigma)\|_\infty
\le
\max\{\varepsilon_G,\varepsilon_A,\varepsilon_K\}.
}
\]

This closes the approximate operational-scale branch for the candidate physical signature. The result remains conditional on explicit semantic compatibility and does not establish physical completeness or consciousness.

[Read P32](docs/proposition_32_delay_quotient_compatibility.md), [P33](docs/proposition_33_joint_operational_quotient.md), [P34](docs/proposition_34_joint_p11_operational_scale.md), [P35](docs/proposition_35_approximate_directed_influence_operational_quotient.md), [P36](docs/proposition_36_partition_irreducibility_operational_quotient.md), and [P37](docs/proposition_37_complete_approximate_p11_operational_scale.md).

## 13.11 P38 - quantum operational sufficiency and the exact non-factorization witness

![P38 quantum operational sufficiency](docs/figures/p38_quantum_operational_sufficiency.svg)

P38 returns to the deeper physical-completeness question. Let \(x\) label a preparation and let

\[
\rho_x\in\mathcal D(\mathcal H)
\]

be its finite-dimensional density operator. Assume the declared measurement class is tomographically complete, so equality of all declared Born statistics is equivalent to equality of density operators.

For an independently defined deterministic target \(y(x)\), quantum operational sufficiency is exactly the factorization

\[
y(x)=g(\rho_x).
\]

P38 proves

\[
\boxed{
\rho_x=\rho_{x'}
\Longrightarrow
y(x)=y(x')
}
\]

is necessary and sufficient for that factorization. Therefore the exact collision

\[
\boxed{
\rho_x=\rho_{x'}
\quad\text{but}\quad
y(x)\neq y(x')
}
\]

is a sufficient non-factorization witness for the declared quantum-state descriptor.

For a stochastic target, the corresponding condition is

\[
\boxed{I(Y;X\mid\rho_X)=0.}
\]

A positive residual means preparation identity still carries target-relevant information not represented by the declared density-operator descriptor. It does **not** by itself show that quantum mechanics is incomplete. Incomplete system boundaries, omitted environment variables, an inadequate preparation model, tomography error, hidden classical variables, and target-measurement error must be constrained first.

The strong open target is

\[
\boxed{
\inf_{Q\in\mathfrak Q_{\mathrm{admissible}}}
I(Y;X\mid Q)>0,
}
\]

for a physically justified class of increasingly complete quantum descriptors. P38 states this target but does not prove it.

The next theorem burden is finite-data quantum non-factorization certification: tomography uncertainty and target-distribution uncertainty must be propagated into a residual or collision certificate before any claimed quantum insufficiency can be considered experimentally meaningful.

[Read Proposition 38](docs/proposition_38_quantum_operational_sufficiency.md). The [P38 theorem map](docs/figures/p38_quantum_operational_sufficiency.svg), [implementation](src/consciousness_bridge/quantum_operational_sufficiency.py), and [tests](tests/test_quantum_operational_sufficiency.py) expose the proof-to-code path.

'''
text = replace_once(text, "---\n\n# 14. Observer-to-bridge handoff", extension + "---\n\n# 14. Observer-to-bridge handoff", "README detailed P32-P38 section")
path.write_text(text, encoding="utf-8")

# Theorem roadmap: retain the legacy P1-P31 visual and add the newer scale/quantum maps.
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "![P1-P31 theorem roadmap](figures/theorem_roadmap.svg)", "![P1-P31 core theorem roadmap](figures/theorem_roadmap.svg)\n\n![P30-P37 operational scale extension](../figures/p30_p37_operational_scale_map.svg)\n\n![P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)", "roadmap visual extension")
index_marker = "| [P31](proposition_31_intervention_quotient_compatibility.md) | quotient factorization of intervention-conditioned response laws | exact criterion for changing the intervention set plus a representative-ambiguity budget | proved operational quotient theorem |"
index_rows = index_marker + "\n" + "\n".join([
    "| [P32](proposition_32_delay_quotient_compatibility.md) | delay-fiber factorization | exact temporal quotient criterion and ambiguity budget | proved operational quotient theorem |",
    "| [P33](proposition_33_joint_operational_quotient.md) | product quotient and triangle inequality | joint intervention-delay descent with additive ambiguity | proved joint quotient theorem |",
    "| [P34](proposition_34_joint_p11_operational_scale.md) | assembly under one complete scale declaration | exact full P11 semantics plus approximate geometry control | proved assembly theorem |",
    "| [P35](proposition_35_approximate_directed_influence_operational_quotient.md) | metric perturbation of matched response pairs | approximate directed-influence and edge stability | proved perturbation theorem |",
    "| [P36](proposition_36_partition_irreducibility_operational_quotient.md) | marginal contraction plus product-measure telescoping | partition-reference and irreducibility stability | proved perturbation theorem |",
    "| [P37](proposition_37_complete_approximate_p11_operational_scale.md) | max-norm assembly of G, A, and K bounds | complete approximate P11 scale certificate | proved complete scale theorem |",
    "| [P38](proposition_38_quantum_operational_sufficiency.md) | factorization through tomographically complete density-operator fibers | exact quantum descriptor sufficiency and non-factorization witness | proved quantum sufficiency theorem |",
])
text = replace_once(text, index_marker, index_rows, "roadmap index P32-P38")
insert = r'''# 7.5 Operational-scale closure and quantum specialization: P32-P38

P32-P37 close the complete operational-scale branch of the P11 physical candidate. The key quantitative chain is

\[
\boxed{\eta_{a\times b}\le\eta_a+\eta_b}
\]

followed by

\[
\boxed{D_G^{\mathrm{full}}\le2\rho_G^*+2\eta_{a\times b}},
\]

\[
\boxed{D_A^{\mathrm{full}}\le2\rho_A^*+2\eta_{a\times b}},
\]

and

\[
\boxed{D_K^{\mathrm{full}}\le\rho_P^*+\rho_\Pi^*+(m_{\max}+1)\eta_{a\times b}}.
\]

P37 combines these into one max-norm scale certificate under one shared semantic declaration.

P38 then changes branches. For a tomographically complete quantum operational state \(\rho_x\), a deterministic independent target factors through the declared quantum descriptor iff

\[
\boxed{\rho_x=\rho_{x'}\Longrightarrow y(x)=y(x').}
\]

The exact collision \(\rho_x=\rho_{x'}\) with \(y(x)\ne y(x')\) is therefore a non-factorization witness for that declared descriptor. The stochastic analogue is \(I(Y;X\mid\rho_X)=0\). Neither result is an experiential or ontological theorem.

Direct proofs: [P32](proposition_32_delay_quotient_compatibility.md), [P33](proposition_33_joint_operational_quotient.md), [P34](proposition_34_joint_p11_operational_scale.md), [P35](proposition_35_approximate_directed_influence_operational_quotient.md), [P36](proposition_36_partition_irreducibility_operational_quotient.md), [P37](proposition_37_complete_approximate_p11_operational_scale.md), [P38](proposition_38_quantum_operational_sufficiency.md).

---

'''
text = replace_once(text, "# 8. Fundamental physical sufficiency: P19", insert + "# 8. Fundamental physical sufficiency: P19", "roadmap P32-P38 section")
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_if_present(text, "from P1 through P31", "from P1 through P38")
nav_index_marker = "| P31 | [Intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent and quantitative representative ambiguity |"
nav_index_rows = nav_index_marker + "\n" + "\n".join([
    "| P32 | [Delay-quotient compatibility](proposition_32_delay_quotient_compatibility.md) | exact temporal descent and ambiguity control |",
    "| P33 | [Joint operational quotient](proposition_33_joint_operational_quotient.md) | product-grid descent and additive ambiguity |",
    "| P34 | [Joint P11 operational scale](proposition_34_joint_p11_operational_scale.md) | complete node/state/intervention/time declaration |",
    "| P35 | [Approximate directed-influence quotient stability](proposition_35_approximate_directed_influence_operational_quotient.md) | influence perturbation and edge-margin control |",
    "| P36 | [Partition irreducibility quotient stability](proposition_36_partition_irreducibility_operational_quotient.md) | product-reference perturbation bound |",
    "| P37 | [Complete approximate P11 operational scale](proposition_37_complete_approximate_p11_operational_scale.md) | full G/A/K distortion certificate |",
    "| P38 | [Quantum operational sufficiency](proposition_38_quantum_operational_sufficiency.md) | quantum factorization and non-factorization criterion |",
])
text = replace_once(text, nav_index_marker, nav_index_rows, "research navigation P32-P38")
path.write_text(text, encoding="utf-8")

# Version metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.31.0"', 'version = "0.38.0"', "pyproject version")
text = replace_once(text, "intervention-quotient compatibility, recoverability", "intervention-quotient compatibility, complete operational-scale certification, quantum operational sufficiency, recoverability", "pyproject description")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.31.0", "version: 0.38.0", "citation version")
text = replace_once(text, "full P11 scale compatibility, intervention-quotient compatibility, robust experiment design", "full P11 scale compatibility, intervention and temporal quotient compatibility, complete approximate operational-scale certification, quantum operational sufficiency, robust experiment design", "citation abstract")
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.38.0 - 2026-09-09

### Integrated theorem sequence
- P32 exact delay-quotient compatibility.
- P33 joint intervention-delay operational quotient and additive ambiguity theorem.
- P34 joint node/state/intervention/time P11 scale assembly.
- P35 approximate directed-influence quotient stability.
- P36 partition-product and irreducibility quotient stability.
- P37 complete approximate P11 operational-scale distortion theorem.
- P38 quantum operational sufficiency and exact non-factorization criterion.

### Publication synchronization
- Main README updated through P38 with equations, scientific boundaries, proof links, code links, and visual maps.
- Theorem roadmap and research navigation synchronized through P38.
- P38 publication map added.
- Package and citation metadata synchronized to 0.38.0.
- Main-page visibility guards extended through P38.

### Scientific boundary
- P32-P37 certify a declared candidate physical signature across operational scale; they do not identify consciousness.
- P38 tests factorization through a declared tomographically complete quantum descriptor; failure of that declared factorization is not by itself evidence that quantum mechanics is incomplete or that consciousness is nonphysical.

'''
text = replace_once(text, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog 0.38.0")
path.write_text(text, encoding="utf-8")

# Main-page visibility test
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p31_intervention_quotient_compatibility.svg",', '    "p31_intervention_quotient_compatibility.svg",\n    "p38_quantum_operational_sufficiency.svg",\n    "p30_p37_operational_scale_map.svg",', "main page P38 figures")
text = replace_once(text, "for index in range(1, 32):", "for index in range(1, 39):", "main page proposition range")
path.write_text(text, encoding="utf-8")
