# Proposition 17: coarse-graining, refinement, and recoverability

## Physical question

Proposition 16 characterizes independent composition and response-level coupling for two systems with fixed block identities. The next structural problem arises when the physical description itself changes granularity:

> What information is preserved when a fine physical response description is mapped to a coarser one, and when can the fine structure be recovered from the coarse representation?

This question is necessary before treating splitting or merging of physical blocks. Proposition 17 addresses the mathematically clean part first: deterministic coarse-graining of intervention-conditioned response laws.

The result concerns loss or preservation of physical response information. It does not identify coarse-graining with physical fusion, and it does not assign an experiential interpretation to either fine or coarse descriptions.

---

# 1. Deterministic coarse-graining

Let \(\Omega_f\) be a finite fine response space and \(\Omega_c\) a finite coarse response space.

Let

\[
\boxed{
C:\Omega_f\to\Omega_c
}
\]

be a deterministic coarse-graining map.

For any fine response law \(P\), define the pushforward law

\[
\boxed{
C_{\#}P(y)
=
\sum_{x:C(x)=y}P(x).
}
\]

For an intervention-conditioned family \(P_p^{u,\tau}\), the coarse response family is

\[
\boxed{
\widetilde P_p^{u,\tau}
=
C_{\#}P_p^{u,\tau}.
}
\]

---

# 2. Proposition 17A - total-variation contraction

For any two fine response laws \(P,Q\),

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

Therefore every intervention-response distance contracts under deterministic coarse-graining:

\[
\boxed{
\widetilde d_p^{\tau}(u,v)
\le
d_p^{\tau}(u,v).
}
\]

## Proof

In the finite case,

\[
\begin{aligned}
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
&=
\frac12
\sum_{y\in\Omega_c}
\left|
\sum_{x:C(x)=y}(P(x)-Q(x))
\right|\\
&\le
\frac12
\sum_{y\in\Omega_c}
\sum_{x:C(x)=y}|P(x)-Q(x)|\\
&=
\frac12
\sum_{x\in\Omega_f}|P(x)-Q(x)|\\
&=
\|P-Q\|_{\mathrm{TV}}.
\end{aligned}
\]

\(\square\)

This is the finite deterministic data-processing inequality for total variation.

---

# 3. Proposition 17B - equality under bijective reparameterization

If \(C\) is bijective on the observed support of both \(P\) and \(Q\), then

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
=
\|P-Q\|_{\mathrm{TV}}.
}
\]

Thus a pure relabeling preserves response geometry exactly, while a genuinely many-to-one coarse-graining can contract it.

This is consistent with the representation-invariance logic of P1 and the relabeling quotient of P14.

---

# 4. Proposition 17C - non-injective coarse-graining is not generically invertible

Suppose \(C\) is not injective. Then there exist

\[
x\ne x'
\]

such that

\[
C(x)=C(x').
\]

Let

\[
P=\delta_x,
\qquad
Q=\delta_{x'}.
\]

Then

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}=1
}
\]

but

\[
\boxed{
C_{\#}P=C_{\#}Q,
\qquad
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}=0.
}
\]

Therefore no decoder from the coarse distribution alone can reconstruct the fine response law on the full domain.

Equivalently, a non-injective deterministic coarse-graining admits an exact information-collision witness.

---

# 5. Corollary - response-geometry collapse

If two intervention-conditioned fine laws differ only within one fiber of \(C\), then the fine response geometry may be nonzero while the corresponding coarse response geometry is zero.

Thus

\[
\boxed{
\widetilde d_p^{\tau}(u,v)=0
\not\Rightarrow
d_p^{\tau}(u,v)=0.
}
\]

A coarse representation can therefore make physically different intervention responses appear identical.

---

# 6. Refinement ambiguity

A later "split" or refinement of a coarse block is not uniquely determined by the coarse response law unless extra physical structure is supplied.

If the coarse map has a fiber

\[
C^{-1}(y)=\{x_1,\ldots,x_r\},
\qquad r>1,
\]

then a coarse mass

\[
\widetilde P(y)
\]

can be distributed among the fine states in infinitely many ways subject only to

\[
\sum_{i=1}^{r}P(x_i)=\widetilde P(y).
\]

Therefore the refinement problem requires additional assumptions, interventions, measurements, dynamics, or priors.

This is an identifiability statement, not merely a computational inconvenience.

---

# 7. Relation to physical splitting and merging

Proposition 17 concerns **descriptive or observational coarse-graining** of an existing physical response law.

A genuine physical merge can change the underlying dynamics and intervention structure:

\[
\mathcal D_{\mathrm{before}}
\ne
\mathcal D_{\mathrm{after}}.
\]

Likewise, a physical split can create new intervention channels or new state variables.

Accordingly,

\[
\boxed{
\text{coarse-graining of a description}
\neq
\text{physical fusion of subsystems}.
}
\]

P17 supplies the representation-theoretic baseline against which future split/merge dynamics must be compared.

---

# 8. Scientific consequence

The theorem establishes a one-way hierarchy:

\[
\boxed{
\text{fine intervention-response structure}
\longrightarrow
\text{coarse response structure}
}
\]

is always well defined under a declared deterministic map, while

\[
\boxed{
\text{coarse response structure}
\longrightarrow
\text{fine intervention-response structure}
}
\]

is not generally identifiable when the map is many-to-one.

This means a future bridge theory cannot assume that a coarse neural, computational, or subsystem description preserves every physical distinction present at a finer scale. The relevant scale must be justified rather than chosen only for convenience.

---

# 9. Provenance

The contraction theorem is standard probability data processing for total variation; the bridge-specific application to intervention-resolved causal structure, the refinement-collision formulation, and the role of this result in the composition/splitting program are repository results.

See:

- [P1 - Representation Invariance](proposition_1_representation_invariance.md)
- [P11 - Intervention-Resolved Causal Structure](proposition_11_intervention_resolved_causal_structure.md)
- [P14 - Temporal Continuation](proposition_14_temporal_continuation.md)
- [P16 - Independent Composition and Coupling](proposition_16_independent_composition_and_coupling.md)
- [Equation and Citation Map](equation_and_citation_map.md)
- [`references.bib`](../references.bib)
