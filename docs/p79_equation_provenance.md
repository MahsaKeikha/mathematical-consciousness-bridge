# P79 Equation and Provenance Record

## Proposition

[P79: Certified Rational Sampling-Radius Envelope](proposition_79_certified_sampling_radius.md)

## Role in the research chain

P77 states the finite-alphabet confidence-region separation theorem. P78 supplies an exact-rational lower bound on distance from the empirical law to the complete continuous P75 model family. P79 supplies the complementary exact-rational **upper bound** on the P77 sampling radius required for a strict, directionally valid rejection comparison.

P79 is a numerical-certification result. The underlying concentration inequality and logarithm identities are standard; the repository-specific contribution is the explicit one-sided exact-rational evaluation layer and its direct P77/P78 interface.

## Core equations

### P77 radius inherited by P79

\[
\varepsilon_{n,K}(\alpha)
=
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
\]

Source role: inherited statistical quantity from P77.

### Exact argument reduction

\[
x=\frac{2K}{\alpha},
\qquad
k=\lfloor\log_2x\rfloor,
\qquad
r=\frac{x}{2^k}\in[1,2),
\]

so

\[
\log x=k\log2+\log r.
\]

Source role: elementary logarithm identity used to guarantee rapid rational-series convergence.

### Positive atanh expansion

For

\[
y(t)=\frac{t-1}{t+1},
\]

\[
\log t
=
2\sum_{j=0}^{\infty}\frac{y(t)^{2j+1}}{2j+1}.
\]

On \(t\in[1,2]\), \(0\le y(t)\le1/3\).

Source role: standard power-series identity.

### Explicit rational tail bound

With

\[
S_m(t)=2\sum_{j=0}^{m-1}\frac{y(t)^{2j+1}}{2j+1},
\]

P79 uses

\[
0\le\log t-S_m(t)
\le
\frac{2y(t)^{2m+1}}{(2m+1)(1-y(t)^2)}.
\]

Derivation: bound every omitted denominator \(2j+1\) by the first omitted denominator \(2m+1\), then sum the remaining geometric series.

### Rational logarithm bracket

Combining the bounds for \(2\) and \(r\) gives

\[
\underline L_m(x)
\le
\log x
\le
\overline L_m(x).
\]

All quantities are rational when \(x\) is rational.

### Dyadic square-root bracket

For

\[
z_-=\frac{\underline L_m(x)}{2n},
\qquad
z_+=\frac{\overline L_m(x)}{2n},
\qquad
D=2^b,
\]

P79 defines

\[
\underline\varepsilon
=
\frac{\lfloor D\sqrt{z_-}\rfloor}{D},
\qquad
\overline\varepsilon
=
\frac{\lceil D\sqrt{z_+}\rceil}{D}.
\]

The implementation determines the floor and ceiling by exact integer comparisons rather than floating square roots.

### Certified envelope

\[
\boxed{
\underline\varepsilon
\le
\varepsilon_{n,K}(\alpha)
\le
\overline\varepsilon.
}
\]

### P78/P79 rejection handoff

If P78 supplies

\[
L_{\mathcal B}
\le
d_\infty(\widehat P,\mathcal M_{4,2})
\]

and P79 supplies

\[
\varepsilon_{n,16}(\alpha)
\le\overline\varepsilon,
\]

then

\[
\boxed{
L_{\mathcal B}>\overline\varepsilon
\Longrightarrow
 d_\infty(\widehat P,\mathcal M_{4,2})
>
\varepsilon_{n,16}(\alpha),
}
\]

which triggers P77 full-law rejection.

## Implementation provenance

- source: [`src/consciousness_bridge/certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py)
- tests: [`tests/test_certified_sampling_radius.py`](../tests/test_certified_sampling_radius.py)
- theorem figure: [`docs/figures/p79_certified_sampling_radius.svg`](figures/p79_certified_sampling_radius.svg)
- predecessor statistical theorem: [P77](proposition_77_full_law_model_set_separation.md)
- predecessor optimization theorem: [P78](proposition_78_certified_continuous_model_separation.md)

## Scientific boundary

P79 certifies numerical inequality direction for the P77 sampling radius. It does not establish the truth of the P75 target model, does not identify a latent state with experience, and does not solve the physical-to-experiential bridge.
