# Proposition 73: three-view target-channel identifiability and stability recovery

**Status:** proved population-identifiability theorem for a declared binary latent-target model with three conditionally independent binary target views, under explicit nondegeneracy assumptions.

## 1. Purpose

P71 separates target provenance from physical sufficiency. P72 then separates a latent target from the noisy process used to observe it.

P72 conditions on a declared target-measurement channel or a defensible lower bound on its stability. That creates the next scientific question:

> When can target-measurement reliability itself be recovered from observable data rather than inserted as an assumption?

P73 gives one exact answer for a deliberately narrow model. It does not solve target validity in general. It shows that, within a fixed physical stratum and under a three-view conditional-independence model, a binary latent target and three binary measurement channels are generically identifiable up to the unavoidable latent-label swap. The P72 stability coefficients are invariant under that swap and are therefore identifiable quantities.

The theorem also proves a two-view non-identifiability result. Agreement among only two noisy views does not, by itself, determine the reliability of either view.

The latent variable used below is a declared statistical target. It is not assumed to be consciousness, phenomenal truth, or a privileged experiential variable.

---

## 2. Fixed-stratum setup

Fix a declared physical descriptor value

\[
T=t.
\]

All probabilities in this proposition are conditional on that stratum. This is important because P72 permits the target channel to depend on \(t\).

Let the latent target be binary and encode it as

\[
S\in\{-1,+1\}.
\]

Define

\[
\pi=P(S=+1),
\qquad
m=\mathbb E[S]=2\pi-1,
\qquad
v=\operatorname{Var}(S)=1-m^2.
\]

Assume

\[
0<\pi<1,
\]

so \(v>0\).

Let three observed binary target views be

\[
X_1,X_2,X_3\in\{-1,+1\}.
\]

The views may represent repeated target instruments, raters, report channels, or other declared target-side observations. P73 does not assert that any such view is intrinsically valid.

### Conditional-independence assumption

Assume

\[
\boxed{
X_1\perp\!\!\!\perp X_2\perp\!\!\!\perp X_3\mid S,T=t
}
\]

in the product-kernel sense

\[
P(x_1,x_2,x_3\mid s,t)
=
\prod_{j=1}^3 P(x_j\mid s,t).
\]

For each view, every binary channel can be written in conditional-mean form

\[
\boxed{
\mathbb E[X_j\mid S]=a_j+b_jS.
}
\]

Here

\[
a_j=
\frac{
\mathbb E[X_j\mid S=+1]
+
\mathbb E[X_j\mid S=-1]
}{2},
\]

and

\[
b_j=
\frac{
\mathbb E[X_j\mid S=+1]
-
\mathbb E[X_j\mid S=-1]
}{2}.
\]

The nondegenerate P73 regime requires

\[
\boxed{b_1b_2b_3\ne0.}
\]

A zero \(b_j\) means that view carries no binary target separation and destroys the moment inversion used below.

---

## 3. Observable moments

Define the observable means

\[
\mu_j=\mathbb E[X_j],
\]

pair covariances

\[
C_{ij}
=
\mathbb E[(X_i-\mu_i)(X_j-\mu_j)],
\]

and third centered moment

\[
M_{123}
=
\mathbb E[
(X_1-\mu_1)(X_2-\mu_2)(X_3-\mu_3)
].
\]

These quantities are determined by the joint observed law of \((X_1,X_2,X_3)\).

---

## 4. P73A: three-view moment factorization

### Proposition

Under the setup above,

\[
\boxed{
\mu_j=a_j+b_jm,
}
\]

\[
\boxed{
C_{ij}=b_ib_jv,
}
\]

and

\[
\boxed{
M_{123}=-2mv\,b_1b_2b_3.
}
\]

### Proof

The mean identity follows from iterated expectation:

\[
\mathbb E[X_j]
=
\mathbb E[\mathbb E[X_j\mid S]]
=a_j+b_jm.
\]

Write

\[
X_j=a_j+b_jS+\varepsilon_j,
\qquad
\mathbb E[\varepsilon_j\mid S]=0.
\]

Conditional independence makes the cross-view conditional products of the centered noise terms vanish. Therefore

\[
C_{ij}
=b_ib_j\mathbb E[(S-m)^2]
=b_ib_jv.
\]

Likewise,

\[
M_{123}
=b_1b_2b_3\mathbb E[(S-m)^3].
\]

For \(S\in\{-1,+1\}\), using \(S^2=1\) and \(S^3=S\),

\[
\mathbb E[(S-m)^3]
=-2m(1-m^2)
=-2mv.
\]

Hence

\[
M_{123}=-2mv\,b_1b_2b_3.
\]

\(\square\)

---

## 5. P73B: explicit population recovery up to latent-label swap

Because every \(b_j\ne0\) and \(v>0\), all three pair covariances are nonzero and

\[
C_{12}C_{13}C_{23}
=b_1^2b_2^2b_3^2v^3>0.
\]

Define the observable ratio

\[
\boxed{
q=
\frac{M_{123}^2}{C_{12}C_{13}C_{23}}.
}
\]

P73A gives

\[
q
=
\frac{4m^2}{1-m^2}.
\]

Therefore

\[
\boxed{
m^2=\frac{q}{q+4},
\qquad
v=\frac{4}{q+4}.
}
\]

So the magnitude of the latent imbalance is observable.

Choose one algebraic orientation, for example

\[
b_1>0.
\]

Then

\[
\boxed{
b_1=
\sqrt{
\frac{C_{12}C_{13}}{C_{23}v}
}.}
\]

The other two loadings follow from

\[
\boxed{
b_2=\frac{C_{12}}{b_1v},
\qquad
b_3=\frac{C_{13}}{b_1v}.}
\]

Finally, the signed latent mean is recovered from

\[
\boxed{
m=
-\frac{M_{123}}{2v b_1b_2b_3}.}
\]

Then

\[
\boxed{a_j=\mu_j-b_jm.}
\]

The two conditional output means are

\[
\mathbb E[X_j\mid S=-1]=a_j-b_j,
\]

\[
\mathbb E[X_j\mid S=+1]=a_j+b_j,
\]

so the channel probabilities are

\[
\boxed{
P(X_j=+1\mid S=-1)=\frac{1+a_j-b_j}{2},
}
\]

and

\[
\boxed{
P(X_j=+1\mid S=+1)=\frac{1+a_j+b_j}{2}.
}
\]

Thus the latent prevalence and all three binary measurement channels are recovered from the observable three-view law once an orientation is selected.

### Why the remaining ambiguity is unavoidable

Replace

\[
S\mapsto -S,
\qquad
m\mapsto -m,
\qquad
b_j\mapsto -b_j.
\]

Equivalently, swap the two latent labels and swap the two columns of every view channel. The observable joint distribution is unchanged.

Therefore the model is identifiable only up to this common latent-label permutation unless an external scientific anchor gives one latent state a semantic orientation.

This is not a numerical defect. It is an exact symmetry of the latent model.

---

## 6. P73C: identification of the P72 stability coefficient

For a binary latent input, the P72 channel-stability coefficient of view \(j\) equals the total-variation distance between its two latent columns:

\[
\gamma_j
=
\operatorname{TV}
\bigl(
K_j(\cdot\mid +1),
K_j(\cdot\mid -1)
\bigr).
\]

For a binary observed output this reduces exactly to

\[
\boxed{\gamma_j=|b_j|.}
\]

Because a global latent-label swap sends \(b_j\mapsto-b_j\), \(|b_j|\) is invariant. Hence all three single-view P72 stability coefficients are identifiable from the observed three-view law even when the semantic latent orientation is not.

### Joint three-view channel

Conditional independence gives the joint target channel

\[
K_{123}(x_1,x_2,x_3\mid s)
=
\prod_{j=1}^3 K_j(x_j\mid s).
\]

Its binary-input P72 stability is

\[
\boxed{
\gamma_{123}
=
\operatorname{TV}
\bigl(
K_{123}(\cdot\mid +1),
K_{123}(\cdot\mid -1)
\bigr).
}
\]

The recovered channel parameters determine \(\gamma_{123}\) exactly, and the common column swap leaves it unchanged.

Moreover, marginalizing the joint observation to any one view is a stochastic map. Total variation cannot increase under that marginalization. Therefore

\[
\boxed{
\gamma_{123}\ge\max\{\gamma_1,\gamma_2,\gamma_3\}.
}
\]

Multiple conditionally independent target views can therefore create a more stable joint observation channel than any single view, while remaining within the same declared latent model.

---

## 7. P73D: two-view non-identifiability theorem

Three views are not a cosmetic choice.

Take a balanced latent state

\[
P(S=+1)=P(S=-1)=\frac12,
\]

and two conditionally independent binary views with

\[
\mathbb E[X_j\mid S]=b_jS.
\]

Then the observed means vanish and

\[
\mathbb E[X_1X_2]=b_1b_2.
\]

The complete two-view law is

\[
\boxed{
P(X_1=x_1,X_2=x_2)
=
\frac14\left(1+b_1b_2x_1x_2\right).
}
\]

It depends on \(b_1\) and \(b_2\) only through their product.

For example,

\[
(b_1,b_2)=(0.60,0.60)
\]

and

\[
(b_1,b_2)=(0.45,0.80)
\]

both give

\[
b_1b_2=0.36
\]

and therefore exactly the same observed two-view distribution.

But their single-view P72 stability coefficients differ:

\[
(\gamma_1,\gamma_2)=(0.60,0.60)
\]

versus

\[
(\gamma_1,\gamma_2)=(0.45,0.80).
\]

Hence the two-view observed law does not identify individual target-channel reliabilities without additional assumptions, calibration information, known error rates, or other anchors.

\(\square\)

---

## 8. P73E: scientific orientation versus algebraic orientation

The recovery convention \(b_1>0\) chooses a coordinate orientation for the latent class. It does not prove what \(S=+1\) means scientifically.

A semantic interpretation requires an independent anchor, such as a predeclared calibration condition whose target state is externally justified under the scientific protocol. Without such an anchor, the two latent labels remain exchangeable.

This distinction matters for consciousness research. Statistical recovery of a latent class does not establish that the class is an experiential state. P73 identifies parameters of a declared latent measurement model. Target meaning remains a separate scientific obligation under P71.

---

## 9. Relation to established latent-class identifiability results

P73 uses standard latent-variable ideas in a bridge-specific role.

Dawid and Skene developed a latent-response model in which observer error rates can be estimated even when the true response is not directly available, using maximum likelihood and the EM algorithm. This is methodological precedent for estimating target-side observer reliability rather than assuming perfect labels.

- A. P. Dawid and A. M. Skene, "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm," *Applied Statistics* 28(1), 20-28 (1979). DOI: [10.2307/2346806](https://doi.org/10.2307/2346806).

Allman, Matias, and Rhodes established broad identifiability results for latent-structure models with observed variables that are independent conditional on hidden classes, including the central role of identifiability up to label swapping.

- E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of Parameters in Latent Structure Models with Many Observed Variables," *The Annals of Statistics* 37(6A), 3099-3132 (2009). DOI: [10.1214/09-AOS689](https://doi.org/10.1214/09-AOS689).

The general latent-class identifiability problem is therefore not claimed as new here. The repository-original contribution of P73 is the explicit three-binary-view moment derivation in the notation of the P71-P72 target-validity branch, the direct recovery of P72 stability quantities, the joint-view stability consequence, and the constructive two-view boundary packaged as an auditable bridge-methodology theorem.

---

## 10. What P73 proves

Under one fixed \(T=t\) stratum, P73 proves that:

1. three conditionally independent binary views obey explicit observable moment factorizations;
2. interior latent prevalence and three nonzero view loadings permit explicit recovery of the latent-class parameters up to global label swapping;
3. every single-view P72 stability coefficient \(\gamma_j\) is identifiable despite the label ambiguity;
4. the joint three-view stability coefficient is identifiable and is at least as large as every single-view coefficient;
5. two views alone do not identify the individual stability coefficients without additional assumptions.

---

## 11. What P73 does not prove

P73 does not prove that:

- the conditional-independence model is empirically correct;
- three human raters are actually conditionally independent;
- repeated reports are independent after conditioning on a latent experiential state;
- the recovered latent class is consciousness or experiential ground truth;
- the semantic orientation of the latent labels is identifiable without an external anchor;
- finite samples recover the population parameters without uncertainty;
- an unknown number of latent classes is identifiable under the same formulas;
- measurement channels are invariant across physical strata, people, time, interventions, or contexts.

The theorem is deliberately local to a declared binary three-view model.

---

## 12. Reproducibility

Executable implementation:

- [`src/consciousness_bridge/target_channel_identifiability.py`](../src/consciousness_bridge/target_channel_identifiability.py)

Regression tests:

- [`tests/test_target_channel_identifiability.py`](../tests/test_target_channel_identifiability.py)

The implementation reconstructs the three-view model from the observed joint distribution, verifies compatibility by rebuilding the full observed law, computes single-view and joint P72 stability coefficients, and exposes the two-view non-identifiability construction.

Finite-sample uncertainty for the recovered channel parameters is intentionally left for a later proposition. P73 is a population identifiability theorem. That separation prevents population invertibility from being confused with finite-data reliability.
