# Proposition 42: Quantum regular-bridge sample complexity under fixed IC measurement

## Status

**Proved finite-sample design theorem under a declared informationally complete measurement and categorical IID target model.** P42 substitutes explicit concentration radii into the P41 trace-ball obstruction and solves for sufficient quantum and target sample sizes.

The result is deliberately conservative. It uses coordinate Hoeffding inequalities and union bounds because their assumptions and constants are transparent. It does not claim statistical optimality, validate an arbitrary tomography estimator, establish quantum incompleteness, or identify the target with consciousness.

---

## 1. Experimental setup

Let

\[
\mathcal X=\{x_1,\ldots,x_K\}
\]

be a finite preparation set.

For every preparation \(x\), measure a fixed informationally complete POVM with \(m\) outcomes. Let

\[
p_x\in\Delta_m
\]

be the true measurement-outcome law and let

\[
\widehat p_x
\]

be the empirical frequency vector from \(n_Q\) IID repetitions for that preparation.

Assume a fixed linear reconstruction map

\[
R:\mathbb R^m\to\mathrm{Herm}(\mathcal H)
\]

satisfying

\[
R(p_x)=\rho_x
\]

for every physically admissible outcome law in the declared model.

Define the reconstruction stability constant

\[
\boxed{
\kappa_R
:=
\frac12
\sup_{v\neq0}
\frac{\|R(v)\|_1}{\|v\|_1}.
}
\]

Equivalently,

\[
\boxed{
\frac12\|R(v)\|_1
\le
\kappa_R\|v\|_1.
}
\]

The value \(\kappa_R\) is part of the declared tomography design. A poorly conditioned reconstruction has a larger \(\kappa_R\) and therefore requires more samples.

For the target, let \(P_x\) be an independently defined categorical distribution on an alphabet of size \(k\). Let \(\widehat P_x\) be the empirical distribution from \(n_Y\) IID target observations for preparation \(x\).

---

## 2. P42A: simultaneous quantum frequency concentration

For one preparation and one POVM outcome, Hoeffding gives

\[
\Pr\left(
|\widehat p_x(j)-p_x(j)|>t
\right)
\le2e^{-2n_Qt^2}.
\]

There are \(Km\) declared preparation-outcome coordinates. A union bound therefore gives simultaneous coverage at level \(1-\alpha_Q\) for

\[
\boxed{
t_Q
=
\sqrt{
\frac{\log(2Km/\alpha_Q)}{2n_Q}
}.
}
\]

On that event,

\[
\|\widehat p_x-p_x\|_1
\le mt_Q
\qquad\forall x.
\]

Define the raw linear reconstruction

\[
\widetilde\rho_x=R(\widehat p_x).
\]

The reconstruction stability inequality gives

\[
\begin{aligned}
\frac12
\|\widetilde\rho_x-\rho_x\|_1
&=
\frac12
\|R(\widehat p_x-p_x)\|_1\\
&\le
\kappa_R
\|\widehat p_x-p_x\|_1\\
&\le
\kappa_R mt_Q.
\end{aligned}
\]

Hence the simultaneous quantum radius is

\[
\boxed{
r_Q
=
\kappa_R m
\sqrt{
\frac{\log(2Km/\alpha_Q)}{2n_Q}
}.
}
\]

### Important estimator boundary

The raw linear estimate \(\widetilde\rho_x\) need not be positive semidefinite. P42 therefore does not call it a density operator. The theorem uses the Hermitian trace-norm error around the true density operator. If a constrained physical estimator is used instead, its own finite-sample coverage theorem must replace this step.

---

## 3. Pairwise quantum upper envelope from raw reconstructions

For any pair \(x,x'\), triangle inequality gives

\[
D(\rho_x,\rho_{x'})
\le
\frac12
\|\widetilde\rho_x-\widetilde\rho_{x'}\|_1
+2r_Q.
\]

Because the true trace distance is at most one, define

\[
\boxed{
\widehat U_{xx'}
=
\min\left\{
1,
\frac12
\|\widetilde\rho_x-\widetilde\rho_{x'}\|_1
+2r_Q
\right\}.
}
\]

Then on the simultaneous quantum event,

\[
\boxed{
D(\rho_x,\rho_{x'})
\le\widehat U_{xx'}
\quad\forall x,x'.
}
\]

This is the P41 quantum envelope with an explicit finite-sample radius.

---

## 4. P42B: simultaneous target total-variation concentration

For each target category and preparation, the same coordinate Hoeffding argument gives

\[
\boxed{
t_Y
=
\sqrt{
\frac{\log(2Kk/\alpha_Y)}{2n_Y}
}.
}
\]

On the corresponding simultaneous event,

\[
\|\widehat P_x-P_x\|_1
\le kt_Y
\qquad\forall x.
\]

Therefore

\[
\boxed{
\|\widehat P_x-P_x\|_{\mathrm{TV}}
\le
\varepsilon_Y
:=
\frac{k}{2}
\sqrt{
\frac{\log(2Kk/\alpha_Y)}{2n_Y}
}
}
\]

for every preparation. The numerical radius may be clipped at one without weakening the statement.

For each pair define the P41-compatible target lower envelope

\[
\boxed{
\widehat L_{xx'}
=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-2\varepsilon_Y
\right]_+.
}
\]

On the simultaneous target event,

\[
\|P_x-P_{x'}\|_{\mathrm{TV}}
\ge\widehat L_{xx'}.
\]

---

## 5. P42C: direct empirical Lipschitz obstruction

Suppose the declared bridge class is \(L\)-Lipschitz in quantum trace distance:

\[
\boxed{
\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}
\le
L D(\rho,\sigma).
}
\]

Define

\[
\boxed{
\widehat M_{xx'}
=
\widehat L_{xx'}
-L\widehat U_{xx'}.
}
\]

If

\[
\boxed{
\widehat M_{xx'}>0
}
\]

for any pair, then no bridge in the declared \(L\)-Lipschitz class can reproduce the true target laws from any true quantum states consistent with the declared simultaneous concentration events.

By the union bound over the two confidence events, the certificate has confidence at least

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

No statistical independence between the quantum and target data sets is required for this joint coverage statement. IID sampling is required within each declared sample stream for the Hoeffding bounds used here.

---

## 6. P42D: population-gap power theorem

The direct P41 design inequality is not yet a sample-size guarantee because the pairwise empirical distances also fluctuate.

For one planned preparation pair define the population distances

\[
d_Q=D(\rho_x,\rho_{x'}),
\qquad
d_Y=\|P_x-P_{x'}\|_{\mathrm{TV}}.
\]

Define the population regularity gap

\[
\boxed{
\Delta=d_Y-Ld_Q.
}
\]

Assume

\[
\boxed{
\Delta>0.
}
\]

On the simultaneous target event,

\[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
\ge d_Y-2\varepsilon_Y,
\]

so

\[
\widehat L_{xx'}
\ge d_Y-4\varepsilon_Y
\]

whenever the right side is positive.

Likewise, the pairwise raw quantum reconstruction distance obeys

\[
\frac12
\|\widetilde\rho_x-\widetilde\rho_{x'}\|_1
\le d_Q+2r_Q.
\]

Therefore its certified upper envelope satisfies, before clipping at one,

\[
\widehat U_{xx'}
\le d_Q+4r_Q.
\]

Combining the two sides yields

\[
\boxed{
\widehat M_{xx'}
\ge
\Delta
-4\varepsilon_Y
-4Lr_Q.
}
\]

This factor of four is important. One uncertainty allowance controls the empirical pair distance relative to the population pair distance, and a second allowance is consumed by the confidence envelope used in the actual certificate. P42 keeps both costs explicit rather than silently reusing the P41 deterministic radius budget.

Consequently, the sufficient condition

\[
\boxed{
4\varepsilon_Y+4Lr_Q<\Delta
}
\]

guarantees a positive empirical obstruction margin on the simultaneous confidence event, provided the quantum upper-envelope clipping does not itself erase the planned gap.

---

## 7. Allocated sample-complexity theorem

Choose an allocation parameter

\[
\lambda\in(0,1).
\]

Assign a fraction \(\lambda\Delta\) of the population gap to target uncertainty and the remaining \((1-\lambda)\Delta\) to quantum uncertainty:

\[
4\varepsilon_Y
\le
\lambda\Delta,
\]

\[
4Lr_Q
\le
(1-\lambda)\Delta.
\]

Substituting the explicit radii and solving for the per-preparation sample sizes gives

\[
\boxed{
n_Y
\ge
\frac{2k^2}{\lambda^2\Delta^2}
\log\frac{2Kk}{\alpha_Y}
}
\]

and, for \(L\kappa_R>0\),

\[
\boxed{
n_Q
\ge
\frac{8L^2\kappa_R^2m^2}
{(1-\lambda)^2\Delta^2}
\log\frac{2Km}{\alpha_Q}.
}
\]

Taking ceilings gives integer sufficient sample sizes.

### Proposition 42

Under the declared fixed IC measurement, exact linear reconstruction relation \(R(p_x)=\rho_x\), stability constant \(\kappa_R\), categorical IID target model, and \(L\)-Lipschitz bridge class, if a preparation pair has population gap \(\Delta>0\) and \(n_Q,n_Y\) satisfy the two inequalities above, then the P42 empirical obstruction is positive on the simultaneous quantum and target concentration event. Hence the declared \(L\)-Lipschitz bridge class is rejected for that pair with confidence at least

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

The result is a sufficient design theorem, not a necessary sample-size bound.

---

## 8. Balanced-allocation corollary

For

\[
\lambda=\frac12,
\]

the sufficient sample sizes simplify to

\[
\boxed{
n_Y
\ge
\frac{8k^2}{\Delta^2}
\log\frac{2Kk}{\alpha_Y}
}
\]

and

\[
\boxed{
n_Q
\ge
\frac{32L^2\kappa_R^2m^2}{\Delta^2}
\log\frac{2Km}{\alpha_Q}.
}
\]

These formulas make four design dependencies explicit:

1. both sample requirements scale as \(\Delta^{-2}\);
2. the quantum requirement scales as \(L^2\);
3. the quantum requirement scales as \(\kappa_R^2\), directly exposing tomography conditioning;
4. the coordinate-union construction gives conservative quadratic dependence on alphabet/outcome counts through \(k^2\) and \(m^2\), with only logarithmic dependence on the number of preparations \(K\).

---

## 9. What can improve these bounds

P42 intentionally uses elementary concentration. Tighter results may replace the coordinate union bounds with multinomial concentration, likelihood-ratio regions, matrix concentration, shadow-tomography methods, or estimator-specific confidence regions.

Any such replacement must preserve the same logical structure:

\[
\boxed{
\text{valid quantum uncertainty}
+
\text{valid target uncertainty}
+
\text{declared bridge regularity}
\Longrightarrow
\text{finite-data obstruction certificate}.
}
\]

A better statistical radius improves power. It does not weaken the need for an explicit physical descriptor, an independent target, and a justified bridge class.

---

## 10. Scientific boundary

P42 can establish only that a particular finite-data experiment has enough declared precision to reject a specified \(L\)-Lipschitz bridge class for the specified quantum descriptor and tomography design.

It does not establish that quantum mechanics is incomplete. It does not establish that all quantum descriptions fail. It does not prove that the chosen system boundary includes every physically relevant degree of freedom. It does not establish that \(L\)-Lipschitz regularity is mandatory. It does not establish that the target is consciousness.

For an experiential application, the experiential variables and their measurement model must be justified independently of the quantum variables used in the factorization test.

---

## 11. Reproducibility

Implementation:
[`quantum_regular_bridge_sample_complexity.py`](../src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py)

Regression tests:
[`test_quantum_regular_bridge_sample_complexity.py`](../tests/test_quantum_regular_bridge_sample_complexity.py)

---

## 12. Next theorem target

P42 supplies a conservative fixed-allocation sample size. It treats all preparations with the same \(n_Q\) and \(n_Y\), even though only a small number of preparation pairs may carry the largest regularity gap.

The next justified extension is an **adaptive or optimized sampling theorem** that allocates quantum measurements and target observations across preparations according to certified pairwise obstruction potential while preserving post-selection validity. A separate route is to bypass full state reconstruction and derive a measurement-frequency certificate directly from a declared informationally complete experiment class.
