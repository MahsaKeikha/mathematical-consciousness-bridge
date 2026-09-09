# Proposition 21 - Physical-Descriptor Refinement and Residual Persistence

## Status

**Proved descriptor-refinement theorem for deterministic nested physical descriptors and finite stochastic variables.**

![P21 descriptor refinement and residual persistence](figures/p21_descriptor_refinement_residual_persistence.svg)

**P21 theorem map.** A residual against one physical descriptor is not treated as an ontological conclusion. The descriptor is refined, unresolved deterministic collisions can only disappear, and the stochastic residual decreases by exactly the target-relevant information supplied by the refinement.

P21 addresses the principal omitted-physics objection left open by [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) and its finite-sample continuation in [Proposition 20](proposition_20_finite_sample_residual_certification.md):

> if a residual is observed relative to a declared descriptor \(T\), what happens when the physical description is made strictly richer?

The answer is exact. For nested deterministic physical descriptors, residual information is monotone under refinement, and the decrease has a precise conditional-mutual-information decomposition.

---

# 1. Nested physical descriptors

Let \(\Omega\) denote the sampled physical state and let

\[
T_c:\Omega\to\mathcal T_c,
\qquad
T_f:\Omega\to\mathcal T_f
\]

be two declared deterministic physical descriptors.

We say that \(T_f\) **refines** \(T_c\) when there exists a deterministic map

\[
c:\mathcal T_f\to\mathcal T_c
\]

such that

\[
\boxed{T_c=c\circ T_f.}
\]

Equivalently,

\[
\boxed{
T_f(\omega)=T_f(\omega')
\Longrightarrow
T_c(\omega)=T_c(\omega').
}
\]

Thus every fine fiber lies inside one coarse fiber. Refinement adds physical detail without changing the underlying sampled state \(\Omega\).

Let \(E\) be an independently declared target variable. P21 does not assume that \(E\) is consciousness, nor that any particular descriptor is physically complete.

---

# 2. Deterministic collision monotonicity

For a descriptor \(T\), define the unresolved target-collision set on a finite audit domain by

\[
\boxed{
\mathcal C(T,E)
=
\left\{
(\omega,\omega'):
T(\omega)=T(\omega'),\;
E(\omega)\ne E(\omega')
\right\}.
}
\]

A nonempty collision set is exactly a deterministic no-factorization witness of the type used in P19.

## Proposition 21A - refinement cannot create unresolved target collisions

If

\[
T_c=c\circ T_f,
\]

then

\[
\boxed{
\mathcal C(T_f,E)
\subseteq
\mathcal C(T_c,E).
}
\]

### Proof

Take any

\[
(\omega,\omega')\in\mathcal C(T_f,E).
\]

Then

\[
T_f(\omega)=T_f(\omega')
\]

and

\[
E(\omega)\ne E(\omega').
\]

Since \(T_c=c\circ T_f\), equality of the fine descriptor implies

\[
T_c(\omega)=T_c(\omega').
\]

Therefore

\[
(\omega,\omega')\in\mathcal C(T_c,E).
\]

Hence

\[
\mathcal C(T_f,E)\subseteq\mathcal C(T_c,E).
\qquad\square
\]

## Corollary

If \(E\) factors through the coarse descriptor,

\[
E=B_c\circ T_c,
\]

then it also factors through every refinement:

\[
\boxed{
E=(B_c\circ c)\circ T_f.
}
\]

The converse does not hold. A finer physical descriptor can remove collisions that are unavoidable at a coarser level.

---

# 3. Stochastic residual associated with a descriptor

For finite stochastic variables define the P19 residual

\[
\boxed{
R(T)
:=
I(E;\Omega\mid T).
}
\]

The screening-off condition is

\[
R(T)=0.
\]

A positive value means that, conditional on the declared descriptor \(T\), the sampled physical state \(\Omega\) still contains information about \(E\).

The essential question is whether that residual disappears when \(T\) is refined.

---

# 4. P21 stochastic refinement theorem

Assume

\[
T_f=f(\Omega)
\]

and

\[
T_c=c(T_f).
\]

Then

\[
\boxed{
I(E;\Omega\mid T_c)
=
I(E;T_f\mid T_c)
+
I(E;\Omega\mid T_f).
}
\]

Equivalently,

\[
\boxed{
R(T_c)-R(T_f)
=
I(E;T_f\mid T_c)
\ge0.
}
\]

Therefore

\[
\boxed{
R(T_f)\le R(T_c).
}
\]

## Proof

Because \(T_f\) is a deterministic function of \(\Omega\), adjoining \(T_f\) to \(\Omega\) does not add information beyond \(\Omega\). Hence

\[
I(E;\Omega\mid T_c)
=
I(E;\Omega,T_f\mid T_c).
\]

Apply the conditional-mutual-information chain rule:

\[
I(E;\Omega,T_f\mid T_c)
=
I(E;T_f\mid T_c)
+
I(E;\Omega\mid T_f,T_c).
\]

Because \(T_c\) is a deterministic function of \(T_f\), conditioning on \((T_f,T_c)\) is equivalent to conditioning on \(T_f\). Therefore

\[
I(E;\Omega\mid T_f,T_c)
=
I(E;\Omega\mid T_f).
\]

Combining the three identities gives

\[
I(E;\Omega\mid T_c)
=
I(E;T_f\mid T_c)
+
I(E;\Omega\mid T_f).
\]

Conditional mutual information is nonnegative, so

\[
R(T_f)\le R(T_c).
\qquad\square
\]

The information-theoretic identities are standard; see [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006). The use of the identity as a descriptor-refinement audit in this bridge program is the repository construction.

---

# 5. Exact meaning of the residual decrease

Define the **refinement capture**

\[
\boxed{
G(T_c\to T_f)
:=
I(E;T_f\mid T_c).
}
\]

Then P21 states

\[
\boxed{
R(T_f)=R(T_c)-G(T_c\to T_f).
}
\]

This separates two questions that should not be conflated:

1. how much target-relevant information the added physical detail captures;
2. how much target-relevant residual remains after that refinement.

Three regimes follow immediately.

### Complete removal at the refined level

If

\[
R(T_f)=0,
\]

then

\[
\boxed{
R(T_c)=G(T_c\to T_f).
}
\]

The entire coarse residual is explained by information present in the finer physical descriptor.

### Residual plateau

If

\[
G(T_c\to T_f)=0,
\]

then

\[
\boxed{
R(T_f)=R(T_c).
}
\]

The added physical variables carry no additional information about \(E\) once \(T_c\) is known. A plateau does **not** prove that the descriptor is complete; it only shows that this particular refinement did not reduce the residual.

### Partial capture with persistence

If

\[
0<G(T_c\to T_f)<R(T_c),
\]

then

\[
\boxed{
0<R(T_f)<R(T_c).
}
\]

The refinement explains part, but not all, of the residual.

---

# 6. Nested refinement chain

Consider a nested chain

\[
T_0\preceq T_1\preceq\cdots\preceq T_m,
\]

where each \(T_{k-1}\) is a deterministic function of \(T_k\), and every \(T_k\) is a deterministic function of \(\Omega\).

Define

\[
R_k=I(E;\Omega\mid T_k)
\]

and

\[
G_k=I(E;T_k\mid T_{k-1}),
\qquad k=1,\ldots,m.
\]

Repeated application of P21 gives

\[
\boxed{
R_0\ge R_1\ge\cdots\ge R_m\ge0.
}
\]

More strongly,

\[
\boxed{
R_{k-1}-R_k=G_k
}
\]

for every refinement step, and therefore

\[
\boxed{
R_0-R_m
=
\sum_{k=1}^{m}G_k.
}
\]

The residual decrease telescopes exactly into the target-relevant information supplied by the successive physical refinements.

For an infinite nested chain, monotonicity and nonnegativity imply that

\[
\boxed{
R_\infty
:=
\lim_{k\to\infty}R_k
=
\inf_k R_k
\ge0
}
\]

whenever the stochastic variables and conditional information are well defined.

A positive limiting residual is meaningful only relative to a scientifically justified claim that the refinement family is physically exhaustive. P21 does not supply that completeness claim.

---

# 7. Omitted-physics control protocol

P19 asks whether a declared physical descriptor is sufficient.

P20 asks whether a positive stochastic residual can be certified from finite data.

P21 adds the required omitted-physics audit:

\[
\boxed{
T_0
\preceq
T_1
\preceq
\cdots
\preceq
T_m
\quad\Longrightarrow\quad
R_0
\ge
R_1
\ge
\cdots
\ge
R_m.
}
\]

A scientifically serious residual claim should therefore report at least:

- the exact variables included in every descriptor level;
- the refinement map or observed refinement witness;
- \(R_k\) at every level;
- \(G_k\), the target-relevant information captured by each refinement;
- the finite-sample uncertainty at each tested level;
- the stopping rule used to decide that additional physically motivated variables have been exhausted.

If P20 certificates are applied simultaneously across multiple levels, the confidence accounting must be adjusted for the family of tests. P21 does not license reusing a single \(1-\alpha\) guarantee as if it covered an arbitrary number of adaptive refinements.

---

# 8. Critical boundary: refinement is not a proof of nonphysicality

P21 deliberately blocks a common overinterpretation.

Suppose

\[
R(T_m)>0
\]

for the finest descriptor currently measured. The correct conclusion is:

> the finest **declared and measured** descriptor has not screened off the target under the stated model.

The result does not establish that no richer physical descriptor exists.

In particular, if a refinement chain reaches the identity descriptor

\[
T_m=\Omega,
\]

then

\[
\boxed{
I(E;\Omega\mid\Omega)=0
}
\]

by definition. Thus conditional screening-off cannot, by itself, prove that a target lies outside physics. Its scientific role is to test sufficiency of explicitly declared physical summaries and to quantify exactly what additional physical detail explains.

This boundary is central to the repository's interpretation policy.

---

# 9. Deterministic and stochastic pictures agree structurally

The deterministic theorem says

\[
\boxed{
\mathcal C(T_f,E)
\subseteq
\mathcal C(T_c,E).
}
\]

The stochastic theorem says

\[
\boxed{
R(T_f)
\le
R(T_c).
}
\]

Both express the same structural principle:

> adding valid physical detail can remove an apparent insufficiency, but it cannot create an insufficiency that was absent at a coarser level.

The deterministic collision count is not itself an information measure, and the stochastic residual is not itself an ontological measure. They are complementary sufficiency diagnostics.

---

# 10. Executable audit

The implementation is

[`descriptor_refinement_residual.py`](../src/consciousness_bridge/descriptor_refinement_residual.py).

It provides:

- explicit refinement-violation witnesses;
- deterministic unresolved target-collision sets;
- collision-set monotonicity checks;
- exact pairwise residual decomposition;
- nested residual trajectories;
- exact telescoping checks across refinement chains.

Regression tests are in

[`test_descriptor_refinement_residual.py`](../tests/test_descriptor_refinement_residual.py).

The executable code checks the theorem identities numerically; it does not replace the mathematical proof.

---

# 11. Relation to P19 and P20

The sequence is now

\[
\boxed{
\begin{aligned}
\text{P19: }&\text{What would physical sufficiency mean at the population level?}\\
\text{P20: }&\text{Can a positive residual be certified from finite data?}\\
\text{P21: }&\text{Does the residual survive systematic physical refinement?}
\end{aligned}
}
\]

This is a stronger scientific sequence than interpreting a single residual in isolation.

A future bridge claim would still require an independently justified target space, a defensible physical-completeness argument, estimator-specific empirical validation, and adversarial alternative explanations.

---

# 12. Research boundary

P21 proves a theorem about nested physical descriptions and residual information.

It does **not** prove:

- that consciousness is a new dimension;
- that consciousness is nonphysical;
- that any current physical descriptor is complete;
- that a residual cannot be explained by unmeasured variables, selection effects, model misspecification, or measurement error;
- that conditional mutual information is a measure of consciousness.

The theorem instead makes omitted-physics reasoning explicit and falsifiable: every proposed refinement has a measurable information gain, and every remaining residual has a precisely stated descriptor-relative meaning.
