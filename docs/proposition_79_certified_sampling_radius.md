# Proposition 79: Certified Rational Sampling-Radius Envelope

## Status

**Proved numerical-certification theorem with an exact-rational implementation.**

P79 closes a deliberately open numerical gap between [P77](proposition_77_full_law_model_set_separation.md) and [P78](proposition_78_certified_continuous_model_separation.md).

P77 gives the simultaneous finite-alphabet Hoeffding radius

\[
\varepsilon_{n,K}(\alpha)
=
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
\]

P78 can certify a rational lower bound on distance from an empirical law to the complete continuous P75 model family. To turn that optimization certificate into a P77 rejection, however, P78 requires a **mathematically valid upper bound** on \(\varepsilon_{n,K}(\alpha)\). Converting an ordinary floating-point evaluation of `log` and `sqrt` into a rational number does not prove that the resulting rational lies above the exact mathematical radius.

P79 supplies that missing one-sided numerical certificate for rational \(\alpha\). It constructs an exact rational bracket for the logarithm by a positive atanh series with an explicit tail bound, then converts the upper logarithm bound into a dyadic rational square-root ceiling using integer arithmetic.

The central result is

\[
\boxed{
\underline\varepsilon_{n,K,\alpha}^{(m,b)}
\le
\varepsilon_{n,K}(\alpha)
\le
\overline\varepsilon_{n,K,\alpha}^{(m,b)}
}
\]

with both endpoints rational and computable without relying on floating-point directionality.

Consequently, if P78 returns a certified model-distance lower bound \(L_{\mathcal B}\) and

\[
\boxed{
L_{\mathcal B}
>
\overline\varepsilon_{n,16,\alpha}^{(m,b)},
}
\]

then the strict P77 full-law rejection condition is certified entirely in exact rational arithmetic on the optimization and radius-comparison sides.

P79 is a numerical-certification layer. It does not strengthen Hoeffding's inequality, does not validate a model when rejection fails, does not identify a latent state with consciousness, and does not solve the physical-to-experiential bridge.

---

## 1. Exact problem statement

Let

\[
n\in\mathbb N,
\qquad
K\in\mathbb N,
\qquad
\alpha\in\mathbb Q\cap(0,1).
\]

Define

\[
x=\frac{2K}{\alpha}>1.
\]

P77 requires the radius

\[
\varepsilon
=
\sqrt{\frac{\log x}{2n}}.
\]

The issue addressed by P79 is not the probabilistic theorem itself. The issue is the numerical direction of the final comparison. A computed decimal \(\widetilde\varepsilon\) may be extremely accurate while still being slightly below the exact \(\varepsilon\). If a rejection condition uses

\[
L>\widetilde\varepsilon,
\]

that comparison is rigorous only when \(\widetilde\varepsilon\) is known to be an upper bound.

P79 therefore constructs a certified rational upper envelope rather than assuming the direction of a floating approximation.

---

## 2. P79A: power-of-two argument reduction

Write

\[
k=\lfloor\log_2 x\rfloor,
\qquad
r=\frac{x}{2^k}.
\]

Then

\[
1\le r<2
\]

and

\[
\boxed{
\log x=k\log 2+\log r.
}
\]

Because \(x\) is rational, the integer \(k\) can be found by exact integer and rational comparisons. No floating logarithm is required for the reduction.

The reason for this reduction is numerical as well as mathematical. The positive series used below converges rapidly when its transformed argument is at most \(1/3\). Reducing every logarithm to \([1,2]\) guarantees exactly that condition.

---

## 3. P79B: rational logarithm bracket

For \(t\in[1,2]\), define

\[
y(t)=\frac{t-1}{t+1}.
\]

Then

\[
0\le y(t)\le\frac13
\]

and the standard identity

\[
\log t
=
2\operatorname{atanh}(y)
=
2\sum_{j=0}^{\infty}
\frac{y^{2j+1}}{2j+1}
\]

has nonnegative terms.

For an integer \(m\ge1\), define the truncated sum

\[
S_m(t)
=
2\sum_{j=0}^{m-1}
\frac{y(t)^{2j+1}}{2j+1}.
\]

Because every omitted term is nonnegative,

\[
S_m(t)\le\log t.
\]

For the tail,

\[
\begin{aligned}
R_m(t)
&=
2\sum_{j=m}^{\infty}
\frac{y^{2j+1}}{2j+1}\\
&\le
\frac{2}{2m+1}
\sum_{j=m}^{\infty}y^{2j+1}\\
&=
\frac{2y^{2m+1}}
{(2m+1)(1-y^2)}.
\end{aligned}
\]

Therefore

\[
\boxed{
S_m(t)
\le
\log t
\le
S_m(t)+
\frac{2y(t)^{2m+1}}
{(2m+1)(1-y(t)^2)}.
}
\]

For rational \(t\), every quantity in this bracket is rational.

Applying this independently to \(2\) and \(r\) gives rational values

\[
\underline L_m(x)
\le
\log x
\le
\overline L_m(x).
\]

Since \(y\le1/3\), the remainder decreases geometrically with \(m\). This is why the implementation does not apply the series directly to a large value such as \(2K/\alpha\).

---

## 4. P79C: dyadic square-root enclosure

Define

\[
z_-
=
\frac{\underline L_m(x)}{2n},
\qquad
z_+
=
\frac{\overline L_m(x)}{2n}.
\]

Then

\[
0\le z_-
\le
\frac{\log x}{2n}
\le z_+.
\]

Choose a dyadic denominator

\[
D=2^b,
\qquad b\ge1.
\]

Define

\[
\underline\varepsilon^{(m,b)}
=
\frac{\left\lfloor D\sqrt{z_-}\right\rfloor}{D}
\]

and

\[
\overline\varepsilon^{(m,b)}
=
\frac{\left\lceil D\sqrt{z_+}\right\rceil}{D}.
\]

Then monotonicity of the square root gives

\[
\boxed{
\underline\varepsilon^{(m,b)}
\le
\sqrt{\frac{\log x}{2n}}
\le
\overline\varepsilon^{(m,b)}.
}
\]

The implementation does not evaluate either square root as a floating number. For a rational \(z=p/q\), it tests candidate dyadic numerators by the exact integer inequality

\[
a^2q
\lesseqgtr
pD^2.
\]

The lower and upper dyadic numerators are therefore certified by integer arithmetic.

---

## 5. P79D: convergence of the rational envelope

Let

\[
\Delta_m(x)
=
\overline L_m(x)-\underline L_m(x).
\]

The logarithm remainder bound implies

\[
\Delta_m(x)\to0
\qquad\text{as }m\to\infty.
\]

The dyadic rounding contributes less than \(1/D\) on each side. Since

\[
\sqrt{a}-\sqrt{b}
\le
\sqrt{a-b}
\qquad(a\ge b\ge0),
\]

one convenient deterministic width bound is

\[
\boxed{
0\le
\overline\varepsilon^{(m,b)}
-
\underline\varepsilon^{(m,b)}
\le
\sqrt{\frac{\Delta_m(x)}{2n}}
+
2^{1-b}.
}
\]

Hence

\[
\overline\varepsilon^{(m,b)}
-
\underline\varepsilon^{(m,b)}
\to0
\]

as both \(m\to\infty\) and \(b\to\infty\).

The certificate can therefore be tightened deterministically without changing the statistical theorem.

---

## 6. P79E: exact P77/P78 handoff

P78 returns a rational lower bound

\[
L_{\mathcal B}
\le
 d_\infty(\widehat P,\mathcal M_{4,2}).
\]

P79 returns

\[
\varepsilon_{n,16}(\alpha)
\le
\overline\varepsilon_{n,16,\alpha}^{(m,b)}.
\]

Therefore

\[
L_{\mathcal B}
>
\overline\varepsilon_{n,16,\alpha}^{(m,b)}
\]

implies

\[
 d_\infty(\widehat P,\mathcal M_{4,2})
>
\varepsilon_{n,16}(\alpha),
\]

which is exactly the strict separation required by P77.

Thus

\[
\boxed{
L_{\mathcal B}
>
\overline\varepsilon_{n,16,\alpha}^{(m,b)}
\Longrightarrow
\text{P77 rejection is numerically certified.}
}
\]

The logical direction matters. P79 supplies an **upper** bound on sampling uncertainty, while P78 supplies a **lower** bound on model distance. Reversing either direction would invalidate the rejection certificate.

---

## 7. L1 envelope

P77 also uses the conservative joint-law radius

\[
\delta_{n,K}(\alpha)
=
\min\{2,K\varepsilon_{n,K}(\alpha)\}.
\]

Therefore P79 immediately gives

\[
\boxed{
\delta_{n,K}(\alpha)
\le
\min\left\{2,
K\overline\varepsilon_{n,K,\alpha}^{(m,b)}
\right\}.
}
\]

The implementation reports this rational L1 upper envelope as well.

---

## 8. Example: the P75 sixteen-cell law

For the four-view P75 model,

\[
K=16.
\]

At

\[
\alpha=0.05=\frac1{20},
\]

one has

\[
\frac{2K}{\alpha}=640.
\]

With \(m=12\), the rational logarithm bracket for \(\log 640\) is already extremely narrow because the argument reduction evaluates only \(\log 2\) and one residual logarithm with transformed series parameter no larger than \(1/3\). A dyadic square-root denominator with \(b=48\) then makes the rounding component far smaller than ordinary experimental sampling uncertainty.

The exact numerical values are produced by the implementation rather than hard-coded into the theorem. The scientific point is the direction of certification, not the number of printed decimal places.

---

## 9. Implementation

The implementation is

[`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py).

Its protocol is:

1. require \(n\) and \(K\) as positive integers;
2. require \(\alpha\) as an exact `Fraction` in \((0,1)\);
3. form \(x=2K/\alpha\) exactly;
4. reduce \(x=2^kr\) with exact comparisons and \(1\le r<2\);
5. compute rational lower and upper logarithm bounds with the explicit positive-series tail;
6. divide the logarithm bracket by \(2n\) exactly;
7. compute dyadic square-root floor and ceiling bounds using integer comparisons;
8. return the certified L-infinity radius bracket and the induced L1 upper envelope;
9. provide a direct helper that feeds the certified upper radius into P78's strict P77 rejection gate.

Tests are in

[`test_certified_sampling_radius.py`](../tests/test_certified_sampling_radius.py).

---

## 10. Scientific boundary

P79 establishes a rigorous numerical envelope for a standard finite-sample concentration radius. It does **not** establish that:

- Hoeffding's bound is the sharpest possible statistical radius;
- the P75 latent model is true when it is not rejected;
- the P75 latent variable is consciousness;
- any target-measurement channel is semantically valid merely because it is identifiable;
- consciousness is reducible to current physics;
- consciousness is irreducible to physics;
- the physical-to-experiential bridge has been solved.

The physical-to-experiential bridge remains open.

---

## 11. Dependency and contribution boundary

P79 depends on the P77 sampling-radius formula and the P78 requirement for a certified sampling-radius upper bound. The probability inequality itself is standard. The repository-specific contribution is the explicit exact-rational evaluation layer that prevents a floating-point approximation from becoming an unexamined weak link in the P77/P78 rejection chain.

The resulting target-side sequence is now:

\[
\boxed{
\text{P75 model family}
\to
\text{P76 finite necessary-constraint rejection}
\to
\text{P77 full-law separation theorem}
\to
\text{P78 certified continuous model-distance lower bound}
\to
\text{P79 certified rational sampling-radius upper bound}.
}
\]

This closes a numerical certification gap. It does not close the physical-to-experiential bridge itself.
