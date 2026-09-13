# Proposition 88: Exact Radius-Three Bounded Primitive Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P88 strengthens P87 for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P87 completes every primitive nonzero four-coefficient pattern with $|c_i|\le2$. P88 asks the next finite completeness question at the **same four-event order**: what changes when the exact primitive coefficient box is enlarged to

\[
0<|c_i|\le3?
\]

The answer is that the larger exact family yields a strictly stronger certified model-distance lower bound on the established rational witness.

P88 is a model-separation theorem. It does not identify the P75 latent state with consciousness, validate an alternative model after rejection, or close the physical-to-experiential bridge.

---

## 1. Radius-three primitive coefficient family

P88 uses

\[
\mathcal C_3=
\{c\in\{-3,-2,-1,1,2,3\}^4:\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1\}/\{c\sim-c\}.
\]

There are $6^4=1296$ nonzero vectors in the ambient coefficient box. A vector is non-primitive only when all four entries share a common factor larger than one. Within this alphabet that occurs for the 16 all-even vectors over $\{-2,2\}^4$ and the 16 all-multiple-of-three vectors over $\{-3,3\}^4$. These classes are disjoint. Hence

\[
1296-16-16=1264
\]

primitive signed vectors, and quotienting by one global sign gives

\[
\boxed{|\mathcal C_3|=632}.
\]

The P83 canonical parity-coordinate family contains eleven events, so there are

\[
\binom{11}{4}=330
\]

four-event subsets. Therefore P88 contains

\[
\boxed{330\times632=208{,}560}
\]

exact sign-normalized functionals.

---

## 2. Canonical functional and exact P75 interval

Choose four distinct canonical parity events $H_{J_1},\ldots,H_{J_4}$ and $c\in\mathcal C_3$. Define

\[
Q_c(p)=\sum_{i=1}^4 c_iP_p(H_{J_i}).
\]

Inside latent branch $s\in\{-,+\}$, with $a_{j,s}=1-2q_{j,s}$, the inherited P83 identity is

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2.
\]

Thus $Q_c$ is multi-affine in every branch-response coordinate and affine in prevalence $\pi$. Its minimum and maximum over an axis-aligned rational P75 box therefore occur at response-box and prevalence endpoints. Every P88 model interval

\[
I_B(Q_c)=[Q^L_B,Q^U_B]
\]

is consequently obtained by finite exact rational endpoint enumeration.

---

## 3. Transfer to full-law distance

Let

\[
g_c(x)=\sum_{i=1}^4c_i\mathbf 1_{H_{J_i}}(x).
\]

Because two probability laws have equal total mass, for any scalar $a$,

\[
Q_c(p)-Q_c(q)=\sum_x[g_c(x)-a][p(x)-q(x)].
\]

Define

\[
D(Q_c)=\min_a\sum_x|g_c(x)-a|.
\]

Then an interval mismatch

\[
\Delta_{Q_c}=\operatorname{dist}(Q_c(\widehat p),I_B(Q_c))
\]

implies

\[
\boxed{\|\widehat p-q\|_\infty\ge\Delta_{Q_c}/D(Q_c)}
\]

for every P75 law $q$ generated in $B$.

Let $L_{\mathrm{r3bp4}}(B)$ be the maximum of this exact ratio over all 208,560 P88 functionals and define

\[
\boxed{L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{r3bp4}}(B)\}}.
\]

Therefore $L_{88}(B)\ge L_{87}(B)$ pointwise.

---

## 4. Proposition 88

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. all 208,560 standard P88 functional intervals are computed exactly;
2. every interval mismatch yields a valid full-law $L_\infty$ lower bound;
3. $L_{88}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{88}(B)\ge L_{87}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{88}(B)>L_{87}(B)$.

---

## 5. Exact strict witness

Use the same exact rational box and sixteen-cell empirical law used for the P86-P87 strict hierarchy. The complete P87 certificate is

\[
\boxed{L_{87}(B)=\frac1{96}}.
\]

P88 exhaustively selects

\[
Q=P(H_{\{0,2\}})-P(H_{\{1,3\}})-3P(H_{\{1,2,3\}})+2P(H_{\{0,1,2,3\}}).
\]

For the empirical law,

\[
Q(\widehat p)=-\frac{11}{8}.
\]

Exact endpoint enumeration gives

\[
I_B(Q)=[-1,2],
\]

so

\[
\Delta_Q=-1-\left(-\frac{11}{8}\right)=\frac38.
\]

The exact centered coefficient calculation gives

\[
D(Q)=24,
\]

with minimizing center $a=-1$. Hence

\[
\frac{\Delta_Q}{D(Q)}=\frac{3/8}{24}=\boxed{\frac1{64}}.
\]

Exhaustion of the complete 208,560-function P88 family attains this value. Therefore

\[
\boxed{L_{87}(B)=\frac1{96}<L_{88}(B)=\frac1{64}}.
\]

Together with the established P85-P87 witness values,

\[
\boxed{0=L_{85}(B)<\frac1{192}=L_{86}(B)<\frac1{96}=L_{87}(B)<\frac1{64}=L_{88}(B)}.
\]

The strict P88 direction has coefficient magnitudes $(1,1,3,2)$ and therefore cannot occur in the P87 radius-two family.

---

## 6. Reproducibility

Implementation:

`src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p88_equation_provenance.md`

Frontier figure:

`docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg`

All declared witness quantities are represented with exact `fractions.Fraction` arithmetic, and the standard P88 family is exhaustively enumerated rather than sampled.

---

## 7. Scientific interpretation boundary

P88 strengthens rejection of the declared P75 latent measurement family under the stated box assumptions. It does not establish that consciousness is nonphysical, identify a latent variable with experience, privilege parity observables as experiential observables, validate a replacement model, imply an extra dimension of consciousness, or solve the physical-to-experiential bridge.
