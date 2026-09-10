# Proposition 35: Approximate directed-influence stability under operational quotienting

## Status

**Proved perturbation theorem for the P11 directed-influence branch.** P35 closes the first approximate branch left open by P34. It shows that once matched intervention-pair source semantics descend, nonzero intervention-delay quotient ambiguity perturbs a total-variation directed-influence value by at most twice the joint response-law ambiguity.

Combined with the P25/P30 node-state reconstruction bound, this gives an explicit full-scale directed-influence certificate.

P35 is a theorem about the declared intervention-response construction. It does not establish consciousness, causal completeness, or equivalence of distinct physical actuators.

---

## 1. Directed influence

For a matched intervention pair

\[
e=(u^+,u^-)
\]

and retained delay \(\tau\), define the response-level directed influence

\[
\boxed{
A(e,\tau)
=
\left\|
P^{u^+,\tau}-P^{u^-,\tau}
\right\|_{\mathrm{TV}}.
}
\]

After the P30 node/state transformation, write the corresponding response laws as

\[
\overline P^{u,\tau}=(C_V)_\#P^{u,\tau}.
\]

P35 studies what happens when intervention and delay labels are subsequently quotient-identified.

---

## 2. Semantic condition

A numerical bound is meaningful only if the fine matched pair has one unambiguous coarse meaning.

Let

\[
b:\mathcal U_f\twoheadrightarrow\mathcal U_c,
\qquad
a:\mathcal T_f\twoheadrightarrow\mathcal T_c.
\]

For each retained fine pair \(e=(u^+,u^-)\), require that

\[
\boxed{
\bar e=(b(u^+),b(u^-))
}
\]

is a declared coarse matched comparison with a unique descended source interpretation, in the sense required by P28 and P34-C7.

Without this condition, two numerically similar response pairs can still represent different physical source questions.

---

## 3. Joint response ambiguity

Let \(\eta_{a\times b}\) be the P33 product-fiber ambiguity after the common node/state map:

\[
\eta_{a\times b}
=
\sup_{\substack{b(u)=b(v)\\a(\tau)=a(\sigma)}}
\left\|
\overline P^{u,\tau}-\overline P^{v,\sigma}
\right\|_{\mathrm{TV}}.
\]

Choose any representatives for the two coarse cells corresponding to the positive and negative members of the matched comparison. Each selected response law can move by at most \(\eta_{a\times b}\) relative to another valid representative of the same cell.

---

## 4. Directed-influence representative stability

Let

\[
A_s
=
\|Q_s^+-Q_s^-\|_{\mathrm{TV}}
\]

and

\[
A_{s'}
=
\|Q_{s'}^+-Q_{s'}^-\|_{\mathrm{TV}}
\]

be directed-influence values computed from two admissible representative selections.

By the reverse triangle inequality for a metric,

\[
\left|
A_s-A_{s'}
\right|
\le
\|Q_s^+-Q_{s'}^+\|_{\mathrm{TV}}
+
\|Q_s^--Q_{s'}^-\|_{\mathrm{TV}}.
\]

Each term is at most \(\eta_{a\times b}\). Therefore

\[
\boxed{
|A_s-A_{s'}|
\le
2\eta_{a\times b}.
}
\]

This is the central P35 perturbation theorem.

Using P33,

\[
\boxed{
|A_s-A_{s'}|
\le
2(\eta_b+\eta_a).
}
\]

---

## 5. Full node/state/intervention/time bound

P25/P30 give the node/state reconstruction-controlled directed-influence bound

\[
D_A^{\mathrm{node}}
\le
2\rho_A^*.
\]

Operational representative uncertainty contributes at most

\[
2\eta_{a\times b}.
\]

By triangle inequality, the full scale distortion obeys

\[
\boxed{
D_A^{\mathrm{full}}
\le
2\rho_A^*
+2\eta_{a\times b}.
}
\]

Using separately audited P31/P32 budgets,

\[
\boxed{
D_A^{\mathrm{full}}
\le
2\rho_A^*
+2(\eta_b+\eta_a).
}
\]

This has the same algebraic form as the P34 response-geometry bound, but here it is now justified specifically for the directed-influence functional.

---

## 6. Threshold-edge preservation

Suppose an influence edge is declared present when

\[
A>\theta.
\]

Let

\[
\varepsilon_A
=
2\rho_A^*+2\eta_{a\times b}.
\]

If the fine or reference-scale influence value has margin

\[
\boxed{
|A-\theta|>\varepsilon_A,
}
\]

then the threshold classification cannot change under the declared complete scale transformation.

In particular,

\[
A>\theta+\varepsilon_A
\Longrightarrow
A_{\mathrm{coarse}}>\theta,
\]

and

\[
A<\theta-\varepsilon_A
\Longrightarrow
A_{\mathrm{coarse}}<\theta.
\]

Thus P35 gives a margin certificate for directed-edge survival.

---

## 7. Exact quotient corollary

When

\[
\eta_{a\times b}=0,
\]

P35 reduces to the P25/P30 scale bound

\[
\boxed{
D_A^{\mathrm{full}}\le2\rho_A^*.
}
\]

If in addition \(\rho_A^*=0\), the directed-influence value is exactly preserved on every semantically descendable matched pair.

---

## 8. Failure mode

A small numerical value of \(\eta_{a\times b}\) is insufficient when matched-pair semantics fail to descend.

Therefore

\[
\boxed{
\text{small }\eta_{a\times b}
+\text{source-semantic failure}
\not\Rightarrow
\text{directed-influence preservation}.
}
\]

This maintains the no-semantic-compensation principle of P30 and P34.

---

## 9. Relation to P34

P34 deliberately withheld an approximate full-P11 theorem because the geometry perturbation bound did not automatically establish stability of \(\mathcal A\) and \(\mathcal K\).

P35 now closes the \(\mathcal A\) branch:

\[
\boxed{
\varepsilon_A^{\mathrm{full}}
=
2\rho_A^*+2\eta_{a\times b}.
}
\]

The remaining missing branch is approximate partition-irredundancy/irreducibility stability under operational quotienting.

---

## 10. Scientific boundary

Directed influence here is a perturbational response statistic in the declared experimental family. P35 does not claim that total-variation influence is a complete causal ontology, nor that it is itself consciousness.

The theorem only proves how this declared physical statistic behaves under a controlled change of experimental scale.

---

## 11. Next theorem target

The next step is to propagate operational response ambiguity through the partition-product reference used by \(\mathcal K\). That requires a separate product-measure stability lemma rather than reusing the geometry bound by analogy.

Once that is proved, P34 can be upgraded to a quantitative approximate bound for the complete P11 vector.

---

## 12. Reproducibility

Implementation: [`directed_influence_operational_quotient.py`](../src/consciousness_bridge/directed_influence_operational_quotient.py)

Tests: [`test_directed_influence_operational_quotient.py`](../tests/test_directed_influence_operational_quotient.py)
