# P71 Equation and Citation Provenance Map

This page is the equation-level provenance record for [Proposition 71: Target-Provenance Non-Circularity and Descriptor-Derived Target Vacuity](proposition_71_target_provenance_noncircularity.md).

P71 extends the P19 bridge-test architecture by formalizing a necessary condition on **target construction**. It does not define consciousness, prove physicalism or nonphysicalism, or establish that any particular target is a valid measure of experience.

## Provenance table

| Equation or object | Role in P71 | Status | Primary provenance |
| --- | --- | --- | --- |
| \(E_h=h\circ T\) | deterministic descriptor-derived target | definition | P71 construction |
| \(T(\omega_1)=T(\omega_2)\Rightarrow E_h(\omega_1)=E_h(\omega_2)\) | shows constancy of a descriptor-derived target on every physical fiber | proved directly from the definition | P71A |
| \(H(E_h\mid T)=0\) | deterministic-target conditional entropy identity | standard information-theoretic consequence of functional dependence | Shannon information theory; P71 specialization |
| \(I(E_h;\Omega\mid T)=0\) | stochastic P19 residual for a deterministic descriptor-derived target | proved from functional dependence | P19 plus P71A |
| \(P(\omega,t,e)=P(\omega,t)K(e\mid t)\) | descriptor-only stochastic target channel | definition of the P71B construction | P71B |
| \(E\perp\!\!\!\perp\Omega\mid T\) | Markov screening-off induced by the descriptor-only channel | standard conditional-independence consequence | finite probability theory; P71B specialization |
| \(I(E;\Omega\mid T)=0\) | conditional-information form of the same screening-off statement | standard finite-alphabet equivalence used by P19 | information theory; P19 and P71B |
| \(\widehat E=h_D(T)\) | learned target after freezing a training artifact \(D\) | definition | P71C |
| \(I(\widehat E;\Omega\mid T,D)=0\) | learned-target conditional vacuity | proved by conditioning on the fixed learned rule | P71C |
| \(D\perp\!\!\!\perp\Omega\mid T\Rightarrow I(\widehat E;\Omega\mid T)=0\) | sufficient condition for unconditional descriptor-only screening-off after averaging over the training artifact | proved by marginalizing over \(D\) | P71C |
| \(K(e\mid t)=P(E=e\mid T=t)\) | reconstructs a descriptor-only target channel from any observed zero-residual law | definition under the P71D premise | P71D |
| \(I(E;\Omega\mid T)=0\Rightarrow P(\omega,t,e)=P(\omega,t)K(e\mid t)\) | provenance non-identifiability result | proved from conditional independence | P71D |
| \(T(\Omega)=\Omega\bmod2\) | finite synthetic physical descriptor | synthetic example | P71 numerical illustration |
| \(E_{\rm circ}=T\) | finite descriptor-derived target | synthetic construction | P71 numerical illustration |
| \(E_{\rm ext}=\mathbf1\{\Omega\ge2\}\) | separately declared synthetic target | synthetic construction, not an experiential variable | P71 numerical illustration |
| \(I(E_{\rm ext};\Omega\mid T)=\log2\approx0.6931\) nats | exact finite residual in the synthetic collision example | analytically derived and numerically regression-tested | P71 synthetic example |

## External methodological context

P71's theorem is proved directly from factorization and conditional-independence identities. External literature is used only to position the scientific motivation.

1. N. Kriegeskorte, W. K. Simmons, P. S. F. Bellgowan, and C. I. Baker, "Circular analysis in systems neuroscience: the dangers of double dipping," *Nature Neuroscience* 12 (2009), 535-540. DOI: 10.1038/nn.2303. This source motivates the broader importance of independence in analysis design. P71 addresses a different structural question: even a statistically held-out target can remain descriptor-derived if its test-time value is computed only from the tested descriptor.
2. C. Koch, M. Massimini, M. Boly, and G. Tononi, "Neural correlates of consciousness: progress and problems," *Nature Reviews Neuroscience* 17 (2016), 307-321. DOI: 10.1038/nrn.2016.22. This source provides consciousness-measurement context for separating correlates, prerequisites, and consequences. P71 does not adopt any one neural correlate as the experiential target.
3. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal* 27 (1948), 379-423 and 623-656. DOI: 10.1002/j.1538-7305.1948.tb01338.x. This is foundational background for entropy and mutual information.
4. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006. DOI: 10.1002/047174882X. This is standard background for conditional mutual information and conditional independence on finite probability spaces.

## What is repository-original here

The basic identities involving functional dependence, Markov screening-off, and conditional mutual information are standard mathematics. The repository-specific contribution is their assembly into the P19 physical-to-experiential test architecture as an explicit **target-provenance non-circularity theorem**, together with:

- the deterministic bridge-vacuity statement for targets defined as \(h(T)\);
- the descriptor-only stochastic target-channel formulation;
- the learned-target corollary distinguishing held-out generalization from independent target provenance;
- the provenance non-identifiability result showing that zero observed P19 residual is compatible with a descriptor-derived target-generation channel;
- the explicit protocol rule that target provenance must be declared outside the observed joint-law statistic;
- the executable finite reference constructions and synthetic residual witness.

This wording intentionally does not claim that the underlying information-theoretic identities are novel.

## Scientific boundary

The P71 result proves that some apparently successful bridge tests are **vacuous by construction**. It does not prove that a separately declared target is genuinely experiential. That remaining problem requires a target-side measurement theory with reliability, validity, uncertainty, and falsification conditions that do not collapse back into the physical descriptor by definition.
