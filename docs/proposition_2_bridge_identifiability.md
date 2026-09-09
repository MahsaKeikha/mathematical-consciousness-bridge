# Proposition 2: experiment-class bridge identifiability

## Physical question

Proposition 1 established that a consciousness bridge must be invariant under physically irrelevant changes of representation.

A deeper scientific problem remains. Two bridge theories may assign different experiential structures to the same physical realization while making exactly the same predictions for every measurement and intervention available to an experimenter. If so, the bridge choice is not empirically identifiable within that experiment class.

The question is therefore:

> Given two complete consciousness bridge theories and a declared family of physical experiments, when can observations actually distinguish them?

Proposition 2 gives an exact answer using total-variation distance and binary statistical decision theory.

---

# 1. Physical and statistical setup

Let

\[
\mathcal Q_P=\mathcal P/{\sim_P}
\]

be the physical quotient supplied by Proposition 1, and fix

\[
q\in\mathcal Q_P.
\]

Let \(\Pi\) be a declared class of admissible experimental protocols. A protocol may specify preparation, intervention, timing, controls, measurement channels, report variables, physiological variables, and a sampling rule.

For each

\[
\pi\in\Pi,
\]

let the observable outcome lie in a measurable space

\[
(\mathcal Y_\pi,\mathcal F_\pi).
\]

Consider two complete bridge theories

\[
\mathfrak T_1,
\qquad
\mathfrak T_2.
\]

A bridge assignment alone need not determine observable probabilities. For empirical comparison, each complete theory must specify a measurement interface that induces an observable law. Write

\[
\boxed{
P_i^{\pi,q}
}
\]

for the probability law predicted by theory \(i\in\{1,2\}\) under protocol \(\pi\) at physical input \(q\).

---

# 2. Experiment-class discriminability

For probability measures \(P\) and \(Q\) on the same measurable space, define total-variation distance by

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}
=
\sup_{A\in\mathcal F}|P(A)-Q(A)|.
}
\]

When densities \(p\) and \(q\) exist with respect to a common dominating measure \(\mu\),

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}
=
\frac12\int |p(y)-q(y)|\,d\mu(y).
}
\]

Define the experiment-class discriminability

\[
\boxed{
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)
=
\sup_{\pi\in\Pi}
\left\|
P_1^{\pi,q}-P_2^{\pi,q}
\right\|_{\mathrm{TV}}.
}
\]

Thus

\[
0\le\Delta_\Pi\le1.
\]

The pair is **empirically identifiable relative to \(\Pi\) at \(q\)** when

\[
\Delta_\Pi>0,
\]

and **empirically non-identifiable relative to \(\Pi\) at \(q\)** when

\[
\Delta_\Pi=0.
\]

This definition is deliberately experiment-class relative. Passive observation may be insufficient even when a richer intervention class is discriminating.

---

# 3. Proposition

## Proposition 2

Fix \(q\in\mathcal Q_P\), an admissible experiment class \(\Pi\), and two complete bridge theories \(\mathfrak T_1,\mathfrak T_2\). Let

\[
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
\]

Then the following statements hold.

### A. Exact non-identifiability criterion

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\text{for every }\pi\in\Pi.
}
\]

### B. Optimal one-shot discrimination

For a fixed protocol \(\pi\), suppose the two theories have equal prior probability \(1/2\). Among all measurable binary decision rules based on one outcome, the minimum achievable probability of error is

\[
\boxed{
R_\pi^*
=
\frac12
\left(
1-
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}
\right).
}
\]

Consequently, optimizing over the admissible experiment class gives

\[
\boxed{
\inf_{\pi\in\Pi}R_\pi^*
=
\frac12(1-\Delta_\Pi).
}
\]

Thus \(\Delta_\Pi=0\) means no admissible one-shot experiment can perform better than chance, while \(\Delta_\Pi>0\) means at least one admissible protocol has nonzero statistical power for distinguishing the theories.

### C. Repeated-experiment consistency under independent repeatability

Assume there exists \(\pi\in\Pi\) with

\[
\delta
=
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}>0,
\]

and that the protocol can be repeated independently under the same physical preparation.

For every \(0<\eta<\delta\), there exists an event \(A\in\mathcal F_\pi\) such that

\[
|P_1^{\pi,q}(A)-P_2^{\pi,q}(A)|>\eta.
\]

Using the empirical frequency of \(A\) over \(n\) independent repetitions and thresholding halfway between the two event probabilities yields a test whose error under either theory is bounded by

\[
\boxed{
\exp\!\left(-\frac{n\eta^2}{2}\right).
}
\]

Hence a positive experiment-class discriminability can be amplified to arbitrarily reliable discrimination when an independently repeatable discriminating protocol exists.

---

# 4. Proof

## 4.1 Part A

Every total-variation distance is nonnegative. Therefore \(\Delta_\Pi=0\) if and only if

\[
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}=0
\]

for every \(\pi\in\Pi\). Total-variation distance is zero if and only if the two probability measures are equal. This proves Part A.

## 4.2 Part B

For a measurable decision region \(A\), decide \(\mathfrak T_1\) when the observed outcome lies in \(A\) and decide \(\mathfrak T_2\) otherwise. With equal priors,

\[
R_\pi(A)
=
\frac12P_1^{\pi,q}(A^c)
+
\frac12P_2^{\pi,q}(A).
\]

Rearranging,

\[
R_\pi(A)
=
\frac12
\left[
1-
\left(P_1^{\pi,q}(A)-P_2^{\pi,q}(A)\right)
\right].
\]

Optimizing over measurable decision regions gives

\[
R_\pi^*
=
\frac12
\left(
1-
\sup_A|P_1^{\pi,q}(A)-P_2^{\pi,q}(A)|
\right),
\]

which is exactly the total-variation formula. Taking the infimum over protocols yields

\[
\inf_{\pi\in\Pi}R_\pi^*
=
\frac12(1-\Delta_\Pi).
\]

## 4.3 Part C

Because

\[
\delta=
\sup_A|P_1(A)-P_2(A)|,
\]

for every \(\eta<\delta\) there exists an event \(A\) with probability gap greater than \(\eta\). Without loss of generality, let

\[
p_1=P_1(A)>p_2=P_2(A),
\qquad
p_1-p_2>\eta.
\]

For independent repetitions define

\[
Z_k=\mathbf 1\{Y_k\in A\}.
\]

Under theory \(i\), \(\mathbb E_i Z_k=p_i\). Use threshold

\[
t=\frac{p_1+p_2}{2}.
\]

Hoeffding's inequality gives, under either theory,

\[
P(\text{error})
\le
\exp\left[
-2n\left(\frac{p_1-p_2}{2}\right)^2
\right]
<
\exp\left(-\frac{n\eta^2}{2}\right).
\]

This proves Part C.

\[
\boxed{\text{QED}}
\]

---

# 5. Physical interpretation

Proposition 2 separates two questions that are often conflated in consciousness research:

1. Do two theories make different consciousness assignments?
2. Do those assignments generate different observable probability laws under physically admissible experiments?

Only the second determines empirical identifiability.

If

\[
\bar B_1(q)\ne\bar B_2(q)
\]

but

\[
\Delta_\Pi=0,
\]

then the bridge disagreement is real inside the formalisms but experimentally unresolved within \(\Pi\).

---

# 6. Connection to unfolding-style arguments

The unfolding argument of Doerig et al. motivates an important case in which implementations differ in internal causal structure while reproducing the same declared functional behavior.

Proposition 2 turns this scientific concern into an explicit quantity. For any chosen experiment class, compute or bound

\[
\Delta_\Pi.
\]

If it vanishes, the theories are experimentally equivalent within that class. If it is positive, the formalism identifies where a discriminating experiment must exist.

---

# 7. Relation to contemporary adversarial testing

The 2025 Cogitate adversarial collaboration directly compared preregistered predictions of IIT and global neuronal workspace theory using fMRI, MEG, and intracranial EEG. Several predictions were supported while key predictions of both theories were challenged.

That study emphasized the need for a quantitative framework integrating theoretical predictions, measurement error, and evidence across modalities. Proposition 2 supplies one component of such a framework: before evidence is accumulated, a theory pair and experiment class can be evaluated for how much observable separation they are capable of producing.

---

# 8. Statistical lineage

The relation between total variation and binary hypothesis testing is standard statistical decision theory; see Le Cam and Yang, *Asymptotics in Statistics*, and Tsybakov, *Introduction to Nonparametric Estimation*.

The repeated-sampling bound uses Hoeffding's inequality for bounded independent random variables.

The application of these tools to explicit consciousness-bridge identifiability is the repository's construction.

---

# 9. Status and next theorem

| Item | Status |
| --- | --- |
| experiment-class discriminability | defined |
| exact non-identifiability criterion | proved |
| optimal one-shot Bayes error | proved from standard testing identity |
| independent-repetition amplification | proved using Hoeffding concentration |
| adaptive/sequential experiment classes | future extension |
| consciousness bridge itself | not yet selected |

The next theorem layer will characterize **bridge-equivalence classes**: groups of consciousness theories that remain observationally indistinguishable under a declared physical experiment class.
