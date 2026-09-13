# P88 Equation Provenance

This record separates inherited mathematics, elementary derivations, repository-original constructions, and interpretation boundaries for Proposition 88.

P88 is a conditional model-separation theorem inside the declared P75 four-view binary latent family. It introduces no claim that the latent state is consciousness and no claim that the physical-to-experiential bridge has been solved.

## Dependencies

P88 depends on:

- **P75** for the declared four-view binary latent target-measurement family;
- **P78** for exact axis-aligned parameter-box certification and the global lower-bound architecture;
- **P83** for the canonical even-parity identity;
- **P84-P85** for shared-parameter parity-functional separation and centered transfer bounds;
- **P86** for the first non-uniform primitive four-event family;
- **P87** for completion of the primitive nonzero coefficient box `0 < |c_i| <= 2` and the inherited complete lower bound.

Direct proof: [Proposition 88](proposition_88_exact_expanded_bounded_primitive_quad_projection_parity_functional.md).

---

## 1. Inherited parity identity

For latent branch $s$ and canonical view set $J$,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This identity is inherited from P83 and follows from conditional independence in the P75 model.

## 2. Inherited latent mixture

For prevalence $\pi$,

\[
P(H_J)=(1-\pi)P_-(H_J)+\pi P_+(H_J).
\]

This is inherited from the P75 two-branch latent mixture.

## 3. P88 coefficient family

P88 defines

\[
\mathcal C_3
=
\left\{
c\in\{-3,-2,-1,1,2,3\}^4:
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1
\right\}/\{c\sim-c\}.
\]

The quotient removes one global sign duplication.

There are

\[
6^4=1296
\]

ambient nonzero vectors.

With maximum coefficient magnitude three, a common divisor greater than one can only be two or three. The vectors with common divisor two are exactly

\[
\{-2,2\}^4,
\]

of which there are $2^4=16$. The vectors with common divisor three are exactly

\[
\{-3,3\}^4,
\]

again numbering $2^4=16$. These sets are disjoint. Therefore

\[
1296-16-16=1264
\]

primitive vectors remain, and global-sign quotienting gives

\[
\boxed{|\mathcal C_3|=632}.
\]

This is an elementary finite counting argument together with the repository-original declaration of the P88 search family.

## 4. Number of P88 functionals

The canonical parity coordinate set contains

\[
\binom42+\binom43+\binom44=11
\]

members. Four distinct coordinates can be selected in

\[
\binom{11}{4}=330
\]

ways. Therefore

\[
\boxed{330\times632=208{,}560}
\]

standard P88 functionals.

The implementation constructs this family exactly and the regression suite asserts both counts.

## 5. Exact box range

For fixed selected parity events and coefficient vector,

\[
Q_s
=
\frac12\sum_i c_i
+
\frac12\sum_i c_i\prod_{j\in J_i}(1-2q_{j,s}).
\]

Each response coordinate enters with degree at most one. The branch functional is therefore multi-affine. Holding all coordinates except one fixed leaves an affine function of that coordinate, whose extrema on an interval occur at endpoints. Repeating coordinate by coordinate gives a box vertex.

After branchwise extrema are known, prevalence enters affinely:

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+.
\]

Prevalence endpoints therefore suffice. This endpoint principle is inherited from the P78/P83-P87 certificate architecture and is re-used without a black-box optimizer.

## 6. Full-law transfer norm

For

\[
g_c(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x),
\]

and probability laws $p,q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Thus for every scalar $a$,

\[
Q_c(p)-Q_c(q)
=
\sum_x[g_c(x)-a][p(x)-q(x)].
\]

Therefore

\[
|Q_c(p)-Q_c(q)|
\le
\left(\sum_x|g_c(x)-a|\right)\|p-q\|_\infty.
\]

Define

\[
D(c)=\min_a\sum_x|g_c(x)-a|.
\]

A median minimizes finite absolute deviation, so $D(c)$ is exactly computable. This centered transfer construction is inherited from P85-P87.

## 7. P88 lower bound

For one functional, let

\[
\Delta_c(B)
=
\operatorname{dist}(Q_c(\widehat p),I_B(Q_c)).
\]

Then

\[
\frac{\Delta_c(B)}{D(c)}
\]

is a valid lower bound on full-law $L_\infty$ distance from the empirical law to every P75 law generated in the parameter box.

P88 exhausts the complete family and defines

\[
L_{\mathrm{bp4},3}(B)
=
\max_{c,J_1,\ldots,J_4}
\frac{\Delta_c(B)}{D(c)}.
\]

The hierarchical certificate is

\[
\boxed{L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{bp4},3}(B)\}}.
\]

Since the P87 coefficient family is contained in the P88 coefficient family,

\[
L_{88}(B)\ge L_{87}(B)
\]

pointwise.

## 8. Repository-original exact strict witness

P88 uses the same rational P75 box and empirical law that support the P86-P87 strict hierarchy. Exhaustion of all 208,560 P88 functionals selects

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-3P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

The exact empirical value is

\[
Q(\widehat p)=-\frac{11}{8}.
\]

The exact P75 parameter-box interval is

\[
I_B(Q)=[-1,2].
\]

Hence

\[
\Delta_Q=\frac38.
\]

The exact centered coefficient norm is

\[
D(Q)=24,
\]

with one minimizing center $a=-1$. Thus

\[
\frac{\Delta_Q}{D(Q)}
=
\frac{3/8}{24}
=
\boxed{\frac1{64}}.
\]

The complete inherited P87 certificate on the same witness is

\[
\boxed{L_{87}(B)=\frac1{96}}.
\]

Therefore

\[
\boxed{L_{87}(B)=\frac1{96}<L_{88}(B)=\frac1{64}}.
\]

Together with the earlier same-witness values,

\[
\boxed{0=L_{85}<\frac1{192}=L_{86}<\frac1{96}=L_{87}<\frac1{64}=L_{88}}.
\]

The specific search family, witness selection, and exact regression record are repository-original constructions. They are not empirical evidence about consciousness.

## 9. Reproducibility

Implementation:

[`expanded_bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/expanded_bounded_primitive_quad_projection_parity_functional_separation.py)

Regression tests:

[`test_expanded_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_expanded_bounded_primitive_quad_projection_parity_functional_separation.py)

Frontier figure:

[`p88_exact_expanded_bounded_primitive_quad_projection_parity.svg`](figures/p88_exact_expanded_bounded_primitive_quad_projection_parity.svg)

All theorem-critical witness arithmetic is exact over `fractions.Fraction`. The declared finite family is exhaustively enumerated rather than sampled.

## 10. Interpretation boundary

No P88 equation identifies the latent P75 state with conscious experience. P88 does not establish nonphysicality, validate a competing ontology, privilege parity observables as experiential variables, imply an extra dimension of consciousness, or solve the physical-to-experiential bridge. Its result is an exact conditional rejection certificate for one declared latent measurement family.
