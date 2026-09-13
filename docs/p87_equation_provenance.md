# P87 Equation Provenance

This record separates inherited model algebra, elementary derivations, and repository-original P87 constructions. P87 is a conditional model-separation theorem inside the declared P75 four-view binary latent family; it introduces no new claim about the ontology of consciousness.

## Dependencies

P87 depends on:

- **P75** for the declared four-view binary latent target-measurement family;
- **P78** for exact axis-aligned parameter-box certification and the global lower-bound architecture;
- **P83** for the canonical even-parity identity;
- **P84-P85** for the shared-parameter parity-functional hierarchy;
- **P86** for the inherited complete lower bound and the minimally non-uniform four-event certificate.

Direct proof: [Proposition 87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md).

---

## 1. Inherited parity identity

For latent branch $s$ and nonempty view set $J$ used by P87,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This identity is inherited from P83 and follows directly from the product of binary parity responses under the P75 conditional-independence assumption. P87 uses only the canonical view sets with $|J|\in\{2,3,4\}$.

## 2. Inherited latent mixture

For prevalence $\pi$,

\[
P(H_J)=(1-\pi)P_-(H_J)+\pi P_+(H_J).
\]

This is inherited from the P75 two-branch latent mixture.

## 3. P87 coefficient family

P87 defines

\[
\mathcal C_2
=
\left\{
c\in\{-2,-1,1,2\}^4:
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1
\right\}/\{c\sim-c\}.
\]

The quotient means that one global sign is removed.

There are $4^4=256$ nonzero vectors in the ambient coefficient box. The only non-primitive vectors are those with all four magnitudes equal to two, of which there are $2^4=16$. Hence

\[
|\mathcal C_2|
=\frac{256-16}{2}
=120.
\]

This enumeration is an elementary finite counting argument and a repository-original declaration of the P87 search family.

## 4. Number of P87 functionals

The canonical P87 parity-coordinate set has

\[
\binom42+\binom43+\binom44=11
\]

members. Four distinct coordinates can be selected in

\[
\binom{11}{4}=330
\]

ways. Therefore

\[
330\times120=39{,}600
\]

standard P87 functionals.

The implementation constructs the same family exactly and the regression suite asserts both counts.

## 5. Exact box range

For a fixed coefficient vector and four selected parity events,

\[
Q_s
=
\frac12\sum_i c_i
+
\frac12\sum_i c_i\prod_{j\in J_i}(1-2q_{j,s}).
\]

Each response coordinate has degree at most one, so the branch functional is multi-affine.

The endpoint result is derived locally. Hold every coordinate except $z$ fixed. Then

\[
f(z)=az+b
\]

on its interval, so a minimum and maximum occur at the interval endpoints. Repeating this reduction coordinate by coordinate yields a full response-box vertex. After branchwise extrema are known, prevalence enters as

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+,
\]

which is affine; prevalence endpoints therefore suffice. This proves exact endpoint enumeration without importing a black-box nonlinear optimizer.

## 6. Mass-conservation centering

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

With

\[
g_c(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x),
\]

any scalar center $a$ satisfies

\[
Q_c(p)-Q_c(q)
=
\sum_x[g_c(x)-a][p(x)-q(x)].
\]

Thus

\[
|Q_c(p)-Q_c(q)|
\le
\left(\sum_x|g_c(x)-a|\right)\|p-q\|_\infty.
\]

P87 minimizes the coefficient factor exactly:

\[
D(Q_c)=\min_a\sum_x|g_c(x)-a|.
\]

For a finite scalar sample the sum of absolute deviations is minimized by any median. This can be checked directly from the piecewise-linear slope: below the median region more terms decrease than increase when $a$ moves right; above the median region the reverse holds. Evaluating the distinct exact integer coefficient values therefore finds an exact minimizer.

## 7. P87 lower bound

For a P75 box $B$ let

\[
\Delta_c
=
\operatorname{dist}\left(Q_c(\widehat p),I_B(Q_c)\right).
\]

Every model law $q$ generated in $B$ has $Q_c(q)\in I_B(Q_c)$, so

\[
|Q_c(\widehat p)-Q_c(q)|\ge\Delta_c.
\]

Combining this with the centered transfer inequality gives

\[
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_c}{D(Q_c)}.
\]

Maximizing over the 39,600-function family gives $L_{\mathrm{bp4}}(B)$. P87 defines

\[
L_{87}(B)=\max\{L_{86}(B),L_{\mathrm{bp4}}(B)\},
\]

so pointwise dominance $L_{87}\ge L_{86}$ is immediate once validity of each new functional lower bound has been established.

## 8. Exact strict witness

The repository's exact rational witness uses

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

For the stored empirical law and P75 box,

\[
Q(\widehat p)=-\frac{17}{24},
\qquad
I_B(Q)=\left[-\frac12,2\right].
\]

Therefore

\[
\Delta_Q=\frac5{24}.
\]

The exact centered coefficient norm is

\[
D(Q)=20,
\]

with one minimizing center $a=0$. Hence

\[
\frac{\Delta_Q}{D(Q)}
=
\frac{5/24}{20}
=
\frac1{96}.
\]

On the same law and box the complete P86 bound is exactly

\[
L_{86}=\frac1{192}.
\]

The regression suite exhausts all 39,600 P87 functionals and verifies

\[
\boxed{L_{86}=1/192<L_{87}=1/96}.
\]

The witness is synthetic and exact. It is not measured biological or experiential data.

## 9. Evidence classification

| P87 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared model assumption | P75 definition and implementation |
| parity identity | inherited exact model algebra | P83 and local substitution |
| 120 coefficient patterns | finite combinatorial derivation | explicit primitive-count argument plus implementation |
| 39,600 functionals | finite combinatorial derivation | $\binom{11}{4}\times120$ plus implementation |
| box-vertex extremization | elementary exact derivation | coordinatewise affine endpoint proof |
| prevalence endpoints | elementary exact derivation | one-dimensional affine endpoint proof |
| centered transfer denominator | elementary finite-dimensional derivation | mass conservation, triangle inequality, median property |
| $L_{87}\ge L_{86}$ | theorem construction | explicit maximum definition |
| $L_{86}=1/192<L_{87}=1/96$ | repository-original strict witness | exact rational exhaustive regression tests |

## 10. Interpretation boundary

No P87 equation identifies the latent P75 state with conscious experience. P87 does not establish nonphysicality, validate a competing ontology, privilege parity observables as experiential variables, imply an extra dimension of consciousness, or solve the physical-to-experiential bridge. Its result is an exact conditional rejection certificate for one declared latent measurement family.
