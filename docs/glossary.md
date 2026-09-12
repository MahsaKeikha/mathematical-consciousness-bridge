# Glossary and Reader Vocabulary

This glossary gives the repository's intended meaning for recurring terms. It is written for readers who may be entering from physics, mathematics, neuroscience, statistics, philosophy of mind, or software engineering and may not share the same default vocabulary.

The definitions below are **local to this research program unless explicitly identified as standard mathematical terminology**. A term's use in a proposition is controlled by that proposition's formal definitions.

| Term | Meaning in this repository |
| --- | --- |
| **Physical realization** | A declared physical system together with the states, dynamics, interventions, observables, and other physical structure relevant to a test. |
| **Physical descriptor \(T\)** | The specific physical information claimed to be sufficient for a target distinction. A descriptor can be incomplete even when it is measured perfectly. |
| **Target \(E\)** | An independently specified distinction that a proposed bridge claims the physical descriptor should determine. The target may be experiential in intended interpretation, but that interpretation must be justified independently. |
| **Latent target \(E^\star\)** | A target variable before an explicit target-measurement channel is applied. A latent statistical variable is not automatically identified with consciousness. |
| **Observed target \(Y\)** | The measured report, response, label, or other observable used as evidence about a latent target. |
| **Bridge** | A declared relation or map connecting physical descriptions to target or experiential structure. The physical-to-experiential bridge is the central open problem, not an assumption already solved by the repository. |
| **Factorization** | The mathematical statement that a target depends on the underlying state only through the declared descriptor; in the deterministic case, \(E=B\circ T\). |
| **Screening off** | The stochastic analogue of sufficiency: after conditioning on \(T\), the underlying state carries no additional information about the target under the declared model. |
| **Conditional-information residual** | The quantity \(I(E;\Omega\mid T)\) used in P19 and later results to test stochastic screening-off. A positive residual rejects sufficiency of the declared descriptor under the model. |
| **Representation invariance** | The requirement that scientifically irrelevant changes of coordinates, units, labels, or encoding do not change the bridge-relevant object. |
| **Operational structure** | Physical structure defined through declared interventions, responses, temporal relations, measurements, or other experimentally meaningful operations rather than through arbitrary representation choices. |
| **Identifiability** | The property that distinct parameter or theory values can be distinguished from the observable law under the declared assumptions. Identifiability is not the same as model adequacy. |
| **Just-identified** | A model regime in which the observable information generically suffices to determine the model parameters but leaves no generic extra equality constraint for an independent adequacy test. |
| **Overidentification** | A regime with more observable constraints than are needed merely to recover parameters, creating testable restrictions that can falsify the model. |
| **Model adequacy** | Compatibility of the observed law with the full declared model, not merely successful parameter fitting. |
| **Model-set separation** | A certified positive distance between an empirical confidence region and every distribution permitted by the declared model family. |
| **Certified lower bound** | A mathematically guaranteed quantity that cannot exceed the true target quantity. In P77-P81, rejection of a continuous model family requires a valid lower bound on model distance, not merely a numerical candidate fit. |
| **Certified upper bound** | A mathematically guaranteed quantity that cannot fall below the true target quantity. P79 uses this direction for the finite-sample uncertainty radius. |
| **Branch-and-bound** | A global optimization method that partitions parameter space, computes rigorous bounds on each region, and refines regions until the desired global certificate is obtained. P78-P81 use exact-rational variants for the P75 family. |
| **Exact rational arithmetic** | Computation using fractions rather than floating-point approximations for the certification path, preserving the direction of inequalities used in the proof. |
| **Probability simplex** | The set of nonnegative probability vectors whose entries sum to one. P80 retains this coupling inside the box relaxation rather than treating probability cells independently. |
| **Projected event** | An event defined by fixing values for a nonempty subset of the observed binary views and summing over the remaining views. P81 uses exact parameter-box ranges for these events. |
| **Target provenance** | The scientific origin of the target and the question of whether it was defined independently of the physical descriptor being tested. P71 shows why descriptor-derived targets can make a sufficiency test circular. |
| **Nondifferential target channel** | The P72 condition that, given the latent target and physical descriptor, the observed target measurement does not retain an additional dependence on the underlying state. |
| **Nondegeneracy gate** | A condition that must be cleared before an unstable inversion is certified. P74 uses covariance intervals to refuse target-channel recovery near the P73 singular set. |
| **Finite-sample certificate** | A statement that remains valid with a declared probability or confidence level under an explicit sampling model. It is stronger than reporting a point estimate from finite data. |
| **Rejection** | A certificate that the declared model or sufficiency claim is incompatible with the data under the theorem's assumptions and uncertainty control. |
| **Non-rejection** | Failure to obtain a rejection certificate. It is deliberately treated as inconclusive rather than as validation or proof of truth. |
| **Scientific boundary** | An explicit statement of what a theorem does **not** establish, included to prevent a valid mathematical result from being extended into an unsupported empirical or ontological claim. |
| **Theorem frontier** | The highest-numbered proposition currently integrated into the documented research program. At version 0.81.0 the frontier is P81. |
| **Physical-to-experiential bridge** | The unresolved scientific connection between complete physical description and experiential structure. The repository builds necessary mathematical, statistical, and experimental obligations for testing bridge claims but does not claim this connection has been derived. |

## Three distinctions that matter throughout the repository

### Identifiability is not adequacy

A model can have uniquely recoverable parameters and still be wrong. P73 addresses identifiability under a declared three-view model; P75 introduces additional views precisely so that the model itself can face independent restrictions.

### Mathematical validity is not empirical truth

A theorem can be completely correct under its assumptions even when those assumptions do not describe nature. This is why the repository keeps proofs, empirical inputs, modeling assumptions, and open hypotheses visibly separate.

### Physical completeness is not experiential completeness

A physical description may be complete relative to a declared physical experiment without thereby supplying an experiential interpretation. This distinction is especially important in the quantum branch: tomographic or operational physical completeness does not eliminate the need for an independently justified bridge principle.

## Suggested companion pages

- [Start Here](../START_HERE.md)
- [Bridge Problem](bridge_problem.md)
- [Theorem Roadmap](theorem_roadmap.md)
- [Research Navigation](research_navigation.md)
- [Equation and Citation Map](equation_and_citation_map.md)
- [Falsification Program](falsification_program.md)
