# Proposition 14: temporal continuation of intervention-resolved causal structure

## Physical question

Propositions 11-13 treat the intervention-resolved causal structure of a physical system as a structured physical signature and audit how much information is lost by compressing that structure.

A further question is unavoidable for any theory intended to describe an evolving physical system:

> When should causal-structure states measured at different physical times be treated as a continuous evolution of the same physical organization rather than as unrelated snapshots?

A temporal criterion must satisfy two requirements immediately:

1. it must compare the full physical signature rather than one selected scalar;
2. it must be invariant under physically irrelevant relabelings that may change from one time point to the next.

Proposition 14 gives a finite-dimensional theorem that satisfies both requirements.

The result is a theorem about temporal organization of the physical candidate. It does not assign an experiential interpretation to temporal continuity.

---

# 1. Fixed-coordinate component fingerprint

For a declared finite audit representation, write the three-component causal-structure fingerprint as

\[
\boxed{
c
=
(g,a,k)
\in
\mathbb R^{m_G}
\times
\mathbb R^{m_A}
\times
\mathbb R^{m_K},
}
\]

where

- \(g\) is the ordered response-geometry fingerprint;
- \(a\) is the ordered directed-influence fingerprint;
- \(k\) is the ordered partition-irredundancy fingerprint.

The coordinates are assumed to have already been generated from the intervention-conditioned response laws defined in Proposition 11.

Let

\[
w_G,w_A,w_K>0
\]

be declared component weights. Define

\[
\boxed{
D_w(c,c')
=
\max\left\{
 w_G\|g-g'\|_\infty,
 w_A\|a-a'\|_\infty,
 w_K\|k-k'\|_\infty
\right\}.
}
\]

The weights state the physical normalization used to put the three component blocks on a common comparison scale. They are part of the declared measurement model and are not fitted to an experiential label in this theorem.

---

# 2. Proposition 14A - weighted component metric

## Statement

For positive weights

\[
w_G,w_A,w_K>0,
\]

\(D_w\) is a metric on the fixed-dimensional fingerprint space.

## Proof

Non-negativity follows from non-negativity of the sup norm.

If

\[
D_w(c,c')=0,
\]

then every weighted component distance is zero. Since all weights are strictly positive,

\[
\|g-g'\|_\infty
=
\|a-a'\|_\infty
=
\|k-k'\|_\infty
=0,
\]

so

\[
c=c'.
\]

Symmetry follows from symmetry of each sup norm.

For the triangle inequality, let

\[
c_1=(g_1,a_1,k_1),
\quad
c_2=(g_2,a_2,k_2),
\quad
c_3=(g_3,a_3,k_3).
\]

For each component,

\[
w_G\|g_1-g_3\|_\infty
\le
w_G\|g_1-g_2\|_\infty
+
w_G\|g_2-g_3\|_\infty,
\]

and analogously for \(a\) and \(k\).

Taking the maximum over the three component blocks gives

\[
\boxed{
D_w(c_1,c_3)
\le
D_w(c_1,c_2)
+
D_w(c_2,c_3).
}
\]

Therefore \(D_w\) is a metric. \(\square\)

---

# 3. Admissible relabeling group

The fixed-coordinate representation still contains labels: block labels, intervention labels, and the corresponding induced coordinate ordering.

Let

\[
\mathcal H
\]

be a finite group of admissible relabelings acting on the fingerprint space. We require each

\[
h\in\mathcal H
\]

to act isometrically:

\[
\boxed{
D_w(hc,hc')
=
D_w(c,c')
\qquad
\forall c,c'.
}
\]

Coordinate permutations induced by compatible relabelings satisfy this condition because the sup norm is permutation invariant.

Write

\[
[c]
=
\{hc:h\in\mathcal H\}
\]

for the orbit of \(c\).

Define the quotient distance

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}
D_w(c,hc').
}
\]

The minimum exists because \(\mathcal H\) is finite.

---

# 4. Proposition 14B - quotient metric under relabeling

## Statement

If the finite group \(\mathcal H\) acts by isometries of \(D_w\), then

\[
\boxed{
\overline D_w
}
\]

is a metric on the orbit space

\[
\mathcal C/\mathcal H.
\]

In particular,

\[
\overline D_w([c],[c'])=0
\iff
[c]=[c'].
\]

## Proof

### Well-definedness

Choose different representatives

\[
\tilde c=h_0c,
\qquad
\tilde c'=h_1c'.
\]

Then

\[
\min_{h\in\mathcal H}D_w(\tilde c,h\tilde c')
=
\min_{h\in\mathcal H}D_w(h_0c,hh_1c').
\]

By isometry of \(h_0^{-1}\), this equals

\[
\min_{h\in\mathcal H}
D_w(c,h_0^{-1}hh_1c').
\]

Because \(\mathcal H\) is a group, the set

\[
\{h_0^{-1}hh_1:h\in\mathcal H\}
\]

is exactly \(\mathcal H\). Hence the value is independent of the chosen representatives.

### Identity of indiscernibles

If

\[
[c]=[c'],
\]

then some \(h\in\mathcal H\) satisfies

\[
c=hc',
\]

so the quotient distance is zero.

Conversely, if

\[
\overline D_w([c],[c'])=0,
\]

then, because the minimum is attained, some \(h\in\mathcal H\) satisfies

\[
D_w(c,hc')=0.
\]

Since \(D_w\) is a metric,

\[
c=hc',
\]

and therefore

\[
[c]=[c'].
\]

### Symmetry

If \(h\) is admissible, so is \(h^{-1}\). Using symmetry and isometry,

\[
D_w(c,hc')
=
D_w(c',h^{-1}c).
\]

Taking minima gives symmetry of \(\overline D_w\).

### Triangle inequality

Let \(h_1\) attain the minimum between \([c_1]\) and \([c_2]\), and let \(h_2\) attain the minimum between \([c_2]\) and \([c_3]\). Then

\[
\begin{aligned}
\overline D_w([c_1],[c_3])
&\le
D_w(c_1,h_1h_2c_3)\\
&\le
D_w(c_1,h_1c_2)
+
D_w(h_1c_2,h_1h_2c_3)\\
&=
D_w(c_1,h_1c_2)
+
D_w(c_2,h_2c_3)\\
&=
\overline D_w([c_1],[c_2])
+
\overline D_w([c_2],[c_3]).
\end{aligned}
\]

Thus \(\overline D_w\) is a metric on the orbit space. \(\square\)

---

# 5. Temporal path variation

Let

\[
[c_0],[c_1],\ldots,[c_T]
\]

be a sequence of representation-invariant causal-structure states measured at physical times

\[
t_0<t_1<\cdots<t_T.
\]

Define the cumulative temporal variation

\[
\boxed{
V_{0:T}
=
\sum_{r=0}^{T-1}
\overline D_w([c_r],[c_{r+1}]).
}
\]

For a subinterval \(s<t\), define

\[
V_{s:t}
=
\sum_{r=s}^{t-1}
\overline D_w([c_r],[c_{r+1}]).
\]

A local continuation scale may also be declared by

\[
\boxed{
J_{0:T}
=
\max_{0\le r<T}
\overline D_w([c_r],[c_{r+1}]).
}
\]

A path with small \(J_{0:T}\) changes gradually at the declared sampling scale; a large value identifies at least one abrupt structural transition.

---

# 6. Proposition 14C - endpoint bound

For every

\[
0\le s<t\le T,
\]

\[
\boxed{
\overline D_w([c_s],[c_t])
\le
V_{s:t}.
}
\]

## Proof

Apply the triangle inequality for \(\overline D_w\) repeatedly along the path:

\[
\begin{aligned}
\overline D_w([c_s],[c_t])
&\le
\overline D_w([c_s],[c_{s+1}])
+
\cdots
+
\overline D_w([c_{t-1}],[c_t])\\
&=
V_{s:t}.
\end{aligned}
\]

\(\square\)

This result turns temporal continuation into a path property rather than an endpoint comparison.

---

# 7. Proposition 14D - invariance under time-dependent relabeling

Let

\[
h_0,h_1,\ldots,h_T\in\mathcal H
\]

be arbitrary admissible relabelings, possibly different at every time point.

Define

\[
\tilde c_t=h_tc_t.
\]

Then

\[
\boxed{
V_{0:T}(\tilde c_0,\ldots,\tilde c_T)
=
V_{0:T}(c_0,\ldots,c_T),
}
\]

and likewise

\[
\boxed{
J_{0:T}(\tilde c_0,\ldots,\tilde c_T)
=
J_{0:T}(c_0,\ldots,c_T).
}
\]

## Proof

Each term is a distance between equivalence classes. Since

\[
[h_tc_t]=[c_t],
\]

for every \(t\), every adjacent quotient distance is unchanged. Therefore both the sum and maximum are unchanged. \(\square\)

This prevents arbitrary changes of physical labels from appearing as false dynamical transitions.

---

# 8. Proposition 14E - endpoint equality does not certify continuation

Endpoint agreement alone is insufficient to characterize the intervening physical trajectory.

Let \([a]\ne[b]\). Consider

\[
[c_0]=[a],
\qquad
[c_1]=[b],
\qquad
[c_2]=[a].
\]

Then

\[
\boxed{
\overline D_w([c_0],[c_2])=0,
}
\]

but

\[
\boxed{
V_{0:2}
=
2\overline D_w([a],[b])
>0.
}
\]

Thus a system can return to the same endpoint signature after a substantial intermediate excursion. Temporal organization must therefore be studied as a path, not only through start/end similarity.

---

# 9. Continuation certificates

The theorem suggests two physically interpretable declarations.

## Local continuation certificate

For declared tolerance \(\rho>0\), call the sampled path locally \(\rho\)-continuous when

\[
\boxed{
J_{0:T}\le\rho.
}
\]

This states that no adjacent sampled transition exceeds the declared causal-structure scale.

## Total-variation certificate

For declared budget \(R>0\), call the path globally \(R\)-bounded when

\[
\boxed{
V_{0:T}\le R.
}
\]

This controls cumulative structural variation over the complete interval.

Neither threshold is universal. A physically meaningful \(\rho\) or \(R\) must come from the measurement scale, uncertainty model, sampling cadence, and scientific comparison being performed.

---

# 10. Relation to the companion observer project

The companion Spatiotemporal Observer Mathematics repository identifies a moving physical subsystem

\[
\mathcal W=(S_0,\ldots,S_{T-1}).
\]

Proposition 14 supplies a complementary object: once an intervention-resolved causal structure is attached to successive physical world-tube states, the quotient metric provides a way to ask whether the causal organization evolves continuously after representation alignment.

This creates the future interface

\[
\boxed{
\text{world-tube continuation}
+
\text{causal-structure continuation}
\longrightarrow
\text{persistent physical process candidate}.
}
\]

The combined statement remains physical. A further bridge principle would still be required to connect persistent physical process structure to experiential continuity.

---

# 11. Physical and mathematical lineage

The metric construction uses standard metric-space and quotient-by-isometry ideas; a general reference is:

- Dmitri Burago, Yuri Burago, and Sergei Ivanov, *A Course in Metric Geometry*, Graduate Studies in Mathematics 33, American Mathematical Society, 2001. DOI: 10.1090/gsm/033.

The use of interventions in explicitly time-evolving dynamical systems is consistent with:

- Jonas Peters, Stefan Bauer, and Niklas Pfister, "Causal models for dynamical systems," arXiv:2001.06208 (2020).

The physical motivation for treating consciousness-related biological states as dynamical regimes rather than static network snapshots is supported by anesthesia research, including:

- George A. Mashour, "Anesthesia and the neurobiology of consciousness," *Neuron* 112(10) (2024): 1553-1567. DOI: 10.1016/j.neuron.2024.03.002.

These sources provide mathematical or physical context. The specific weighted causal-structure quotient metric, path-variation construction, and its use within this bridge program are developed here.

---

# 12. Scope and current limitations

Proposition 14 establishes temporal comparison on a declared finite-dimensional fingerprint representation with a finite group of admissible isometric relabelings.

The present result does not yet solve:

1. changing numbers of physical blocks;
2. births, deaths, splits, or merges of subsystem components;
3. continuous or infinite relabeling groups;
4. statistical uncertainty in each time-indexed fingerprint;
5. irregular-time normalization of structural variation;
6. whether physical temporal continuity corresponds to experiential continuity.

These are extension points rather than hidden assumptions.

The next mathematically natural steps are to combine the temporal metric with finite-data uncertainty and then address composition, splitting, and merging.

---

# 13. Reproducibility map

| Artifact | Location |
| --- | --- |
| theorem and proof | this document |
| implementation | `src/consciousness_bridge/temporal_causal_structure.py` |
| claim-level tests | `tests/test_temporal_causal_structure.py` |
| visual explanation | `docs/figures/p14_temporal_continuation.svg` |
| theorem roadmap | `docs/theorem_roadmap.md` |
| equation provenance | `docs/equation_and_citation_map.md` |
| bibliography | `docs/literature_map.md`, `references.bib` |
