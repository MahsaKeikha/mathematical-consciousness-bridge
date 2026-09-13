# Proposition 88: Held-Out Certification for a Discovery-Frozen P75 Box/P87 Functional Test

## Why this result matters

P87 can search **39,600 exact four-event parity functionals** and identify a strong incompatibility witness for a declared P75 parameter box. That creates a statistical problem: if the same observations are used both to discover the strongest-looking witness and to validate it, an ordinary single-test confidence statement ignores the selection step.

**P88 asks whether a discovered incompatibility can survive fresh data.**

The answer is yes under an explicit sample-splitting design. Discovery data may choose the P75 box and P87 functional by any discovery-only rule. The chosen pair is then frozen before an independent validation sample is examined. Conditional on discovery, one fixed scalar score is tested, so scalar Hoeffding concentration applies without a 39,600-way functional multiplicity penalty.

> **Status:** proved conditional finite-sample theorem with exact computational certificate.

> **Scientific boundary:** the certificate is for the P75 laws inside the frozen box unless a separate covering argument extends it. P88 does not identify the P75 latent state with consciousness, prove consciousness is nonphysical, validate an alternative ontology, or solve the physical-to-experiential bridge.

### Result at a glance

| Question | P88 answer |
| --- | --- |
| Can discovery search many P87 functionals? | Yes, if selection uses discovery data only. |
| Can the selected box and functional be changed after validation is seen? | No, not under this proof. |
| Is a 39,600-way validation union bound required? | No. One discovery-frozen scalar score is evaluated on independent validation data. |
| What does the stored witness certify? | A positive 95% lower-confidence bound on distance from the P75 laws inside the frozen box. |
| Minimum certified held-out size for the stored target gap | 1063 observations under the declared P79 settings. |
| Does rejection establish a theory of consciousness? | No. It rejects only the declared statistical model set covered by the certificate. |

### Audit trail

[Equation provenance](p88_equation_provenance.md) · [Implementation](../src/consciousness_bridge/heldout_selected_parity_functional_certification.py) · [Regression tests](../tests/test_heldout_selected_parity_functional_certification.py) · [Frontier figure](figures/p88_heldout_selected_parity_functional_certification.svg) · [Reproducibility guide](reproducibility.md)

---

## 1. Selection-validity gap after P87

Let discovery data be `D`, and let an arbitrary discovery-only rule return a pair

\[
(B_D,Q_D),
\]

where `B_D` is a P75 parameter box and

\[
Q_D(p)=E_p[g_D(X)]
\]

is one P87 functional. The selection rule may search the complete P87 family, tune the tested parameter region, use a P87 witness routine, or apply another discovery-only criterion. The subsequent validation sample

\[
V=(X_1,\ldots,X_n)
\]

must be IID from the target population law `p` and independent of `D`.

Conditional on `D`, both `B_D` and `Q_D` are fixed. Reusing the validation observations to alter either the box or the functional after seeing the validation result would invalidate this proof unless an additional selection correction were supplied.

---

## 2. Exact frozen-box interval and score range

For the discovery-frozen pair `(B,Q)`, P87 provides an exact rational P75 box interval

\[
I_B(Q)=[L_B(Q),U_B(Q)]
\]

by multi-affine endpoint enumeration.

On each of the sixteen binary outcomes define the exact score

\[
g_Q(x)=\sum_{i=1}^4 c_i\mathbf 1_{H_{J_i}}(x).
\]

Let

\[
g_{\min}=\min_x g_Q(x),\qquad
g_{\max}=\max_x g_Q(x),\qquad
R_Q=g_{\max}-g_{\min}.
\]

The validation empirical functional is

\[
\widehat Q_V=\frac1n\sum_{k=1}^n g_Q(X_k).
\]

---

## 3. Conditional Hoeffding theorem after discovery selection

Conditional on `D`, the selected pair `(B_D,Q_D)` is fixed. The normalized score

\[
Y_k=\frac{g_D(X_k)-g_{\min,D}}{R_D}
\]

lies in `[0,1]`. Hoeffding therefore gives

\[
\Pr\left(
|\widehat Q_V-Q_D(p)|>R_D\sqrt{\frac{\log(2/\alpha)}{2n}}
\;\middle|\;D
\right)
\le \alpha.
\]

The bound holds for every discovery realization. Averaging over `D` therefore gives the same unconditional coverage. There is no union bound over the 39,600 candidate functionals because only one discovery-frozen functional is evaluated on validation data. The box may also have been selected on discovery data because its interval is frozen before validation is inspected.

P88 reuses P79 with `alphabet_size=1` to construct a rational upper bound

\[
\overline r_{n,\alpha}
\ge
\sqrt{\frac{\log(2/\alpha)}{2n}}.
\]

Thus

\[
\overline\varepsilon_Q
=R_Q\overline r_{n,\alpha}
\]

is a certified rational upper bound on the validation functional error.

---

## 4. Finite-sample frozen-box rejection and population-distance lower bound

Define

\[
\widehat\Delta_Q
=\operatorname{dist}(\widehat Q_V,I_B(Q)).
\]

On the held-out Hoeffding event,

\[
\operatorname{dist}(Q(p),I_B(Q))
\ge
\left[\widehat\Delta_Q-\overline\varepsilon_Q\right]_+.
\]

Therefore the strict finite-sample rejection condition is

\[
\boxed{\widehat\Delta_Q>\overline\varepsilon_Q.}
\]

Under the null that `p` is generated by a P75 parameter inside the discovery-frozen box `B`, the population functional lies in `I_B(Q)`. The rejection rule therefore has type-I error at most `alpha` under the stated independence assumption.

P87 also gives

\[
D(Q)=\min_a\sum_x|g_Q(x)-a|.
\]

For every P75 law `q` generated inside `B`,

\[
|Q(p)-Q(q)|\le D(Q)\|p-q\|_\infty.
\]

Thus with probability at least `1-alpha`,

\[
\boxed{
\inf_{q\in\mathcal M_B}\|p-q\|_\infty
\ge
\frac{[\widehat\Delta_Q-\overline\varepsilon_Q]_+}{D(Q)}.
}
\]

This is a lower confidence bound on distance to the P75 law set generated by `B`; no statement about parameters outside `B` follows without a separate covering argument.

---

## 5. Exact rational regression witness

Use the P87 witness functional

\[
Q=P(H_{\{0,2\}})-P(H_{\{1,3\}})-2P(H_{\{1,2,3\}})+2P(H_{\{0,1,2,3\}}).
\]

Its sixteen-cell score range is

\[
g_{\min}=-3,\qquad g_{\max}=2,\qquad R_Q=5.
\]

Use the stored strict P87 box and an independent validation sample of size

\[
n=2400
\]

whose exact empirical proportions equal the stored P87 rational witness law, with

\[
\alpha=1/20.
\]

With 12 P79 logarithm-series terms and a 24-bit dyadic square-root ceiling,

\[
\overline r=\frac{465101}{16777216},
\qquad
\overline\varepsilon_Q=\frac{2325505}{16777216}.
\]

The empirical interval gap is

\[
\widehat\Delta_Q=\frac5{24},
\]

so

\[
\widehat\Delta_Q-\overline\varepsilon_Q
=\frac{3509245}{50331648}>0.
\]

With `D(Q)=20`, P88 certifies

\[
\boxed{
\inf_{q\in\mathcal M_B}\|p-q\|_\infty
\ge
\frac{701849}{201326592}
>0
}
\]

at confidence at least 95%, under the frozen-pair held-out assumption.

For comparison, the P79 simultaneous sixteen-cell radius on the same validation sample is

\[
\frac{615553}{16777216},
\]

while the available P87 empirical model-distance lower bound for this box is

\[
\frac1{96}.
\]

Thus that particular P87-lower-bound-to-P77-global-radius handoff is inconclusive because `1/96` is below the sixteen-cell radius, whereas the discovery-frozen scalar functional certificate rejects the tested box. This is a strict operational advantage of the held-out scalar route; it is not a claim that the exact P77 full-model test itself can never reject this empirical law.

---

## 6. What P88 does and does not solve

P88 solves a real post-P87 statistical problem: a box/functional test chosen from discovery data can be validated on independent held-out data without paying a family-size union bound over the functional search.

It does **not** make arbitrary reuse of the same data valid. If discovery and validation overlap, or if the box/function is revised after validation is inspected, the proof does not apply. The software cannot certify experimental independence; that is a data-provenance obligation. A rejection applies to the law set inside the frozen box, not automatically to the entire P75 family. Non-rejection remains inconclusive, and no statistical latent variable is identified with consciousness.

Implementation: [`src/consciousness_bridge/heldout_selected_parity_functional_certification.py`](../src/consciousness_bridge/heldout_selected_parity_functional_certification.py)

Regression tests: [`tests/test_heldout_selected_parity_functional_certification.py`](../tests/test_heldout_selected_parity_functional_certification.py)

Equation provenance: [`docs/p88_equation_provenance.md`](p88_equation_provenance.md)

---

## 7. Exact held-out sample-size design threshold

For a discovery-frozen functional with exact score width $R$ and a specified
functional interval gap $\Delta>0$, the ideal Hoeffding rejection inequality is

\[
R\sqrt{\frac{\log(2/\alpha)}{2n}}<\Delta.
\]

Equivalently,

\[
\boxed{
n>\frac{R^2\log(2/\alpha)}{2\Delta^2}.
}
\]

P88 does not use a floating-point approximation to decide the implemented
threshold. The function `p88_minimum_validation_sample_size_for_gap_exact`
searches for the smallest integer $n$ for which the P79-certified rational
upper radius satisfies the strict inequality.

For the stored witness, $R=5$, $\Delta=5/24$, and $\alpha=1/20$, so the ideal
expression is $n>288\log 40$. With the declared P79 settings (12 logarithm
series terms and a 24-bit dyadic square-root ceiling), the exact certified
threshold is

\[
\boxed{n_{\min}=1063.}
\]

At $n=1062$ the certified unit-range radius is $349591/8388608$ and the strict
rejection inequality still fails. At $n=1063$ the unit-range radius is
$698853/16777216$ and the strict inequality holds. This is a deterministic
design threshold for a *specified* gap; it is not a prospective guarantee that
a random validation sample will realize that gap.

---

## 8. Proposition 88

Let discovery data $D$ determine a P75 parameter box $B_D$ and one P87
functional $Q_D$. Let an IID validation sample of size $n$ from population law
$p$ be independent of $D$. Conditional on $D$, define the exact P75 interval
$I_{B_D}(Q_D)$, exact score width $R_D$, empirical validation value
$\widehat Q_D$, exact centered transfer norm $D(Q_D)$, and a P79-certified
rational upper bound $\bar r_{n,\alpha}$ on
$\sqrt{\log(2/\alpha)/(2n)}$. Then with probability at least $1-\alpha$,

\[
\boxed{
\inf_{q\in\mathcal M_{B_D}}\|p-q\|_\infty
\ge
\frac{
[\operatorname{dist}(\widehat Q_D,I_{B_D}(Q_D))
-R_D\bar r_{n,\alpha}]_+
}{D(Q_D)}.
}
\]

Consequently, under the null $p\in\mathcal M_{B_D}$, the rejection rule

\[
\operatorname{dist}(\widehat Q_D,I_{B_D}(Q_D))
>R_D\bar r_{n,\alpha}
\]

has conditional type-I error at most $\alpha$, and the same coverage holds
unconditionally after averaging over discovery data. No union bound over the
39,600-function discovery family is required because exactly one box/functional
pair is frozen before validation.

The theorem is box-specific. It becomes a statement about the full admissible
P75 family only when the frozen box covers that family or a separately certified
covering argument extends the result to every required box.

---

## 9. Scientific interpretation boundary

P88 is a finite-sample validation theorem for a declared statistical model set.
It does not establish that the P75 latent variable is consciousness; it does not
prove consciousness is nonphysical; it does not validate an alternative model
after rejection; and it does not close the physical-to-experiential bridge.
The software also cannot establish experimental independence or prove that the
tested box/function was genuinely frozen before validation was inspected.

---

## Continue reading

- [Previous result: P87 complete bounded primitive four-event functionals](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)
- [P88 equation provenance](p88_equation_provenance.md)
- [Research Traceability Index](research_traceability_index.md)
- [Theorem Roadmap](theorem_roadmap.md)
- [Reproducibility Guide](reproducibility.md)
