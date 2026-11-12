# Thirty milestones for Quantum Impurity Feedback

This map connects one measured impurity charge to the complete computational statement: a quantum algorithm with a paid feedback loop, a substantial classical easy regime, and qualified hardness for programmable interacting inputs. Its thirty stable IDs describe the scientific understanding needed to read that statement as a whole.

The single educational anchor is **Lin Lin, [Lecture Notes on Quantum Algorithms for Scientific Computation, arXiv:2201.08309v1 (2022)][lin]**. Section numbers below refer to that version. The [bridge](BRIDGE.md) translates its notation and supplies the connections that its quantum-algorithm foundations do not cover. Canonical claims and research-level proof dependencies remain in the linked scientific pages and their references.

## Allocation and route

**Background/preliminaries has 14 milestones, M01–M14.** This project joins four languages: quantum states and fermionic charge, coherent circuit access and measurement, finite resource accounting, and stable mean-field approximation. The phase moves from individual states and observables to the full output contract and its competing computational routes.

**Narrative/innovation has 16 milestones, M15–M30.** Seven milestones build and price the reconstruction, three establish the classical boundary, four separate the two hardness arguments and their physical assumptions, and two integrate the evidence and conclusion. Each component has a distinct job; the final milestones put their consequences together. This is a map of the load-bearing ideas, rather than an inventory of every lemma or a requirement to read the anchor in full.

| ID | Phase | Central understanding target |
|---|---|---|
| [M01](#m01) | Background/preliminaries | A bounded observable under unitary evolution |
| [M02](#m02) | Background/preliminaries | A local expectation inside a correlated state |
| [M03](#m03) | Background/preliminaries | Fermionic occupation, qubit encoding and the prepared input |
| [M04](#m04) | Background/preliminaries | The distinction between quadratic and interacting dynamics |
| [M05](#m05) | Background/preliminaries | Known preparation, inverse access and replay |
| [M06](#m06) | Background/preliminaries | A scalar output with separate error and confidence |
| [M07](#m07) | Background/preliminaries | Coherent amplitude estimation and its access requirements |
| [M08](#m08) | Background/preliminaries | Explicit input cost versus an oracle query count |
| [M09](#m09) | Background/preliminaries | Hamiltonian normalization and constructible matrix access |
| [M10](#m10) | Background/preliminaries | Finite tables, arithmetic and a finite gate program |
| [M11](#m11) | Background/preliminaries | Unitary perturbation bounds and time-dependent simulation |
| [M12](#m12) | Background/preliminaries | What the Hartree closure approximates |
| [M13](#m13) | Background/preliminaries | Function approximation and stable self-consistency |
| [M14](#m14) | Background/preliminaries | The complete task and the two actions |
| [M15](#m15) | Narrative/innovation | Analyticity of the exact local mean |
| [M16](#m16) | Narrative/innovation | Contraction of a finite collocation map |
| [M17](#m17) | Narrative/innovation | Noisy values and stored coefficients with separate budgets |
| [M18](#m18) | Narrative/innovation | Global error from physically consistent prefixes |
| [M19](#m19) | Narrative/innovation | Joint reconstruction parameters and final accuracy |
| [M20](#m20) | Narrative/innovation | The complete circuit for one nodal response |
| [M21](#m21) | Narrative/innovation | The full quantum, classical and storage cost |
| [M22](#m22) | Narrative/innovation | Exact classical shortcuts that an advantage must survive |
| [M23](#m23) | Narrative/innovation | A classical response estimator controlled by impurity action |
| [M24](#m24) | Narrative/innovation | The full-task classical easy regime |
| [M25](#m25) | Narrative/innovation | The inherited computational power of an interacting impurity |
| [M26](#m26) | Narrative/innovation | Causal cancellation and the adaptive hardness reduction |
| [M27](#m27) | Narrative/innovation | An exactly soluble, measurably active nonlinear probe |
| [M28](#m28) | Narrative/innovation | The source-free direct hardness statement and its controls |
| [M29](#m29) | Narrative/innovation | What is proved, imported, checked and inherited |
| [M30](#m30) | Narrative/innovation | The conditional advantage and its remaining physical limits |

## Phase I: background/preliminaries

### M01

**States, bounded observables and unitary evolution**

- **Central question:** What mathematical objects determine the mean of a charge measurement at one time?
- **Understanding target:** Relate a normalized state, a Hermitian Hamiltonian, its unitary propagator and a bounded observable. For an observable with norm one, explain why its expectation lies in $[-1,1]$, while the state itself can require exponentially many classical amplitudes.
- **Dependencies and story role:** No earlier milestone. This supplies the local objects from which the entire task is assembled.
- **Conceptual connection:** The algorithm ultimately returns an expectation value. The size of the state representation alone does not determine the difficulty of that output.
- **Sources:** [Lin §§1.1 and 1.3][lin]; [model, §1](../science/model.md#1-input-evolution-and-output); [bridge, §1](BRIDGE.md#1-a-charge-measurement-with-an-unknown-field).

### M02

**A local expectation inside a correlated state**

- **Central question:** How can one local charge depend on correlations with an arbitrarily large bath?
- **Understanding target:** Use a positive, trace-one density operator to describe pure or mixed states, and distinguish a local reduced state from the full impurity–bath state. The charge is local, but its future evolution need not close on that charge or on the impurity's reduced state.
- **Dependencies and story role:** M01. This extends the single-state picture to the correlated subsystem that the scientific model retains.
- **Conceptual connection:** Trace normalization and operator norms provide dimension-independent expectation bounds. They do not grant a small classical representation of all correlations.
- **Sources:** [Lin §§1.2 and 1.5][lin]; [model, §§1–2](../science/model.md#1-input-evolution-and-output); [spectral reconstruction, proof part 1](../science/spectral-reconstruction.md#proof-part-1-physical-existence-and-dimension-independent-analyticity).

### M03

**Fermionic charge and the input state**

- **Central question:** What does the measured qubit represent in the fermionic problem?
- **Understanding target:** Connect a mode's occupation $n_u=a_u^\dagger a_u$ with the centered observable $A=1-2n_u=Z_u$ after the fixed Jordan–Wigner encoding. Distinguish a readily prepared Fock product input from an unknown interacting equilibrium state, and retain the cost of fermionic strings in later circuits.
- **Dependencies and story role:** M01–M02. This identifies the physical observable, its normalization and the actual initial-state access.
- **Conceptual connection:** The occupation output is $(1-m)/2$. Changing to an uncentered convention also changes the Hamiltonian coefficients; it is not only a relabeling of the final number.
- **Sources:** [Lin §4.1, Example 4.2, and §1.3][lin] for fermionic encoding and circuits; [model, §§1–2](../science/model.md#1-input-evolution-and-output). The ground-state estimation task surrounding Lin's example is separate from this transient-response task.

### M04

**Quadratic dynamics and a genuine interaction**

- **Central question:** Why does an exponentially large fermionic Hilbert space sometimes have a small classical description?
- **Understanding target:** Distinguish quadratic Hamiltonians, whose Gaussian evolution closes on one-body data, from a quartic impurity interaction that can destroy that closure. Understand why fixed impurity support does not bound the correlations generated throughout a growing bath.
- **Dependencies and story role:** M02–M03. This introduces the structural distinction that makes both the classical comparison and the hard family meaningful.
- **Conceptual connection:** A large bath is insufficient evidence for advantage. The later comparison must track how much non-Gaussian interaction is used, as well as how many modes are present.
- **Sources:** [Lin §4.1, Example 4.2][lin] for second-quantized Hamiltonians; [model, §§2–3](../science/model.md#2-the-impurity-specialization); [classical boundary, §§1–2](../science/classical-boundary.md#1-the-input-subclass). Gaussian closure is supplied by the project and its cited research sources.

### M05

**Known preparation, inverse access and replay**

- **Central question:** What does it mean to have an implementable state-preparation procedure?
- **Understanding target:** Distinguish a finite circuit that can be rerun and reversed from a single unknown state or an uncontrolled analog device. Explain why a later response experiment can prepare the original input and replay a prescribed evolution, while a previously produced intermediate quantum state is not a freely reusable copy.
- **Dependencies and story role:** M01–M02. This establishes the access model before any favorable measurement cost is quoted.
- **Conceptual connection:** No-cloning, coherent inverse access and the physical meaning of a panel-start state meet in the paid-prefix rule used throughout the reconstruction.
- **Sources:** [Lin §§1.3–1.4 and 1.7][lin]; [spectral reconstruction, algorithm](../science/spectral-reconstruction.md#algorithm-the-state-at-a-panel-boundary-is-a-paid-prefix); [complete cost, §6](../science/complete-cost.md#6-scalar-estimation-inverse-circuits-and-confidence).

### M06

**One classical number, two error parameters**

- **Central question:** What exactly counts as a successful output?
- **Understanding target:** Read the guarantee $\Pr(|\widehat m_T-m(T)|\le\epsilon)\ge1-p$ as a scalar approximation with additive error $\epsilon$ and failure probability $p$. Separate these from the nodal additive allowance $\delta$, and from producing a quantum state without its requested readout.
- **Dependencies and story role:** M02 and M05. This fixes the output contract before introducing its estimation algorithm.
- **Conceptual connection:** An accuracy guarantee and a confidence guarantee have different roles and costs. The bridge also translates Lin's use of $\delta$ for a failure probability in amplitude estimation; it is not the project's nodal $\delta$.
- **Sources:** [Lin §§1.5 and 4.2][lin]; [model, §1](../science/model.md#1-input-evolution-and-output); [bridge, §2](BRIDGE.md#2-notation-and-access-translation).

### M07

**Coherent amplitude estimation**

- **Central question:** Which access changes the cost of estimating a measurement probability?
- **Understanding target:** Connect state preparation, reflections and the actual inverse circuit to amplitude estimation's inverse-additive-error query count. Distinguish this from independent measurement sampling, and retain the cost of each coherent call and the repetitions needed for confidence.
- **Dependencies and story role:** M05–M06. This identifies the readout mechanism whose precision advantage the reconstruction must preserve.
- **Conceptual connection:** The project does not gain its full-task bound merely by naming amplitude estimation. The feedback curve, the preparation circuit and every replay must first be specified and charged.
- **Sources:** [Lin §§2.3, 3.4 and 4.2][lin]; [complete cost, §6](../science/complete-cost.md#6-scalar-estimation-inverse-circuits-and-confidence). Lin §3.1 supplies the related Hadamard-test viewpoint for expectation access.

### M08

**Explicit data and computational resources**

- **Central question:** When does a small query count describe an efficient algorithm for a supplied instance?
- **Understanding target:** Separate input length, coefficient bit lengths, numerical Hamiltonian norms, evolution time, requested accuracy, query count and elementary-gate count. A short binary description of a huge coefficient does not make its norm–time cost small.
- **Dependencies and story role:** M03 and M05–M07. This moves from quantum primitives to a complete computational task.
- **Conceptual connection:** Explicit Pauli pulse data permits circuit construction and input reading to be priced. Later efficiency statements require polynomial bounds on the numerical resources as well as the description size.
- **Sources:** [Lin §§1.8 and 1.10][lin]; [model, §1](../science/model.md#1-input-evolution-and-output); [complete cost, §1](../science/complete-cost.md#1-finite-input-and-output).

### M09

**Hamiltonian access and normalization**

- **Central question:** How does a finite operator list become the access assumed by a simulator?
- **Understanding target:** Relate a Pauli sum, a computable coefficient-sum bound and explicit sparse row/value circuits. Use block encoding and linear combinations of unitaries as access-and-normalization language, while distinguishing those abstractions from the particular time-dependent simulator used here.
- **Dependencies and story role:** M08. This exposes the work hidden by a Hamiltonian oracle before the full circuit is assembled.
- **Conceptual connection:** The finite Pauli lists and coefficient tables must supply the matrix entries coherently. Neither free QRAM nor an unexplained entry oracle is part of the resource promise.
- **Sources:** [Lin §§6.1–6.3 and 7.3][lin]; [complete cost, §§3–5](../science/complete-cost.md#3-ordinary-tables-and-reversible-arithmetic); [bridge, §6](BRIDGE.md#6-from-a-response-circuit-to-the-full-cost).

### M10

**A polynomial table becomes a finite program**

- **Central question:** What is the computed field when every stored coefficient and gate has finite precision?
- **Understanding target:** Treat the rational coefficient table as defining the actual proxy polynomial. Connect reversible fixed-point arithmetic, polynomial evaluation, gate synthesis and classical circuit generation, and distinguish coefficient-map error from bias in evaluating a response to that stored polynomial.
- **Dependencies and story role:** M05 and M08–M09. This supplies the finite interface used by both the approximation proof and the cost proof.
- **Conceptual connection:** A mathematical polynomial is useful to the algorithm only when its coefficients, selection and evaluation are represented by paid data and operations.
- **Sources:** [Lin §§1.7–1.8][lin]; [spectral reconstruction, finite-precision interface](../science/spectral-reconstruction.md#finite-precision-and-the-response-evaluation-interface); [complete cost, §3](../science/complete-cost.md#3-ordinary-tables-and-reversible-arithmetic).

### M11

**Perturbations of unitary evolution**

- **Central question:** How does an error in the driving field affect the final state and observable?
- **Understanding target:** Use Duhamel's principle to connect an integrated Hamiltonian perturbation to a state or expectation error. Distinguish this prescribed-evolution comparison from the additional stability analysis needed when the field itself depends on the state.
- **Dependencies and story role:** M01, M05 and M10. This provides the error mechanism shared by reconstruction, simulation and hardness.
- **Conceptual connection:** Piecewise polynomial feedback gives a time-dependent prescribed Hamiltonian. Lin's time-independent simulation theorem is background; the project's actual simulation step invokes a separate time-dependent theorem and pays its access requirements.
- **Sources:** [Lin §1.6, §§5.1–5.2 and §7.7][lin]; [spectral reconstruction, proof parts 2 and 4](../science/spectral-reconstruction.md#proof-part-2-contraction-uses-only-real-time-unitarity); [complete cost, §5](../science/complete-cost.md#5-simulation-of-a-complete-prefix).

### M12

**The Hartree closure and the retained quantum problem**

- **Central question:** Which correlations does this mean-field approximation discard, and which does it retain?
- **Understanding target:** Derive the meaning of $H(t)=B(t)+\lambda m(t)A$ with $m(t)=\mathrm{Tr}(A\rho(t))$. In the array motivation, the product closure is between correlated impurity–bath units; it does not factor the impurity from its own bath. The computational theorem solves the resulting closed equation.
- **Dependencies and story role:** M02, M04 and M11. This identifies the nonlinear model that the algorithm must solve, rather than assuming its mean is supplied.
- **Conceptual connection:** A prescribed-field quantum response can be a subroutine inside self-consistency. Error relative to a finite physical array is a separate modeling question, not part of the algorithmic tolerance.
- **Sources:** [Lin §§1.2 and 1.6][lin] for state and propagation foundations; [model, §4](../science/model.md#4-why-this-is-a-mean-field-response-problem); [bridge, §1](BRIDGE.md#1-a-charge-measurement-with-an-unknown-field).

### M13

**Approximating a curve while solving for it**

- **Central question:** How can a short polynomial description of an unknown mean be acquired reliably?
- **Understanding target:** Distinguish an interpolation approximation to a known smooth curve from a fixed-point computation that must acquire its values. Identify the roles of local analyticity, a Chebyshev interpolation operator, its Lebesgue constant and a contraction bound. These are separate ingredients.
- **Dependencies and story role:** M06 and M10–M12. This introduces the mathematical framework required for the reconstruction proof.
- **Conceptual connection:** The polynomial here is a classical function of time. It is different from the matrix polynomial used in quantum eigenvalue transformation; a short output representation does not supply its coefficients for free.
- **Sources:** [Lin §7.5][lin] as a contrast in the role of polynomial approximation; [spectral reconstruction, theorem and proof parts 1–2](../science/spectral-reconstruction.md#the-reconstruction-theorem); [bridge, §4](BRIDGE.md#4-reconstructing-one-scalar-curve).

### M14

**The full task and the two actions**

- **Central question:** What must a meaningful quantum–classical comparison hold fixed, vary and output?
- **Understanding target:** Assemble the explicit input, known initial preparation, unknown feedback curve and final scalar guarantee. Distinguish feedback action $\kappa=\lambda T$ from non-Gaussian impurity action $S$, and distinguish a quantum upper bound, a classical algorithm and a conditional hardness statement.
- **Dependencies and story role:** M04, M07–M08 and M10–M13. This integrates the background into the exact problem the narrative phase addresses.
- **Conceptual connection:** Small $\kappa$ controls the cost of stable feedback acquisition; small $S$ can permit a classical shortcut. Efficient quantum readout at fixed parameters does not by itself give an asymptotic separation from all classical methods.
- **Sources:** [Lin §1.10][lin] for resource accounting; [model, §§3–5](../science/model.md#3-two-actions-with-different-roles); [scientific reading route](../science/README.md).

## Phase II: narrative/innovation

### M15

**Analyticity of the exact local mean**

- **Central question:** Why can each exact local mean be approximated exponentially well in polynomial degree?
- **Understanding target:** Follow the holomorphic density-matrix ODE inside a bounded trace-norm neighborhood of an arbitrary physical panel-start state. Recognize how the bounds on $B$, $A$ and $\lambda$ give a complex-time radius independent of Hilbert-space dimension and a Chebyshev error of order $2^{-q}$ on a sufficiently short panel.
- **Dependencies and story role:** M02 and M11–M13. This is the first local ingredient of the reconstruction, before any noisy coefficient acquisition.
- **Conceptual connection:** Positivity and unit trace at the real initial time provide the physical norm control. No assertion that arbitrary noisy interpolants share the exact solution's analytic bound is needed.
- **Sources:** [Lin §§1.2 and 1.6][lin] for background; [spectral reconstruction, proof part 1](../science/spectral-reconstruction.md#proof-part-1-physical-existence-and-dimension-independent-analyticity); [bridge, §4](BRIDGE.md#4-reconstructing-one-scalar-curve). The complex-time argument is local to the project.

### M16

**A finite collocation map that contracts**

- **Central question:** How is analyticity converted into a stable finite computation?
- **Understanding target:** Define the prescribed-field response $F_\sigma(p)$ and the finite map $\mathcal I_qF_\sigma(p)$. Combine its real-time Lipschitz bound $2\lambda h$ with the interpolation norm $L_q$ to obtain a contraction when $2\lambda hL_q\le1/2$.
- **Dependencies and story role:** M11–M13 and M15. This turns the approximation property into an iteration with a well-defined finite fixed point.
- **Conceptual connection:** Analyticity controls the interpolation defect of the exact physical mean. Real-time unitarity controls the finite map for every admissible real polynomial. Keeping those two arguments separate is what makes noisy acquisition legitimate.
- **Sources:** [Lin §1.6][lin] for the perturbation tool; [spectral reconstruction, proof part 2](../science/spectral-reconstruction.md#proof-part-2-contraction-uses-only-real-time-unitarity); [bridge, §4](BRIDGE.md#4-reconstructing-one-scalar-curve).

### M17

**Measurement error and coefficient error are different**

- **Central question:** What must remain true when the iteration uses noisy numbers and rounded coefficients?
- **Understanding target:** Track nodal response error $\delta$ through the interpolation factor $L_q$, and track the separate coefficient-map allowance $\beta$ in the real polynomial norm. Explain the roles of clipped reports, bounded stored proxies and contraction in preventing either contribution from accumulating without control.
- **Dependencies and story role:** M06, M10 and M15–M16. This supplies the robust finite-data version of the local theorem.
- **Conceptual connection:** The stored polynomial defines the prescribed Hamiltonian for the next response. Its construction error must not also be charged as if the response oracle were evaluating a different, idealized polynomial.
- **Sources:** [Lin §§1.8 and 4.2][lin] for finite values and statistical estimation; [spectral reconstruction, proof part 3](../science/spectral-reconstruction.md#proof-part-3-measurement-and-coefficient-errors) and [finite-precision interface](../science/spectral-reconstruction.md#finite-precision-and-the-response-evaluation-interface).

### M18

**Physical prefixes and global stability**

- **Central question:** Why do valid local approximations combine into the requested global solution?
- **Understanding target:** Define each panel-start state as the ideal evolution from the original prepared input under all previously stored proxies. Compare a local exact nonlinear solution from that physical state with the stored panel and then propagate the discrepancy globally, retaining the $e^{2\kappa}$ stability factor and any initial preparation error.
- **Dependencies and story role:** M05, M11 and M17. This joins the local proof to both a consistent global trajectory and an executable state-access rule.
- **Conceptual connection:** Every nodal experiment pays to prepare and replay its complete prefix. Neither the proof nor the implementation resets a correlated intermediate state to a simpler state for free.
- **Sources:** [Lin §§1.4 and 1.6][lin]; [spectral reconstruction, algorithm](../science/spectral-reconstruction.md#algorithm-the-state-at-a-panel-boundary-is-a-paid-prefix) and [proof part 4](../science/spectral-reconstruction.md#proof-part-4-global-error-from-local-physical-prefixes); [bridge, §5](BRIDGE.md#5-the-panel-start-state-is-a-complete-prefix).

### M19

**Choosing all reconstruction parameters together**

- **Central question:** How does the theorem reach final error $\epsilon$ without a number of time panels proportional to $1/\epsilon$?
- **Understanding target:** Connect the local tolerance $\eta=\epsilon e^{-2\kappa}/16$ to the degree $q$, iteration count $I$, nodal tolerance $\delta$, coefficient tolerance $\beta$ and panel count $P$. Account for $J=P(q+1)I$ response evaluations and for panel boundaries at supplied pulse changes.
- **Dependencies and story role:** M14–M18. This integrates the local analytic, contraction and global-stability ingredients into a finite acquisition plan.
- **Conceptual connection:** At fixed physical parameters the temporal representation and iteration counts grow only polylogarithmically with inverse accuracy. The theorem preserves an algebraic precision cost for acquiring response values; it does not eliminate that cost.
- **Sources:** [Lin §§1.8 and 1.10][lin] for precision and accounting background; [spectral reconstruction, theorem](../science/spectral-reconstruction.md#the-reconstruction-theorem); [complete cost, §2](../science/complete-cost.md#2-reconstruction-parameters-and-the-error-interface).

### M20

**One response, fully compiled**

- **Central question:** What operations are hidden inside one nodal response estimate?
- **Understanding target:** Assemble original-state preparation, ordinary coefficient-table access, reversible polynomial arithmetic, explicit sparse-Hamiltonian access, a complete time-dependent prefix simulation, amplitude estimation and its reflections. Use the inverse of the actual compiled circuit, so its fixed approximation bias is not incorrectly multiplied by the number of estimation calls.
- **Dependencies and story role:** M05, M07, M09–M11 and M19. This supplies an implementable realization of the response interface rather than treating it as an oracle.
- **Conceptual connection:** The imported time-dependent simulator, finite gate synthesis and conditional confidence guarantee serve different parts of the nodal error allowance. The argument counts logical gates, without assuming unmodeled physical errors cancel.
- **Sources:** [Lin §§1.7–1.8, 4.2, 6.1–6.3 and 7.7][lin] for the component language; [complete cost, §§3–6](../science/complete-cost.md#3-ordinary-tables-and-reversible-arithmetic); [bridge, §6](BRIDGE.md#6-from-a-response-circuit-to-the-full-cost).

### M21

**The complete quantum cost statement**

- **Central question:** What remains of the precision improvement after every response and classical operation is priced?
- **Understanding target:** Combine $J$, the estimation cost proportional to $1/\delta$, the full prefix cost and adaptive confidence amplification. Include input reading, circuit generation, classical gate-control instructions, coefficient storage and endpoint evaluation. Read $G+C_{\rm cl}=\widetilde O(\epsilon^{-1})$ with physical/input parameters and failure probability fixed.
- **Dependencies and story role:** M08 and M19–M20. This completes the constructive quantum part of the narrative.
- **Conceptual connection:** For growing instances, $e^{O(\kappa)}$, numerical norm–time products and input resources remain visible. A fixed-parameter precision upper bound is different from a universal classical precision lower bound or a hardware crossover estimate.
- **Sources:** [Lin §1.10 and §4.2][lin]; [complete cost, §§7–9](../science/complete-cost.md#7-end-to-end-resource-theorem); [bridge, §6](BRIDGE.md#6-from-a-response-circuit-to-the-full-cost).

### M22

**Exact classical shortcuts**

- **Central question:** Which apparently quantum instances already have a small classical solution?
- **Understanding target:** Recognize closed Gaussian covariance dynamics when all prescribed terms and the feedback operator are quadratic and the initial state is Gaussian. Also identify stationary number-conserving vacuum/full-filling inputs and the zero centered charge of the maximally mixed state.
- **Dependencies and story role:** M03–M04 and M12–M14. This begins the classical comparison with exact structural simplifications before considering a more general estimator.
- **Conceptual connection:** Nonlinear feedback can coexist with an efficient classical covariance equation. Neither the word “mean-field” nor the dimension of the bath by itself obstructs such a shortcut.
- **Sources:** [Lin §§1.2 and 4.1, Example 4.2][lin] for state and fermionic background; [classical boundary, §§1–2](../science/classical-boundary.md#1-the-input-subclass); [bridge, §7](BRIDGE.md#7-the-classical-boundary-uses-two-actions).

### M23

**Poisson/Dyson words and Gaussian evaluation**

- **Central question:** How can a genuinely interacting response still be computed classically at bounded interaction action?
- **Understanding target:** Expand the non-Gaussian impurity evolution around a prescribed Gaussian evolution. Understand why the expectation needs independent forward and backward random words, why their weight is controlled by the action $S$, and how Wick/Pfaffian evaluation reduces each word pair to finite one-body calculations.
- **Dependencies and story role:** M04, M09, M11 and M22. This supplies a constructive comparator beyond exact Gaussian closure.
- **Conceptual connection:** The classical algorithm expands complete prefixes from the original Gaussian input; it does not assume a later interacting state is Gaussian. Finite word truncation, sampling precision and Gaussian propagation are paid parts of the response cost.
- **Sources:** [Lin §7.3][lin] for the linear-combination viewpoint, not for this classical estimator; [classical boundary, §§3–6](../science/classical-boundary.md#3-a-prescribed-interacting-response-as-an-expectation-over-words); [bridge, §7](BRIDGE.md#7-the-classical-boundary-uses-two-actions).

### M24

**Closing and pricing the classical feedback loop**

- **Central question:** When does the response estimator yield a polynomial classical algorithm for the complete nonlinear task?
- **Understanding target:** Insert the classical nodal estimator into the same robust reconstruction and retain its $e^{4(S+\kappa)}\epsilon^{-2}$ factor, response count and explicitly polynomial word-evaluation cost. Derive the easy regime $S+\kappa=O(\log N)$ when all remaining descriptions, numerical resources and inverse accuracy are polynomially bounded in $N$.
- **Dependencies and story role:** M18–M19 and M23. This completes the full-task classical comparison rather than stopping at one prescribed response.
- **Conceptual connection:** Growing $S$ can leave this proved easy regime, but an exponential factor in this estimator's upper bound is not a classical lower bound. Other classical algorithms can exploit more structure.
- **Sources:** [Lin §1.10][lin] for complexity accounting; [classical boundary, §§7–8](../science/classical-boundary.md#7-closing-the-actual-self-consistent-task); [bridge, §7](BRIDGE.md#7-the-classical-boundary-uses-two-actions).

### M25

**The interacting impurity as an inherited computational resource**

- **Central question:** How can a fixed two-mode interaction support a computation on a growing set of fermionic modes?
- **Understanding target:** Follow the one-particle dual-rail encoding, Gaussian single-qubit gates, fermionic routing and an impurity quartic phase that supplies an entangling logical gate. Keep the Fock product preparation, occupation readout, finite pulse compilation and allowed interaction controls explicit.
- **Dependencies and story role:** M03–M05, M08 and M10. This identifies the established computational core on which both hardness consequences depend.
- **Conceptual connection:** Fixed interaction support is compatible with growing accumulated non-Gaussian action. The universality is inherited from fermionic linear optics plus interaction; the project does not claim that mean-field feedback creates it.
- **Sources:** [Lin §1.7 and §4.1, Example 4.2][lin] for gate and encoding background; [hardness, §§1–2](../science/hardness.md#1-model-and-control-promises) and its primary universality references; [bridge, §8](BRIDGE.md#8-how-the-qualified-hardness-statements-fit).

### M26

**Causal cancellation and an adaptive reduction**

- **Central question:** How can an algorithm for nonzero feedback recover a prescribed-field computation?
- **Understanding target:** Construct a finite source sequentially so that each new segment cancels the actual feedback to controlled error. Use causality, the charge-derivative bound and Duhamel comparison to control the residual; freeze the measured charge after an intermediate time when only terminal queries are available.
- **Dependencies and story role:** M11–M12, M18 and M25. This gives the first hardness consequence for the actual self-consistent equation.
- **Conceptual connection:** The reduction uses polynomially many adaptive scalar queries, fresh preparations and charged source tables. It is a Turing reduction; its conclusion at fixed feedback action does not require treating an unknown mean curve as input.
- **Sources:** [Lin §§1.6 and 1.10][lin] for propagation and resource language; [hardness, §§3–4](../science/hardness.md#3-causal-cancellation-of-the-actual-feedback); [bridge, §8](BRIDGE.md#8-how-the-qualified-hardness-statements-fit). The reduction itself is supplied locally.

### M27

**An exactly soluble active probe**

- **Central question:** What does a nonzero feedback effect look like when the entire nonlinear response is analytically known?
- **Understanding target:** Relate the two-mode one-particle problem to $H=(\lambda/2)X+\lambda zZ$ and the solutions $z(t)=\pm\mathrm{sech}(\lambda t)$. Explain how feedback changes the same final charge that is measured, while recognizing that this isolated probe has an elementary classical shortcut.
- **Dependencies and story role:** M01–M02 and M11–M12. This supplies a concrete nonlinear mechanism before attaching it to a hard computation.
- **Conceptual connection:** Observable nonlinear activity and computational difficulty are different properties. The probe can certify the former and transmit a computational signal without itself accounting for the latter.
- **Sources:** [Lin §§1.1–1.2][lin] for the two-level state language; [examples, §§1–2](../science/examples.md#1-derivation-of-the-critical-probe); [hardness, §5](../science/hardness.md#5-a-nonlinear-probe-with-an-exact-response); [bridge, §3](BRIDGE.md#3-a-complete-two-mode-example).

### M28

**Direct source-free hardness with an active output**

- **Central question:** Can one explicit source-free instance have both a hard final charge and a certified nonzero feedback effect?
- **Understanding target:** Connect a compressed amplified computation to the probe, control the resulting state error and retain the final constant promise gap. Distinguish this direct reduction from M26's adaptive reduction. State the polynomial control caps and the scaling of the quartic interaction when computation is compressed to a fixed horizon.
- **Dependencies and story role:** M18, M21, M25 and M27. This gives the stronger, separately qualified hardness construction and its efficient quantum upper bound.
- **Conceptual connection:** The final probe acts on the same output rails; its ideal one-particle sector nulls the quartic term there. The construction permits growing strengths and action, so it is not a fixed-time, fixed-strength hardness claim.
- **Sources:** [Lin §§1.6–1.7 and 1.10][lin] for background; [hardness, §§6–7](../science/hardness.md#6-a-direct-source-free-hardness-corollary-with-an-active-probe); [verification, §6](../science/verification.md#6-exact-certificate-for-the-active-probe-margins); [bridge, §8](BRIDGE.md#8-how-the-qualified-hardness-statements-fit).

### M29

**The evidence and attribution behind the combined result**

- **Central question:** Which parts of the conclusion rest on local proofs, imported theorems, finite checks or established predecessors?
- **Understanding target:** Separate the analytic reconstruction proof, the imported simulation and estimation tools, the explicit classical construction, and the qualified reductions. Interpret small ODE comparisons and the exact probe-margin certificate at their finite scope. Locate the contribution relative to earlier spectral self-consistency, noisy fixed points and quantum expectation-feedback algorithms.
- **Dependencies and story role:** M15–M28. This integrates the narrative's arguments into a defensible account of what the project adds.
- **Conceptual connection:** A short polynomial representation and amplitude estimation are established ideas. The substantive guarantee is their stable, physically normalized and completely charged composition, with an honest classical boundary and hard-family qualification.
- **Sources:** [Lin §1.10][lin] for the distinction between abstract and implemented resources; [prior work](../science/prior-work.md); [verification](../science/verification.md); [complete cost, §§8–9](../science/complete-cost.md#8-what-the-accuracy-statement-does-and-does-not-establish); [research references](../references/REFERENCES.md).

### M30

**The complete conditional advantage and its physical limits**

- **Central question:** What scientific conclusion survives when output, feedback acquisition, classical shortcuts and control assumptions are considered together?
- **Understanding target:** State the inverse-linear quantum precision upper bound at fixed parameters, the polynomial classical regime at logarithmic total action, and the separate worst-case hardness consequences under their explicit resource promises. Explain why the growing hard families leave the bounded-action shortcut while keeping feedback acquisition efficient.
- **Dependencies and story role:** M14, M21, M24, M26 and M28–M29. This is the global synthesis of the narrative phase and of the full map.
- **Conceptual connection:** The result supports a complete algorithmic capability and a conditional obstruction to a uniform efficient classical solver. It leaves practical crossover, typical natural-drive difficulty and finite-array mean-field-model error as separate scientific questions; none follows from the presence of feedback alone.
- **Sources:** [Lin §1.10][lin] as resource-accounting background; [model, §§3–5](../science/model.md#3-two-actions-with-different-roles); [complete cost, §§7–8](../science/complete-cost.md#7-end-to-end-resource-theorem); [classical boundary, §8](../science/classical-boundary.md#8-consequences-for-advantage-claims); [hardness, §7](../science/hardness.md#7-scope-of-the-conditional-advantage); [bridge, §9](BRIDGE.md#9-reading-the-complete-conclusion).

[lin]: https://arxiv.org/pdf/2201.08309v1
