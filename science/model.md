# A self-consistent local charge as the computational task

The output is one impurity charge at a specified time. The input describes an interacting quantum subsystem and its bath explicitly; its Hartree field is an unknown part of the solution. This distinction determines both the algorithm and its classical comparison.

## 1. Input, evolution and output

There are $n$ fermionic modes, represented by $n$ qubits after a fixed Jordan–Wigner transformation. On each of $K$ supplied time intervals, the base Hamiltonian is a finite Pauli sum

$$
B(t)=B_j=\sum_{\ell=1}^{R_j}c_{j\ell}P_{j\ell},
\qquad R_j\le R.
$$

The real coefficients and interval boundaries are finite classical data. Their total description length is $L_{\mathrm{in}}$; $B_{\mathrm{in}}$ bounds the supplied bit lengths. Reading this input and constructing its quantum circuits are charged. The coefficient bound

$$
\alpha_0=\max_j\sum_\ell |c_{j\ell}|
$$

is directly computable. A certified operator-norm bound $\Lambda\ge\max_j\|B_j\|$ may be used; $\Lambda=\alpha_0$ always suffices. Complexity depends on numerical norm–time products as well as input bit length. A succinct description of an exponentially large norm does not make its evolution cheap.

The central observable is the centered occupation of one impurity mode,

$$
A=1-2a_u^\dagger a_u=Z_u,\qquad \|A\|=1.
$$

For $\lambda\ge0$ and $T>0$, the target is the unique physical solution of

$$
\dot\rho(t)=-i[B(t)+\lambda m(t)A,\rho(t)],
\qquad m(t)=\operatorname{Tr}[A\rho(t)],
\qquad \rho(0)=\rho_0.
\tag{M1}
$$

The initial state is a specified Fock product state for the impurity application and the hardness constructions. More generally, the algorithm accepts a supplied finite preparation circuit, including a purification when needed, and pays its preparation and inverse costs. It does not assume that an unknown interacting equilibrium state is available.

Given $0<\epsilon<1$ and $0<p<1$, return a classical number $\widehat m_T$ satisfying

$$
\Pr\bigl[|\widehat m_T-m(T)|\le\epsilon\bigr]\ge1-p.
\tag{M2}
$$

The actual occupation is $(1-m(T))/2$, with half the centered-observable error. The coupling $\lambda$ throughout refers to the centered convention in (M1); replacing $A$ by an uncentered density requires converting the Hamiltonian coefficients as well.

The scalar source used in the causal reduction is an ordinary part of the input: $B(t)=H_{\mathrm{base}}(t)+b(t)A$. The field $m(t)$ itself is never supplied. The source-free hard family in [the hardness account](hardness.md) instead sets $b=0$ and pays explicitly for its concentrated control pulses.

## 2. The impurity specialization

For the classical comparison and physical interpretation, split the base into

$$
B(t)=Q(t)+V(t)+b(t)A,
\qquad
Q(t)=\sum_{j,k}h_{jk}(t)a_j^\dagger a_k.
\tag{M3}
$$

$Q$ is quadratic; $V$ acts on a fixed number of impurity modes. A concrete number-conserving interaction is $V(t)=\chi(t)n_un_v$ on two impurity modes. The bath can contain arbitrarily many modes and become entangled with the impurity. Its quadratic character does not imply Gaussianity of the full interacting state.

The general algorithm only needs the explicit Pauli description of (M1). It therefore also accommodates other few-observable Hamiltonian feedback models. The impurity structure is used to identify a strong classical shortcut and a concrete hard subfamily, rather than to supply a free Hamiltonian simulator.

Jordan–Wigner strings, their lengths and their selectors are included in the circuit cost. The bounded impurity support is an input restriction; it does not mean that all correlations or the computational work live in a constant-dimensional Hilbert space.

## 3. Two actions with different roles

The feedback action is

$$
\kappa=\lambda T.
\tag{M4}
$$

It controls the stability factor in the reconstruction theorem. Separately, expand the non-Gaussian impurity term in normalized even Majorana monomials,

$$
V(t)=\sum_a v_a(t)M_a,\qquad \|M_a\|=1,
\qquad S=\int_0^T\sum_a|v_a(t)|\,dt.
\tag{M5}
$$

The number of these terms is constant for a fixed impurity. Identity and quadratic contributions can be absorbed into $Q$. In particular, the genuinely quartic component of $\chi n_un_v$ has coefficient magnitude $|\chi|/4$ in this convention.

The quantum cost is polynomial in the explicitly charged Hamiltonian description, norm and time parameters, while retaining an exponential dependence on $\kappa$. The [classical Dyson/Wick construction](classical-boundary.md) has an exponential upper bound in $S$. At fixed $\kappa$ and polynomially bounded remaining resources, $S=O(\log L)$ still admits a polynomial classical algorithm at inverse-polynomial accuracy, where $L$ is an ordinary input-size parameter. Hard growing-input examples must leave that easy-action regime.

This is a comparison of proved upper bounds and a separate conditional complexity obstruction. An exponential classical upper bound is not an exponential lower bound.

## 4. Why this is a mean-field response problem

One physical motivation is an array of correlated units, each consisting of an impurity and its own bath, coupled through their local charge. For $M$ identical units, consider the formal collective Hamiltonian

$$
\mathcal H_M(t)=\sum_{r=1}^M B^{(r)}(t)
 +\frac{\lambda}{M-1}\sum_{r<s}A^{(r)}A^{(s)}.
\tag{M6}
$$

The first marginal of a permutation-symmetric state obeys

$$
\dot\rho_1=-i[B,\rho_1]
 -i\lambda\operatorname{Tr}_2[A\otimes A,\rho_{12}].
$$

The product closure $\rho_{12}\approx\rho\otimes\rho$ gives (M1), because

$$
\operatorname{Tr}_2[A\otimes A,\rho\otimes\rho]
 =m[A,\rho].
$$

Correlations within each impurity–bath unit remain in $\rho$. Only the inter-unit density coupling is closed at Hartree level. The charge transient is therefore an operational output of a specified embedded quantum model.

The computational theorem concerns the closed equation (M1). Applying it as a finite-array prediction additionally requires a controlled mean-field-model error for (M6), which is not part of its algorithmic error budget. Likewise, a self-consistent two-time bath kernel in full dynamical mean-field theory is a different, larger input/output task. Earlier quantum impurity and DMFT workflows are credited in [the prior-work comparison](prior-work.md).

## 5. Assumptions that affect the consequence

| Feature | Role in the result |
|---|---|
| Explicit finite pulse/Pauli data | Makes input reading and Hamiltonian entry circuits constructible and chargeable |
| Known initial preparation and its reverse | Permits coherent amplitude estimation of each paid prefix |
| A fixed number of bounded expectation fields | Keeps the reconstructed classical feedback description small |
| Moderate feedback action | Keeps the stated $e^{O(\kappa)}$ acquisition cost efficient |
| Growing non-Gaussian action in hard families | Avoids the bounded-action Gaussian/Dyson shortcut |
| Programmable controls in the hardness construction | Supplies a worst-case complexity statement, without a typical-material claim |

The classical output and full task cost are central: producing a quantum state with an unspecified readout, or assuming an already known mean curve, would answer a different question.

**Next:** [spectral reconstruction](spectral-reconstruction.md), [complete cost](complete-cost.md), and [the classical boundary](classical-boundary.md).
