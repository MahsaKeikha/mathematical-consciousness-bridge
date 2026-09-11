# Proposition 74: finite-sample target-channel recovery certification

## Purpose

P73 is a population identifiability theorem. It shows that, under a nondegenerate binary three-view latent model, the observable joint law determines the latent prevalence and all three target-view channels up to a common latent-label swap. It also identifies the P72 single-view stability coefficients

\[
\gamma_j=|b_j|.
\]

P74 asks the next experimental question:

> If the three-view joint law is observed only through finitely many samples, when can the P73 inversion be certified without confusing sampling noise with target-channel structure?

The result below gives a conservative simultaneous confidence construction. It deliberately refuses inversion when the finite-data covariance margins do not separate the observed law from the P73 degeneracy boundary.

This is a statistical theorem under a declared latent-variable model. It does not validate that model empirically, assign semantic meaning to the latent labels, or identify the latent state with consciousness.

---

## 1. Model and sampling assumptions

Fix one physical stratum \(T=t\). Assume the P73 population model:

1. \(S\in\{-1,+1\}\) is a declared binary latent target;
2. \(X_1,X_2,X_3\in\{-1,+1\}\) are binary target views;
3. the three views are conditionally independent given \(S\);
4. the latent prevalence is interior;
5. every P73 loading is nonzero;
6. \(n\) observed triples are IID draws from the same three-view population law \(P\).

Let \(\widehat P\) be the empirical distribution on the eight cells of \(\{-1,+1\}^3\).

The P73 population moments are

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

Write hats for their empirical analogues.

---

## 2. One simultaneous eight-cell confidence event

For each of the eight cells \(x\), the empirical cell frequency is an average of Bernoulli indicators. Hoeffding's inequality gives

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

The cap at 2 uses the maximum possible \(L^1\) distance between probability distributions.

Everything below is deterministic on this single simultaneous event. No additional confidence spending is introduced.

---

## 3. Moment perturbation bounds

For any function \(f:\{-1,+1\}^3\to[-1,1]\),

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

Hence every first moment, pair-product moment, and triple-product moment differs from its population value by at most \(\delta_n\).

### 3.1 Pair covariance

Write

\[
C_{ij}
=
\mathbb E[X_iX_j]-\mu_i\mu_j.
\]

Since \(|\mu_i|,|\widehat\mu_i|\le1\),

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

### 3.2 Third centered moment

Let

\[
r_{ij}=\mathbb E[X_iX_j],
\qquad
r_{123}=\mathbb E[X_1X_2X_3].
\]

The third centered moment expands as

\[
M_{123}
=
r_{123}
-\mu_1r_{23}
-\mu_2r_{13}
-\mu_3r_{12}
+2\mu_1\mu_2\mu_3.
\]

The raw triple term contributes at most \(\delta_n\). Each mean-times-pair term contributes at most \(2\delta_n\), because both factors have magnitude at most one. The three such terms therefore contribute at most \(6\delta_n\). The difference between the two products of three means is at most \(3\delta_n\), and the leading factor 2 contributes at most \(6\delta_n\).

Thus

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

These constants are conservative. P74 does not claim them to be minimax-optimal.

---

## 4. Confidence intervals for absolute moments

For the three pair covariances define

\[
L_{ij}
=
\max\{|\widehat C_{ij}|-r_C,0\},
\]

\[
U_{ij}
=
\min\{|\widehat C_{ij}|+r_C,1\}.
\]

The cap \(U_{ij}\le1\) is valid for covariances of \(\{-1,+1\}\)-valued variables.

For the third centered moment define

\[
L_M
=
\max\{|\widehat M_{123}|-r_M,0\},
\qquad
U_M
=
|\widehat M_{123}|+r_M.
\]

On the simultaneous confidence event,

\[
|C_{ij}|\in[L_{ij},U_{ij}],
\qquad
|M_{123}|\in[L_M,U_M].
\]

---

## 5. The P74 nondegeneracy gate

P73 divides by products of pair covariances. A finite-data procedure should therefore not perform that inversion merely because the empirical covariances happen to be nonzero.

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

When this condition fails, the correct P74 output is

> **P73 nondegeneracy is not certified by these finite data.**

That output does not prove that a population covariance is zero and does not prove that the latent model is nonidentifiable in truth. It says only that the present finite sample does not safely separate the joint law from the inversion singularity.

If all three lower margins are positive, their signs are also fixed on the simultaneous event. The nondegenerate P73 model requires

\[
C_{12}C_{13}C_{23}>0.
\]

Therefore an empirical sign product that is nonpositive after all three intervals exclude zero is incompatible with the nondegenerate P73 model on that confidence event.

---

## 6. Finite-sample inversion of the P73 latent imbalance

Under P73,

\[
q
=
\frac{M_{123}^2}{C_{12}C_{13}C_{23}}
=
\frac{|M_{123}|^2}
{|C_{12}||C_{13}||C_{23}|}.
\]

When the P74 nondegeneracy gate passes, define

\[
\boxed{
q_L
=
\frac{L_M^2}
{U_{12}U_{13}U_{23}},
}
\]

\[
\boxed{
q_U
=
\frac{U_M^2}
{L_{12}L_{13}L_{23}}.
}
\]

Then on the simultaneous event

\[
q\in[q_L,q_U].
\]

P73 gives

\[
|m|
=
\sqrt{\frac{q}{q+4}},
\qquad
v=1-m^2=\frac4{q+4}.
\]

The first map is increasing in \(q\) and the second is decreasing. Therefore

\[
\boxed{
|m|
\in
\left[
\sqrt{\frac{q_L}{q_L+4}},
\sqrt{\frac{q_U}{q_U+4}}
\right].
}
\]

and

\[
\boxed{
v
\in
\left[
\frac4{q_U+4},
\frac4{q_L+4}
\right]
=:[v_L,v_U].
}
\]

Because the global latent-label swap remains observationally invisible, the prevalence \(\pi=P(S=+1)\) is reported as a two-interval orbit rather than as a falsely oriented single estimate. If

\[
|m|\in[m_L,m_U],
\]

then

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

## 7. Simultaneous confidence intervals for P72 stability

P73 gives the label-invariant single-view stability coefficients

\[
\gamma_1
=
\sqrt{
\frac{|C_{12}C_{13}|}
{v|C_{23}|}
},
\]

\[
\gamma_2
=
\sqrt{
\frac{|C_{12}C_{23}|}
{v|C_{13}|}
},
\]

\[
\gamma_3
=
\sqrt{
\frac{|C_{13}C_{23}|}
{v|C_{12}|}
}.
\]

Every factor is positive after the nondegeneracy gate. Monotonic interval propagation therefore gives

\[
\boxed{
\gamma_{1,L}
=
\sqrt{
\frac{L_{12}L_{13}}
{v_UU_{23}}
},
\qquad
\gamma_{1,U}
=
\sqrt{
\frac{U_{12}U_{13}}
{v_LL_{23}}
}.
}
\]

The corresponding bounds for \(\gamma_2\) and \(\gamma_3\) are obtained by cyclic permutation. Since every binary-channel stability lies in \([0,1]\), upper endpoints may be clipped at 1 without weakening coverage.

Thus, on the original eight-cell confidence event,

\[
\boxed{
\gamma_j
\in
[\gamma_{j,L},\gamma_{j,U}]
\quad
\text{simultaneously for }j=1,2,3.
}
\]

P73 also proves

\[
\gamma_{123}
\ge
\max_j\gamma_j
\]

for the joint three-view channel. Hence P74 immediately obtains the certified lower bound

\[
\boxed{
\gamma_{123}
\ge
\max_j\gamma_{j,L}.
}
\]

---

## 8. Conservative design condition for clearing the covariance gate

Suppose before sampling that the population model is known to satisfy

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

To make the empirical lower margin

\[
|\widehat C_{ij}|-3\delta_n
\]

strictly positive for every pair, it is sufficient that

\[
6\delta_n<c_{\min}.
\]

Using the uncapped expression

\[
\delta_n
=
8\sqrt{\frac{\log(16/\alpha)}{2n}},
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
O\!\left(
\sqrt{\frac{\log(1/\alpha)}{n}}
\right).
\]

The interval endpoints above are continuous functions of the moments on any region whose covariance denominators remain bounded away from zero. Therefore, for fixed \(\alpha\), the P74 confidence intervals contract to the P73 population quantities as \(n\to\infty\).

This statement is deliberately local to the nondegenerate region. P74 does not claim uniform stability through the singular set

\[
C_{12}C_{13}C_{23}=0.
\]

Near that set, a wide or failed certificate is the scientifically appropriate output.

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

1. every pair covariance satisfies \(|\widehat C_{ij}-C_{ij}|\le3\delta_n\);
2. the third centered moment satisfies \(|\widehat M_{123}-M_{123}|\le13\delta_n\);
3. if all three covariance lower margins \(L_{ij}\) are positive and their empirical sign product is positive, the interval formulas in Sections 6 and 7 contain the P73 latent imbalance, latent variance, prevalence orbit, and all three P72 single-view stability coefficients;
4. the joint three-view stability is at least \(\max_j\gamma_{j,L}\);
5. if a covariance lower margin reaches zero, finite-data inversion is not certified rather than extrapolated through the P73 singularity.

The result quantifies finite-sample uncertainty in a declared statistical target model. It does not establish the model assumptions, consciousness, experiential ground truth, or a physical-to-experiential bridge.

---

## 11. Executable audit path

Implementation:

[`src/consciousness_bridge/finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py)

Regression tests:

[`tests/test_finite_sample_target_channel_recovery.py`](../tests/test_finite_sample_target_channel_recovery.py)

Population theorem used by P74:

[Proposition 73](proposition_73_target_channel_identifiability.md)

Measurement-stability theorem used by P74:

[Proposition 72](proposition_72_target_measurement_channel_robustness.md)

---

## 12. Scientific boundary

P74 closes one finite-data gap and opens the next methodological one. It can certify uncertainty in target-channel recovery **if the P73 three-view model is the correct population model**. It does not test the conditional-independence assumption itself.

A scientifically mature target pipeline therefore still needs model diagnostics capable of detecting dependence among the observed views that remains after conditioning on the proposed latent target, or alternative identification schemes that do not rely on the same three-view assumption.

The physical-to-experiential bridge remains open.
