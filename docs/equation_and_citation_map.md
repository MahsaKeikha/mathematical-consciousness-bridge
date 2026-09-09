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

# 15. Candidate consciousness-theory feature families

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

# 16. Citation discipline

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
