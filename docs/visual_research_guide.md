# Visual Research Guide

This guide is the visual entry point to the **Mathematical Consciousness Bridge** research program. Every figure corresponds to a defined physical object, mathematical equation, theorem, empirical evidence class, or open problem. The figures are intended to function as research diagrams, not decoration.

The visual program is organized in three complementary directions:

1. **theorem progression** - what has been proved and what remains open;
2. **physics and mathematics atlas** - how dynamics, information, causality, thermodynamics, neural measurement, and bridge mathematics connect;
3. **application and evidence maps** - how equations connect to experiments, clinical states, extreme environments, and competing consciousness theories.

---

## 1. Entire research architecture

![Research architecture](figures/research_architecture.svg)

The project separates:

\[
\boxed{
\text{physical realization}
\rightarrow
\text{physical equivalence}
\rightarrow
\text{candidate physical structure}
\rightarrow
\text{bridge principles}
\rightarrow
\text{experiential structure}
\rightarrow
\text{observable predictions}
\rightarrow
\text{finite-data certification}.
}
\]

The central distinction is

\[
\boxed{
\text{physical structure}
\neq
\text{experiential interpretation}
}
\]

until an independently justified bridge connects them.

---

## 2. Physics and Mathematics Atlas

![Physics and mathematics atlas](figures/physics_mathematics_atlas.svg)

This figure gives the interdisciplinary map of the repository.

### Physical dynamics

A physical system may be represented by deterministic or stochastic dynamics such as

\[
\dot x(t)=F(x(t),u(t)),
\]

or

\[
\boxed{
dX_t=f(X_t,u_t)\,dt+G(X_t,u_t)\,dW_t.
}
\]

### Information theory

For probability law \(P\),

\[
H(X)=-\sum_x p(x)\log p(x),
\]

and

\[
\boxed{
I(X;Y)=D_{\mathrm{KL}}(P_{XY}\Vert P_XP_Y).
}
\]

### Information geometry

A smooth family of probability laws \(p(x\mid\theta)\) defines a statistical manifold with Fisher information

\[
\boxed{
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\partial_i\log p(X\mid\theta)
\partial_j\log p(X\mid\theta)
\right].
}
\]

### Causal intervention

The repository uses intervention-conditioned response laws

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

### Thermodynamics of information

For logically irreversible erasure, Landauer's bound gives

\[
\boxed{
W_{\mathrm{erase}}
\ge
k_B T\ln 2.
}
\]

This is a physical bound on irreversible information processing, not a consciousness criterion.

### Bridge mathematics

The physical-to-experiential target is represented abstractly as

\[
\boxed{
\bar B:\mathcal Q_P\rightarrow\mathcal Q_E.
}
\]

The mathematical challenge is to establish which physical equivalence classes, if any, correspond to which experiential equivalence classes under explicit and independently testable bridge principles.

For the full equation-by-equation discussion, see [Physics and Mathematics Atlas](physics_mathematics_atlas.md).

---

## 3. Equation-to-evidence map

![Equation to evidence map](figures/equation_evidence_map.svg)

This figure is the repository's scientific provenance map in visual form. It separates five layers:

\[
\boxed{
\text{equation}
\rightarrow
\text{physical meaning}
\rightarrow
\text{measurement}
\rightarrow
\text{empirical evidence}
\rightarrow
\text{bridge interpretation}.
}
\]

These arrows must not be collapsed.

Examples:

| Equation | Physical meaning | Possible measurement interface | Scientific role |
| --- | --- | --- | --- |
| \(dX_t=fdt+GdW_t\) | stochastic physical dynamics | time-resolved sensor/neural trajectories | physical model |
| \(I(X;Y)\) | statistical dependence / information | estimated joint distributions | mathematical observable |
| \(P(Y\mid do(u))\) | interventional response law | controlled stimulation / perturbation | causal observable |
| \(\kappa_p^\tau(\pi)\) | deviation from partition factorization | joint post-perturbation responses | repository physical candidate |
| \(\bar B:\mathcal Q_P\to\mathcal Q_E\) | physical-to-experiential relation | requires independent bridge evidence | open bridge problem |

This map is intended to prevent a common category error: a mathematically valid statistic is not automatically an experiential variable.

---

## 4. Theorem dependency map

![Theorem roadmap](figures/theorem_roadmap.svg)

The current theorem chain is organized as follows:

- **P1-P4:** physical well-definedness, theory identifiability, observational equivalence, and discriminating experiment design;
- **P5-P10:** physical-feature sufficiency, bridge completeness, experimental recoverability, finite-data recovery, sample complexity, and robust experiment design;
- **P11-P13:** construction and minimality audit of intervention-resolved causal structure;
- **P14-P15:** representation-invariant temporal continuation and finite-error temporal certification;
- **P16:** independent composition and response-level coupling defect;
- **P17:** deterministic coarse-graining, contraction of total-variation geometry, and irreversibility of many-to-one scale reduction.

---

## 5. Anatomy of the causal-structure candidate

![Causal-structure anatomy](figures/causal_structure_anatomy.svg)

The candidate begins from intervention-conditioned response laws

\[
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p)
\]

and retains three complementary structures:

\[
\boxed{
\mathcal G_p
\quad
\mathcal A_p
\quad
\mathcal K_p
}
\]

for response geometry, directed interventional influence, and partition irreducibility.

Its representation-independent form is

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

---

## 6. Why one component is not enough

![Proposition 12 collisions](figures/p12_collision_map.svg)

Proposition 12 constructs realizable collision pairs demonstrating that the full physical candidate cannot generally be reconstructed from:

- response geometry alone;
- directed marginal influence alone;
- partition irreducibility alone;
- response diameter;
- one scalar irreducibility value;
- a cycle/no-cycle recurrence flag.

The governing collision theorem is

\[
\boxed{
H(x)=H(x')
\text{ and }
F(x)\ne F(x')
\Longrightarrow
\nexists g\text{ such that }F=g\circ H.
}
\]

---

## 7. Why two components are still not enough

![Proposition 13 pairwise irredundancy](figures/p13_component_irredundancy.svg)

Proposition 13 gives three independent constructions:

\[
(\mathcal G,\mathcal A)\text{ fixed},\quad\mathcal K\text{ changes},
\]

\[
(\mathcal G,\mathcal K)\text{ fixed},\quad\mathcal A\text{ changes},
\]

\[
(\mathcal A,\mathcal K)\text{ fixed},\quad\mathcal G\text{ changes}.
\]

Thus each component contributes information not reconstructible from the other two on the declared audit domain.

---

## 8. Temporal continuation

![Proposition 14 temporal continuation](figures/p14_temporal_continuation.svg)

For fingerprint \(c=(g,a,k)\), define

\[
D_w(c,c')
=
\max\left\{
w_G\|g-g'\|_\infty,
\;w_A\|a-a'\|_\infty,
\;w_K\|k-k'\|_\infty
\right\}.
\]

After quotienting admissible relabelings,

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

and path variation is

\[
\boxed{
V_{0:T}
=
\sum_t\overline D_w([c_t],[c_{t+1}]).
}
\]

This separates temporal physical organization from mere endpoint similarity.

---

## 9. Finite-sample temporal certification

![Proposition 15 finite-sample temporal certification](figures/p15_finite_sample_temporal_certification.svg)

If

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t,
\]

then

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

The theorem yields a certified interval

\[
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}
\le d_{st}\le
\widehat d_{st}+\varepsilon_s+\varepsilon_t.
\]

The unresolved region is explicit.

---

## 10. Independent composition and controlled coupling

![Proposition 16 independent composition and controlled coupling](figures/p16_composition_coupling.svg)

For independent composition,

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

The cross-system influence vanishes and top-level partition irreducibility is zero:

\[
A_{ij}^{A\otimes B}(\tau)=0
\quad(i\in A,j\in B),
\]

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0.
}
\]

For an observed joint response, the coupling defect

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B})
}
\]

measures departure from response factorization on the declared intervention-observation regime.

---

## 11. Coarse-graining and refinement

![Proposition 17 coarse-graining and refinement](figures/p17_coarse_graining.svg)

Let \(C:X\to Z\) be a deterministic coarse-graining map. For probability laws \(P,Q\), the pushforward satisfies

\[
\boxed{
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

Thus deterministic coarse-graining cannot increase total-variation distinguishability.

If \(C\) is bijective, equality is preserved. If \(C\) is many-to-one, distinct fine states can collapse:

\[
x\ne x',
\qquad
C(x)=C(x'),
\]

so that

\[
\|\delta_x-\delta_{x'}\|_{\mathrm{TV}}=1
\]

but

\[
\boxed{
\|C_\#\delta_x-C_\#\delta_{x'}\|_{\mathrm{TV}}=0.
}
\]

This theorem makes physical scale an explicit part of the bridge problem: a coarse description may erase distinctions present at a finer physical level.

---

## 12. Universal proof criteria

![Universal proof ladder](figures/universal_proof_ladder.svg)

The project uses twelve criteria to separate a theorem internal to a formalism from a scientifically exposed physical-to-experiential result. Full statements are in [Universal Consciousness Proof Target](universal_proof_target.md).

---

## 13. Competing theory families

![Theory comparison map](figures/theory_comparison_map.svg)

Contemporary theory families are translated into the common interface

\[
\boxed{
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
}
\]

This permits theory-specific physical features, bridge architectures, measurement models, and interventions to be compared using the same P2-P6 identifiability and sufficiency machinery.

---

## 14. Spaceflight and extreme-environment relevance

![Spaceflight and extreme-environment relevance map](figures/spaceflight_extreme_environment_map.svg)

Spaceflight is included as an **extreme-environment validation domain**, not as evidence for any specific consciousness equation.

Relevant environmental and operational stressors include

\[
\boxed{
\text{altered gravity}
+
\text{radiation}
+
\text{sleep/circadian disruption}
+
\text{isolation}
+
\text{workload}.
}
\]

These can influence cognition, perceptual performance, neural dynamics, physiology, and behavioral reliability. A consciousness-bridge framework that eventually proposes physical state markers should be tested for robustness under such environmental perturbations.

Relevant authoritative programs include NASA's Human Research Program, Human Factors and Behavioral Performance work, sleep/circadian risk research, and Artemis-oriented behavioral-health data collection.

See [Physics and Mathematics Atlas](physics_mathematics_atlas.md) for the exact role of the spaceflight layer.

---

## 15. Recommended reading order

| Stage | Read | Main question |
| --- | --- | --- |
| 1 | [README](../README.md) | What is the complete research program? |
| 2 | [Physics and Mathematics Atlas](physics_mathematics_atlas.md) | How do physics, information, causality, thermodynamics, neural measurement, and bridge mathematics connect? |
| 3 | [Bridge Problem](bridge_problem.md) | What is missing between physical structure and experience? |
| 4 | [Physical Foundation](physical_foundation.md) | What counts as a physical system and admissible intervention? |
| 5 | [Theorem Roadmap](theorem_roadmap.md) | What has actually been proved? |
| 6 | [P11 - Intervention-Resolved Causal Structure](proposition_11_intervention_resolved_causal_structure.md) | What is the first original candidate physical signature? |
| 7 | [P12 - Component Insufficiency](proposition_12_component_insufficiency.md) | Which one-component reductions fail? |
| 8 | [P13 - Pairwise Component Irredundancy](proposition_13_pairwise_component_irredundancy.md) | Can any two components reconstruct the third? |
| 9 | [P14 - Temporal Continuation](proposition_14_temporal_continuation.md) | How is the physical candidate compared through time after relabeling? |
| 10 | [P15 - Finite-Sample Temporal Certification](proposition_15_finite_sample_temporal_certification.md) | When is apparent temporal change larger than uncertainty? |
| 11 | [P16 - Independent Composition and Coupling](proposition_16_independent_composition_and_coupling.md) | When do systems merely coexist, and when does response structure depart from factorization? |
| 12 | [P17 - Coarse-Graining and Refinement](proposition_17_coarse_graining_refinement.md) | Which physical distinctions survive a change of scale? |
| 13 | [Candidate Theory Families](candidate_theory_families.md) | How are major consciousness theories compared? |
| 14 | [Universal Proof Target](universal_proof_target.md) | What would the final theorem-and-evidence package require? |
| 15 | [Equation and Citation Map](equation_and_citation_map.md) | Which equations are original, standard, assumed, or externally sourced? |
| 16 | [Literature Map](literature_map.md) | What role does each cited source play? |

---

## 16. Reading-status convention

| Label | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the program |
| **Proved** | theorem derived from declared assumptions |
| **Candidate physical signature** | physical structure under test, not an experiential conclusion |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Counterexample / no-go** | a sufficiency, compression, recoverability, or scale-preservation claim fails on an explicit construction |
| **Finite-error certificate** | statement guaranteed under explicitly declared estimation-error radii |
| **Physical composition theorem** | theorem about factorization, coupling, or decomposition of physical response structure |
| **Scale-change theorem** | theorem about which physical distinctions survive coarse-graining or refinement |
| **Open bridge problem** | unresolved connection between physical and experiential structure |

This convention is essential for reading every figure, equation, and theorem in the repository correctly.