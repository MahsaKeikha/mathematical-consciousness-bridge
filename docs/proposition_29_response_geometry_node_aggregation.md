# Proposition 29: Response-Geometry Transport Under Node Aggregation

## Status

**Repository theorem.** Proposition 29 transports the P11 response-geometry component through the same changing node set used by P27 and P28.

The theorem holds the declared intervention labels and delay labels fixed. It changes the physical response representation by a declared node aggregation and aggregate-state map. It does not merge interventions, resample time, establish physical completeness, or assign experiential meaning to response geometry.

---

# 1. Problem

P27 transports partition semantics through a surjective node quotient. P28 transports source labels for matched intervention comparisons and then certifies directed influence. The remaining major P11 component is the full response geometry

\[
\mathcal G.
\]

For a declared intervention set

\[
\mathcal U=\{u_1,\ldots,u_m\}
\]

and delay family

\[
\mathcal T=\{\tau_1,\ldots,\tau_r\},
\]

P11 compares every pair of intervention-conditioned response laws at every retained delay.

P29 asks:

> If the physical node set is aggregated while intervention and delay semantics remain unchanged, how much of this entire indexed response geometry can be lost?

---

# 2. Fine response geometry

Let

\[
P^{u,\tau}
\]

be the fine joint response law for intervention \(u\in\mathcal U\) at delay \(\tau\in\mathcal T\).

For every unordered intervention pair \(u\ne v\), define

\[
\boxed{
G_f(u,v,\tau)
=
\left\|P^{u,\tau}-P^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The complete fine geometry is the indexed family

\[
\boxed{
\mathcal G_f
=
\{G_f(u,v,\tau):u<v,\ \tau\in\mathcal T\}.
}
\]

This theorem treats the labels \(u,v,\tau\) as part of the scientific object. A numerical matrix without those semantics is not sufficient.

---

# 3. Node aggregation and aggregate-state map

Let

\[
a:V_f\twoheadrightarrow V_c
\]

be the P27 node aggregation. For every coarse node \(c\in V_c\), let

\[
F_c=a^{-1}(c)
\]

be its fine-node fiber and let

\[
g_c:\Omega_{F_c}\to\overline\Omega_c
\]

be the declared deterministic aggregate-state map.

The global map is

\[
\boxed{
C_a(x)
=
\bigl(g_c(x_{F_c})\bigr)_{c\in V_c}.
}
\]

The coarse response law is

\[
\boxed{
\overline P^{u,\tau}
=(C_a)_\#P^{u,\tau}.
}
\]

P29 requires the **same** declared intervention set \(\mathcal U\) and delay family \(\mathcal T\) on both sides. Intervention merging or temporal resampling is a different theorem problem.

---

# 4. Coarse response geometry

Define

\[
\boxed{
G_c(u,v,\tau)
=
\left\|
\overline P^{u,\tau}
-
\overline P^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

Then

\[
\mathcal G_c
=
\{G_c(u,v,\tau):u<v,\ \tau\in\mathcal T\}.
\]

Because the index set is unchanged, each coarse geometry entry has one exact fine counterpart.

---

# 5. Entrywise contraction theorem

Total-variation data processing under deterministic pushforward gives, for every \(u,v,\tau\),

\[
\left\|
(C_a)_\#P^{u,\tau}
-
(C_a)_\#P^{v,\tau}
\right\|_{\mathrm{TV}}
\le
\left\|
P^{u,\tau}
-
P^{v,\tau}
\right\|_{\mathrm{TV}}.
\]

Therefore

\[
\boxed{
0\le
G_f(u,v,\tau)-G_c(u,v,\tau).
}
\]

This statement holds simultaneously for the complete declared geometry because it is a deterministic statement for every indexed pair.

---

# 6. Reconstruction-controlled geometry distortion

Let \(R\) be a P18 decoder for the global aggregate-state map and define

\[
D=R_\#(C_a)_\#.
\]

For each intervention-delay response law, define

\[
\rho_{u,\tau}
=
\left\|
P^{u,\tau}-DP^{u,\tau}
\right\|_{\mathrm{TV}}.
\]

P18 applied to the pair \(P^{u,\tau},P^{v,\tau}\) gives the sharper entrywise inequality

\[
\boxed{
0\le
G_f(u,v,\tau)-G_c(u,v,\tau)
\le
\rho_{u,\tau}+\rho_{v,\tau}.
}
\]

Define the uniform reconstruction defect over the declared grid:

\[
\boxed{
\rho_*
=
\sup_{u\in\mathcal U,\ \tau\in\mathcal T}
\rho_{u,\tau}.
}
\]

Then

\[
\boxed{
0\le
G_f(u,v,\tau)-G_c(u,v,\tau)
\le2\rho_*
\quad\forall u,v,\tau.
}
\]

Equivalently, using the sup norm on the common indexed geometry,

\[
\boxed{
\|\mathcal G_f-\mathcal G_c\|_\infty
\le2\rho_*.
}
\]

This is the central P29 result.

---

# 7. Exact geometry preservation

If

\[
\rho_*=0,
\]

then every declared response law reconstructs exactly on the tested intervention-delay family. Hence

\[
\boxed{
G_c(u,v,\tau)=G_f(u,v,\tau)
\quad\forall u,v,\tau.
}
\]

Therefore

\[
\boxed{
\mathcal G_c=\mathcal G_f.
}
\]

The node count may decrease while the complete operational geometry remains exactly preserved. Global microscopic invertibility outside the declared response family is unnecessary.

---

# 8. Diameter corollary

Define the fine and coarse response diameters

\[
\Delta_f
=
\sup_{u,v,\tau}G_f(u,v,\tau),
\qquad
\Delta_c
=
\sup_{u,v,\tau}G_c(u,v,\tau).
\]

Entrywise contraction gives

\[
\boxed{
\Delta_c\le\Delta_f.
}
\]

The uniform P18 bound gives

\[
\boxed{
0\le\Delta_f-\Delta_c\le2\rho_*.
}
\]

The diameter is therefore a corollary of the full geometry theorem, not a replacement for it.

---

# 9. Threshold preservation for every geometry entry

Let \(\theta\in[0,1]\) be a declared separation threshold. If

\[
\boxed{
G_f(u,v,\tau)>\theta+2\rho_*,
}
\]

then

\[
\boxed{
G_c(u,v,\tau)>\theta.
}
\]

Conversely, contraction implies

\[
G_c(u,v,\tau)>\theta
\Longrightarrow
G_f(u,v,\tau)>\theta.
\]

Thus coarse state aggregation cannot manufacture a threshold-level intervention distinction that is absent at the fine scale, while sufficiently separated fine response pairs must survive.

---

# 10. Why the common index grid matters

P29 does not compare two unlabeled distance matrices. It compares the same scientific experiment grid before and after response-state aggregation.

The requirements are:

1. the same intervention labels \(\mathcal U\);
2. the same delay labels \(\mathcal T\);
3. complete response data for every declared \((u,\tau)\) cell;
4. one declared aggregation-compatible physical state map \(C_a\).

If intervention labels are merged, split, or replaced, there is no longer a one-to-one identification of geometry entries. If delays are resampled or warped, a temporal alignment theorem is required first.

Therefore

\[
\boxed{
\text{state-space aggregation}
\neq
\text{intervention aggregation}
\neq
\text{time aggregation}.
}
\]

---

# 11. Relation to P17 and P18

P17 supplies the non-expansion statement for any deterministic coarse map:

\[
D_{\mathrm{TV}}(C_\#P,C_\#Q)
\le
D_{\mathrm{TV}}(P,Q).
\]

P18 supplies the reconstruction-controlled reverse inequality:

\[
D_{\mathrm{TV}}(P,Q)
\le
D_{\mathrm{TV}}(C_\#P,C_\#Q)
+ho(P)+\rho(Q).
\]

P29 applies those results simultaneously to every pair in the P11 response family indexed by the declared experiment grid.

Its contribution is not a new distance inequality. Its contribution is the **complete structured transport statement for \(\mathcal G\)** under the same node aggregation program used by P27 and P28.

---

# 12. Relation to P27 and P28

P27 controls the P11 partition component \(\mathcal K\) when nodes are aggregated.

P28 controls the P11 directed-influence component \(\mathcal A\) after matched intervention source labels have validly descended.

P29 controls the P11 response-geometry component \(\mathcal G\) on a fixed intervention-delay grid.

The three branches now cover the central P11 physical components:

\[
\boxed{
\mathcal G,
\qquad
\mathcal A,
\qquad
\mathcal K.
}
\]

This is still not automatically a proof that the complete P11 object

\[
\mathfrak C=(V,\mathcal U,\mathcal T,\mathcal G,\mathcal A,\mathcal K)
\]

is equivalent across scale. A full assembly theorem must state a single compatible node map, state map, intervention semantics, delay semantics, and reconstruction family and then show that all component correspondences hold simultaneously.

---

# 13. Scientific boundary

P29 proves response-geometry transport under a declared node aggregation with fixed intervention and delay semantics. It does not establish:

- merging or quotienting intervention labels;
- creation of new interventions;
- simultaneous aggregate-source actuation;
- temporal resampling or delay equivalence;
- exact full P11 structure equivalence by itself;
- physical completeness;
- experiential equivalence;
- consciousness.

The natural next theorem target is a **simultaneous full-structure scale certificate** assembling P27, P28, and P29 under one declared compatibility diagram.

---

# 14. Executable realization

Implementation:

[`src/consciousness_bridge/response_geometry_node_aggregation.py`](../src/consciousness_bridge/response_geometry_node_aggregation.py)

Regression tests:

[`tests/test_response_geometry_node_aggregation.py`](../tests/test_response_geometry_node_aggregation.py)

The executable suite checks complete experiment-grid validation, all pairwise geometry entries, exact preservation under lossless node aggregation, contraction and P18 distortion under information-destroying aggregation, geometry-index consistency, threshold certification, and uniqueness of intervention and delay labels.
