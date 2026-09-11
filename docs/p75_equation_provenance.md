# P75 Equation and Provenance Record

## Scope

This record classifies the equations used in Proposition 75: Target-Model Adequacy and Four-View Overidentification.

The purpose is to separate:

- standard latent-class and algebraic-statistics background;
- direct algebraic consequences of the declared binary model;
- repository-specific synthesis inside the physical-to-experiential bridge test architecture.

No entry in this file should be read as a claim that the latent target is consciousness.

---

## Declared model

Let \(S\in\{-1,+1\}\) be a latent binary target and let \(X_1,\ldots,X_k\in\{-1,+1\}\) be observed binary target views. P75 assumes

\[
P(x_1,\ldots,x_k\mid S=s)
=\prod_{j=1}^kP(x_j\mid S=s).
\]

**Classification:** declared modeling assumption.

**Novelty status:** not new. This is the standard latent-class or mixture-of-product-distributions structure used throughout latent-variable statistics.

Relevant background: Allman, Matias, and Rhodes (2009); Drton, Sturmfels, and Sullivant (2009).

---

## P75-E1. Observable dimension

For \(k\) binary observed variables,

\[
d_{\mathrm{obs}}(k)=2^k-1.
\]

**Classification:** standard simplex dimension count.

**Novelty status:** not new.

---

## P75-E2. Model parameter dimension

For one binary latent state and \(k\) binary observed channels,

\[
d_{\mathrm{model}}(k)=1+2k.
\]

The one latent prevalence contributes one degree of freedom and each binary observed channel contributes two latent-conditioned response probabilities.

**Classification:** direct parameter count for the declared model.

**Novelty status:** standard.

The connection of hidden-variable models to secant varieties is classical algebraic-statistics background. Garcia, Stillman, and Sturmfels (2005) and Drton, Sturmfels, and Sullivant (2009) are appropriate references.

---

## P75-E3. Just-identification and overidentification counts

For three views,

\[
2^3-1=7=1+2(3).
\]

For four views,

\[
2^4-1=15,
\qquad
1+2(4)=9,
\qquad
15-9=6.
\]

**Classification:** arithmetic consequence of P75-E1 and P75-E2.

**Novelty status:** the dimension arithmetic itself is not new. The repository-specific role is methodological: it explains why P73 three-view identifiability should not be misread as generic model validation and why a fourth view creates an overidentifying adequacy layer after P74.

**Important qualification:** equal model and observable dimensions do not mean every three-view probability law belongs to the real stochastic model. Positivity and semialgebraic membership restrictions remain.

---

## P75-E4. Affine conditional mean

For a binary observed view and binary latent state,

\[
\mathbb E[X_j\mid S]=a_j+b_jS.
\]

**Classification:** elementary binary-state parametrization.

**Novelty status:** not new.

---

## P75-E5. Pair covariance factorization

Let

\[
m=\mathbb E[S],
\qquad
v=1-m^2.
\]

For distinct views under conditional independence,

\[
C_{ij}=b_ib_jv.
\]

**Classification:** direct moment derivation from the declared conditional-independence model.

**Novelty status:** standard latent-variable covariance factorization.

---

## P75-E6. Four-view covariance tetrads

From P75-E5,

\[
C_{12}C_{34}
=C_{13}C_{24}
=C_{14}C_{23}.
\]

**Classification:** observable polynomial equality implied by the model.

**Novelty status:** tetrad-style algebraic constraints are not new. Algebraic model invariants and hidden-variable constraints are established parts of algebraic statistics. See Garcia, Stillman, and Sturmfels (2005) and Drton, Sturmfels, and Sullivant (2009).

**Repository-specific role:** P75 uses these constraints as explicit target-channel adequacy obligations downstream of P71-P74.

---

## P75-E7. Binary latent third central moment

For \(S\in\{-1,+1\}\) with mean \(m\) and variance \(v=1-m^2\),

\[
\mathbb E[(S-m)^3]=-2mv.
\]

**Classification:** elementary binary-distribution identity.

**Novelty status:** not new.

---

## P75-E8. Triple centered moment

For distinct \(i,j,k\),

\[
M_{ijk}
=-2m\,b_ib_jb_kv.
\]

**Classification:** direct consequence of P75-E4, conditional independence, and P75-E7.

**Novelty status:** not claimed as a new general identity.

---

## P75-E9. Cross-triple latent-imbalance ratio

Combining P75-E5 and P75-E8 gives

\[
q_{ijk}
=\frac{M_{ijk}^2}{C_{ij}C_{ik}C_{jk}}
=\frac{4m^2}{v}.
\]

Thus for four views,

\[
q_{123}=q_{124}=q_{134}=q_{234}.
\]

**Classification:** direct algebraic derivation under the declared model.

**Novelty status:** the ratio used for three-view recovery is already part of P73's repository derivation and is closely connected to classical moment-based latent-class identification. P75's new role is cross-subset adequacy: every available triple must agree on the same latent quantity.

---

## P75-E10. Binary latent fourth central moment

\[
\mathbb E[(S-m)^4]
=v(1+3m^2).
\]

**Classification:** elementary binary-distribution identity.

**Novelty status:** not new.

---

## P75-E11. Four-view fourth centered moment

Conditional independence gives

\[
M_{1234}
=b_1b_2b_3b_4v(1+3m^2).
\]

Using a covariance pairing and

\[
q=\frac{4m^2}{v},
\]

we obtain

\[
M_{1234}
=(1+q)C_{12}C_{34}
=(1+q)C_{13}C_{24}
=(1+q)C_{14}C_{23}.
\]

**Classification:** direct repository derivation from standard moment identities.

**Novelty status:** do not claim the underlying algebraic relation as a general first discovery without a dedicated literature search establishing that point. P75 uses it as one transparent higher-order adequacy diagnostic and verifies compatibility more strongly by reconstructing the full observable law.

---

## P75-E12. Full-law reconstruction membership audit

P75 recovers an anchor three-view model using P73, infers the fourth loading through

\[
b_4=\frac{C_{14}}{b_1v},
\]

and its intercept through

\[
a_4=\mu_4-b_4m.
\]

The fourth latent-conditioned probabilities are

\[
P(X_4=+1\mid S=-1)=\frac{1+a_4-b_4}{2},
\]

\[
P(X_4=+1\mid S=+1)=\frac{1+a_4+b_4}{2}.
\]

The complete four-view law is then reconstructed by

\[
P(x_1,x_2,x_3,x_4)
=\sum_s P(S=s)\prod_{j=1}^4P(X_j=x_j\mid S=s).
\]

**Classification:** executable model-membership audit assembled from P73 recovery plus the declared four-view conditional-independence factorization.

**Novelty status:** reconstruction-based goodness-of-fit for latent-class models is standard in spirit. The repository-specific contribution is its explicit placement as the adequacy gate following P71 non-circularity, P72 noisy-target robustness, P73 identifiability, and P74 finite-sample recovery.

---

## Literature anchors

### Allman, Matias, and Rhodes

E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of parameters in latent structure models with many observed variables," *The Annals of Statistics* 37(6A), 3099-3132, 2009. DOI: 10.1214/09-AOS689.

Use for:

- generic identifiability context;
- latent-class and mixture-of-product-distributions background;
- the distinction between global and generic identifiability.

### Garcia, Stillman, and Sturmfels

L. D. Garcia, M. Stillman, and B. Sturmfels, "Algebraic geometry of Bayesian networks," *Journal of Symbolic Computation* 39(3-4), 331-355, 2005. DOI: 10.1016/j.jsc.2004.11.007.

Use for:

- hidden-variable models and secant varieties;
- algebraic constraints implied by Bayesian networks with hidden variables.

### Drton, Sturmfels, and Sullivant

M. Drton, B. Sturmfels, and S. Sullivant, *Lectures on Algebraic Statistics*, Birkhauser, 2009. DOI: 10.1007/978-3-7643-8905-5.

Use for:

- algebraic-statistics background;
- hidden variables and secant varieties;
- model invariants as tools for statistical model analysis.

---

## Repository-specific contribution boundary

P75 should be described as a **methodological synthesis and explicit theorem package inside this research program**, not as the invention of latent-class identifiability, secant-variety dimension counting, tetrads, or algebraic model invariants.

Its specific contribution is to enforce the distinction

\[
\text{identifiable target channel}
\not\Rightarrow
\text{validated target model},
\]

and to make that distinction operational in the bridge-test architecture by introducing a four-view overidentification layer with explicit moment residuals and full-law reconstruction.

The physical-to-experiential bridge remains open.
