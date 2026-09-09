# Proposition 11: intervention-resolved causal structure

## Candidate A - a physical signature to be tested, not assumed

The preceding propositions establish what a scientifically useful consciousness bridge must eventually accomplish. They do not by themselves supply the physical signature that would make such a bridge valid.

Proposition 11 introduces the first original candidate physical object in this repository:

\[
\boxed{
\text{intervention-resolved causal structure}.
}
\]

The construction combines three complementary features of controlled physical response:

1. how strongly different interventions separate the whole-system response distribution;
2. how perturbational influence propagates from one physical block to another;
3. how strongly the joint response resists factorization across physical partitions.

The construction is motivated by perturbational-complexity experiments, causal-structure theories, recurrent and workspace models, synergistic-information results, and anesthesia-related integration/controllability studies. None of those sources is treated as independently establishing the physical-to-experiential bridge.

The mathematical question is:

> Can a sufficiently rich structure of controlled causal responses provide a representation-invariant physical signature whose equivalence classes can be tested against candidate experiential equivalence classes?

That question remains open. Proposition 11 constructs the physical object and proves its initial invariance and structural certificates.

---

# 1. Physical domain and admissible perturbations

Let

\[
p\in\mathcal Q_P
\]

be a physical system already quotiented by physically irrelevant representation choices as required by Proposition 1.

Let the candidate physical subsystem be divided into blocks

\[
V=\{1,\ldots,m\}.
\]

Let

\[
\mathcal U_p
\]

be a declared set of physically admissible interventions, and let

\[
\mathcal T=\{\tau_1,\ldots,\tau_L\}
\]

be a set of post-intervention delays.

For intervention \(u\in\mathcal U_p\) and delay \(\tau\in\mathcal T\), define the joint response law

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L\!\left(Y_{t+\tau}^V\mid do(u),p\right).
}
\]

The \(do(u)\) notation denotes controlled intervention semantics rather than passive observational association.

---

# 2. Response geometry

For two admissible interventions \(u,v\in\mathcal U_p\), define

\[
\boxed{
d_p^\tau(u,v)
=
\left\|P_p^{u,\tau}-P_p^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

For fixed \(\tau\), this is a pseudometric on the intervention set whenever distinct interventions may induce identical response laws.

The family

\[
\boxed{
\mathcal G_p
=
\{d_p^\tau:\tau\in\mathcal T\}
}
\]

is the intervention-response geometry.

It records which interventions produce similar or different responses and how that geometry evolves with physical time.

A derived diameter is

\[
\operatorname{Diam}_p(\tau)
=
\sup_{u,v\in\mathcal U_p}d_p^\tau(u,v).
\]

This is a differentiation diagnostic, not a consciousness criterion.

---

# 3. Directed interventional influence

Let \(P_{p,j}^{u,\tau}\) be the marginal response law on block \(j\).

For source block \(i\), let

\[
\mathcal E_i
\subseteq
\mathcal U_p\times\mathcal U_p
\]

contain intervention pairs differing only in the controlled value of source block \(i\), with all other externally fixed intervention components matched.

Define

\[
\boxed{
A_{ij}^{p}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\left\|
P_{p,j}^{u,\tau}
-
P_{p,j}^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The tensor

\[
\boxed{
\mathcal A_p
=
\{A_{ij}^{p}(\tau)\}_{i,j,\tau}
}
\]

records strength, direction, and timing of perturbational influence among physical blocks.

Define the aggregated directed graph by

\[
i\to j
\quad\Longleftrightarrow\quad
\sup_{\tau\in\mathcal T}A_{ij}^{p}(\tau)>0,
\qquad i\ne j.
\]

A directed cycle is therefore a structural certificate of a causal return path under the declared interventions.

---

# 4. Partition response irreducibility

For a nontrivial partition

\[
\pi=\{B_1,\ldots,B_k\}
\]

of the physical blocks, define the productized partition model

\[
\boxed{
P_{p,\pi}^{u,\tau}
=
\bigotimes_{r=1}^{k}P_{p,B_r}^{u,\tau}.
}
\]

The partition response irreducibility is

\[
\boxed{
\kappa_p^\tau(\pi)
=
\sup_{u\in\mathcal U_p}
\left\|
P_p^{u,\tau}
-
P_{p,\pi}^{u,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The complete partition landscape is

\[
\boxed{
\mathcal K_p
=
\left\{
\kappa_p^\tau(\pi)
:
\pi\in\mathfrak P(V),\ \tau\in\mathcal T
\right\}.
}
\]

A convenient derived scalar is

\[
\kappa_p^*
=
\inf_{\pi\in\mathfrak P_{\mathrm{nt}}(V)}
\sup_{\tau\in\mathcal T}
\kappa_p^\tau(\pi).
\]

This measures failure of the observed intervention-conditioned response law to factor into productized block marginals. It is not identified with any external theory's integrated-information quantity.

---

# 5. Full causal-structure candidate

Define the raw physical object

\[
\boxed{
\mathfrak C_p
=
\left(
V,
\mathcal U_p,
\mathcal T,
\mathcal G_p,
\mathcal A_p,
\mathcal K_p
\right).
}
\]

Physical labels themselves are not intended to matter. Let \(\cong\) identify two such objects whenever compatible bijections of block labels, intervention labels, outcome coordinates, and declared delays transport every response law into the corresponding response law.

The representation-independent candidate signature is

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

This is a structured signature rather than a scalar threshold.

The strongest long-term completeness target would be

\[
\boxed{
F_{\mathrm{causal}}(p)
=
F_{\mathrm{causal}}(p')
\iff
C_B(p)=C_B(p').
}
\]

Nothing in Proposition 11 assumes this biconditional.

---

# 6. Proposition 11A - invariance under compatible physical reparameterization

Suppose two physical descriptions \(p,p'\) are related by:

1. a bijection of physical block labels;
2. a bijection of admissible intervention labels preserving manipulated blocks;
3. a measurable bijection \(h\) of response space satisfying

\[
P_{p'}^{\phi(u),\tau}
=
h_\#P_p^{u,\tau};
\]

4. preservation of declared physical delays.

Then

\[
\boxed{
F_{\mathrm{causal}}(p)
=
F_{\mathrm{causal}}(p').
}
\]

## Proof

Total variation is invariant under measurable bijective pushforward:

\[
\|h_\#P-h_\#Q\|_{\mathrm{TV}}
=
\|P-Q\|_{\mathrm{TV}}.
\]

Therefore all response-geometry distances are preserved. Compatible relabeling commutes with marginalization, so the directed influence tensor is preserved up to block permutation. Product measures transform to product measures under component-wise bijections, so every partition irreducibility value is likewise preserved. Hence the full physical objects are isomorphic and determine the same quotient signature.

\[
\boxed{\mathrm{QED}}
\]

---

# 7. Proposition 11B - exact partition-factorization certificate

For any fixed nontrivial partition \(\pi\) and delay \(\tau\),

\[
\boxed{
\kappa_p^\tau(\pi)=0
\iff
P_p^{u,\tau}
=
\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
\quad\forall u\in\mathcal U_p.
}
\]

## Proof

Total-variation distance is zero if and only if the two probability measures are equal. Since every term in the supremum is nonnegative, the supremum is zero if and only if every intervention-specific distance is zero.

\[
\boxed{\mathrm{QED}}
\]

---

# 8. Proposition 11C - feedforward no-return certificate

If the aggregated directed influence graph is acyclic, then no sequence of positive directed interventional influences can return from a physical block to itself through distinct intermediate blocks.

Equivalently, if a causal return path exists, the aggregated graph contains a directed cycle.

This is a graph-theoretic structural certificate. It does not convert recurrence into an experiential conclusion.

---

# 9. Immediate counterexample discipline

The causal-structure candidate is exposed to failure from the beginning.

Priority counterexample classes include:

| Counterexample class | Scientific question |
| --- | --- |
| highly integrated non-neural biological network | can the same physical structure occur without the target experiential evidence? |
| recurrent artificial controller | do recurrence and irreducibility overgenerate the candidate? |
| feedforward surrogate matched on passive output | do controlled interventions expose a hidden causal difference? |
| conscious/unconscious biological pair with similar gross activity | does the full physical structure separate the states? |

This program is necessary because integration, feedback, controllability, and rich causal organization occur outside systems for which consciousness can simply be presumed.

---

# 10. Relation to existing theories and measures

| External framework | What motivates the candidate | What is not assumed |
| --- | --- | --- |
| PCI / TMS-EEG | controlled perturbation and differentiated spatiotemporal response | that one perturbational-complexity scalar is the bridge |
| IIT | intrinsic causal organization and irreducibility | IIT's constitutive identity or postulates |
| GNWT | distributed recurrent influence and large-scale availability | that broadcasting alone is sufficient |
| RPT | recurrent processing | that recurrence alone is sufficient |
| synergistic-workspace results | distributed integration and synergy | that synergy alone is sufficient |
| predictive / neurorepresentational approaches | structured state-dependent dynamics | a specific generative-model semantics |

The candidate is therefore best understood as a theory-comparison substrate: a rich physical object against which different bridge proposals can be expressed and tested.

---

# 11. Empirical program

A biological implementation would require a declared perturbation-response protocol:

1. identify or certify the candidate physical subsystem;
2. apply localized interventions at multiple locations and strengths;
3. record multichannel responses across a declared physical-time grid;
4. estimate intervention-conditioned joint response laws;
5. construct \(d_p^\tau\), \(A_{ij}^{p}(\tau)\), and \(\kappa_p^\tau(\pi)\);
6. retain protocols that improve between-signature discrimination more than within-signature nuisance variation;
7. propagate finite-data uncertainty using Propositions 8-10;
8. test the candidate across conscious/unconscious transitions and non-conscious counterexample systems.

TMS-EEG is one possible human implementation, but the mathematical structure is substrate independent when the intervention semantics are physically justified.

---

# 12. What Proposition 11 establishes

**Proved:**

- a precise intervention-resolved causal-response structure;
- representation invariance under compatible bijective reparameterization;
- an exact partition-factorization certificate;
- a feedforward no-return certificate;
- a structured physical signature suitable for the P5-P10 falsification and recovery framework.

**Open:**

- whether the candidate is sufficient for any experiential bridge;
- whether it is complete for any formally justified experiential equivalence relation;
- whether a particular region of its physical state space corresponds to consciousness;
- whether current experiments can recover the required structure with sufficient precision;
- whether the candidate survives biological, artificial, and non-neural counterexamples.

Propositions 12 and 13 therefore stress-test the candidate's internal information content before any experiential interpretation is attached.

---

# References used for the physical candidate

- Albantakis L, Barbosa L, Findlay G, et al. Integrated information theory (IIT) 4.0. *PLOS Computational Biology* 19(10), e1011465 (2023). DOI: 10.1371/journal.pcbi.1011465.
- Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine* 5(198), 198ra105 (2013). DOI: 10.1126/scitranslmed.3006294.
- Lamme VAF. Towards a true neural stance on consciousness. *Trends in Cognitive Sciences* 10(11), 494-501 (2006). DOI: 10.1016/j.tics.2006.09.001.
- Luppi AI, Mediano PAM, Rosas FE, et al. A synergistic workspace for human consciousness revealed by Integrated Information Decomposition. *eLife* 12, RP88173 (2024). DOI: 10.7554/eLife.88173.
- Luppi AI, Uhrig L, Tasserie J, et al. Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains. *Nature Human Behaviour* 10, 777-802 (2026). DOI: 10.1038/s41562-025-02381-5.
- Maschke C, O'Byrne J, Colombo MA, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Communications Biology* 7, 946 (2024). DOI: 10.1038/s42003-024-06613-8.
- Mashour GA, Roelfsema P, Changeux JP, Dehaene S. Conscious Processing and the Global Neuronal Workspace Hypothesis. *Neuron* 105(5), 776-798 (2020). DOI: 10.1016/j.neuron.2020.01.026.
- Pearl J. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press (2009).
- Pigozzi F, Goldstein A, Levin M. Associative conditioning in gene regulatory network models increases integrative causal emergence. *Communications Biology* 8, 1027 (2025). DOI: 10.1038/s42003-025-08411-2.
