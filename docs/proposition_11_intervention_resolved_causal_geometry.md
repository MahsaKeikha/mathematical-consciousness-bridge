# Proposition 11: intervention-resolved causal geometry

## Candidate A - a physical signature to be tested, not assumed

The preceding propositions establish what a scientifically useful consciousness bridge must eventually accomplish. They do not yet provide the physical signature that makes the bridge true.

Proposition 11 introduces the first original candidate physical object in this repository:

\[
\boxed{
\text{Intervention-Resolved Causal Geometry (IRCG)}.
}
\]

The construction is motivated by several empirical and theoretical facts without identifying consciousness with any one of them:

- perturbational-complexity work shows that a direct cortical perturbation followed by a distributed, differentiated response can discriminate many conscious and unconscious conditions without requiring behavioral report [Casali et al., 2013; Maschke et al., 2024];
- integrated-information theories emphasize intrinsic causal structure and irreducibility [Albantakis et al., 2023];
- global-neuronal-workspace and recurrent-processing accounts emphasize recurrent, sustained, distributed processing [Mashour et al., 2020; Changeux and Farisco, 2026; Lamme, 2006];
- synergistic-workspace analyses report reductions in integrated information during loss of consciousness across anesthesia and disorders of consciousness [Luppi et al., 2024];
- cross-species anesthesia work links reduced information integration with reduced controllability of brain dynamics [Luppi et al., 2026].

The mathematical question is therefore:

> Can the full geometry of controlled causal responses provide a representation-invariant physical signature whose equivalence classes eventually match experiential equivalence classes?

That question is open. Proposition 11 constructs the object and proves its basic invariance and structural certificates so that Propositions 5-10 can attack it.

---

# 1. Physical domain and admissible perturbations

Let

\[
p\in\mathcal Q_P
\]

be a physical system already quotiented by physically irrelevant representation choices as required by Proposition 1.

For applications to a spatially extended system, let the candidate subsystem be divided into physical blocks

\[
V=\{1,\ldots,m\}.
\]

In the companion Spatiotemporal Observer Mathematics program, these blocks may belong to a certified time-dependent subsystem or world-tube. Proposition 11 does not assume that such a subsystem is conscious.

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

The use of \(do(u)\) is intervention semantics in the sense of causal modeling: it distinguishes a controlled perturbation from a merely observational correlation.

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

For every fixed \(\tau\), \(d_p^\tau\) is a pseudometric on the intervention set whenever distinct interventions can induce identical response laws.

The family

\[
\boxed{
\mathcal G_p
=
\left\{d_p^\tau:\tau\in\mathcal T\right\}
}
\]

is the **intervention-response geometry**.

It preserves more information than a single perturbational-complexity score. In particular, it records which perturbations produce similar responses, which produce distinct responses, and how that geometry changes with physical time.

Two useful derived quantities are

\[
\operatorname{Diam}_p(\tau)
=
\sup_{u,v\in\mathcal U_p}d_p^\tau(u,v),
\]

and, for a finite intervention family, the number of response-equivalence classes

\[
N_p(\tau)
=
\left|
\mathcal U_p/{\sim_{p,\tau}}
\right|,
\qquad
u\sim_{p,\tau}v
\iff
d_p^\tau(u,v)=0.
\]

These are differentiation diagnostics. Neither is interpreted as consciousness by definition.

---

# 3. Directed interventional influence tensor

Let \(P_{p,j}^{u,\tau}\) denote the marginal response law on block \(j\).

For each source block \(i\), let

\[
\mathcal E_i
\subseteq
\mathcal U_p\times\mathcal U_p
\]

contain intervention pairs that differ only in the controlled value of source block \(i\), while all other externally fixed intervention components are matched.

Define

\[
\boxed{
A_{ij}^p(\tau)
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
\left\{A_{ij}^p(\tau)ight\}_{i,j,\tau}
}
\]

records the strength and timing of directed perturbational influence among physical blocks.

This is intentionally stronger than a static connectivity matrix. A structural edge is admitted only when changing a controlled source intervention changes the target response law.

Define the aggregated directed graph

\[
i\to j
\quad\Longleftrightarrow\quad
\sup_{\tau\in\mathcal T}A_{ij}^p(\tau)>0,
\qquad i\ne j.
\]

A directed cycle in this graph is a minimal certificate of recurrent causal influence. A directed acyclic graph cannot contain such a return loop.

---

# 4. Partition response irreducibility

For a nontrivial partition

\[
\pi=\{B_1,\ldots,B_k\}
\]

of the physical blocks, let

\[
P_{p,B_r}^{u,\tau}
\]

be the corresponding marginal response law.

Define the productized partition model

\[
\boxed{
P_{p,\pi}^{u,\tau}
=
\bigotimes_{r=1}^{k}
P_{p,B_r}^{u,\tau}.
}
\]

The partition response-irredundancy is

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
\pi\in\mathfrak P(V),\ 	au\in\mathcal T
\right\}.
}
\]

A convenient minimum-partition diagnostic is

\[
\boxed{
\kappa_p^*
=
\inf_{\pi\in\mathfrak P_{\mathrm{nt}}(V)}
\sup_{\tau\in\mathcal T}
\kappa_p^\tau(\pi),
}
\]

where \(\mathfrak P_{\mathrm{nt}}(V)\) denotes nontrivial partitions.

This quantity measures irreducibility of the **observed interventional response law relative to productized block marginals**. It is not asserted to equal IIT's integrated information and should not be cited as such.

---

# 5. Candidate IRCG signature

Define the raw candidate object

\[
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
\]

Physical labels themselves are not intended to matter. Let \(\cong\) identify two such objects whenever there exist compatible bijections of block labels, intervention labels, and outcome coordinates that preserve delay values and transport every response law into the corresponding response law.

The **Intervention-Resolved Causal Geometry signature** is

\[
\boxed{
F_{\mathrm{IRCG}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

This is a structured signature, not a scalar threshold.

The long-term bridge question is whether there exists a physically and empirically justified relation between

\[
F_{\mathrm{IRCG}}(p)
\]

and the canonical bridge signature

\[
C_B(p)
\]

of Proposition 6.

The strongest possible target would be

\[
\boxed{
F_{\mathrm{IRCG}}(p)=F_{\mathrm{IRCG}}(p')
\iff
C_B(p)=C_B(p').
}
\]

Nothing in Proposition 11 assumes that biconditional.

---

# 6. Proposition 11A - invariance under compatible physical reparameterization

Suppose two descriptions \(p,p'\) are related by:

1. a bijection of physical block labels;
2. a bijection of admissible intervention labels preserving which block is manipulated;
3. for each response space, a measurable bijection \(h\) such that

\[
P_{p'}^{\phi(u),\tau}
=
h_\#P_p^{u,\tau};
\]

4. preservation of the declared delay values.

Then

\[
\boxed{
F_{\mathrm{IRCG}}(p)
=
F_{\mathrm{IRCG}}(p').
}
\]

## Proof

For a measurable bijection \(h\), total variation is invariant under pushforward:

\[
\left\|h_\#P-h_\#Q\right\|_{\mathrm{TV}}
=
\|P-Q\|_{\mathrm{TV}}.
\]

Therefore every response-geometry distance is preserved:

\[
d_{p'}^\tau(\phi(u),\phi(v))
=
d_p^\tau(u,v).
\]

Marginalization commutes with compatible relabeling of the physical blocks, so every directed influence entry is preserved under the corresponding block permutation. Product measures are likewise transported to product measures under component-wise bijections, hence

\[
\kappa_{p'}^\tau(\phi(\pi))
=
\kappa_p^\tau(\pi).
\]

Thus all components of \(\mathfrak C_p\) are carried isomorphically into \(\mathfrak C_{p'}\), and the two descriptions determine the same IRCG equivalence class.

\[
\boxed{\text{QED}}
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
\quad
\forall u\in\mathcal U_p.
}
\]

## Proof

Total-variation distance is zero if and only if the two probability measures are equal. The supremum of nonnegative distances over interventions equals zero if and only if every intervention-specific distance is zero.

\[
\boxed{\text{QED}}
\]

Therefore a positive \(\kappa_p^\tau(\pi)\) certifies failure of that particular product factorization at delay \(\tau\).

---

# 8. Proposition 11C - feedforward no-return certificate

Let the aggregated directed influence graph contain edge \(i\to j\) whenever

\[
\sup_{\tau\in\mathcal T}A_{ij}^p(\tau)>0.
\]

If this graph is directed acyclic, then no sequence of positive interventional influences can return from a block to itself through distinct physical blocks.

Equivalently, if a directed return loop exists, the aggregated graph must contain a directed cycle.

## Proof

A return sequence

\[
i_0\to i_1\to\cdots\to i_r=i_0
\]

with distinct intermediate blocks is, by definition, a directed cycle. Directed acyclic graphs contain no directed cycles.

\[
\boxed{\text{QED}}
\]

This is a structural recurrence certificate. The converse interpretation "directed cycle implies consciousness" is not made.

---

# 9. Immediate counterexample discipline

Candidate A is intentionally exposed to failure from the beginning.

Several observations already show why **integration alone** cannot be the final bridge:

1. non-neural systems can display causal emergence or integrated collective behavior;
2. engineered recurrent controllers can have strong feedback and complex perturbational responses;
3. a computer simulation can reproduce selected response statistics without thereby settling whether the relevant physical causal organization is preserved;
4. unconscious biological states may retain substantial local recurrence or information integration while losing other large-scale dynamical properties.

Accordingly, the IRCG program must search for at least four counterexample classes:

| Counterexample class | P5 question |
| --- | --- |
| highly integrated non-neural biological network | can IRCG be matched without the target experiential class? |
| recurrent artificial controller | does recurrence plus irreducibility overgenerate the bridge? |
| feedforward surrogate matched on passive outputs | do interventions expose the hidden structural difference? |
| conscious/unconscious biological pair with matched gross activity | does the full causal geometry separate them? |

The first two are especially important because causal emergence has been demonstrated in learned gene-regulatory-network models, making it scientifically unsafe to equate generic causal integration with consciousness.

---

# 10. Relation to existing theories and measures

The IRCG construction deliberately occupies a different logical role from the major existing theory families.

| External framework | What IRCG borrows as motivation | What IRCG does not assume |
| --- | --- | --- |
| PCI / TMS-EEG | controlled perturbation and spatiotemporal response complexity | that one scalar PCI threshold is the bridge |
| IIT | intrinsic causal organization and irreducibility | IIT axioms, postulates, or identity claim |
| GNWT | recurrent sustained distributed influence | that broadcast alone is sufficient |
| RPT | recurrent processing | that local recurrence alone is sufficient |
| synergistic workspace | integration plus distributed availability | that synergy alone is sufficient |
| predictive / neurorepresentational theories | structured internal dynamics and state dependence | a specific generative-model semantics |

IRCG is therefore best understood as a **theory-comparison substrate**: a physical object rich enough that different bridge theories can be translated into constraints on its geometry, while the repository remains free to reject those constraints if counterexamples defeat them.

---

# 11. Empirical program

A biological IRCG experiment would require a declared perturbation-response protocol such as:

1. identify or certify the candidate physical subsystem;
2. apply localized interventions at multiple subsystem locations and strengths;
3. record multichannel responses across a declared time grid;
4. estimate intervention-conditioned joint response laws;
5. construct \(d_p^\tau\), \(A_{ij}^p(\tau)\), and \(\kappa_p^\tau(\pi)\);
6. use Proposition 10 to retain protocols that improve bridge-relevant separation rather than within-class nuisance variation;
7. use Propositions 8 and 9 to certify finite-data uncertainty;
8. test Candidate A against conscious/unconscious transitions and non-conscious counterexample systems.

TMS-EEG is one possible perturbational implementation for human cortex, but the mathematical object is intentionally substrate independent. Electrical stimulation, optogenetic perturbation, closed-loop stimulation, pharmacological perturbation, or intervention on artificial systems can instantiate the same abstract protocol when causal semantics are justified.

---

# 12. What Proposition 11 establishes

**Proved:**

- a precise intervention-resolved causal-response geometry;
- representation invariance under compatible bijective reparameterization;
- an exact partition-factorization certificate;
- a feedforward no-return certificate;
- a structured physical signature suitable for P5-P10 falsification and recovery analysis.

**Not yet established:**

- that IRCG is sufficient for any experiential bridge;
- that IRCG is complete for consciousness;
- that a particular region of IRCG space corresponds to consciousness;
- that recurrence, integration, criticality, synergy, or controllability alone is sufficient;
- that current empirical datasets uniquely identify the correct bridge.

The next result should therefore be a **counterexample stress test and minimal-feature audit**, not a declaration that Candidate A is the answer.

---

# References used for Candidate A

- Albantakis L, Barbosa L, Findlay G, et al. Integrated information theory (IIT) 4.0. *PLOS Computational Biology* 19(10), e1011465 (2023). DOI: 10.1371/journal.pcbi.1011465.
- Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine* 5(198), 198ra105 (2013). DOI: 10.1126/scitranslmed.3006294.
- Lamme VAF. Towards a true neural stance on consciousness. *Trends in Cognitive Sciences* 10(11), 494-501 (2006). DOI: 10.1016/j.tics.2006.09.001.
- Luppi AI, Mediano PAM, Rosas FE, et al. A synergistic workspace for human consciousness revealed by Integrated Information Decomposition. *eLife* 12, RP88173 (2024). DOI: 10.7554/eLife.88173.
- Luppi AI, Uhrig L, Tasserie J, et al. Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains. *Nature Human Behaviour* 10, 777-802 (2026). DOI: 10.1038/s41562-025-02381-5.
- Maschke C, O'Byrne J, Colombo MA, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Communications Biology* 7, 946 (2024). DOI: 10.1038/s42003-024-06613-8.
- Mashour GA, Roelfsema P, Changeux JP, Dehaene S. Conscious Processing and the Global Neuronal Workspace Hypothesis. *Neuron* 105(5), 776-798 (2020). DOI: 10.1016/j.neuron.2020.01.026.
- Pearl J. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press (2009).
- Pigozzi F, Goldstein A, Levin M. Associative conditioning in gene regulatory network models increases integrative causal emergence. *Communications Biology* 8, 1027 (2025). DOI: 10.1038/s42003-025-08411-2.
