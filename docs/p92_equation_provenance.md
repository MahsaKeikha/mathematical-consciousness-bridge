# P92 Equation Provenance

## Scope

This record tracks the mathematical ingredients used by Proposition 92, the complete single-minor rank-two optimality result.

P92 is repository-original theorem development built on the declared P75 target-measurement model and the P91 mixed-prevalence rank-two flattening result.

## Domain distinction from P89 and P90

P89 and P90 use the earlier strict P75 parameter box with prevalence fixed at \(\pi=0\). Their exact values concern that single-component boundary problem.

P91 and P92 remove that restriction and work over the entire P75 parameter cube, including genuinely mixed prevalence. Therefore the P89 value \(5/168\), the P90 value \(5/72\), and the P92 radius \(\rho_*\) do not optimize over one identical model domain. P92 strengthens P91's full-cube lower exclusion, not the older boundary-box values.

## Dependency chain

### P75 model family

P75 defines the four-view binary latent conditional-independence family with one binary latent state and two latent-conditioned product Bernoulli components.

For any 2+2 bipartition of the four observed binary views, the resulting 4 by 4 probability flattening is a sum of two rank-one matrices. Therefore its matrix rank is at most two.

This gives the algebraic model obligation

\[
\det M_{I,J}=0
\]

for every 3 by 3 submatrix \(M_{I,J}\) of every bipartite flattening.

### P91 selected-minor certificate

P91 selects the \((X_1,X_4)\mid(X_2,X_3)\) flattening with row indices \((1,2,3)\) and column indices \((0,1,3)\).

For the established empirical law, the selected minor is

\[
\begin{pmatrix}
1/24 & 1/12 & 1/8\\
1/8 & 0 & 0\\
1/24 & 5/24 & 1/8
\end{pmatrix}
\]

with exact determinant

\[
D_{\mathrm{emp}}=\frac{1}{512}.
\]

At radius \(1/42\), exact 512-vertex evaluation gives

\[
D_{\min}=\frac{23}{677376},
\qquad
D_{\max}=\frac{2939}{677376}.
\]

P91 therefore proves strict rank-two exclusion at that rational radius.

## P92 complete minor class

There are three distinct 2+2 bipartitions of four views:

\[
12\mid34,\qquad 13\mid24,\qquad 14\mid23.
\]

Each 4 by 4 flattening has

\[
\binom{4}{3}^2=16
\]

3 by 3 minors, giving

\[
3\times16=48
\]

single-minor constraints in the complete class.

The implementation enumerates these 48 minors directly. At radius \(1/42\), each minor is evaluated over all

\[
2^9=512
\]

vertices of its entrywise uncertainty box using exact rational arithmetic.

Exactly one minor excludes determinant zero: the P91 minor.

Because the entrywise boxes are nested as the radius grows, every other minor, which already admits determinant zero at \(1/42\), also admits determinant zero at every larger radius. This monotonicity is what turns the radius-\(1/42\) complete audit into a global comparison of single-minor certificate ceilings once the selected P91 minor is shown to survive beyond \(1/42\).

## Multi-affine box extremization

For a 3 by 3 matrix with entries \(x_1,\ldots,x_9\), the determinant is affine in each entry separately while the other eight entries are fixed.

Therefore the determinant is multi-affine on a rectangular entrywise box, and its minimum and maximum occur at box vertices.

This justifies exhaustive vertex evaluation as an exact determinant-range calculation for the declared relaxation.

## Active P91 vertex polynomial

On the interval

\[
0\le r\le\frac{1}{41},
\]

no selected-minor clipping breakpoint is reached. Every nonzero lower endpoint has the form \(m-r\), every upper endpoint has the form \(m+r\), and zero lower endpoints remain zero.

For active vertex bits

`(1, 1, 0, 0, 0, 1, 0, 0, 1)`

the determinant polynomial is

\[
q(r)
=
\frac{1}{512}
-\frac{17}{192}r
+\frac{1}{3}r^2
=
\frac{512r^2-136r+3}{1536}.
\]

The two roots of the numerator are

\[
\frac{17\pm\sqrt{193}}{128}.
\]

The smaller root is

\[
\rho_*=\frac{17-\sqrt{193}}{128}.
\]

Exact integer comparisons establish

\[
\frac{1}{42}<\rho_*<\frac{1}{41}.
\]

## Exact root ordering

The implementation constructs all 512 selected-minor determinant-vertex polynomials using rational polynomial arithmetic.

A Sturm sequence is generated for each polynomial. Exact sign-variation counts at the rational endpoints 0 and \(1/41\) establish:

- one root in \((0,1/41)\) for the active polynomial,
- zero roots in \((0,1/41)\) for each of the other 511 vertex polynomials.

Since every vertex polynomial equals \(1/512>0\) at radius zero, all 512 remain positive until the active polynomial reaches zero at \(\rho_*\).

Thus \(\rho_*\) is the exact single-minor relaxation ceiling for the selected P91 determinant.

## Global lower-bound transfer

Every P75 model law has selected determinant zero. If a P75 law were at full-law \(L_\infty\) distance strictly below \(\rho_*\), its selected nine entries would lie inside a box in which every determinant is strictly positive. This contradiction gives

\[
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})\ge\rho_*.
\]

P91's explicit mixed P75 point remains an admissible upper certificate at \(1/24\), producing

\[
\frac{17-\sqrt{193}}{128}
\le
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\le
\frac{1}{24}.
\]

## Scientific boundary

The algebraic contact at \(\rho_*\) occurs in the relaxed nine-entry determinant box. It is not, by itself, a complete sixteen-cell P75 law and does not prove that the full nonlinear model distance equals \(\rho_*\).

The full P75 optimum therefore remains open after P92.

Nothing in P92 identifies a latent statistical state with consciousness, proves nonphysicality, or establishes the physical-to-experiential bridge.
