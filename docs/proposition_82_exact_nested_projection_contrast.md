# Proposition 82: Exact Nested Projection-Contrast Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P82 strengthens the P81 projected-event certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P81 tests each cylinder event separately. P82 adds a finite family of non-cylinder residual events formed from nested cylinders. Its key new step is stronger than simple interval subtraction: for every nested pair, P82 computes the **exact parameter-box range** of the residual event directly from the P75 conditional-independence factorization.

P82 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. Motivation

P81 uses all 80 nonempty cylinder events of four observed binary views. For a cylinder $C(J,a)$ it computes an exact parameter-box interval

\[
\ell_{J,a}(B)\le q(C(J,a))\le u_{J,a}(B)
\]

and converts empirical event mismatch into a full-law $L_\infty$ lower bound by dividing by the number of sixteen-cell outcomes inside the event.

Testing each cylinder separately can still discard useful structure. Suppose one cylinder $B$ is nested inside another cylinder $A$. The difference

\[
\mathbf 1_A-\mathbf 1_B
=\mathbf 1_{A\setminus B}
\]

is itself an observable event. When the child fixes at least two additional views, $A\setminus B$ is generally not a cylinder and therefore is not among the 80 P81 events.

A naive approach would subtract the separate P81 intervals for $A$ and $B$. That is sound but can be loose because the separate extrema need not occur at the same parameter point. P82 instead derives the residual-event interval directly and exactly.

---

## 2. Nested cylinders and residual events

Let

\[
A=C(J,a),\qquad B=C(K,b),
\]

with

\[
\emptyset\ne J\subset K\subseteq\{1,2,3,4\},
\qquad
b|_J=a.
\]

Thus $B\subset A$. Define the added-view coordinate set

\[
R=K\setminus J
\]

and the corresponding added-view event

\[
D=C(R,b|_R).
\]

Inside each latent branch of the P75 model, conditional independence gives

\[
B=A\cap D
\]

and therefore

\[
\boxed{
P_s(A\setminus B)
=P_s(A)\bigl(1-P_s(D)\bigr),
\qquad s\in\{-,+\}.
}
\]

Because $J$ and $R$ are disjoint, the response parameters entering $P_s(A)$ and $P_s(D)$ are disjoint coordinates of the parameter box.

The residual support contains

\[
\boxed{
|A\setminus B|
=2^{4-|J|}-2^{4-|K|}
}
\]

full observed cells.

---

## 3. Exact branchwise residual interval

For one latent branch $s$, let

\[
P_s(A)\in[a_s^L,a_s^U]
\]

and

\[
P_s(D)\in[d_s^L,d_s^U].
\]

Each interval is exact because it is a product of monotone binary response factors over independent box coordinates.

Since the parent and added-view factors depend on disjoint coordinates, their extrema are jointly attainable. The function

\[
(a,d)\mapsto a(1-d)
\]

is nondecreasing in $a$ and nonincreasing in $d$ on $[0,1]^2$. Hence the exact branchwise residual interval is

\[
\boxed{
P_s(A\setminus B)
\in
\left[
a_s^L(1-d_s^U),

a_s^U(1-d_s^L)
\right].
}
\]

Define

\[
r_s^L=a_s^L(1-d_s^U),
\qquad
r_s^U=a_s^U(1-d_s^L).
\]

---

## 4. Exact latent-mixture interval

Let the prevalence parameter satisfy

\[
\pi\in[\pi_L,\pi_U].
\]

For any P75 parameter vector in the box,

\[
q(A\setminus B)
=(1-\pi)r_-+\pi r_+.
\]

For fixed $\pi$, the expression is increasing in both $r_-$ and $r_+$. Therefore the exact lower and upper envelopes are

\[
L(\pi)=(1-\pi)r_-^L+\pi r_+^L,
\]

\[
U(\pi)=(1-\pi)r_-^U+\pi r_+^U.
\]

Both are affine in $\pi$, so their extrema occur at a prevalence endpoint. Thus

\[
\boxed{
\ell_{A\setminus B}(B)
=
\min_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)r_-^L+\pi r_+^L\right],
}
\]

and

\[
\boxed{
u_{A\setminus B}(B)
=
\max_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)r_-^U+\pi r_+^U\right].
}
\]

These endpoints are exact for the declared axis-aligned P75 parameter box and are rational whenever the box endpoints are rational.

---

## 5. Why direct residual extremization is stronger than interval subtraction

P81 separately gives

\[
q(A)\in[\ell_A,u_A],
\qquad
q(B)\in[\ell_B,u_B].
\]

Subtracting those intervals yields the sound enclosure

\[
\boxed{
q(A\setminus B)
\in
\left[
\max\{0,\ell_A-u_B\},
\min\{1,u_A-\ell_B\}
\right].
}
\]

But this construction forgets that $A$ and $B$ arise from the **same** parameter vector.

The exact P82 interval is always contained in that subtraction enclosure because every attainable residual value is a difference of simultaneously attainable parent and child values. The containment can be strict.

A simple example fixes the two added views to satisfy the child constraints with probability one in both latent branches while leaving the parent response unconstrained. Then $A=B$ for every model law, so

\[
q(A\setminus B)=0
\]

exactly, whereas the separate parent and child ranges can both equal $[0,1]$, giving the useless subtraction enclosure $[0,1]$.

This is why P82 computes the residual range directly instead of relying on interval subtraction.

---

## 6. Event-mass transfer to full-law distance

For any event $S\subseteq\{0,1\}^4$, if

\[
\|\widehat p-q\|_\infty\le r,
\]

then

\[
\left|
\widehat p(S)-q(S)
\right|
\le
|S|r.
\]

Applying this to $S=A\setminus B$ gives

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat p(A\setminus B),
[\ell_{A\setminus B}(B),u_{A\setminus B}(B)]
\right)
}{|A\setminus B|}.
}
\]

Define the exact nested-contrast lower bound

\[
\boxed{
L_{\mathrm{nest}}(B)
=
\max_{(A,B)\in\mathcal N}
\frac{
d\!\left(
\widehat p(A\setminus B),
[\ell_{A\setminus B}(B),u_{A\setminus B}(B)]
\right)
}{|A\setminus B|},
}
\]

where $\mathcal N$ is the predeclared standard family of nested pairs described next.

---

## 7. The finite P82 contrast family

P82 includes every nested parent-child cylinder pair for which the child fixes at least two additional views.

One-view refinements are omitted because if the child adds exactly one binary constraint, then $A\setminus B$ is exactly the sibling cylinder already tested by P81.

For four binary views, the genuinely new family has

\[
\begin{aligned}
|\mathcal N|
&={4\choose1}2
\left[{3\choose2}2^2+{3\choose3}2^3\right]
+{4\choose2}2^2{2\choose2}2^2\\
&=8(12+8)+24(4)\\
&=\boxed{256}.
\end{aligned}
\]

Thus the complete P82 residual audit is finite and small.

---

## 8. P82 theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{82}(B)
=
\max\{L_{81}(B),L_{\mathrm{nest}}(B)\}.
}
\]

Then:

1. $L_{82}(B)$ is a rigorous lower bound on the $L_\infty$ distance from $\widehat p$ to every P75 law generated inside $B$;
2. $L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. every nested residual interval used by $L_{\mathrm{nest}}$ is the exact image interval of that residual event over the declared axis-aligned P75 box;
4. every interval endpoint and every P82 lower bound is exactly computable in rational arithmetic when the empirical law and parameter-box endpoints are rational;
5. for every finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{82}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{82}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

6. on the same partition,

\[
\boxed{
L_{82}(\mathcal B)\ge L_{81}(\mathcal B);
}
\]

7. explicit admissible parameter vectors remain valid global upper-bound witnesses;
8. the previously proved P78 mesh-width upper certificate remains valid and is retained unchanged. No new P82 convergence-rate theorem is assumed.

---

## 9. Proof

### 9.1 Exactness of the residual box interval

For one branch $s$, conditional independence gives

\[
P_s(A\setminus B)=P_s(A)(1-P_s(D)).
\]

The parent factors and added-view factors use disjoint response coordinates. Their box extrema are therefore simultaneously attainable. Monotonicity of $a(1-d)$ on $[0,1]^2$ gives the exact branchwise endpoints in Section 3.

The minus-branch response coordinates, plus-branch response coordinates, and prevalence are also distinct coordinates of the full parameter box. Therefore the branchwise endpoint choices are jointly attainable with either prevalence endpoint. The mixture is affine in prevalence, proving the formulas in Section 4 are exact rather than merely enclosing.

### 9.2 Soundness of each residual lower bound

For $S=A\setminus B$,

\[
|\widehat p(S)-q(S)|
\le
|S|\|\widehat p-q\|_\infty.
\]

Every P75 law generated inside $B$ has $q(S)$ inside the exact residual interval. Therefore the distance from the empirical residual mass to that interval, divided by $|S|$, is a valid lower bound on full-law distance.

### 9.3 Soundness and dominance of $L_{82}$

$L_{\mathrm{nest}}(B)$ is the maximum of finitely many sound lower bounds and is therefore sound. P81 is already a sound lower bound. Their maximum is sound and satisfies

\[
L_{82}(B)\ge L_{81}(B).
\]

Taking the minimum over a partition preserves a valid lower bound to the complete model family because the active boxes cover the complete parameter cube.

### 9.4 Exact arithmetic

The calculation uses only rational endpoint products, subtraction from one, affine prevalence combinations, empirical rational sums, interval distance, maxima, minima, and division by positive integer support sizes. Rational inputs therefore produce exact rational outputs.

---

## 10. Strict improvement witness over P81

Consider the P75 parameter box with

\[
q_{3,-}=q_{3,+}=q_{4,-}=q_{4,+}=\frac12,
\]

while prevalence and all four response parameters for views 1 and 2 remain free in $[0,1]$.

Define an empirical sixteen-cell law by

\[
\widehat p_{0011}=0,
\]

\[
\widehat p_x=\frac16
\quad\text{for the other three cells with }(x_3,x_4)=(1,1),
\]

and

\[
\widehat p_x=\frac1{24}
\quad\text{for the remaining twelve cells}.
\]

The masses sum to one.

Let

\[
A=\{X_3=1,X_4=1\}.
\]

Every model law in the box satisfies

\[
q(A)=\frac14,
\]

whereas

\[
\widehat p(A)=\frac12.
\]

Because $|A|=4$, this gives the strongest P81 projected-event lower bound

\[
L_{81}(B)=\frac{1/2-1/4}{4}=\frac1{16}.
\]

Now choose the child

\[
B_0=\{X_1=0,X_2=0,X_3=1,X_4=1\}.
\]

The residual event $A\setminus B_0$ contains three cells. Empirically,

\[
\widehat p(A\setminus B_0)=\frac12.
\]

For every model law in the box,

\[
q(A\setminus B_0)\in\left[0,\frac14\right].
\]

Therefore

\[
L_{\mathrm{nest}}(B)
\ge
\frac{1/2-1/4}{3}
=\boxed{\frac1{12}}.
\]

The exact executable audit gives

\[
\boxed{
L_{80}(B)=0,
\qquad
L_{81}(B)=\frac1{16},
\qquad
L_{82}(B)=\frac1{12}.
}
\]

Hence P82 is strictly stronger than P81 on a concrete exact-rational P75 box.

---

## 11. Global branch-and-bound handoff

P82 can replace the P81 box lower bound inside the same branch-and-bound framework. Active boxes continue to partition the complete nine-dimensional parameter cube. The global lower bound is the minimum active P82 box bound.

For the upper direction, P82 deliberately reuses what is already proved:

- any explicit P75 parameter vector gives a valid model-distance upper bound;
- the P78 mesh-width upper certificate remains valid because it bounds the same underlying model-distance problem.

P82 does not claim that the new lower bound has a separately proved convergence rate.

---

## 12. P79 finite-data rejection handoff

Let $\overline\varepsilon_{79}$ be the certified rational upper envelope for the P77 cellwise sampling radius supplied by P79. Then

\[
\boxed{
L_{82}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\mathcal C_n(\widehat p)\cap\mathcal M_{4,2}=\varnothing.
}
\]

This is a one-sided rejection statement. If the inequality does not hold, the result is inconclusive.

---

## 13. Implementation and independent checks

Implementation:

- [`nested_projection_contrast_separation.py`](../src/consciousness_bridge/nested_projection_contrast_separation.py)

Tests:

- [`test_nested_projection_contrast_separation.py`](../tests/test_nested_projection_contrast_separation.py)

The test suite includes:

1. the exact count of 256 standard nested contrasts;
2. exhaustive parameter-box vertex enumeration for a nontrivial rational box, verifying the closed-form residual interval equals the actual minimum and maximum over all vertices;
3. a case where the exact residual interval is strictly tighter than separate interval subtraction;
4. the strict $L_{82}>L_{81}$ witness above;
5. P82 dominance over P81;
6. branch-and-bound bracket invariants.

---

## 14. Scientific interpretation

P82 strengthens a computational certificate for rejecting one declared target-view model family. It is evidence about **model compatibility**, not about an experiential ontology.

A positive certified separation says that the observed population law cannot lie in the declared P75 four-view conditional-independence family once finite-data uncertainty is accounted for by the P77/P79 handoff. It does not say why the model fails, and it does not establish what consciousness is.

A non-rejection is also limited. It means only that the current certificate has not separated the population from the declared family at the stated resolution and confidence.

The physical-to-experiential bridge therefore remains open.
