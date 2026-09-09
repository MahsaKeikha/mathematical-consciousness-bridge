# Proposition 28: Intervention Compatibility Under Node Aggregation

## Status

**Repository theorem.** Proposition 28 extends the P25 directed-influence scale theorem through the changing node set formalized by P27.

It addresses a specific physical question: when several fine source nodes are represented by one coarse source node, when do the P11 matched intervention-pair families retain an unambiguous source meaning, and what directed-influence statement survives at the corresponding coarse target?

P28 does not infer a new physical intervention mechanism from node aggregation. In particular, pooling fine intervention pairs into one coarse source family does not create a simultaneous perturbation of all fine constituents.

---

# 1. Fine and coarse source nodes

Let

\[
a:V_f\twoheadrightarrow V_c
\]

be the P27 surjective node-aggregation map and let

\[
F_c=a^{-1}(c)
\]

be the fine-node fiber represented by coarse node \(c\).

For each fine source \(i\in V_f\), P11 supplies a declared family of matched intervention pairs

\[
\mathcal E_i
\subseteq
\mathcal U\times\mathcal U.
\]

Each pair \((u,v)\in\mathcal E_i\) is interpreted only according to the declared experimental design: the pair is a comparison attributed to source \(i\).

---

# 2. Source-label compatibility

The same matched intervention pair may appear under more than one fine source label. Under node aggregation, that is harmless only when all of those source labels lie in the same aggregation fiber.

For a matched pair \(e=(u,v)\), define its fine source-incidence set

\[
S_f(e)
=
\{i\in V_f:e\in\mathcal E_i\}.
\]

Its coarse source-image set is

\[
S_c(e)
=
\{a(i):i\in S_f(e)\}.
\]

## Proposition 28A: exact source-label descent criterion

The fine matched-pair incidence relation descends to an unambiguous coarse source labeling if and only if

\[
\boxed{
|S_c(e)|\le1
\qquad
\text{for every declared pair }e.
}
\]

Equivalently,

\[
\boxed{
e\in\mathcal E_i\cap\mathcal E_j
\Longrightarrow
a(i)=a(j).
}
\]

### Necessity

If one pair were assigned to fine sources \(i\) and \(j\) with \(a(i)\ne a(j)\), then that unchanged pair would acquire two different coarse source labels. No single-valued coarse source assignment could preserve the fine incidence semantics.

### Sufficiency

If every pair's fine source labels all map to one coarse source, assign that pair to the unique coarse image. This gives a well-defined descended incidence relation.

---

# 3. Canonical coarse matched-pair family

When the compatibility condition holds, define

\[
\boxed{
\mathcal E_c^{a}
=
\bigcup_{i\in F_c}\mathcal E_i.
}
\]

Duplicate pairs are retained only once.

This operation is a **pooling of inherited comparisons**. It does not assert

\[
\text{intervene on every }i\in F_c\text{ simultaneously}.
\]

That would be an additional intervention protocol requiring its own physical definition and response laws.

Thus

\[
\boxed{
\text{aggregate source label}
\neq
\text{new aggregate physical actuator}.
}
\]

---

# 4. Coarse target as a fine response block

Let \(d\in V_c\) be a coarse target node with fine target fiber

\[
F_d=a^{-1}(d).
\]

For each intervention \(u\), delay \(\tau\), and fine joint response law \(P^{u,\tau}\), define the target-fiber marginal

\[
\boxed{
P_{F_d}^{u,\tau}
=\operatorname{Marg}_{F_d}P^{u,\tau}.
}
\]

The correct fine comparison for the aggregate target is therefore the joint law of the entire target fiber, not an arbitrary one-node marginal.

---

# 5. Fine block influence attached to a coarse source

For coarse source \(c\) and coarse target \(d\), define the inherited fine block influence

\[
\boxed{
A_{c\to d}^{f,a}(\tau)
=
\sup_{(u,v)\in\mathcal E_c^a}
\left\|
P_{F_d}^{u,\tau}
-
P_{F_d}^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

This is not a new causal primitive. It is the P11 matched-pair supremum evaluated on the target block corresponding to the P27 node fiber and over the canonically pooled pair family corresponding to the aggregate source.

---

# 6. Aggregate target-state map

Let

\[
g_d:
\Omega_{F_d}	o\overline\Omega_d
\]

be the declared deterministic state map for aggregate target node \(d\).

The coarse target law is

\[
\boxed{
\overline P_d^{u,\tau}
=(g_d)_\#P_{F_d}^{u,\tau}.
}
\]

Define coarse directed influence

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
=
\sup_{(u,v)\in\mathcal E_c^a}
\left\|
\overline P_d^{u,\tau}
-
\overline P_d^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The same descended matched-pair family is used on both sides of the scale comparison.

---

# 7. Directed-influence contraction

For each pair \((u,v)\in\mathcal E_c^a\), total-variation data processing gives

\[
\left\|
(g_d)_\#P_{F_d}^{u,\tau}
-
(g_d)_\#P_{F_d}^{v,\tau}
\right\|_{\mathrm{TV}}
\le
\left\|
P_{F_d}^{u,\tau}
-
P_{F_d}^{v,\tau}
\right\|_{\mathrm{TV}}.
\]

Taking the supremum over the identical pair family yields

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
\le
A_{c\to d}^{f,a}(\tau).
}
\]

Thus target-state aggregation cannot manufacture a stronger directed-influence value once the source intervention semantics have validly descended.

---

# 8. Reconstruction-controlled influence loss

Let \(R_d\) be a P18 decoder for the target-fiber state map \(g_d\). Define

\[
D_d=(R_d)_\#(g_d)_\#
\]

and the target-family reconstruction defect

\[
\boxed{
\rho_{c\to d}^{a}(\tau)
=
\sup_{u\in U(\mathcal E_c^a)}
\left\|
P_{F_d}^{u,\tau}-D_dP_{F_d}^{u,\tau}
\right\|_{\mathrm{TV}},
}
\]

where \(U(\mathcal E_c^a)\) contains all interventions appearing in the descended pair family.

Applying P18 to every pair and then taking the supremum gives

\[
\boxed{
0
\le
A_{c\to d}^{f,a}(\tau)
-
A_{c\to d}^{c,a}(\tau)
\le
2\rho_{c\to d}^{a}(\tau).
}
\]

Equivalently,

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
\ge
A_{c\to d}^{f,a}(\tau)
-2\rho_{c\to d}^{a}(\tau).
}
\]

---

# 9. Exact preservation and threshold certification

If

\[
\rho_{c\to d}^{a}(\tau)=0,
\]

then

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
=
A_{c\to d}^{f,a}(\tau).
}
\]

For a declared threshold \(\theta\),

\[
\boxed{
A_{c\to d}^{f,a}(\tau)
>
\theta+2\rho_{c\to d}^{a}(\tau)
\Longrightarrow
A_{c\to d}^{c,a}(\tau)>	heta.
}
\]

Conversely, contraction gives

\[
\boxed{
A_{c\to d}^{c,a}(\tau)>	heta
\Longrightarrow
A_{c\to d}^{f,a}(\tau)>	heta.
}
\]

So a compatible coarse construction cannot create a threshold edge that was absent in the inherited fine block comparison.

---

# 10. Why source compatibility is not optional

Suppose the same matched pair \(e=(u,v)\) is attributed to fine sources \(i\) and \(j\), but

\[
a(i)\ne a(j).
\]

Then any coarse representation preserving that pair unchanged would need to assign one physical comparison simultaneously to two distinct coarse sources. A source-indexed P11 influence matrix would no longer have an unambiguous row assignment.

This is not fixed by target reconstruction, more samples, or finer state measurement. It is a defect in the source intervention semantics.

Therefore

\[
\boxed{
\text{target-response recoverability}
\not\Rightarrow
\text{source-intervention compatibility}.
}
\]

P25 controlled the former while holding the latter fixed. P28 makes the latter explicit under node aggregation.

---

# 11. Aggregate-source influence is a supremum, not synergy

If a coarse source fiber contains two fine sources \(i_1,i_2\), then

\[
\mathcal E_c^a
=
\mathcal E_{i_1}\cup\mathcal E_{i_2}
\]

and

\[
A_{c\to d}^{f,a}
=
\max
\left\{
\sup_{e\in\mathcal E_{i_1}}d_e,
\sup_{e\in\mathcal E_{i_2}}d_e
\right\}
\]

when the pair families are finite.

No term involving a simultaneous \((i_1,i_2)\) perturbation appears unless such an intervention is independently included in the experimental design.

Hence P28 cannot be used to infer collective causal synergy merely from node aggregation.

---

# 12. Relation to P25 and P27

P25 proves directed-influence stability under target observation while source and intervention semantics are fixed.

P27 proves which node partitions and response blocks have exact meaning after a node quotient.

P28 combines those requirements on the directed-influence branch:

\[
\boxed{
\text{P11 matched interventions}
+
\text{P25 target-scale theorem}
+
\text{P27 node aggregation}
\Longrightarrow
\text{P28 aggregate-source influence certificate}.
}
\]

The theorem does not make P25 obsolete. P25 is the fixed-source special case; P28 adds a source-label descent condition and uses target-fiber marginals induced by the node aggregation.

---

# 13. What remains before full P11 scale equivalence

After P27 and P28, two major P11 components have explicit changing-node-set transport rules:

- \(\mathcal K\): partition structure via saturated partition descent;
- \(\mathcal A\): directed influence via compatible matched-pair descent and target-fiber aggregation.

The full structure

\[
\mathfrak C
=(V,\mathcal U,\mathcal T,\mathcal G,\mathcal A,\mathcal K)
\]

still requires a theorem aligning the **entire response geometry \(\mathcal G\)**, admissible intervention set \(\mathcal U\), and delay family \(\mathcal T\) across the same node quotient.

That is the natural next physical theorem burden.

---

# 14. Scope boundary

P28 does not establish:

- a new simultaneous intervention on all members of an aggregate source;
- physical fusion of the fine nodes;
- intervention equivalence when the actual actuator physics differ;
- preservation of unmeasured intervention channels;
- complete P11 scale equivalence;
- physical completeness;
- experiential equivalence;
- consciousness.

It gives an exact bookkeeping and distinguishability theorem for **declared matched intervention comparisons** under a declared node aggregation.

---

# 15. Executable realization

Implementation:

[`src/consciousness_bridge/intervention_node_aggregation_compatibility.py`](../src/consciousness_bridge/intervention_node_aggregation_compatibility.py)

Regression tests:

[`tests/test_intervention_node_aggregation_compatibility.py`](../tests/test_intervention_node_aggregation_compatibility.py)

The executable suite checks source-label descent, pair deduplication inside one aggregate source, rejection of cross-fiber source ambiguity, lossless target aggregation, P18-controlled lossy aggregation, aggregate-source supremum semantics, missing response rejection, and surjectivity of the node quotient.
