# Proposition 26: Partition-Irreducibility Scale Certification

## Status

**Repository theorem.** This proposition extends the P11 partition-irreducibility component through the P18 scale-reconstruction framework.

It is a theorem about finite physical response laws under declared block-compatible observation maps. It is **not** a consciousness criterion, a theorem of physical fusion, or a claim that every coarse-graining preserves causal organization.

---

# 1. Problem

P11 defines partition irreducibility by comparing an intervention-conditioned joint response law with the product of its block marginals. P17 shows that deterministic coarse-graining contracts total variation, while P18 gives a reconstruction-controlled upper bound on how much pairwise total-variation geometry may be lost.

The missing question is:

> When a physical response is observed at a coarser scale, under what conditions does the P11 partition-irreducibility quantity remain meaningful and quantitatively controlled?

This is more delicate than ordinary pairwise response geometry because the reference distribution is itself constructed from the response law through partition productization.

---

# 2. Fine partition irreducibility

Let the fine response space be a finite product space

\[
\Omega_f=\Omega_1\times\cdots\times\Omega_m,
\]

and let

\[
\pi=\{B_1,\ldots,B_r\}
\]

be a declared partition of the coordinate set \(\{1,\ldots,m\}\).

For intervention \(u\) and delay \(\tau\), write

\[
P^{u,\tau}
\]

for the fine joint response law. Its partition-factorized reference is

\[
\boxed{
P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi} P_B^{u,\tau}.
}
\]

The P11 irreducibility at that intervention is

\[
\boxed{
\kappa_f^{u,\tau}(\pi)
=
\left\|P^{u,\tau}-P_{\pi}^{u,\tau}\right\|_{\mathrm{TV}}.
}
\]

The intervention-aggregated P11 quantity is obtained by taking the declared supremum over \(u\).

---

# 3. Block-compatible coarse observation

A coarse observation map must respect the declared partition if the same partition semantics are to be compared across scale.

Assume

\[
C=C_1\times\cdots\times C_m,
\]

where each coordinate map

\[
C_j:\Omega_j\to\overline\Omega_j
\]

acts only on its own coordinate.

Equivalently, each coarse block associated with \(B\in\pi\) depends only on the fine coordinates in \(B\). This is the **block-compatibility assumption**.

Define

\[
\overline P^{u,\tau}=C_\#P^{u,\tau}.
\]

Because \(C\) factorizes along the declared blocks,

\[
\boxed{
C_\#P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}
(C_B)_\#P_B^{u,\tau}.
}
\]

Thus partition productization commutes with block-compatible coarse observation.

This identity is essential. Without it, one would be comparing different partition semantics at the two scales.

---

# 4. P26 contraction theorem

Define coarse irreducibility by

\[
\boxed{
\kappa_c^{u,\tau}(\pi)
=
\left\|
C_\#P^{u,\tau}
-
C_\#P_{\pi}^{u,\tau}
\right\|_{\mathrm{TV}}.
}
\]

By total-variation data processing,

\[
\left\|
C_\#P^{u,\tau}
-
C_\#P_{\pi}^{u,\tau}
\right\|_{\mathrm{TV}}
\le
\left\|
P^{u,\tau}-P_{\pi}^{u,\tau}
\right\|_{\mathrm{TV}}.
\]

Therefore

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi).
}
\]

## Interpretation

Block-compatible deterministic observation cannot create additional partition irreducibility relative to the same declared partition. It can only preserve or erase dependence visible at the fine scale.

This is an observation theorem, not a fusion theorem.

---

# 5. Reconstruction-controlled upper bound

Let \(R\) be a P18 fiber-consistent stochastic decoder for the coarse observation map \(C\). Define the reconstruction operator

\[
D=R_\#C_\#.
\]

For any fine law \(Q\), let

\[
\rho(Q)=\|Q-DQ\|_{\mathrm{TV}}.
\]

Apply the P18 pairwise theorem to the pair

\[
P^{u,\tau},
\qquad
P_{\pi}^{u,\tau}.
\]

Then

\[
\boxed{
0
\le
\kappa_f^{u,\tau}(\pi)
-
\kappa_c^{u,\tau}(\pi)
\le
\rho(P^{u,\tau})
+
\rho(P_{\pi}^{u,\tau}).
}
\]

Define the partition-specific reconstruction budget

\[
\boxed{
\varepsilon_{\pi}^{u,\tau}
=
\rho(P^{u,\tau})
+
\rho(P_{\pi}^{u,\tau}).
}
\]

Then

\[
\boxed{
\kappa_c^{u,\tau}(\pi)
\ge
\kappa_f^{u,\tau}(\pi)
-
\varepsilon_{\pi}^{u,\tau}.
}
\]

This form is sharper and more informative than replacing both reconstruction terms by one common supremum immediately.

If a uniform bound

\[
\rho(P^{u,\tau})\le\rho_*,
\qquad
\rho(P_{\pi}^{u,\tau})\le\rho_*
\]

holds, then the simpler corollary is

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi)
\le2\rho_*.
}
\]

---

# 6. Exact preservation

If both the response law and its partition-product reference reconstruct exactly,

\[
\rho(P^{u,\tau})=0,
\qquad
\rho(P_{\pi}^{u,\tau})=0,
\]

then

\[
\boxed{
\kappa_c^{u,\tau}(\pi)
=
\kappa_f^{u,\tau}(\pi).
}
\]

Microscopic invertibility of \(C\) is not required globally. Exact reconstruction is needed only on the two-law family relevant to the declared irreducibility comparison.

---

# 7. Threshold preservation

Let \(\theta\ge0\) be a declared irreducibility threshold. If

\[
\boxed{
\kappa_f^{u,\tau}(\pi)
>
\theta+arepsilon_{\pi}^{u,\tau},
}
\]

then

\[
\boxed{
\kappa_c^{u,\tau}(\pi)>	heta.
}
\]

Conversely, contraction implies

\[
\boxed{
\kappa_c^{u,\tau}(\pi)>	heta
\Longrightarrow
\kappa_f^{u,\tau}(\pi)>	heta.
}
\]

Thus block-compatible coarse observation cannot manufacture a threshold crossing, while a sufficiently large fine-scale margin must survive.

---

# 8. Counterexample: dependence can disappear completely

Consider two binary coordinates with

\[
P(0,0)=P(1,1)=0.45,
\qquad
P(0,1)=P(1,0)=0.05.
\]

The marginals are uniform, so

\[
P_{\pi}(x_1,x_2)=\frac14
\]

for the partition \(\pi=\{\{1\},\{2\}\}\), and

\[
\kappa_f(\pi)=0.4.
\]

Now collapse the first coordinate to a single coarse value while leaving the second unchanged. The coarse joint law factorizes exactly, giving

\[
\boxed{
\kappa_c(\pi)=0.
}
\]

Therefore positive fine-scale partition irreducibility need not survive arbitrary information-destroying observation.

This counterexample rules out a naive scale-invariance claim.

---

# 9. Relation to P11, P17, P18, and P25

The logical dependency is

\[
\boxed{
\text{P11 partition irreducibility}
+
\text{P17 contraction}
+
\text{P18 reconstruction}
\Longrightarrow
\text{P26 partition-scale certificate}.
}
\]

P25 applies the same scale philosophy to the directed-influence component \(\mathcal A\). P26 applies it to the partition component \(\mathcal K\).

Together they move the scale program closer to the full P11 structured physical object

\[
\mathfrak C_p
=(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

But neither theorem yet establishes full-structure equivalence across scale.

---

# 10. Scope boundary

P26 certifies **observation-scale behavior** of one declared partition under a block-compatible deterministic map and a declared reconstruction decoder.

It does not establish:

- arbitrary node aggregation;
- source/intervention merging;
- changing intervention semantics;
- optimization over all partitions after coarse-graining;
- genuine physical split or fusion;
- preservation of the complete P11 structure;
- physical completeness;
- experiential equivalence;
- consciousness.

The next mathematical problem is to characterize how the **partition lattice itself** transforms when multiple fine blocks are physically or observationally aggregated into coarse blocks.

---

# 11. Executable realization

Implementation:

[`src/consciousness_bridge/partition_irreducibility_scale_certification.py`](../src/consciousness_bridge/partition_irreducibility_scale_certification.py)

Regression tests:

[`tests/test_partition_irreducibility_scale_certification.py`](../tests/test_partition_irreducibility_scale_certification.py)

The executable tests include exact preservation, complete loss under coordinate collapse, threshold certification, and construction of factorized coordinate decoders.
