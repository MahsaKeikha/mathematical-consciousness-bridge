# P79 Equation and Provenance Record

This record classifies the mathematical ingredients used in [Proposition 79](proposition_79_joint_statistical_computational_power.md). It separates standard probability and optimization facts from repository-specific composition in the P77-P78 testing architecture.

## 1. Finite-alphabet simultaneous radius

For \(K\) categorical cells and \(q\in(0,1)\),

\[
\varepsilon_{n,K}(q)
=
\sqrt{\frac{\log(2K/q)}{2n}}.
\]

Then

\[
\Pr\left(
\|\widehat P_n-P\|_\infty
\le\varepsilon_{n,K}(q)
\right)
\ge1-q.
\]

**Classification:** standard Hoeffding inequality plus union bound, already used by P76 and P77.

Representative source: Hoeffding (1963), DOI 10.2307/2282952.

## 2. Distance-to-set Lipschitz inequality

For a nonempty model set \(\mathcal M\),

\[
\left|
d_\infty(R,\mathcal M)
-
d_\infty(S,\mathcal M)
\right|
\le
\|R-S\|_\infty.
\]

**Classification:** standard metric consequence of the triangle inequality.

P77 already uses this fact to transport empirical model distance to population model distance.

## 3. Certified three-way bracket decision

Given

\[
L_n\le d_\infty(\widehat P_n,\mathcal M)\le U_n
\]

and a valid rejection-radius upper bound \(r_n\):

\[
L_n>r_n
\quad\Longrightarrow\quad
\text{certified rejection},
\]

\[
U_n\le r_n
\quad\Longrightarrow\quad
\text{explicit model-confidence-ball overlap witness},
\]

while

\[
L_n\le r_n<U_n
\]

is unresolved at the current optimization precision.

**Classification:** repository-specific decision protocol assembled from standard lower-bound, upper-bound, and confidence-region logic.

The overlap state is not model acceptance. It means only that an explicit admissible model candidate lies inside the current closed confidence ball.

## 4. Type I error inheritance

If the rule rejects only when

\[
L_n>\varepsilon_{n,K}(\alpha)
\]

with \(L_n\le d_\infty(\widehat P_n,\mathcal M)\), then under \(P\in\mathcal M\),

\[
\sup_{P\in\mathcal M}\Pr_P(\mathrm{reject})\le\alpha.
\]

**Classification:** direct confidence-set inversion using the P77 simultaneous empirical-law event.

P79 does not claim a new general hypothesis-testing theorem here. Its role is to preserve P77 validity when the empirical distance is represented by a certified lower bound rather than computed exactly.

## 5. Alternative-side concentration radius

For desired Type II error \(\beta\), use the same standard concentration construction with

\[
\varepsilon_{n,K}(\beta)
=
\sqrt{\frac{\log(2K/\beta)}{2n}}.
\]

Then with probability at least \(1-\beta\),

\[
d_\infty(\widehat P_n,\mathcal M)
\ge
d_\infty(P,\mathcal M)-\varepsilon_{n,K}(\beta).
\]

**Classification:** standard concentration plus the standard distance-to-set Lipschitz inequality.

The use of \(\beta\) here is distinct from the \(\alpha\)-level rejection calibration.

## 6. P78 deterministic optimization gap

Assume

\[
0\le
d_\infty(\widehat P_n,\mathcal M)-L_n\le\eta.
\]

For the immediate P75 application, P78 supplies such a deterministic bound through its multi-affine parameter-box mesh certificate.

**Classification:** imported repository result from P78.

The general idea of certified global lower bounds is standard optimization methodology; the concrete P75 mesh certificate is the P78 specialization.

## 7. Joint power-margin inequality

If

\[
d_\infty(P,\mathcal M)\ge\Delta_0,
\]

then on the \(1-\beta\) concentration event,

\[
L_n
\ge
\Delta_0
-
\varepsilon_{n,K}(\beta)
-
\eta.
\]

Therefore

\[
\boxed{
\Delta_0
>
\varepsilon_{n,K}(\alpha)
+
\varepsilon_{n,K}(\beta)
+
\eta
}
\]

implies rejection on that event and hence power at least \(1-\beta\).

**Classification:** repository-specific composition of the P77 rejection radius, a standard alternative-side concentration event, and the P78 deterministic optimization-gap certificate.

The algebra is elementary. P79 does not present it as a new concentration inequality. Its contribution is the explicit statistical-computational budgeting rule inside this testing architecture.

## 8. Sufficient sample-size inequality

For \(0\le\eta<\Delta_0\), the P79 margin condition is guaranteed if

\[
\boxed{
n
>
\frac{
\left(
\sqrt{\log(2K/\alpha)}
+
\sqrt{\log(2K/\beta)}
\right)^2
}{2(\Delta_0-\eta)^2}.
}
\]

**Classification:** direct algebraic rearrangement of the preceding sufficient power condition.

This is a conservative planning rule, not an exact or optimal sample-complexity theorem.

## 9. Computational tolerance budget

For fixed \(n,K,\alpha,\beta\), define

\[
\eta_{\max}
=
\Delta_0
-
\varepsilon_{n,K}(\alpha)
-
\varepsilon_{n,K}(\beta).
\]

Then every certified \(\eta\) satisfying

\[
0\le\eta<\eta_{\max}
\]

meets the P79 sufficient power condition.

**Classification:** direct rearrangement of the joint power inequality.

If \(\eta_{\max}\le0\), the P79 sufficient certificate is unavailable at that design point. This is not an impossibility statement about actual statistical power.

## 10. Planning-margin provenance

The alternative margin \(\Delta_0\) is treated as a prospective design quantity or externally justified lower bound, not as a same-sample statistic that can be selected post hoc without changing interpretation.

**Classification:** methodological design requirement.

This is analogous in spirit to the repository's earlier target-provenance discipline: an inferential guarantee must not quietly obtain a favorable premise from the same evidence being evaluated unless the selection mechanism is itself accounted for.

P79 does not assert stochastic independence between \(\Delta_0\) and the observations. It requires that the prospective interpretation of \(\Delta_0\) be scientifically justified rather than retrofitted from the test result.

## 11. Exact arithmetic versus numerical planning

The executable final comparison uses exact `Fraction` inputs for certified lower and upper bounds. The convenience sample-size helper evaluates logarithms and square roots with ordinary floating-point arithmetic.

**Classification:** implementation boundary rather than a mathematical theorem.

The numerical helper supports planning. It is not promoted to a formal interval proof. A formal certificate requires mathematically valid bound directions for every supplied quantity.

## 12. Repository-specific contribution

The P79 contribution within the Mathematical Consciousness Bridge architecture is the following assembly:

1. combine P77's full-law rejection radius with P78's certified optimization bracket;
2. distinguish a certified rejection, an explicit overlap witness, and an unresolved bracket;
3. introduce a separate \(\beta\)-level concentration event for prospective power;
4. derive the sufficient separation budget \(\Delta_0>\varepsilon_\alpha+\varepsilon_\beta+\eta\);
5. expose the equivalent sample-size and optimization-tolerance budgets;
6. preserve the distinction between exact certification and floating-point planning;
7. keep the population separation margin subject to an explicit provenance requirement.

These results are statistical and computational. They do not constitute a consciousness ontology. The physical-to-experiential bridge remains open.
