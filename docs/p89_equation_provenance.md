# P89 Equation Provenance

This record separates standard mathematical tools from repository-original derivations and exact computational certificates for Proposition 89.

## Scope

P89 studies the complete class of real linear functionals of the eleven canonical P83 even-parity observables for the declared P75 four-view binary latent target-measurement family.

It does not treat the P75 latent state as an established experiential variable. Every statement below is conditional on the declared P75 model, the rational parameter box, and the stated empirical law.

## Provenance table

| Equation / claim | Provenance class | Support |
| --- | --- | --- |
| \(P_s(H_J)=(1+\prod_{j\in J}(1-2q_{j,s}))/2\) | inherited repository derivation | P83 parity identity |
| P75 parity-vector multi-affinity in all nine parameters | repository derivation from the P83 identity and P75 mixture | direct algebra |
| Linear-functional extrema occur at parameter-box vertices | standard multi-affine vertex-extremum fact, specialized here | direct coordinatewise affine argument |
| \(D(c)=\min_a\sum_x|(Ac)_x-a|\) | repository transfer construction inherited from P84-P88 and generalized to eleven coordinates | mass-conservation centering |
| \(|Q_c(p)-Q_c(q)|\le D(c)\|p-q\|_\infty\) | repository derivation | Holder inequality after centering |
| \(L_{\mathrm{lin}}(B)=\sup_{c\ne0}\Delta_B(c)/D(c)\) | P89 definition | repository-original formulation |
| Convex-combination plus zero-mass perturbation upper certificate | P89 repository-original derivation | Proposition 89A |
| \(L_{\mathrm{lin}}(B)=R_B(\widehat y)\) | finite-dimensional linear-programming duality applied to the P89 primal/dual pair | standard LP strong duality plus repository specialization |
| Strict coefficient vector \((0,-2,-1,1,1,1,-2,-1,-3,2,-3)\) | exact computational discovery, then exact rational verification | P89 implementation/tests |
| Exact empirical value \(-13/6\) | exact repository computation | `Fraction` arithmetic |
| Exact P75 interval \([-51/8,-3]\) | exact box-vertex evaluation | `Fraction` arithmetic |
| Exact centered norm \(28\) with center \(-3\) | exact finite minimization | `Fraction` arithmetic |
| Exact lower certificate \(5/168\) | repository derivation from gap \(5/6\) divided by norm \(28\) | exact arithmetic |
| Eight nonzero convex weights in the strict upper certificate | exact computational discovery, then exact rational verification | P89 tests |
| Signed perturbation \(\delta\) with zero mass and \(\|\delta\|_\infty=5/168\) | exact computational discovery, then exact rational verification | P89 tests |
| \(\widehat y=\bar v+A^\top\delta\) | exact repository verification | componentwise `Fraction` equality |
| \(L_{\mathrm{lin}}(B)=5/168\) on the strict witness | matching exact lower/upper certificate | Proposition 89 |
| \(1/64<5/168\) | exact arithmetic | difference \(19/1344>0\) |

## Standard results used

P89 uses only elementary finite-dimensional tools beyond the already documented P75-P88 machinery:

1. a scalar multi-affine function on a rectangular box attains its extrema at box vertices;
2. Holder's inequality between \(\ell_1\) and \(\ell_\infty\);
3. strong duality for feasible finite linear programs with finite optimum.

The scientifically substantive specialization is repository-original: the eleven-coordinate parity map, its centered full-law transfer norm, the exact primal perturbation formulation, and the matching rational strict certificate are assembled specifically for the P75 model-separation problem.

## Exact strict certificate data

Canonical parity-coordinate order:

```text
(01), (02), (03), (12), (13), (23),
(012), (013), (023), (123), (0123)
```

Dual/lower functional coefficient vector:

```text
(0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)
```

Exact values:

```text
empirical functional value = -13/6
P75 box interval          = [-51/8, -3]
interval gap              = 5/6
centering constant        = -3
centered transfer norm    = 28
normalized lower bound    = 5/168
```

The complete upper certificate is stored directly in `tests/test_complete_linear_parity_duality.py` and verified by `verify_complete_linear_parity_upper_certificate_exact`.

## Scientific boundary

The matching P89 certificate proves completeness only for real linear combinations of the eleven declared parity observables on the stated P75 box. It is not a proof that the true model distance equals \(5/168\), not a proof that all nonlinear P75 constraints have been exhausted, and not evidence that consciousness is nonphysical or an additional physical dimension.
