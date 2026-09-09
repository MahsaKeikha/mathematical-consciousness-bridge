# Proposition 25 - Directed-Influence Scale Certification

## 1. Purpose

Proposition 18 certifies when deterministic coarse observation approximately preserves pairwise total-variation response geometry. Proposition 25 applies that reconstruction logic to a specific structured component of the Proposition 11 physical candidate: the directed perturbational influence tensor.

The question is physical and operational:

> If a directed intervention-response influence is present at a fine observational scale, when must it remain detectable after deterministic coarse observation of the target response?

The result does not identify directed influence with consciousness. It does not claim that the P11 candidate is bridge complete. It certifies one component of a declared physical causal description across scale.

---

## 2. Fine-scale directed influence

Fix a source block \(i\), target block \(j\), and response delay \(\tau\). Let

\[
\mathcal E_i
\]

be the declared family of matched intervention pairs that differ in the source intervention according to the P11 protocol semantics.

For intervention \(u\), let

\[
P_j^{u,\tau}
\]

be the fine-scale marginal response law of target \(j\) at delay \(\tau\).

The P11 directed influence is

\[
\boxed{
A_{i\to j}^{f}(\tau)
:=
\sup_{(u,v)\in\mathcal E_i}
\left\|P_j^{u,\tau}-P_j^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The same intervention-pair family \(\mathcal E_i\) is used at fine and coarse observational scales. Changing the intervention semantics is a different scientific operation and is not covered by P25.

---

## 3. Deterministic target coarse-graining

Let

\[
C_j:\mathcal Y_j^{f}\to\mathcal Y_j^{c}
\]

be a deterministic coarse observation map on the target response variable. Define the coarse intervention-conditioned law

\[
\overline P_j^{u,\tau}
:=
(C_j)_{\#}P_j^{u,\tau}.
\]

The coarse directed influence is

\[
\boxed{
A_{i\to j}^{c}(\tau)
:=
\sup_{(u,v)\in\mathcal E_i}
\left\|
\overline P_j^{u,\tau}-\overline P_j^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

---

## 4. Lemma - coarse observation cannot increase directed influence

For every intervention pair \((u,v)\), total variation contracts under deterministic pushforward:

\[
\left\|
(C_j)_{\#}P_j^{u,\tau}
-
(C_j)_{\#}P_j^{v,\tau}
\right\|_{\mathrm{TV}}
\le
\left\|P_j^{u,\tau}-P_j^{v,\tau}\right\|_{\mathrm{TV}}.
\]

Taking the supremum over the same pair family gives

\[
\boxed{
A_{i\to j}^{c}(\tau)
\le
A_{i\to j}^{f}(\tau).
}
\]

### Consequence

Deterministic coarse observation of the target cannot create a larger P11 directed-influence value when intervention semantics are held fixed.

In particular, for any threshold \(\theta\ge0\),

\[
A_{i\to j}^{f}(\tau)\le\theta
\Longrightarrow
A_{i\to j}^{c}(\tau)\le\theta.
\]

Thus a thresholded coarse edge cannot be a false positive relative to the corresponding fine-scale influence under the declared map and intervention family.

---

## 5. Approximate reconstruction

Contraction alone is one-sided. A fine-scale influence can disappear after an information-destroying coarse map. To quantify how much can be lost, introduce a fiber-consistent stochastic decoder

\[
R_j:\mathcal Y_j^{c}\rightsquigarrow\mathcal Y_j^{f}
\]

as in P18.

For each intervention-conditioned target law define

\[
\rho_u
:=
\left\|
P_j^{u,\tau}
-
(R_j)_{\#}(C_j)_{\#}P_j^{u,\tau}
\right\|_{\mathrm{TV}}.
\]

Over all interventions participating in \(\mathcal E_i\), define

\[
\boxed{
\rho_{i\to j}(\tau)
:=
\sup_{u\in\mathcal U(\mathcal E_i)}\rho_u.
}
\]

where \(\mathcal U(\mathcal E_i)\) is the set of interventions appearing in the matched-pair family.

---

## 6. Main theorem - directed-influence distortion bound

For each matched pair \((u,v)\), P18 gives

\[
0
\le
\left\|P_j^{u,\tau}-P_j^{v,\tau}\right\|_{\mathrm{TV}}
-
\left\|(C_j)_{\#}P_j^{u,\tau}-(C_j)_{\#}P_j^{v,\tau}\right\|_{\mathrm{TV}}
\le
\rho_u+\rho_v.
\]

Since

\[
\rho_u+\rho_v
\le
2\rho_{i\to j}(\tau),
\]

we have for every pair

\[
\left\|P_j^{u,\tau}-P_j^{v,\tau}\right\|_{\mathrm{TV}}
\le
\left\|(C_j)_{\#}P_j^{u,\tau}-(C_j)_{\#}P_j^{v,\tau}\right\|_{\mathrm{TV}}
+
2\rho_{i\to j}(\tau).
\]

Taking the supremum over \(\mathcal E_i\) yields

\[
A_{i\to j}^{f}(\tau)
\le
A_{i\to j}^{c}(\tau)
+
2\rho_{i\to j}(\tau).
\]

Combining this with contraction proves

\[
\boxed{
0
\le
A_{i\to j}^{f}(\tau)-A_{i\to j}^{c}(\tau)
\le
2\rho_{i\to j}(\tau).
}
\]

Equivalently,

\[
\boxed{
A_{i\to j}^{c}(\tau)
\ge
A_{i\to j}^{f}(\tau)-2\rho_{i\to j}(\tau).
}
\]

This is the P25 directed-influence scale certificate.

---

## 7. Exact-preservation corollary

If

\[
\rho_{i\to j}(\tau)=0,
\]

then

\[
\boxed{
A_{i\to j}^{c}(\tau)
=
A_{i\to j}^{f}(\tau).
}
\]

Thus global microscopic invertibility of \(C_j\) is unnecessary. Exact reconstruction is required only on the declared intervention-conditioned target-response family.

---

## 8. Thresholded edge-preservation theorem

Let \(\theta\in[0,1]\) be a declared directed-edge threshold.

If

\[
\boxed{
A_{i\to j}^{f}(\tau)
>
\theta+2\rho_{i\to j}(\tau),
}
\]

then

\[
A_{i\to j}^{c}(\tau)
\ge
A_{i\to j}^{f}(\tau)-2\rho_{i\to j}(\tau)
>
\theta,
\]

so

\[
\boxed{
A_{i\to j}^{c}(\tau)>\theta.
}
\]

Therefore a fine directed edge with more than \(2\rho\) of margin above threshold must survive the declared coarse observation.

Conversely,

\[
A_{i\to j}^{c}(\tau)>\theta
\Longrightarrow
A_{i\to j}^{f}(\tau)>\theta
\]

by contraction.

The only ambiguous regime is

\[
\boxed{
\theta
<
A_{i\to j}^{f}(\tau)
\le
\theta+2\rho_{i\to j}(\tau),
}
\]

where coarse observation may erase an edge that exists at the fine scale.

---

## 9. Tensor-level corollary

Suppose the construction is available for every declared source-target-delay triple \((i,j,\tau)\). Let

\[
\rho_{\max}
:=
\sup_{i,j,\tau}\rho_{i\to j}(\tau).
\]

Then componentwise

\[
0
\le
A_{ij}^{f}(\tau)-A_{ij}^{c}(\tau)
\le
2\rho_{\max},
\]

and therefore

\[
\boxed{
\|\mathcal A^{f}-\mathcal A^{c}\|_{\infty}
\le
2\rho_{\max}.
}
\]

This certifies the P11 directed-influence tensor in the sup norm when a common reconstruction envelope is available.

This corollary still assumes compatible target maps, matched intervention semantics, and a common index structure across scales. Genuine node fusion, source aggregation, or changing intervention channels requires an additional theorem.

---

## 10. Counterexample - why reconstruction control is necessary

Let the fine target be binary. Under interventions \(u\) and \(v\), suppose

\[
P^u=(0.9,0.1),
\qquad
P^v=(0.1,0.9).
\]

Then

\[
A^f=0.8.
\]

Now choose the constant coarse map that sends both fine outcomes to one coarse symbol. Both pushed-forward laws become identical, so

\[
A^c=0.
\]

With a balanced decoder \((0.5,0.5)\), each reconstruction error is \(0.4\). Hence

\[
2\rho=0.8,
\]

and P25 is tight:

\[
A^f-A^c
=0.8
=2\rho.
\]

The example shows why deterministic coarse-graining alone cannot preserve directed influence. Reconstruction quality is the missing quantitative condition.

---

## 11. What P25 establishes

P25 establishes, for a declared source-target-delay entry with fixed intervention semantics:

1. deterministic target coarse-graining cannot increase P11 directed influence;
2. the influence loss is at most twice the uniform P18 reconstruction defect;
3. exact family reconstruction gives exact directed-influence preservation;
4. thresholded edges with sufficient fine-scale margin must survive coarse observation;
5. a coarse threshold edge implies a corresponding fine threshold edge;
6. the componentwise theorem extends to a tensor sup-norm bound when a common reconstruction envelope exists.

---

## 12. What P25 does not establish

P25 does not prove that:

- directed influence is consciousness;
- the full P11 causal structure is preserved across scale;
- the partition-irreducibility component \(\mathcal K\) is scale stable;
- arbitrary node aggregation preserves source semantics;
- coarse interventions are automatically equivalent to fine interventions;
- a thresholded causal graph is ontologically fundamental;
- a physical descriptor is complete;
- an experiential bridge exists.

The next scale theorem must address the partition structure and/or genuine block aggregation rather than treating observation coarse-graining as physical fusion.

---

## 13. Executable audit path

Implementation:

`src/consciousness_bridge/directed_influence_scale_certification.py`

Regression tests:

`tests/test_directed_influence_scale_certification.py`

The executable certificate reports the fine and coarse influence, uniform reconstruction defect, additive distortion bound, guaranteed coarse influence, thresholded edge state, and whether the fine-scale margin is sufficient to certify edge preservation.

---

## 14. Interpretation boundary

The scientifically defensible conclusion of P25 is:

\[
\boxed{
\text{small response-family reconstruction defect}
\Longrightarrow
\text{small directed-influence distortion under target coarse observation}.
}
\]

It is not

\[
\text{scale-stable directed influence}
\Longrightarrow
\text{consciousness}.
\]

P25 strengthens the physical side of the bridge program by making one part of the P11 causal structure quantitatively testable across observational scale while keeping the experiential question open.
