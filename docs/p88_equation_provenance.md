# P88 Equation Provenance

This record separates inherited model algebra, elementary finite counting, and repository-original P88 constructions. P88 is a conditional model-separation theorem inside the declared P75 four-view binary latent family; it introduces no new claim about the ontology of consciousness.

## Dependencies

P88 depends on:

- **P75** for the declared four-view binary latent target-measurement family;
- **P78** for exact rational parameter-box certification and the full-law lower-bound architecture;
- **P83** for the canonical even-parity identity;
- **P84-P87** for the shared-parameter parity-functional hierarchy;
- **P87** specifically for the complete radius-two primitive four-event certificate inherited into $L_{88}$.

Direct proof: [Proposition 88](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md).

---

## 1. Inherited parity identity

For latent branch $s$ and canonical nonempty view set $J$ used by P88,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This is inherited from P83 under the P75 conditional-independence model.

## 2. Inherited latent mixture

For prevalence $\pi$,

\[
P(H_J)=(1-\pi)P_-(H_J)+\pi P_+(H_J).
\]

## 3. P88 coefficient family

P88 declares

\[
\mathcal C_3=
\left\{c\in\{-3,-2,-1,1,2,3\}^4:\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1\right\}/\{c\sim-c\}.
\]

The ambient box contains $6^4=1296$ vectors. The non-primitive vectors are exactly the 16 vectors over $\{-2,2\}^4$ and the 16 vectors over $\{-3,3\}^4$. The two sets are disjoint. Thus

\[
|\mathcal C_3|=\frac{1296-16-16}{2}=\boxed{632}.
\]

This is an elementary finite counting argument and a repository-original declaration of the P88 search family.

## 4. Number of P88 functionals

The canonical parity-coordinate set has eleven members. Four distinct coordinates can be selected in

\[
\binom{11}{4}=330
\]

ways. Therefore

\[
330\times632=\boxed{208{,}560}
\]

standard P88 functionals.

## 5. Exact box range

For a fixed coefficient vector and four selected parity events,

\[
Q_s=\frac12\sum_i c_i+\frac12\sum_i c_i\prod_{j\in J_i}(1-2q_{j,s}).
\]

Each response coordinate appears with degree at most one, hence $Q_s$ is multi-affine. Repeated one-coordinate endpoint reduction proves that branch extrema over an axis-aligned box occur at response vertices. Prevalence enters affinely, so its endpoints suffice as well.

## 6. Mass-conservation transfer

For

\[
g_c(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x),
\]

and probability laws $p,q$,

\[
Q_c(p)-Q_c(q)=\sum_x[g_c(x)-a][p(x)-q(x)]
\]

for any scalar $a$, because $\sum_x[p(x)-q(x)]=0$. Therefore

\[
\|p-q\|_\infty\ge
\frac{\operatorname{dist}(Q_c(p),I_B(Q_c))}{\min_a\sum_x|g_c(x)-a|}.
\]

The denominator is exactly minimized by a median of the sixteen outcome coefficients.

## 7. Hierarchy definition

Let $L_{\mathrm{r3bp4}}(B)$ be the maximum exact lower bound over all P88 radius-three functionals. P88 defines

\[
L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{r3bp4}}(B)\}.
\]

Pointwise dominance $L_{88}\ge L_{87}$ is therefore immediate from the definition.

## 8. Exact strict witness arithmetic

For

\[
Q=P(H_{02})-P(H_{13})-3P(H_{123})+2P(H_{0123}),
\]

the established exact empirical law gives

\[
Q(\widehat p)=-11/8.
\]

Exact P75 endpoint enumeration gives

\[
I_B(Q)=[-1,2],
\]

hence

\[
\Delta_Q=3/8.
\]

The sixteen outcome coefficients have exact centered absolute-deviation norm

\[
D(Q)=24
\]

with minimizing center $a=-1$. Therefore

\[
\Delta_Q/D(Q)=(3/8)/24=1/64.
\]

The exhaustive implementation verifies that this value is the maximum over all 208,560 standard P88 functionals on the declared witness. Since the complete P87 value on the same witness is $1/96$,

\[
\boxed{L_{88}=1/64>1/96=L_{87}}.
\]

## 9. Verification surface

Implementation: `src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`

Tests: `tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`

The implementation uses exact `fractions.Fraction` arithmetic throughout the declared certificate.

## 10. Interpretation boundary

No P88 equation identifies the latent P75 state with conscious experience. P88 does not establish nonphysicality, validate a competing ontology, privilege parity observables as experiential variables, imply an extra dimension of consciousness, or solve the physical-to-experiential bridge.
