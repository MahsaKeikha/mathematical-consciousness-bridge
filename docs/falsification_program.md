# Falsification Program

**This page asks one question: how could a proposed bridge claim fail?**

A scientific framework becomes more useful when it makes failure visible. This repository therefore treats counterexamples, nonidentifiability, uncertainty, and model rejection as part of the main research program.

If you want the broad story first, open the [Research Map](research_map.md). If you want the formal details, use the expandable sections below.

![Research architecture](figures/research_architecture.svg)

## The failure map in one minute

| Failure type | Plain language question | Main formal route |
| --- | --- | --- |
| **Representation failure** | Does the conclusion change when only labels or equivalent descriptions change? | P1 |
| **Sufficiency failure** | Can two cases look the same to the proposed physical feature but differ in the target? | P5, P19 |
| **Observational failure** | Could competing theories produce exactly the same observable data? | P2 to P4 |
| **Recovery failure** | Can the proposed signature actually be inferred from the declared experiments? | P7 to P10 |
| **Uncertainty failure** | Is the claimed separation larger than finite data or numerical uncertainty? | P8, P9, P15 and later finite data results |
| **Candidate stress test** | Does a simplified physical feature collapse distinctions that the fuller candidate preserves? | P12, P13 |
| **Temporal failure** | Does the method confuse relabeling, endpoints, or estimation noise with real structural change? | P14, P15 |
| **Domain failure** | Does the proposed criterion also classify engineered or nonneural systems in ways the theory cannot justify? | Counterexample program |
| **Comparative failure** | Can the proposal be distinguished from serious alternative theories? | Common theory interface |

The point is not to make every theory fail. The point is to make it clear **what evidence would count against a claim**.

## How to use this page

You do not need to read every test.

If your question is about representation, open Tests 1 and 2.

If your question is about data and experiments, open Tests 3 through 6.

If your question is about the intervention resolved physical candidate, open Tests 7 through 11.

If your question is about broader scientific interpretation, open Tests 12 through 16.

---

<details>
<summary><strong>Test 1: Representation failure</strong></summary>

Apply coordinate transformations, relabelings, unit changes, invertible encodings, and other transformations included in the declared physical equivalence relation.

If

\[
p\sim_Pp'
\]

but a proposed physical signature or bridge satisfies

\[
F(p)\ne F(p')
\]

or

\[
B(p)\ne B(p'),
\]

the object is not well defined on the declared physical quotient.

[Proposition 1](proposition_1_representation_invariance.md) gives the exact quotient factorization criterion.

**Interpretation:** changing only the representation should not create a different scientific conclusion.

</details>

<details>
<summary><strong>Test 2: Physical feature sufficiency failure</strong></summary>

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

This is the principal collision test for claims that one physical feature, such as integration, recurrence, broadcasting, complexity, prediction, or temporal continuity, is sufficient by itself.

**Interpretation:** if the proposed feature treats two cases as identical while the target distinguishes them, that feature is not sufficient for that target.

</details>

<details>
<summary><strong>Test 3: Observational identifiability failure</strong></summary>

For competing theories \(\mathfrak T_1,\mathfrak T_2\), define

\[
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
\]

If

\[
\boxed{\Delta_\Pi=0,}
\]

then every experiment in the declared class produces the same observable law under the two theories.

[Propositions 2 and 3](theorem_roadmap.md) formalize this condition.

**Interpretation:** no amount of statistical analysis can distinguish two theories when the declared experiments generate the same probability law under both.

</details>

<details>
<summary><strong>Test 4: Experimental recoverability failure</strong></summary>

Suppose \(F_*\) is proposed as a complete physical signature. Let

\[
\Psi_\Pi(p)=(P^{\pi,p})_{\pi\in\Pi}
\]

be the observable physical fingerprint.

If there exists

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\qquad\text{but}\qquad
F_*(p)\ne F_*(p'),
}
\]

then [Proposition 7](proposition_7_experimental_signature_recovery.md) proves that the signature is not recoverable from that experiment class.

The scientific options are then clear: enlarge the experiment class, weaken the signature claim, or state the underdetermination explicitly.

</details>

<details>
<summary><strong>Test 5: Finite data failure</strong></summary>

A population separation can disappear once estimation error is included.

For robust signature gap

\[
\gamma_S=\delta_S-\omega_S,
\]

[Proposition 8](proposition_8_robust_signature_recovery.md) requires

\[
\boxed{\gamma_S>4\varepsilon}
\]

for its exact recovery guarantee under uniform total variation error \(\varepsilon\).

If the certified error radius is too large for this condition, the data do not certify exact recovery under the current theorem.

[Proposition 9](proposition_9_categorical_sample_complexity.md) converts the same requirement into an explicit trial bound in the categorical benchmark.

**Interpretation:** a visible gap is not enough. The gap must be larger than the uncertainty relevant to the theorem.

</details>

<details>
<summary><strong>Test 6: Experiment design failure</strong></summary>

More measurements are not automatically more informative.

For protocol family \(S\),

\[
\Gamma(S)=\delta(S)-\omega(S).
\]

If added protocol \(\rho\) produces between signature gain \(a_\rho(S)\) and within signature inflation \(b_\rho(S)\), [Proposition 10](proposition_10_robust_experiment_design.md) proves

\[
\Gamma(S\cup\{\rho\})-\Gamma(S)=a_\rho(S)-b_\rho(S).
\]

A modality that mainly increases nuisance variation should therefore not be treated as an automatic scientific improvement.

</details>

---

## Stress testing the physical candidate

<details>
<summary><strong>Test 7: Causal structure component insufficiency</strong></summary>

The intervention resolved causal structure candidate retains

\[
\mathcal G_p,
\qquad
\mathcal A_p,
\qquad
\mathcal K_p.
\]

[Proposition 12](proposition_12_component_insufficiency.md) uses the projection collision criterion

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

[Proposition 13](proposition_13_pairwise_component_irredundancy.md) then constructs three pairwise collision families in which two components are fixed while the third changes.

![P13 pairwise component irredundancy](figures/p13_component_irredundancy.svg)

The conclusion is component level irredundancy on the declared audit domain, not a global minimality theorem over every physical representation.

</details>

<details>
<summary><strong>Test 8: Temporal representation failure</strong></summary>

A temporal comparison can be physically meaningless if arbitrary label changes appear as structural jumps.

[Proposition 14](proposition_14_temporal_continuation.md) compares causal structure states through the quotient metric

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

under a declared finite group of admissible isometric relabelings.

A temporal statistic fails this representation test if an admissible relabeling changes its reported physical variation.

</details>

<details>
<summary><strong>Test 9: Endpoint only temporal failure</strong></summary>

A start and end comparison can hide large intermediate change.

P14 gives the construction

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
\boxed{V_{0:2}=2\overline D_w([a],[b])>0.}
\]

Any method that infers a trivial path solely because the endpoints match fails on this construction.

![P14 temporal continuation](figures/p14_temporal_continuation.svg)

</details>

<details>
<summary><strong>Test 10: Temporal uncertainty overclaiming</strong></summary>

An estimated temporal change is not automatically a certified physical change.

Suppose

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t
\]

holds on the declared simultaneous error event. [Proposition 15](proposition_15_finite_sample_temporal_certification.md) proves

\[
\boxed{|\hat d_{st}-d_{st}|\le\varepsilon_s+\varepsilon_t.}
\]

Therefore a measured distance inside the uncertainty radius is not evidence that the true distance is zero. It means only that a nonzero separation is not certified by the current radius.

For a threshold \(\eta\), the correct output is three way:

1. certified above threshold when the lower bound exceeds \(\eta\);
2. certified below threshold when the upper bound is at most \(\eta\);
3. unresolved otherwise.

![P15 finite sample temporal certification](figures/p15_finite_sample_temporal_certification.svg)

</details>

<details>
<summary><strong>Test 11: Estimator and model mismatch</strong></summary>

The explicit P15 Hoeffding radius applies only to its declared special case: bounded coordinates estimated as IID sample means.

The general P11 components can involve response law distances, suprema over interventions, marginals, and partition product constructions. If those estimators do not satisfy the assumptions used to derive the claimed radius, then the temporal certificate is unsupported.

The remedy is estimator specific concentration or a weaker uncertainty statement, not reuse of a simple sample mean bound outside its scope.

</details>

---

## Broader scientific counterexamples

<details>
<summary><strong>Test 12: Nonneural and engineered counterexamples</strong></summary>

The physical candidate is deliberately tested outside the human brain domain because causal integration, recurrence, complexity, controllability, and temporal continuity can occur in systems for which an experiential interpretation cannot simply be assumed.

Priority counterexample classes include:

| Counterexample class | Scientific question |
| --- | --- |
| integrated nonneural biological network | Can a rich physical signature occur without the target experiential evidence? |
| recurrent artificial controller | Do recurrence and irreducibility overgenerate the candidate? |
| feedforward surrogate matched on passive behavior | Do interventions reveal a hidden causal difference? |
| simulator reproducing selected response statistics | Which physical causal properties survive simulation and which do not? |
| biological states with similar gross activity but different target evidence | Does the fuller candidate separate the states? |

These cases help prevent a circular rule in which any sufficiently complicated causal system is assigned the target experiential class by construction.

</details>

<details>
<summary><strong>Test 13: Composition</strong></summary>

Compare isolated systems, independent compositions, weakly coupled systems, strongly coupled systems, split systems, merged systems, and systems connected only through controlled communication channels.

The theory must predict whether physical signature and bridge classes remain separate, combine, become nonidentifiable, or undergo a defined structural transition.

Composition is a major structural frontier because a fixed dimensional temporal fingerprint does not by itself handle block birth, death, splitting, or merging.

</details>

<details>
<summary><strong>Test 14: Cross theory adversarial comparison</strong></summary>

IIT, GNWT, RPT, higher order approaches, predictive and neurorepresentational approaches, active inference, and the intervention resolved physical candidate can be represented through the common interface

\[
\mathfrak T_j=(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
\]

The aim is to identify protocols under which their predicted observable laws diverge, then use the experimental design layer to expose those differences efficiently.

See [Candidate Theory Families](candidate_theory_families.md).

</details>

<details>
<summary><strong>Test 15: Clinical and behavioral interfaces</strong></summary>

Future empirical work may compare bridge predictions across states in which report, responsiveness, memory, arousal, perturbational complexity, integration, temporal dynamics, and neural organization dissociate.

No single behavioral report, neural measure, or temporal continuation statistic is used as the definition of the target experiential class.

The purpose is to test whether a proposed bridge or signature explains convergent and divergent evidence across independently specified measurement models.

</details>

<details>
<summary><strong>Test 16: Falsification ledger standard</strong></summary>

Every major candidate should eventually receive a record with at least:

| Field | Required record |
| --- | --- |
| claim | Exact mathematical or empirical statement being tested |
| assumptions | Declared physical, statistical, temporal, and bridge assumptions |
| counterexample class | System family capable of defeating the claim |
| protocol | Admissible intervention and observation design |
| discriminant | Quantity whose sign, distance, or distribution separates hypotheses |
| uncertainty | Finite data confidence or error radius |
| outcome | Supported, rejected, unresolved, or nonidentifiable under the declared model |
| next test | Experiment or theorem needed to reduce the remaining ambiguity |

The strongest bridge result should survive this ledger rather than bypass it.

</details>

---

## The scientific reading rule

A failed test should be interpreted at the level where the failure occurred.

A failed descriptor does not prove that every physical description must fail.

A failed model does not identify the correct replacement.

Nonidentifiability does not mean a claim is false. It means the declared evidence cannot distinguish the alternatives.

Nonrejection does not mean a model is true.

The bridge from physical description to experience remains open unless it is separately justified.

## Where to continue

For the central bridge question, open the **[Bridge Problem](bridge_problem.md)**.

For the complete formal dependency chain, open the **[Theorem Roadmap](theorem_roadmap.md)**.

For individual theorem pages, use the **[Detailed Proposition Record](detailed_proposition_record.md)**.

For code, tests, and numerical audit, use the **[Reproducibility Guide](reproducibility.md)**.
