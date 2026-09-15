# Proposition 92: Complete single-minor rank-two optimality

## Question

P91 used one selected 3 by 3 determinant from one bipartite flattening of the four-view P75 law and certified

\[
\frac{1}{42}
<
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\le
\frac{1}{24}.
\]

Was that selected determinant merely one convenient nonlinear witness, or is it the strongest possible certificate within the complete class of single 3 by 3 rank-two flattening minors?

P92 answers this question exactly for the declared entrywise box relaxation.

## Scope relative to P89 and P90

P89 and P90 use the earlier strict parameter box whose prevalence coordinate is fixed at \(\pi=0\). Their exact values therefore characterize the single-component boundary problem, not the full mixed-prevalence P75 cube.

P91 removes that prevalence restriction and works over the entire P75 parameter cube. P92 continues exactly that full-cube problem. Consequently the P89 value \(5/168\), the P90 value \(5/72\), and the P92 radius \(\rho_*\) are not competing lower bounds for one identical optimization domain. P92 should be compared directly with P91's full-cube lower exclusion \(1/42\).

## Setup

For each of the three distinct 2+2 bipartitions of four binary views, reshape a sixteen-cell law into a 4 by 4 probability matrix. Under the P75 two-component latent conditional-independence model, every such matrix is a sum of two rank-one matrices. Therefore every P75 flattening has rank at most two, and every 3 by 3 minor must vanish.

Each 4 by 4 matrix has

\[
\binom{4}{3}\binom{4}{3}=16
\]

3 by 3 minors. Across the three bipartitions, the complete single-minor class therefore contains

\[
3\times 16=48
\]

constraints.

For one minor with empirical entries \(m_1,\ldots,m_9\), an \(L_\infty\) full-law radius \(r\) implies the entrywise box

\[
I_j(r)=
[\max(0,m_j-r),\min(1,m_j+r)].
\]

The determinant is multi-affine in its nine entries, so its extrema over this rectangular box occur at the \(2^9=512\) vertices.

A single minor certifies rank-two exclusion at radius \(r\) when zero is not contained in its exact determinant range over that box.

## Result A: complete 48-minor audit at the published P91 radius

At

\[
r=\frac{1}{42},
\]

P92 evaluates all 48 minors and all 512 determinant vertices for each minor using exact rational arithmetic.

Exactly one of the 48 minors excludes zero.

It is precisely the P91 minor from the \((X_1,X_4)\mid(X_2,X_3)\) flattening, using rows \((1,2,3)\) and columns \((0,1,3)\) in the repository's lexicographic 00, 01, 10, 11 ordering.

Its empirical determinant is

\[
D_{\mathrm{emp}}=\frac{1}{512}.
\]

At radius \(1/42\), its exact determinant range satisfies

\[
D_{\min}=\frac{23}{677376}>0,
\qquad
D_{\max}=\frac{2939}{677376}>0.
\]

Every other single minor has zero inside its relaxed determinant range by radius \(1/42\).

Because each entrywise uncertainty box grows monotonically with \(r\), a minor that already contains a determinant-zero point at \(1/42\) cannot recover strict exclusion at any larger radius. Therefore the P91 minor is already uniquely strongest within the complete 48-minor class at the published P91 radius.

## Result B: exact algebraic ceiling of the selected relaxation

For the selected P91 minor, P92 writes every determinant-box vertex as an exact polynomial in \(r\) on the interval

\[
0\le r\le \frac{1}{41}.
\]

This interval lies below every clipping breakpoint of the selected minor, so each endpoint remains affine in \(r\).

Among the 512 vertex polynomials, one active vertex has

\[
q(r)
=
\frac{512r^2-136r+3}{1536}.
\]

Its smaller positive root is

\[
\rho_*
=
\frac{17-\sqrt{193}}{128}
\approx 0.0242777813324234.
\]

Exact comparison gives

\[
\frac{1}{42}<\rho_*<\frac{1}{41}.
\]

P92 then applies an exact Sturm-sequence root count to all 512 vertex polynomials on \((0,1/41)\):

- the active polynomial \(q\) has exactly one root in the interval,
- the other 511 vertex polynomials have no roots in the interval.

At \(r=0\), every vertex polynomial equals the empirical determinant \(1/512>0\). Therefore every determinant-box vertex remains strictly positive for

\[
0\le r<\rho_*.
\]

At \(r=\rho_*\), the active vertex reaches determinant zero.

Thus \(\rho_*\) is the exact ceiling of this selected single-minor entrywise-box certificate.

## Result C: unique optimality in the complete single-minor class

Every other minor already fails to exclude determinant zero by radius \(1/42\), while the selected P91 minor remains certifying beyond \(1/42\) up to the algebraic ceiling \(\rho_*\).

Hence the P91 minor is the unique optimal certificate among all 48 single 3 by 3 flattening minors under the declared entrywise-box relaxation.

This also shows that the P91 witness was not an arbitrary choice among equivalent minors.

## Consequence for the full P75 model distance

Every P75 law has rank at most two in the selected flattening and therefore has selected determinant zero.

If a P75 law existed at full-law distance \(\delta<\rho_*\) from the empirical law, its selected minor would lie inside the corresponding radius-\(\delta\) entrywise box. But P92 proves that every matrix in that box has strictly positive determinant. This is impossible.

Therefore

\[
\boxed{
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\ge
\frac{17-\sqrt{193}}{128}
}
\]

and P91's constructive mixed-prevalence upper certificate remains valid:

\[
\boxed{
\frac{17-\sqrt{193}}{128}
\le
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\le
\frac{1}{24}
}.
\]

This strictly improves the P91 full-cube rational lower exclusion \(1/42\).

## What P92 does not prove

P92 does **not** prove that

\[
d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\rho_*.
\]

At \(r=\rho_*\), one relaxed minor-box vertex has determinant zero. That vertex need not extend to a normalized sixteen-cell law satisfying all shared P75 parameter constraints. Therefore \(\rho_*\) is the exact ceiling of the declared single-minor box relaxation, not the exact solution of the full nonlinear P75 distance problem.

P92 also does not identify the latent variable with consciousness, establish nonphysicality, validate a competing ontology, or close the physical-to-experiential bridge.

## Reproducibility record

Implementation:

`src/consciousness_bridge/complete_single_minor_rank_two_optimality.py`

Tests:

`tests/test_complete_single_minor_rank_two_optimality.py`

Equation provenance:

`docs/p92_equation_provenance.md`

The executable audit uses exact `Fraction` arithmetic for all 48 minor boxes and all determinant vertices, plus exact rational polynomial arithmetic and Sturm sequences for the root-ordering certificate.
