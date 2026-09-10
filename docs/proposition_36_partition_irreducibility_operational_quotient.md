# Proposition 36: Approximate partition-irreducibility stability under operational quotienting

## Status

**Proved product-reference perturbation theorem for the P11 partition branch.** P36 closes the second approximate branch left open by P34. It propagates intervention-delay response ambiguity through the partition-product operator and gives an explicit bound for the resulting change in partition irreducibility.

The key point is that a partition statistic compares a response law not with a fixed reference, but with the product of its own block marginals. Therefore the reference distribution also moves when the response law changes.

P36 handles that movement explicitly.

---

## 1. Fixed-partition irreducibility

Let the physical state space be partitioned into \(m\) blocks

\[
\pi=\{B_1,\ldots,B_m\}.
\]

For a response law \(P\), let \(P_{B_j}\) denote its marginal on block \(B_j\). Define the partition-product reference

\[
\Pi_\pi(P)
=
\bigotimes_{j=1}^{m}P_{B_j}.
\]

The partition irreducibility statistic is

\[
\boxed{
\kappa_\pi(P)
=
\left\|
P-\Pi_\pi(P)
\right\|_{\mathrm{TV}}.
}
\]

---

## 2. Marginal contraction

Suppose two response laws satisfy

\[
\|P-Q\|_{\mathrm{TV}}\le\eta.
\]

Marginalization is a deterministic pushforward, so total variation contracts:

\[
\boxed{
\|P_{B_j}-Q_{B_j}\|_{\mathrm{TV}}
\le
\eta
\qquad
j=1,\ldots,m.
}
\]

---

## 3. Product-reference stability lemma

For probability measures \(P_j,Q_j\) on the corresponding block spaces,

\[
\left\|
\bigotimes_{j=1}^{m}P_j
-
\bigotimes_{j=1}^{m}Q_j
\right\|_{\mathrm{TV}}
\le
\sum_{j=1}^{m}
\|P_j-Q_j\|_{\mathrm{TV}}.
\]

This follows from a telescoping replacement of one factor at a time together with invariance of total variation under multiplication by a common probability factor.

Applying the marginal contraction bound gives

\[
\boxed{
\|\Pi_\pi(P)-\Pi_\pi(Q)\|_{\mathrm{TV}}
\le
m\eta.
}
\]

---

## 4. Fixed-partition perturbation theorem

Using the reverse triangle inequality,

\[
\begin{aligned}
|\kappa_\pi(P)-\kappa_\pi(Q)|
&\le
\|P-Q\|_{\mathrm{TV}}
+
\|\Pi_\pi(P)-\Pi_\pi(Q)\|_{\mathrm{TV}}\\
&\le
\eta+m\eta.
\end{aligned}
\]

Therefore

\[
\boxed{
|\kappa_\pi(P)-\kappa_\pi(Q)|
\le
(m+1)\eta.
}
\]

This is the central P36 result.

---

## 5. Operational quotient corollary

Let \(\eta_{a\times b}\) be the P33 joint intervention-delay response ambiguity after the common node/state map.

For two admissible representatives of one coarse operational cell,

\[
\|P-Q\|_{\mathrm{TV}}\le\eta_{a\times b}.
\]

Hence for any descendable \(m\)-block partition,

\[
\boxed{
|\kappa_{\pi,s}-\kappa_{\pi,s'}|
\le
(m+1)\eta_{a\times b}.
}
\]

Using P33,

\[
\boxed{
|\kappa_{\pi,s}-\kappa_{\pi,s'}|
\le
(m+1)(\eta_b+\eta_a).
}
\]

---

## 6. Minimum-over-partitions irreducibility

Suppose a declared irreducibility score takes the minimum over an admissible family \(\mathfrak P\):

\[
K(P)=\min_{\pi\in\mathfrak P}\kappa_\pi(P).
\]

Let

\[
m_{\max}
=
\max_{\pi\in\mathfrak P}|\pi|.
\]

For any two functions \(f_\pi,g_\pi\),

\[
\left|\min_\pi f_\pi-\min_\pi g_\pi\right|
\le
\max_\pi|f_\pi-g_\pi|.
\]

Therefore

\[
\boxed{
|K(P)-K(Q)|
\le
(m_{\max}+1)\eta.
}
\]

and under the P33 operational quotient

\[
\boxed{
|K_s-K_{s'}|
\le
(m_{\max}+1)\eta_{a\times b}.
}
\]

---

## 7. Full node/state/intervention/time bound

P26/P30 give the node/state partition bound

\[
D_K^{\mathrm{node}}
\le
\rho_P^*+\rho_\Pi^*.
\]

P36 adds the operational representative term. Hence

\[
\boxed{
D_K^{\mathrm{full}}
\le
\rho_P^*+\rho_\Pi^*
+(m_{\max}+1)\eta_{a\times b}.
}
\]

Using the separate P31/P32 audits,

\[
\boxed{
D_K^{\mathrm{full}}
\le
\rho_P^*+\rho_\Pi^*
+(m_{\max}+1)(\eta_b+\eta_a).
}
\]

This is the missing quantitative partition branch required by P34.

---

## 8. Threshold preservation

If a partition or global irreducibility decision uses threshold \(\theta_K\), define

\[
\varepsilon_K
=
\rho_P^*+\rho_\Pi^*
+(m_{\max}+1)\eta_{a\times b}.
\]

Whenever

\[
\boxed{
|K-\theta_K|>\varepsilon_K,
}
\]

the threshold classification is invariant under the declared complete scale transformation.

---

## 9. Semantic condition

The bound applies only to partitions that descend under the P27 saturation criterion and to operational cells that have the P34-C8 meaning.

Thus

\[
\boxed{
\text{numerical stability}
\not\Rightarrow
\text{valid partition semantics}.
}
\]

A non-descendable partition cannot be rescued by a small perturbation bound.

---

## 10. Why the factor \(m+1\) appears

One factor of \(\eta\) comes from moving the actual response law.

The remaining at most \(m\eta\) comes from moving the \(m\) block marginals that form the partition-product reference.

Therefore

\[
\boxed{
(m+1)\eta
=
\underbrace{\eta}_{\text{response movement}}
+
\underbrace{m\eta}_{\text{factorized-reference movement}}.
}
\]

This is why reusing the geometry constant \(2\eta\) would generally be unjustified for a multi-block partition statistic.

---

## 11. Relation to the theorem chain

P34 identified the missing approximate branches.

P35 proved

\[
D_A^{\mathrm{full}}
\le
2\rho_A^*+2\eta_{a\times b}.
\]

P36 now proves

\[
D_K^{\mathrm{full}}
\le
\rho_P^*+\rho_\Pi^*+(m_{\max}+1)\eta_{a\times b}.
\]

Together with the P34 geometry result,

\[
D_G^{\mathrm{full}}
\le
2\rho_G^*+2\eta_{a\times b},
\]

the complete approximate P11 scale vector can now be assembled in the next proposition.

---

## 12. Scientific boundary

P36 is a stability theorem for one declared partition-product irreducibility statistic. It does not establish that this statistic measures consciousness or that independence across a partition has an experiential interpretation.

---

## 13. Reproducibility

Implementation: [`partition_irreducibility_operational_quotient.py`](../src/consciousness_bridge/partition_irreducibility_operational_quotient.py)

Tests: [`test_partition_irreducibility_operational_quotient.py`](../tests/test_partition_irreducibility_operational_quotient.py)
