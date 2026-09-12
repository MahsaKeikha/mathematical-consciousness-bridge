# Proposition 83: Exact Signed Cylinder-Contrast Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem candidate on the P83 branch.** P83 strengthens the P82 continuous P75 model-distance certificate by testing exact signed contrasts between pairs of non-nested observed cylinder events.

P83 does not change the declared P75 target-measurement family, the full-law $L_\infty$ metric, the P79 finite-sample rejection gate, or the P78 mesh-width upper certificate. It changes only the lower-bound relaxation used to certify separation from a P75 parameter box.

The result is scientific model certification, not a consciousness ontology. It does not identify the P75 latent state with consciousness, does not turn non-rejection into model validation, and does not close the physical-to-experiential bridge.

---

## 1. Motivation

P81 tests each of the 80 nonempty cylinder events separately. P82 adds 256 exact nested residual events of the form $A\setminus B$.

Those results can still discard compatibility information because two event probabilities may each lie inside their own exact parameter-box intervals while **no single parameter vector can realize the observed difference between them**.

P83 retains that shared-parameter information with signed contrasts

\[
\phi_{A,B}(x)=\mathbf 1_A(x)-\mathbf 1_B(x),
\]

for non-nested cylinder events $A$ and $B$.

The key point is simple: separate interval tests ask whether $\widehat p(A)$ and $\widehat p(B)$ are individually possible. P83 asks whether their **signed combination** is possible under one common P75 parameter vector.

---

## 2. Cylinder events

For nonempty $J\subseteq\{1,2,3,4\}$ and binary assignment $a\in\{0,1\}^{|J|}$, define

\[
C(J,a)
=
\{x\in\{0,1\}^4:x_j=a_j\text{ for every }j\in J\}.
\]

There are

\[
\sum_{k=1}^4 {4\choose k}2^k
=3^4-1
=80
\]

nonempty cylinders.

Let

\[
A=C(J,a),\qquad B=C(K,b)
\]

be two distinct cylinders.

P83 calls the pair **non-nested** when neither $A\subset B$ nor $B\subset A$.

---

## 3. Signed cylinder contrast

Define

\[
\boxed{
\phi_{A,B}(x)=\mathbf 1_A(x)-\mathbf 1_B(x).
}
\]

Its coefficients take values in $\{-1,0,1\}$.

For any two probability laws $p$ and $q$ on the sixteen observed cells,

\[
\begin{aligned}
\left|E_p\phi_{A,B}-E_q\phi_{A,B}\right|
&=
\left|
\sum_x \phi_{A,B}(x)(p_x-q_x)
\right|\\
&\le
\sum_x|\phi_{A,B}(x)|\,|p_x-q_x|\\
&\le
\|p-q\|_\infty
\sum_x|\phi_{A,B}(x)|.
\end{aligned}
\]

Therefore

\[
\boxed{
\|p-q\|_\infty
\ge
\frac{
\left|E_p\phi_{A,B}-E_q\phi_{A,B}\right|
}{\|\phi_{A,B}\|_1}.
}
\]

Because the contrast is a difference of two indicators,

\[
\boxed{
\|\phi_{A,B}\|_1
=|A\triangle B|,
}
\]

where $A\triangle B$ is the symmetric difference.

If $A$ and $B$ are disjoint, this reduces to $|A|+|B|$.

---

## 4. P75 branchwise signed contrast

The P75 model has a binary latent branch $s\in\{-,+\}$ and four conditionally independent binary observed views.

Inside one branch,

\[
P_s(C(J,a))
=
\prod_{j\in J} f(q_{j,s},a_j),
\]

with

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

For the signed pair define

\[
g_s(q_s)
=
P_s(A)-P_s(B).
\]

Each cylinder probability is multi-affine in the response coordinates that it uses. Their difference is therefore also multi-affine in the union of the response coordinates appearing in $A$ or $B$.

Since there are only four views, $g_s$ depends on at most four branch-specific coordinates.

---

## 5. Exact branchwise interval by vertex extremization

Let $B_\theta$ be an axis-aligned rational P75 parameter box.

A multi-affine scalar function on a hyperrectangle reaches its minimum and maximum at hyperrectangle vertices. Therefore

\[
\boxed{
\ell_s(A,B;B_\theta)
=
\min_{v\in V_s(A,B;B_\theta)} g_s(v),
}
\]

and

\[
\boxed{
u_s(A,B;B_\theta)
=
\max_{v\in V_s(A,B;B_\theta)} g_s(v),
}
\]

where $V_s(A,B;B_\theta)$ is the endpoint-vertex set for the branch response coordinates used by the pair.

At most four coordinates are involved, so each branch requires at most

\[
2^4=16
\]

vertex evaluations.

This is exact endpoint enumeration in rational arithmetic. No floating optimizer is used in the certification path.

---

## 6. Exact latent-mixture interval

Let prevalence satisfy

\[
\pi\in[\pi_L,\pi_U].
\]

The full-model contrast is

\[
E_{q_\theta}\phi_{A,B}
=(1-\pi)g_-(q_-)+\pi g_+(q_+).
\]

The minus-branch and plus-branch response coordinates are disjoint parameter coordinates. Thus, for fixed $\pi$, their extrema are independently attainable.

Define exact branch intervals

\[
g_-\in[\ell_-,u_-],
\qquad
g_+\in[\ell_+,u_+].
\]

Then the exact lower envelope at fixed prevalence is

\[
L(\pi)=(1-\pi)\ell_-+\pi\ell_+,
\]

and the exact upper envelope is

\[
U(\pi)=(1-\pi)u_-+\pi u_+.
\]

Both are affine in prevalence, so the exact global endpoints occur at $\pi_L$ or $\pi_U$:

\[
\boxed{
\ell_{A,B}(B_\theta)
=
\min_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)\ell_-+\pi\ell_+\right],
}
\]

\[
\boxed{
u_{A,B}(B_\theta)
=
\max_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)u_-+\pi u_+\right].
}
\]

These endpoints are exact rational numbers whenever the parameter-box endpoints are rational.

---

## 7. Full-law lower bound from one signed pair

The empirical contrast is

\[
\widehat c_{A,B}
=
\widehat p(A)-\widehat p(B).
\]

Every P75 law generated inside $B_\theta$ has signed contrast inside

\[
[\ell_{A,B}(B_\theta),u_{A,B}(B_\theta)].
\]

Combining Section 3 with the exact model interval gives

\[
\boxed{
\|\widehat p-q_\theta\|_\infty
\ge
\frac{
d\!\left(
\widehat c_{A,B},
[\ell_{A,B}(B_\theta),u_{A,B}(B_\theta)]
\right)
}{|A\triangle B|}.
}
\]

This is a valid lower bound for every $\theta$ in the parameter box.

---

## 8. Why P83 excludes nested pairs from the new family

There are ${80\choose2}=3160$ unordered pairs of distinct nonempty cylinders.

If one cylinder is nested in the other, the signed difference is already covered by the existing frontier:

- if the child adds one binary view, the residual is exactly the sibling cylinder and is already a P81 event;
- if the child adds at least two views, the residual is one of the exact P82 nested contrasts.

The number of unordered nested pairs is

\[
\begin{aligned}
N_{\mathrm{nested}}
&={4\choose2}2^2{2\choose1}
+{4\choose3}2^3\left({3\choose1}+{3\choose2}\right)\\
&\quad+{4\choose4}2^4
\left({4\choose1}+{4\choose2}+{4\choose3}\right)\\
&=48+192+224\\
&=464.
\end{aligned}
\]

Therefore the genuinely new P83 family contains

\[
\boxed{
3160-464=2696
}
\]

unordered non-nested signed cylinder pairs.

---

## 9. P83 box certificate

Define

\[
\boxed{
L_{\mathrm{signed}}(B_\theta)
=
\max_{(A,B)\in\mathcal S_{83}}
\frac{
d\!\left(
\widehat c_{A,B},
[\ell_{A,B}(B_\theta),u_{A,B}(B_\theta)]
\right)
}{|A\triangle B|},
}
\]

where $\mathcal S_{83}$ is the fixed family of 2696 unordered non-nested cylinder pairs.

P83 then defines

\[
\boxed{
L_{83}(B_\theta)
=
\max\{L_{82}(B_\theta),L_{\mathrm{signed}}(B_\theta)\}.
}
\]

Hence

\[
\boxed{
L_{83}(B_\theta)
\ge
L_{82}(B_\theta)
\ge
L_{81}(B_\theta)
\ge
L_{80}(B_\theta)
\ge
L_{78}(B_\theta).
}
\]

---

## 10. Proposition 83 theorem

For every admissible P78 parameter box $B_\theta$:

1. every P83 signed-cylinder interval is the exact image interval of its contrast over $B_\theta$;
2. every P83 signed-cylinder lower bound is a rigorous lower bound on full-law $L_\infty$ distance;
3. $L_{83}(B_\theta)$ is a rigorous lower bound on distance from $\widehat p$ to every P75 law generated inside the box;
4. $L_{83}(B_\theta)\ge L_{82}(B_\theta)$;
5. rational empirical probabilities and rational box endpoints produce exact rational interval endpoints and exact rational lower bounds;
6. for every finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{83}(\mathcal B)
:=
\min_{B_\theta\in\mathcal B}L_{83}(B_\theta)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

7. the already-proved P78 mesh-width upper certificate remains valid and is retained unchanged;
8. no new convergence-rate theorem is claimed for P83.

---

## 11. Proof

### 11.1 Exactness of the branchwise interval

For one latent branch, $P_s(A)$ and $P_s(B)$ are products of affine Bernoulli factors. Their difference is multi-affine in the union of the response coordinates used by the two cylinders.

Fix all but one coordinate. The result is affine in the remaining coordinate, so its extremum over that coordinate interval occurs at an endpoint. Repeating this coordinate by coordinate proves that a global minimum and maximum occur at box vertices. Exhaustive endpoint evaluation therefore gives the exact branchwise interval.

### 11.2 Exactness after latent mixing

The minus and plus branch response coordinates are disjoint, so their branch extrema can be attained independently. At fixed prevalence, the full contrast is nonnegative-affine in the two branch values, hence its extrema use the two branch minima or the two branch maxima respectively.

The resulting lower and upper envelopes are affine in prevalence. Their extrema over the prevalence interval therefore occur at prevalence endpoints. This proves the global interval formulas in Section 6 are exact.

### 11.3 Soundness of the transfer to full-law distance

For every signed coefficient vector $\phi$,

\[
|\langle\phi,\widehat p-q\rangle|
\le
\|\phi\|_1\|\widehat p-q\|_\infty.
\]

For $\phi=\mathbf 1_A-\mathbf 1_B$, the coefficient norm equals $|A\triangle B|$. The model contrast belongs to the exact P83 interval, so distance of the empirical contrast to that interval, divided by $|A\triangle B|$, is a sound full-law lower bound.

### 11.4 Dominance

$L_{\mathrm{signed}}$ is a maximum of sound lower bounds and is therefore sound. P82 is already sound. Their maximum is sound and cannot be smaller than P82.

### 11.5 Exact arithmetic

The implementation uses rational endpoint enumeration, products, additions, subtractions, affine prevalence combinations, finite maxima/minima, interval distance, and division by a positive integer support norm. Every certification quantity is therefore exact under rational input.

---

## 12. Strict exact-rational witness over P82

Consider the P75 box with free prevalence

\[
\pi\in[0,1]
\]

and fixed branch-response vectors

\[
q_-=
\left(
\frac14,
1,
0,
\frac12
\right),
\]

\[
q_+=
\left(
0,
\frac34,
\frac34,
\frac34
\right).
\]

Use the empirical sixteen-cell law, in lexicographic binary order $0000,0001,\ldots,1111$,

\[
\widehat p=
\frac1{64}
(
0,0,0,5,
18,19,1,10,
0,0,0,0,
8,3,0,0
).
\]

The masses sum exactly to one.

The exhaustive exact-rational audit of the complete existing relaxation gives

\[
\boxed{
L_{80}(B_\theta)=L_{81}(B_\theta)=L_{82}(B_\theta)=0.
}
\]

Thus every individual P81 cylinder constraint and every standard P82 nested-residual constraint is compatible with this empirical law on the box.

Now choose the two non-nested singleton cylinders

\[
A=\{1100\},
\qquad
B=\{1101\}.
\]

For the minus branch,

\[
P_-(1100)
=
\frac14\cdot1\cdot1\cdot\frac12
=rac18,
\]

and

\[
P_-(1101)
=
\frac14\cdot1\cdot1\cdot\frac12
=rac18.
\]

For the plus branch, the first observed bit equals one with probability zero, so

\[
P_+(1100)=P_+(1101)=0.
\]

Therefore every model law in the entire witness box satisfies

\[
\boxed{
q(1100)-q(1101)=0.
}
\]

Empirically,

\[
\widehat p(1100)-\widehat p(1101)
=
\frac{8}{64}-\frac{3}{64}
=rac5{64}.
\]

The two singleton events are disjoint, so

\[
|A\triangle B|=2.
\]

Hence

\[
\boxed{
L_{\mathrm{signed}}(B_\theta)
\ge
\frac{5/64}{2}
=rac5{128}.
}
\]

The exhaustive standard P83 search finds this pair as the unique strongest signed-cylinder witness on the box, so

\[
\boxed{
L_{83}(B_\theta)=\frac5{128}>0=L_{82}(B_\theta).
}
\]

This proves strict dominance over P82 on a concrete exact-rational example.

---

## 13. The strict witness is tight

P83 does more than improve the relaxation on the witness. It certifies the exact distance to the witness-box model family.

Choose the admissible prevalence

\[
\pi=\frac5{16}.
\]

Using the fixed response vectors above gives an explicit P75 law $q_{5/16}$ with

\[
\boxed{
\|\widehat p-q_{5/16}\|_\infty
=rac5{128}.
}
\]

P83 already proves the matching lower bound

\[
\|\widehat p-q_\theta\|_\infty\ge\frac5{128}
\]

for every admissible parameter vector in the witness box. Therefore

\[
\boxed{
\inf_{\theta\in B_\theta}
\|\widehat p-q_\theta\|_\infty
=rac5{128}.
}
\]

Thus the P83 strict witness is an **exactly closed model-distance example**: P82 returns zero while P83 reaches the true box-model distance.

---

## 14. Global branch-and-bound handoff

P83 can replace the P82 box lower bound inside the same certified branch-and-bound framework.

Active boxes continue to partition the complete nine-dimensional P75 parameter cube. The global lower bound is the minimum active P83 box bound.

For the upper direction, P83 deliberately keeps the established guarantees:

- every explicit P75 parameter vector gives a valid model-distance upper witness;
- the P78 mesh-width upper certificate remains valid for the same underlying distance problem.

P83 therefore strengthens the lower direction without silently claiming a new convergence theorem.

---

## 15. P79 finite-data rejection handoff

Let $\overline\varepsilon_{79}$ be the exact-rational upper certificate for the P77 cellwise sampling radius. Then

\[
\boxed{
L_{83}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\mathcal C_n(\widehat p)\cap\mathcal M_{4,2}=\varnothing.
}
\]

This remains a one-sided rejection rule.

If the strict inequality fails, the scientifically correct conclusion is **inconclusive under the current data, model family, partition, and certificate**. It is not model validation.

---

## 16. Executable implementation and audit

Primary implementation:

`src/consciousness_bridge/signed_cylinder_contrast_separation.py`

Primary regression tests:

`tests/test_signed_cylinder_contrast_separation.py`

The tests enforce:

- the exact count of 2696 new non-nested pairs;
- exact agreement between the closed-form interval routine and exhaustive full parameter-box vertex evaluation on a rational audit box;
- the symmetric-difference $L_1$ normalization;
- exact dominance $L_{83}\ge L_{82}$;
- the strict witness $L_{80}=L_{81}=L_{82}=0<L_{83}=5/128$;
- the matching explicit upper witness at $\pi=5/16$;
- exact-rational branch-and-bound bracket invariants;
- the scientific boundary language.

---

## 17. What P83 proves, and what it does not

P83 proves that exact signed combinations of separately observable cylinder events can retain common-parameter compatibility information that is lost by the P81/P82 one-event relaxation.

It does **not** prove that the P75 latent variable is consciousness.

It does **not** prove that a non-rejected P75 model is true.

It does **not** establish that consciousness is a scalar, state of matter, quantum variable, field, or additional spacetime dimension.

It does **not** close the physical-to-experiential bridge.

Its role is narrower and scientifically useful: it makes one declared continuous target-measurement model harder to falsely regard as compatible with data merely because many event constraints pass separately.
