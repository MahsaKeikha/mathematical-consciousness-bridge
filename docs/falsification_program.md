# Falsification Program

A bridge theory or candidate physical signature is scientifically useful only when its assumptions and predictions are exposed to explicit failure modes.

The repository therefore treats counterexamples as part of the main theorem program, not as an appendix.

![Research architecture](figures/research_architecture.svg)

---

# 1. Representation failure

Apply physically equivalent coordinate transformations, relabelings, unit changes, invertible encodings, and other transformations included in the declared physical equivalence relation.

If

\[
p\sim_Pp'
\]

but a proposed bridge or physical signature satisfies

\[
F(p)\ne F(p')
\]

or

\[
B(p)\ne B(p'),
\]

the object is not well defined on the declared physical quotient.

[Proposition 1](proposition_1_representation_invariance.md) gives the exact quotient factorization criterion.

---

# 2. Physical-feature sufficiency failure

Suppose a theory claims that a physical feature

\[
F:\mathcal Q_P\to\mathcal Z
\]

is sufficient to determine the bridge.

A direct counterexample is a pair

\[
\boxed{
F(p)=F(p')
\qquad\text{but}\qquad
\bar B(p)\ne\bar B(p').
}
\]

By [Proposition 5](proposition_5_feature_sufficiency.md), such a pair proves that the bridge cannot factor through \(F\) on the declared domain.

This is the principal test for claims that integration, recurrence, broadcasting, complexity, prediction, or another physical feature is sufficient by itself.

---

# 3. Observational identifiability failure

For competing theories \(\mathfrak T_1,\mathfrak T_2\), define

\[
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
\]

If

\[
\boxed{
\Delta_\Pi=0,
}
\]

then every experiment in the declared class produces the same observable law under the two theories.

[Propositions 2 and 3](theorem_roadmap.md) formalize this no-go condition. A theory pair in the same observational equivalence class cannot be separated by statistical analysis of that experiment family because the data-generating laws coincide.

---

# 4. Experimental-recoverability failure

Suppose \(F_*\) is proposed as a complete physical signature. Let

\[
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi}
\]

be the complete observable physical fingerprint.

If there exists

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\qquad\text{but}\qquad
F_*(p)\ne F_*(p'),
}
\]

then [Proposition 7](proposition_7_experimental_signature_recovery.md) proves that the signature is not recoverable from that experiment class.

The remedy is not to relabel the signature as unobservable. The theory must either enlarge the admissible experiment class, weaken the signature claim, or state the resulting underdetermination explicitly.

---

# 5. Finite-data failure

A population-level separation can disappear under finite estimation error.

For robust signature gap

\[
\gamma_S
=
\delta_S-\omega_S,
\]

[Proposition 8](proposition_8_robust_signature_recovery.md) requires

\[
\boxed{
\gamma_S>4\varepsilon
}
\]

for its current exact-recovery guarantee under uniform TV error \(\varepsilon\).

If the certified error radius is too large for this condition, the declared data do not certify exact recovery under the current theorem.

[Proposition 9](proposition_9_categorical_sample_complexity.md) converts the same requirement into an explicit finite trial bound in the categorical benchmark.

---

# 6. Experiment-design failure

More measurements are not automatically more informative for a bridge signature.

For protocol family \(S\),

\[
\Gamma(S)
=
\delta(S)-\omega(S).
\]

If added protocol \(\rho\) produces between-signature gain \(a_\rho(S)\) and within-signature inflation \(b_\rho(S)\), [Proposition 10](proposition_10_robust_experiment_design.md) proves

\[
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
\]

Thus a modality that mainly increases nuisance variation should not be treated as an automatic scientific improvement.

---

# 7. Causal-structure component minimality

The intervention-resolved causal-structure candidate retains

\[
\mathcal G_p,
\qquad
\mathcal A_p,
\qquad
\mathcal K_p.
\]

[Proposition 12](proposition_12_component_insufficiency.md) applies the projection-collision theorem

\[
\boxed{
H(x)=H(x')
\text{ and }
F(x)\ne F(x')
\Longrightarrow
\nexists g:F=g\circ H.
}
\]

It constructs explicit finite systems showing that response geometry alone, directed marginal influence alone, partition irreducibility alone, response diameter, minimum irreducibility, and a Boolean cycle indicator are each incomplete reductions on the tested domains.

![P12 collision map](figures/p12_collision_map.svg)

[Proposition 13](proposition_13_pairwise_component_irredundancy.md) strengthens the audit by constructing three pairwise collision families:

\[
(\mathcal G,\mathcal A)\text{ fixed while }\mathcal K\text{ changes},
\]

\[
(\mathcal G,\mathcal K)\text{ fixed while }\mathcal A\text{ changes},
\]

\[
(\mathcal A,\mathcal K)\text{ fixed while }\mathcal G\text{ changes}.
\]

![P13 pairwise component irredundancy](figures/p13_component_irredundancy.svg)

The current conclusion is component-level irredundancy on the declared audit domain, not a global minimality theorem over every physical representation.

---

# 8. Non-neural and engineered counterexamples

The causal-structure candidate is deliberately tested outside the human-brain domain because generic causal integration, recurrence, complexity, and controllability can occur in systems for which an experiential interpretation cannot simply be assumed.

Priority counterexample classes include:

| Counterexample class | Scientific question |
| --- | --- |
| integrated non-neural biological network | can a rich causal-structure signature occur without the target experiential evidence? |
| recurrent artificial controller | do recurrence and irreducibility overgenerate the candidate? |
| feedforward surrogate matched on passive behavior | do interventions reveal the hidden causal difference? |
| simulator reproducing selected response statistics | which physical causal properties survive simulation and which do not? |
| conscious/unconscious biological pair with similar gross activity | does the full causal-structure candidate separate the states? |

These cases are essential for avoiding a circular definition in which any sufficiently complicated causal system is assigned the target experiential class by construction.

---

# 9. Temporal disruption tests

Perturb or compare:

- persistence;
- recurrence;
- memory;
- synchronization;
- time-resolved intervention-response structure;
- world-tube continuity;
- state transitions under anesthesia, sleep, injury, recovery, or controlled artificial dynamics.

A future temporal theorem must state which changes should preserve a bridge class and which should change it.

---

# 10. Composition tests

Compare:

1. isolated systems;
2. independent composition;
3. weakly coupled systems;
4. strongly coupled systems;
5. split systems;
6. merged systems;
7. systems connected only through controlled communication channels.

The theory must predict whether physical-signature and bridge classes remain separate, combine, become non-identifiable, or undergo a defined structural transition.

---

# 11. Cross-theory adversarial tests

IIT, GNWT, RPT, higher-order, predictive/neurorepresentational, active-inference, and the intervention-resolved causal-structure candidate are represented through the common interface

\[
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
\]

The goal is to identify protocols under which their predicted observable laws diverge, then use P4 to choose experiments that expose those differences efficiently.

See [Candidate Theory Families](candidate_theory_families.md).

---

# 12. Clinical and behavioral interfaces

Future empirical work may compare bridge predictions across states in which report, responsiveness, memory, arousal, perturbational complexity, integration, and neural dynamics dissociate.

No single behavioral report or single neural measure is used as the definition of the target experiential class. The purpose is to test whether a proposed bridge/signature explains convergent and divergent evidence across independently specified measurement models.

---

# 13. Falsification ledger standard

Every major candidate should eventually receive a table with at least:

| Field | Required record |
| --- | --- |
| claim | exact mathematical or empirical statement being tested |
| assumptions | declared physical, statistical, and bridge assumptions |
| counterexample class | system family capable of defeating the claim |
| protocol | admissible intervention / observation design |
| discriminant | quantity whose sign, distance, or distribution separates hypotheses |
| uncertainty | finite-data confidence or error radius |
| outcome | supported, rejected, unresolved, or non-identifiable under the declared model |
| next test | experiment or theorem needed to reduce the remaining ambiguity |

The strongest bridge result should survive this ledger rather than bypass it.
