# P74 equation and provenance record

This page classifies the equations used in Proposition 74 so that standard probability tools are not confused with repository-specific bridge methodology.

P74 is a finite-sample extension of the P73 target-channel identifiability result. It does not claim invention of Hoeffding concentration, the union bound, elementary moment perturbation, or interval arithmetic.

---

## 1. Equation classification

| Equation or construction | Role in P74 | Classification | Provenance |
| --- | --- | --- | --- |
| \(\Pr(|\widehat p-p|>\varepsilon)\le2e^{-2n\varepsilon^2}\) | one-cell concentration | standard mathematics | Hoeffding inequality |
| \(\Pr(\max_x|\widehat P(x)-P(x)|>\varepsilon)\le16e^{-2n\varepsilon^2}\) | simultaneous eight-cell event | standard union-bound application assembled for the P74 alphabet | Hoeffding plus union bound |
| \(\varepsilon_n=\sqrt{\log(16/\alpha)/(2n)}\) | simultaneous cell radius | direct inversion of the preceding bound | P74 application of standard concentration |
| \(\delta_n=\min\{2,8\varepsilon_n\}\) | joint-law \(L^1\) radius | elementary finite-alphabet consequence | P74 application |
| \(|\widehat C_{ij}-C_{ij}|\le3\delta_n\) | covariance perturbation | repository derivation from bounded raw moments | P74 |
| \(|\widehat M_{123}-M_{123}|\le13\delta_n\) | third-centered-moment perturbation | repository derivation from the centered-moment expansion | P74 |
| \(L_{ij}=\max\{|\widehat C_{ij}|-3\delta_n,0\}\) | finite-data nondegeneracy margin | repository confidence construction | P74 |
| \(q_L=L_M^2/(U_{12}U_{13}U_{23})\), \(q_U=U_M^2/(L_{12}L_{13}L_{23})\) | interval propagation through P73 inversion | repository assembly using elementary monotonicity | P74 built on P73 |
| \(|m|\in[\sqrt{q_L/(q_L+4)},\sqrt{q_U/(q_U+4)}]\) | label-invariant latent imbalance interval | repository finite-sample extension | P74 built on P73 |
| \(v\in[4/(q_U+4),4/(q_L+4)]\) | latent variance interval | repository finite-sample extension | P74 built on P73 |
| prevalence two-interval orbit | preserves global latent-label ambiguity | repository reporting construction | P74 built on P73 label symmetry |
| \(\gamma_{1,L}=\sqrt{L_{12}L_{13}/(v_UU_{23})}\) and cyclic bounds | P72 stability confidence intervals | repository finite-sample bridge-methodology assembly | P74 built on P72-P73 |
| \(\gamma_{123}\ge\max_j\gamma_{j,L}\) | joint-view certified lower bound | direct consequence of P73 plus simultaneous P74 bounds | P73-P74 |
| \(n>1152\log(16/\alpha)/c_{\min}^2\) | sufficient covariance-gate design condition | repository conservative derivation | P74 |

---

## 2. What is standard

The following ingredients are standard and are not claimed as new:

- Hoeffding concentration for bounded IID observations;
- finite union bounds;
- total probability and finite-alphabet empirical distributions;
- triangle inequalities;
- elementary product perturbation bounds for bounded quantities;
- monotone interval propagation through positive algebraic expressions.

The repository already uses Hoeffding-style finite-data control in earlier propositions, including P9, P20, and P58. P74 applies the same general concentration discipline to a different object: the eight-cell joint law needed for the P73 three-view latent-channel inversion.

---

## 3. What P74 contributes to this research program

The repository-specific contribution is the assembly of those standard tools around the exact target-side dependency chain

\[
\text{P71 target provenance}
\to
\text{P72 measurement stability}
\to
\text{P73 population channel identification}
\to
\text{P74 finite-sample channel certification}.
\]

In particular, P74 contributes:

1. one simultaneous empirical-law event that controls every downstream target-channel quantity used in the theorem;
2. explicit conservative constants for covariance and third-centered-moment perturbation;
3. a finite-data nondegeneracy gate that refuses inversion when covariance confidence intervals touch zero;
4. a confidence set for latent prevalence that preserves the P73 global label-swap symmetry rather than silently selecting a semantic orientation;
5. simultaneous finite-sample confidence intervals for the P72 stability coefficients \(\gamma_1,\gamma_2,\gamma_3\);
6. a finite-sample lower bound for the joint three-view stability;
7. an explicit sufficient sample-size condition for separating a population covariance margin from the P73 singular set.

These are finite-sample statements about a declared latent statistical model. They are not empirical evidence that the model describes consciousness.

---

## 4. Assumption boundary

P74 requires the assumptions of P73 plus IID sampling within the fixed physical stratum. The confidence construction does not establish:

- conditional independence of the three views given the latent target;
- correctness of the binary latent-state model;
- semantic meaning of either latent label;
- independence of target provenance from the physical descriptor beyond the separate P71 requirement;
- the P72 nondifferential measurement condition in a real experiment;
- a physical-to-experiential bridge.

If the finite-data nondegeneracy gate fails, P74 reports that safe inversion is **not certified by the current data**. That is not a population nonidentifiability theorem.

---

## 5. Audit paths

- [P74 proof](proposition_74_finite_sample_target_channel_recovery.md)
- [P73 population identifiability theorem](proposition_73_target_channel_identifiability.md)
- [P72 measurement-channel robustness theorem](proposition_72_target_measurement_channel_robustness.md)
- [`finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py)
- [`test_finite_sample_target_channel_recovery.py`](../tests/test_finite_sample_target_channel_recovery.py)

The physical-to-experiential bridge remains open.
