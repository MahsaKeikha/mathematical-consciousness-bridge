# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.18.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a physical description of a system to support a scientifically testable claim about consciousness?**

This repository develops a formal mathematical-physics program for the **consciousness bridge problem**: connecting physically meaningful structure to formal experiential structure through explicit assumptions, quotient spaces, intervention-resolved response laws, empirical identifiability, finite-data certification, temporal continuation, composition, coarse-graining, scale sufficiency, and falsification.

It is the continuation of **[Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math)**. That foundation repository asks when a persistent moving subsystem can be inferred from measured dynamics. This repository begins from physically defined systems and asks what further mathematical, causal, statistical, and empirical structure would be required before a physical-to-experiential bridge could be justified.

The intended research sequence is

\[
\boxed{
\text{measured physical dynamics}
\longrightarrow
\text{certified moving subsystem}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{temporal + compositional + scale structure}
\longrightarrow
\text{finite-data certification}
\longrightarrow
\text{empirical discrimination}
\longrightarrow
\text{formal bridge test}.
}
\]

The repository does **not** assume that a physical quantity is consciousness. It builds the mathematical objects, counterexamples, experiments, and certification machinery needed to make such a bridge scientifically auditable.

---

# Abstract

A physical theory can specify states, dynamics, interventions, causal response laws, probability distributions, thermodynamic constraints, and measurement procedures without specifying why any physical organization should correspond to subjective experience. A mathematical theory of consciousness therefore requires an additional object: a bridge from physically meaningful equivalence classes to formally defined experiential equivalence classes.

This repository makes that bridge itself the object of mathematics. Propositions **P1-P10** establish representation invariance, theory identifiability, observational equivalence classes, discriminating experiment design, physical-feature sufficiency, canonical bridge completeness, experimental recoverability, robust finite-error recovery, explicit sample complexity, and robust protocol design. **P11** introduces a structured physical candidate—intervention-resolved causal structure. **P12-P13** construct no-go examples showing that major one-component and two-component compressions lose information. **P14-P15** add representation-invariant temporal continuation and finite-error temporal certification. **P16** establishes the independent-composition null model and a measurable response-level coupling defect. **P17** proves total-variation contraction under deterministic coarse-graining and exact refinement ambiguity under many-to-one maps. **P18** adds a quantitative scale-sufficiency certificate: if a declared family can be approximately reconstructed from the coarse scale with defect \(\rho_{\mathcal F}\), then every pairwise response distance is distorted by at most \(2\rho_{\mathcal F}\), and distinct response laws remain identifiable whenever \(\delta_f>2\rho_{\mathcal F}\).

The research record now includes **18 proposition-level results, 40 equation-driven quantitative figures, a large set of canonical scientific maps, reproducible numerical examples, and a Python 3.10/3.11/3.12 test matrix**. Synthetic examples are labeled synthetic. Closed-form mathematical facts are labeled as such. Empirical claims remain separated from bridge interpretation.

---

# Paper map

| Section | Scientific question |
| --- | --- |
| **1. Research architecture** | What are the distinct physical, mathematical, empirical, and experiential layers? |
| **2. Physics first** | What dynamical and thermodynamic structures are legitimate physical starting points? |
| **3. Probability and information geometry** | How are response laws compared and statistically distinguished? |
| **4. Bridge domains and proof target** | What would a mathematically well-defined bridge actually have to map? |
| **5. P1-P10** | What can be identified, recovered, discriminated, and certified from finite data? |
| **6. P11-P13** | What structured physical candidate survives internal compression tests? |
| **7. P14-P15** | How is physical structure compared through time? |
| **8. P16** | How do independent systems differ from coupled systems? |
| **9. P17-P18** | What is lost under coarse-graining, and when is a coarse scale still sufficient? |
| **10. Observer-to-bridge handoff** | How does the previous world-tube research feed this program? |
| **11. Empirical measurement interface** | Which perturbational and state-dependent observations constrain the physical side? |
| **12. Competing theories and falsification** | How are alternative theories translated into discriminating tests? |
| **13. Numerical validation** | Which mathematical facts and examples are automatically checked? |
| **14. Reproducibility** | Can figures, examples, propositions, and tests be regenerated and audited? |
| **15. Current frontier** | What remains open before any responsible bridge theorem? |

---

# Research record at a glance

| Research record | Current state |
| --- | ---: |
| proposition-level results | **18** |
| structured physical candidate | **1 — intervention-resolved causal structure** |
| universal proof criteria | **12** |
| equation-driven quantitative figures | **40** |
| canonical architecture / theorem / theory maps | **17+** |
| visible scientific figures on this main page | **50+** |
| collected automated tests in the current branch | **117** |
| CI matrix | **Python 3.10, 3.11, 3.12** |
| research-software version | **0.18.0** |

---

# 1. Research architecture

![Mathematical Consciousness Bridge research architecture](docs/figures/research_architecture.svg)

**Research architecture.** Physical realization, representation-independent physical structure, candidate signatures, bridge principles, experiential structure, observable predictions, finite-data certification, and falsification are treated as distinct scientific layers.

The central target is

\[
\boxed{
\text{physical first principles}
+
\text{bridge principles}
+
\text{empirically discriminating evidence}
+
\text{finite-data certification}
\Longrightarrow
\text{formal experiential property}.
}
\]

The implication must follow from explicit premises. The physical-to-experiential premises must also expose themselves to empirical discrimination.

![Multiscale physical hierarchy](docs/figures/multiscale_physical_hierarchy.svg)

**Multiscale physical hierarchy.** The project separates local dynamics, network-scale state, a certified moving subsystem, intervention-resolved causal structure, temporal/compositional/scale analysis, and the still-open bridge layer.

![Equation to evidence map](docs/figures/equation_evidence_map.svg)

**Equation-to-evidence discipline.** A valid equation, physical interpretation, measurement model, empirical observation, and experiential conclusion are different scientific objects.

\[
\boxed{
\text{equation}
\neq
\text{physical interpretation}
\neq
\text{measurement model}
\neq
\text{empirical evidence}
\neq
\text{bridge conclusion}.
}
\]

---

# 2. Physics first

A controlled stochastic system may be represented by

\[
\boxed{
dX_t=f(X_t,u_t)\,dt+G(X_t,u_t)\,dW_t,
}
\]

or, more generally, by a transition kernel

\[
\boxed{
X_{t+\Delta t}\sim K_{\Delta t}(\cdot\mid X_t,u_t).
}
\]

The physical model must declare state variables, observables, interventions, noise, timescale, boundary conditions, and the scale at which the description is intended to be valid.

![State-space dynamics map](docs/figures/state_space_dynamics_map.svg)

**State-space dynamics map.** The physical starting point is dynamical: trajectories, transition laws, perturbations, relaxation, and stochastic forcing precede any proposed bridge interpretation.

## 2.1 Stochastic dynamics: mean reversion

![Q01 Ornstein-Uhlenbeck trajectories](docs/figures/quantitative/q01_ornstein_uhlenbeck_trajectories.svg)

**Q01 — Ornstein-Uhlenbeck trajectories.** For

\[
dX_t=\theta(\mu-X_t)dt+\sigma dW_t,
\]

linear drift pulls trajectories toward equilibrium while diffusion sustains fluctuations. This is a fixed-seed equation-driven stochastic simulation.

![Q02 OU stationary variance](docs/figures/quantitative/q02_ou_stationary_variance.svg)

**Q02 — OU variance.** With zero initial variance,

\[
\boxed{
\operatorname{Var}[X_t]
=\frac{\sigma^2}{2\theta}
\left(1-e^{-2\theta t}\right),
}
\]

so the stationary variance is \(\sigma^2/(2\theta)\). For the atlas parameters \(\theta=1.4\), \(\sigma=0.65\), the tested limit is approximately **0.1508928571**.

## 2.2 Metastability and physical landscapes

![Q03 double-well potential](docs/figures/quantitative/q03_double_well_potential.svg)

**Q03 — Double-well potential.** The model

\[
U(x)=\frac{a}{4}x^4-\frac{b}{2}x^2
\]

contains two minima separated by a barrier, providing a standard physical illustration of metastability and noise-driven switching.

![Q04 double-well stationary density](docs/figures/quantitative/q04_double_well_stationary_density.svg)

**Q04 — Stationary density.** At fixed inverse temperature,

\[
p(x)\propto e^{-\beta U(x)},
\]

so probability mass concentrates near low-potential regions.

## 2.3 Linear dynamics and stability

![Q05 linear state-space flow](docs/figures/quantitative/q05_linear_state_space_flow.svg)

**Q05 — Linear state-space flow.** For

\[
\dot x=Ax,
\]

negative real parts of the eigenvalues produce decay toward the fixed point while off-diagonal terms generate rotation.

![Q06 eigenvalue stability map](docs/figures/quantitative/q06_eigenvalue_stability_map.svg)

**Q06 — Stability map.** Continuous-time asymptotic stability requires

\[
\boxed{
\operatorname{Re}\lambda_i(A)<0
\quad\forall i.
}
\]

The tested matrix used by Q05 has eigenvalues with real part **-0.4**, placing them in the stable half-plane.

## 2.4 Diffusion and propagators

![Q07 diffusion mean-square displacement](docs/figures/quantitative/q07_diffusion_mean_square_displacement.svg)

**Q07 — Diffusive mean-square displacement.** For isotropic Brownian diffusion,

\[
\boxed{
\mathbb E\|X_t-X_0\|^2=2dDt.
}
\]

The mean-square displacement therefore grows linearly with physical time and spatial dimension.

![Q08 heat-kernel propagator](docs/figures/quantitative/q08_heat_kernel_propagator.svg)

**Q08 — Heat kernel.** The one-dimensional diffusion propagator

\[
G(x,t)=\frac{1}{\sqrt{4\pi Dt}}
\exp\left(-\frac{x^2}{4Dt}\right)
\]

broadens through time while conserving total probability.

## 2.5 Thermodynamics of information

![Thermodynamics and information processing](docs/figures/thermodynamics_information_processing.svg)

**Thermodynamics map.** Information processing is physically constrained by work, heat, entropy production, and nonequilibrium trajectories, but those constraints are not themselves consciousness criteria.

![Q09 Landauer bound](docs/figures/quantitative/q09_landauer_bound_temperature.svg)

**Q09 — Landauer bound.** Logical irreversibility implies the standard lower bound

\[
\boxed{
W_{\mathrm{erase}}\ge k_BT\ln 2.
}
\]

At **300 K**, the numerical validation test gives approximately

\[
2.870978885\times10^{-21}\ \mathrm{J}
\]

per erased bit.

## 2.6 Directional information, synchronization, mixing, and control

![Q10 two-state KL asymmetry](docs/figures/quantitative/q10_two_state_kl_asymmetry.svg)

**Q10 — KL divergence.** For probability laws \(P,Q\),

\[
D_{\mathrm{KL}}(P\|Q)=\sum_i P_i\log\frac{P_i}{Q_i}.
\]

The figure shows how divergence grows as two Bernoulli laws approach opposing deterministic limits.

![Q11 Kuramoto order parameter](docs/figures/quantitative/q11_kuramoto_order_parameter.svg)

**Q11 — Synchronization order parameter.** The standard phase-coherence summary

\[
r e^{i\psi}=\frac1N\sum_{j=1}^{N}e^{i\theta_j}
\]

is shown as a **synthetic coupled-oscillator benchmark**, not neural evidence and not a consciousness index.

![Q12 Markov spectral mixing](docs/figures/quantitative/q12_markov_spectral_mixing.svg)

**Q12 — Markov mixing.** For an ergodic finite Markov chain, the subdominant eigenvalue controls asymptotic mixing. The example used by the atlas has

\[
|\lambda_2|=0.74.
\]

![Q13 controllability Gramian](docs/figures/quantitative/q13_controllability_gramian_trace.svg)

**Q13 — Controllability.** The finite-horizon controllability Gramian is

\[
\boxed{
W_c(T)=\int_0^T e^{At}BB^{\mathsf T}e^{A^{\mathsf T}t}\,dt.
}
\]

For the displayed stable controllable system, the Gramian grows toward a finite infinite-horizon limit.

---

# 3. Probability, distinguishability, and information geometry

![Physics and mathematics atlas](docs/figures/physics_mathematics_atlas.svg)

**Physics and mathematics atlas.** Physical law, measurable structure, mathematical invariants, empirical evidence, and bridge interpretation remain distinct.

## 3.1 Correlated Gaussian geometry

![Q14 correlated Gaussian contours](docs/figures/quantitative/q14_correlated_gaussian_contours.svg)

**Q14 — Gaussian covariance geometry.** For

\[
p(x)\propto
\exp\left[-\frac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)\right],
\]

off-diagonal covariance rotates elliptical equal-density contours and encodes statistical dependence.

![Information-geometry response manifold](docs/figures/information_geometry_response_manifold.svg)

**Information-geometric response manifold.** Intervention-conditioned laws can be treated as points in a statistical family. The existence of useful geometric structure does not determine an experiential interpretation; it gives mathematical structure to distinguishability and perturbation.

## 3.2 Gaussian KL divergence

![Q15 Gaussian shift KL](docs/figures/quantitative/q15_gaussian_shift_kl.svg)

**Q15 — Equal-variance Gaussian shift.** If two one-dimensional Gaussians have common variance \(\sigma^2\),

\[
\boxed{
D_{\mathrm{KL}}
=\frac{(\mu_1-\mu_2)^2}{2\sigma^2}.
}
\]

The divergence grows quadratically with normalized mean separation.

## 3.3 Fisher information

![Q16 Bernoulli Fisher information](docs/figures/quantitative/q16_bernoulli_fisher_information.svg)

**Q16 — Bernoulli Fisher information.** Under the direct parameterization,

\[
\boxed{
I(p)=\frac1{p(1-p)}.
}
\]

The local statistical metric is smallest at \(p=1/2\) and diverges toward the boundaries.

## 3.4 Gaussian mutual information

![Q17 Gaussian mutual information](docs/figures/quantitative/q17_gaussian_mutual_information.svg)

**Q17 — Correlated Gaussian variables.** For jointly Gaussian scalar variables,

\[
\boxed{
I(X;Y)=-\frac12\log(1-\rho^2).
}
\]

The information depends on \(|\rho|\) and increases as correlation approaches unit magnitude.

## 3.5 Total variation as operational distinguishability

![Q18 Gaussian total variation](docs/figures/quantitative/q18_gaussian_total_variation.svg)

**Q18 — Gaussian total variation.** The project repeatedly uses

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}
=\frac12\int|p-q|.
}
\]

For equal-variance Gaussians, the numerical integration shows distinguishability rising from zero toward one as the means separate.

---

# 4. Physical and experiential domains

A physical input is modeled abstractly as

\[
\boxed{
p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O),
}
\]

where \(\mathcal X\) is state space, \(\mathcal D\) dynamics, \(\mathfrak I\) admissible interventions, and \(\mathcal O\) the observable map.

Physical descriptions are quotiented by

\[
p\sim_Pp',
\qquad
\boxed{
\mathcal Q_P=\mathcal P/{\sim_P}.
}
\]

Let \(\mathcal E\) be a formal experiential space with experiential equivalence

\[
e\sim_Ee',
\qquad
\boxed{
\mathcal Q_E=\mathcal E/{\sim_E}.
}
\]

The target bridge is

\[
\boxed{
\bar B:\mathcal Q_P\longrightarrow\mathcal Q_E.
}
\]

A complete empirical bridge theory must additionally specify bridge principles, a measurement interface, and an experiment family:

\[
\boxed{
\mathfrak T
=(\mathcal P,\mathcal E,\sim_P,\sim_E,\mathcal B,\mathcal M,\Pi).
}
\]

![Universal proof ladder](docs/figures/universal_proof_ladder.svg)

**Universal proof ladder.** A bridge theorem must satisfy physical, mathematical, empirical, and finite-data requirements rather than jumping directly from a physical statistic to experience.

| Criterion | Requirement | Current support |
| --- | --- | --- |
| U1 | physical well-definedness | physical foundation + P1 |
| U2 | experiential well-definedness | open formalization problem |
| U3 | non-definitional bridge | architectural requirement |
| U4 | representation invariance | P1 |
| U5 | physical-feature sufficiency | P5 |
| U6 | bridge completeness | P6 |
| U7 | empirical identifiability | P2-P3 |
| U8 | cross-theory discrimination | P4 + theory interface |
| U9 | experimental recoverability | P7 |
| U10 | finite-measurement certification | P8, P15 |
| U11 | explicit sample complexity | P9 + finite-data extensions |
| U12 | temporal, compositional, scale, substrate, and falsification consistency | P14-P18 partially address this layer |

A strong conditional theorem would have the form

\[
\boxed{
\begin{aligned}
& p\in\mathcal Q_P,\\
& A_1,\ldots,A_k\text{ bridge principles hold},\\
& F_*(p)\text{ is a complete physical signature},\\
& \widehat F_*(p)\text{ is recovered with declared confidence},\\
& V_1,\ldots,V_r\text{ discriminating validation conditions hold}
\\[1mm]
&\qquad\Longrightarrow
\bar B(p)\in\mathcal C_E.
\end{aligned}
}
\]

The stronger target is

\[
\boxed{
\bar B(p)\in\mathcal C_E
\iff
F_*(p)\in\mathcal R_C.
}
\]

Both directions require independent justification.

---

# 5. Theorem roadmap — P1 through P18

![Theorem roadmap](docs/figures/theorem_roadmap.svg)

**Theorem roadmap.** The program moves from invariance and identifiability to recoverability, a structured physical candidate, temporal continuation, composition, scale loss, and scale sufficiency.

| Proposition | Core result | Status | Proof |
| --- | --- | --- | --- |
| **P1** | representation-invariant bridge descends to physical quotient | proved | [P1](docs/proposition_1_representation_invariance.md) |
| **P2** | exact experiment-class bridge identifiability using total variation | proved | [P2](docs/proposition_2_bridge_identifiability.md) |
| **P3** | observational theory-equivalence classes | proved | [P3](docs/proposition_3_bridge_equivalence_classes.md) |
| **P4** | maximin and set-cover discriminating experiment design | proved | [P4](docs/proposition_4_discriminating_experiment_design.md) |
| **P5** | exact physical-feature sufficiency criterion | proved | [P5](docs/proposition_5_feature_sufficiency.md) |
| **P6** | canonical complete bridge signature | proved | [P6](docs/proposition_6_canonical_bridge_signature.md) |
| **P7** | exact experimental recoverability criterion | proved | [P7](docs/proposition_7_experimental_signature_recovery.md) |
| **P8** | robust finite-error signature recovery | proved | [P8](docs/proposition_8_robust_signature_recovery.md) |
| **P9** | explicit categorical sample-complexity guarantee | proved | [P9](docs/proposition_9_categorical_sample_complexity.md) |
| **P10** | robust protocol-family design | proved | [P10](docs/proposition_10_robust_experiment_design.md) |
| **P11** | intervention-resolved causal structure | proved construction / candidate | [P11](docs/proposition_11_intervention_resolved_causal_structure.md) |
| **P12** | single-component and scalar insufficiency | proved no-go | [P12](docs/proposition_12_component_insufficiency.md) |
| **P13** | pairwise component irredundancy | proved no-go | [P13](docs/proposition_13_pairwise_component_irredundancy.md) |
| **P14** | representation-invariant temporal continuation | proved | [P14](docs/proposition_14_temporal_continuation.md) |
| **P15** | finite-error temporal certification | proved | [P15](docs/proposition_15_finite_sample_temporal_certification.md) |
| **P16** | independent composition and response-level coupling defect | proved | [P16](docs/proposition_16_independent_composition_and_coupling.md) |
| **P17** | coarse-graining contraction and refinement non-recoverability | proved | [P17](docs/proposition_17_coarse_graining_and_refinement.md) |
| **P18** | approximate reconstruction gives a quantitative scale-sufficiency certificate | proved | [P18](docs/proposition_18_scale_sufficiency_certification.md) |

---

# 6. P1-P10 — invariance, identifiability, recovery, and finite data

## 6.1 Representation invariance

There exists a unique quotient bridge

\[
\bar B:\mathcal Q_P\to\mathcal Q_E
\]

with \(B=\bar B\circ\pi_P\) if and only if

\[
\boxed{
p\sim_Pp'\Longrightarrow B(p)=B(p').
}
\]

## 6.2 Theory identifiability

For complete theories \(\mathfrak T_1,\mathfrak T_2\), define

\[
\boxed{
\Delta_\Pi
=\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
}
\]

Then

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
}
\]

With equal priors, optimal one-shot discrimination error is

\[
\boxed{
R_\pi^*=\frac12
\left(1-\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\right).
}
\]

## 6.3 Feature sufficiency and canonical completeness

For proposed feature \(F:\mathcal Q_P\to\mathcal Z\),

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')\Longrightarrow\bar B(p)=\bar B(p').
}
\]

Define bridge equivalence

\[
p\sim_Bp'\iff\bar B(p)=\bar B(p')
\]

and canonical bridge signature

\[
\boxed{
C_B(p)=[p]_{\sim_B}.
}
\]

The strongest complete physical-signature target is

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

## 6.4 Robust finite-data recovery

For protocol family \(S\), define within-signature spread \(\omega_S\), between-signature separation \(\delta_S\), and robust gap

\[
\boxed{
\gamma_S=\delta_S-\omega_S.
}
\]

![Q35 robust signature gap](docs/figures/quantitative/q35_robust_signature_gap.svg)

**Q35 — Robust signature gap.** Increasing nuisance spread reduces the robust gap one-for-one.

P8 gives exact recovery under uniform total-variation estimation error \(\varepsilon\) when

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

## 6.5 Explicit sample complexity

For the categorical benchmark, P9 gives

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(\frac{2N_PN_\pi K}{\alpha}\right).
}
\]

![Q33 sample complexity versus gap](docs/figures/quantitative/q33_sample_complexity_vs_gap.svg)

**Q33 — Sample complexity.** The sufficient sample requirement scales as \(\gamma_S^{-2}\). Doubling the robust gap therefore divides this bound by four; that inverse-square relation is explicitly tested.

![Q36 Hoeffding repeated-event bound](docs/figures/quantitative/q36_hoeffding_repeated_event_bound.svg)

**Q36 — Repeated-event concentration.** The finite-sample bound

\[
\boxed{
\Pr(\text{error})\lesssim e^{-n\eta^2/2}
}
\]

decays exponentially with independent repetitions for fixed effect size \(\eta\).

![Q34 empirical TV Monte Carlo](docs/figures/quantitative/q34_empirical_tv_monte_carlo.svg)

**Q34 — Monte Carlo TV convergence.** Fixed-seed categorical experiments verify that empirical total variation approaches the population value as sample size increases. This is a simulation test of the estimator behavior, not empirical neuroscience.

---

# 7. P11 — intervention-resolved causal structure

![Causal-structure anatomy](docs/figures/causal_structure_anatomy.svg)

**Causal-structure anatomy.** The candidate retains response differentiation, directed causal influence, and partition-specific irreducibility rather than compressing the physics into one scalar.

Let the physical subsystem have blocks \(V=\{1,\ldots,m\}\). For intervention \(u\) and delay \(\tau\),

\[
\boxed{
P_p^{u,\tau}
=\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

![Q19 intervention response laws](docs/figures/quantitative/q19_intervention_response_laws.svg)

**Q19 — Intervention-conditioned response laws.** Synthetic distributions illustrate the primitive observable object of P11: different interventions can produce distinguishable future response laws.

## 7.1 Response geometry

\[
\boxed{
d_p^\tau(u,v)
=\|P_p^{u,\tau}-P_p^{v,\tau}\|_{\mathrm{TV}}.
}
\]

The family is \(\mathcal G_p\).

![Q20 response geometry matrix](docs/figures/quantitative/q20_response_geometry_matrix.svg)

**Q20 — Response geometry.** Because total variation is a metric on probability laws, the displayed response-distance matrix is symmetric and has zero diagonal.

## 7.2 Directed interventional influence

For source-pair family \(\mathcal E_i\),

\[
\boxed{
A_{ij}^{p}(\tau)
=\sup_{(u,v)\in\mathcal E_i}
\|P_{p,j}^{u,\tau}-P_{p,j}^{v,\tau}\|_{\mathrm{TV}}.
}
\]

The full tensor is \(\mathcal A_p\).

![Q21 directed influence matrix](docs/figures/quantitative/q21_directed_influence_matrix.svg)

**Q21 — Directed influence.** A synthetic influence matrix illustrates an important structural fact: intervention effects are generally asymmetric.

## 7.3 Partition irreducibility

For partition \(\pi\), define

\[
P_{p,\pi}^{u,\tau}
=\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
\]

and

\[
\boxed{
\kappa_p^\tau(\pi)
=\sup_u
\|P_p^{u,\tau}-P_{p,\pi}^{u,\tau}\|_{\mathrm{TV}}.
}
\]

The complete partition landscape is \(\mathcal K_p\).

The raw candidate is

\[
\boxed{
\mathfrak C_p
=(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p),
}
\]

and its representation-independent form is

\[
\boxed{
F_{\mathrm{causal}}(p)=[\mathfrak C_p]_{\cong}.
}
\]

---

# 8. P12-P13 — internal minimality and no-go tests

![P12 constructive collision map](docs/figures/p12_collision_map.svg)

**P12 collision map.** Explicit finite response laws show that response geometry, directed influence, partition irreducibility, and several simple scalar reductions are individually incomplete.

The collision theorem is

\[
\boxed{
H(x)=H(x')
\quad\text{and}\quad
F(x)\ne F(x')
\Longrightarrow
\nexists g\text{ with }F=g\circ H.
}
\]

![P13 pairwise component irredundancy](docs/figures/p13_component_irredundancy.svg)

**P13 pairwise irredundancy.** Every two-component projection admits a collision on the declared audit domain:

\[
(\mathcal G,\mathcal A)\text{ fixed},\quad\mathcal K\text{ changes},
\]

\[
(\mathcal G,\mathcal K)\text{ fixed},\quad\mathcal A\text{ changes},
\]

\[
(\mathcal A,\mathcal K)\text{ fixed},\quad\mathcal G\text{ changes}.
\]

These results are deliberately negative: they prevent premature compression into a one-number consciousness score.

---

# 9. P14-P15 — temporal continuation and finite-error certification

![P14 temporal continuation](docs/figures/p14_temporal_continuation.svg)

**P14 temporal continuation.** Causal-structure states are compared after quotienting admissible relabelings.

For fingerprint \(c=(g,a,k)\), define

\[
D_w(c,c')
=\max\left\{
w_G\|g-g'\|_\infty,
\;w_A\|a-a'\|_\infty,
\;w_K\|k-k'\|_\infty
\right\}.
\]

For finite relabeling group \(\mathcal H\),

\[
\boxed{
\overline D_w([c],[c'])
=\min_{h\in\mathcal H}D_w(c,hc').
}
\]

![Q30 temporal fingerprint trajectory](docs/figures/quantitative/q30_temporal_fingerprint_trajectory.svg)

**Q30 — Temporal fingerprint trajectory.** A synthetic time-indexed physical structure traces a path through feature space. Representation alignment is conceptually prior to interpreting structural change.

Temporal path variation is

\[
\boxed{
V_{0:T}
=\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}]).
}
\]

![Q31 cumulative path variation](docs/figures/quantitative/q31_cumulative_path_variation.svg)

**Q31 — Cumulative variation.** Path variation is nondecreasing because it sums nonnegative adjacent structural distances.

![P15 finite-sample temporal certification](docs/figures/p15_finite_sample_temporal_certification.svg)

**P15 finite-error certification.** If

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t,
\]

then

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le\varepsilon_s+\varepsilon_t.
}
\]

![Q32 temporal certification interval width](docs/figures/quantitative/q32_temporal_certification_interval_width.svg)

**Q32 — Certification width.** Under an illustrative \(n^{-1/2}\) estimator-error schedule, the temporal-distance uncertainty interval shrinks at the same rate.

The purpose is to report uncertainty explicitly rather than force uncertain comparisons into binary categories.

---

# 10. P16 — independent composition and coupling

![P16 composition and coupling](docs/figures/p16_composition_coupling.svg)

**P16 composition.** The independent product-response model provides a physical null model for two coexisting systems.

Define

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

For response distances \(d_A,d_B,d_{AB}\), P16 proves

\[
\boxed{
\max\{d_A,d_B\}
\le d_{AB}
\le d_A+d_B-d_Ad_B.
}
\]

For independent composition, cross-system directed influence is zero and the top-level partition factorizes:

\[
\boxed{
A_{ij}^{A\otimes B}(\tau)=0
\quad(i\in A,j\in B),
}
\]

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0.
}
\]

For an observed joint response, define coupling defect

\[
\boxed{
\chi_{A|B}(\tau)
=\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

![Q22 partition irreducibility versus coupling](docs/figures/quantitative/q22_partition_irreducibility_coupling.svg)

**Q22 — Partition irreducibility.** For the displayed balanced binary family, departure from the product partition grows linearly with the synthetic coupling parameter.

![Q23 coupled binary joint law](docs/figures/quantitative/q23_coupled_binary_joint_law.svg)

**Q23 — Marginals can hide coupling.** A dependent joint law can have unchanged one-variable marginals. Marginal inspection alone therefore does not establish independence.

![Q24 coupling defect versus correlation](docs/figures/quantitative/q24_coupling_defect_vs_correlation.svg)

**Q24 — Coupling defect.** In the displayed balanced binary family, the response-factorization defect is zero at independence and grows with correlation magnitude.

---

# 11. P17-P18 — coarse-graining, information loss, and scale sufficiency

![P17 coarse-graining and refinement](docs/figures/p17_coarse_graining_refinement.svg)

## 11.1 P17 — information can be erased by scale reduction

Let

\[
C:\Omega_f\to\Omega_c
\]

be deterministic and define pushforward

\[
\boxed{
C_\#P(y)=\sum_{x:C(x)=y}P(x).
}
\]

P17 proves the data-processing inequality

\[
\boxed{
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

![Q25 TV contraction under binning](docs/figures/quantitative/q25_tv_contraction_binning.svg)

**Q25 — Progressive coarse binning.** Deterministic merging cannot increase total-variation distinguishability. The numerical example directly verifies the P17 inequality.

![Q26 exact coarse-graining collision](docs/figures/quantitative/q26_exact_coarse_graining_collision.svg)

**Q26 — Exact collision.** If \(x\ne x'\) but \(C(x)=C(x')\), then

\[
\|\delta_x-\delta_{x'}\|_{\mathrm{TV}}=1,
\qquad
\boxed{
\|C_\#\delta_x-C_\#\delta_{x'}\|_{\mathrm{TV}}=0.
}
\]

Thus a coarse representation can make distinct fine responses observationally identical.

## 11.2 P18 — a coarse scale can still be sufficient for a declared family

![P18 scale-sufficiency certificate](docs/figures/p18_scale_sufficiency_certificate.svg)

Let \(R(x\mid y)\) be a fiber-consistent stochastic decoder. Define

\[
D=R_\#C_\#,
\qquad
\rho(P)=\|P-DP\|_{\mathrm{TV}},
\]

and for declared response family \(\mathcal F\),

\[
\boxed{
\rho_{\mathcal F}
=\sup_{P\in\mathcal F}\rho(P).
}
\]

P18 proves

\[
\boxed{
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}
\le
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
+\rho(P)+\rho(Q).
}
\]

Therefore

\[
\boxed{
0
\le
\|P-Q\|_{\mathrm{TV}}
-
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
2\rho_{\mathcal F}.
}
\]

![Q27 reconstruction defect versus decoder mismatch](docs/figures/quantitative/q27_reconstruction_defect_decoder_mismatch.svg)

**Q27 — Decoder mismatch.** With fixed coarse mass, reconstruction error is controlled by mismatch between the decoder and the true within-fiber conditional structure.

For finite family \(\mathcal F\), define

\[
\delta_f
=\min_{P\ne Q}\|P-Q\|_{\mathrm{TV}},
\qquad
\delta_c
=\min_{P\ne Q}\|C_\#P-C_\#Q\|_{\mathrm{TV}}.
\]

Then

\[
\boxed{
\delta_c\ge\delta_f-2\rho_{\mathcal F}.
}
\]

![Q28 P18 identifiability margin](docs/figures/quantitative/q28_p18_scale_identifiability_margin.svg)

**Q28 — Scale-identifiability margin.** If

\[
\boxed{
\delta_f>2\rho_{\mathcal F},
}
\]

then \(\delta_c>0\), so all declared response laws remain distinct at the coarse scale.

![Q29 exact family scale sufficiency](docs/figures/quantitative/q29_exact_family_scale_sufficiency.svg)

**Q29 — Exact family sufficiency.** If \(\rho_{\mathcal F}=0\), then all pairwise response distances are preserved exactly on the declared family even when the global map \(C\) is many-to-one. Global microscopic invertibility is therefore sufficient but not necessary for family-level sufficiency.

![Q40 P18 admissible bound region](docs/figures/quantitative/q40_p18_bound_admissible_region.svg)

**Q40 — P18 bound region.** Every admissible geometry-loss value lies below

\[
\boxed{
d_f-d_c\le\rho(P)+\rho(Q).
}
\]

The sharp collapsed-fiber witness can attain the boundary.

### Scientific boundary of P18

P18 certifies response-law and response-geometry preservation. It does **not** automatically prove preservation of directed influence \(\mathcal A\), partition irreducibility \(\mathcal K\), intervention semantics, genuine split/merge dynamics, or any experiential property. Those require separate compatibility assumptions and theorems.

---

# 12. Observer-to-bridge handoff

![Observer-to-bridge handoff](docs/figures/observer_to_bridge_handoff.svg)

The foundation repository identifies candidate moving subsystems as world-tubes

\[
\boxed{
\mathcal W=(S_0,\ldots,S_{T-1}).
}
\]

with recovery, identifiability, physical-time calibration, and finite-sample certification. This repository asks what happens **after** a physical subsystem has been identified.

![Q39 world-tube centerline projection](docs/figures/quantitative/q39_world_tube_centerline_projection.svg)

**Q39 — Moving subsystem.** The synthetic world-tube projection makes the handoff geometrically explicit: a persistent physical subsystem moves through observed coordinates before its intervention-response structure is analyzed.

The combined program is

```text
physical measurements
        |
        v
effective dynamical model
        |
        v
certified persistent moving subsystem
        |
        |  Spatiotemporal Observer Mathematics
        v
physical equivalence class [p]
        |
        v
intervention-resolved causal structure
        |
        v
temporal continuation + finite-error certification
        |
        v
composition + coupling
        |
        v
coarse-graining + scale sufficiency
        |
        v
candidate physical-to-experiential bridge
        |
        v
empirical discrimination / falsification
```

**Foundation:** [MahsaKeikha/spatiotemporal-observer-math](https://github.com/MahsaKeikha/spatiotemporal-observer-math)

---

# 13. Empirical consciousness-measurement interface

![Conscious-state measurement map](docs/figures/conscious_state_measurement_map.svg)

**Measurement map.** Behavioral responsiveness, report, perturbational response, neural dynamics, imaging, and theoretical interpretation are not interchangeable measurements.

## 13.1 Perturbational response

![Q37 synthetic perturbational spreading](docs/figures/quantitative/q37_synthetic_perturbational_spreading.svg)

**Q37 — Synthetic perturbational spreading.** This is a controlled network-response illustration showing spatial propagation and temporal decay before response distances are computed. It is explicitly **synthetic**, not patient or neural data.

Empirical perturbational work such as Casali et al. uses controlled cortical perturbation and distributed EEG response across conscious and unconscious conditions. The repository treats such work as an empirical measurement interface, not as proof of the present bridge candidate.

## 13.2 Dynamical complexity

![Q38 synthetic dynamical complexity trace](docs/figures/quantitative/q38_synthetic_dynamical_complexity_trace.svg)

**Q38 — Synthetic complexity trace.** The figure stress-tests time-varying structure using a deterministic multiscale signal. It is **not** presented as a validated consciousness measure.

Empirical consciousness science reports state-dependent changes in perturbational complexity, critical dynamics, integration, and network organization. Those findings constrain candidate physical models but do not independently supply an experiential bridge.

## 13.3 Selected empirical lineages

- **Casali et al. 2013** — perturbational complexity across conscious and unconscious conditions.
- **Maschke et al. 2024** — relationships among critical EEG dynamics, anesthesia, and perturbational complexity.
- **Luppi et al. 2024** — synergistic information integration across conscious-state conditions.
- **Cogitate Consortium et al. 2025** — adversarial comparison of predictions from major consciousness theories using fMRI, MEG, and intracranial EEG.

See [Literature Map](docs/literature_map.md) and [Foundational Physics, Mathematics, and Spaceflight Bibliography](docs/foundational_physics_mathematics_bibliography.md) for the source-role map.

---

# 14. Candidate theory families and empirical discrimination

![Candidate theory comparison map](docs/figures/theory_comparison_map.svg)

Major theory families are translated into a common interface

\[
\boxed{
\mathfrak T_j=(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
}
\]

| Theory family | Physical feature family | Bridge style | Empirical exposure |
| --- | --- | --- | --- |
| **IIT** | intrinsic causal / cause-effect structure | phenomenal axioms to physical postulates | causal structure and perturbation |
| **GNWT** | workspace organization, ignition, amplification, long-range availability | access/content tied to workspace dynamics | timing, report, long-range dynamics |
| **RPT** | recurrent processing | recurrence as central phenomenal-processing condition | local temporal disruption and recurrence |
| **Higher-order** | higher-order representational relation | consciousness in virtue of higher-order relation | first-order / higher-order dissociation |
| **Predictive / neurorepresentational / active-inference families** | prediction, inference, precision, multimodal representation | heterogeneous theory-specific bridge | prediction, precision, hierarchy, perturbation |
| **Repository candidate** | response geometry, directed influence, partition landscape, temporal path, composition, scale behavior | experiential bridge intentionally left open | perturbation, counterexamples, finite-data recovery, temporal, composition, scale and substrate tests |

The comparison is **not a ranking**. P2-P7 provide precise questions about what an experiment class can distinguish, what a physical feature can support, and when two theories are observationally equivalent.

---

# 15. Spaceflight and extreme-environment stress testing

![Spaceflight and extreme-environment relevance map](docs/figures/spaceflight_extreme_environment_map.svg)

Spaceflight is included as a demanding application environment for cognition, physiology, temporal state estimation, sleep/circadian disruption, workload, altered gravity, radiation, isolation, and human-system monitoring.

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
\text{workload}
}
\]

The role of this layer is **robustness testing and application**, not independent evidence for a consciousness bridge.

---

# 16. Falsification program

A scientifically useful physical signature or bridge must be able to fail.

## Representation failure

\[
p\sim_Pp'
\quad\text{but}\quad
F(p)\ne F(p').
\]

## Feature-sufficiency failure

\[
F(p)=F(p')
\quad\text{but}\quad
\bar B(p)\ne\bar B(p').
\]

## Observational identifiability failure

\[
\Delta_\Pi=0.
\]

## Experimental-recoverability failure

\[
\Psi_\Pi(p)=\Psi_\Pi(p')
\quad\text{but}\quad
F_*(p)\ne F_*(p').
\]

## Compression failure

P12-P13 give explicit one-component and pairwise projection collisions.

## Temporal failure

P14 shows that equal endpoints can conceal nonzero path variation. P15 prevents finite-error uncertainty from being hidden by forced classification.

## Composition failure

P16 provides the independent product-response null model. Any higher-level theory must distinguish coexistence from coupling.

## Scale failure

P17 proves that coarse-graining can erase physical distinctions. P18 adds the complementary positive criterion: a chosen coarse scale must have reconstruction defect small relative to the response distinctions that the theory needs to preserve.

[Read the complete falsification program](docs/falsification_program.md).

---

# 17. Numerical validation facts

The visual atlas is tied to executable checks rather than decorative graphics.

| Validation checkpoint | Tested value / relation | Role |
| --- | ---: | --- |
| OU stationary variance, \(\theta=1.4,\sigma=0.65\) | **0.1508928571** | verifies Q02 closed form |
| Landauer bound at 300 K | **2.870978885e-21 J** | verifies Q09 physical scale |
| Q05 state-space eigenvalue real part | **-0.4** | verifies asymptotic stability |
| Q12 Markov subdominant eigenvalue | **0.74** | verifies mixing relation |
| explicit P17 fine TV witness | **0.6** | verifies nonzero fine distinction |
| same P17 witness after collision coarse map | **0.0** | verifies exact information loss |
| P18 exact-family reconstruction defect | **0.0** | verifies exact family sufficiency |
| P18 fine/coarse minimum separation under exact decoding | **equal** | verifies exact geometry preservation |
| P9 gap scaling | \(n(2\gamma)=n(\gamma)/4\) | verifies inverse-square law |
| quantitative figure inventory | **40** | guards visual completeness |

The complete numerical audit is documented in [Quantitative Atlas Validation Report](docs/quantitative_atlas_validation_report.md).

---

# 18. Claim hierarchy

| Status | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the framework |
| **Proved** | theorem derived from explicit assumptions |
| **Identifiability / no-go result** | theorem about what observations, projections, or scale transformations can or cannot determine |
| **Candidate physical signature** | physical structure proposed for testing, not an experiential conclusion |
| **Finite-error certificate** | conclusion guaranteed under declared estimation-error bounds |
| **Synthetic example** | controlled mathematical or numerical illustration, not empirical evidence |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Application domain** | environment in which physical or cognitive markers may be stress-tested |
| **Counterexample** | explicit construction defeating a sufficiency, compression, recoverability, or scale-preservation claim |
| **Open bridge problem** | unresolved relation between physical and experiential equivalence structure |

This distinction is maintained throughout the main page, code, proposition documents, and visual atlas.

---

# 19. Reproducibility and audit path

Install the research package and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the complete test suite:

```bash
pytest
```

Run static checks:

```bash
ruff check .
```

Regenerate the 40 quantitative figures:

```bash
python scripts/generate_quantitative_atlas.py
```

The repository also contains a GitHub workflow that regenerates the quantitative atlas and commits changed SVGs, making the visual record reproducible from code.

The code audits:

- representation invariance;
- theory discriminability and optimal binary testing;
- observational theory-equivalence classes;
- maximin and set-cover experiment design;
- physical-feature sufficiency and canonical bridge signatures;
- experimental recoverability;
- finite-error partition recovery;
- categorical sample complexity;
- robust protocol-family optimization;
- intervention-response geometry;
- partition-product models and irreducibility;
- directed perturbational influence;
- one-component and pairwise projection collisions;
- quotient temporal metrics and temporal path variation;
- finite-error temporal certification;
- independent product-response composition;
- cross-system influence and coupling defects;
- deterministic coarse-graining and pushforward laws;
- total-variation contraction and refinement collisions;
- P18 stochastic decoding and scale-sufficiency bounds;
- quantitative-atlas figure inventory and SVG integrity;
- numerical physics and mathematics checkpoints;
- documentation-link integrity;
- publication-style figure quality and terminology consistency.

---

# 20. Full visual and source audit

The entire quantitative atlas is visible here on the main page in scientific order. For researchers who want the same material as a dedicated figure index:

- [Quantitative Physics & Mathematics Atlas](docs/quantitative_physics_mathematics_atlas.md)
- [Quantitative Atlas Validation Report](docs/quantitative_atlas_validation_report.md)
- [Theorem Roadmap](docs/theorem_roadmap.md)
- [Multiscale Physical Hierarchy](docs/multiscale_physical_hierarchy.md)
- [Equation and Citation Map](docs/equation_and_citation_map.md)
- [Foundational Physics, Mathematics, and Spaceflight Bibliography](docs/foundational_physics_mathematics_bibliography.md)
- [`references.bib`](references.bib)
- [`CITATION.cff`](CITATION.cff)

The links are audit paths, not substitutes for the main narrative: the core mathematics, figures, examples, theorem chain, and research boundary are intentionally visible directly in this README.

---

# 21. Current frontier

The current frontier is deliberately more demanding than adding another scalar or another conceptual diagram.

1. **Extend scale certification from response geometry to directed influence.** Determine block-compatibility conditions under which \(\mathcal A\) admits a P18-style distortion bound.
2. **Control partition structure across scale.** Characterize when the partition lattice is compatible enough for \(\mathcal K\) to remain comparable.
3. **Finite-sample scale certification.** Derive confidence radii for \(\rho_{\mathcal F}\), \(\delta_f\), \(\delta_c\), and the P18 margin from actual estimators.
4. **Genuine physical splitting and merging.** Distinguish descriptive coarse-graining from changes in dynamics, state variables, and intervention channels.
5. **Observer-to-causal-structure interface.** Feed certified world-tubes directly into time-indexed intervention-response systems.
6. **Irregular physical time.** Normalize structural path variation by actual cadence and continuous-time limits.
7. **Thermodynamic constraints.** Connect candidate physical structure to measurable energy flow and entropy production without assuming a bridge conclusion.
8. **Information-geometric structure.** Determine whether intervention-conditioned response families admit useful invariant manifold geometry beyond total variation.
9. **Cross-theory adversarial experiments.** Maximize empirical separation among serious theory families on shared perturbational protocols.
10. **Biological and artificial counterexamples.** Search for systems matching rich causal structure while differing in relevant experiential evidence.
11. **Experiential formalization.** Define \(\mathcal Q_E\), experiential invariances, and candidate bridge principles independently of the physical candidate.
12. **Bridge theorem.** Attempt a conditional physical-to-experiential implication only after physical, experiential, identifiability, finite-data, temporal, compositional, scale, and falsification layers are jointly explicit.

The current mathematical research chain is

\[
\boxed{
\text{controlled physical response}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{representation-invariant temporal trajectory}
\longrightarrow
\text{finite-error certification}
\longrightarrow
\text{composition and coupling}
\longrightarrow
\text{scale loss + scale sufficiency}.
}
\]

The next scientific problem is not to declare that this chain *is* consciousness. It is to determine what additional, independently justified structure could connect this certified physical chain to a formal experiential domain—and what experiments could prove that proposed connection wrong.

---

# Start here for a deeper audit

| Reader goal | Entry point |
| --- | --- |
| Follow the complete quantitative visual program | **[Quantitative Physics & Mathematics Atlas](docs/quantitative_physics_mathematics_atlas.md)** |
| Check the numerical facts behind the figures | **[Quantitative Atlas Validation Report](docs/quantitative_atlas_validation_report.md)** |
| Follow P1-P18 in proof order | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Read the structured physical candidate | **[P11 — Intervention-Resolved Causal Structure](docs/proposition_11_intervention_resolved_causal_structure.md)** |
| Read the scale-loss theorem | **[P17 — Coarse-Graining and Refinement](docs/proposition_17_coarse_graining_and_refinement.md)** |
| Read the scale-sufficiency theorem | **[P18 — Scale Sufficiency by Approximate Reconstruction](docs/proposition_18_scale_sufficiency_certification.md)** |
| Trace equations to sources | [Equation and Citation Map](docs/equation_and_citation_map.md) |
| Inspect failure conditions | [Falsification Program](docs/falsification_program.md) |
| Continue backward to subsystem identification | [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math) |
| Cite the program | [`CITATION.cff`](CITATION.cff) |
