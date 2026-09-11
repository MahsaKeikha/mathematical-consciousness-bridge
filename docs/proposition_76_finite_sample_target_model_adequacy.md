# Proposition 76: Finite-Sample Target-Model Adequacy Rejection

## Status

**Proved conditional theorem, implemented and regression-tested on a synthetic finite-alphabet model.**

P76 is the finite-data continuation of [P75](proposition_75_target_model_adequacy_overidentification.md). P75 gives population-level necessary constraints and a full-law reconstruction audit for one binary latent state observed through four conditionally independent binary views. P76 asks when finite IID data are already strong enough to **reject** that declared target-measurement model.

The scientific direction is intentionally one-sided. P76 can certify incompatibility when a necessary P75 constraint is separated from zero after finite-sample uncertainty is propagated. If the current data do not reject the model, the conclusion is only **not rejected by this certificate**. It is not model acceptance, not proof of conditional independence, and not evidence that the latent state is consciousness.

---

## 1. Setup

Fix one declared physical stratum and let

\[
X=(X_1,X_2,X_3,X_4)\in\{-1,+1\}^4
\]

have unknown population law \(P\). We observe \(n\) IID copies and let \(\widehat P\) denote the empirical law on the sixteen binary cells.

The P75 null model is the existence of a binary latent state \(S\in\{-1,+1\}\) such that the four views are conditionally independent given \(S\):

\[
P(x_1,x_2,x_3,x_4)
=
\sum_{s\in\{-1,+1\}}
P(S=s)\prod_{j=1}^4P(X_j=x_j\mid S=s).
\]

P76 does not assume that this model is true. It derives finite-data consequences that must hold if it is true.

---

## 2. P76A: one simultaneous sixteen-cell confidence event

Define

\[
\boxed{
\varepsilon_n(\alpha)
=
\sqrt{\frac{\log(32/\alpha)}{2n}}
}
\]

and

\[
\boxed{
\delta_n(\alpha)
=
\min\{2,16\varepsilon_n(\alpha)\}.
}
\]

For any fixed binary cell \(x\), the empirical cell frequency is the mean of IID Bernoulli indicators. Hoeffding's inequality gives

\[
\Pr\left(
|\widehat P(x)-P(x)|>\varepsilon
\right)
\le
2e^{-2n\varepsilon^2}.
\]

A union bound over the sixteen cells therefore yields

\[
\boxed{
\Pr\left(
\max_x|\widehat P(x)-P(x)|
\le
\varepsilon_n(\alpha)
\right)
\ge
1-\alpha.
}
\]

On the same event,

\[
\boxed{
\|\widehat P-P\|_1
\le
\delta_n(\alpha).
}
\]

This is one shared event. P76 does not spend a new error probability for every downstream moment or polynomial constraint.

---

## 3. P76B: simultaneous raw-moment transport

For every nonempty index set \(A\subseteq\{1,2,3,4\}\), define the raw binary monomial moment

\[
r_A
=
\mathbb E_P\left[\prod_{j\in A}X_j\right],
\qquad
\widehat r_A
=
\mathbb E_{\widehat P}\left[\prod_{j\in A}X_j\right].
\]

Because every binary monomial has absolute value one,

\[
|\widehat r_A-r_A|
\le
\|\widehat P-P\|_1.
\]

Hence, simultaneously for every nonempty \(A\),

\[
\boxed{
|\widehat r_A-r_A|
\le
\delta_n(\alpha)
}
\]

with probability at least \(1-\alpha\).

All P75 means, pair covariances, third centered moments, fourth centered moment, and polynomial adequacy constraints are polynomial functions of these raw moments. P76 propagates the same raw-moment confidence box through those polynomial maps by conservative interval arithmetic.

---

## 4. P76C: explicit finite-sample tetrad certificate

Write

\[
C_{ij}=\operatorname{Cov}(X_i,X_j),
\qquad
\widehat C_{ij}=\operatorname{Cov}_{\widehat P}(X_i,X_j).
\]

Since

\[
C_{ij}=r_{ij}-r_ir_j,
\]

P76B and the fact that all raw moments lie in \([-1,1]\) give

\[
\boxed{
|\widehat C_{ij}-C_{ij}|
\le
3\delta_n.
}
\]

P75 requires the covariance tetrads

\[
C_{12}C_{34}=C_{13}C_{24}=C_{14}C_{23}.
\]

Define the two residuals

\[
D_1=C_{12}C_{34}-C_{13}C_{24},
\]

\[
D_2=C_{12}C_{34}-C_{14}C_{23}.
\]

Because every covariance of binary variables has absolute value at most one,

\[
\boxed{
|\widehat D_\ell-D_\ell|
\le
12\delta_n,
\qquad \ell\in\{1,2\}.
}
\]

Therefore the following is a finite-data rejection rule:

\[
\boxed{
|\widehat D_\ell|>12\delta_n
\quad\Longrightarrow\quad
D_\ell\ne0
}
\]

with confidence at least \(1-\alpha\). Since every P75 four-view conditional-independence model has \(D_1=D_2=0\), such a result certifies incompatibility with the declared model.

### Conservative design corollary

If the population alternative has a known tetrad margin

\[
|D_\ell|\ge\tau>0,
\]

then it is sufficient that

\[
24\delta_n<\tau
\]

for the finite-sample tetrad rule to be guaranteed to reject on the P76 confidence event. Using the uncapped expression for \(\delta_n\), a sufficient condition is

\[
\boxed{
n>
\frac{73728\log(32/\alpha)}{\tau^2}.
}
\]

This is a conservative design bound, not an optimal sample-complexity claim.

---

## 5. P76D: denominator-free cross-triple adequacy constraints

P75 writes the latent-imbalance quantity for a nondegenerate triple as

\[
q_{ijk}
=
\frac{M_{ijk}^2}{C_{ij}C_{ik}C_{jk}},
\]

where \(M_{ijk}\) is the third centered moment. Direct finite-sample ratio inversion is undesirable near a small covariance denominator. P76 therefore uses polynomial forms of the same necessary equalities.

Taking \((1,2,3)\) as the anchor triple, P75 implies

\[
\boxed{
G_1
=
M_{123}^2C_{14}C_{24}
-
M_{124}^2C_{13}C_{23}
=0,
}
\]

\[
\boxed{
G_2
=
M_{123}^2C_{14}C_{34}
-
M_{134}^2C_{12}C_{23}
=0,
}
\]

and

\[
\boxed{
G_3
=
M_{123}^2C_{24}C_{34}
-
M_{234}^2C_{12}C_{13}
=0.
}
\]

These equations are obtained by cross-multiplying the P75 equal-\(q\) conditions. They remain polynomial and require no empirical division by an uncertain covariance.

P76 constructs simultaneous intervals for every covariance and third centered moment from the P76B raw-moment box, then evaluates interval extensions of \(G_1,G_2,G_3\). If any resulting interval excludes zero, the P75 model is rejected at confidence at least \(1-\alpha\).

---

## 6. P76E: denominator-free fourth-moment constraints

Let

\[
M_{1234}
=
\mathbb E\left[
\prod_{j=1}^4(X_j-\mathbb E[X_j])
\right].
\]

P75 requires

\[
M_{1234}=(1+q)P_C,
\]

where \(P_C\) is one of the equivalent covariance-pair products. P76 again removes the ratio.

For example, using the \((1,2,3)\) triple and \(P_C=C_{12}C_{34}\), define

\[
D_{123}=C_{12}C_{13}C_{23}.
\]

Then the P75 relation implies the polynomial equality

\[
\boxed{
H_{123}
=
M_{1234}D_{123}
-
(C_{12}C_{34})D_{123}
-
M_{123}^2(C_{12}C_{34})
=0.
}
\]

The implementation also evaluates the corresponding \((1,2,4)\) and \((1,3,4)\) forms. Each receives a simultaneous interval from the same P76A event. Exclusion of zero by any one of these intervals certifies rejection of the declared model.

---

## 7. P76F: simultaneous rejection theorem

Let \(\mathcal I_n\) denote the complete family of P76 tetrad, cross-triple polynomial, and fourth-moment polynomial confidence intervals constructed from one empirical four-view table.

Under IID sampling,

\[
\boxed{
\Pr\left(
\text{every true P75 polynomial value lies in its reported interval}
\right)
\ge
1-\alpha.
}
\]

Therefore

\[
\boxed{
0\notin I
\text{ for any }I\in\mathcal I_n
\quad\Longrightarrow\quad
\text{the declared P75 model is incompatible with }P
}
\]

with confidence at least \(1-\alpha\).

No multiplicity correction is added after the fact because all intervals are deterministic consequences of the one simultaneous cell-frequency event.

---

## 8. P76G: asymptotic detection of fixed tracked violations

Under IID sampling, the empirical cell law converges to the population law. Also

\[
\delta_n(\alpha)\to0.
\]

Every tracked P76 polynomial is continuous in the finite vector of raw moments. Consequently, if at least one tracked population residual is nonzero, its P76 interval shrinks to that nonzero value and eventually excludes zero.

Thus P76 is consistent against every fixed alternative that violates at least one of the tracked necessary P75 polynomial constraints.

This does **not** mean the tracked polynomial family is a complete characterization of every possible model failure. An alternative may satisfy the displayed necessary constraints while failing the stronger P75 full sixteen-cell model-reconstruction audit.

---

## 9. Synthetic adequacy stress test

The implementation uses the same valid four-view latent model employed in P75 and a deliberately misspecified comparison law that mixes it with a direct \(X_3=X_4\) coupling not explained by the declared latent state.

For the stronger 50 percent coupling mixture used in the P76 regression test, both population tetrad residuals equal

\[
|D_1|=|D_2|=0.06.
\]

At \(n=2\times10^8\) and \(\alpha=0.05\),

\[
\delta_n\approx 0.00203,
\qquad
12\delta_n\approx0.0244,
\qquad
24\delta_n\approx0.0488<0.06.
\]

So the declared tetrad violation is large enough to clear the conservative P76 design margin on the simultaneous confidence event.

This is a synthetic stress test of theorem logic. It is not biological evidence and the binary latent state is not asserted to be consciousness.

---

## 10. Why P76 does not use an ordinary chi-square claim

Goodness-of-fit statistics such as Pearson chi-square and likelihood-ratio statistics are common in latent-class analysis. However, latent-variable models can contain boundaries and singularities where ordinary regular-model asymptotics are not reliable. P76 therefore does not claim that a naive six-degree-of-freedom chi-square calibration follows automatically from the P75 dimension count.

Instead, P76 uses a finite-alphabet concentration event plus deterministic interval propagation. This is more conservative, but its coverage statement does not require Wilks-type local regularity.

The dimension count in P75 remains scientifically useful: four binary views provide six generic overidentifying degrees of freedom. P76 simply refuses to convert that count into an asymptotic null distribution without additional regularity analysis.

---

## 11. Scientific interpretation

P76 adds the fifth explicit target-side obligation after P71-P75:

1. **P71:** target provenance must not impose the bridge.
2. **P72:** target observation must preserve the distinctions used as evidence.
3. **P73:** target-channel reliability must be identifiable or externally calibrated when claimed.
4. **P74:** finite data must support stable recovery of those channel quantities.
5. **P75:** an identifiable recovered model must still face independent adequacy checks.
6. **P76:** finite data must separate a model-adequacy violation from sampling uncertainty before the model is rejected.

P76 does not establish the converse. If no interval excludes zero, the data may be insufficient, the violation may be too small, or the misspecified law may lie on the tracked necessary-constraint set. The scientifically permitted conclusion is therefore **not rejected by the current P76 certificate**, never **validated because P76 did not reject it**.

---

## 12. Provenance and novelty boundary

The ingredients have different statuses:

- Hoeffding concentration and union bounds are standard probability tools.
- Raw-moment interval propagation is standard deterministic interval reasoning applied to the P75 polynomial system.
- Latent-class model fit, local dependence, algebraic constraints, and nonstandard asymptotics at latent-model singularities belong to established statistical literature.
- The P75 population constraints are the immediate repository input.
- The repository-specific P76 contribution is their assembly into one explicit finite-sample, familywise-valid, denominator-free **rejection gate** inside the P71-P76 physical-to-experiential bridge test architecture.

See [P76 equation and provenance record](p76_equation_provenance.md) for equation-level classification.

---

## 13. Reproducibility

Implementation:

- [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py)

Regression tests:

- [`test_finite_sample_target_model_adequacy.py`](../tests/test_finite_sample_target_model_adequacy.py)

Population theorem used by P76:

- [P75 target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md)

The physical-to-experiential bridge remains open.
