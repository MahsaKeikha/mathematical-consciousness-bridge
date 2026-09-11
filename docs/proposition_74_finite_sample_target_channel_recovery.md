# Proposition 74: finite-sample target-channel recovery certification

## Purpose

P73 is a population identifiability theorem. Under a nondegenerate binary three-view latent model, it shows that the observable joint law determines the latent prevalence and all three binary target-view channels up to one common latent-label swap. It also identifies the P72 single-view stability coefficients

\[
\gamma_j=|b_j|.
\]

P74 asks the next experimental question:

> If the three-view joint law is observed only through finitely many samples, when can the P73 inversion be certified without confusing sampling noise with target-channel structure?

The result below builds one conservative simultaneous confidence event for the complete observed eight-cell law and propagates that event through the P73 inversion. It deliberately refuses recovery when the finite-data covariance margins do not separate the observed law from the P73 degeneracy boundary.

P74 also closes a distinction that matters scientifically. Finite-data recovery should not mean only estimating a reliability magnitude. When the nondegeneracy gate passes, the same confidence event certifies the latent prevalence orbit, all three P72 stability coefficients, each binary channel offset, and the unordered pair of latent-conditioned response probabilities for every view. The unordered representation is the correct identifiable object before an external semantic anchor chooses a latent-label orientation.

This is a statistical theorem under a declared latent-variable model. It does not validate that model empirically, assign semantic meaning to the latent labels, identify the latent state with consciousness, or establish the physical-to-experiential bridge.

---

## 1. Model and sampling assumptions

Fix one physical stratum \(T=t\). Assume the P73 population model:

1. \(S\in\{-1,+1\}\) is a declared binary latent target;
2. \(X_1,X_2,X_3\in\{-1,+1\}\) are binary target views;
3. the three views are conditionally independent given \(S\);
4. the latent prevalence is interior;
5. every P73 loading is nonzero;
6. \(n\) observed triples are IID draws from the same three-view population law \(P\).

Let \(\widehat P\) be the empirical distribution on the eight cells of \(\{-1,+1\}^3\). Define

\[
\mu_j=\mathbb E[X_j],
\qquad
C_{ij}=\operatorname{Cov}(X_i,X_j),
\]

and

\[
M_{123}
=
\mathbb E[(X_1-\mu_1)(X_2-\mu_2)(X_3-\mu_3)].
\]

Write hats for empirical analogues. P73 parameterizes each binary target view by

\[
\mathbb E[X_j\mid S]=a_j+b_jS,
\]

with latent mean \(m=\mathbb E[S]\), latent variance \(v=1-m^2\), and stability \(\gamma_j=|b_j|\).

---

## 2. One simultaneous eight-cell confidence event

For each of the eight cells \(x\), the empirical cell frequency is an average of Bernoulli indicators. Hoeffding concentration gives

\[
\Pr\left(
|\widehat P(x)-P(x)|>\varepsilon
\right)
\le
2e^{-2n\varepsilon^2}.
\]

A union bound over the eight cells yields

\[
\Pr\left(
\max_x|\widehat P(x)-P(x)|>\varepsilon
\right)
\le
16e^{-2n\varepsilon^2}.
\]

For confidence level \(1-\alpha\), define

\[
\boxed{
\varepsilon_n(\alpha)
=
\sqrt{\frac{\log(16/\alpha)}{2n}}.
}
\]

Then, with probability at least \(1-\alpha\),

\[
\max_x|\widehat P(x)-P(x)|
\le
\varepsilon_n(\alpha).
\]

Therefore

\[
\boxed{
\|\widehat P-P\|_1
\le
\delta_n(\alpha)
:=
\min\left\{
2,
8\sqrt{\frac{\log(16/\alpha)}{2n}}
\right\}.
}
\]

The cap at 2 uses the maximum possible \(L^1\) distance between probability distributions. Every confidence statement below is deterministic on this same event, so no additional confidence spending is introduced.

---

## 3. Moment perturbation bounds

For any \(f:\{-1,+1\}^3\to[-1,1]\),

\[
\left|
\mathbb E_{\widehat P}f-
\mathbb E_P f
\right|
\le
\|\widehat P-P\|_1
\le
\delta_n.
\]

Hence each first moment, pair-product moment, and triple-product moment differs from its population value by at most \(\delta_n\).

### 3.1 First moments

Immediately,

\[
\boxed{|\widehat\mu_j-\mu_j|\le\delta_n.}
\]

For later channel recovery define the signed interval

\[
I_{\mu_j}
=
[\widehat\mu_j-\delta_n,\widehat\mu_j+\delta_n]
\cap[-1,1].
\]

### 3.2 Pair covariance

Because

\[
C_{ij}=\mathbb E[X_iX_j]-\mu_i\mu_j
\]

and \(|\mu_i|,|\widehat\mu_i|\le1\),

\[
|\widehat\mu_i\widehat\mu_j-\mu_i\mu_j|
\le
|\widehat\mu_i-\mu_i|
+
|\widehat\mu_j-\mu_j|
\le
2\delta_n.
\]

Therefore

\[
\boxed{
|\widehat C_{ij}-C_{ij}|
\le
3\delta_n.
}
\]

Define

\[
r_C:=3\delta_n.
\]

The signed covariance interval is

\[
I_{C_{ij}}
=
[\widehat C_{ij}-r_C,\widehat C_{ij}+r_C]
\cap[-1,1].
\]

For absolute values define

\[
L_{ij}=\max\{|\widehat C_{ij}|-r_C,0\},
\qquad
U_{ij}=\min\{|\widehat C_{ij}|+r_C,1\}.
\]

### 3.3 Third centered moment

Let

\[
r_{ij}=\mathbb E[X_iX_j],
\qquad
r_{123}=\mathbb E[X_1X_2X_3].
\]

Then

\[
M_{123}
=
r_{123}
-\mu_1r_{23}
-\mu_2r_{13}
-\mu_3r_{12}
+2\mu_1\mu_2\mu_3.
\]

The raw triple term contributes at most \(\delta_n\). Each mean-times-pair term contributes at most \(2\delta_n\), for a total of at most \(6\delta_n\). The difference between products of three means is at most \(3\delta_n\), and the leading factor 2 contributes at most \(6\delta_n\). Hence

\[
\boxed{
|\widehat M_{123}-M_{123}|
\le
13\delta_n.
}
\]

Define

\[
r_M:=13\delta_n.
\]

The signed interval is

\[
I_M
=
[\widehat M_{123}-r_M,\widehat M_{123}+r_M].
\]

For the absolute moment define

\[
L_M=\max\{|\widehat M_{123}|-r_M,0\},
\qquad
U_M=|\widehat M_{123}|+r_M.
\]

These constants are conservative. P74 does not claim them to be minimax-optimal.

---

## 4. The P74 nondegeneracy gate

P73 divides by products of pair covariances. A finite-data procedure should therefore not perform that inversion merely because empirical covariances happen to be nonzero.

P74 requires

\[
\boxed{
L_{12}>0,
\qquad
L_{13}>0,
\qquad
L_{23}>0.
}
\]

When this condition fails, the correct output is

> **P73 nondegeneracy is not certified by these finite data.**

That output does not prove that a population covariance is zero and does not prove that the latent model is nonidentifiable in truth. It says only that the present sample does not safely separate the joint law from the inversion singularity.

If all three lower margins are positive, each signed covariance interval excludes zero. The nondegenerate P73 model also requires

\[
C_{12}C_{13}C_{23}>0.
\]

Therefore an empirical sign product that is nonpositive after all three intervals exclude zero is incompatible with the nondegenerate P73 model on the simultaneous confidence event.

---

## 5. Finite-sample inversion of the latent imbalance

P73 gives

\[
q
=
\frac{M_{123}^2}{C_{12}C_{13}C_{23}}
=
\frac{|M_{123}|^2}{|C_{12}||C_{13}||C_{23}|}.
\]

When the nondegeneracy gate passes, define

\[
\boxed{
q_L
=
\frac{L_M^2}{U_{12}U_{13}U_{23}},
\qquad
q_U
=
\frac{U_M^2}{L_{12}L_{13}L_{23}}.
}
\]

Then

\[
q\in[q_L,q_U].
\]

P73 gives

\[
|m|=\sqrt{\frac{q}{q+4}},
\qquad
v=\frac4{q+4}.
\]

Since the first map is increasing and the second decreasing,

\[
\boxed{
|m|
\in
\left[
\sqrt{\frac{q_L}{q_L+4}},
\sqrt{\frac{q_U}{q_U+4}}
\right]
=:[m_L,m_U],
}
\]

and

\[
\boxed{
v\in\left[\frac4{q_U+4},\frac4{q_L+4}\right]=:[v_L,v_U].}
\]

Because the global latent-label swap remains observationally invisible, the prevalence \(\pi=P(S=+1)\) is reported as a two-interval orbit:

\[
\boxed{
\pi
\in
\left[
\frac{1-m_U}{2},
\frac{1-m_L}{2}
\right]
\cup
\left[
\frac{1+m_L}{2},
\frac{1+m_U}{2}
\right].
}
\]

An external semantic anchor may choose an orientation, but P74 does not manufacture one statistically.

---

## 6. Simultaneous confidence intervals for P72 stability

P73 gives

\[
\gamma_1
=
\sqrt{\frac{|C_{12}C_{13}|}{v|C_{23}|}},
\qquad
\gamma_2
=
\sqrt{\frac{|C_{12}C_{23}|}{v|C_{13}|}},
\qquad
\gamma_3
=
\sqrt{\frac{|C_{13}C_{23}|}{v|C_{12}|}}.
\]

Every factor is positive after the nondegeneracy gate. Monotone interval propagation gives, for example,

\[
\boxed{
\gamma_{1,L}
=
\sqrt{\frac{L_{12}L_{13}}{v_UU_{23}}},
\qquad
\gamma_{1,U}
=
\sqrt{\frac{U_{12}U_{13}}{v_LL_{23}}}.
}
\]

The corresponding bounds for \(\gamma_2\) and \(\gamma_3\) follow by cyclic permutation. Because binary-channel stability lies in \([0,1]\), upper endpoints may be clipped at 1 without weakening coverage. Thus

\[
\boxed{
\gamma_j\in[\gamma_{j,L},\gamma_{j,U}]
\quad\text{simultaneously for }j=1,2,3.
}
\]

P73 also proves

\[
\gamma_{123}\ge\max_j\gamma_j,
\]

so P74 obtains

\[
\boxed{
\gamma_{123}\ge\max_j\gamma_{j,L}.
}
\]

---

## 7. Full binary-channel recovery up to latent-label swap

Stability alone does not specify a general asymmetric binary channel. P74 therefore also certifies the channel offset and the two latent-conditioned response probabilities.

For view \(j\), let \(k,\ell\) be the other two views. P73 gives

\[
M_{123}=-2mv\,b_1b_2b_3
\]

and

\[
C_{k\ell}=b_kb_\ell v.
\]

Dividing the two identities yields the label-invariant product

\[
\boxed{
 b_jm=-\frac{M_{123}}{2C_{k\ell}}.
}
\]

This quantity is invariant under the common latent-label swap because both \(m\) and \(b_j\) change sign.

Since

\[
\mu_j=a_j+b_jm,
\]

we obtain

\[
\boxed{
 a_j=\mu_j-b_jm.
}
\]

### 7.1 Interval construction

After the P74 covariance gate passes, the signed denominator interval \(I_{C_{k\ell}}\) excludes zero. For two intervals \(I_N=[N_L,N_U]\) and \(I_D=[D_L,D_U]\) with \(0\notin I_D\), define the exact ratio hull

\[
I_N/I_D
=
\left[
\min_{u\in\{N_L,N_U\},\,v\in\{D_L,D_U\}}\frac uv,
\max_{u\in\{N_L,N_U\},\,v\in\{D_L,D_U\}}\frac uv
\right].
\]

Then

\[
\boxed{
I_{b_jm}
=-\frac12\left(I_M/I_{C_{k\ell}}\right).
}
\]

Combining this with the first-moment interval gives

\[
\boxed{
I_{a_j}
=
I_{\mu_j}-I_{b_jm},
}
\]

with the endpoint hull clipped to the physically valid interval \([-1,1]\).

### 7.2 Label-invariant channel orbit

The two latent-conditioned output means are

\[
a_j-b_j,
\qquad
a_j+b_j.
\]

Without an external semantic orientation, the sign of \(b_j\) is not identifiable, but \(\gamma_j=|b_j|\) is. Therefore the unordered pair of latent-conditioned probabilities is

\[
\boxed{
\left\{
P(X_j=+1\mid S=-1),
P(X_j=+1\mid S=+1)
\right\}
=
\left\{
\frac{1+a_j-\gamma_j}{2},
\frac{1+a_j+\gamma_j}{2}
\right\}.
}
\]

Let \(I_{a_j}=[a_{j,L},a_{j,U}]\) and \(I_{\gamma_j}=[\gamma_{j,L},\gamma_{j,U}]\). A conservative simultaneous confidence orbit is

\[
\boxed{
P_{j,\mathrm{small}}
\in
\left[
\frac{1+a_{j,L}-\gamma_{j,U}}2,
\frac{1+a_{j,U}-\gamma_{j,L}}2
\right]\cap[0,1],
}
\]

and

\[
\boxed{
P_{j,\mathrm{large}}
\in
\left[
\frac{1+a_{j,L}+\gamma_{j,L}}2,
\frac{1+a_{j,U}+\gamma_{j,U}}2
\right]\cap[0,1].
}
\]

This box propagation is deliberately conservative because the offset and stability intervals are statistically dependent. Coverage is nevertheless inherited from the original simultaneous eight-cell event. No new confidence allocation is introduced.

The result is a finite-sample confidence set for the full binary channel up to the same unavoidable common column swap already present in P73.

---

## 8. Conservative design condition for clearing the covariance gate

Suppose the population model satisfies

\[
c_{\min}
:=
\min\{|C_{12}|,|C_{13}|,|C_{23}|\}>0.
\]

On the confidence event,

\[
|\widehat C_{ij}|
\ge
|C_{ij}|-3\delta_n
\ge
c_{\min}-3\delta_n.
\]

For every empirical lower margin \(|\widehat C_{ij}|-3\delta_n\) to be strictly positive, it is sufficient that

\[
6\delta_n<c_{\min}.
\]

Using the uncapped expression

\[
\delta_n
=8\sqrt{\frac{\log(16/\alpha)}{2n}},
\]

one sufficient condition is

\[
\boxed{
 n>
\frac{1152\log(16/\alpha)}{c_{\min}^2}.
}
\]

This is a transparent conservative design rule, not an optimal sample-complexity theorem.

---

## 9. Convergence away from the degeneracy boundary

Fix a P73-compatible population law whose three absolute pair covariances are bounded below by a positive margin. Then

\[
\delta_n(\alpha)
=
O\!\left(\sqrt{\frac{\log(1/\alpha)}{n}}\right).
\]

Every P74 interval endpoint is a continuous function of the observed moments on any compact region whose covariance denominators remain bounded away from zero. Therefore, for fixed \(\alpha\), the intervals for \(|m|\), \(v\), prevalence orbit, \(\gamma_j\), \(b_jm\), \(a_j\), and the unordered channel probabilities contract to their P73 population values as \(n\to\infty\).

This statement is deliberately local to the nondegenerate region. P74 does not claim uniform stability through

\[
C_{12}C_{13}C_{23}=0.
\]

Near that singular set, a wide or failed certificate is the scientifically appropriate output.

---

## 10. Proposition statement

**Proposition 74.** Under the P73 nondegenerate binary three-view latent model and IID sampling of \(n\) observed triples, let

\[
\delta_n(\alpha)
=
\min\left\{
2,
8\sqrt{\frac{\log(16/\alpha)}{2n}}
\right\}.
\]

With probability at least \(1-\alpha\), simultaneously:

1. every first moment satisfies \(|\widehat\mu_j-\mu_j|\le\delta_n\);
2. every pair covariance satisfies \(|\widehat C_{ij}-C_{ij}|\le3\delta_n\);
3. the third centered moment satisfies \(|\widehat M_{123}-M_{123}|\le13\delta_n\);
4. if all three covariance lower margins \(L_{ij}\) are positive and their empirical sign product is positive, the interval formulas above contain the P73 latent imbalance, latent variance, prevalence orbit, and all three P72 single-view stability coefficients;
5. under the same gate, the signed-ratio construction contains each invariant product \(b_jm\), each channel offset \(a_j\), and the unordered pair of latent-conditioned binary response probabilities for every view;
6. the joint three-view stability is at least \(\max_j\gamma_{j,L}\);
7. if a covariance lower margin reaches zero, finite-data inversion is not certified rather than extrapolated through the P73 singularity.

The entire statement uses one simultaneous confidence event. The result quantifies finite-sample uncertainty in a declared statistical target model. It does not establish the model assumptions, consciousness, experiential ground truth, or a physical-to-experiential bridge.

---

## 11. What P74 establishes and what it does not

P74 establishes a finite-sample certification layer for the P73 model. In particular, it distinguishes three outcomes that should not be conflated:

- **certified recovery:** the covariance gate passes and simultaneous parameter/channel intervals are reported;
- **model incompatibility on the confidence event:** the covariance intervals exclude zero but the required sign pattern fails;
- **not certified by the current data:** at least one covariance confidence interval reaches zero, so P73 inversion is intentionally withheld.

The theorem does not test the conditional-independence assumption itself. It also does not show that a binary latent target is scientifically adequate, that the three views are valid measurements of experience, or that an inferred latent class has any particular phenomenal meaning.

A future empirical program must therefore pair P74 with diagnostics or alternative designs capable of challenging the P73 model assumptions rather than merely conditioning on them.

---

## 12. Executable audit path

Implementation:

[`src/consciousness_bridge/finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py)

Regression tests:

[`tests/test_finite_sample_target_channel_recovery.py`](../tests/test_finite_sample_target_channel_recovery.py)

Population theorem used by P74:

[Proposition 73](proposition_73_target_channel_identifiability.md)

Measurement-stability theorem used by P74:

[Proposition 72](proposition_72_target_measurement_channel_robustness.md)

Equation and provenance classification:

[P74 equation provenance](p74_equation_provenance.md)

---

## 13. Scientific boundary

P74 closes one finite-data gap and opens the next methodological one. It can certify uncertainty in target-channel recovery **if the P73 three-view model is the correct population model**. It does not test the conditional-independence assumption itself.

A scientifically mature target pipeline still needs model diagnostics capable of detecting dependence among observed views that remains after conditioning on the proposed latent target, or alternative identification schemes that do not rely on the same three-view assumption.

The physical-to-experiential bridge remains open.
