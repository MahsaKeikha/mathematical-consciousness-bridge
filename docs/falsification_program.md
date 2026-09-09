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

This is the principal test for claims that integration, recurrence, broadcasting, complexity, prediction, temporal continuity, or another physical feature is sufficient by itself.

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

# 8. Temporal representation failure

A temporal comparison can be physically meaningless if arbitrary changes of labels appear as structural jumps.

[Proposition 14](proposition_14_temporal_continuation.md) addresses this by comparing causal-structure states through the quotient metric

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

under a declared finite group of admissible isometric relabelings.

A candidate temporal statistic fails the P14 representation test if time-dependent admissible relabeling changes its reported physical variation.

---

# 9. Endpoint-only temporal failure

A start/end comparison can hide substantial intermediate change.

P14 gives the explicit construction

\[
[a]\longrightarrow[b]\longrightarrow[a],
\qquad [a]\ne[b].
\]

Then

\[
\overline D_w([c_0],[c_2])=0,
\]

while

\[
\boxed{
V_{0:2}
=
2\overline D_w([a],[b])
>0.
}
\]

Any theory of physical continuation that infers a trivial path solely from equal endpoints fails on this construction.

![P14 temporal continuation](figures/p14_temporal_continuation.svg)

---

# 10. Temporal finite-error overclaiming

An estimated temporal change is not automatically a certified physical change.

Suppose

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t
\]

holds on the declared simultaneous error event. [Proposition 15](proposition_15_finite_sample_temporal_certification.md) proves

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

Therefore

\[
\widehat d_{st}
\le
\varepsilon_s+\varepsilon_t
\]

is **not** evidence that the true temporal distance is zero. It means only that a nonzero separation is not certified by the current radius.

For a threshold \(\eta\), the correct finite-data output is three-way:

1. certified above threshold when the lower bound exceeds \(\eta\);
2. certified below threshold when the upper bound is at most \(\eta\);
3. unresolved otherwise.

Forcing an unresolved interval into a binary scientific conclusion is a falsification failure of the inference procedure, not evidence for the physical hypothesis.

![P15 finite-sample temporal certification](figures/p15_finite_sample_temporal_certification.svg)

---

# 11. Estimator-model mismatch

The explicit P15 Hoeffding radius applies only to its declared special case: bounded coordinates estimated as IID sample means.

The general P11 components can involve response-law distances, suprema over interventions, marginals, and partition-product constructions. If those estimators do not satisfy the assumptions used to derive the claimed radius, then the temporal certificate is unsupported.

The remedy is estimator-specific concentration or a weaker uncertainty statement, not reuse of the simple sample-mean bound outside its scope.

---

# 12. Non-neural and engineered counterexamples

The causal-structure candidate is deliberately tested outside the human-brain domain because generic causal integration, recurrence, complexity, controllability, and temporal continuity can occur in systems for which an experiential interpretation cannot simply be assumed.

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

# 13. Composition tests

Compare:

1. isolated systems;
2. independent composition;
3. weakly coupled systems;
4. strongly coupled systems;
5. split systems;
6. merged systems;
7. systems connected only through controlled communication channels.

The theory must predict whether physical-signature and bridge classes remain separate, combine, become non-identifiable, or undergo a defined structural transition.

Composition is the next major structural frontier after P14-P15 because the current temporal metric assumes a fixed-dimensional fingerprint and therefore does not yet handle block birth, death, splitting, or merging.

---

# 14. Cross-theory adversarial tests

IIT, GNWT, RPT, higher-order, predictive/neurorepresentational, active-inference, and the intervention-resolved causal-structure candidate are represented through the common interface

\[
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
\]

The goal is to identify protocols under which their predicted observable laws diverge, then use P4 to choose experiments that expose those differences efficiently.

See [Candidate Theory Families](candidate_theory_families.md).

---

# 15. Clinical and behavioral interfaces

Future empirical work may compare bridge predictions across states in which report, responsiveness, memory, arousal, perturbational complexity, integration, temporal dynamics, and neural organization dissociate.

No single behavioral report, neural measure, or temporal-continuation statistic is used as the definition of the target experiential class. The purpose is to test whether a proposed bridge/signature explains convergent and divergent evidence across independently specified measurement models.

---

# 16. Falsification ledger standard

Every major candidate should eventually receive a table with at least:

| Field | Required record |
| --- | --- |
| claim | exact mathematical or empirical statement being tested |
| assumptions | declared physical, statistical, temporal, and bridge assumptions |
| counterexample class | system family capable of defeating the claim |
| protocol | admissible intervention / observation design |
| discriminant | quantity whose sign, distance, or distribution separates hypotheses |
| uncertainty | finite-data confidence or error radius |
| outcome | supported, rejected, unresolved, or non-identifiable under the declared model |
| next test | experiment or theorem needed to reduce the remaining ambiguity |

The strongest bridge result should survive this ledger rather than bypass it.
