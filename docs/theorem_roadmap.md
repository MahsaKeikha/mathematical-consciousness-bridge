# Theorem Roadmap

This roadmap records the current proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

![P1-P21 theorem roadmap](figures/theorem_roadmap.svg)

---

# 1. Complete proposition index

| Proposition | Mathematical role | Scientific role | Status |
| --- | --- | --- | --- |
| [P1](proposition_1_representation_invariance.md) | quotient factorization | representation-independent bridge objects | proved |
| [P2](proposition_2_bridge_identifiability.md) | total-variation discriminability | exact theory non-identifiability criterion | proved |
| [P3](proposition_3_bridge_equivalence_classes.md) | quotient by observable fingerprints | identifies what an experiment class can resolve | proved |
| [P4](proposition_4_discriminating_experiment_design.md) | maximin and set-cover design | adversarial theory-discriminating experiments | proved |
| [P5](proposition_5_feature_sufficiency.md) | bridge factorization through physical features | exact sufficiency / counterexample criterion | proved |
| [P6](proposition_6_canonical_bridge_signature.md) | canonical bridge quotient | defines the exact completeness target | proved |
| [P7](proposition_7_experimental_signature_recovery.md) | observable-fingerprint factorization | exact recoverability / no-go condition | proved |
| [P8](proposition_8_robust_signature_recovery.md) | deterministic perturbation bound | finite-error signature recovery | proved |
| [P9](proposition_9_categorical_sample_complexity.md) | Hoeffding + union bound | explicit finite trial requirement | proved |
| [P10](proposition_10_robust_experiment_design.md) | robust protocol optimization | separates discrimination from nuisance variation | proved |
| [P11](proposition_11_intervention_resolved_causal_structure.md) | structured intervention-response object | first original candidate physical signature | proved construction / candidate |
| [P12](proposition_12_component_insufficiency.md) | projection-collision theorem | one-component and scalar reductions lose information | proved minimality / no-go |
| [P13](proposition_13_pairwise_component_irredundancy.md) | pairwise projection collisions | every major component is irredundant relative to the other two on the audit domain | proved irredundancy |
| [P14](proposition_14_temporal_continuation.md) | quotient metric and path variation | representation-invariant temporal continuation | proved temporal-structure theorem |
| [P15](proposition_15_finite_sample_temporal_certification.md) | perturbation bounds for quotient distances and paths | finite-error certification of temporal change | proved certification theorem |
| [P16](proposition_16_independent_composition_and_coupling.md) | product-response composition and factorization defect | distinguishes independent coexistence from observed cross-system coupling | proved composition theorem |
| [P17](proposition_17_coarse_graining_and_refinement.md) | deterministic pushforward and data processing | quantifies information loss under coarse-graining and refinement ambiguity | proved scale-loss theorem |
| [P18](proposition_18_scale_sufficiency_certification.md) | approximate reconstruction and separation margin | certifies when a coarse scale preserves a declared response family | proved scale-sufficiency theorem |
| [P19](proposition_19_fundamental_physical_sufficiency.md) | quotient factorization, conditional mutual information, and differential rank obstruction | tests whether an independent target is fixed by the declared physical descriptor | proved physical-sufficiency theorem |
| [P20](proposition_20_finite_sample_residual_certification.md) | Hoeffding joint-TV concentration plus finite-alphabet entropy continuity | finite-sample confidence interval for the P19 conditional-information residual | proved finite-sample certification theorem |
| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | nested descriptor factorization and conditional-information chain rule | explicit omitted-physics audit and residual-persistence trajectory | proved descriptor-refinement theorem |

---

# 2. Foundation layer: P1-P4

P1 makes the bridge representation independent:

\[
\boxed{
p\sim_Pp'\Longrightarrow B(p)=B(p').
}
\]

P2 defines experiment-class discriminability

\[
\boxed{
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}
}
\]

and proves exact non-identifiability when \(\Delta_\Pi=0\).

P3 quotients theory space by complete observable fingerprints:

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

P4 turns theory discrimination into protocol design:

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

---

# 3. Sufficiency and completeness: P5-P6

For a proposed physical feature \(F\), P5 proves

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p').
}
\]

P6 defines the canonical bridge signature

\[
C_B(p)=[p]_{\sim_B}
\]

and proves

\[
\boxed{
C_B(p)=C_B(p')
\iff
\bar B(p)=\bar B(p').
}
\]

This gives the exact equivalence-class target a complete physical signature would need to match.

---

# 4. Recoverability and finite data: P7-P10

P7 characterizes exact experimental recoverability:

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

P8 introduces the robust signature gap

\[
\boxed{
\gamma_S=\delta_S-\omega_S
}
\]

and proves exact recovery under uniform error when

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

P9 gives an explicit categorical finite-sample sufficient condition:

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(\frac{2N_PN_\pi K}{\alpha}\right).
}
\]

P10 proves that an added protocol is useful only when its between-signature gain exceeds its within-signature inflation.

---

# 5. Physical candidate and internal falsification: P11-P13

P11 defines the intervention-resolved causal structure

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong},
\qquad
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
}
\]

The three retained structures are:

\[
\mathcal G_p
\quad\text{response geometry},
\qquad
\mathcal A_p
\quad\text{directed influence},
\qquad
\mathcal K_p
\quad\text{partition irreducibility}.
\]

P12 proves that each component alone, and several scalar reductions, are incomplete by explicit projection collisions.

P13 strengthens the minimality result:

\[
\boxed{
(\mathcal G,\mathcal A),
\quad
(\mathcal G,\mathcal K),
\quad
(\mathcal A,\mathcal K)
}
\]

are each incomplete on the declared audit domain.

---

# 6. Temporal structure and certification: P14-P15

P14 defines a weighted metric on component fingerprints and then quotients admissible relabelings:

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

It also defines temporal path variation

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}])
}
\]

and proves endpoint and relabeling-invariance results.

P15 propagates finite fingerprint error through this geometry:

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

The same theorem yields certified intervals for cumulative path variation and the maximum adjacent structural jump.

---

# 7. Composition and scale structure: P16-P18

## P16 - independent composition and coupling

For exact independent product-response composition,

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

P16 proves:

- subsystem response geometry is preserved when the other factor is held fixed;
- cross-system directed influence is zero;
- irreducibility across the \(A|B\) partition is zero;
- response-level coupling is detected by departure from the product-factorization null.

The coupling defect is

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

## P17 - coarse-graining and refinement loss

For deterministic coarse map

\[
C:\Omega_f\to\Omega_c,
\]

P17 proves total-variation contraction:

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

If \(C\) is bijective on observed support, equality holds.

If \(C\) is many-to-one, there exist distinct fine laws with identical coarse pushforwards. Thus coarse structure does not generally determine a unique refinement.

This establishes the baseline distinction

\[
\boxed{
\text{descriptive coarse-graining}
\neq
\text{physical fusion}.
}
\]

## P18 - scale sufficiency by approximate reconstruction

P18 asks when the coarse description is nevertheless sufficient for a declared finite family \(\mathcal F\).

Let \(R\) be a fiber-consistent stochastic decoder and define

\[
\boxed{
\rho_{\mathcal F}
=
\sup_{P\in\mathcal F}
\|P-R_{\#}C_{\#}P\|_{\mathrm{TV}}.
}
\]

Then for every \(P,Q\in\mathcal F\),

\[
\boxed{
0
\le
\|P-Q\|_{\mathrm{TV}}
-
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
2\rho_{\mathcal F}.
}
\]

For minimum pairwise separations \(\delta_f\) and \(\delta_c\),

\[
\boxed{
\delta_c
\ge
\delta_f-2\rho_{\mathcal F}.
}
\]

Therefore

\[
\boxed{
\delta_f>2\rho_{\mathcal F}
\Longrightarrow
\delta_c>0,
}
\]

so all response laws in the declared family remain identifiable at the coarse scale.

If \(\rho_{\mathcal F}=0\), pairwise response geometry is preserved exactly even when \(C\) is globally many-to-one. The relevant requirement is family sufficiency, not microscopic invertibility everywhere.

---

# 8. Fundamental physical sufficiency: P19

P19 asks whether an independently defined target descriptor \(E\) is already fixed by the declared physical descriptor \(T\).

The deterministic criterion is

\[
\boxed{
E=B_T\circ T
\iff
T(\Omega)=T(\Omega')\Rightarrow E(\Omega)=E(\Omega').
}
\]

For finite stochastic variables, physical sufficiency is equivalent to

\[
\boxed{
I(E;\Omega\mid T)=0.
}
\]

For differentiable local coordinates, any smooth factorization requires

\[
\boxed{
\operatorname{rank}D(T,E)=\operatorname{rank}DT.
}
\]

A positive rank residual is therefore a sufficient local no-factorization certificate. Neither a positive information residual nor a positive rank residual establishes a nonphysical ontology. Both first challenge the completeness of the declared physical descriptor.

Direct proof: [Proposition 19](proposition_19_fundamental_physical_sufficiency.md). Provenance: [Equation and Citation Map](equation_and_citation_map.md). Empirical burden: [Falsification Program](falsification_program.md).

---

# 9. Finite-sample residual certification: P20

P20 converts the P19 population condition into a finite-data statement. For IID categorical samples on a declared joint alphabet of size

\[
M=d_\Omega d_T d_E,
\]

it defines the conservative total-variation radius

\[
\boxed{
\tau_n(\alpha)
=
\min\left\{1,
\frac M2\sqrt{\frac1{2n}\log\frac{2M}{\alpha}}
\right\}.
}
\]

Finite-alphabet entropy continuity gives a deterministic function \(\Delta_{\mathrm{CMI}}\) such that, with probability at least \(1-\alpha\),

\[
\boxed{
|I_P(E;\Omega\mid T)-\widehat I_n|
\le
\Delta_{\mathrm{CMI}}(\tau_n(\alpha)).
}
\]

Thus the lower bound

\[
L_n=\max\{0,\widehat I_n-\Delta_{\mathrm{CMI}}(\tau_n)\}
\]

satisfies

\[
\boxed{L_n>0\Longrightarrow I_P(E;\Omega\mid T)>0}
\]

with the declared confidence. This certifies failure of screening-off by the declared \(T\), not a nonphysical ontology.

Direct proof: [Proposition 20](proposition_20_finite_sample_residual_certification.md). Implementation: [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py). Tests: [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py).

---

# 10. Descriptor refinement and omitted-physics control: P21

Let \(T_f=f(\Omega)\) refine \(T_c\) through

\[
\boxed{T_c=c(T_f).}
\]

For deterministic target collisions, P21 proves

\[
\boxed{
\mathcal C(T_f,E)
\subseteq
\mathcal C(T_c,E).
}
\]

For the P19 stochastic residual

\[
R(T)=I(E;\Omega\mid T),
\]

the conditional-information chain rule gives

\[
\boxed{
R(T_c)
=
I(E;T_f\mid T_c)
+
R(T_f).
}
\]

Therefore

\[
\boxed{R(T_f)\le R(T_c).}
\]

For a nested chain \(T_0\preceq\cdots\preceq T_m\),

\[
\boxed{
R_0-R_m
=
\sum_{k=1}^{m}I(E;T_k\mid T_{k-1}),
}
\]

so every residual decrease is assigned exactly to target-relevant information added by one physical refinement step. A positive terminal residual remains descriptor relative; it does not establish physical completeness or a nonphysical ontology.

Direct proof: [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md). Implementation: [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py). Tests: [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py).

---

# 11. Dependency chain

\[
\boxed{
\begin{aligned}
&\text{P1-P4: invariance + identifiability}\\
&\Downarrow\\
&\text{P5-P10: sufficiency + recovery + finite data}\\
&\Downarrow\\
&\text{P11-P13: physical candidate + minimality}\\
&\Downarrow\\
&\text{P14-P15: temporal continuation + certification}\\
&\Downarrow\\
&\text{P16: composition + coupling}\\
&\Downarrow\\
&\text{P17-P18: scale loss + scale sufficiency}\\
&\Downarrow\\
&\text{P19: population physical sufficiency}\\
&\Downarrow\\
&\text{P20: finite-sample residual certification}\\
&\Downarrow\\
&\text{P21: physical-descriptor refinement + residual persistence}.
\end{aligned}
}
\]

---

# 12. Current frontier

The next structural problems are:

1. extend scale certification from response geometry \(\mathcal G\) to directed influence \(\mathcal A\) under block-compatible coarse maps;
2. characterize partition-lattice compatibility required to control \(\mathcal K\) across scale;
3. derive simultaneous finite-sample confidence accounting across P21 refinement chains, including adaptive refinement and principled stopping rules for physical-completeness audits;
4. model genuine physical split/merge dynamics where state variables and intervention channels change;
5. formalize the moving world-tube / causal-structure interface;
6. normalize temporal geometry under irregular observation time;
7. run cross-theory adversarial experiments on a shared perturbational protocol family;
8. search biological and non-biological counterexamples;
9. formalize experiential space independently of the physical candidate;
10. attempt a bridge theorem only after the physical, statistical, scale, and falsification layers have been jointly addressed.
