# Prior work and the scope of the contribution

This research account establishes a complete computational guarantee for a restricted class of selfconsistent quantum dynamics. The state evolves under an explicitly described Hamiltonian whose additional coefficients are a small number of expectation values. The requested output is a classical scalar. Preparing the initial state, reconstructing the unknown field, replaying earlier evolution, estimating the scalar, and compiling the field into quantum circuits are all part of the task.

The one-field model is

```math
\dot\rho(t)=-i[B(t)+\lambda m(t)A,\rho(t)],
\qquad m(t)=\mathrm{Tr}(O\rho(t)),
\qquad \|A\|,\|O\|\leq1.
```

The main specialization has a local impurity occupation as both the feedback observable and the coupled operator. The theorem is for an explicitly represented pulse Hamiltonian and a supplied state-preparation circuit. Its precision dependence, at fixed physical parameters, is $`\mathstrut \epsilon^{-1}\mathrm{polylog}(1/\epsilon)`$. Dependence on integrated feedback strength, Hamiltonian norm, input length, and circuit costs remains explicit. A fixed-size extension of the feedback vector requires corresponding norm and cost bookkeeping; an extensive density field is outside the scalar theorem.

## What is inherited

| Ingredient | Established antecedent | Consequence for the present claim |
|---|---|---|
| Chebyshev selfconsistent time propagation | [Baer (2000)](../references/REFERENCES.md#baer2000) | Polynomial interpolation and Picard iteration are inherited numerical tools. |
| High-order propagation with a few state-dependent coefficients | [Tal-Ezer, Kosloff, and Schaefer (2012)](../references/REFERENCES.md#tal-ezer2012); [Schaefer, Tal-Ezer, and Kosloff (2017)](../references/REFERENCES.md#schaefer2017) | Neither spectral propagation nor the few-field representation is new. |
| Measured expectation values driving later quantum evolution | [Andress et al. (2025)](../references/REFERENCES.md#andress2025) | Feedback measurements, classical history storage, and prefix replay are inherited. |
| Noisy quantum selfconsistent iteration with inverse-error cost | [Ko, Li, and Wang (2023)](../references/REFERENCES.md#ko2023) | Amplitude estimation inside a convergent fixed-point iteration is established. |
| General nonlinear quantum algorithms with accurate expectation output | [Brüstle and Wiebe (2025)](../references/REFERENCES.md#brustle2025) | Inverse-error scalar precision is not a new general principle. |
| Refined Carleman convergence and nonlinear complexity results | [Jennings et al. (2026)](../references/REFERENCES.md#jennings2026) | Stability, normalization, sparsity, and access assumptions must be compared explicitly. |
| Mean-field evolution from bounded interactions among many copies | [Lloyd et al. (2020)](../references/REFERENCES.md#lloyd2020) | Dimension-efficient mean-field simulation has an established physical construction. |
| Quantum impurity solvers inside classical selfconsistency | [Bauer et al. (2016)](../references/REFERENCES.md#bauer2016); [Kreula, Clark, and Jaksch (2016)](../references/REFERENCES.md#kreula2016) | A quantum core coupled to a classical mean field is established. |

## Classical spectral selfconsistency

[Baer](../references/REFERENCES.md#baer2000), Section II, writes nonlinear Schrödinger evolution as an integral equation, samples it at Chebyshev nodes, and solves the resulting implicit equations by iteration. Equations (20)–(22) give the sampled equations, iteration, and continuous reconstruction. The method stores full classical state vectors at the nodes and measures work in Hamiltonian applications. Its use of short intervals to obtain convergence directly anticipates the numerical architecture relevant here.

[Tal-Ezer, Kosloff, and Schaefer](../references/REFERENCES.md#tal-ezer2012) and the more extensive [2017 analysis](../references/REFERENCES.md#schaefer2017) develop semiglobal propagation of time-dependent and nonlinear equations. The latter explicitly considers a generator of the form $`\mathstrut G_0+\sum_j\xi_j(u,t)G_j`$ in Section 3.3, equations (92)–(95). Appendix D separates iteration, time interpolation, matrix-function, and accumulated errors. This is closer prior work than a generic reference to spectral methods.

Those methods manipulate the evolving state as a classical vector. Substituting a quantum state for that vector does not implement the vector arithmetic or nonlinear iteration at its stated cost. The present construction instead interpolates a scalar response, obtains its values through unitary evolution and measurement, and proves the resulting noisy fixed-point and gate-cost bounds. The numerical approximation ideas remain inherited.

## The closest dynamic quantum predecessor

The published version of [Andress et al.](../references/REFERENCES.md#andress2025), Sections 2.2 and 2.10, uses Hamiltonian–observable pairs and freezes measured expectations during a short step. It explicitly stores the estimated history and replays evolution from the initial state because measured copies cannot be reused. For $`\mathstrut M`$ pairs, $`\mathstrut m`$ copies, step $`\mathstrut \Delta t`$, and horizon $`\mathstrut T`$, it counts $`\mathstrut O(MmT/\Delta t)`$ measurements and $`\mathstrut O(MmT^2/\Delta t^2)`$ evolution steps, before their individual implementation costs.

The journal's discussion of the required $`\mathstrut m`$ is system dependent, includes a numerical ensemble-error scaling, and mentions a possible improvement from amplitude amplification. The arXiv version's Section 2.8 is more explicit about inverse-error estimation. Neither version supplies the complete spectral error-to-gate-cost guarantee used here. The [complete-cost theorem](complete-cost.md) removes the accuracy-driven time-mesh penalty under its stated input assumptions, with all replays retained in the accounting. Measured feedback and amplitude estimation remain inherited ingredients.

## Noisy quantum fixed points already have inverse-error guarantees

[Ko, Li, and Wang](../references/REFERENCES.md#ko2023) study a stochastic selfconsistent density-functional calculation. Their Theorem 17 gives

```math
O\!\left(\frac{sN_I}{\epsilon}
\log\frac1\epsilon\log\frac1\delta\right)
```

Hamiltonian-oracle queries for the full-coordinate fixed-point method, with the theorem's additional probability term for the initial neighborhood. The result assumes an appropriate local contraction and a sufficiently close initial density; quantum singular-value transformation and amplitude estimation implement the density update.

This is a direct antecedent for combining noisy selfconsistency with inverse-error quantum estimation. The different task here is initial-value evolution of an interacting quantum state. Short physical time panels establish contraction from operator-norm bounds for every physical panel-start state, without an unknown stationary solution as a warm start. The scalar field record is then compiled into explicit evolution circuits. These dynamic and access-model guarantees are proved in [spectral reconstruction](spectral-reconstruction.md) and [complete cost](complete-cost.md); the general fixed-point precision principle is already known.

## General nonlinear algorithms and normalization

[Brüstle and Wiebe](../references/REFERENCES.md#brustle2025) give quantum and classical algorithms for nonlinear unitary dynamics. Their Corollary 13 already combines state preparation, its inverse, and expectation estimation to obtain an output estimate at cost proportional to $`\mathstrut 1/\epsilon`$, up to logarithms and their coefficient-norm parameters. General polynomial systems can be transformed into their quadratic form.

Directly vectorizing the present density equation gives the quadratic coefficient map

```math
F_2=\lambda\,\mathcal L_A\otimes\mathrm{vec}(O)^\dagger,
\qquad \mathcal L_A(X)=-i[A,X].
```

For a local Pauli $`\mathstrut A=O`$ acting on dimension $`\mathstrut D`$, its Euclidean operator norm is $`\mathstrut 2|\lambda|\sqrt D`$, although both physical operators have norm one. Thus that direct application of the general theorem does not establish a bound polynomial in the number of qubits. The scalar-response construction uses the physical operator norms instead.

This is an obstruction to a particular flattening, not a lower bound against every Carleman representation, rescaling, or structured embedding. A different representation must be assessed with its own preparation, normalization, sparsity, and readout costs.

[Jennings et al.](../references/REFERENCES.md#jennings2026) substantially strengthen Carleman analysis. Theorems 6.1–6.3 involve nonresonance, transformed nonlinear-coefficient norms and sparsity, and costs containing $`\mathstrut 2^k\kappa_Q^k`$, with $`\mathstrut k`$ logarithmic in inverse precision. Theorem 6.4 has better precision behavior under Lyapunov-transform access and the stability assumptions of Theorem 3.6. The conservation-law extension in Section 4 also constrains nonlinear coupling into marginal modes and retains a spectral-gap condition. Conservation alone is not its sufficient hypothesis.

These results do not directly give the arbitrary bounded-observable feedback guarantee above, and the canonical flattening retains its normalization cost. They also do not exclude a more effective structured embedding. Their nonlinear Schrödinger complexity results preclude claiming that nonlinear quantum hardness itself is new here.

## Many-copy constructions and dense output

[Lloyd et al.](../references/REFERENCES.md#lloyd2020) realize nonlinear evolution through symmetrized interactions among copies and a mean-field limit. Such interactions can have small physical operator norm even when a flattened polynomial coefficient matrix does not. Their analysis includes finite-copy and discretization errors. This is an important alternative to measured feedback; the present result does not establish a separation from every refined many-copy implementation. The specific complete scalar precision bound claimed here was not identified in that construction.

[Liu and Lin](../references/REFERENCES.md#liu2024) analyze time-accumulated observables for prescribed quantum dynamics, including complexity near $`\mathstrut T/\epsilon`$ for certain low-rank outputs. Their output variable does not in general feed back into the Hamiltonian. Adding an unknown selfconsistent field therefore needs a separate analysis, while their work supplies relevant precedent for pricing the observable rather than stopping at a prepared state.

## Impurity physics and the classical comparison

Quantum impurity solvers with classical selfconsistency appear in [Bauer et al.](../references/REFERENCES.md#bauer2016) and [Kreula et al.](../references/REFERENCES.md#kreula2016). The scalar occupation feedback used here is a specified Hartree closure around an interacting impurity. It is not a full dynamical mean-field theory algorithm: general DMFT selfconsistency involves richer bath or Green-function data.

[Jiang et al.](../references/REFERENCES.md#jiang2026) establish a useful distinction between static and dynamical impurity tasks. Their static ground-state and partition-function results are classical algorithms, while Section 7 establishes universal computational power of impurity dynamics. Universal fermionic computation also has established antecedents in [Bravyi and Kitaev](../references/REFERENCES.md#bravyi2002). The [hardness account](hardness.md) gives a self-contained dual-rail implementation for the specified number-conserving impurity and Fock input.

Two feedback consequences are distinguished. Causal cancellation transfers the bare scalar task through adaptive polynomially many calls, giving a Turing reduction. A separately proved source-free construction gives a direct constant-gap reduction by concentrating a universal computation into a short interval and appending an active, analytically solvable nonlinear probe. It pays polynomially growing control strengths, including the quartic interaction. This second construction preserves inherited computational hardness while ensuring that feedback changes the same measured output by a constant; it does not make the nonlinear probe itself hard.

The classical baseline must preserve the same task. Gaussian bath dynamics alone is not a faithful replacement for the interacting impurity. A closed analytic mean-field example can verify a nonlinear effect, but cannot establish a quantum advantage. Conversely, worst-case hardness of explicitly controlled instances does not establish a practical crossover for typical material parameters.

The [classical boundary](classical-boundary.md) makes this comparison quantitative. It derives an independent Poisson-word estimator for the full interacting prefix, evaluates each word with established [Gaussian and Wick methods](../references/REFERENCES.md#terhal2002), and closes the same feedback task. The resulting sufficient classical regime has logarithmically bounded non-Gaussian action and feedback action, together with polynomially bounded remaining input resources. Real-time impurity expansions have a substantial [diagrammatic antecedent](../references/REFERENCES.md#werner2009), and [inchworm methods](../references/REFERENCES.md#cohen2015) can improve particular regimes. The derived upper bound is therefore a conservative comparator, not a claim of optimal classical complexity.

## The established guarantee and its limits

The proved interface connects a scalar numerical solver to actual quantum circuits. The [reconstruction](spectral-reconstruction.md) and [complete-cost](complete-cost.md) arguments establish four linked statements:

1. A complex-time bound for the exact physical response gives geometrically accurate interpolation on short panels, with constants independent of Hilbert-space dimension.
2. For arbitrary real polynomial proxies, unitarity gives a real-time response Lipschitz bound. After interpolation, the panel map is contractive. Bounded nodal errors remain controlled even though the noisy iterates need not obey an analytic bound.
3. Every response query is reconstructed from the original supplied state and the recorded earlier field. The inverse required for amplitude estimation is the inverse of this compiled circuit.
4. Polynomial coefficients, finite-precision arithmetic, time-dependent simulation, query failure probabilities, and final scalar extraction are charged explicitly. No coherent random-access memory or unknown field oracle is supplied without cost.

The resulting statement is a composition theorem for a physically structured output task. It permits high precision without a power-law time-mesh penalty and combines with a restricted interacting-impurity hardness construction. It does not establish the first spectral selfconsistent algorithm, the first quantum mean-field algorithm, a universal $`\mathstrut 1/\epsilon`$ lower bound for explicitly described inputs, or an observed advantage on present hardware.

The primary-source comparison above supports a narrow gap in existing guarantees, not proof that no unpublished or differently encoded algorithm can subsume it. Novelty and significance should be judged on the explicit theorem and task consequence, with the inherited ingredients credited.
