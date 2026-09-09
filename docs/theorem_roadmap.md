# Theorem Roadmap

This roadmap records the current proved theorem chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

The program is layered deliberately: a theorem about a physical feature is not promoted to an experiential conclusion unless the bridge dependency and empirical evidence are explicit.

![P1-P12 theorem roadmap](figures/theorem_roadmap.svg)

---

# 1. Complete proposition index

| Proposition | Mathematical role | Scientific role | Status |
| --- | --- | --- | --- |
| [P1](proposition_1_representation_invariance.md) | quotient factorization | representation-independent physical/bridge objects | proved |
| [P2](proposition_2_bridge_identifiability.md) | total-variation experiment-class discriminability | exact theory non-identifiability criterion | proved |
| [P3](proposition_3_bridge_equivalence_classes.md) | quotient of theories by observable fingerprint | identifies what an experiment class can actually resolve | proved |
| [P4](proposition_4_discriminating_experiment_design.md) | maximin and set-cover protocol design | adversarial theory-discriminating experiment design | proved |
| [P5](proposition_5_feature_sufficiency.md) | bridge factorization through physical features | exact sufficiency/counterexample criterion | proved |
| [P6](proposition_6_canonical_bridge_signature.md) | canonical bridge quotient | defines the exact completeness target | proved |
| [P7](proposition_7_experimental_signature_recovery.md) | decoder/fingerprint factorization | exact experimental recoverability/no-go condition | proved |
| [P8](proposition_8_robust_signature_recovery.md) | deterministic metric perturbation | finite-error signature recovery | proved |
| [P9](proposition_9_categorical_sample_complexity.md) | Hoeffding + union bound | explicit finite trial requirement | proved |
| [P10](proposition_10_robust_experiment_design.md) | robust protocol-family optimization | separates useful discrimination from nuisance variation | proved |
| [P11](proposition_11_intervention_resolved_causal_geometry.md) | structured intervention-response signature | first original candidate physical object | proved construction / candidate |
| [P12](proposition_12_component_insufficiency.md) | projection-collision no-go theorem | proves simple IRCG reductions lose information | proved minimality/no-go |

---

# 2. Layer A - physical and representational well-definedness

## Proposition 1 - representation invariance

A bridge descends uniquely to the physical quotient if and only if it is constant on physical-equivalence classes:

\[
\boxed{
p\sim_Pp'
\Longrightarrow
B(p)=B(p').
}
\]

Equivalently,

\[
\bar B:\mathcal P/{\sim_P}\to\mathcal E/{\sim_E}.
\]

**Role:** coordinates, units, labels, and other physically irrelevant encodings cannot change the bridge assignment.

---

# 3. Layer B - theory identifiability and empirical no-go structure

## Proposition 2 - experiment-class identifiability

\[
\boxed{
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
}
\]

The exact non-identifiability condition is

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
}
\]

## Proposition 3 - observational theory quotient

With

\[
\Phi_{\Pi,q}(\mathfrak T)
=
(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi},
\]

observational equivalence gives

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

## Proposition 4 - discriminating experiment design

For

\[
d_{ij}(\pi)
=
\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}},
\]

define

\[
U(S)
=
\min_{\{i,j\}\in\mathcal U}
\max_{\pi\in S}d_{ij}(\pi).
\]

Then

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

Finite complete theory discrimination is therefore a set-cover problem over distinguishable theory pairs.

---

# 4. Layer C - physical-feature sufficiency and completeness

## Proposition 5 - feature sufficiency

For

\[
F:\mathcal Q_P\to\mathcal Z,
\qquad
\bar B:\mathcal Q_P\to\mathcal Q_E,
\]

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p').
}
\]

A single feature-matched, bridge-different pair refutes sufficiency on the declared domain.

## Proposition 6 - canonical complete bridge signature

Define

\[
p\sim_Bp'
\iff
\bar B(p)=\bar B(p')
\]

and

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
\boxed{
\mathcal Q_B
\cong
\operatorname{Im}(\bar B).
}
\]

This defines the exact equivalence-class geometry a complete physical signature would need to match.

---

# 5. Layer D - recoverability and finite-data certification

## Proposition 7 - experimental signature recovery

For

\[
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi},
\]

a target signature \(F_*\) is recoverable exactly when

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

## Proposition 8 - robust signature recovery

Let

\[
\gamma_S
=
\delta_S-\omega_S,
\]

where \(\delta_S\) is minimum between-signature separation and \(\omega_S\) is maximum within-signature spread. If uniform distribution error is at most \(\varepsilon\), exact recovery is guaranteed when

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

## Proposition 9 - categorical sample complexity

A sufficient per-cell sample count is

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

## Proposition 10 - robust protocol design

Define

\[
\Gamma(S)
=
\delta(S)-\omega(S).
\]

For newly added protocol \(\rho\),

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

Thus an additional modality helps exactly when its between-signature gain exceeds its within-signature inflation.

---

# 6. Layer E - first original physical candidate

## Proposition 11 - Intervention-Resolved Causal Geometry

For physical system \(p\), intervention \(u\in\mathcal U_p\), and delay \(\tau\in\mathcal T\), define

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

IRCG retains three complementary structures:

\[
\boxed{
\mathcal G_p
\quad\text{response geometry},
\qquad
\mathcal A_p
\quad\text{directed influence},
\qquad
\mathcal K_p
\quad\text{partition irreducibility}.
}
\]

The representation-invariant signature is

\[
\boxed{
F_{\mathrm{IRCG}}(p)
=
[\mathfrak C_p]_{\cong},
\qquad
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
}
\]

P11 proves compatible-reparameterization invariance, an exact partition-factorization certificate, and a feedforward no-return certificate.

The strongest possible future candidate-completeness target is

\[
F_{\mathrm{IRCG}}(p)=F_{\mathrm{IRCG}}(p')
\iff
C_B(p)=C_B(p').
\]

This biconditional is the target being tested, not a premise of P11.

---

# 7. Layer F - internal minimality and falsification

## Proposition 12 - component insufficiency

Let \(H\) be a proposed compression of target signature \(F\). If

\[
\boxed{
H(x)=H(x')
\quad\text{but}\quad
F(x)\ne F(x'),
}
\]

then no map \(g\) can satisfy

\[
F=g\circ H
\]

on the declared domain.

P12 constructs explicit realizable intervention-response systems proving

\[
\boxed{
\mathcal G_p,\quad
\mathcal A_p,\quad
\mathcal K_p
\text{ are each individually insufficient to reconstruct full IRCG.}
}
\]

It also constructs collisions for scalar summaries including

\[
\operatorname{Diam}_p(\tau),
\qquad
\kappa_p^*,
\qquad
\mathbf 1\{\text{directed cycle exists}\}.
\]

![P12 constructive collision map](figures/p12_collision_map.svg)

---

# 8. Current dependency graph

\[
\boxed{
\begin{array}{ccccccccccccccc}
P1
&\to&P5
&\to&P6
&\to&P7
&\to&P8
&\to&P9
&\to&P10
&\to&P11
\to P12\\
&&&&&&\uparrow\\
P2&\to&P3&\to&P4
&&\text{experiment design}
\end{array}
}
\]

Interpretation:

- P1 makes physical features and bridges representation well defined.
- P2-P4 determine what competing theories can be distinguished and how to design tests.
- P5-P6 define sufficiency and bridge completeness.
- P7-P10 make complete signatures experimentally recoverable and finite-data certifiable.
- P11 supplies the first original candidate physical object.
- P12 attacks simplifications of that candidate before an experiential interpretation is attached.

---

# 9. Immediate frontier

The next target is **P13 - pairwise-component minimality**.

The program will test whether any of

\[
(\mathcal G_p,\mathcal A_p),
\qquad
(\mathcal G_p,\mathcal K_p),
\qquad
(\mathcal A_p,\mathcal K_p)
\]

can reconstruct full IRCG on increasingly rich declared domains, or whether each admits constructive collisions.

After that, the major structural frontiers are:

1. temporal continuation of physical-signature states;
2. composition, splitting, merging, and controlled coupling;
3. observer-to-bridge interface with certified moving world-tubes;
4. source-faithful cross-theory adversarial experiments;
5. biological and artificial counterexample programs;
6. a bridge theorem only after the physical, experiential, identifiability, recovery, and falsification conditions have been jointly addressed.
