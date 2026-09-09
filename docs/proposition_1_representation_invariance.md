# Proposition 1: representation-invariant consciousness bridges

## Physical question

A single physical realization may admit many mathematically different descriptions.

Examples include:

\[
x\mapsto z=\varphi(x),
\]

unit changes, coordinate permutations, invertible encodings, and alternative state-space parameterizations.

If such transformations preserve the physical content declared relevant by a consciousness theory, then the consciousness assignment should not depend on which description is used.

The first theorem makes that requirement exact.

---

# 1. Mathematical setup

Let

\[
\mathcal P
\]

be a set of physical descriptions and let

\[
\sim_P
\]

be an equivalence relation encoding physically irrelevant representational differences.

Let

\[
\mathcal E
\]

be a set of formal experiential structures with experiential equivalence relation

\[
\sim_E.
\]

Write the experiential quotient as

\[
\mathcal Q_E=\mathcal E/{\sim_E}.
\]

Let a candidate bridge assignment be

\[
B:\mathcal P\to\mathcal Q_E.
\]

The physical quotient is

\[
\mathcal Q_P=\mathcal P/{\sim_P}.
\]

The quotient projection is

\[
\pi_P:\mathcal P\to\mathcal Q_P,
\qquad
\pi_P(p)=[p]_{\sim_P}.
\]

The question is:

> When does there exist a unique map
>
> \[
> \bar B:\mathcal Q_P\to\mathcal Q_E
> \]
>
> such that
>
> \[
> B=\bar B\circ\pi_P?
> \]

---

# 2. Proposition

## Proposition 1

The following are equivalent:

1. There exists a unique map

   \[
   \bar B:\mathcal P/{\sim_P}\to\mathcal E/{\sim_E}
   \]

   satisfying

   \[
   B=\bar B\circ\pi_P.
   \]

2. The bridge assignment is constant on physical equivalence classes:

   \[
   \boxed{
   p\sim_P p'
   \Longrightarrow
   B(p)=B(p').
   }
   \]

Equivalently, a physical-to-experiential bridge is well defined on physical equivalence classes if and only if it is representation invariant with respect to the declared physical equivalence relation.

---

# 3. Proof

### \(1\Rightarrow2\)

Assume there exists

\[
\bar B:\mathcal Q_P\to\mathcal Q_E
\]

such that

\[
B=\bar B\circ\pi_P.
\]

If

\[
p\sim_P p',
\]

then

\[
\pi_P(p)=\pi_P(p').
\]

Therefore

\[
B(p)
=
\bar B(\pi_P(p))
=
\bar B(\pi_P(p'))
=
B(p').
\]

Thus \(B\) is constant on physical equivalence classes.

### \(2\Rightarrow1\)

Assume

\[
p\sim_P p'
\Longrightarrow
B(p)=B(p').
\]

Define

\[
\bar B([p]_{\sim_P})=B(p).
\]

To show that this definition is well defined, suppose

\[
[p]_{\sim_P}=[p']_{\sim_P}.
\]

Then

\[
p\sim_P p',
\]

so by assumption

\[
B(p)=B(p').
\]

Hence the value of \(\bar B\) does not depend on the chosen representative of the equivalence class.

Moreover,

\[
\bar B(\pi_P(p))
=
\bar B([p]_{\sim_P})
=
B(p),
\]

so

\[
B=\bar B\circ\pi_P.
\]

For uniqueness, suppose \(\tilde B\) also satisfies

\[
B=\tilde B\circ\pi_P.
\]

For any class \([p]_{\sim_P}\),

\[
\tilde B([p]_{\sim_P})
=
B(p)
=
\bar B([p]_{\sim_P}).
\]

Therefore

\[
\tilde B=\bar B.
\]

\[
\boxed{\text{QED}}
\]

---

# 4. Physical interpretation

The theorem is elementary as quotient mathematics, but scientifically important.

It says that before asking whether a physical system is conscious, a theory must answer a prior question:

\[
\boxed{
\text{Which differences in physical description are physically meaningful to the bridge?}
}
\]

Once the physical equivalence relation is declared, representation invariance is no longer optional. It is exactly the condition required for a unique consciousness assignment on physical equivalence classes.

---

# 5. Examples

## 5.1 Coordinate relabeling

Suppose a finite system has state

\[
x=(x_1,\ldots,x_n)
\]

and a permutation matrix \(P\) gives

\[
z=Px.
\]

If this permutation merely relabels coordinates and the corresponding dynamics and interventions are transformed consistently, then

\[
p\sim_P p'.
\]

A valid bridge must satisfy

\[
B(p)=B(p').
\]

## 5.2 Change of units

If

\[
z_i=a_i x_i,
\qquad
a_i>0,
\]

is only a change of physical units, the bridge cannot change solely because meters were replaced by centimeters or volts by millivolts.

## 5.3 Non-equivalent transformation

If an operation changes physically admissible interventions or alters the causal response structure, then the transformed system need not belong to the same equivalence class.

Representation invariance therefore does not imply that every mathematical transformation is physically irrelevant.

The burden is to define \(\sim_P\) correctly.

---

# 6. Consequence for consciousness metrics

Suppose a scalar candidate metric is

\[
C:\mathcal P\to\mathbb R.
\]

If consciousness is later defined through \(C\), a necessary representation condition is

\[
\boxed{
p\sim_P p'
\Longrightarrow
C(p)=C(p').
}
\]

Otherwise the numerical value depends on physically irrelevant description choices.

This is one reason the project does not begin by proposing a new scalar consciousness index.

---

# 7. Relation to existing consciousness mathematics

Tegmark 2015 emphasizes the importance of factorization and invariance questions in connecting physical descriptions to observer-like structure.

Kleiner 2019 develops a general mathematical framework for models of consciousness and emphasizes the need to justify the mathematical representation of phenomenal experience.

Kleiner and Tull formalize the mathematical structure of IIT in an axiomatic setting.

The present proposition addresses a prior bridge requirement in a general form: once physical and experiential equivalence relations are declared, the bridge must descend to their quotient structure.

See [Literature Map](literature_map.md).

---

# 8. Status

| Item | Status |
| --- | --- |
| proposition | proved |
| physical equivalence relation | theory-dependent object to be specified |
| experiential equivalence relation | open formalization problem |
| empirical claim | none required for the quotient theorem |
| next theorem | bridge identifiability under an experiment class |

The next result will ask when two quotient-level bridges

\[
\bar B_1,\bar B_2
\]

can be distinguished by admissible physical observations and interventions.
