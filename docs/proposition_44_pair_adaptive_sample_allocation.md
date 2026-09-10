# Proposition 44: Pair-adaptive sample allocation with valid post-selection

## Status

**Proved finite-family simultaneous-confidence and post-selection theorem.** P44 extends the P42-P43 experimental design from one preselected preparation pair to a finite declared family of candidate pairs. It allows the final witness pair to be chosen after observing the data without losing the stated confidence level, provided the complete candidate family is covered by a predeclared error budget.

The result does not require independence between candidate-pair analyses. Shared preparations and shared observations are allowed as long as every stated marginal confidence event is valid.

P44 does not establish physical completeness, quantum incompleteness, or consciousness.

---

## 1. Setup

Let

\[
\mathcal J=\{1,\ldots,J\}
\]

index a finite declared family of candidate preparation pairs. Candidate \(j\) has a true population regularity margin

\[
\boxed{
M_j
=
d_{Y,j}-L_jd_{Q,j},
}
\]

where \(d_{Y,j}\) is the target-law total-variation separation, \(d_{Q,j}\) is the quantum trace distance, and \(L_j\ge0\) is the declared bridge Lipschitz constant for that candidate analysis.

For each candidate, suppose the P41-P42 analysis returns a random lower confidence margin

\[
\underline M_j.
\]

Allocate candidate-specific failure probabilities

\[
\alpha_{Q,j}\ge0,
\qquad
\alpha_{Y,j}\ge0,
\]

such that

\[
\boxed{
\sum_{j=1}^J\alpha_{Q,j}\le\alpha_Q,
\qquad
\sum_{j=1}^J\alpha_{Y,j}\le\alpha_Y.
}
\]

Assume for every candidate that the quantum and target confidence constructions imply

\[
\Pr(\underline M_j\le M_j)
\ge
1-\alpha_{Q,j}-\alpha_{Y,j}.
\]

No pairwise independence assumption is made.

---

## 2. P44A: simultaneous family coverage

Define the valid-margin event

\[
E_j=\{\underline M_j\le M_j\}.
\]

By the union bound,

\[
\begin{aligned}
\Pr\left(\bigcap_{j=1}^J E_j\right)
&=1-\Pr\left(\bigcup_{j=1}^J E_j^c\right)\\
&\ge
1-\sum_{j=1}^J\Pr(E_j^c)\\
&\ge
1-\sum_{j=1}^J(\alpha_{Q,j}+\alpha_{Y,j}).
\end{aligned}
\]

Therefore

\[
\boxed{
\Pr\left(
\underline M_j\le M_j
\ \forall j\in\mathcal J
\right)
\ge
1-\alpha_Q-\alpha_Y.
}
\]

The lower bound is clipped at zero if the declared total error budget exceeds one.

### Interpretation

The family event is simultaneous. Once it holds, every candidate lower margin is valid at the same time. Dependence among the candidates does not weaken the union-bound statement.

---

## 3. P44B: arbitrary data-dependent pair selection

Let

\[
\widehat j=\mathcal S(\mathcal D)
\]

be any measurable selection rule based on the observed data \(\mathcal D\), with values in the predeclared candidate family \(\mathcal J\).

On the simultaneous event from P44A,

\[
\underline M_j\le M_j
\quad\forall j.
\]

In particular, this inequality holds at the random selected index:

\[
\boxed{
\underline M_{\widehat j}
\le
M_{\widehat j}.
}
\]

Hence

\[
\boxed{
\underline M_{\widehat j}>0
\Longrightarrow
M_{\widehat j}>0
}
\]

with confidence at least

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

This remains valid even when \(\widehat j\) is chosen specifically because it looks most favorable in the data.

---

## 4. Maximum-lower-margin selector

A natural rule is

\[
\boxed{
\widehat j
\in
\arg\max_{j\in\mathcal J}\underline M_j.
}
\]

Define

\[
\boxed{
\underline M_*
=
\max_{j\in\mathcal J}\underline M_j.
}
\]

Then

\[
\boxed{
\underline M_*>0
}
\]

certifies that the selected pair has a positive population regularity margin at the same simultaneous confidence level.

This is not a claim that the selected pair has the largest true population margin. Selection is based on lower confidence margins, not on unobserved population values.

---

## 5. P44C: weighted confidence spending

Let positive design weights \(w_{Q,j}\) and \(w_{Y,j}\) be chosen before inspecting the evidence used for certification. Normalize them as

\[
\pi_{Q,j}
=
\frac{w_{Q,j}}{\sum_{\ell=1}^Jw_{Q,\ell}},
\qquad
\pi_{Y,j}
=
\frac{w_{Y,j}}{\sum_{\ell=1}^Jw_{Y,\ell}}.
\]

The allocation

\[
\boxed{
\alpha_{Q,j}=\alpha_Q\pi_{Q,j},
\qquad
\alpha_{Y,j}=\alpha_Y\pi_{Y,j}
}
\]

uses the complete family error budget exactly and therefore preserves P44A-P44B.

Equal weights recover the Bonferroni allocation

\[
\alpha_{Q,j}=\frac{\alpha_Q}{J},
\qquad
\alpha_{Y,j}=\frac{\alpha_Y}{J}.
\]

The weights can encode scientific priority or anticipated efficiency, but they must not be retroactively chosen from the same evidence unless the resulting adaptive rule is separately covered by a valid theorem.

---

## 6. P44D: pair-specific P42-P43 sample design

For candidate \(j\), let

\[
\Delta_j=d_{Y,j}-L_jd_{Q,j}>0
\]

be the anticipated population gap and define the P42 coefficients using the candidate-specific confidence spending:

\[
\boxed{
A_{Y,j}
=
\frac{2k_j^2}{\Delta_j^2}
\log\frac{2K_jk_j}{\alpha_{Y,j}},
}
\]

\[
\boxed{
A_{Q,j}
=
\frac{8L_j^2\kappa_{R,j}^2m_j^2}{\Delta_j^2}
\log\frac{2K_jm_j}{\alpha_{Q,j}}.
}
\]

With positive per-sample costs \(c_{Y,j},c_{Q,j}\), P43 gives the candidate-specific optimal uncertainty split

\[
\boxed{
\lambda_j^*
=
\frac{(c_{Y,j}A_{Y,j})^{1/3}}
{(c_{Y,j}A_{Y,j})^{1/3}+(c_{Q,j}A_{Q,j})^{1/3}}.
}
\]

Sufficient integer sample counts are

\[
\boxed{
N_{Y,j}
=
\left\lceil
\frac{A_{Y,j}}{(\lambda_j^*)^2}
\right\rceil,
\qquad
N_{Q,j}
=
\left\lceil
\frac{A_{Q,j}}{(1-\lambda_j^*)^2}
\right\rceil.
}
\]

If every candidate analysis satisfies its declared P42-P43 construction with its allocated confidence budget, then all candidate lower margins are simultaneously valid and the final pair may be selected after seeing the data.

### Shared observations

These formulas are sufficient candidate-level requirements. When candidate pairs share preparations, the same observations may contribute to multiple candidate analyses. P44 does not require duplicating those observations merely because they appear in more than one pair. Exact global cost optimization under shared preparation counts is a separate combinatorial design problem.

---

## 7. Why naive winner selection is not enough

Suppose each candidate is analyzed at nominal failure probability \(\alpha\), and the most favorable result is selected afterward. Without simultaneous correction, one cannot generally claim family confidence \(1-\alpha\). The probability that at least one candidate bound fails can grow with the number of candidates.

P44 closes this gap by requiring

\[
\sum_j(\alpha_{Q,j}+\alpha_{Y,j})
\le
\alpha_Q+\alpha_Y.
\]

The price of post-selection validity is therefore explicit in the logarithmic confidence terms of the P42 sample sizes.

---

## 8. Scientific boundary

P44 proves only a statistical statement about selecting among a finite predeclared family of P42-P43 regularity tests.

A positive selected margin means

\[
\boxed{
\text{the selected declared quantum descriptor and bridge regularity class are incompatible with the target laws under the stated confidence model}.
}
\]

It does not establish that a richer quantum descriptor cannot work. It does not establish that the modeled system boundary is complete. It does not establish that the target is consciousness. It does not establish that quantum mechanics is incomplete.

Candidate-family choice, measurement validity, tomography assumptions, bridge regularity, target independence, omitted environment variables, and nonstationarity remain part of the scientific burden.

---

## 9. Next theorem target

P44 controls selection over a finite fixed candidate family, but it does not optimize shared preparation-level sampling when one preparation participates in many candidate pairs.

The next design problem is a graph allocation theorem. Preparations are vertices, candidate pairs are edges, and one sample count at a vertex contributes simultaneously to every incident edge. The objective is to minimize total experimental cost while satisfying all edgewise quantum and target precision constraints required for a declared family certificate.

That problem should separate:

1. statistical validity of the simultaneous family event,
2. resource sharing across incident candidate pairs,
3. integer sample allocation,
4. adaptive stopping or expansion of the candidate graph.

---

## 10. Reproducibility

Implementation:
[`pair_adaptive_sample_allocation.py`](../src/consciousness_bridge/pair_adaptive_sample_allocation.py)

Regression tests:
[`test_pair_adaptive_sample_allocation.py`](../tests/test_pair_adaptive_sample_allocation.py)
