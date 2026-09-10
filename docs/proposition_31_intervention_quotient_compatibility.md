# Proposition 31: Intervention-quotient compatibility

## Status

**Proved operational quotient theorem for the declared intervention family.** P31 states when several fine intervention labels may be replaced by one coarse intervention label without making the coarse response law representative-dependent. It does not claim that distinct physical actuators are identical, simultaneous, synergistic, or interchangeable outside the declared response experiment.

## 1. Motivation

P30 assembles the P11 physical signature under one shared node quotient while deliberately retaining the intervention set \(\mathcal U\). The next unresolved scale operation is intervention quotienting itself.

Let

\[
b:\mathcal U_f\twoheadrightarrow\mathcal U_c
\]

be a declared surjective map from fine intervention labels to coarse intervention labels. The question is not whether the labels can be renamed. The question is whether the response law depends only on the coarse intervention label.

Assume the response laws being compared are already expressed on one common physical response space. If a node/state coarse map is part of the experiment, write these laws as

\[
\overline P^{u,\tau}=(C_a)_\#P^{u,\tau}.
\]

P31 then analyzes the intervention quotient \(b\) on this declared response family.

## 2. Exact descent criterion

A coarse response table \(Q^{c,\tau}\) descends through \(b\) exactly when

\[
\boxed{
\overline P^{u,\tau}=Q^{b(u),\tau}
\qquad
\forall u\in\mathcal U_f,\ \tau\in\mathcal T.
}
\]

The necessary and sufficient condition is

\[
\boxed{
b(u)=b(v)
\Longrightarrow
\overline P^{u,\tau}=\overline P^{v,\tau}
\quad\forall\tau\in\mathcal T.}
\]

### Proof

If the coarse response table exists, then two fine interventions in the same \(b\)-fiber both equal \(Q^{b(u),\tau}\), so their response laws are equal at every retained delay.

Conversely, suppose all response laws are constant on each \(b\)-fiber at every retained delay. For each coarse label \(c\), choose any representative \(u_c\in b^{-1}(c)\) and define

\[
Q^{c,\tau}=\overline P^{u_c,\tau}.
\]

Fiberwise equality makes this definition independent of representative. Therefore the descended response table is unique. \(\square\)

## 3. Quotient ambiguity defect

When exact descent fails, define the operational intervention-quotient ambiguity

\[
\boxed{
\eta_b
=
\sup_{\tau\in\mathcal T}
\sup_{u,v:\,b(u)=b(v)}
\left\|
\overline P^{u,\tau}-\overline P^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

Then

\[
\boxed{
\eta_b=0
\iff
\text{the response family descends exactly through }b.
}
\]

This quantity has a direct scientific interpretation. It measures how much physically observable response variation is hidden when distinct fine interventions are assigned the same coarse intervention label.

## 4. Representative-selection stability

Suppose exact descent does not hold and a coarse table is nevertheless constructed by choosing one representative \(s(c)\in b^{-1}(c)\) for each coarse intervention. Write

\[
Q_s^{c,\tau}=\overline P^{s(c),\tau}.
\]

For any two representative selections \(s\) and \(s'\),

\[
\boxed{
\sup_{c,\tau}
\left\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\right\|_{\mathrm{TV}}
\le\eta_b.
}
\]

This bound is immediate because \(s(c)\) and \(s'(c)\) belong to the same quotient fiber.

Thus \(\eta_b\) is not only a failure indicator. It is the worst-case representative dependence of a quotient response table.

## 5. Induced response-geometry uncertainty

For two coarse intervention labels \(c,d\), a representative selection \(s\) induces

\[
G_s(c,d,\tau)
=
\left\|Q_s^{c,\tau}-Q_s^{d,\tau}\right\|_{\mathrm{TV}}.
\]

For two selections \(s,s'\), the reverse triangle inequality gives

\[
\left|
G_s(c,d,\tau)-G_{s'}(c,d,\tau)
\right|
\le
\left\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\right\|_{\mathrm{TV}}
+
\left\|Q_s^{d,\tau}-Q_{s'}^{d,\tau}\right\|_{\mathrm{TV}}.
\]

Therefore

\[
\boxed{
\sup_{c,d,\tau}
|G_s-G_{s'}|
\le2\eta_b.
}
\]

This is the intervention-space analogue of a scale-ambiguity budget: if the quotient merges fine interventions whose response laws remain distinguishable, the resulting coarse response geometry is not unique.

## 6. Exact quotient geometry

If \(\eta_b=0\), then the descended response table \(Q\) is unique and so is its intervention-response geometry:

\[
\boxed{
G_c(c,d,\tau)
=
\|Q^{c,\tau}-Q^{d,\tau}\|_{\mathrm{TV}}.
}
\]

No representative selection remains in the definition.

This gives a mathematically meaningful coarse intervention geometry only after response-law descent has been established.

## 7. What P31 does not mean

The intervention quotient

\[
b:\mathcal U_f\twoheadrightarrow\mathcal U_c
\]

is a quotient of **declared operational intervention labels relative to a response experiment**. It is not by itself a statement that the underlying physical perturbations are the same mechanism.

In particular,

\[
\boxed{
\text{same coarse intervention label}
\neq
\text{same physical actuator}.
}
\]

Also,

\[
\boxed{
\text{intervention quotient}
\neq
\text{simultaneous intervention}.
}
\]

and

\[
\boxed{
\text{small }\eta_b
\neq
\text{proof of physical equivalence}.
}
\]

A small \(\eta_b\) only says that the declared response family is insensitive, up to that tolerance, to which fine intervention in the quotient fiber was used.

## 8. Relation to P28-P30

P28 answers a different question: whether an already-declared matched intervention pair has an unambiguous **source-node label** after node aggregation.

P31 asks whether multiple **intervention labels themselves** may be identified after the physical response space has been fixed.

These operations must not be conflated:

\[
\boxed{
\text{source-node aggregation}
\neq
\text{intervention-label quotienting}.
}
\]

P30 therefore remains correct in holding \(\mathcal U\) fixed. P31 supplies the missing theorem that would be needed before extending P30 to a changing intervention set.

## 9. Scientific boundary

P31 is a response-law quotient theorem. It does not establish consciousness, physical completeness, causal equivalence outside the declared experiment, or ontological identity between interventions.

The next unresolved scale operation is the delay/time quotient: when may several fine delays be represented by one coarse temporal label without making response structure dependent on the chosen fine time representative?

## 10. Reproducibility

Implementation: [`intervention_quotient_compatibility.py`](../src/consciousness_bridge/intervention_quotient_compatibility.py)

Tests: [`test_intervention_quotient_compatibility.py`](../tests/test_intervention_quotient_compatibility.py)
