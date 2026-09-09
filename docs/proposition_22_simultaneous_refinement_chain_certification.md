# Proposition 22 - Simultaneous Finite-Sample Certification of Physical-Refinement Chains

## Status

**Proved finite-alphabet IID simultaneous-certification theorem for nested deterministic physical descriptors.**

![P22 simultaneous refinement-chain certification](figures/p22_simultaneous_refinement_chain_certification.svg)

**P22 theorem map.** One confidence event for the empirical \((\Omega,E)\) distribution controls every descriptor-relative residual and every P21 refinement gain in the declared chain. No separate confidence allocation over refinement levels is required for this construction.

P22 combines three earlier layers:

- [P19](proposition_19_fundamental_physical_sufficiency.md): population physical sufficiency and the residual \(I(E;\Omega\mid T)\);
- [P20](proposition_20_finite_sample_residual_certification.md): a conservative finite-alphabet IID confidence bound for one conditional-information residual;
- [P21](proposition_21_descriptor_refinement_residual_persistence.md): exact residual monotonicity and refinement-gain decomposition across nested physical descriptors.

The new question is:

> can the entire refinement trajectory be certified from one finite data set without treating every descriptor level as a separate statistical experiment?

For deterministic descriptor chains, the answer is yes.

---

# 1. Declared finite-alphabet model

Let the sampled base variable be

\[
Z=(\Omega,E)
\]

with finite alphabets

\[
|\mathcal \Omega|=d_\Omega,
\qquad
|\mathcal E|=d_E.
\]

Assume

\[
Z_1,\ldots,Z_n
\overset{\mathrm{IID}}{\sim}
P_{\Omega E}.
\]

Let

\[
T_0,T_1,\ldots,T_m
\]

be declared deterministic physical descriptors satisfying

\[
T_k=f_k(\Omega)
\]

and the nested refinement relations

\[
\boxed{
T_{k-1}=c_k(T_k),
\qquad
k=1,\ldots,m.
}
\]

Write

\[
|\mathcal T_k|=d_k.
\]

The theorem assumes the descriptor maps and nesting relations hold on the declared physical alphabet. The executable implementation can check consistency on the observed support, but an empirical support check is not a proof that an undeclared map is globally well defined.

---

# 2. One base confidence event

Let

\[
\widehat P_{\Omega E}
\]

be the empirical base distribution.

Using the same cellwise Hoeffding argument as P20, now on the base alphabet of size

\[
M=d_\Omega d_E,
\]

define

\[
\boxed{
\tau_n(\alpha)
=
\min\left\{
1,
\frac{M}{2}
\sqrt{
\frac{1}{2n}
\log\left(\frac{2M}{\alpha}\right)
}
\right\}.
}
\]

Then

\[
\boxed{
\Pr\left(
\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\right)
\ge
1-\alpha.
}
\]

Call this event \(\mathcal A_n\).

The important point is that \(\mathcal A_n\) is defined **before** choosing any particular level-specific conditional-information expression. It is a confidence event for the common base law.

---

# 3. Deterministic pushforward lemma

For every descriptor level define

\[
\phi_k(\omega,e)
=
(\omega,f_k(\omega),e).
\]

The level-specific joint law is

\[
P_k=(\phi_k)_\#P_{\Omega E},
\]

and its empirical counterpart is

\[
\widehat P_k=(\phi_k)_\#\widehat P_{\Omega E}.
\]

Total variation contracts under deterministic pushforward, so on \(\mathcal A_n\),

\[
\boxed{
\|P_k-\widehat P_k\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\qquad
\text{for every }k.
}
\]

The same event also controls the refinement-gain distributions. For \(k\ge1\), define

\[
\psi_k(\omega,e)
=
(f_k(\omega),f_{k-1}(\omega),e).
\]

Then

\[
Q_k=(\psi_k)_\#P_{\Omega E},
\qquad
\widehat Q_k=(\psi_k)_\#\widehat P_{\Omega E},
\]

and therefore

\[
\boxed{
\|Q_k-\widehat Q_k\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\qquad
\text{for every }k=1,\ldots,m.
}
\]

No second probabilistic argument is needed. Every inequality follows deterministically from the same base event.

---

# 4. Simultaneous residual intervals

Define the P21 residual trajectory

\[
\boxed{
R_k
:=
I(E;\Omega\mid T_k),
\qquad
k=0,\ldots,m.
}
\]

Let

\[
\widehat R_k
=
I_{\widehat P}(E;\Omega\mid T_k).
\]

P20 supplies a finite-alphabet continuity function

\[
\Delta_k(\tau)
\]

for the conditional-mutual-information functional on alphabet sizes

\[
(d_\Omega,d_k,d_E).
\]

Because every level-specific distribution lies inside the same TV ball on \(\mathcal A_n\),

\[
\boxed{
|R_k-\widehat R_k|
\le
\Delta_k(\tau_n(\alpha))
\qquad
\text{for all }k=0,\ldots,m
}
\]

**simultaneously** with probability at least \(1-\alpha\).

Thus define

\[
L_k^R
=
\max\{0,\widehat R_k-\Delta_k\},
\]

\[
U_k^R
=
\min\{R_{\max},\widehat R_k+\Delta_k\},
\]

where

\[
R_{\max}
=
\min\{\log d_\Omega,\log d_E\}.
\]

Then

\[
\boxed{
\Pr\left(
R_k\in[L_k^R,U_k^R]
\text{ for every }k
\right)
\ge1-\alpha.
}
\]

---

# 5. Simultaneous refinement-gain intervals

P21 defines the information captured by refinement step \(k\) as

\[
\boxed{
G_k
:=
I(E;T_k\mid T_{k-1}),
\qquad k=1,\ldots,m.
}
\]

Its empirical estimate is

\[
\widehat G_k
=
I_{\widehat P}(E;T_k\mid T_{k-1}).
\]

Apply the P20 continuity construction to the alphabet dimensions

\[
(d_k,d_{k-1},d_E)
\]

to obtain a direct radius

\[
\Gamma_k(\tau_n(\alpha)).
\]

On the same event \(\mathcal A_n\),

\[
\boxed{
|G_k-\widehat G_k|
\le
\Gamma_k(\tau_n(\alpha))
\qquad
\text{for all }k=1,\ldots,m.
}
\]

Again, all gain intervals hold simultaneously at the same confidence level.

---

# 6. P21 identity sharpens the gain interval

P21 proves the population identity

\[
\boxed{
G_k=R_{k-1}-R_k.
}
\]

The same algebra holds for the empirical distribution:

\[
\boxed{
\widehat G_k
=
\widehat R_{k-1}-\widehat R_k.
}
\]

Therefore the residual intervals imply a second valid interval for \(G_k\):

\[
G_k
\ge
\max\{0,L_{k-1}^R-U_k^R\},
\]

\[
G_k
\le
\min\{G_{k,\max},U_{k-1}^R-L_k^R\},
\]

where

\[
G_{k,\max}
=
\min\{\log d_k,\log d_E\}.
\]

P22 intersects this difference-based interval with the direct CMI-continuity interval. The intersection cannot weaken coverage on \(\mathcal A_n\) because both intervals contain the same population quantity on that event.

This provides a stricter executable certificate whenever the two constructions contribute complementary information.

---

# 7. Main theorem

## Proposition 22 - simultaneous refinement-chain certification

Under the finite-alphabet IID model and declared deterministic nested descriptors above, let \(\mathcal I_k^R\) be the P22 residual intervals and \(\mathcal I_k^G\) the intersected refinement-gain intervals.

Then

\[
\boxed{
\Pr\left(
\bigcap_{k=0}^{m}
\{R_k\in\mathcal I_k^R\}
\cap
\bigcap_{k=1}^{m}
\{G_k\in\mathcal I_k^G\}
\right)
\ge
1-\alpha.
}
\]

### Proof

P20's Hoeffding construction gives the base event \(\mathcal A_n\) with probability at least \(1-\alpha\).

Condition on \(\mathcal A_n\). Total-variation contraction transfers the same radius to every deterministic pushforward \(P_k\) and \(Q_k\). The P20 entropy-continuity argument is deterministic once a TV radius is known, so every residual inequality and every direct gain inequality holds simultaneously on \(\mathcal A_n\).

P21 supplies

\[
G_k=R_{k-1}-R_k,
\]

so the difference-based gain interval also contains \(G_k\) on \(\mathcal A_n\). Intersecting two intervals that both contain \(G_k\) preserves containment on that event.

Therefore the entire residual-and-gain interval family holds whenever \(\mathcal A_n\) occurs. Since

\[
\Pr(\mathcal A_n)\ge1-\alpha,
\]

the simultaneous statement follows. \(\square\)

---

# 8. Why there is no extra factor for the number of levels

A naive strategy would apply P20 separately to each residual and each gain and then allocate confidence across the resulting family of tests.

P22 instead certifies the common base law once:

\[
P_{\Omega E}
\longrightarrow
\left\{
P_0,\ldots,P_m,Q_1,\ldots,Q_m
\right\}
\]

through deterministic pushforwards.

The probabilistic event is therefore

\[
\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}
\le\tau_n(\alpha),
\]

not a collection of separately sampled events indexed by \(k\).

Consequently, this construction does not replace \(\alpha\) by \(\alpha/(2m+1)\).

This does **not** mean that arbitrarily long refinement chains are statistically free. The continuity radii still depend on descriptor alphabet sizes, and the base Hoeffding radius can be extremely conservative when \(d_\Omega d_E\) is large.

---

# 9. Certification statements

P22 supports several precise finite-data conclusions.

## Terminal residual persistence

If

\[
\boxed{L_m^R>0,}
\]

then

\[
R_m>0
\]

with simultaneous confidence at least \(1-\alpha\) under the declared finite-alphabet IID model and descriptor chain.

The correct interpretation is:

> the finest declared physical descriptor in the tested chain has not screened off the target under the model.

It is not a physical-completeness theorem.

## Certified informative refinement

If

\[
\boxed{L_k^G>0,}
\]

then refinement step \(T_{k-1}\preceq T_k\) captures strictly positive target-relevant information with the same simultaneous confidence guarantee.

## Unresolved step

If a lower bound is zero, the finite data do not certify positivity. This is not evidence that the population quantity is zero.

---

# 10. Relation to the P21 monotone trajectory

At the population level P21 gives

\[
R_0\ge R_1\ge\cdots\ge R_m\ge0
\]

and

\[
R_0-R_m
=
\sum_{k=1}^{m}G_k.
\]

P22 does not replace that theorem. It places simultaneous finite-data uncertainty around the entire structure:

\[
\boxed{
R_k\in[L_k^R,U_k^R]
\quad\forall k
}
\]

and

\[
\boxed{
G_k\in[L_k^G,U_k^G]
\quad\forall k
}
\]

on one event of probability at least \(1-\alpha\).

The empirical chain-rule discrepancy is also checked numerically. Under exactly nested deterministic descriptors, the empirical identity should close up to floating-point tolerance.

---

# 11. Executable implementation

The implementation is

[`refinement_chain_certification.py`](../src/consciousness_bridge/refinement_chain_certification.py).

It provides:

- validation of declared alphabet sizes;
- observed-support checks that descriptors are deterministic functions of \(\Omega\);
- observed-support checks of nested refinement;
- one shared base-TV confidence radius;
- simultaneous residual confidence intervals;
- simultaneous direct refinement-gain intervals;
- P21 difference-based gain intervals;
- intersection of the two gain certificates;
- empirical chain-rule closure checks;
- terminal residual-persistence certification.

Regression tests are in

[`test_refinement_chain_certification.py`](../tests/test_refinement_chain_certification.py).

The executable checks observed data and theorem identities. A scientific application must still declare the physical descriptor maps on the intended physical domain, not merely infer global validity from the samples that happened to be observed.

---

# 12. Statistical and physical limitations

P22 is deliberately narrow.

It assumes:

- finite alphabets;
- IID samples;
- a declared base physical-state alphabet;
- deterministic descriptor maps;
- a globally valid nested descriptor chain;
- exact categorical observations.

It does not yet cover:

- continuous or extremely high-dimensional physical state spaces;
- dependent time series;
- hidden-state uncertainty;
- noisy descriptor assignment;
- quantum measurement models requiring operator-level confidence regions;
- estimator-specific improvements beyond the conservative empirical-cell Hoeffding baseline.

The base alphabet is especially important. The radius scales with \(d_\Omega d_E\), so the theorem can become numerically weak long before it becomes mathematically invalid.

---

# 13. Research boundary

P22 strengthens the statistical treatment of omitted physics. It does not establish an ontological conclusion.

Even if

\[
L_m^R>0,
\]

the result remains relative to:

- the declared physical state \(\Omega\);
- the declared descriptor family;
- the target variable \(E\);
- the sampling assumptions;
- the measurement model.

P21's identity-descriptor boundary remains decisive:

\[
I(E;\Omega\mid\Omega)=0.
\]

Therefore neither P21 nor P22 turns residual persistence into a proof that consciousness is outside physics or occupies an additional spacetime dimension.

Their scientific value is different: they make the omitted-physics objection explicit, quantitative, and testable across an entire physical-refinement program.
