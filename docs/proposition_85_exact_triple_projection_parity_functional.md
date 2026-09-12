# Proposition 85: Exact Three-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P85 strengthens P84 for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 asks whether one parity observable is compatible with a P75 parameter box. P84 asks whether two parity observables remain compatible when the same parameter assignment must explain both. P85 asks the next logically stronger question: **can three parity observables remain compatible under one shared parameter assignment even when every one-event and two-event certificate is still silent?**

The answer can be no.

P85 is a model-separation result. It does not identify the P75 latent state with consciousness, does not validate an alternative model after rejection, and does not close the physical-to-experiential bridge.

---

## Plain-language meaning

A collection of measurements can look consistent when each measurement is checked by itself. The same collection can still look consistent when every pair is checked. That does not guarantee that all three measurements can be produced together by one common model parameter choice.

P85 detects this three-way incompatibility.

A useful analogy is three overlapping constraints on one mechanism. Constraint A can coexist with B. A can coexist with C. B can coexist with C. Yet there may be no single mechanism setting that satisfies A, B, and C simultaneously. P85 converts that possibility into an exact, auditable certificate for the P75 parity-observable family.

For the strict rational witness in the repository:

- the complete P84 lower bound is exactly $0$;
- one P85 three-event functional has empirical value $19/8$;
- its exact P75 box range is $[0,2]$;
- the exact interval gap is $3/8$;
- the centered coefficient norm is $12$;
- therefore the certified full-law lower bound is

\[
\frac{3/8}{12}=\boxed{\frac{1}{32}}.
\]

So P85 proves a positive separation on a box where P84 proves none.

---

## 1. Canonical parity coordinates

For each view set

\[
J\subseteq\{0,1,2,3\},\qquad |J|\in\{2,3,4\},
\]

define the canonical even-parity event

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv 0\pmod 2\right\}.
\]

There are

\[
\binom42+\binom43+\binom44=6+4+1=11
\]

such view sets.

P85 selects three distinct view sets $J_1,J_2,J_3$ and signs

\[
\sigma_i\in\{-1,+1\}.
\]

Because multiplying all signs by $-1$ only reverses the functional, the first sign is normalized to $+1$. Thus there are

\[
\binom{11}{3}2^2=165\cdot4=\boxed{660}
\]

standard P85 functionals.

For one such triple define

\[
T(p)=\sum_{i=1}^3\sigma_i P_p(H_{J_i}).
\]

---

## 2. Exact P75 branch formula

Inside latent branch $s\in\{-,+\}$ define

\[
a_{j,s}=1-2q_{j,s}.
\]

The parity identity already used by P83 and P84 gives

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}{2}.
\]

Therefore

\[
T_s
=
\frac12\sum_{i=1}^3\sigma_i
+
\frac12\sum_{i=1}^3
\sigma_i\prod_{j\in J_i}a_{j,s}.
\]

Every coordinate $a_{j,s}$ appears with degree at most one. Hence $T_s$ is multi-affine in the response coordinates appearing in

\[
J_1\cup J_2\cup J_3.
\]

A multi-affine function on an axis-aligned box reaches its extrema at box vertices. With four observed views, at most $2^4=16$ branch endpoint combinations are required.

This is an exact extremization, not a numerical relaxation.

---

## 3. Exact full-box interval

Let the exact minus-branch interval be

\[
[m_-,M_-]
\]

and the exact plus-branch interval be

\[
[m_+,M_+].
\]

For latent prevalence $\pi$,

\[
T=(1-\pi)T_-+\pi T_+.
\]

Once the branch extrema are fixed, the lower and upper envelopes are affine in $\pi$. Therefore the full P75 box extrema occur at the prevalence endpoints.

For any rational P75 parameter box $B$, P85 computes an exact interval

\[
I_B(T)=[T_B^L,T_B^U].
\]

No local optimizer is used.

---

## 4. Exact transfer to full-law $L_\infty$ distance

Define the outcome coefficient

\[
g(x)=\sum_{i=1}^3\sigma_i\mathbf 1_{H_{J_i}}(x).
\]

Then

\[
T(p)-T(q)=\sum_x g(x)[p(x)-q(x)].
\]

Because $p$ and $q$ both have total mass one,

\[
\sum_x[p(x)-q(x)]=0.
\]

So for any constant $c$,

\[
T(p)-T(q)
=
\sum_x[g(x)-c][p(x)-q(x)].
\]

Therefore

\[
|T(p)-T(q)|
\le
\left(\sum_x|g(x)-c|\right)\|p-q\|_\infty.
\]

P85 minimizes the coefficient factor over constant shifts:

\[
D(T)=\min_c\sum_x|g(x)-c|.
\]

For finitely many real coefficients, any median is an $L_1$ minimizer. Here the sixteen $g(x)$ values are integers, so the exact minimum can be computed by evaluating the finitely many distinct coefficient values.

If the empirical functional $T(\widehat p)$ lies a distance

\[
\Delta_T
=
\operatorname{dist}\left(T(\widehat p),I_B(T)\right)
\]

outside the exact P75 box interval, then every $q$ generated in $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{\Delta_T}{D(T)}.
}
\]

---

## 5. P85 box certificate

Let $L_{84}(B)$ be the complete P84 box lower bound. Let

\[
L_{\text{triple}}(B)
=
\max_{T\in\mathcal T_{85}}
\frac{
\operatorname{dist}\left(T(\widehat p),I_B(T)\right)
}{D(T)},
\]

where $\mathcal T_{85}$ is the 660-function standard family.

Define

\[
\boxed{
L_{85}(B)=\max\{L_{84}(B),L_{\text{triple}}(B)\}.
}
\]

Immediately,

\[
L_{85}(B)\ge L_{84}(B)
\]

for every empirical law and every admissible P75 parameter box.

### Proposition 85

For every empirical sixteen-cell law $\widehat p$ and every rational P75 parameter box $B$:

1. each of the 660 standard signed triple-functional intervals is computed exactly;
2. each triple-functional mismatch gives a valid full-law $L_\infty$ lower bound through the centered coefficient norm;
3. $L_{85}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{85}(B)\ge L_{84}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{84}(B)=0$ but $L_{85}(B)>0$.

---

## 6. Proof

### Step 1: exact branch extrema

Each canonical even-parity probability is a constant plus one product of distinct branch response coordinates. A signed sum of three such probabilities is therefore multi-affine. Multi-affine extrema over a rectangle occur at vertices. The branch interval is exact.

### Step 2: exact latent-mixture extrema

The minus-branch and plus-branch response coordinates are disjoint. After each branch is extremized, the mixture is affine in prevalence. Its extrema occur at the prevalence endpoints. The full P75 box interval is exact.

### Step 3: centered coefficient inequality

For any constant $c$,

\[
\sum_x c[p(x)-q(x)]=0.
\]

Hence

\[
T(p)-T(q)
=
\sum_x[g(x)-c][p(x)-q(x)].
\]

Applying the triangle inequality and the definition of $L_\infty$ gives

\[
|T(p)-T(q)|
\le
\sum_x|g(x)-c|\,\|p-q\|_\infty.
\]

Minimizing over $c$ proves the transfer denominator $D(T)$.

### Step 4: distance to the exact model interval

Every P75 law in $B$ produces a functional value inside $I_B(T)$. Therefore, if the empirical value is $\Delta_T$ outside that interval, every model law must change the functional by at least $\Delta_T$. The centered coefficient inequality implies

\[
\|\widehat p-q\|_\infty\ge \Delta_T/D(T).
\]

### Step 5: dominance

P85 is defined as the maximum of the complete P84 certificate and the new triple-functional family, so $L_{85}(B)\ge L_{84}(B)$ identically.

### Step 6: strictness

The exact rational witness below has $L_{84}(B)=0$ and $L_{85}(B)=1/32$. Therefore dominance is strict on at least one admissible input.

$\square$

---

## 7. Exact rational strict witness

Use P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Take

\[
B_L=
\left(
1,0,0,1,0,\frac12,0,\frac12,\frac12
\right),
\]

\[
B_U=
\left(
1,1,1,1,1,\frac12,1,\frac12,1
\right).
\]

The prevalence is fixed at $\pi=1$, so only the plus branch contributes to the observed law. The unused minus-branch coordinates remain in the box because the theorem is stated in the common nine-parameter P75 representation.

Let the empirical law place mass

\[
\widehat p(0000)=\frac38,
\qquad
\widehat p(0010)=\frac18,
\qquad
\widehat p(0100)=\frac18,
\qquad
\widehat p(0101)=\frac38,
\]

and zero mass on the other twelve cells.

The complete P84 certificate gives

\[
L_{84}(B)=0.
\]

Now use

\[
T
=
P(H_{\{0,3\}})
+
P(H_{\{1,3\}})
+
P(H_{\{0,1,3\}}).
\]

For the empirical law,

\[
T(\widehat p)=\frac{19}{8}.
\]

Exact endpoint enumeration gives

\[
I_B(T)=[0,2].
\]

Thus

\[
\Delta_T=\frac{19}{8}-2=\frac38.
\]

Across the sixteen observed cells, the uncentered coefficient values are distributed as

\[
0\text{ on 2 cells},\quad
1\text{ on 6 cells},\quad
2\text{ on 6 cells},\quad
3\text{ on 2 cells}.
\]

Centering at either $c=1$ or $c=2$ gives

\[
D(T)=12.
\]

Therefore

\[
L_{85}(B)
\ge
\frac{3/8}{12}
=
\boxed{\frac1{32}}.
\]

Since the implemented exhaustive P85 family attains this value and P84 is zero on the same box,

\[
\boxed{L_{84}(B)=0<L_{85}(B)=\frac1{32}}.
\]

---

## 8. Global branch-and-bound use

The implementation inserts $L_{85}(B)$ into the same certified parameter-box branch-and-bound architecture used from P78 onward.

At every finite iteration:

- active parameter boxes cover every not-yet-pruned candidate minimizer region;
- each active box has a rigorous P85 lower bound;
- every evaluated box center is an admissible P75 parameter vector and therefore supplies a valid upper bound;
- the minimum active lower bound and best evaluated upper bound form a certified global distance bracket.

P85 does not require a new convergence principle. Its lower bound contains P84, which contains the earlier P78 cellwise certificate. The new contribution is a tighter exact box lower bound, not a different model family.

---

## 9. Why P85 is scientifically useful

P85 isolates a specific logical weakness in pairwise checking.

A model can survive:

- every one-observable test;
- every two-observable shared-parameter test;

and still fail a three-observable shared-parameter requirement.

This matters whenever a latent physical model is judged by a collection of derived observables. Compatibility of low-order subsets should not be silently promoted to compatibility of the complete collection.

P85 makes that failure mode explicit and computationally testable.

---

## 10. What P85 does not prove

P85 does **not** prove that:

- consciousness is nonphysical;
- the P75 latent variable is a conscious state;
- a different latent model is correct;
- parity observables are privileged experiential observables;
- three-way failure implies a new dimension of reality;
- quantum mechanics is incomplete;
- the physical-to-experiential bridge has been solved.

It proves a narrower statement: under the declared P75 model and the stated exact box assumptions, three parity-derived observables can expose a shared-parameter incompatibility that all P84 checks miss.

---

## 11. Executable record

Implementation:

`src/consciousness_bridge/triple_projection_parity_functional_separation.py`

Regression tests:

`tests/test_triple_projection_parity_functional_separation.py`

The tests verify:

- all 660 standard sign-normalized triple functionals are present;
- exact box intervals agree with exhaustive parameter-vertex evaluation;
- the centered coefficient transfer is computed exactly;
- P85 dominates P84 on every tested box by construction;
- the strict rational witness has $L_{84}=0$ and $L_{85}=1/32$;
- the global branch-and-bound wrapper returns a valid exact-rational bracket;
- the scientific interpretation boundary remains present in the executable source.
