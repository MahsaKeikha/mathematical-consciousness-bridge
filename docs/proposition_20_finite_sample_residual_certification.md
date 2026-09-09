# Proposition 20 - Finite-Sample Certification of Fundamental Residual Information

## Status

**Proved finite-sample theorem under an explicit finite-alphabet IID sampling model.**

P20 turns the population-level stochastic criterion from [Proposition 19](proposition_19_fundamental_physical_sufficiency.md),

\[
I(E;\Omega\mid T)=0,
\]

into a finite-data confidence statement. The theorem does not prove that consciousness is nonphysical. A certified positive residual shows that the declared physical descriptor \(T\) is not sufficient for the declared target \(E\) under the stated sampling model.

---

# 1. Sampling model

Let

\[
Z_i=(\Omega_i,T_i,E_i),
\qquad i=1,\ldots,n,
\]

be IID samples from a population law \(P\) on finite declared alphabets with cardinalities

\[
d_\Omega,\qquad d_T,\qquad d_E.
\]

The declared joint alphabet size is

\[
\boxed{M=d_\Omega d_T d_E.}
\]

Let \(\widehat P_n\) be the empirical joint distribution and define

\[
I_P=I_P(E;\Omega\mid T),
\qquad
\widehat I_n=I_{\widehat P_n}(E;\Omega\mid T).
\]

The finite-sample problem is to construct an explicit interval

\[
\boxed{L_n\le I_P\le U_n}
\]

with coverage at least \(1-\alpha\).

---

# 2. Simultaneous empirical-distribution radius

For one declared joint category \(z\), Hoeffding's inequality gives

\[
\Pr\left(
|\widehat P_n(z)-P(z)|>a
\right)
\le
2e^{-2na^2}.
\]

Applying a union bound over the \(M\) declared categories gives

\[
\Pr\left(
\max_z|\widehat P_n(z)-P(z)|>a
\right)
\le
2M e^{-2na^2}.
\]

Set

\[
\boxed{
a_n(\alpha)
=
\sqrt{
\frac{1}{2n}
\log\frac{2M}{\alpha}
}.
}
\]

Then, with probability at least \(1-\alpha\),

\[
\|\widehat P_n-P\|_1
\le
M a_n(\alpha).
\]

Since total variation is one half of the \(L^1\) distance,

\[
\boxed{
\|\widehat P_n-P\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
:=
\min\left\{
1,
\frac{M}{2}
\sqrt{
\frac{1}{2n}
\log\frac{2M}{\alpha}
}
\right\}.
}
\]

This radius is conservative. Its advantage is that every step follows directly from a standard concentration inequality and a union bound.

**Source:** Wassily Hoeffding, 1963, "Probability Inequalities for Sums of Bounded Random Variables," *Journal of the American Statistical Association* 58(301): 13-30. [DOI 10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).

---

# 3. Entropy continuity lemma for an upper TV radius

For a finite alphabet of size \(d\), define

\[
h_2(r)
=
-r\log r-(1-r)\log(1-r)
\]

with the usual continuous convention at \(r=0\) and \(r=1\).

Define

\[
\boxed{
c_d(r)=
\begin{cases}
0, & d=1,\\[4pt]
h_2(r)+r\log(d-1),
& d>1\text{ and }r<1-1/d,\\[4pt]
\log d,
& d>1\text{ and }r\ge1-1/d.
\end{cases}
}
\]

## Lemma

If probability laws \(P_d\) and \(Q_d\) on the same \(d\)-symbol alphabet satisfy

\[
\|P_d-Q_d\|_{\mathrm{TV}}\le r,
\]

then

\[
\boxed{
|H(P_d)-H(Q_d)|\le c_d(r).
}
\]

## Proof

Let the exact total variation distance be \(\delta\le r\). The common probability mass

\[
\sum_x\min\{P_d(x),Q_d(x)\}=1-\delta
\]

constructs a coupling \((X,Y)\) with

\[
\Pr(X\ne Y)=\delta.
\]

For this coupling,

\[
H(X)-H(Y)
\le
H(X\mid Y).
\]

The standard finite-alphabet decoding bound gives

\[
H(X\mid Y)
\le
h_2(\delta)+\delta\log(d-1).
\]

The same argument with \(X\) and \(Y\) exchanged bounds \(H(Y)-H(X)\). The function

\[
h_2(\delta)+\delta\log(d-1)
\]

is increasing on \([0,1-1/d]\). Therefore, when \(r<1-1/d\), replacing \(\delta\) by the known upper radius \(r\) is valid. For larger \(r\), the universal entropy range \(0\le H\le\log d\) gives the safe bound \(\log d\). \(\square\)

The entropy and conditional-information identities used here follow standard information theory. See [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006).

---

# 4. P20 theorem - finite-sample CMI certificate

Conditional mutual information can be written as

\[
\boxed{
I(E;\Omega\mid T)
=
H(E,T)+H(\Omega,T)-H(T)-H(E,\Omega,T).
}
\]

Marginalization cannot increase total variation. Therefore, on the event

\[
\|\widehat P_n-P\|_{\mathrm{TV}}\le\tau_n,
\]

each marginal distribution appearing in the four entropy terms is also within TV radius \(\tau_n\) of its population counterpart.

Define

\[
\begin{aligned}
\Delta_{\mathrm{CMI}}(r)
=
\min\Bigl\{
&\min(\log d_\Omega,\log d_E),\\
&c_{d_Ed_T}(r)
+c_{d_\Omega d_T}(r)
+c_{d_T}(r)
+c_{d_Ed_\Omega d_T}(r)
\Bigr\}.
\end{aligned}
\]

The first term is the full possible range of conditional mutual information. The second term is the continuity bound obtained from the four entropy terms.

## Proposition

With probability at least \(1-\alpha\),

\[
\boxed{
|I_P-\widehat I_n|
\le
\Delta_{\mathrm{CMI}}\bigl(\tau_n(\alpha)\bigr).
}
\]

Hence the interval

\[
\boxed{
L_n
=
\max\left\{
0,
\widehat I_n-\Delta_{\mathrm{CMI}}(\tau_n)
\right\},
}
\]

\[
\boxed{
U_n
=
\min\left\{
\min(\log d_\Omega,\log d_E),
\widehat I_n+\Delta_{\mathrm{CMI}}(\tau_n)
\right\}
}
\]

satisfies

\[
\boxed{
\Pr\left(L_n\le I_P\le U_n\right)
\ge
1-\alpha.
}
\]

## Proof

The Hoeffding and union-bound argument gives the joint TV event with probability at least \(1-\alpha\). TV contraction under marginalization transfers the same radius to the four entropy marginals. Applying the entropy continuity lemma to each entropy term and then the triangle inequality gives the stated \(\Delta_{\mathrm{CMI}}\) bound. Intersecting with the universal range

\[
0\le I(E;\Omega\mid T)
\le
\min(\log d_\Omega,\log d_E)
\]

gives \([L_n,U_n]\). \(\square\)

---

# 5. Certified failure of stochastic physical sufficiency

P19 states that stochastic physical sufficiency requires

\[
\boxed{I(E;\Omega\mid T)=0.}
\]

P20 therefore gives a finite-data rejection certificate:

\[
\boxed{
L_n>0
\Longrightarrow
I_P(E;\Omega\mid T)>0
\quad\text{with confidence at least }1-\alpha.
}
\]

Under the declared finite-alphabet IID model, this rules out the screening-off condition associated with that declared \(T\).

The correct first interpretation is

\[
\boxed{
\text{certified residual}
\Longrightarrow
\text{declared }T\text{ is insufficient for }E.
}
\]

It does not justify the stronger statement

\[
\text{certified residual}
\Longrightarrow
\text{nonphysical consciousness}.
\]

That stronger implication is not part of P20.

---

# 6. Synthetic numerical checkpoint

Consider a declared binary underlying coordinate and binary target with one physical label,

\[
d_\Omega=2,
\qquad
d_T=1,
\qquad
d_E=2,
\]

so \(M=4\). Suppose the empirical residual is the maximum binary value

\[
\widehat I_n=\log 2
\]

with

\[
n=10{,}000,
\qquad
\alpha=0.05.
\]

The P20 radius is

\[
\tau_n\approx0.0318596,
\]

and the resulting conservative CMI continuity radius is

\[
\Delta_{\mathrm{CMI}}\approx0.458446\text{ nats}.
\]

Therefore

\[
\boxed{
L_n\approx0.234702\text{ nats}>0.
}
\]

This is a synthetic mathematical checkpoint, not an empirical consciousness result.

---

# 7. Why the theorem is deliberately conservative

The certificate scales with the declared joint alphabet size \(M\). This can become loose in high-dimensional systems. P20 is therefore a baseline theorem, not the final estimator for realistic neuroscience or fundamental physics.

Its role is to establish a transparent finite-data standard before introducing sharper tools. Future work may replace the cellwise Hoeffding radius with tighter multinomial concentration, structured estimators, cross-fitting, conditional-randomization methods, or model-based confidence sets. Any replacement must preserve explicit coverage assumptions and must be tested against adversarial finite-sample cases.

---

# 8. Assumptions that must be declared

P20 requires all of the following:

1. the samples are IID under the declared sampling regime;
2. \(\Omega\), \(T\), and \(E\) are represented on finite declared alphabets;
3. the declared alphabet sizes are not smaller than the true support cardinalities;
4. the observed labels correspond to the variables used in the theorem;
5. the target \(E\) is defined independently of the physical descriptor \(T\);
6. the confidence level \(\alpha\) is fixed before interpreting the certificate;
7. selection, repeated testing, and model search are accounted for separately when present.

Violating these assumptions can invalidate nominal coverage.

---

# 9. Scientific interpretation hierarchy

A positive lower confidence bound should trigger the following sequence:

1. audit sampling independence and preprocessing;
2. audit target measurement and reporting noise;
3. audit physical variables omitted from \(T\);
4. audit spatial, temporal, and system-boundary choices;
5. enlarge \(T\) with plausible missing physical variables;
6. repeat the P19 and P20 sufficiency tests;
7. seek independent replication across protocols, subjects, laboratories, and measurement modalities where applicable;
8. only after those controls, evaluate whether the surviving residual motivates a new primitive.

This hierarchy prevents a finite-sample statistical residual from being promoted directly into an ontological conclusion.

---

# 10. Direct audit path

| Item | Direct link |
| --- | --- |
| population sufficiency theorem | [P19](proposition_19_fundamental_physical_sufficiency.md) |
| finite-sample implementation | [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py) |
| claim-level tests | [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py) |
| information-theory source | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) |
| concentration source | [Hoeffding 1963](https://doi.org/10.1080/01621459.1963.10500830) |
| citation rules | [Citation and Reference Policy](citation_and_reference_policy.md) |
| empirical burden | [Falsification Program](falsification_program.md) |

The implementation and tests use natural logarithms, so information values are reported in nats.
