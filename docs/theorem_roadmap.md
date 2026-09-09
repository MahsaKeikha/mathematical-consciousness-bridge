# Theorem Roadmap

This roadmap records the current proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

![P1-P17 theorem roadmap](figures/theorem_roadmap.svg)

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
| [P17](proposition_17_coarse_graining_and_refinement.md) | deterministic pushforward and data processing | quantifies information loss under coarse-graining and refinement ambiguity | proved scale-change theorem |

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

# 7. Composition and scale change: P16-P17

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

## P17 - coarse-graining and refinement

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

---

# 8. Dependency chain

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
&\text{P16-P17: composition + scale change}.
\end{aligned}
}
\]

---

# 9. Current frontier

The next structural problems are:

1. estimator-specific finite-sample certification for composition and coarse-graining quantities;
2. genuine physical split/merge dynamics where state variables and intervention channels change;
3. moving world-tube / causal-structure interface;
4. irregular-time normalization of temporal geometry;
5. cross-theory adversarial experiments on a shared perturbational protocol family;
6. biological and non-biological counterexample search;
7. experiential-space formalization independent of the physical candidate;
8. a bridge theorem only after the preceding physical, statistical, and falsification layers have been jointly addressed.
