# Theorem Roadmap

This roadmap records the current proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

![P1-P27 theorem roadmap](figures/theorem_roadmap.svg)

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
| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared base-TV confidence event plus deterministic pushforward contraction | simultaneous finite-data confidence family for P21 residuals and gains | proved simultaneous-certification theorem |
| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | universal pushforward control plus post-selection regret analysis | adaptive fixed-sample physical-refinement selection with valid coverage | proved post-selection theorem |
| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | summable alpha spending plus countable union control | repeated-look adaptive refinement and finite stopping-time validity | proved anytime-valid theorem |
| [P25](proposition_25_directed_influence_scale_certification.md) | P11 influence plus P18 reconstruction distortion | directed-influence preservation and edge-margin certification across target observation scale | proved physical scale theorem |
| [P26](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition productization plus P17 contraction and P18 reconstruction | partition-irreducibility preservation and margin certification under block-compatible observation | proved physical scale theorem |
| [P27](proposition_27_partition_lattice_node_aggregation.md) | surjective node quotient plus partition saturation, lattice transport, P17 contraction, and P18 reconstruction | exact criterion for surviving partition semantics under node aggregation and quantitative irreducibility control | proved physical scale theorem |

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

## P25 - directed-influence scale certification from P11 + P18

P25 is a branch extension of the physical scale program, not a consequence of P24. It combines the P11 directed-influence definition with the P18 reconstruction theorem.

For fixed source \(i\), target \(j\), delay \(\tau\), and matched intervention family \(\mathcal E_i\),

\[
A_{i\to j}^{f}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\|P_j^{u,\tau}-P_j^{v,\tau}\|_{\mathrm{TV}}.
\]

A deterministic target map \(C_j\) gives

\[
\boxed{A_{i\to j}^{c}(\tau)\le A_{i\to j}^{f}(\tau).}
\]

If a P18 decoder reconstructs all relevant target response laws with uniform defect \(\rho_{i\to j}(\tau)\), then

\[
\boxed{
0\le
A_{i\to j}^{f}(\tau)-A_{i\to j}^{c}(\tau)
\le2\rho_{i\to j}(\tau).
}
\]

Hence for threshold \(\theta\),

\[
\boxed{
A_{i\to j}^{f}(\tau)>\theta+2\rho_{i\to j}(\tau)
\Longrightarrow
A_{i\to j}^{c}(\tau)>\theta.
}
\]

The theorem controls observation loss for \(\mathcal A\). It does not yet solve block aggregation, changing intervention semantics, or scale behavior of \(\mathcal K\).

Direct proof: [Proposition 25](proposition_25_directed_influence_scale_certification.md). Implementation: [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py). Tests: [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py).

## P26 - partition-irreducibility scale certification from P11 + P17 + P18

P26 applies the scale theorem to the P11 partition component. For a declared partition \(\pi\),

\[
\kappa_f^{u,\tau}(\pi)
=
\|P^{u,\tau}-P_{\pi}^{u,\tau}\|_{\mathrm{TV}},
\qquad
P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}P_B^{u,\tau}.
\]

Under a block-compatible deterministic observation map \(C\), productization commutes with pushforward and therefore

\[
\boxed{
\kappa_c^{u,\tau}(\pi)
\le
\kappa_f^{u,\tau}(\pi).
}
\]

If \(D=R_\#C_\#\) is the P18 reconstruction operator, then

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi)
\le
\rho(P^{u,\tau})+\rho(P_{\pi}^{u,\tau}).
}
\]

Exact reconstruction of both laws gives exact preservation. A fine margin larger than the reconstruction budget guarantees survival of a declared coarse threshold.

The theorem does not yet transport the entire partition lattice through physical node aggregation. It certifies one declared partition under observation-compatible scale change.

Direct proof: [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md). Implementation: [partition_irreducibility_scale_certification.py](../src/consciousness_bridge/partition_irreducibility_scale_certification.py). Tests: [test_partition_irreducibility_scale_certification.py](../tests/test_partition_irreducibility_scale_certification.py).

## P27 - partition-lattice transport under node aggregation

Let \(a:V_f\twoheadrightarrow V_c\) be a surjective node map. A fine partition \(\pi_f\) descends exactly when every aggregation fiber lies wholly within one fine block:

\[
\boxed{
\pi_f\text{ descends}
\iff
\forall c\in V_c\;\exists B\in\pi_f:\;a^{-1}(c)\subseteq B.
}
\]

Coarse partitions and aggregation-saturated fine partitions are in bijection through lift and descent, and the correspondence preserves refinement, meet, and join:

\[
\boxed{
\operatorname{Part}(V_c)
\simeq_{\mathrm{lattice}}
\operatorname{Part}_{\mathrm{sat}}(V_f;a).
}
\]

For an aggregation-compatible state map \(C_a\), partition productization commutes with pushforward for every descendable partition. Therefore

\[
\boxed{
\kappa_c(\pi_c)\le\kappa_f(L_a\pi_c)
}
\]

and P18 gives

\[
\boxed{
0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f}).
}
\]

P27 separates structural non-descendability from ordinary information loss. It does not yet transport intervention channels or directed influence through source-node aggregation.

Direct proof: [Proposition 27](proposition_27_partition_lattice_node_aggregation.md). Implementation: [partition_lattice_node_aggregation.py](../src/consciousness_bridge/partition_lattice_node_aggregation.py). Tests: [test_partition_lattice_node_aggregation.py](../tests/test_partition_lattice_node_aggregation.py).

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

# 11. Simultaneous finite-sample refinement certification: P22

Let the finite-alphabet IID base law be \(P_{\Omega E}\), and let every descriptor \(T_k=f_k(\Omega)\) be predeclared and nested.

P22 constructs one base event

\[
\boxed{
\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
}
\]

with probability at least \(1-\alpha\). Because every residual and gain law is a deterministic pushforward of this base law, the same event implies

\[
\boxed{
|R_k-\widehat R_k|
\le
\Delta_k(\tau_n)
\qquad
\forall k
}
\]

and

\[
\boxed{
|G_k-\widehat G_k|
\le
\Gamma_k(\tau_n)
\qquad
\forall k.
}
\]

Using the P21 identity \(G_k=R_{k-1}-R_k\), P22 also intersects each direct gain interval with the difference interval implied by adjacent residual bounds.

Therefore

\[
\boxed{
\Pr\left(
R_k\in\mathcal I_k^R\ \forall k,
\quad
G_k\in\mathcal I_k^G\ \forall k
\right)
\ge1-\alpha.
}
\]

No additional confidence split over the number of descriptor levels is required for this shared-base-event construction. The bound can nevertheless become weak as the declared physical-target and descriptor alphabets grow.

Direct proof: [Proposition 22](proposition_22_simultaneous_refinement_chain_certification.md). Implementation: [refinement_chain_certification.py](../src/consciousness_bridge/refinement_chain_certification.py). Tests: [test_refinement_chain_certification.py](../tests/test_refinement_chain_certification.py).

---

# 12. Adaptive physical-descriptor selection: P23

Let \(T_c=c(\Omega)\) be a common coarse physical descriptor and let every admissible \(T_f=f(\Omega)\) refine \(T_c\).

On the one P22 base confidence event,

\[
\boxed{
\|P-\widehat P\|_{\mathrm{TV}}
\le\tau_n(\alpha),
}
\]

total-variation contraction implies uniform control for every deterministic candidate pushforward. Hence the simultaneous gain and residual bounds remain valid even after selecting

\[
\boxed{
\widehat f\in\operatorname*{arg\,max}_f\widehat G_f.
}
\]

If \(G^*=\max_fG_f\), then P23 proves

\[
\boxed{
0\le G^*-G_{\widehat f}
\le\max_fU_f^G-L_{\widehat f}^G
\le2\Gamma_{\max}.
}
\]

By P21,

\[
\boxed{
R_{\widehat f}-\min_fR_f
=G^*-G_{\widehat f}.
}
\]

Thus fixed-sample adaptive selection retains coverage and receives a quantitative near-optimality certificate relative to the declared admissible descriptor class.

P23 does not cover optional stopping across sample sizes, and statistical post-selection validity does not by itself establish that a selected map is a scientifically meaningful physical descriptor.

Direct proof: [Proposition 23](proposition_23_adaptive_descriptor_selection_certification.md). Implementation: [adaptive_descriptor_selection.py](../src/consciousness_bridge/adaptive_descriptor_selection.py). Tests: [test_adaptive_descriptor_selection.py](../tests/test_adaptive_descriptor_selection.py).

---

# 13. Anytime-valid adaptive refinement: P24

P24 distributes the global error budget over all positive sample sizes using

\[
\boxed{
\alpha_n=\frac{6\alpha}{\pi^2n^2},
\qquad
\sum_{n\ge1}\alpha_n=\alpha.
}
\]

The resulting time-indexed P20 radius is

\[
\boxed{
\tau_n^{\mathrm{any}}(\alpha)
=
\min\left\{
1,
\frac M2
\sqrt{\frac1{2n}\log\left(\frac{M\pi^2n^2}{3\alpha}\right)}
\right\}.
}
\]

A countable union bound gives

\[
\boxed{
\Pr\left(
\forall n\ge1:
\|P-\widehat P_n\|_{\mathrm{TV}}
\le\tau_n^{\mathrm{any}}(\alpha)
\right)
\ge1-\alpha.
}
\]

P23's post-selection bounds are deterministic consequences of the base-law event. They therefore hold at every time simultaneously and at any realized finite stopping time.

Direct proof: [Proposition 24](proposition_24_anytime_adaptive_refinement_certification.md). Implementation: [anytime_refinement_certification.py](../src/consciousness_bridge/anytime_refinement_certification.py). Tests: [test_anytime_refinement_certification.py](../tests/test_anytime_refinement_certification.py).

---

# 14. Dependency chain

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
&\text{P21: physical-descriptor refinement + residual persistence}\\
&\Downarrow\\
&\text{P22: simultaneous finite-sample refinement certification}\\
&\Downarrow\\
&\text{P23: fixed-sample adaptive descriptor selection}\\
&\Downarrow\\
&\text{P24: anytime-valid adaptive selection + finite stopping-time control}.
\end{aligned}
}
\]

---

# 15. Current frontier

The next structural problems are:

1. extend P25-P26 from observation-compatible scale change to genuine block aggregation with source/intervention compatibility;
2. characterize the induced map between fine and coarse partition lattices and determine when the full \(\mathcal A,\mathcal K\) structure survives node aggregation;
3. sharpen P24 beyond conservative alpha spending and extend the refinement program to continuous, dependent, hidden-state, noisy-descriptor, and learned-descriptor settings;
4. model genuine physical split/merge dynamics where state variables and intervention channels change;
5. formalize the moving world-tube / causal-structure interface;
6. normalize temporal geometry under irregular observation time;
7. run cross-theory adversarial experiments on a shared perturbational protocol family;
8. search biological and non-biological counterexamples;
9. formalize experiential space independently of the physical candidate;
10. attempt a bridge theorem only after the physical, statistical, scale, and falsification layers have been jointly addressed.
