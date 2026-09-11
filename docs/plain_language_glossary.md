# Plain-Language Glossary

This glossary is written for readers who want to follow the scientific logic of the **Mathematical Consciousness Bridge** without already being specialists in mathematical physics, information theory, statistics, or latent-variable modeling.

The definitions below are intentionally plain first and technical second.

---

## Admissible state or history, \(\Omega\)

**Plain language:** the collection of physical situations the study allows as possible.

A point \(\omega\in\Omega\) can represent a physical state, a trajectory through time, an experimental condition, or another declared physical object.

The repository does not assume that \(\Omega\) is already a complete description of all physics. It must be declared for each problem.

---

## Physical descriptor, \(T\)

**Plain language:** the physical information we choose to use when testing a bridge claim.

Formally,

\[
T:\Omega\to\mathcal T.
\]

The descriptor might contain measurements, causal response structure, time-dependent behavior, a quantum state, a coarse-grained representation, or another operational physical summary.

A central question of the repository is whether the declared descriptor has preserved every distinction that matters for the declared target.

---

## Target, \(E\)

**Plain language:** the distinction the physical descriptor is supposed to explain.

Formally,

\[
E:\Omega\to\mathcal E.
\]

For the bridge problem, the target is intended to represent an independently justified experiential distinction. The target cannot simply be manufactured from the same descriptor being tested and then used as evidence that the descriptor explains it. P71 formalizes this non-circularity requirement.

---

## Bridge, \(B\)

**Plain language:** a rule that maps the physical descriptor to the target.

A deterministic bridge has the form

\[
E=B\circ T.
\]

This means that once \(T\) is known, the target \(E\) is determined by a rule acting only on \(T\).

The repository studies when such factorization exists, when it fails, and what finite data can legitimately tell us about it.

---

## Factorization

**Plain language:** the target can be computed from the chosen descriptor alone.

The equation

\[
E=B\circ T
\]

is called a factorization of \(E\) through \(T\).

Factorization is not automatically evidence of a scientifically meaningful bridge. If the target itself was created as \(E=h(T)\), factorization is guaranteed by construction. That is the circularity problem addressed by P71.

---

## Fiber of a descriptor

**Plain language:** all physical situations that the chosen descriptor treats as the same.

For a descriptor value \(t\), the fiber is

\[
T^{-1}(t)=\{\omega\in\Omega:T(\omega)=t\}.
\]

If a deterministic bridge exists, the target must be constant on each fiber.

---

## Collision

**Plain language:** two situations look identical to the chosen physical descriptor but different to the target.

A collision has

\[
T(\omega_1)=T(\omega_2)
\quad\text{and}\quad
E(\omega_1)\neq E(\omega_2).
\]

Such a collision disproves exact sufficiency of the declared descriptor for the declared target.

It does not, by itself, prove that the target is nonphysical. The descriptor may simply be incomplete or too coarse.

---

## Sufficiency

**Plain language:** the chosen physical description contains enough information for the declared target under the declared bridge class.

Exact deterministic sufficiency means that \(E\) factors through \(T\).

Stochastic sufficiency means that, under the declared probabilistic model, the target contains no additional information about the underlying state once \(T\) is known.

---

## Conditional mutual information, \(I(E;\Omega\mid T)\)

**Plain language:** how much information about the underlying situation remains in the target after the descriptor is already known.

The repository uses

\[
R_{\mathrm{stoch}}(T)=I(E;\Omega\mid T)
\]

as a stochastic residual.

A positive residual means that the target still distinguishes aspects of the underlying situation that were not screened off by the descriptor, under the declared probabilistic model.

A zero residual alone does not prove a scientifically meaningful bridge. Target circularity, measurement design, or model assumptions can force it to zero.

---

## Residual

**Plain language:** what the target still tells us after the chosen physical descriptor has done all the explaining it can.

In the stochastic bridge problem, the main residual is conditional mutual information.

Residuals are useful because they turn vague claims of "missing information" into measurable mathematical quantities.

---

## Descriptor refinement

**Plain language:** adding more physical information to the descriptor.

If \(T_f\) is a finer descriptor and \(T_c\) is a coarser one, then often

\[
T_c=c\circ T_f.
\]

P21 quantifies how much stochastic residual can disappear when the descriptor is refined.

This helps distinguish "the bridge failed" from "the physical description was too coarse."

---

## Representation invariance

**Plain language:** the scientific conclusion should not change just because the same physical system was written in different coordinates or notation.

A valid bridge object should track physical content rather than arbitrary representation choices.

This is one of the foundational concerns of P1-P10.

---

## Intervention

**Plain language:** actively changing part of a system to learn how other parts respond.

Interventions are stronger than passive correlations because they help reveal causal response structure.

P11 and later propositions use intervention-resolved structure as part of a richer physical descriptor.

---

## Coarse-graining

**Plain language:** replacing a detailed physical description with a simpler one.

Examples include grouping states, combining variables, aggregating nodes, or using a lower-resolution scale.

Coarse-graining can destroy distinctions. P17-P18 and P25-P37 study when important structure survives such compression.

---

## Operational quotient

**Plain language:** a principled way of grouping physical situations that are indistinguishable under a declared class of operations or observations.

The repository uses quotient constructions to distinguish genuine physical equivalence from arbitrary data compression.

---

## Latent variable

**Plain language:** a variable included in a statistical model even though it is not observed directly.

In P73-P79, a binary latent variable is used to study target-measurement reliability under explicit assumptions.

The repository does **not** identify that latent variable with consciousness. It is a methodological object in a measurement model.

---

## Target-measurement channel

**Plain language:** the process by which an underlying target becomes an observed report, label, behavioral response, rating, or other measurement.

If \(E^\star\) is an underlying target and \(Y\) is what is observed, the measurement channel describes how \(Y\) depends on \(E^\star\).

P72 shows that measurement noise can attenuate or erase a real target distinction.

---

## Conditional independence

**Plain language:** once a specified variable is known, two other variables no longer carry additional dependence under the model.

For example, a multi-view latent model may assume that several measurements are independent once the latent state is fixed.

This is an assumption that can be scientifically wrong. The repository treats it as a model condition, not a fact about consciousness.

---

## Identifiability

**Plain language:** whether the hidden parameters of a model can, in principle, be recovered uniquely from the observable distribution, up to explicitly described symmetries.

P73 shows a restricted three-view binary target-channel model can be identifiable under nondegeneracy conditions, up to a common latent-label swap.

Identifiability is not the same as model truth.

---

## Nondegeneracy

**Plain language:** the model is not sitting on a special boundary where the parameters become impossible or unstable to recover.

Examples include zero covariance, identical channels, or a latent state with vanishing prevalence.

P74 includes a nondegeneracy gate so the method refuses to make unstable claims near such boundaries.

---

## Overidentification

**Plain language:** the data contain more independent observable constraints than are needed merely to fit the model parameters.

This creates the possibility of testing whether the model is adequate rather than only estimating its parameters.

P75 uses a fourth binary view to create overidentifying restrictions for the target-measurement model.

---

## Model adequacy

**Plain language:** whether the observed data are compatible with the full mathematical structure imposed by the declared model.

A model can be identifiable and still be wrong.

P75-P77 distinguish fitting parameters from testing adequacy.

---

## Confidence region

**Plain language:** a set of population distributions that remain statistically compatible with the observed data at a declared confidence level.

P77 asks whether this entire region intersects the declared model family.

If the regions are disjoint, the model can be rejected under the theorem's assumptions.

---

## Model family

**Plain language:** all observable distributions allowed by a declared statistical model as its parameters vary.

The P75 four-view latent model is a continuous family generated by nine parameters.

Testing only a few parameter values is not the same as testing the entire model family.

---

## Global lower bound

**Plain language:** a number that is guaranteed not to exceed the best possible value over the entire allowed search space.

For P78, the relevant quantity is the distance from the empirical law to the complete continuous model family.

A valid global lower bound is essential for certified rejection.

A local optimizer value generally gives the opposite kind of information: an upper bound obtained from one explicit candidate.

---

## Upper bound from a candidate

**Plain language:** if you exhibit one allowed model with a certain error, the true best possible error cannot be worse than that candidate's error.

Therefore a candidate model supplies an **upper bound** on the minimum distance to the model family.

P78 uses both lower and upper bounds but keeps their logical roles separate.

---

## Branch-and-bound

**Plain language:** a global optimization method that divides the parameter space into smaller regions, computes rigorous bounds for each region, and repeatedly refines the regions that matter most.

P78 uses this idea with exact rational arithmetic and multi-affine structure to bound the distance to the continuous P75 family.

---

## Multi-affine function

**Plain language:** a function that is affine in each parameter separately when all the other parameters are held fixed.

This structure allows exact coordinatewise extrema on a parameter box to be determined from its endpoints.

P78 exploits this property of the P75 cell probabilities.

---

## Exact rational arithmetic

**Plain language:** calculations performed with exact fractions rather than ordinary floating-point approximations.

P78 uses Python `Fraction` arithmetic for empirical count laws, dyadic box boundaries, and optimization bounds.

This prevents a formal global certificate from depending on hidden floating-point rounding.

---

## Certified rejection

**Plain language:** the mathematical and statistical assumptions are strong enough to prove that the declared model cannot lie inside the current confidence region.

For the P77-P79 L-infinity interface, rejection follows when a certified lower bound on model distance exceeds a certified upper bound on the sampling radius.

---

## Non-rejection

**Plain language:** the test did not establish rejection.

This may happen because the model is compatible with the data, because the sample is too small, because the computational bound is still too loose, or for other reasons.

Non-rejection is not model acceptance.

---

## Certified non-separation

**Plain language:** we can rigorously show that the current confidence region intersects the declared model family.

P79 distinguishes this from mere computational uncertainty.

For the compact P75 family, a sufficiently small certified upper bound on model distance proves that at least one model law lies inside the P77 confidence ball.

This is still not model acceptance. It is a statement about what the current test can or cannot reject.

---

## Unresolved computation

**Plain language:** the current certified lower and upper bounds are still too wide to determine which side of the statistical decision boundary the exact answer lies on.

P79 makes this a separate status rather than confusing it with non-rejection or compatibility.

---

## Falsification

**Plain language:** specifying in advance what observation or certified result would count against a claim.

The repository treats falsification as part of the architecture, not as an optional philosophical add-on.

See the [Falsification Program](falsification_program.md).

---

## Bridge regularity class

**Plain language:** a declared restriction on what kinds of bridge functions are considered admissible.

On a finite sampled set, an unrestricted lookup table can always fit an injective descriptor. Therefore claims about continuous non-factorization require a declared regularity or structural class for the bridge.

This limitation is made explicit in P40 and related quantum bridge results.

---

## Quantum operational description

**Plain language:** a quantum-mechanical description used to predict the outcomes of declared physical measurements.

For state \(\rho\) and measurement operators \(M_a\),

\[
p(a\mid M)=\operatorname{Tr}(\rho M_a).
\]

This predicts physical measurement probabilities. It does not, by itself, define a map from quantum state to experience.

---

## Scientific boundary

**Plain language:** an explicit statement of what a theorem or computation does **not** establish.

Major documents in this repository include boundaries because mathematical correctness inside a model is not the same as empirical validation, ontology, or a completed consciousness theory.

---

# The most important distinctions to remember

| Do not confuse | With |
| --- | --- |
| correlation | physical sufficiency |
| factorization by construction | independent bridge evidence |
| an observed target | a perfectly measured latent target |
| identifiability | model adequacy |
| model adequacy | ontological truth |
| a local best fit | certified global separation |
| non-rejection | model acceptance |
| certified non-separation | proof that the model is true |
| failure of one physical descriptor | failure of physics |
| a quantum physical description | a theory of experience |
| a theorem under assumptions | an empirical discovery |

---

# One practical reading rule

Whenever you see an equation in this repository, ask:

> What was assumed, what exactly was proved, and what stronger interpretation is explicitly *not* justified?

That question captures the scientific discipline of the project better than memorizing every symbol.
