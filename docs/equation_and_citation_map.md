# Equation and Citation Map

This page distinguishes repository definitions, standard mathematics, physical modeling assumptions, candidate physical hypotheses, bridge hypotheses, theorem statements, theory-family translations, and external empirical evidence.

Its purpose is provenance: a reader should be able to determine immediately whether an equation is introduced here, inherited from standard mathematics, adapted from an external theory, or motivated by experiment.

---

# 1. Physical and bridge objects

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O)\) | physical-system object | repository definition | physical modeling framework |
| \(dX_t=f(X_t,u_t)dt+G(X_t,u_t)dW_t\) | example stochastic physical model | standard modeling form | stochastic dynamics |
| \(K_{\Delta t}(\cdot\mid X_t,u_t)\) | transition-kernel representation | standard probability object | stochastic-process modeling |
| \(\mathcal B\subseteq\mathcal P\times\mathcal E\) | general physical-to-experiential bridge relation | repository definition | bridge formulation |
| \(p\sim_Pp'\) | physically irrelevant representation equivalence | repository definition, theory dependent | quotient framework |
| \(e\sim_Ee'\) | experiential equivalence | repository definition, open formalization | mathematical-consciousness context |
| \(\mathcal Q_P=\mathcal P/{\sim_P}\) | physical quotient | repository construction using standard quotient mathematics | P1 |
| \(\mathcal Q_E=\mathcal E/{\sim_E}\) | experiential quotient | repository construction using standard quotient mathematics | P1 |
| \(\bar B:\mathcal Q_P\to\mathcal Q_E\) | quotient-level bridge | repository construction | P1 |
| \(B=\bar B\circ\pi_P\) | bridge factorization through physical quotient | proved | P1 + standard quotient logic |

---

# 2. P1-P4 - representation, identifiability, and theory comparison

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p\sim_Pp'\Rightarrow B(p)=B(p')\) | representation-invariance criterion | proved equivalent to quotient factorization | P1 |
| \(P_i^{\pi,q}\) | observable law predicted by complete bridge theory \(i\) | repository notation | P2 |
| \(\|P-Q\|_{\mathrm{TV}}\) | probability distance controlling binary distinguishability | standard probability/statistics | Le Cam-Yang; Tsybakov |
| \(\Delta_\Pi=\sup_{\pi\in\Pi}\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\) | experiment-class bridge discriminability | repository construction | P2 |
| \(R_\pi^*=\tfrac12(1-\|P_1-P_2\|_{\mathrm{TV}})\) | optimal equal-prior binary testing error | standard identity applied here | decision theory; P2 |
| \(\exp(-n\eta^2/2)\) | repeated-event discrimination bound | standard concentration applied here | Hoeffding 1963; P2 |
| \(\Phi_{\Pi,q}(\mathfrak T)=(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}\) | complete observable theory fingerprint | repository construction | P3 |
| \(\Theta/{\sim_{\Pi,q}}\cong\operatorname{Im}(\Phi_{\Pi,q})\) | observational theory quotient | proved | P3 + quotient logic |
| \(d_{ij}(\pi)=\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}\) | protocol-specific theory-pair separation | repository construction | P4 |
| \(U(S)=\min_{\{i,j\}\in\mathcal U}\max_{\pi\in S}d_{ij}(\pi)\) | worst-pair protocol-family separation | repository construction | P4 |
| \(U(S)>0\iff\bigcup_{\pi\in S}C_\pi=\mathcal U\) | complete-discrimination / set-cover equivalence | proved | P4 |

---

# 3. P5-P6 - physical-feature sufficiency and bridge completeness

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(F:\mathcal Q_P\to\mathcal Z\) | proposed representation-invariant physical feature | generic repository notation | P5 |
| \(\bar B=g\circ F\) | bridge factorization through physical feature | definition of sufficiency | P5 |
| \(F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p')\) | fiber-constancy criterion | proved equivalent to factorization | P5 |
| \(p\sim_Bp'\iff\bar B(p)=\bar B(p')\) | bridge-induced physical equivalence | repository definition | P6 |
| \(\mathcal Q_B=\mathcal Q_P/{\sim_B}\) | canonical bridge quotient | repository construction | P6 |
| \(C_B(p)=[p]_{\sim_B}\) | canonical complete bridge signature | repository construction | P6 |
| \(C_B(p)=C_B(p')\iff\bar B(p)=\bar B(p')\) | exact canonical completeness | proved | P6 |
| \(\mathcal Q_B\cong\operatorname{Im}(\bar B)\) | quotient / bridge-image equivalence | proved | P6 |
| \(F_*(p)=F_*(p')\iff C_B(p)=C_B(p')\) | complete physical-signature target | repository theorem target | P6 / Universal Proof Target |

---

# 4. P7-P10 - recoverability, finite data, and experiment design

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Psi_\Pi(p)=(P^{\pi,p})_{\pi\in\Pi}\) | complete experimental fingerprint of a physical realization | repository construction | P7 |
| \(\Psi_\Pi(p)=\Psi_\Pi(p')\Rightarrow F_*(p)=F_*(p')\) | exact recoverability criterion | proved | P7 |
| \(d_S(p,p')=\max_{\pi\in S}\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}\) | protocol-family physical distance | repository construction | P8 |
| \(\omega_S\) | maximum within-signature spread | repository definition | P8 |
| \(\delta_S\) | minimum between-signature separation | repository definition | P8 |
| \(\gamma_S=\delta_S-\omega_S\) | robust signature gap | repository construction | P8 |
| \(|\widehat d_S-d_S|\le2\varepsilon\) | distance perturbation bound | proved from the TV triangle inequality | P8 |
| \(\gamma_S>4\varepsilon\) | sufficient exact-partition recovery condition | proved | P8 |
| \(\Pr(|\widehat p_j-p_j|>a)\le2e^{-2na^2}\) | one-category empirical-frequency concentration | standard inequality | Hoeffding 1963 |
| \(2N_PN_\pi K\exp(-8n\varepsilon^2/K^2)\) | uniform categorical failure bound | proved from Hoeffding + union bounds | P9 |
| \(n\ge\frac{8K^2}{\gamma_S^2}\log\frac{2N_PN_\pi K}{\alpha}\) | sufficient per-cell trials for exact signature recovery | proved | P9 |
| \(\Gamma(S)=\delta(S)-\omega(S)\) | robust protocol-family design objective | repository construction | P10 |
| \(\Gamma(S\cup\{\rho\})-\Gamma(S)=a_\rho(S)-b_\rho(S)\) | exact marginal protocol-value identity | proved | P10 |
| \(\Gamma(S\cup\{\rho\})>\Gamma(S)\iff a_\rho(S)>b_\rho(S)\) | added-protocol improvement criterion | proved | P10 |

---

# 5. P11 - intervention-resolved causal structure

The intervention-resolved causal structure is a repository-original **candidate physical signature**. The equations in this section are definitions or theorems about that physical object; none is imported from an external source as an identity with consciousness.

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_p^{u,\tau}=\mathcal L(Y_{t+\tau}^V\mid do(u),p)\) | intervention-conditioned joint response law | repository definition using standard intervention semantics | P11; Pearl for \(do\)-notation context |
| \(d_p^\tau(u,v)=\|P_p^{u,\tau}-P_p^{v,\tau}\|_{\mathrm{TV}}\) | intervention-response pseudometric | repository construction | P11 + standard TV distance |
| \(\mathcal G_p=\{d_p^\tau:\tau\in\mathcal T\}\) | response-geometry family | repository definition | P11 |
| \(A_{ij}^{p}(\tau)=\sup_{(u,v)\in\mathcal E_i}\|P_{p,j}^{u,\tau}-P_{p,j}^{v,\tau}\|_{\mathrm{TV}}\) | directed perturbational influence | repository construction | P11 |
| \(\mathcal A_p=\{A_{ij}^{p}(\tau)\}_{i,j,\tau}\) | directed influence tensor | repository definition | P11 |
| \(P_{p,\pi}^{u,\tau}=\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}\) | productized partition response | standard product measure applied here | P11 |
| \(\kappa_p^\tau(\pi)=\sup_u\|P_p^{u,\tau}-P_{p,\pi}^{u,\tau}\|_{\mathrm{TV}}\) | partition response irreducibility | repository construction | P11 |
| \(\mathcal K_p=\{\kappa_p^\tau(\pi)\}_{\pi,\tau}\) | complete partition landscape | repository definition | P11 |
| \(\mathfrak C_p=(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p)\) | raw intervention-resolved causal structure | repository definition | P11 |
| \(F_{\mathrm{causal}}(p)=[\mathfrak C_p]_{\cong}\) | representation-invariant causal-structure signature | repository construction | P11 |
| \(\kappa_p^\tau(\pi)=0\iff P_p^{u,\tau}=\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}\ \forall u\) | exact factorization certificate | proved | P11 |
| DAG influence graph \(\Rightarrow\) no directed return loop | feedforward no-return certificate | proved | P11 + graph-theoretic definition |

## P11 empirical motivation map

| Physical idea motivating measurement | External evidence / theory role | Citation |
| --- | --- | --- |
| direct perturbation + differentiated distributed response | perturbational-complexity evidence | Casali et al. 2013; Maschke et al. 2024 |
| intrinsic causal organization / irreducibility | existing bridge-theory motivation | Albantakis et al. 2023 |
| recurrent and distributed processing | theory-family motivation | Mashour et al. 2020; Lamme 2006; Changeux-Farisco 2026 |
| synergistic integration changing with consciousness | empirical information-integration evidence | Luppi et al. 2024 |
| integration and controllability under anesthesia | cross-species empirical evidence | Luppi et al. 2026 |

These sources motivate quantities worth measuring. They do not establish the bridge-completeness target for the causal-structure candidate.

---

# 6. P12 - single-component minimality and projection collisions

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(H(x)=H(x')\) but \(F(x)\ne F(x')\) | projection collision | repository definition of collision witness | P12 |
| collision \(\Rightarrow\nexists g:F=g\circ H\) | compression non-reconstructibility theorem | proved | P12 + P5 factorization logic |
| \(\mathcal G_C=\mathcal G_P\) but \(\kappa_C\ne\kappa_P\) | response-geometry collision | explicit realizable construction | P12 |
| \(\mathcal K_D=\mathcal K_S\) but \(\mathcal G_D\ne\mathcal G_S\) | partition-landscape collision | explicit realizable construction | P12 |
| \(\mathcal A_R=\mathcal A_I\) but \(\mathcal G_R\ne\mathcal G_I\) | directed-influence collision | explicit realizable construction | P12 |
| \(\operatorname{Diam}_p(\tau)\) | scalar response-diameter compression | proved incomplete on explicit domain | P12 |
| \(\kappa_p^*\) | minimum irreducibility scalar | proved incomplete on explicit domain | P12 |
| cycle/no-cycle indicator | Boolean recurrence compression | proved incomplete for influence strength | P12 |

P12 is a physical-signature minimality theorem. It demonstrates that several natural one-component or scalar compressions lose information before any experiential interpretation is attached.

---

# 7. P13 - pairwise component irredundancy

Define the labeled component fingerprint

\[
F_C(p)=(\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

P13 proves on the declared audit domain that each pairwise projection is incomplete:

\[
\boxed{
H_{GA},\ H_{GK},\ H_{AK}
\text{ are all incomplete projections on }D_{13}.
}
\]

This is a component-level irredundancy result on the declared finite domain, not a global minimality theorem over every possible physical representation.

---

# 8. P14 - temporal continuation on the causal-structure quotient

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(c=(g,a,k)\) | finite ordered causal-structure fingerprint | repository notation | P14, built from P11-P13 |
| \(D_w(c,c')=\max\{w_G\|g-g'\|_\infty,w_A\|a-a'\|_\infty,w_K\|k-k'\|_\infty\}\) | fixed-coordinate weighted component metric | repository construction using standard sup-norm metrics | P14; metric background: Burago-Burago-Ivanov |
| \(\mathcal H\) | finite group of physically admissible fingerprint relabelings acting by isometries | declared physical/modeling assumption | P14 |
| \(\overline D_w([c],[c'])=\min_{h\in\mathcal H}D_w(c,hc')\) | representation-invariant quotient distance | repository construction; proved metric on orbit space | P14; quotient/metric background: Burago-Burago-Ivanov |
| \(V_{0:T}=\sum_{t=0}^{T-1}\overline D_w([c_t],[c_{t+1}])\) | cumulative structural path variation | repository construction | P14 |
| \(J_{0:T}=\max_t\overline D_w([c_t],[c_{t+1}])\) | maximum local structural transition | repository construction | P14 |
| \(\overline D_w([c_s],[c_t])\le V_{s:t}\) | endpoint/path bound | proved from quotient-metric triangle inequality | P14 |
| time-dependent relabelings leave \(V\) and \(J\) invariant | representation-invariant temporal continuation | proved | P14 |
| \([a]\to[b]\to[a]\) with zero endpoint distance but positive path variation | endpoint-only insufficiency counterexample | proved explicit construction | P14 |

Peters-Bauer-Pfister provide dynamical causal-model context and Mashour 2024 supplies biological motivation for treating consciousness-related conditions as evolving dynamical regimes. Neither source supplies the P14 metric or implies that temporal smoothness is consciousness.

---

# 9. P15 - finite-sample temporal certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D_w(c_t,\widehat c_t)\le\varepsilon_t\) simultaneously over time | declared fingerprint-error event | theorem assumption | P15 |
| \(|\widehat d_{st}-d_{st}|\le\varepsilon_s+\varepsilon_t\) | quotient-distance stability | proved | P15 + P14 metric triangle inequality |
| \(\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}\le d_{st}\le\widehat d_{st}+\varepsilon_s+\varepsilon_t\) | certified interval for true structural change | proved | P15 |
| \(|\widehat V-V|\le\varepsilon_0+2\sum_{t=1}^{T-1}\varepsilon_t+\varepsilon_T\) | cumulative path-variation perturbation bound | proved | P15 |
| \(|\widehat J-J|\le\max_t(\varepsilon_t+\varepsilon_{t+1})\) | maximum-step perturbation bound | proved | P15 |
| lower bound above \(\eta\), upper bound below \(\eta\), otherwise unresolved | three-way threshold certificate | repository decision rule derived from the proved interval | P15 |
| \(\delta_n(\alpha)=\sqrt{\frac1{2n}\log\frac{2M(T+1)}{\alpha}}\) | simultaneous coordinate radius for the restricted bounded-IID sample-mean model | standard Hoeffding inequality + union bound applied here | Hoeffding 1963; P15 corollary |
| \(\varepsilon_t=w_{\max}\delta_n(\alpha)\) | translation from coordinate error to weighted max-metric radius in that restricted model | repository corollary | P15 |

The bounded-coordinate corollary is intentionally narrow. It does not assert that every P11 response-geometry, influence, or irreducibility coordinate is a direct IID sample mean; estimator-specific concentration is required outside that special case.

---

# 10. P16 - independent composition and controlled coupling

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_{A\otimes B}^{(u_A,u_B),\tau}=P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}\) | independent product-response composition | repository physical null-model definition using standard product measures | P16; product-measure background: standard probability |
| \(\max\{d_A,d_B\}\le d_{AB}\) | lower response-distance bound under composition | proved by total-variation contraction under marginalization | P16; standard TV data-processing property |
| \(d_{AB}\le d_A+d_B-d_Ad_B\) | product-coupling upper bound | proved using maximal coupling of subsystem response pairs | P16; coupling interpretation of total variation |
| one subsystem unchanged \(\Rightarrow d_{AB}=d_A\) or \(d_B\) | exact one-factor distance preservation | proved | P16 |
| \(A_{ij}^{A\otimes B}(\tau)=0\) for \(i\in A,j\in B\) | zero cross-system directed influence under independent composition | proved | P16 + P11 directed-influence definition |
| \(\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0\) | exact factorization across complete subsystem split | proved | P16 + P11 partition irreducibility |
| \(\chi_{A|B}(\tau)=\sup_{u_A,u_B}\|P_{AB}-P_{A,\mathrm{marg}}\otimes P_{B,\mathrm{marg}}\|_{\mathrm{TV}}\) | response-level coupling defect | repository construction | P16 |
| \(\chi_{A|B}(\tau)=\kappa_{AB}^{\tau}(\pi_{A|B})\) | identification of coupling defect with P11 partition irreducibility | proved | P16 |
| \(\chi=0\) certifies factorization only on the declared intervention-observable regime | identifiability boundary | theorem interpretation / limitation | P16 + P2-P4/P7 identifiability framework |

The mathematical ingredients are standard properties of total variation, measurable marginalization, product measures, and couplings. The specific physical composition null model, coupling-defect use, and connection to the bridge program are repository constructions.

---

# 11. P17 - coarse-graining and refinement

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C:\Omega_f\to\Omega_c\) | deterministic coarse-graining map | repository modeling definition | P17 |
| \(C_\#P(y)=\sum_{x:C(x)=y}P(x)\) | pushforward of a fine response law | standard pushforward construction applied here | P17; standard probability |
| \(\|C_\#P-C_\#Q\|_{\mathrm{TV}}\le\|P-Q\|_{\mathrm{TV}}\) | data-processing contraction under deterministic coarse-graining | proved for the declared response laws | P17; standard TV contraction principle |
| fine-scale collision with identical coarse pushforwards | exact refinement non-recoverability witness | repository counterexample | P17 |
| bijective reparameterization preserves TV exactly | representation-preserving special case | proved | P17 |

P17 is a physical information-loss theorem. It does not identify a privileged biological scale and does not attach an experiential interpretation to coarse-graining.

---

# 12. P18 - scale sufficiency by approximate reconstruction

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D=R_\#C_\#\) | reconstruction operator induced by a coarse map and declared decoder | repository construction using standard pushforwards | P18 |
| \(\rho(P)=\|P-R_\#C_\#P\|_{\mathrm{TV}}\) | response-law reconstruction defect | repository definition | P18 |
| \(\rho_{\mathcal F}=\sup_{P\in\mathcal F}\rho(P)\) | uniform family reconstruction defect | repository definition | P18 |
| \(0\le d_f-d_c\le\rho(P)+\rho(Q)\le2\rho_{\mathcal F}\) | pairwise response-geometry distortion certificate | proved | P18 |
| \(\delta_c\ge\delta_f-2\rho_{\mathcal F}\) | finite-family separation guarantee | proved | P18 |
| \(\rho_{\mathcal F}=0\Rightarrow d_c=d_f\) on the declared family | exact family scale sufficiency | proved | P18 |

The pushforward, total variation, and triangle inequality are standard mathematics. The reconstruction-defect certificate and its role as a scale-sufficiency criterion are repository results.

---

# 13. P19 - fundamental physical sufficiency and residual tests

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(T:\mathcal M\to\mathcal Q_T\) | declared physical descriptor on a candidate fundamental state space | repository abstraction | [P19](proposition_19_fundamental_physical_sufficiency.md) |
| \(E:\mathcal M\to\mathcal Q_E\) | independently defined target descriptor | repository abstraction; experiential instantiation remains open | P19 |
| \(E=B_T\circ T\) iff \(E\) is constant on every fiber of \(T\) | exact deterministic physical-sufficiency criterion | proved | P19; standard quotient and factorization logic |
| \(T(\Omega)=T(\Omega')\) and \(E(\Omega)\ne E(\Omega')\) | exact no-factorization witness relative to the declared \(T\) | proved | [P19](proposition_19_fundamental_physical_sufficiency.md) |
| \(E\perp\!\!\!\perp\Omega\mid T\) | stochastic physical-sufficiency condition | standard conditional-independence form applied here | [P19](proposition_19_fundamental_physical_sufficiency.md); [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) |
| \(I(E;\Omega\mid T)=0\) | finite-alphabet information criterion equivalent to conditional independence | standard information-theoretic identity applied here | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P19](proposition_19_fundamental_physical_sufficiency.md) |
| \(I(E;\Omega\mid T)=H(E\mid T)\) for deterministic \(E=E(\Omega)\) | deterministic-target corollary | proved from standard entropy identities | [P19](proposition_19_fundamental_physical_sufficiency.md); [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) |
| \(\operatorname{rank}D(T,E)=\operatorname{rank}DT\) under local smooth factorization | necessary differential condition | proved by the chain rule | [P19](proposition_19_fundamental_physical_sufficiency.md); [Lee 2013](foundational_physics_mathematics_bibliography.md#lee-2013) |
| \(d_\perp=\operatorname{rank}D(T,E)-\operatorname{rank}DT>0\) | sufficient local no-factorization witness | proved | [P19](proposition_19_fundamental_physical_sufficiency.md) |

P19 is a theorem about sufficiency relative to a declared physical descriptor. A residual first indicates that the declared descriptor may be incomplete. It is not by itself evidence for a nonphysical substance, a new spacetime dimension, or a failure of quantum mechanics.

---

# 14. P20 - finite-sample residual certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(M=d_\Omega d_T d_E\) | declared joint alphabet size | repository sampling-model definition | [P20](proposition_20_finite_sample_residual_certification.md) |
| \(a_n(\alpha)=\sqrt{\frac1{2n}\log\frac{2M}{\alpha}}\) | simultaneous cell-frequency radius | standard Hoeffding inequality plus union bound applied here | [Hoeffding 1963](https://doi.org/10.1080/01621459.1963.10500830); [P20](proposition_20_finite_sample_residual_certification.md) |
| \(\tau_n(\alpha)=\min\{1,\frac M2 a_n(\alpha)\}\) | conservative joint total-variation confidence radius | proved from the simultaneous cell bounds | [P20](proposition_20_finite_sample_residual_certification.md) |
| \(c_d(r)\) | uniform finite-alphabet entropy-continuity radius for a known TV upper bound | standard finite-alphabet entropy reasoning applied and proved here | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P20](proposition_20_finite_sample_residual_certification.md) |
| \(\Delta_{\mathrm{CMI}}(r)\) | propagates joint-distribution TV error through the four entropy terms of conditional mutual information | repository finite-sample construction | [P20](proposition_20_finite_sample_residual_certification.md) |
| \(|I_P-\widehat I_n|\le\Delta_{\mathrm{CMI}}(\tau_n(\alpha))\) | finite-sample population-residual confidence bound | proved under the declared finite-alphabet IID model | [P20](proposition_20_finite_sample_residual_certification.md) |
| \(L_n>0\Rightarrow I_P(E;\Omega\mid T)>0\) at confidence \(1-\alpha\) | certified rejection of P19 stochastic screening-off for the declared descriptor | proved finite-sample decision rule | [P20](proposition_20_finite_sample_residual_certification.md) |

P20 is deliberately conservative. A positive lower confidence bound certifies insufficiency of the declared descriptor under the sampling model. It does not identify the residual as nonphysical and does not remove the need to test omitted physical variables, measurement error, system boundaries, timescale, preprocessing, and sampling assumptions.

---

# 15. P21 - physical-descriptor refinement and residual persistence

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(T_c=c\circ T_f\) with \(T_f=f(\Omega)\) | declares a nested deterministic physical-description relation | repository modeling assumption using standard function composition | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(\mathcal C(T_f,E)\subseteq\mathcal C(T_c,E)\) | deterministic target-collision monotonicity under valid refinement | proved | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T)=I(E;\Omega\mid T)\) | descriptor-relative stochastic residual inherited from P19 | repository diagnostic built from standard conditional mutual information | [P19](proposition_19_fundamental_physical_sufficiency.md); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T_c)=I(E;T_f\mid T_c)+R(T_f)\) | exact decomposition of the coarse residual into refinement capture plus remaining residual | proved from the conditional-mutual-information chain rule and deterministic nesting | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R(T_f)\le R(T_c)\) | residual monotonicity under valid physical refinement | proved | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(R_0-R_m=\sum_{k=1}^{m}I(E;T_k\mid T_{k-1})\) | exact telescoping accounting for a nested descriptor chain | proved by repeated P21 decomposition | [P21](proposition_21_descriptor_refinement_residual_persistence.md) |
| \(I(E;\Omega\mid\Omega)=0\) | identity-descriptor boundary preventing ontological overinterpretation of screening-off residuals | standard conditional-information identity used here as an interpretation guard | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P21](proposition_21_descriptor_refinement_residual_persistence.md) |

P21 formalizes an omitted-physics control. Persistence of a residual through a finite declared refinement chain is evidence only relative to that chain. Physical completeness requires an independent scientific argument; the conditional-information residual cannot supply that argument by itself.

---

# 16. P22 - simultaneous finite-sample refinement-chain certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(M=d_\Omega d_E\) | alphabet size of the common sampled base law \((\Omega,E)\) | repository sampling-model definition | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\|P_{\Omega E}-\widehat P_{\Omega E}\|_{\mathrm{TV}}\le\tau_n(\alpha)\) | one finite-sample confidence event shared by the whole descriptor chain | Hoeffding plus union bound applied to the base categorical law | [Hoeffding 1963](https://doi.org/10.1080/01621459.1963.10500830); [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(P_k=(\phi_k)_\#P_{\Omega E}\) and \(Q_k=(\psi_k)_\#P_{\Omega E}\) | expresses residual and gain distributions as deterministic pushforwards of one base law | repository construction using standard pushforward probability | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\|P_k-\widehat P_k\|_{\mathrm{TV}}\le\tau_n\) and \(\|Q_k-\widehat Q_k\|_{\mathrm{TV}}\le\tau_n\) for all \(k\) | transfers one base confidence event to every level by TV contraction | standard data-processing property applied here | [P17](proposition_17_coarse_graining_and_refinement.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(|R_k-\widehat R_k|\le\Delta_k(\tau_n)\) simultaneously for all \(k\) | finite-sample confidence family for the P21 residual trajectory | proved from shared TV event plus P20 continuity | [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(|G_k-\widehat G_k|\le\Gamma_k(\tau_n)\) simultaneously for all \(k\) | finite-sample confidence family for target information captured by each refinement | proved from the same shared event | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(G_k=R_{k-1}-R_k\) and \(\widehat G_k=\widehat R_{k-1}-\widehat R_k\) | population and empirical chain-rule identity used to sharpen gain intervals | proved in P21 and inherited by P22 | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| \(\Pr(R_k\in\mathcal I_k^R\ \forall k,\ G_k\in\mathcal I_k^G\ \forall k)\ge1-\alpha\) | simultaneous residual-and-gain coverage | proved | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |
| no \(\alpha/(2m+1)\) replacement is required | one base-TV event deterministically implies every level-specific bound in this construction | theorem consequence, not a generic multiple-testing exemption | [P22](proposition_22_simultaneous_refinement_chain_certification.md) |

P22 is a finite-data theorem for a fixed declared deterministic refinement chain. It does not justify post hoc adaptive descriptor selection using the same confidence statement, and it does not establish physical completeness.

---

# 17. P23 - adaptive physical-descriptor selection certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\|h_\#P-h_\#\widehat P\|_{\mathrm{TV}}\le\|P-\widehat P\|_{\mathrm{TV}}\) for every deterministic \(h\) | pathwise pushforward contraction supporting uniform candidate control | standard total-variation data processing applied here | standard probability; [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(G_f=I(E;T_f\mid T_c)\) | target-relevant information captured by candidate refinement \(f\) | P21 refinement gain used as P23 selection objective | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(\widehat f\in\operatorname*{arg\,max}_f\widehat G_f\) | fixed-sample data-dependent descriptor-selection rule | repository selection construction | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(|G_f-\widehat G_f|\le\Gamma_f(\tau_n)\) for all candidates on one base event | simultaneous gain confidence family before and after selection | proved from P22 base event, TV contraction, and P20 entropy continuity | [P20](proposition_20_finite_sample_residual_certification.md); [P22](proposition_22_simultaneous_refinement_chain_certification.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(0\le G^*-G_{\widehat f}\le2\Gamma_{\max}\) | generic post-selection refinement-regret bound | proved | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(G^*-G_{\widehat f}\le\max_fU_f^G-L_{\widehat f}^G\) | data-dependent regret certificate from simultaneous candidate intervals | proved | [P23](proposition_23_adaptive_descriptor_selection_certification.md) |
| \(R_{\widehat f}-\min_fR_f=G^*-G_{\widehat f}\) | converts gain regret into excess remaining residual under a common coarse descriptor | proved from P21 identity | [P21](proposition_21_descriptor_refinement_residual_persistence.md); [P23](proposition_23_adaptive_descriptor_selection_certification.md) |

P23 is a fixed-sample post-selection theorem. The shared base confidence event supports data-dependent candidate choice because all candidate laws are deterministic pushforwards of the same finite base law. This does not provide optional-stopping validity across sample sizes and does not establish the physical admissibility or completeness of the selected descriptor.

---

# 18. P24 - anytime-valid adaptive physical-refinement certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\alpha_n=6\alpha/(\pi^2n^2)\) | summable time-indexed failure allocation | repository choice using the standard Basel identity | standard analysis; [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\sum_{n\ge1}\alpha_n=\alpha\) | exact total error-budget identity | follows from \(\sum_{n\ge1}n^{-2}=\pi^2/6\) | standard analysis; [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\tau_n^{\mathrm{any}}(\alpha)\) | time-indexed P20 base-law TV radius evaluated at local level \(\alpha_n\) | repository construction from P20 | [P20](proposition_20_finite_sample_residual_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\Pr(\forall n\ge1:\|P-\widehat P_n\|_{\mathrm{TV}}\le\tau_n^{\mathrm{any}})\ge1-\alpha\) | time-uniform base-law confidence event | proved by countable union bound over P20 failures | [P20](proposition_20_finite_sample_residual_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(\widehat f_n=S_n(Z_1,\ldots,Z_n)\) | data-dependent descriptor selected at time \(n\) | repository notation | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| selected gain and residual intervals valid for every \(n\) | repeated-look adaptive-selection coverage | proved from the P24 base event plus P23 pathwise pushforward control | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| stopping-time certificate at finite \(\tau\) | validity after a data-dependent finite stopping rule | proved because the confidence event is simultaneous over all positive times | [P24](proposition_24_anytime_adaptive_refinement_certification.md) |
| \(0\le G^*-G_{\widehat f_n}\le B_n\) for all \(n\) | anytime refinement-regret certificate | proved by applying P23 on the time-uniform event | [P23](proposition_23_adaptive_descriptor_selection_certification.md); [P24](proposition_24_anytime_adaptive_refinement_certification.md) |

P24 uses a transparent alpha-spending union-bound construction. It is intentionally conservative and is not claimed to be an optimal confidence sequence. Anytime statistical validity does not establish physical completeness or experiential interpretation.

---

# 19. P25 - directed-influence scale certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(A_{i\to j}^{f}(\tau)=\sup_{(u,v)\in\mathcal E_i}\|P_j^{u,\tau}-P_j^{v,\tau}\|_{\mathrm{TV}}\) | fine P11 directed perturbational influence | repository physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(\overline P_j^{u,\tau}=(C_j)_\#P_j^{u,\tau}\) | deterministic target observation coarse-graining | standard pushforward applied to P11 marginal law | P17; [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A_{i\to j}^{c}(\tau)\le A_{i\to j}^{f}(\tau)\) | coarse target observation cannot increase matched-pair influence | proved by TV contraction and supremum monotonicity | P17; [P25](proposition_25_directed_influence_scale_certification.md) |
| \(\rho_{i\to j}(\tau)=\sup_u\|P_j^{u,\tau}-R_{j\#}C_{j\#}P_j^{u,\tau}\|_{\mathrm{TV}}\) | uniform response-family reconstruction defect | P18 reconstruction object specialized to the P11 target family | [P18](proposition_18_scale_sufficiency_certification.md); [P25](proposition_25_directed_influence_scale_certification.md) |
| \(0\le A^f-A^c\le2\rho\) | directed-influence scale distortion theorem | proved | [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A^f>\theta+2\rho\Rightarrow A^c>\theta\) | threshold-edge preservation margin | proved corollary | [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A^c>\theta\Rightarrow A^f>\theta\) | no threshold false positive under deterministic target coarse observation | proved by contraction | [P25](proposition_25_directed_influence_scale_certification.md) |

P25 is a physical scale theorem with dependency branch P11 + P18. It does not by itself establish scale stability of partition irreducibility, arbitrary source aggregation, changed intervention semantics, physical completeness, or experience.

---

# 20. P26 - partition-irreducibility scale certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_{\pi}^{u,\tau}=\bigotimes_{B\in\pi}P_B^{u,\tau}\) | partition-factorized reference law | P11 physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(\kappa_f^{u,\tau}(\pi)=\|P^{u,\tau}-P_{\pi}^{u,\tau}\|_{\mathrm{TV}}\) | fine partition irreducibility | P11 physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(C_\#P_{\pi}^{u,\tau}=\bigotimes_{B\in\pi}(C_B)_\#P_B^{u,\tau}\) | commutation of productization with block-compatible coarse observation | proved from product pushforward factorization | [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\kappa_c^{u,\tau}(\pi)\le\kappa_f^{u,\tau}(\pi)\) | coarse observation cannot increase declared partition irreducibility | proved by TV contraction | P17; [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi})\) | reconstruction-controlled partition-scale loss | proved by applying P18 to the response/product-law pair | [P18](proposition_18_scale_sufficiency_certification.md); [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\rho(P)=\rho(P_{\pi})=0\Rightarrow\kappa_c=\kappa_f\) | exact preservation on the declared two-law family | proved corollary | [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\kappa_f>\theta+\rho(P)+\rho(P_{\pi})\Rightarrow\kappa_c>\theta\) | threshold-preservation margin | proved corollary | [P26](proposition_26_partition_irreducibility_scale_certification.md) |

P26 is an observation-scale theorem for one declared partition. P27 supplies the missing node-aggregation transport criterion.

---

# 21. P27 - partition-lattice transport under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(a:V_f\twoheadrightarrow V_c\), \(F_c=a^{-1}(c)\) | declared surjective node aggregation and its fibers | repository definition | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(F_c\subseteq B\) for some \(B\in\pi_f\) for every \(c\) | aggregation-saturation criterion | necessary and sufficient for exact partition descent | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(L_a(\pi_c)=\{a^{-1}(C):C\in\pi_c\}\) | lifts coarse partitions to saturated fine partitions | repository construction | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(\operatorname{Part}(V_c)\simeq_{\mathrm{lattice}}\operatorname{Part}_{\mathrm{sat}}(V_f;a)\) | exact surviving partition-lattice correspondence | proved | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \((C_a)_\#P_{\pi_f}=((C_a)_\#P)_{\pi_c}\) | productization commutes with aggregation-compatible state mapping for descendable partitions | proved | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(\kappa_c(\pi_c)\le\kappa_f(L_a\pi_c)\) | node aggregation cannot increase corresponding partition irreducibility | proved by TV contraction | P17; [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f})\) | reconstruction-controlled irreducibility loss after node aggregation | proved by P18 applied to the response/product pair | P18; [P27](proposition_27_partition_lattice_node_aggregation.md) |

P27 distinguishes failure of partition semantics from loss of partition signal. P28 supplies the matched-intervention source-label transport needed for the directed-influence branch.

---

# 22. P28 - intervention compatibility under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(S_f(e)=\{i:e\in\mathcal E_i\}\) | fine source-incidence set of one matched intervention pair | repository definition | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(|\{a(i):i\in S_f(e)\}|\le1\) | exact compatibility criterion for unambiguous coarse source labeling | proved necessary and sufficient | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(\mathcal E_c^a=\bigcup_{i\in a^{-1}(c)}\mathcal E_i\) | canonical pooling of inherited matched comparisons | repository construction | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(P_{F_d}^{u,\tau}=\operatorname{Marg}_{F_d}P^{u,\tau}\) | complete fine response block represented by aggregate target \(d\) | repository construction from P11 marginalization | P11; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(A_{c\to d}^{c,a}\le A_{c\to d}^{f,a}\) | target aggregation cannot increase directed influence for the descended pair family | proved by TV contraction | P17, P25; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(0\le A_f-A_c\le2\rho_{c\to d}^{a}\) | reconstruction-controlled aggregate-node influence loss | proved by P18 applied pairwise before the supremum | P18, P25; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| aggregate source label \(\ne\) new aggregate actuator | prevents pair-family pooling from being misread as physical intervention synergy | interpretation boundary | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |

P28 is a theorem about declared intervention comparisons and target response blocks. P29 supplies the complete response-geometry transport statement on a fixed intervention-delay grid.

---

# 23. P29 - response-geometry transport under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(G_f(u,v,\tau)=\|P^{u,\tau}-P^{v,\tau}\|_{\mathrm{TV}}\) | fine P11 response-geometry entry | P11 definition applied to declared grid | P11; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\overline P^{u,\tau}=(C_a)_\#P^{u,\tau}\) | node-aggregated response law | repository construction using P27 aggregate-state map | P27; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(G_c(u,v,\tau)\le G_f(u,v,\tau)\) | entrywise geometry contraction | proved by TV data processing | P17; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(0\le G_f-G_c\le\rho_{u,\tau}+\rho_{v,\tau}\) | law-specific reconstruction-controlled geometry loss | proved by P18 | P18; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\rho_*=\sup_{u,\tau}\rho_{u,\tau}\) | uniform reconstruction defect on the declared experiment grid | repository definition | [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\|\mathcal G_f-\mathcal G_c\|_\infty\le2\rho_*\) | simultaneous distortion bound for the complete indexed geometry | proved | [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(0\le\Delta_f-\Delta_c\le2\rho_*\) | response-diameter corollary | proved | [P29](proposition_29_response_geometry_node_aggregation.md) |

P29 fixes intervention and delay semantics. It does not merge intervention labels, resample time, establish full P11 scale equivalence, physical completeness, or experience.

---

# 24. P30 full declared P11 scale compatibility

| Equation / statement | Role | Provenance | Audit path |
| --- | --- | --- | --- |
| \(\mathbf D_{P11}(a)=(D_G,D_A,D_K)\) | combines response-geometry, directed-influence, and partition distortions | repository definition | [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_G\le2\rho_G^*\) | complete response-geometry distortion control | P29 + P18 | [P29](proposition_29_response_geometry_node_aggregation.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_A\le2\rho_A^*\) | compatible directed-influence distortion control | P28/P25 + P18 | [P28](proposition_28_intervention_node_aggregation_compatibility.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_K\le\rho_P^*+\rho_\Pi^*\) | descendable partition-irreducibility distortion control | P27/P26 + P18 | [P27](proposition_27_partition_lattice_node_aggregation.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(\|\mathbf D_{P11}\|_\infty\le\max\{2\rho_G^*,2\rho_A^*,\rho_P^*+\rho_\Pi^*\}\) | simultaneous declared P11 scale certificate | proved assembly theorem | [P30](proposition_30_full_p11_scale_compatibility.md) |
| zero component distortion does not replace semantic compatibility | prevents incomparable scale constructions from being declared equivalent | repository no-semantic-compensation result | [P30](proposition_30_full_p11_scale_compatibility.md) |

P30 is a theorem about simultaneous transport of the declared P11 physical candidate. It does not establish consciousness, physical completeness, genuine node fusion, intervention quotienting, or time quotienting.

---

# 25. P31 intervention-quotient compatibility

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(b:\mathcal U_f\twoheadrightarrow\mathcal U_c\) | declared surjective quotient of operational intervention labels | repository definition | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(b(u)=b(v)\Rightarrow\overline P^{u,\tau}=\overline P^{v,\tau}\;\forall\tau\) | exact fiber-constancy condition | necessary and sufficient for unique response-law descent | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\eta_b=\sup_\tau\sup_{b(u)=b(v)}\|\overline P^{u,\tau}-\overline P^{v,\tau}\|_{\mathrm{TV}}\) | operational quotient ambiguity defect | repository definition | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\eta_b=0\iff\) exact intervention-quotient descent | exact quotient certificate | proved | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\sup_{c,\tau}\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}\le\eta_b\) | representative-selection stability | proved | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\sup_{c,d,\tau}|G_s-G_{s'}|\le2\eta_b\) | induced coarse response-geometry ambiguity | proved by reverse triangle inequality | [P31](proposition_31_intervention_quotient_compatibility.md) |
| same coarse intervention label \(\ne\) same physical actuator | prevents operational quotienting from being overinterpreted as mechanism identity | interpretation boundary | [P31](proposition_31_intervention_quotient_compatibility.md) |

P31 changes intervention labels only after a common response space is declared. It does not establish physical actuator identity, simultaneity, consciousness, or physical completeness. Delay/time quotienting remains a separate theorem burden.

---

# 26. P32-P37 operational-scale closure

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\eta_{a\times b}\le\eta_a+\eta_b\) | joint intervention-delay ambiguity budget | proved | [P33](proposition_33_joint_operational_quotient.md) |
| \(D_G^{\mathrm{full}}\le2\rho_G^*+2\eta_{a\times b}\) | complete geometry-scale bound | proved | [P34](proposition_34_joint_p11_operational_scale.md) |
| \(D_A^{\mathrm{full}}\le2\rho_A^*+2\eta_{a\times b}\) | complete directed-influence bound | proved | [P35](proposition_35_approximate_directed_influence_operational_quotient.md) |
| \(|\kappa_\pi(P)-\kappa_\pi(Q)|\le(m+1)\|P-Q\|_{\mathrm{TV}}\) | partition-product perturbation bound | proved | [P36](proposition_36_partition_irreducibility_operational_quotient.md) |
| complete P11 max-norm distortion budget | simultaneous G/A/K scale certificate | proved | [P37](proposition_37_complete_approximate_p11_operational_scale.md) |

---

# 27. P38 quantum operational sufficiency

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(x\mapsto\rho_x\in\mathcal D(\mathcal H)\) | declared finite-dimensional quantum operational descriptor | repository specialization of standard density-operator formalism | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(\rho_x=\rho_{x'}\Rightarrow y(x)=y(x')\) | deterministic quantum sufficiency criterion | necessary and sufficient for factorization through the declared descriptor | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(I(Y;X\mid\rho_X)=0\) | stochastic quantum sufficiency criterion | population criterion | [P38](proposition_38_quantum_operational_sufficiency.md) |
| \(\rho_x=\rho_{x'}\) but \(y(x)\ne y(x')\) | exact descriptor-relative non-factorization witness | proved sufficient | [P38](proposition_38_quantum_operational_sufficiency.md) |

---

# 28. P39 finite-data quantum model-set non-factorization

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q\) | tomography model-set coverage assumption | declared input | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(L_{xx'}=[\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}-\varepsilon_x-\varepsilon_{x'}]_+\) | lower confidence bound on true target-law separation | proved by triangle inequality | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V(h)=\max_{q_h(x)=q_h(x')}L_{xx'}\) | model-specific P38 violation margin | repository definition | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V_*=\min_{h\in\mathcal C_Q}V(h)\) | worst surviving quantum-model margin | repository definition | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| \(V_*>0\Rightarrow\) P38 non-factorization for the true declared model with confidence \(\ge1-\alpha_Q-\alpha_Y\) | finite-data robust model-set theorem | proved by simultaneous target bound plus union bound | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |
| small trace distance \(\not\Rightarrow\) exact state equality | blocks false collision certificates from noisy tomography | mathematical boundary | [P39](proposition_39_finite_data_quantum_nonfactorization.md) |

P39 rejects only the declared quantum confidence set as sufficient for the independently defined target. It does not establish that quantum mechanics is incomplete or that the target is nonphysical.

---

# 29. P40 continuous quantum-region regularity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| injective \(Q\) on finite \(\mathcal X\Rightarrow y=g\circ Q\) for arbitrary \(y\) | unrestricted-factorization no-go | proved by defining \(g\) on the finite image | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}\le\omega(D(\rho,\sigma))\) | declared bridge regularity class | explicit additional assumption | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(U_{xx'}=\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q)\) | worst allowed quantum separation over the continuous confidence region | repository definition | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(M_{xx'}=L_{xx'}-\omega(U_{xx'})\) | pairwise regularity obstruction margin | repository definition | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(M_*>0\) | robust incompatibility of the whole region with the declared bridge class | proved | [P40](proposition_40_continuous_quantum_region_regularity.md) |
| \(\omega(r)=Lr\) | Lipschitz special case | standard regularity model specialized here | [P40](proposition_40_continuous_quantum_region_regularity.md) |

P40 does not infer bridge regularity from quantum mechanics. The modulus is an independently declared model restriction.

---

# 30. P41 trace-ball quantum envelope

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D(\rho_x,\rho_{x'})\le D(\widehat\rho_x,\widehat\rho_{x'})+r_x+r_{x'}\) | true quantum pairwise distance control from simultaneous trace balls | standard triangle inequality applied here | standard trace distance; [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(U^{\mathrm{ball}}_{xx'}=\min\{1,\widehat D^Q_{xx'}+r_x+r_{x'}\}\) | analytic outer bound on the P40 confidence-region envelope | repository construction | [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(L^{\mathrm{ball}}_{xx'}=[\widehat D^Y_{xx'}-\varepsilon_x-\varepsilon_{x'}]_+\) | target-law lower confidence separation | triangle inequality | [P39](proposition_39_finite_data_quantum_nonfactorization.md); [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(L^{\mathrm{ball}}_{xx'}>\omega(U^{\mathrm{ball}}_{xx'})\) | end-to-end continuous-region regularity obstruction | proved | [P40](proposition_40_continuous_quantum_region_regularity.md); [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(M^{\mathrm{ball}}=L^{\mathrm{ball}}-LU^{\mathrm{ball}}\) | Lipschitz obstruction margin | repository definition | [P41](proposition_41_trace_ball_quantum_envelope.md) |
| \(d_Y-Ld_Q>2\varepsilon+2Lr\) | symmetric unsaturated experimental design condition | derived sufficient inequality | [P41](proposition_41_trace_ball_quantum_envelope.md) |

P41 assumes valid simultaneous confidence balls. It does not itself derive their statistical radii.

---

# 31. P42 quantum regular-bridge sample complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\frac12\|R(v)\|_1\le\kappa_R\|v\|_1\) | conditioning bound for the declared linear IC reconstruction | declared tomography-design assumption | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(t_Q=\sqrt{\log(2Km/\alpha_Q)/(2n_Q)}\) | simultaneous coordinate-frequency radius over the IC experiment | Hoeffding plus union bound | standard concentration; [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(r_Q=\kappa_Rmt_Q\) | simultaneous raw-reconstruction half-trace-norm radius | proved from reconstruction stability and the frequency bound | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\varepsilon_Y=\frac{k}{2}\sqrt{\log(2Kk/\alpha_Y)/(2n_Y)}\) | simultaneous categorical target-TV radius | Hoeffding plus union bound | standard concentration; [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\Delta=d_Y-Ld_Q\) | population regularity gap for one preparation pair | repository design quantity | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(\widehat M\ge\Delta-4\varepsilon_Y-4Lr_Q\) | finite-data lower bound on the empirical P41 obstruction margin | proved | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(n_Y\ge2k^2\log(2Kk/\alpha_Y)/(\lambda^2\Delta^2)\) | sufficient target samples per preparation | proved by uncertainty-budget allocation | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |
| \(n_Q\ge8L^2\kappa_R^2m^2\log(2Km/\alpha_Q)/((1-\lambda)^2\Delta^2)\) | sufficient quantum samples per preparation | proved by uncertainty-budget allocation | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) |

P42 uses a fixed informationally complete measurement, a declared linear reconstruction stability constant, and IID categorical sampling. The coordinate Hoeffding construction is conservative. The raw linear reconstruction need not be a physical density operator. The theorem does not establish quantum incompleteness or consciousness.

---

# 32. P43 optimal quantum-target uncertainty allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C(\lambda)=c_YA_Y/\lambda^2+c_QA_Q/(1-\lambda)^2\) | weighted P42 sampling cost | repository design objective | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C''(\lambda)>0\) on \((0,1)\) | strict convexity and uniqueness of the optimizer | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(\lambda_*=(c_YA_Y)^{1/3}/[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}]\) | exact optimal target-side gap fraction | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C_*=[(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}]^3\) | exact minimum continuous weighted cost | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(C_*\le C_{int}\le C_*+c_Y+c_Q\) | sufficient integer-rounding overhead bound | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |
| \(1\le C_{1/2}/C_*\le4\) | universal balanced-allocation approximation bound | proved | [P43](proposition_43_optimal_quantum_target_allocation.md) |

P43 optimizes a declared P42 resource objective with design weights fixed before data collection. It does not add evidence for physical completeness, quantum incompleteness, or consciousness.

---

# 33. P44 pair-adaptive finite-family certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(M_j=d_{Y,j}-L_jd_{Q,j}\) | candidate population regularity margin | repository design quantity | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\sum_j\alpha_{Q,j}\le\alpha_Q,\ \sum_j\alpha_{Y,j}\le\alpha_Y\) | predeclared family failure-budget constraint | declared statistical design condition | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\Pr(\underline M_j\le M_j\ \forall j)\ge1-\alpha_Q-\alpha_Y\) | simultaneous finite-family lower-margin coverage | union bound | standard probability; [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\underline M_{\widehat j}>0\Rightarrow M_{\widehat j}>0\) | post-selection validity for any measurable selector in the predeclared family | proved | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| weighted alpha spending | allocates family confidence before viewing certification data | proved to preserve family budget | [P44](proposition_44_pair_adaptive_sample_allocation.md) |

P44 is a finite-family statistical theorem. It does not establish physical completeness, quantum incompleteness, or consciousness.

---

# 34. P45 shared-preparation graph allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Delta_e=d_{Y,e}-L_ed_{Q,e}\) | candidate edge population regularity gap | repository design quantity | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(2(\varepsilon_i+\varepsilon_j)+2L_e(r_i+r_j)\le\Delta_e\) | preparation-specific sufficient edge budget | nonuniform extension of the P42 power bound | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md); [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(C=\sum_iw_{Y,i}/\varepsilon_i^2+\sum_iw_{Q,i}/r_i^2\) | shared preparation-level weighted sampling cost | repository design objective | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(w_{Y,i}/\varepsilon_i^3=\sum_{e\ni i}\lambda_e\) | target-side KKT incidence law | proved | convex KKT conditions applied in [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(w_{Q,i}/r_i^3=\sum_{e\ni i}\lambda_eL_e\) | quantum-side KKT incidence law | proved | convex KKT conditions applied in [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(C_e^*=S_e^3/\Delta_e^2\) | exact single-edge minimum cost | proved by strict convexity and stationarity | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| ceiling continuous sample counts preserves edge feasibility | conservative integer conversion | monotonicity of \(a/\sqrt n\) | [P45](proposition_45_shared_preparation_graph_allocation.md) |

P45 is a resource-allocation theorem for a declared statistical design. It does not establish physical completeness, quantum incompleteness, or consciousness.

---

# 35. Candidate consciousness-theory feature families

The following are source-grounded translations into generic feature notation. They are not claims that each named theory reduces to one scalar or one universally agreed implementation.

| Theory family | Generic feature notation in this repository | Primary source role |
| --- | --- | --- |
| IIT 4.0 | \(\mathcal F_{\mathrm{IIT}}(p)=\) intrinsic cause-effect structure and maximal-substrate organization | Albantakis et al. 2023 |
| GNWT | \(\mathcal F_{\mathrm{GNW}}(p)=\) multilevel workspace organization, ignition, and global availability | Dehaene-Changeux 2011; Mashour et al. 2020; Changeux-Farisco 2026 |
| RPT | \(\mathcal F_{\mathrm{RPT}}(p)=\) relevant recurrent-processing structure and dynamics | Lamme 2006 |
| HOT | \(\mathcal F_{\mathrm{HOT}}(p)=\) theory-specific higher-order representational relation | Brown-Lau-LeDoux 2019 |
| predictive / NR / active-inference families | \(\mathcal F_{\mathrm{PP}}(p)=\) theory-specific predictive, inferential, and representational structure | Seth-Hohwy 2021; Pennartz 2022; Corcoran et al. 2026 |
| intervention-resolved causal structure | \(F_{\mathrm{causal}}(p)=[\mathfrak C_p]_{\cong}\) | repository-original candidate physical signature; temporal, finite-error, and composition extensions remain physical | P11-P16 |

Detailed caveats and source roles are maintained in [Candidate Theory Families](candidate_theory_families.md) and [Literature Map](literature_map.md).

---

# 36. Citation discipline

A result is cited as a repository result when the bridge-specific statement, construction, or counterexample is introduced here.

External literature is cited only for the conceptual, mathematical, statistical, physical, or empirical role it supplies.

The project maintains the distinction

\[
\boxed{
\text{definition}
\neq
\text{bridge axiom}
\neq
\text{candidate physical signature}
\neq
\text{theorem}
\neq
\text{empirical evidence}.
}
\]

This distinction is central to the final proof target: mathematics establishes what follows from premises, while the physical-to-experiential premises themselves require independently discriminating evidence.

---

# 35. P46 budget-constrained witness graph

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(F(S)=\sum_{\{i,j\}\in E}w_{ij}\mathbf 1\{i,j\in S\}\) | total value of candidate witness edges induced by measured preparations | repository definition | [P46](proposition_46_budget_constrained_witness_graph.md) |
| monotonicity and supermodularity of \(F\) | formalizes preparation complementarity | proved from nonnegative edge weights | [P46](proposition_46_budget_constrained_witness_graph.md) |
| unit-cost, unit-weight threshold \(\binom{k}{2}\) | reduction from CLIQUE | proves NP-hardness of optimization and NP-completeness of decision form | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(2F(S)\le\sum_{i\in S}d_i\) | weighted-degree relaxation | proved by comparing internal and full weighted degrees | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(F^*(B)\le U_{\rm deg}(B)\) | fractional degree-knapsack upper bound | proved relaxation bound | [P46](proposition_46_budget_constrained_witness_graph.md) |
| \(F^*(B)-F(S)\le U_{\rm deg}(B)-F(S)\) | a posteriori optimality-gap certificate | proved | [P46](proposition_46_budget_constrained_witness_graph.md) |

P46 is a combinatorial experimental-design result. Its graph weights are declared design values, not consciousness scores or evidence of quantum incompleteness.

---

# 36. P47 anytime-valid sequential witness graph

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\mathcal E_*=\bigcap_i(\mathcal E_{Y,i}\cap\mathcal E_{Q,i})\) | one event covering every declared preparation stream and every local sample size | repository definition | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\Pr(\mathcal E_*)\ge1-\alpha_Y-\alpha_Q\) | finite-family simultaneous coverage | proved by union bound from preparation-level confidence sequences | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(N_{Y,i}(t),N_{Q,i}(t)\) | history-dependent local sample counts | adaptive design object | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\underline M_e(t)\le M_e\le\overline M_e(t)\) | simultaneous regularity-margin envelope for every declared edge and global time | proved from metric triangle inequalities on \(\mathcal E_*\) | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\underline M_{\widehat e_\tau}(\tau)>0\Rightarrow M_{\widehat e_\tau}>0\) | selected-edge stopping-time certificate | proved from the simultaneous event | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\overline M_e(t)<0\) | safe edge elimination criterion | proved from simultaneous upper coverage | [P47](proposition_47_anytime_sequential_witness_graph.md) |

P47 is a time-uniform statistical and experimental-design result. It does not convert a regularity obstruction into an ontological or experiential conclusion.

---

# 37. P48 gap-dependent stopping complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(g_e=|M_e|\) | population sign gap for a declared regularity witness | repository definition | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(U_e(n)\le A_e\sqrt{\log(B_e n^2)/n}\) | common edge-level uncertainty envelope from target and quantum endpoint radii | proved envelope reduction | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(\underline M_e\ge M_e-2U_e\), \(\overline M_e\le M_e+2U_e\) | deterministic sign-certification perturbation bounds | proved from P47 interval geometry | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(N_e=\lceil4Q_e\log(4Q_e\sqrt{B_e})\rceil\) | explicit sufficient local count for every nonzero margin | proved elementary inversion bound | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(K_+=\min_{M_e>0}N_e\) | positive-witness stopping-epoch upper bound | proved on the P47 simultaneous event | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(K_-=\max_eN_e\) when all \(M_e<0\) | all-negative stopping-epoch upper bound | proved on the P47 simultaneous event | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(C_{\rm active}(K)\le C_{\rm full}(K)\) | safe-pruning acquisition-cost comparison | proved by active-set inclusion | [P48](proposition_48_gap_dependent_stopping_complexity.md) |

P48 is a sufficient sequential upper bound. It is not a minimax lower bound or an adaptive-optimality theorem.

---

# 38. P49 dyadic certification schedules

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(D(N)=2^{\lceil\log_2N\rceil}\) | first dyadic checkpoint at or above a finite P48 threshold | repository definition | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(N\le D(N)<2N\) | exact sample-threshold overhead bound | proved integer scheduling theorem | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(L(N)=\lceil\log_2N\rceil+1\) | complete certification-look count through the dyadic threshold | proved counting identity | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(\widetilde K_+=D(K_+)<2K_+\) | positive-witness dyadic stopping bound | proved from P48 plus monotonicity of \(D\) | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(\widetilde K_-=D(K_-)<2K_-\) | all-negative dyadic stopping bound | proved from P48 plus monotonicity of \(D\) | [P49](proposition_49_dyadic_stopping_overhead.md) |
| \(C_{\rm dyad}(K)<2C_{\rm full}(K)\) | linear acquisition-cost overhead | proved by multiplying the dyadic epoch inequality by positive per-epoch cost | [P49](proposition_49_dyadic_stopping_overhead.md) |

P49 changes checkpoint frequency only. Statistical validity remains inherited from P47 and finite sign separation remains inherited from P48.

---

# 39. P50 bounded-starvation asynchronous sampling

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(H\)-fairness | every continuously active preparation receives service in each H-round window | repository definition | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(N_i(T)\ge\lfloor T/H\rfloor\) | deterministic local-count growth from bounded starvation | proved block-counting lemma | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(\tau_{+,H}\le HK_+\) | positive-witness global-round stopping bound | proved from P47 positive-edge persistence, P48 threshold, and H-fairness | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(\tau_{0,H}\le HK_-\) | all-negative global-round stopping bound | proved from P48 edge elimination and H-fairness | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| unrestricted starvation counterexample | demonstrates that P47 validity alone gives no finite global-time progress bound | proved impossibility construction | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(H D(N_e)<2HN_e\) | P49 dyadic batching composed with P50 asynchronous fairness | proved composition bound | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |

P50 is a progress/scheduling theorem. It does not alter the scientific meaning of the underlying regularity margin.

---

# 40. P51 heterogeneous finite-window service-rate stopping

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \((W_i,q_i)\) | preparation-specific finite-window service guarantee | repository definition | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(N_i(T)\ge q_i\lfloor T/W_i\rfloor\) | finite-time local-count growth | proved block-counting theorem | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_i(N)=W_i\lceil N/q_i\rceil\) | sufficient global rounds for endpoint local threshold | proved inversion of the service bound | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_e=\max\{T_i(N_e),T_j(N_e)\}\) | edge service bottleneck | proved endpoint assembly | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_+=\min_{M_e>0}T_e\) | positive-witness global stopping bound | proved from P47-P48 plus P51 service | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |
| \(T_-=\max_eT_e\) | all-negative global stopping bound | proved from P47-P48 plus P51 service | [P51](proposition_51_heterogeneous_service_rate_stopping.md) |

---

# 41. P52 capacity-optimal service allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(d_i=\max\{N_e:e\ni i\}\) | componentwise-minimal vertex demand sufficient for all incident P48 thresholds | proved threshold reduction | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T(\pi)=\max_i d_i/\pi_i\) | continuous capacity-constrained threshold makespan | repository optimization definition | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T\ge(\sum_i d_i)/C\) | universal capacity lower bound | proved by summing \(d_i\le T\pi_i\) | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(\pi_i^*=C d_i/\sum_jd_j\) | unique minimax service allocation on positive demand support | proved exact optimum | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T^*=(\sum_i d_i)/C\) | exact optimal continuous completion time | proved by lower-bound attainment | [P52](proposition_52_capacity_optimal_service_allocation.md) |
| \(T_{\rm discrete}^*=\sum_i d_i\) for unit capacity | exact integer quota-saturation length | proved counting lower bound plus construction | [P52](proposition_52_capacity_optimal_service_allocation.md) |

P52 optimizes deterministic saturation of declared sufficient thresholds; it is not an information-theoretic lower bound on the underlying statistical problem.

---

# 42. P53 residual-demand reoptimization

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(r_i(t)=\max_{e\in E_t:e\ni i}(N_e-n_i(t))_+\) | componentwise-minimal current vertex demand | proved residual reduction | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(R(t)=\sum_i r_i(t)\) | total residual threshold burden | repository definition | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(T_{\rm rem}^*(t)=R(t)/C\) | exact optimal remaining deterministic completion time | P52 applied to residual demands | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(E_b\subseteq E_a,\ n_i(b)\ge n_i(a)\Rightarrow r_i(b)\le r_i(a)\) | residual monotonicity under sampling and safe pruning | proved max-envelope monotonicity | [P53](proposition_53_residual_demand_reoptimization.md) |
| \(T_{\rm rem}^*(a)-T_{\rm rem}^*(b)=[R(a)-R(b)]/C\) | exact released optimal time | proved identity | [P53](proposition_53_residual_demand_reoptimization.md) |

P53 quantifies deterministic threshold burden after valid pruning; it does not itself justify the statistical pruning decision.

---

# 43. P54 metric switching-cost residual scheduling

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(C_{\rm total}(\sigma)=a\sum_i r_i+C_{\rm sw}(\sigma)\) | deterministic acquisition and switching-cost decomposition | repository scheduling definition | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(C_{\rm sw}(\bar\sigma)\le C_{\rm sw}(\sigma)\) | first-visit metric batching inequality | proved by repeated triangle inequality | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(C_{\rm total}^*=a\sum_i r_i+L^*(V_+;s)\) | exact optimum after batching | proved Hamiltonian-path reduction | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |
| \(D(S,j)=\min_{k\in S\setminus\{j\}}[D(S\setminus\{j\},k)+c(k,j)]\) | exact finite-instance Held-Karp recurrence | standard subset-DP construction applied here | [P54](proposition_54_metric_switching_cost_residual_scheduling.md) |

The metric assumption is structural: without triangle inequality the batching inequality and Hamiltonian-path reduction need not hold.

---

# 44. P55 pruning-aware metric switching-cost monotonicity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(S(r')\subseteq S(r)\) for \(r'\le r\) | support nesting under componentwise residual decrease | immediate consequence | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(L^*(S(r');s)\le L^*(S(r);s)\) | optimal metric route monotonicity under support deletion | proved by shortcutting | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(C^*(r;s)-C^*(r';s)=a(\sum r_i-\sum r_i')+[L^*(S(r);s)-L^*(S(r');s)]\) | exact deterministic optimal cost-release decomposition | proved by P54 subtraction plus route monotonicity | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(0\le\Delta_{\rm shortcut}\le L^*(S(r);s)-L^*(S(r');s)\) | computable lower certificate on route release | proved from retained old optimal route | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |

P55 compares states under one fixed metric and fixed start/setup state. A moving start requires a separate stability theorem.

---

# 45. P56 moving-start metric reoptimization stability

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(|L^*(S;s)-L^*(S;s')|\le c(s,s')\) | start-state perturbation of the optimal P54 route | proved sharp 1-Lipschitz theorem | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(|C^*(r;s)-C^*(r;s')|\le c(s,s')\) | fixed-residual total-cost start stability | immediate from P56 route theorem | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(C^*(r;s)-C^*(r';s')\ge\Delta_{\rm fixed}-c(s,s')\) | residual decrease with moving setup origin | proved P55-P56 perturbation bound | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(\Delta_{\rm fixed}>c(s,s')\) | sufficient strict-decrease condition | proved consequence | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |

P56 assumes the metric itself is unchanged. Time-varying switching geometry requires a separate perturbation analysis.

---

# 46. P57 switching-metric perturbation stability

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\delta=\max_{x,y}|c(x,y)-c'(x,y)|\) | common-point sup distance between two declared finite switching metrics | repository definition | [P57](proposition_57_switching_metric_perturbation.md) |
| \(q(S;s)\in\{|S|-1,|S|\}\) | exact maximum number of nontrivial metric edges required by the rooted P54 route | repository definition with metric shortcut justification | [P57](proposition_57_switching_metric_perturbation.md) |
| \(|L_c^*(S;s)-L_{c'}^*(S;s)|\le q(S;s)\delta\) | stability of the exact switching optimum under metric drift | proved sharp perturbation theorem | [P57](proposition_57_switching_metric_perturbation.md) |
| \(P_{57}=\min\{c(s,s')+q(S';s')\delta,\ q(S';s)\delta+c'(s,s')\}\) | combined start-motion and metric-drift penalty | proved by two valid perturbation orders | [P57](proposition_57_switching_metric_perturbation.md) |
| \(C_c^*(r;s)-C_{c'}^*(r';s')\ge\Delta_{\rm fixed}-P_{57}\) | full residual/start/metric reoptimization lower bound | proved P55-P56-P57 composition | [P57](proposition_57_switching_metric_perturbation.md) |
| \(L_{c'}^*(S;s')\le\ell_{c'}(\pi_c^*;s')\) | old-optimal-route reuse certificate under the new geometry | proved feasibility upper bound | [P57](proposition_57_switching_metric_perturbation.md) |

P57 is a deterministic experimental-scheduling robustness theorem. Uncertain or statistically estimated switching metrics require a separate confidence-set analysis.

---

# 47. P58 finite-data switching-metric uncertainty

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\rho_e=B_e\sqrt{\log(2/\alpha_e)/(2n_e)}\) | two-sided bounded-mean transition-cost confidence radius | standard Hoeffding consequence under declared pairwise sampling assumptions | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\Pr(|\widehat c_e-c_e|\le\rho_e\ \forall e)\ge1-\alpha\) | simultaneous finite transition-family coverage | finite-family union-bound theorem | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\underline c_e=\max\{0,\widehat c_e-\rho_e\},\ \overline c_e=\widehat c_e+\rho_e\) | rectangular pairwise transition envelope | repository definition | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(L^-=\min_\pi\underline\ell(\pi;s),\ L^+=\min_\pi\overline\ell(\pi;s)\) | exact lower and upper route-envelope optima | repository definition plus Held-Karp computation | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(L^-\le L_c^*\le L^+\) | finite-data confidence bracket for the unknown true P54 switching optimum | proved confidence-envelope theorem | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(\ell_c(\pi^{\rm rob};s)-L_c^*\le L^+-L^-\) | robust-route regret certificate | proved deterministic consequence on the shared confidence event | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(C_0^->C_1^+\Rightarrow C_{c_0}^*>C_{c_1}^*\) | robust strict reoptimization comparison | proved interval-separation certificate | [P58](proposition_58_finite_data_metric_uncertainty.md) |
| \(n\ge 2B^2q_{\rm rect}^2\varepsilon^{-2}\log(2M/\alpha)\) | sufficient common pairwise calibration count for route-envelope width at most \(\varepsilon\) | derived sufficient design inequality, not minimax | [P58](proposition_58_finite_data_metric_uncertainty.md) |

P58 assumes an unknown true metric and a valid finite-data observation model. The empirical center itself need not satisfy the triangle inequality.

---

# P59 optimal transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\rho_e(n_e)=a_e/\sqrt{n_e}\) | declared inverse-square-root transition-calibration uncertainty model | repository design model, with Hoeffding coefficient available from P58 | [P58](proposition_58_finite_data_metric_uncertainty.md), [P59](proposition_59_optimal_transition_calibration.md) |
| \(U(n)=\sum_e w_ea_e/\sqrt{n_e}\) | weighted route-uncertainty surrogate under edge-specific calibration effort | repository definition | [P59](proposition_59_optimal_transition_calibration.md) |
| \(n_e^*=N(w_ea_e)^{2/3}/\sum_j(w_ja_j)^{2/3}\) | unique minimum-uncertainty continuous allocation | proved by strict convexity and KKT conditions | [P59](proposition_59_optimal_transition_calibration.md) |
| \(U^*(N)=S^{3/2}/\sqrt N\) | exact minimum value of the declared surrogate | proved by substitution at the unique optimum | [P59](proposition_59_optimal_transition_calibration.md) |
| \(N\ge S^3/\varepsilon^2\) | exact continuous budget threshold for target surrogate uncertainty \(\varepsilon\) | algebraic consequence of the optimum | [P59](proposition_59_optimal_transition_calibration.md) |

P59 is an exact resource-allocation result for a declared convex uncertainty surrogate. It does not establish optimality for the full combinatorial robust-routing design problem.

---

# P60 integer transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(N_0=B-m\) | effective continuous budget after reserving one possible rounding unit per calibrated edge | repository construction | [P60](proposition_60_integer_transition_calibration.md) |
| \(k_e=\lceil n_e^*(B-m)\rceil\) | implementable integer calibration allocation | repository construction | [P60](proposition_60_integer_transition_calibration.md) |
| \(\sum_e k_e\le B\) | hard-budget feasibility guarantee | proved by the ceiling inequality | [P60](proposition_60_integer_transition_calibration.md) |
| \(U(k)\le U^*(B-m)\) | integer uncertainty guarantee | proved by coordinatewise monotonicity of the P59 surrogate | [P60](proposition_60_integer_transition_calibration.md) |
| \(U(k)/U^*(B)\le\sqrt{B/(B-m)}\) | multiplicative implementation overhead relative to the full-budget continuous optimum | proved P59-P60 comparison | [P60](proposition_60_integer_transition_calibration.md) |
| \(B\ge m+\lceil S^3/\varepsilon^2\rceil\) | sufficient hard integer budget for target uncertainty \(\varepsilon\) | proved algebraic consequence | [P60](proposition_60_integer_transition_calibration.md) |

P60 proves a closed-form feasible integer construction and an overhead bound. It does not claim exact discrete optimality.

---

# 50. P61 exact integer transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(U(k)=\sum_e b_e/\sqrt{k_e}\) with integer \(k_e\ge1\) | hard-budget whole-measurement version of the P59 separable uncertainty surrogate | repository definition | [P61](proposition_61_exact_integer_transition_calibration.md) |
| \(\Delta_e(k)=b_e(k^{-1/2}-(k+1)^{-1/2})\) | marginal uncertainty reduction from one additional calibration measurement | repository definition | [P61](proposition_61_exact_integer_transition_calibration.md) |
| \(\Delta_e(k+1)<\Delta_e(k)\) | strict diminishing marginal gain on each calibrated edge | proved discrete-convexity property | [P61](proposition_61_exact_integer_transition_calibration.md) |
| largest-current-\(\Delta\) allocation rule | exact integer optimizer under \(\sum_e k_e=B\) | proved by prefix representation and exchange argument | [P61](proposition_61_exact_integer_transition_calibration.md) |
| selected/unselected marginal exchange condition | directly checkable certificate of discrete optimality | proved optimality condition | [P61](proposition_61_exact_integer_transition_calibration.md) |

P61 exactness applies to the declared unit-cost separable calibration surrogate. It is not a proof that the full robust-routing experiment-design problem is greedy-solvable.

