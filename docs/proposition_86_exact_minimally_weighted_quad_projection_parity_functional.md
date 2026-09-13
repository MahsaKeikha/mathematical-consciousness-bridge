# Proposition 86: Exact Minimally Weighted Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P86 strengthens P85 for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 tests one parity observable at a time. P84 couples two observables under one shared parameter assignment. P85 tests all 660 sign-normalized three-event unit-weight functionals. P86 asks the next sharper question: **can a minimally non-uniform weighted relation among four parity observables reject a P75 parameter box even when the complete P85 certificate is still zero?**

The answer can be yes.

P86 is a model-separation result. It does not identify the P75 latent state with consciousness, does not validate an alternative model after rejection, and does not close the physical-to-experiential bridge.

---

## 1. Why P86 changes the functional family

A direct four-event extension with only unit-magnitude coefficients is not the only natural next test. Linear separation in parity-coordinate space can require unequal coefficients even when all lower-order unit-weight relations are compatible.

P86 therefore uses the smallest non-uniform primitive positive magnitude multiset

\[
\{1,1,1,2\}.
\]

This is the first integer weighting beyond the all-unit pattern after removal of an irrelevant common scale.

For each four-element subset of the eleven canonical even-parity view sets, P86 assigns the magnitudes $1,1,1,2$ in every distinct order and every sign pattern, modulo one global sign. The first coefficient is normalized positive.

There are four locations for the doubled magnitude and eight residual sign patterns, giving

\[
4\times 8=32
\]

standard coefficient patterns for each four-event subset. Hence the full P86 family contains

\[
\boxed{\binom{11}{4}\times 32=330\times 32=10{,}560}
\]

standard functionals.

---

## 2. Canonical parity coordinates

For each

\[
J\subseteq\{0,1,2,3\},\qquad |J|\in\{2,3,4\},
\]

define

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\}.
\]

Choose four distinct view sets $J_1,J_2,J_3,J_4$ and integer coefficients $c_i$ satisfying

\[
\{|c_1|,|c_2|,|c_3|,|c_4|\}=\{1,1,1,2\}.
\]

After fixing one global sign, define

\[
Q(p)=\sum_{i=1}^4 c_iP_p(H_{J_i}).
\]

---

## 3. Exact P75 box interval

Inside latent branch $s\in\{-,+\}$ write

\[
a_{j,s}=1-2q_{j,s}.
\]

Then

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2,
\]

so

\[
Q_s=\frac12\sum_{i=1}^4c_i+
\frac12\sum_{i=1}^4c_i\prod_{j\in J_i}a_{j,s}.
\]

Every response coordinate occurs with degree at most one. Thus $Q_s$ is multi-affine, and its extrema on any axis-aligned rational response box occur at endpoint vertices.

For latent prevalence $\pi$,

\[
Q=(1-\pi)Q_-+\pi Q_+.
\]

After exact branch extremization, the lower and upper envelopes are affine in $\pi$, so their extrema occur at the prevalence endpoints.

Therefore every standard P86 functional has an exact rational P75 box interval

\[
I_B(Q)=[Q_B^L,Q_B^U].
\]

No floating-point optimizer is required.

---

## 4. Transfer to full-law $L_\infty$ distance

Define the sixteen-cell outcome coefficient

\[
g(x)=\sum_{i=1}^4c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Hence for any constant $a$,

\[
Q(p)-Q(q)=\sum_x[g(x)-a][p(x)-q(x)].
\]

Therefore

\[
|Q(p)-Q(q)|\le
\left(\sum_x|g(x)-a|\right)\|p-q\|_\infty.
\]

Define the exact centered coefficient norm

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

Any median of the sixteen integer coefficient values minimizes the $L_1$ objective, so $D(Q)$ is exactly computable.

If the empirical value lies a distance

\[
\Delta_Q=\operatorname{dist}(Q(\widehat p),I_B(Q))
\]

outside the P75 box interval, then every P75 law generated in $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{\Delta_Q}{D(Q)}.
}
\]

---

## 5. P86 certificate

Let $L_{85}(B)$ be the complete P85 lower bound and let

\[
L_{\mathrm{w4}}(B)=
\max_{Q\in\mathcal Q_{86}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)},
\]

where $\mathcal Q_{86}$ is the 10,560-function standard family.

Define

\[
\boxed{L_{86}(B)=\max\{L_{85}(B),L_{\mathrm{w4}}(B)\}.}
\]

Then immediately

\[
L_{86}(B)\ge L_{85}(B)
\]

for every empirical law and every admissible rational P75 box.

### Proposition 86

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. every standard P86 weighted four-event box interval is computed exactly;
2. every mismatch gives a valid full-law $L_\infty$ lower bound through the exact centered coefficient norm;
3. $L_{86}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{86}(B)\ge L_{85}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{85}(B)=0$ but $L_{86}(B)>0$.

---

## 6. Exact rational strict witness

Use P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Take

\[
B_L=\left(
0,\frac14,\frac12,\frac14,\frac34,\frac12,\frac12,\frac14,\frac34
\right),
\]

\[
B_U=\left(
0,1,1,1,\frac34,1,\frac34,1,1
\right).
\]

Let the empirical law have the following nonzero masses:

\[
\begin{aligned}
\widehat p(0001)&=\frac1{24}, &
\widehat p(0011)&=\frac2{24}, &
\widehat p(0101)&=\frac2{24},\\
\widehat p(0110)&=\frac1{24}, &
\widehat p(0111)&=\frac3{24}, &
\widehat p(1000)&=\frac3{24},\\
\widehat p(1001)&=\frac1{24}, &
\widehat p(1011)&=\frac5{24}, &
\widehat p(1101)&=\frac3{24},\\
\widehat p(1111)&=\frac3{24}.&&
\end{aligned}
\]

All other six cells have zero mass.

The complete P85 certificate is exactly

\[
\boxed{L_{85}(B)=0}.
\]

Now use the P86 functional

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+P(H_{\{0,1,2,3\}}).
\]

For the empirical law,

\[
Q(\widehat p)=-\frac{13}{12}.
\]

Exact endpoint enumeration gives

\[
I_B(Q)=[-1,1].
\]

Thus

\[
\Delta_Q=-1-\left(-\frac{13}{12}\right)=\frac1{12}.
\]

The exact centered coefficient calculation gives

\[
D(Q)=16,
\]

with the deterministic implementation selecting the smaller optimal center $a=-1$.

Therefore

\[
L_{86}(B)\ge\frac{1/12}{16}=\boxed{\frac1{192}}.
\]

Exhausting the full 10,560-function standard P86 family attains this value, while P85 remains zero on the same exact box. Hence

\[
\boxed{L_{85}(B)=0<L_{86}(B)=\frac1{192}}.
\]

---

## 7. Why this is a real hierarchy step

The strict witness is not merely a four-event restatement of a P85 triple mismatch. By regression construction, every complete P85 component is silent on the same empirical law and box.

The new information comes from a shared-parameter relation that requires four canonical parity coordinates and a minimally non-uniform primitive integer weighting. This demonstrates that lower-order unit-weight compatibility does not exhaust linear shared-parameter structure in the declared P75 family.

---

## 8. Global branch-and-bound use

The implementation inserts $L_{86}(B)$ into the same certified P78-P85 parameter-box branch-and-bound architecture.

At every finite iteration, active boxes cover all unpruned candidate minimizer regions, each active box has a rigorous P86 lower bound, and evaluated parameter points give valid upper bounds. The active minimum and best feasible upper value therefore remain a certified global distance bracket.

P86 changes the box lower bound, not the P75 model family or the underlying convergence principle.

---

## 9. Scientific interpretation boundary

P86 does **not** prove that:

- consciousness is nonphysical;
- the P75 latent variable is a conscious state;
- a different latent model is correct;
- parity observables are privileged experiential observables;
- a weighted four-event failure implies an additional physical dimension;
- quantum mechanics is incomplete;
- the physical-to-experiential bridge has been solved.

It proves a narrower statement: under the declared P75 model and exact box assumptions, a minimally weighted four-event parity functional can expose a shared-parameter incompatibility that the complete P85 certificate misses.

---

## 10. Executable record

Implementation:

`src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_weighted_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p86_equation_provenance.md`
