# Proposition 92: Complete single-minor rank-two optimality

> Technical draft status: this theorem record is under exact implementation and CI review. It is intentionally staged outside the canonical published proposition namespace. The public theorem frontier remains P91 until P92 publication surfaces are promoted together.

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

P89 and P90 use the earlier strict P75 parameter box with prevalence fixed at \(\pi=0\). Their exact values concern that single-component boundary problem.

P91 and P92 remove that restriction and work over the entire P75 parameter cube, including genuinely mixed prevalence. Therefore the P89 value \(5/168\), the P90 value \(5/72\), and the P92 radius \(\rho_*\) do not optimize over one identical model domain. P92 strengthens P91's full-cube lower exclusion, not the older boundary-box values.

## Model obligation

For every P75 law and every 2+2 bipartition of the four binary observed views, the corresponding 4 by 4 probability flattening is the sum of two rank-one outer products:

\[
F
=
(1-\pi)u_-v_-^\mathsf{T}
+
\pi u_+v_+^\mathsf{T}.
\]

Hence

\[
\operatorname{rank}(F)\le 2,
\]

so every 3 by 3 minor of every such flattening must vanish.

There are three distinct 2+2 bipartitions and

\[
\binom{4}{3}^2=16
\]

3 by 3 minors per flattening. The complete single-minor class therefore contains

\[
3\times16=48
\]

constraints.

The implementation constructs the two rank-one factors explicitly for every bipartition and verifies exact reconstruction of the P75 law.

## Complete radius-1/42 audit

For the established exact empirical law, P92 evaluates all 48 minors under the same entrywise L-infinity box relaxation used by P91.

Each selected 3 by 3 minor has nine entries. Because the determinant is multi-affine in those nine entries, its exact minimum and maximum over an axis-aligned box occur at the

\[
2^9=512
\]

vertices.

The complete audit therefore evaluates

\[
48\times512=24576
\]

exact determinant vertices at radius \(1/42\).

Exactly one minor excludes zero: the P91 minor from the \((X_1,X_4)\mid(X_2,X_3)\) flattening with row indices \((1,2,3)\) and column indices \((0,1,3)\).

For that minor,

\[
D_{\mathrm{emp}}=\frac{1}{512},
\]

and at radius \(1/42\),

\[
D_{\min}=\frac{23}{677376}>0,
\qquad
D_{\max}=\frac{2939}{677376}>0.
\]

Thus the P91 minor is the unique member of the complete 48-minor class that still certifies rank-two exclusion at the published P91 radius.

## Why this already eliminates the other 47 minors from the larger-radius competition

The entrywise uncertainty boxes are nested as the radius increases.

If a minor already admits determinant zero at radius \(1/42\), then every larger uncertainty box contains that same zero-admitting point. Therefore that minor can never recover a strict determinant-sign certificate at any radius greater than \(1/42\).

Consequently, once the P91 minor is shown to remain strictly separated beyond \(1/42\), it is automatically the unique optimal member of the complete 48-minor class.

## Exact selected-minor ceiling

On

\[
0\le r\le\frac{1}{41},
\]

no clipping breakpoint is reached for the nine selected empirical entries. Every determinant-box vertex is therefore an exact polynomial in \(r\).

For the active vertex

`(1, 1, 0, 0, 0, 1, 0, 0, 1)`

the exact determinant polynomial is

\[
q(r)
=
\frac{1}{512}
-\frac{17}{192}r
+\frac{1}{3}r^2
=
\frac{512r^2-136r+3}{1536}.
\]

The roots of the numerator are

\[
\frac{17\pm\sqrt{193}}{128}.
\]

Define

\[
\rho_*
=
\frac{17-\sqrt{193}}{128}.
\]

Exact rational comparisons give

\[
\frac{1}{42}<\rho_*<\frac{1}{41}.
\]

Numerically,

\[
\rho_*\approx 0.0242777813324234.
\]

The endpoint signs are

\[
q\!\left(\frac{1}{42}\right)
=
\frac{23}{677376}>0,
\]

and

\[
q\!\left(\frac{1}{41}\right)
=
-\frac{7}{860672}<0.
\]

## Exact Sturm audit

P92 constructs all 512 selected-minor determinant-vertex polynomials using exact rational polynomial arithmetic.

For each polynomial, the implementation builds a Sturm sequence and counts roots in the rational interval

\[
\left(0,\frac{1}{41}\right).
\]

The exact result is:

- the active polynomial has exactly one root in the interval;
- each of the other 511 vertex polynomials has zero roots there.

All 512 vertex polynomials equal \(1/512>0\) at \(r=0\). Therefore all remain positive until the active polynomial first reaches zero at \(\rho_*\).

Hence the selected P91 determinant excludes rank two for every

\[
r<\rho_*,
\]

and cannot certify strict exclusion at

\[
r=\rho_*
\]

because one determinant-box vertex has reached zero.

Thus \(\rho_*\) is the exact ceiling of the selected single-minor entrywise-box certificate.

Together with the complete 48-minor audit and nested-box monotonicity, this proves that the P91 minor is uniquely optimal in the declared complete single-minor certificate class.

## Full-model consequence

Every exact P75 law has determinant zero on the selected minor.

Suppose a P75 law existed with

\[
\|P-P_{\mathrm{emp}}\|_\infty<\rho_*.
\]

Its nine selected entries would lie in a determinant box of radius strictly below \(\rho_*\), where every determinant value is strictly positive. That contradicts the rank-two P75 obligation.

Therefore

\[
\boxed{
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\ge
\frac{17-\sqrt{193}}{128}
}.
\]

P91 already provides an explicit genuinely mixed P75 point at full-law distance \(1/24\). Hence

\[
\boxed{
\frac{17-\sqrt{193}}{128}
\le
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})
\le
\frac{1}{24}
}.
\]

This strictly strengthens the P91 lower certificate \(1/42\).

## What P92 does not prove

P92 proves the exact ceiling of the complete single-minor entrywise-box relaxation.

It does **not** prove

\[
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\rho_*.
\]

At \(r=\rho_*\), one relaxed nine-entry determinant-box vertex has determinant zero. That relaxed point need not extend to a normalized sixteen-cell law, and it need not satisfy the shared P75 parameterization across all cells.

The exact full nonlinear P75 distance therefore remains open.

P92 also does not identify the latent variable with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.

## Reproducibility

Implementation:

`src/consciousness_bridge/complete_single_minor_rank_two_optimality.py`

Tests:

`tests/test_complete_single_minor_rank_two_optimality.py`

Equation provenance:

`docs/drafts/p92_equation_provenance.md`

The implementation uses exact `fractions.Fraction` arithmetic for the empirical law, flattenings, minors, interval vertices, determinant polynomials, polynomial division, and Sturm sequences. The algebraic radius is stored exactly as a quadratic surd rather than rounded into the theorem logic.
