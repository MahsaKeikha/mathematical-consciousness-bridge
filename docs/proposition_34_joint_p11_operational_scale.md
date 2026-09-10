# Proposition 34: Joint P11 operational-scale compatibility

## Status

**Proved exact assembly theorem with an approximate response-geometry corollary.** P34 combines the node/state scale theorem of P30 with the intervention-delay quotient theorem of P33. It identifies the additional semantic conditions required before the full P11 signature may be transported to a representation in which nodes, states, intervention labels, and delay labels all change simultaneously.

The theorem deliberately separates an exact full-signature statement from an approximate geometry-only statement. P33 controls response-law ambiguity in total variation. That control transfers directly to response geometry, but it does not by itself certify the same perturbation bound for every derived directed-influence or partition-irredundancy functional unless their own semantics descend through the operational quotient.

P34 therefore does not identify consciousness, prove physical completeness, or claim that coarse physical descriptions are fundamental.

---

## 1. Fine P11 structure

Write the declared fine physical candidate as

\[
\mathfrak C_f
=
(V_f,\mathcal U_f,\mathcal T_f,\mathcal G_f,\mathcal A_f,\mathcal K_f).
\]

Let

\[
q_V:V_f\twoheadrightarrow V_c
\]

be the node quotient, with compatible physical state map \(C_V\), and let

\[
b:\mathcal U_f\twoheadrightarrow\mathcal U_c,
\qquad
 a:\mathcal T_f\twoheadrightarrow\mathcal T_c
\]

be the intervention and delay quotients.

The complete operational scale declaration is therefore

\[
\boxed{
\Sigma
=
(q_V,C_V,b,a,R)
}
\]

where \(R\) is the declared reconstruction family used in the P18/P25-P30 scale certificates.

---

## 2. Shared compatibility conditions

P34 requires the P30 conditions and adds three operational conditions.

### C1-C5. P30 node/state conditions

The partition saturation, source-pair compatibility, common response grid, common state map, and common reconstruction declaration of P30 all hold on the fine experiment grid.

### C6. Joint response-law descent

The state-coarsened response laws descend through the product intervention-delay quotient:

\[
\boxed{
 b(u)=b(v),\ a(\tau)=a(\sigma)
\Longrightarrow
(C_V)_\#P^{u,\tau}
=
(C_V)_\#P^{v,\sigma}.
}
\]

Equivalently, the P33 joint ambiguity is zero:

\[
\boxed{
\eta_{a\times b}=0.
}
\]

### C7. Directed-influence semantic descent

Every fine matched intervention comparison retained by \(\mathcal A_f\) maps to a unique declared coarse intervention comparison, and all fine representatives of that coarse comparison have the same descended aggregate-source semantics.

This is stronger than response-law equality alone. It prevents one coarse intervention pair from mixing fine perturbations that have incompatible source interpretations.

### C8. Partition-domain descent

Every partition statistic retained by \(\mathcal K_f\) is evaluated on a response law and factorized reference whose node partition descends under P27 and whose operational intervention-delay label is well defined under C6.

Thus the partition comparison is not allowed to combine representative-dependent experiment labels.

---

## 3. Exact full-signature theorem

Under C1-C8, define the fully coarse signature

\[
\mathfrak C_c
=
(V_c,\mathcal U_c,\mathcal T_c,\mathcal G_c,\mathcal A_c,\mathcal K_c).
\]

Because C6 makes each coarse intervention-delay response law unique, the geometry branch is representative independent. Because C7 makes the matched-pair semantics unique, the directed-influence branch is also well defined. Because C8 combines operational descent with P27 partition descent, the partition branch is well defined.

Let the P30 component reconstruction budgets be

\[
D_G\le 2\rho_G^*,
\qquad
D_A\le 2\rho_A^*,
\qquad
D_K\le \rho_P^*+\rho_\Pi^*.
\]

Then the same bounds hold after exact operational quotienting:

\[
\boxed{
\|\mathbf D_{P11}(\Sigma)\|_\infty
\le
\max\left\{
2\rho_G^*,
2\rho_A^*,
\rho_P^*+\rho_\Pi^*
\right\}.
}
\]

### Proof

P30 already proves the three component bounds after node/state coarse observation while holding \(\mathcal U\) and \(\mathcal T\) fixed. C6 then identifies response laws only inside product fibers on which the state-coarsened response law is exactly constant. Therefore choosing the descended coarse operational label introduces no additional response-law error. C7 guarantees that the directed-influence entries being identified have one common coarse source/intervention meaning. C8 guarantees that partition statistics are evaluated only on descendable node partitions and unique descended operational response laws. Hence operational quotienting adds no numerical distortion to the P30 component bounds. Taking their maximum proves the result. \(\square\)

---

## 4. Exact preservation corollary

If the relevant reconstruction defects also vanish,

\[
\rho_G^*=\rho_A^*=\rho_P^*=\rho_\Pi^*=0,
\]

then under C1-C8

\[
\boxed{
\mathbf D_{P11}(\Sigma)=0.
}
\]

This is exact preservation of the declared P11 signature under the complete node/state/intervention/time quotient.

It is still an operational equivalence theorem, not a claim of ontological identity.

---

## 5. Approximate joint quotient: geometry branch

Now allow

\[
\eta_{a\times b}>0.
\]

P33 gives representative response-law ambiguity at most \(\eta_{a\times b}\). Pairwise total-variation geometry therefore varies by at most

\[
2\eta_{a\times b}.
\]

Combining this with the P29/P30 node-state geometry bound gives

\[
\boxed{
D_G^{\mathrm{full}}
\le
2\rho_G^*
+
2\eta_{a\times b}.
}
\]

Using P33,

\[
\eta_{a\times b}\le\eta_b+\eta_a,
\]

so a separately audited sufficient bound is

\[
\boxed{
D_G^{\mathrm{full}}
\le
2\rho_G^*
+2(\eta_b+\eta_a).
}
\]

This is a certified additive budget separating state/node reconstruction loss from intervention/time representative ambiguity.

---

## 6. Why the same approximate formula is not asserted for A and K

For \(\mathcal A\), a numerical response perturbation bound is insufficient if the operational quotient changes which perturbation comparison counts as the same directed source relation.

For \(\mathcal K\), a response-law perturbation also changes the corresponding partition-product reference. A bound on the response law alone does not automatically equal a bound on the irreducibility statistic.

Therefore P34 does **not** assert

\[
D_A^{\mathrm{full}}\le 2\rho_A^*+2\eta_{a\times b}
\]

or

\[
D_K^{\mathrm{full}}\le \rho_P^*+\rho_\Pi^*+2\eta_{a\times b}
\]

without additional propositions proving the required semantic and functional stability.

This is a scientific boundary, not a missing algebraic convenience.

---

## 7. No-semantic-compensation principle

P30 established that small numerical distortion cannot compensate for failed node-level semantics. P34 extends the principle to the complete operational quotient:

\[
\boxed{
\text{small numerical ambiguity}
\not\Rightarrow
\text{valid P11 scale transport}
}
\]

when C7 or C8 fails.

A response table can be nearly invariant while its coarse intervention meaning is ambiguous. Likewise, a partition statistic can be numerically stable while the partition itself fails to descend.

---

## 8. Scale decomposition

P34 exposes four logically distinct sources of scale change:

\[
\boxed{
\text{node semantics}
\oplus
\text{state reconstruction}
\oplus
\text{intervention semantics}
\oplus
\text{temporal semantics}.
}
\]

They must be audited separately before being assembled.

For the response-geometry branch, their quantitative contribution is explicit:

\[
\boxed{
\varepsilon_G^{\mathrm{full}}
=
2\rho_G^*+2\eta_{a\times b}
\le
2\rho_G^*+2(\eta_b+\eta_a).
}
\]

---

## 9. Scientific significance

P27-P30 showed how the structured P11 candidate behaves when the physical node/state description changes. P31-P33 established intervention and temporal quotient consistency. P34 now provides the first theorem in the repository in which all four scale operations are declared in one object.

The result closes an important methodological loophole. A future claim that a physical signature persists across scale must no longer switch node maps, state maps, intervention equivalences, or time bins implicitly. All of them belong to one declared scale transformation \(\Sigma\).

---

## 10. What P34 does not establish

P34 does not prove that P11 is consciousness. It does not prove that P11 is a complete physical descriptor. It does not prove that quantum theory is incomplete. It does not establish an experiential variable outside spacetime.

What it does establish is narrower and necessary: the conditions under which the candidate physical signature itself remains mathematically well defined when the complete experimental scale changes.

---

## 11. Next theorem targets

Two mathematically justified extensions now become natural.

1. **Approximate directed-influence quotient stability.** Derive the exact Lipschitz or margin conditions under which nonzero \(\eta_{a\times b}\) preserves directed-influence values and threshold edges.
2. **Approximate partition-irredundancy quotient stability.** Propagate response-law quotient ambiguity through the partition-product operator and obtain a certified bound for \(\mathcal K\).

Only after those two branches are closed should an approximate full-P11 operational-scale bound be claimed.

The deeper physical-to-experiential program remains separate: test whether an independently defined experiential target factors through increasingly complete physical descriptors, including an operationally complete quantum description.

---

## 12. Reproducibility

Implementation: [`joint_p11_operational_scale.py`](../src/consciousness_bridge/joint_p11_operational_scale.py)

Tests: [`test_joint_p11_operational_scale.py`](../tests/test_joint_p11_operational_scale.py)
