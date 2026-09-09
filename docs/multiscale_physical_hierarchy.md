# Multiscale Physical Hierarchy

![Multiscale physical hierarchy](figures/multiscale_physical_hierarchy.svg)

This page explains how the two research repositories connect across physical scale and mathematical abstraction.

The key research sequence is

\[
\boxed{
\text{local physical dynamics}
\longrightarrow
\text{network state}
\longrightarrow
\text{certified moving subsystem}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{temporal / compositional / scale analysis}
\longrightarrow
\text{bridge test}.
}
\]

The sequence is not intended as a reduction of consciousness to one physical quantity. Each arrow introduces an additional scientific problem with its own assumptions, observables, equations, and failure modes.

---

## 1. Local physical dynamics

A stochastic controlled physical model may be written

\[
dX_t
=
f(X_t,u_t)\,dt
+G(X_t,u_t)\,dW_t.
\]

At this layer the scientific questions concern physical state, dynamics, noise, energy exchange, boundary conditions, and intervention semantics.

Relevant mathematical and physical lineages include stochastic processes, statistical mechanics, nonequilibrium thermodynamics, and control theory.

---

## 2. Network-scale physical state

At cellular, neural, sensor-network, or engineered-system scale, the physical process may be represented through a transition kernel

\[
X_{t+\Delta t}
\sim
K_{\Delta t}(\cdot\mid X_t,u_t).
\]

The declared state variables may be spikes, local field potentials, coarse physiological variables, device states, or other experimentally defined coordinates.

The scale choice matters. Proposition 17 proves that deterministic many-to-one coarse-graining can contract total-variation distinguishability and can map physically distinct fine states to exactly the same coarse state.

---

## 3. Certified moving subsystem

The companion repository [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math) asks which subsystem boundary is dynamically distinguished by the measured process.

Its candidate physical object is a world-tube

\[
\mathcal W
=
(S_0,\ldots,S_{T-1}).
\]

The observer-math layer studies integration, insulation, persistence, transport, identifiability, temporal calibration, and finite-sample certification.

The result is a physically and statistically defined subsystem. It does not assign an experiential property to that subsystem.

---

## 4. Intervention-resolved causal structure

For a physical subsystem \(p\), admissible intervention \(u\), and delay \(\tau\), define

\[
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
\]

The repository then studies three complementary structures:

\[
\mathcal G_p
\quad\text{response geometry},
\]

\[
\mathcal A_p
\quad\text{directed interventional influence},
\]

and

\[
\mathcal K_p
\quad\text{partition irreducibility}.
\]

The combined physical signature is

\[
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
\]

Propositions 11-13 define this physical structure and show, on explicit audit domains, that one-component and two-component compressions lose information.

---

## 5. Time, composition, and scale

The physical candidate is then tested under operations that a universal physical theory must handle.

### Temporal continuation

Proposition 14 defines a quotient-space distance between time-indexed causal-structure states and a cumulative path variation

\[
V_{0:T}
=
\sum_t
\overline D([c_t],[c_{t+1}]).
\]

Proposition 15 adds finite-error certification.

### Independent composition and coupling

For independent systems \(A\) and \(B\), the declared null model is

\[
P_{AB}
=
P_A\otimes P_B.
\]

Proposition 16 characterizes this null model and introduces a response-level coupling defect based on departure from product structure.

### Coarse-graining

For deterministic coarse-graining map \(C\), Proposition 17 proves

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

This is a direct data-processing statement: deterministic coarse-graining cannot increase total-variation distinguishability.

---

## 6. Empirical interface

The physical and mathematical structure must connect to measurements without identifying the measurement with consciousness.

Relevant empirical interfaces include:

- perturbational EEG and complexity measures;
- anesthesia and state transitions;
- sleep and dream reports;
- command-following and covert cognitive-motor dissociation;
- MEG, fMRI, intracranial recordings, and physiological monitoring;
- extreme-environment cognition and human-performance monitoring.

The [Conscious-State Measurement Atlas](conscious_state_measurement_atlas.md) documents important dissociations between behavioral responsiveness, report, neural evidence, perturbational response, and theory interpretation.

---

## 7. Extreme-environment robustness

NASA Human Research Program sources are included as an application and validation domain for cognition, sleep, behavioral performance, workload, altered gravity, radiation, and human-system monitoring.

The repository does not use spaceflight research as evidence for a consciousness equation. Its scientific role is different: it provides demanding conditions under which temporal state estimation, physiological monitoring, measurement stability, and model robustness can be stress-tested.

See the [Foundational Physics, Mathematics, and Spaceflight Bibliography](foundational_physics_mathematics_bibliography.md).

---

## 8. Open bridge layer

The open mathematical target is a quotient-level bridge

\[
\bar B:
\mathcal Q_P
\longrightarrow
\mathcal Q_E,
\]

where \(\mathcal Q_P\) is a physically meaningful quotient and \(\mathcal Q_E\) is an independently formalized experiential quotient.

The strongest structural target remains

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

for a physical feature \(F_*\) justified independently of the bridge labels.

The multiscale program therefore asks not only whether a physical signature is mathematically interesting, but whether it is:

1. representation invariant;
2. temporally coherent;
3. compositionally consistent;
4. stable or interpretable across scale;
5. experimentally recoverable;
6. finite-data certifiable;
7. empirically discriminating against serious alternatives;
8. compatible with an independently justified experiential formalization.

---

## 9. Source-role discipline

The figure combines several source traditions, but their roles remain separate:

| Source lineage | Role in the hierarchy |
| --- | --- |
| Shannon | information-theoretic quantities |
| Amari | statistical-manifold / information-geometric structure |
| Landauer and Seifert | thermodynamics of information and nonequilibrium trajectories |
| Pearl | intervention semantics |
| Tegmark | physical factorization / observer-structure lineage |
| Casali and related perturbational work | empirical perturbation-response interface |
| Luppi and related information-integration work | empirical integration / control / state evidence |
| adversarial theory-testing literature | cross-theory empirical discrimination |
| NASA Human Research Program | extreme-environment cognition and operational validation domain |

Full role-aware citations are maintained in the repository bibliographies and [Physics Equation Provenance](physics_equation_provenance.md).