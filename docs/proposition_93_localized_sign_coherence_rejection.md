# Proposition 93: Localized Finite-Sample Sign-Coherence Rejection

## Purpose

P92 proves the exact population result

\[
 d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\frac1{24}
\]

for the established empirical witness and the complete mixed-prevalence P75 family. Its lower certificate comes from a nonlinear sign-coherence invariant shared by three selected conditional two-by-two determinants.

P93 asks the next statistical question:

> When can finite IID data certify that the unknown population law itself violates that P92 sign-coherence invariant?

The answer does not require a simultaneous confidence box for all sixteen observable cells. The three P92 minors involve only **seven distinct cell probabilities**. P93 therefore builds one simultaneous seven-cell confidence event and propagates it directly through the exact determinant sign-stability radii.

The resulting finite-sample rule is:

\[
\boxed{
\widehat D_1\widehat D_2\widehat D_3<0
\quad\text{and}\quad
\overline\varepsilon_{n,7}(\alpha)
<
\min_i \widehat r_i
\quad\Longrightarrow\quad
P\notin\mathcal M_{75}
}
\]

with confidence at least \(1-\alpha\), where \(\overline\varepsilon_{n,7}\) is a P79-certified rational upper bound on the seven-cell Hoeffding radius and \(\widehat r_i\) are the empirical determinant sign-stability radii.

For the established P92 profile, the smallest exact radius is \(1/24\). At \(\alpha=0.05\), the exact mathematical seven-cell threshold crosses between \(n=1622\) and \(n=1623\). Because the original empirical profile has denominator 24, the first exact integer replication that can realize the same proportions and clear the P93 certificate is

\[
\boxed{n=1632=68\times24.}
\]

---

## P93A. The seven cells used by P92

Condition on the observable event

\[
X_1=1
\]

and write

\[
A=X_2,\qquad B=X_3,\qquad C=X_4.
\]

P92 uses the three matrices

\[
M_{AB\mid C=1},
\qquad
M_{AC\mid B=0},
\qquad
M_{BC\mid A=0}.
\]

Across those three matrices, only seven of the eight \(X_1=1\) cells appear. The one unused cell is \((A,B,C)=(1,1,0)\).

Let \(\mathcal J\) denote those seven selected observable cells.

For each \(x\in\mathcal J\), the empirical frequency \(\widehat P(x)\) is the mean of IID Bernoulli indicators. Therefore

\[
\Pr\left(
|\widehat P(x)-P(x)|>\varepsilon
\right)
\le
2e^{-2n\varepsilon^2}.
\]

A union bound over only the seven selected cells gives

\[
\boxed{
\varepsilon_{n,7}(\alpha)
=
\sqrt{\frac{\log(14/\alpha)}{2n}}
}
\]

and

\[
\boxed{
\Pr\left(
\max_{x\in\mathcal J}
|\widehat P(x)-P(x)|
\le
\varepsilon_{n,7}(\alpha)
\right)
\ge
1-\alpha.
}
\]

The seven selected cells do not need to form a normalized probability law. The argument only uses seven Bernoulli cell indicators and a simultaneous union bound.

---

## P93B. Empirical determinant sign stability

For a nonnegative two-by-two matrix

\[
M=
\begin{pmatrix}
a&b\\c&d
\end{pmatrix}
\]

with nonzero determinant, P92 proves the exact entrywise sign-stability radius

\[
\boxed{
r(M)=\frac{|ad-bc|}{a+b+c+d}
}
\]

when the product supporting the observed sign stays away from the zero clipping boundary.

Apply this separately to the three empirical P92 minors. Write

\[
\widehat D_i=\det\widehat M_i
\]

and

\[
\widehat r_i=r(\widehat M_i).
\]

If

\[
\varepsilon<\min_i\widehat r_i,
\]

then every nonnegative population matrix whose four entries differ from the empirical entries by at most \(\varepsilon\) has the same determinant sign as the corresponding empirical matrix.

On the P93A simultaneous seven-cell event, this statement holds for all three population minors at once.

---

## P93C. Finite-sample sign-coherence rejection theorem

P92 proves that every P75 law satisfies

\[
D_1D_2D_3\ge0.
\]

Suppose the observed empirical law satisfies

\[
\widehat D_1\widehat D_2\widehat D_3<0
\]

and all three empirical sign-stability radii are valid and positive.

If

\[
\boxed{
\varepsilon_{n,7}(\alpha)
<
\min_i\widehat r_i,
}
\]

then on the P93A confidence event every population determinant has the same sign as its empirical counterpart. Hence

\[
D_1D_2D_3<0,
\]

contradicting the universal P75 sign-coherence constraint.

Therefore

\[
\boxed{
\widehat D_1\widehat D_2\widehat D_3<0
\quad\text{and}\quad
\varepsilon_{n,7}(\alpha)<\min_i\widehat r_i
\Longrightarrow
P\notin\mathcal M_{75}
}
\]

with confidence at least \(1-\alpha\).

This is a one-sided rejection theorem. If the inequality does not clear, the conclusion is only that P93 does not reject at the requested confidence level.

---

## P93D. Exact-rational sampling-radius handoff

The mathematical radius \(\varepsilon_{n,7}(\alpha)\) contains a logarithm and square root. P93 does not compare an ordinary floating approximation against an exact determinant radius.

Instead it reuses P79. For rational \(\alpha\), P79 returns exact rational numbers

\[
\underline\varepsilon_{n,7,\alpha}
\le
\varepsilon_{n,7}(\alpha)
\le
\overline\varepsilon_{n,7,\alpha}.
\]

The executable P93 rejection gate uses only the safe direction

\[
\boxed{
\overline\varepsilon_{n,7,\alpha}
<
\min_i\widehat r_i.
}
\]

Thus both sides of the final comparison are direction-certified.

---

## P93E. Established witness profile

For the established empirical profile, P92 gives

\[
\widehat D_1=-\frac1{48},
\qquad
\widehat D_2=\frac1{64},
\qquad
\widehat D_3=\frac5{192},
\]

with

\[
\boxed{
\widehat r_1=\frac1{24},
\qquad
\widehat r_2=\frac3{56},
\qquad
\widehat r_3=\frac5{72}.
}
\]

Hence the limiting observed sign-stability radius is exactly

\[
\boxed{\widehat r_{\min}=\frac1{24}.}
\]

The P93 condition becomes

\[
\sqrt{\frac{\log(14/\alpha)}{2n}}
<
\frac1{24}.
\]

Squaring gives

\[
\boxed{
n>288\log(14/\alpha).}
\]

At

\[
\alpha=\frac1{20},
\]

this is

\[
n>288\log 280.
\]

P79 exact-rational envelopes certify that

\[
\varepsilon_{1622,7}(0.05)>\frac1{24}
\]

while

\[
\varepsilon_{1623,7}(0.05)<\frac1{24}.
\]

Therefore the first integer sample size satisfying the exact mathematical radius inequality is

\[
\boxed{n=1623.}
\]

This does not mean the original 24-count proportions can literally occur at sample size 1623. Exact replication of that profile requires \(n\) to be divisible by 24. The first such replication above the threshold is

\[
\boxed{n=1632=68\times24.}
\]

The previous exact replication is

\[
n=1608=67\times24,
\]

which does not clear the P93 radius.

---

## P93F. Relation to the generic P77 design bound

P77 already proves a generic fixed-population-margin theorem. If

\[
d_\infty(P,\mathcal M)\ge\tau,
\]

then a sufficient condition for guaranteed rejection on the full sixteen-cell confidence event is

\[
\varepsilon_{n,16}(\alpha)<\frac\tau2.
\]

Substituting the P92 exact population margin

\[
\tau=\frac1{24}
\]

gives the generic P77 sufficient condition

\[
\varepsilon_{n,16}(\alpha)<\frac1{48}.
\]

At \(\alpha=0.05\), P79 exact-rational envelopes place that crossing between

\[
n=7443
\]

and

\[
\boxed{n=7444.}
\]

P93's 1623 threshold and P77's 7444 threshold are **not the same type of guarantee**.

- P77 is a generic pre-specified fixed-population-margin guarantee using the complete sixteen-cell model distance.
- P93 is a localized observed-data rejection certificate that exploits the specific P92 nonlinear sign witness and only the seven cells entering that witness.

The comparison shows why the P92 structure matters statistically. It does not claim that P93 is a minimax-optimal testing procedure.

---

## What P93 establishes

P93 establishes that:

1. the P92 nonlinear witness needs simultaneous control of only seven observable cells;
2. those seven cells admit a familywise Hoeffding radius \(\varepsilon_{n,7}(\alpha)\);
3. a negative empirical three-minor sign product remains a valid population rejection witness whenever the certified sampling radius is smaller than every empirical determinant sign-stability radius;
4. the established P92 profile has limiting radius exactly \(1/24\);
5. at 95% confidence, the exact mathematical radius crossing occurs between 1622 and 1623 samples;
6. the first exact replication of the original 24-count profile that clears the localized certificate is 1632 samples; and
7. the entire comparison can be performed with exact rational one-sided numerical certification through P79.

---

## What P93 does not establish

P93 does not claim that 1623 samples are universally sufficient for every alternative to P75. The threshold is tied to the established observed sign geometry.

P93 also does not claim minimax optimality, model acceptance under non-rejection, semantic validity of the latent state, nonphysicality of consciousness, or a completed physical-to-experiential bridge.

Non-rejection remains inconclusive. The physical-to-experiential bridge remains open.

---

## Reproducibility record

- Implementation: `src/consciousness_bridge/localized_sign_coherence_rejection.py`
- Exact tests: `tests/test_localized_sign_coherence_rejection.py`
- Equation provenance: `docs/p93_equation_provenance.md`
- Population invariant: [P92 exact global mixed-prevalence distance](proposition_92_exact_global_mixed_prevalence_distance.md)
- Generic full-law finite-sample theorem: [P77](proposition_77_full_law_model_set_separation.md)
- Exact sampling-radius envelope: [P79](proposition_79_certified_sampling_radius.md)
