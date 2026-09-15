# Glossary and Reader Vocabulary

**Use this page as a reference, not as a chapter to read from top to bottom.**

The terms below describe how words are used inside this research program. When a proposition gives a more specific formal definition, that proposition controls the technical meaning.

If you are new to the project, begin with [Start Here](../START_HERE.md) or the [Research Map](research_map.md).

## Quick orientation

The vocabulary falls into four groups:

1. **Physical description:** what system and information are being represented.
2. **Target and bridge:** what distinction is being explained and what connects it to physics.
3. **Inference and model testing:** what can be identified, tested, rejected, or certified.
4. **Scientific status:** what a result does and does not justify.

## 1. Physical description

| Term | Meaning in this repository |
| --- | --- |
| **Physical realization** | A declared physical system together with the states, dynamics, interventions, observables, and other physical structure relevant to a test. |
| **Physical descriptor \(T\)** | The specific physical information claimed to be sufficient for a target distinction. A descriptor can be incomplete even when it is measured perfectly. |
| **Representation invariance** | The requirement that scientifically irrelevant changes of coordinates, units, labels, or encoding do not change the bridge relevant object. |
| **Operational structure** | Physical structure defined through declared interventions, responses, temporal relations, measurements, or other experimentally meaningful operations rather than arbitrary representation choices. |
| **Probability simplex** | The set of nonnegative probability vectors whose entries sum to one. Some later certificates preserve this coupling instead of treating probability cells independently. |
| **Projected event** | An event defined by fixing values for a nonempty subset of observed binary views and summing over the remaining views. |

## 2. Target and bridge

| Term | Meaning in this repository |
| --- | --- |
| **Target \(E\)** | An independently specified distinction that a proposed bridge claims the physical descriptor should determine. The target may be experiential in intended interpretation, but that interpretation must be justified independently. |
| **Latent target \(E^\star\)** | A target variable before an explicit target measurement channel is applied. A latent statistical variable is not automatically identified with consciousness. |
| **Observed target \(Y\)** | The measured report, response, label, or other observable used as evidence about a latent target. |
| **Bridge** | A declared relation or map connecting physical descriptions to target or experiential structure. The bridge from physical description to experience is the central open problem, not an assumption already solved by the repository. |
| **Factorization** | The mathematical statement that a target depends on the underlying state only through the declared descriptor. In the deterministic case, \(E=B\circ T\). |
| **Screening off** | The stochastic analogue of sufficiency. After conditioning on \(T\), the underlying state carries no additional information about the target under the declared model. |
| **Conditional information residual** | The quantity \(I(E;\Omega\mid T)\) used in P19 and later results to test stochastic screening off. A positive residual rejects sufficiency of the declared descriptor under the model. |
| **Target provenance** | The scientific origin of the target and the question of whether it was defined independently of the physical descriptor being tested. P71 shows why descriptor derived targets can make a sufficiency test circular. |
| **Nondifferential target channel** | The P72 condition that, given the latent target and physical descriptor, the observed target measurement does not retain an additional dependence on the underlying state. |
| **Physical to experiential bridge** | The unresolved scientific connection between a physical description and experiential structure. The repository develops mathematical, statistical, and experimental obligations for testing bridge claims but does not claim this connection has been derived. |

## 3. Identification, adequacy, and uncertainty

| Term | Meaning in this repository |
| --- | --- |
| **Identifiability** | The property that distinct parameter or theory values can be distinguished from the observable law under the declared assumptions. Identifiability is not the same as model adequacy. |
| **Just identified** | A model regime in which the observable information generically suffices to determine the model parameters but leaves no generic extra equality constraint for an independent adequacy test. |
| **Overidentification** | A regime with more observable constraints than are needed merely to recover parameters, creating testable restrictions that can falsify the model. |
| **Model adequacy** | Compatibility of the observed law with the full declared model, not merely successful parameter fitting. |
| **Model set separation** | A certified positive distance between an empirical confidence region and every distribution permitted by the declared model family. |
| **Nondegeneracy gate** | A condition that must be cleared before an unstable inversion is certified. P74 uses covariance intervals to refuse target channel recovery near the P73 singular set. |
| **Finite sample certificate** | A statement that remains valid with a declared probability or confidence level under an explicit sampling model. It is stronger than reporting a point estimate from finite data. |
| **Rejection** | A certificate that the declared model or sufficiency claim is incompatible with the data under the theorem assumptions and uncertainty control. |
| **Nonrejection** | Failure to obtain a rejection certificate. It is deliberately treated as inconclusive rather than validation or proof of truth. |

## 4. Certified computation

| Term | Meaning in this repository |
| --- | --- |
| **Certified lower bound** | A mathematically guaranteed quantity that cannot exceed the true target quantity. Later model separation results require a valid lower bound on model distance rather than only a numerical candidate fit. |
| **Certified upper bound** | A mathematically guaranteed quantity that cannot fall below the true target quantity. P79 uses this direction for the finite sample uncertainty radius. |
| **Branch and bound** | A global optimization method that partitions parameter space, computes rigorous bounds on each region, and refines regions until the desired global certificate is obtained. |
| **Exact rational arithmetic** | Computation using fractions rather than floating point approximations for the certification path, preserving the direction of inequalities used in the proof. |

## 5. Scientific status language

| Term | Meaning in this repository |
| --- | --- |
| **Scientific boundary** | An explicit statement of what a theorem does not establish. It prevents a valid mathematical result from being extended into an unsupported empirical or ontological claim. |
| **Theorem frontier** | The highest numbered proposition currently integrated into the documented public research program. The current public frontier is **P97**. |
| **Formal release** | The tagged software and publication release line. The current formal release remains **v0.82.0**, which is intentionally distinct from the theorem frontier. |

## Three distinctions worth remembering

### Identifiability is not adequacy

A model can have uniquely recoverable parameters and still be wrong. P73 addresses identifiability under a declared three view model. P75 adds another observed view so that the model itself can face independent restrictions.

### Mathematical validity is not empirical truth

A theorem can be completely correct under its assumptions even when those assumptions do not describe nature. This is why the repository keeps proofs, empirical inputs, modeling assumptions, and open hypotheses visibly separate.

### Physical completeness is not experiential completeness

A physical description may be complete relative to a declared physical experiment without thereby supplying an experiential interpretation. This distinction is especially important in the quantum branch: tomographic or operational physical completeness does not eliminate the need for an independently justified bridge principle.

## Where to continue

For the central question, open the **[Bridge Problem](bridge_problem.md)**.

For the scientific story, open the **[Research Map](research_map.md)**.

For the formal dependency structure, open the **[Theorem Roadmap](theorem_roadmap.md)**.

For model failure logic, open the **[Falsification Program](falsification_program.md)**.

For equations and source roles, open the **[Equation and Citation Map](equation_and_citation_map.md)**.

For the complete technical record, open **[Research Navigation](research_navigation.md)**.

## Historical IID theorem frontier: P93

P93 is the historical IID finite-sample predecessor of P94. P92 remains the exact population-distance theorem at `d_inf(P_emp, M75) = 1/24`; P93 adds the localized seven-cell IID rejection handoff. P94 then extends that handoff to declared finite-range temporal dependence under one common marginal law. None of these frontier labels identifies consciousness or closes the physical-to-experiential bridge.


## Historical finite-range predecessor: P94

**Finite-range dependence:** observations may depend across nearby time indices but sigma-fields separated by more than a declared range `m` are independent. P94 uses residue classes modulo `m+1` to recover independent groups.

**Common marginal law:** every observation has the same four-view population law. P94 requires this because an exact counterexample shows that pooling different valid P75 regimes can create a negative P92 determinant product.


## Immediate predecessor theorem frontier: P95

**Predeclared regime:** a time or experimental block whose boundary is fixed independently of the selected sign-coherence witness. P95 tests such regimes separately instead of pooling drifting marginal laws.

**Familywise regime certificate:** each regime receives its own P94-style finite-range confidence event and error budget `alpha_b`. If the budgets satisfy `sum_b alpha_b <= alpha`, a union bound provides simultaneous confidence at least `1-alpha` without requiring independence between regimes.

**P95 boundary:** data-dependent segmentation, unrestricted gradual drift inside a regime, model acceptance under non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.


## Immediate predecessor theorem frontier: P96

**Pilot-selection information:** the information used to choose a finite regime plan before certification. P96 permits this selection rule to be arbitrarily complicated under its declared sample-separation assumptions.

**Frozen plan:** the selected number of regimes, regime definitions, declared dependence ranges, rational error budgets, and certification allocation are fixed before holdout statistics are inspected.

**Independent holdout certification:** certification information is independent of the pilot-selection information in the sense required by the conditional P96 theorem. An ordinary random split of one temporally dependent stream is not automatically such an independent holdout design.

**Selection-complexity alpha penalty:** under the P96 independent-holdout and frozen-plan assumptions, the pilot search itself requires no additional alpha spending. The cost is sample separation: pilot observations are not certification observations.

**P96 boundary:** same-data redesign, unrestricted within-regime drift, model acceptance under non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.


## Current theorem frontier: P97

**Finite candidate family:** a complete list of candidate regime plans fixed before the certification statistics are inspected. P97 permits post-inspection selection only from this predeclared finite family.

**Candidate-level error budget:** the exact rational failure budget assigned to one candidate plan. Inside that candidate, P95 divides or otherwise allocates the candidate budget across its regimes.

**Simultaneous candidate certificate:** the event on which every candidate-specific P95 certificate is valid at once. P97 obtains it by a union bound across candidates, so the candidate certificates may reuse the same observations and may be statistically dependent.

**Same-data selection cost:** unlike P96, P97 does not require a separate pilot sample. It pays instead through multiplicity: the global error budget is split across the predeclared candidates.

**P97 boundary:** a candidate created after inspecting certification results is outside the theorem. Unbounded post-inspection search, unrestricted within-regime drift, model acceptance under non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.
