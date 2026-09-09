# Proposition 12: IRCG component insufficiency and minimal-feature audit

## Why this theorem is necessary

Proposition 11 introduces the Intervention-Resolved Causal Geometry signature

\[
F_{\mathrm{IRCG}}(p)
=
[\mathfrak C_p]_{\cong},
\]

with three major structural components:

\[
\mathcal G_p
\quad\text{response geometry},
\qquad
\mathcal A_p
\quad\text{directed interventional influence},
\qquad
\mathcal K_p
\quad\text{partition irreducibility}.
\]

A natural temptation is to simplify this object immediately to one component or one scalar. Proposition 12 tests that temptation before any consciousness interpretation is attached to the candidate.

The central result is:

\[
\boxed{
\mathcal G_p,\ \mathcal A_p,\ \mathcal K_p
\text{ are each individually insufficient to reconstruct full IRCG.}
}
\]

The proof is constructive. Each insufficiency result is demonstrated by finite, explicitly realizable intervention-conditioned probability laws.

This is a **physical-signature minimality result**, not a consciousness theorem.

---

# 1. General projection-collision theorem

Let

\[
F:X\to Z
\]

be a target signature and let

\[
H:X\to W
\]

be a proposed compressed feature.

## Proposition 12A - projection collision no-go theorem

If there exist \(x,x'\in X\) such that

\[
\boxed{
H(x)=H(x')
\qquad\text{but}\qquad
F(x)\ne F(x'),
}
\]

then there is no map

\[
g:W\to Z
\]

satisfying

\[
F=g\circ H
\]

on the declared domain.

## Proof

Assume for contradiction that \(F=g\circ H\). If \(H(x)=H(x')\), then

\[
F(x)=g(H(x))=g(H(x'))=F(x'),
\]

contradicting \(F(x)\ne F(x')\).

\[
\boxed{\text{QED}}
\]

This is the Proposition 5 factorization criterion applied internally to IRCG compression.

---

# 2. Response geometry alone is not complete

Consider two two-block physical systems at one delay \(\tau\), each with interventions \(u_0,u_1\).

Use the outcome alphabet

\[
\{00,01,10,11\}.
\]

## System \(p_C\): correlated response pair

\[
P_C^{u_0}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11},
\]

\[
P_C^{u_1}
=
\tfrac12\delta_{01}+\tfrac12\delta_{10}.
\]

The two response laws have disjoint support, hence

\[
\boxed{
d_C(u_0,u_1)=1.}
\]

For the partition

\[
\pi=\{\{1\},\{2\}\},
\]

each marginal is uniform. The product of marginals is therefore uniform on the four joint outcomes. Consequently,

\[
\boxed{
\kappa_C^\tau(\pi)=\frac12.
}
\]

## System \(p_P\): product response pair

\[
P_P^{u_0}
=
\tfrac12\delta_{00}+\tfrac12\delta_{01},
\]

\[
P_P^{u_1}
=
\tfrac12\delta_{10}+\tfrac12\delta_{11}.
\]

Again the two intervention-conditioned laws have disjoint support:

\[
\boxed{
d_P(u_0,u_1)=1.}
\]

Thus the complete one-delay response geometries are identical:

\[
\boxed{
\mathcal G_C=\mathcal G_P.
}
\]

However, both laws in \(p_P\) factor exactly across the two blocks, so

\[
\boxed{
\kappa_P^\tau(\pi)=0.
}
\]

Therefore

\[
\mathcal G_C=\mathcal G_P
\qquad\text{but}\qquad
F_{\mathrm{IRCG}}(p_C)
e F_{\mathrm{IRCG}}(p_P).
\]

By Proposition 12A:

\[
\boxed{
F_{\mathrm{IRCG}}
\text{ cannot factor through response geometry alone.}
}
\]

### Physical interpretation

A metric describing how distinguishable whole-system responses are under different perturbations does not reveal whether those joint responses are internally factorized or irreducible.

---

# 3. Partition irreducibility alone is not complete

Consider two systems whose intervention-conditioned responses all factor exactly across blocks.

## System \(p_D\): differentiated product responses

\[
P_D^{u_0}=\delta_{00},
\qquad
P_D^{u_1}=\delta_{11}.
\]

Both are product distributions, hence

\[
\kappa_D^\tau(\pi)=0
\]

for the two-block partition. But

\[
\boxed{
d_D(u_0,u_1)=1.}
\]

## System \(p_S\): stereotyped product responses

\[
P_S^{u_0}=\delta_{00},
\qquad
P_S^{u_1}=\delta_{00}.
\]

Again

\[
\kappa_S^\tau(\pi)=0,
\]

but now

\[
\boxed{
d_S(u_0,u_1)=0.}
\]

Thus

\[
\boxed{
\mathcal K_D=\mathcal K_S
\qquad\text{but}\qquad
\mathcal G_D\ne\mathcal G_S.
}
\]

Therefore

\[
\boxed{
F_{\mathrm{IRCG}}
\text{ cannot factor through the partition-irredundancy landscape alone.}
}
\]

### Physical interpretation

Exact factorization information says whether responses decompose across a declared partition. It does not say whether the system has a rich family of distinct causal responses or produces essentially the same response to every intervention.

---

# 4. Directed influence alone is not complete

Now compare two systems whose single-block marginals are identical under all tested interventions.

Let

\[
P_R^{u_0}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11},
\]

\[
P_R^{u_1}
=
\tfrac12\delta_{01}+\tfrac12\delta_{10}.
\]

Every one-block marginal is uniform under both interventions. Therefore any matched source-pair influence defined from target marginals satisfies

\[
\boxed{
A_{ij}^R(\tau)=0
}
\]

for all tested source-target pairs.

Now define

\[
P_I^{u_0}
=
P_I^{u_1}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11}.
\]

Again every single-block marginal is uniform, so

\[
\boxed{
A_{ij}^I(\tau)=0.
}
\]

Hence

\[
\boxed{
\mathcal A_R=\mathcal A_I.
}
\]

But their response geometries differ maximally:

\[
d_R(u_0,u_1)=1,
\qquad
d_I(u_0,u_1)=0.
\]

Thus

\[
\boxed{
F_{\mathrm{IRCG}}
\text{ cannot factor through the directed-influence tensor alone.}
}
\]

### Physical interpretation

Marginal perturbational influence can miss changes that live purely in joint dependence structure. Two systems can have the same single-block causal marginals while having radically different whole-system response geometry.

---

# 5. Scalar response diameter is not complete

Even the response-geometry component itself can be over-compressed.

Consider three interventions \(u_0,u_1,u_2\).

For system \(p_A\), let

\[
P_A^{u_0}=\delta_{00},
\qquad
P_A^{u_1}=\delta_{11},
\qquad
P_A^{u_2}=\delta_{00}.
\]

Its pairwise geometry is

\[
(d_{01},d_{02},d_{12})=(1,0,1).
\]

For system \(p_B\), let

\[
P_B^{u_0}=\delta_{00},
\qquad
P_B^{u_1}=\delta_{11},
\qquad
P_B^{u_2}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11}.
\]

Its pairwise geometry is

\[
(d_{01},d_{02},d_{12})=(1,\tfrac12,\tfrac12).
\]

Both have response diameter

\[
\boxed{
\operatorname{Diam}=1,
}
\]

but their geometries are not equal.

Therefore

\[
\boxed{
\operatorname{Diam}_p
\text{ is not sufficient to reconstruct }\mathcal G_p.
}
\]

A maximum pairwise response difference is consequently too coarse to serve as the complete IRCG descriptor.

---

# 6. Scalar minimum-partition irreducibility is not complete

For the correlated systems

\[
P_R^{u_0}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11},
\qquad
P_R^{u_1}
=
\tfrac12\delta_{01}+\tfrac12\delta_{10},
\]

and

\[
P_I^{u_0}=P_I^{u_1}
=
\tfrac12\delta_{00}+\tfrac12\delta_{11},
\]

the two-block partition gives

\[
\boxed{
\kappa_R^*=\kappa_I^*=\frac12.
}
\]

Yet

\[
d_R(u_0,u_1)=1,
\qquad
d_I(u_0,u_1)=0.
\]

Thus the same scalar irreducibility value can coexist with different intervention-response geometry.

\[
\boxed{
\kappa_p^*
\text{ is not a complete IRCG statistic.}
}
\]

---

# 7. Boolean recurrence is not complete

Let two directed influence matrices be

\[
A^{(1)}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
A^{(2)}
=
\begin{pmatrix}
0&0.2\\
0.2&0
\end{pmatrix}.
\]

Both contain a directed two-cycle. Therefore the Boolean predicate

\[
R(A)=\mathbf 1\{A\text{ contains a directed cycle}\}
\]

gives

\[
R(A^{(1)})=R(A^{(2)})=1.
\]

But

\[
A^{(1)}\ne A^{(2)}.
\]

Therefore recurrence presence alone cannot reconstruct the directed influence tensor.

\[
\boxed{
\text{cycle/no-cycle is a structural certificate, not a complete causal signature.}
}
\]

---

# 8. Proposition 12B - single-component insufficiency theorem for IRCG

On the explicit finite domain containing the constructions above, none of the projections

\[
F_G(p)=\mathcal G_p,
\qquad
F_A(p)=\mathcal A_p,
\qquad
F_K(p)=\mathcal K_p
\]

is sufficient to reconstruct

\[
F_{\mathrm{IRCG}}(p).
\]

Equivalently, there exist no maps \(g_G,g_A,g_K\) satisfying all three identities

\[
F_{\mathrm{IRCG}}=g_G\circ F_G,
\]

\[
F_{\mathrm{IRCG}}=g_A\circ F_A,
\]

\[
F_{\mathrm{IRCG}}=g_K\circ F_K
\]

on that domain.

## Proof

Sections 2-4 provide an explicit collision for each projection. Proposition 12A then rules out the corresponding factorization.

\[
\boxed{\text{QED}}
\]

---

# 9. What this rules out

Proposition 12 rules out the following shortcuts as complete descriptions of Candidate A:

| Compression | Exact failure |
| --- | --- |
| response geometry only | cannot determine partition irreducibility |
| directed influence only | can miss joint-dependence changes invisible in marginals |
| partition irreducibility only | cannot determine perturbational differentiation |
| response diameter | different geometries can share one maximum distance |
| minimum irreducibility scalar | different geometries can share one irreducibility value |
| recurrence yes/no | different directed causal structures can share cycle status |

This does **not** establish that the full IRCG object is minimal. Pairwise combinations of components may still contain redundancy, and the complete isomorphism class may itself contain more detail than any eventual bridge requires.

---

# 10. Scientific consequence

The theorem changes the design philosophy of the project.

A future consciousness bridge should not begin by selecting one intuitively appealing number such as:

- complexity;
- integration;
- recurrence;
- broadcast strength;
- controllability;
- entropy;
- criticality.

Instead, the project first preserves a sufficiently rich physical causal object and then asks which information can be removed **without creating counterexample collisions**.

The criterion is mathematical:

\[
\boxed{
H(p)=H(p')
\Longrightarrow
F_{\mathrm{target}}(p)=F_{\mathrm{target}}(p')
}
\]

must hold before \(H\) can be called sufficient for the declared target.

For IRCG, Proposition 12 shows that several obvious compressions fail this criterion already at the purely physical level.

---

# 11. Next frontier

The next audit should test **pairwise component combinations**:

\[
(\mathcal G,\mathcal A),
\qquad
(\mathcal G,\mathcal K),
\qquad
(\mathcal A,\mathcal K),
\]

and determine whether any pair reconstructs the third component on scientifically relevant model classes.

A stronger future result would identify a mathematically minimal invariant sufficient to reconstruct IRCG on a declared class of causal systems.

Only after that physical minimality problem is understood should the program test whether the surviving physical invariant is sufficient or complete for a physical-to-experiential bridge.
