# Proposition 9: finite categorical sample complexity for exact signature recovery

## Physical question

Proposition 8 says exact signature recovery is guaranteed whenever the uniform total-variation estimation error satisfies

\[
\varepsilon<\frac{\gamma_S}{4},
\qquad
\gamma_S=\delta_S-\omega_S.
\]

The remaining question is operational:

> How many repeated experimental trials are sufficient to make that uniform error event hold with a declared confidence?

Proposition 9 gives one explicit finite-sample answer for categorical outcome measurements.

The bound is intentionally elementary and conservative. It uses coordinate-wise Hoeffding concentration and a union bound so every step is transparent.

---

# 1. Setup

Let

\[
\mathcal Q_0
\]

contain

\[
N_P=|\mathcal Q_0|
\]

physical realizations, and let the selected protocol family \(S\) contain

\[
N_\pi=|S|
\]

protocols.

There are therefore

\[
\boxed{
M=N_PN_\pi
}
\]

physical-system/protocol cells.

For every cell, assume the observable outcome alphabet has at most

\[
K
\]

categories.

For each cell, collect

\[
n
\]

independent identically distributed repetitions from the cell's true categorical law

\[
P^{\pi,p}
\]

and form the empirical distribution

\[
\widehat P^{\pi,p}.
\]

Cross-cell independence is not needed for the union bound below; the required concentration assumption is the declared within-cell IID sampling model.

---

# 2. One categorical distribution

For one categorical law

\[
P=(p_1,\ldots,p_K)
\]

and its empirical frequency vector

\[
\widehat P=(\widehat p_1,\ldots,\widehat p_K),
\]

Hoeffding's inequality gives, for one category and any \(a>0\),

\[
\Pr\left(
|\widehat p_j-p_j|>a
\right)
\le
2e^{-2na^2}.
\]

Applying the union bound over at most \(K\) categories,

\[
\Pr\left(
\max_j|\widehat p_j-p_j|>a
\right)
\le
2K e^{-2na^2}.
\]

If every coordinate error is at most \(a\), then

\[
\begin{aligned}
\|\widehat P-P\|_{\mathrm{TV}}
&=
\frac12
\sum_{j=1}^{K}
|\widehat p_j-p_j|\\
&\le
\frac{Ka}{2}.
\end{aligned}
\]

Set

\[
a=\frac{2\varepsilon}{K}.
\]

Then

\[
\boxed{
\Pr\left(
\|\widehat P-P\|_{\mathrm{TV}}>\varepsilon
\right)
\le
2K
\exp\left(
-\frac{8n\varepsilon^2}{K^2}
\right).
}
\]

---

# 3. Uniform theorem over all experimental cells

Apply the union bound over all

\[
M=N_PN_\pi
\]

cells.

## Proposition 9A

For every \(\varepsilon>0\),

\[
\boxed{
\Pr\left[
\sup_{p\in\mathcal Q_0}
\sup_{\pi\in S}
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
>
\varepsilon
\right]
\le
2MK
\exp\left(
-\frac{8n\varepsilon^2}{K^2}
\right).
}
\]

Therefore a sufficient condition for the uniform event

\[
\sup_{p,\pi}
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
\le\varepsilon
\]

with probability at least \(1-\alpha\) is

\[
\boxed{
n
\ge
\frac{K^2}{8\varepsilon^2}
\log\left(
\frac{2MK}{\alpha}
\right).
}
\]

---

# 4. Direct sample size for signature recovery

Let the population signature gap from Proposition 8 be

\[
\gamma_S
=
\delta_S-\omega_S
>0.
\]

Choose the conservative error target

\[
\boxed{
\varepsilon
=
\frac{\gamma_S}{8}.
}
\]

Then

\[
4\varepsilon
=
\frac{\gamma_S}{2}
<
\gamma_S,
\]

so Proposition 8's strict robustness condition is satisfied with slack.

Substitution gives the following result.

## Proposition 9B

If

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right),
}
\]

then, under the stated categorical IID sampling model, the uniform error event required by Proposition 8 holds with probability at least \(1-\alpha\).

Consequently, using the midpoint threshold

\[
\boxed{
\tau_*
=
\frac{\omega_S+\delta_S}{2},
}
\]

recovers every signature-equivalence decision correctly with probability at least

\[
\boxed{1-\alpha.}
\]

Therefore the complete signature partition on the finite physical domain is recovered exactly with the same confidence lower bound.

---

# 5. Proof of Proposition 9B

With

\[
\varepsilon=\frac{\gamma_S}{8},
\]

Proposition 9A requires

\[
\begin{aligned}
n
&\ge
\frac{K^2}
{8(\gamma_S^2/64)}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right)\\
&=
\frac{8K^2}{\gamma_S^2}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right).
\end{aligned}
\]

On the resulting uniform event, Proposition 8 gives

\[
\widehat d_S(p,p')
\le
\omega_S+\frac{\gamma_S}{4}
\]

for same-signature pairs and

\[
\widehat d_S(p,p')
\ge
\delta_S-\frac{\gamma_S}{4}
\]

for different-signature pairs.

Because

\[
\gamma_S
=
\delta_S-\omega_S,
\]

we have

\[
\omega_S+\frac{\gamma_S}{4}
<
\frac{\omega_S+\delta_S}{2}
<
\delta_S-\frac{\gamma_S}{4}.
\]

Therefore the midpoint threshold

\[
\tau_*
=
\frac{\omega_S+\delta_S}{2}
\]

classifies every pair correctly.

\[
\boxed{\text{QED}}
\]

---

# 6. Physical interpretation

The sample complexity scales as

\[
\boxed{
n
=
O\left(
\frac{K^2}{\gamma_S^2}
\log\frac{N_PN_\pi K}{\alpha}
\right).
}
\]

The dominant scientific quantity is the signature gap

\[
\gamma_S.
\]

A protocol family that doubles the robust gap can reduce this conservative trial requirement by approximately a factor of four.

This gives experiment design a direct statistical objective: choose protocols that enlarge between-signature separation while suppressing irrelevant within-signature variation.

---

# 7. What the bound means and what it does not mean

The theorem supplies a sufficient trial count under a declared finite categorical model.

It is deliberately conservative because it uses:

- coordinate-wise Hoeffding concentration;
- a union bound over outcomes;
- a union bound over all physical/protocol cells;
- a fixed safety choice \(\varepsilon=\gamma_S/8\).

Tighter multinomial concentration inequalities, adaptive designs, sequential testing, hierarchical models, and cross-protocol information sharing may reduce the required sample size.

The theorem does not claim the displayed bound is minimax optimal.

Its purpose is to establish a transparent first end-to-end finite-sample bridge from experimental repetitions to exact recovery of a proposed complete signature partition.

---

# 8. Scientific dependency chain

The current chain is now

\[
\boxed{
\begin{array}{rcl}
\text{P5} &:& \text{Is a physical feature bridge-sufficient?}\\
\text{P6} &:& \text{Is it bridge-complete?}\\
\text{P7} &:& \text{Can the experiment class recover it?}\\
\text{P8} &:& \text{How much distribution error can recovery tolerate?}\\
\text{P9} &:& \text{How many categorical trials suffice for that error?}
\end{array}
}
\]

This is the first complete theorem chain in the repository from a candidate physical signature to an explicit finite-data recovery guarantee.

---

# 9. Statistical lineage

The coordinate concentration step uses Hoeffding 1963. The union bounds and total-variation identity are standard probability tools.

Sharper empirical-distribution deviation inequalities exist and are candidates for later tightening. The present theorem intentionally uses an elementary proof so that the assumptions and constants remain auditable.

---

# 10. Status and next frontier

| Item | Status |
| --- | --- |
| one-cell categorical TV bound | proved from Hoeffding + union bound |
| uniform cellwise TV bound | proved |
| explicit confidence-dependent sample size | proved |
| exact partition-recovery corollary | proved via Proposition 8 |
| optimal sample complexity | open |
| adaptive/multimodal experimental design | open |
| empirically justified complete physical signature | central open bridge problem |

The next frontier is to construct and compare concrete candidate physical signatures, including composites of causal integration, recurrent persistence, global accessibility, higher-order structure, and predictive organization, and to search systematically for feature-matched counterexamples under Proposition 5.
