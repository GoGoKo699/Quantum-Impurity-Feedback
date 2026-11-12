# Scientific reading route

The central question is whether a classical scalar can be extracted efficiently from self-consistent quantum dynamics after the whole acquisition and feedback loop is charged. The answer has three parts: a quantum upper bound, a classical easy regime and a conditional obstruction for more general programmable inputs. None of those parts substitutes for the others.

## 1. Define the output before comparing algorithms

[Model](model.md) specifies the finite pulse input, initial preparation, local mean, final error and failure probability. It separates the feedback action $\kappa$ from the impurity interaction action $S$, and explains the Hartree interpretation. The computational target is the closed equation itself.

[Examples](examples.md) derives the exact hyperbolic-secant probe. Its analytic solution supplies a useful correctness check and makes clear why an observable nonlinear effect alone cannot establish computational advantage.

## 2. Acquire the unknown field with a controlled error

[Spectral reconstruction](spectral-reconstruction.md) proves a local analytic radius for the exact mean, contraction of a finite collocation map, stability under noisy response values and finite coefficient errors, and global accumulation from a consistent physical prefix. Only the exact local solution needs an analytic continuation. The noisy proxy polynomials are controlled by real-time unitary estimates.

Each panel begins with the ideal state produced by the already stored prefix. A response experiment obtains that state by a paid replay from the original input. This keeps local approximation, global stability and implementable state access aligned.

## 3. Implement and price every response

[Complete cost](complete-cost.md) turns the reconstruction interface into a logical quantum circuit algorithm. It constructs finite coefficient arithmetic and sparse-matrix access, invokes a specified time-dependent simulator, synthesizes a fixed gate set and uses the actual compiled circuit and its inverse for amplitude estimation. Classical circuit generation, gate-control work and field storage are included.

The inverse-linear precision power is an upper bound at fixed physical parameters and fixed failure probability. The explicit dependence on feedback action, norms, time, input length and replay counts determines whether an instance family is polynomially solvable.

## 4. Challenge the advantage with a classical algorithm

[Classical boundary](classical-boundary.md) begins with the exact Gaussian and trivial-state shortcuts. It then constructs a two-branch Poisson/Dyson estimator from the original Gaussian state, evaluates its words by Wick/Pfaffian methods, and pays for finite sampling and one-body propagation. Applying the same feedback reconstruction proves a full-task classical algorithm when $S+\kappa=O(\log N)$, provided the remaining descriptions, norm–time resources, numerical bit lengths, and $1/\epsilon$ are polynomially bounded in $N$.

The independent forward and backward words are essential. Resetting a correlated intermediate state to a Gaussian state, or counting only a single branch, would give a different and generally incorrect algorithm.

## 5. State the remaining complexity obstruction precisely

[Hardness](hardness.md) supplies a number-conserving dual-rail construction using a fixed two-mode interacting impurity, Gaussian routing and an easy Fock product input. It then gives two consequences: a causal cancellation reduction using finite adaptive source tables, and a separate direct source-free reduction with a certified active final probe. The latter permits polynomially large controls and scales the quartic strength when compressing time.

These are worst-case statements for explicitly programmable families. The hard core is the quantum computation already supported by the impurity. The results do not establish difficulty for an arbitrary natural drive, practical hardware savings or hardness created by mean-field feedback alone.

## 6. Locate the contribution and its checks

[Prior work](prior-work.md) compares the construction with spectral self-consistent propagation, noisy quantum fixed points, expectation-valued Hamiltonians, Carleman methods, many-copy mean-field simulation and quantum impurity solvers. The contribution is the stated composition with physical norm bounds and a finite complete cost account, together with the classical boundary and qualified hard-family consequences.

[Verification](verification.md) describes the reproducible small-state checks, the exact-probe inequality check and their limits. [References](../references/REFERENCES.md) gives the primary source record. These sources and checks support different parts of the argument; the numerical examples are not evidence of asymptotic quantum advantage.
