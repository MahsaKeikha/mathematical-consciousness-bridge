# Theorem Roadmap

This roadmap records the proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

![P1-P16 theorem roadmap](figures/theorem_roadmap.svg)

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
| [P14](proposition_14_temporal_continuation.md) | quotient metric and path variation | representation-invariant temporal continuation of the physical candidate | proved temporal-structure theorem |
| [P15](proposition_15_finite_sample_temporal_certification.md) | perturbation bounds for quotient distances and paths | finite-error certification of temporal change and continuity | proved certification theorem |
| [P16](proposition_16_independent_composition_and_coupling.md) | product-response composition and factorization defect | distinguishes independent coexistence from observed cross-system response structure | proved composition theorem |

---

# 2. P1 - physical and representational well-definedness

A bridge descends uniquely to the physical quotient exactly when it is constant on physical-equivalence classes:

\[
\boxed{
p\sim_Pp'
\Longrightarrow
B(p)=B(p').
}
\]

This removes dependence on arbitrary coordinates, units, labels, and equivalent encodings.

---

# 3. P2-P4 - theory identifiability and experiment design

For complete theories \(\mathfrak T_1,\mathfrak T_2\),

\[
\boxed{
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
}
\]

P2 proves

\[
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
\]

P3 defines the complete theory fingerprint

\[
\Phi_{\Pi,q}(\mathfrak T)
=
(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}
\]

and proves

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

P4 defines pairwise protocol separation

\[
d_{ij}(\pi)
=
\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}
\]

and proves the complete-discrimination / set-cover equivalence

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

---

# 4. P5-P6 - physical-feature sufficiency and bridge completeness

For physical feature

\[
F:\mathcal Q_P\to\mathcal Z,
\]

P5 proves

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p').
}
\]

P6 defines the canonical bridge equivalence

\[
p\sim_Bp'
\iff
\bar B(p)=\bar B(p')
\]

and signature

\[
C_B(p)=[p]_{\sim_B}.
\]

Then

\[
\boxed{
C_B(p)=C_B(p')
\iff
\bar B(p)=\bar B(p')
}
\]

and

\[
\mathcal Q_B\cong\operatorname{Im}(\bar B).
\]

The complete physical-signature target is therefore

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

on a declared domain.

---

# 5. P7-P10 - recoverability, finite data, and robust protocol design

P7 uses the physical observable fingerprint

\[
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi}
\]

and proves exact recoverability when

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

P8 defines the robust signature gap

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S
}
\]

and gives the finite-error condition

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

P9 turns that error tolerance into the explicit sufficient categorical bound

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right).
}
\]

P10 defines

\[
\Gamma(S)=\delta(S)-\omega(S)
\]

and proves

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

An added modality improves the robust gap exactly when its between-signature gain exceeds its within-signature inflation.

---

# 6. P11 - intervention-resolved causal structure

For physical system \(p\), intervention \(u\), and delay \(\tau\), define

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

The candidate retains

\[
\boxed{
\mathcal G_p
\quad\text{response geometry},
\qquad
\mathcal A_p
\quad\text{directed interventional influence},
\qquad
\mathcal K_p
\quad\text{partition irreducibility}.
}
\]

Define

\[
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p)
\]

and

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

P11 proves compatible-reparameterization invariance, an exact partition-factorization certificate, and a feedforward no-return certificate.

---

# 7. P12 - single-component insufficiency

If a compression \(H\) satisfies

\[
H(x)=H(x')
\quad\text{but}\quad
F(x)\ne F(x'),
\]

then no map \(g\) can satisfy \(F=g\circ H\) on the declared domain.

P12 constructs explicit realizable systems proving that response geometry alone, directed influence alone, partition irreducibility alone, response diameter, one scalar irreducibility value, and a Boolean recurrence indicator are incomplete descriptors of the richer causal-structure candidate.

![P12 constructive collision map](figures/p12_collision_map.svg)

---

# 8. P13 - pairwise component irredundancy

Define

\[
F_C(p)
=
(\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

P13 constructs collision families satisfying

\[
\mathcal G_L=\mathcal G_H,
\quad
\mathcal A_L=\mathcal A_H,
\quad
\mathcal K_L\ne\mathcal K_H,
\]

\[
\mathcal G_0=\mathcal G_+,
\quad
\mathcal K_0=\mathcal K_+,
\quad
\mathcal A_0\ne\mathcal A_+,
\]

and

\[
\mathcal A_D=\mathcal A_S,
\quad
\mathcal K_D=\mathcal K_S,
\quad
\mathcal G_D\ne\mathcal G_S.
\]

Therefore

\[
\boxed{
H_{GA},
\quad
H_{GK},
\quad
H_{AK}
\text{ are all incomplete on }D_{13}.
}
\]

![P13 pairwise component irredundancy](figures/p13_component_irredundancy.svg)

This proves component-level irredundancy on the declared audit domain, not global minimality over every possible physical representation.

---

# 9. P14 - temporal continuation on the quotient space

For finite component fingerprint

\[
c=(g,a,k),
\]

P14 defines

\[
\boxed{
D_w(c,c')
=
\max\left\{
w_G\|g-g'\|_\infty,
w_A\|a-a'\|_\infty,
w_K\|k-k'\|_\infty
\right\}.
}
\]

If the declared finite relabeling group \(\mathcal H\) acts isometrically, then

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc')
}
\]

is a metric on the orbit space.

For a temporal path \([c_0],\ldots,[c_T]\), define

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}]),
}
\]

and

\[
\boxed{
J_{0:T}
=
\max_t
\overline D_w([c_t],[c_{t+1}]).
}
\]

P14 proves the endpoint bound

\[
\boxed{
\overline D_w([c_s],[c_t])\le V_{s:t},
}
\]

and invariance under time-dependent admissible relabelings. It also gives the excursion counterexample showing that equal endpoints do not imply a trivial temporal path.

![P14 temporal continuation](figures/p14_temporal_continuation.svg)

---

# 10. P15 - finite-error temporal certification

Let \(\widehat c_t\) estimate \(c_t\) and suppose simultaneous radii satisfy

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t.
\]

P15 proves the quotient-distance stability inequality

\[
\boxed{
\left|
\overline D_w([\widehat c_s],[\widehat c_t])
-
\overline D_w([c_s],[c_t])
\right|
\le
\varepsilon_s+\varepsilon_t.
}
\]

Therefore the true temporal separation lies in

\[
\boxed{
\left[
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\},
\widehat d_{st}+\varepsilon_s+\varepsilon_t
\right].
}
\]

For cumulative variation,

\[
\boxed{
|\widehat V_{0:T}-V_{0:T}|
\le
\varepsilon_0
+2\sum_{t=1}^{T-1}\varepsilon_t
+\varepsilon_T.
}
\]

For maximum adjacent change,

\[
\boxed{
|\widehat J_{0:T}-J_{0:T}|
\le
\max_t(\varepsilon_t+\varepsilon_{t+1}).
}
\]

The theorem yields a three-way finite-data classification relative to any declared physical threshold \(\eta\): certified above threshold, certified below threshold, or unresolved.

For the special case of \(M\) bounded sample-mean coordinates at each of \(T+1\) times, each estimated from \(n\) IID repetitions, the simultaneous Hoeffding radius is

\[
\boxed{
\delta_n(\alpha)
=
\sqrt{
\frac{1}{2n}
\log\left(\frac{2M(T+1)}{\alpha}\right)
}.
}
\]

This bounded-coordinate corollary is intentionally limited: more complex causal-structure estimators require estimator-specific concentration results.

![P15 finite-sample temporal certification](figures/p15_finite_sample_temporal_certification.svg)

---

# 11. P16 - independent composition and controlled coupling

For two systems \(A\) and \(B\), define the independent product-response composition

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

If

\[
d_A
=
\|P_A^{u_A,\tau}-P_A^{v_A,\tau}\|_{\mathrm{TV}},
\qquad
 d_B
=
\|P_B^{u_B,\tau}-P_B^{v_B,\tau}\|_{\mathrm{TV}},
\]

then P16 proves

\[
\boxed{
\max\{d_A,d_B\}
\le d_{AB}
\le d_A+d_B-d_Ad_B.
}
\]

When one subsystem intervention is unchanged, the corresponding one-factor distance is preserved exactly.

For source and target blocks lying in different independent subsystems,

\[
\boxed{
A_{ij}^{A\otimes B}(\tau)=0.
}
\]

For the partition separating the two complete subsystems,

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0.
}
\]

For an arbitrary observed joint response law, define the response-factorization defect

\[
\boxed{
\chi_{A|B}(\tau)
=
\sup_{u_A,u_B}
\left\|
P_{AB}^{(u_A,u_B),\tau}
-
P_{A,\mathrm{marg}}^{(u_A,u_B),\tau}
\otimes
P_{B,\mathrm{marg}}^{(u_A,u_B),\tau}
\right\|_{\mathrm{TV}}.
}
\]

P16 identifies this exactly with the P11 irreducibility of the \(A|B\) partition:

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

A positive defect certifies departure from response factorization on the declared intervention-observable regime. A zero defect certifies factorization of the measured response laws, not universal absence of every hidden mechanistic interaction.

![P16 independent composition and controlled coupling](figures/p16_composition_coupling.svg)

---

# 12. Current dependency graph

\[
\boxed{
\begin{array}{ccccccccccccccccccccccc}
P1
&\to&P5
&\to&P6
&\to&P7
&\to&P8
&\to&P9
&\to&P10
&\to&P11
&\to&P12
&\to&P13
&\to&P14
&\to&P15
&\to&P16\\
&&&&&&\uparrow\\
P2&\to&P3&\to&P4
&&\text{experiment design}
\end{array}
}
\]

---

# 13. Current frontier

With independent composition and a response-level coupling defect established, the next structural program is:

1. finite-sample confidence intervals for the coupling defect and cross-system influence;
2. splitting, merging, birth, and disappearance of physical blocks;
3. controlled coupling trajectories that connect P14 temporal continuation to P16 composition;
4. observer-to-bridge interface with certified moving world-tubes;
5. estimator-specific concentration for the full Proposition 11 causal-structure coordinates;
6. irregular-time normalization and sampling-cadence sensitivity;
7. source-faithful cross-theory adversarial experiments;
8. biological and artificial counterexample programs;
9. experiential-space formalization;
10. a bridge theorem only after physical, experiential, identifiability, recovery, finite-data, composition, and falsification requirements have been jointly addressed.
