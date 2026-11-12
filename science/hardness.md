# Hardness of a local impurity mean with nonzero feedback

The task is to predict one local occupation in an explicitly driven quantum impurity system with a scalar Hartree field. The nonzero integrated feedback strength is fixed. The initial state, all controls, every source value, the requested accuracy, and the output are finite classical data.

There are two distinct statements below.

1. **Causal transfer:** a general solver for the feedback task would solve the corresponding driven linear quantum problem through polynomially many adaptive scalar calls. This works without assuming small integrated feedback.
2. **An active final probe:** a more specially controlled, source-free family admits a direct reduction from quantum circuits. Its terminal nonlinear stage changes the measured answer by a constant. That construction deliberately places a universal computation before an analytically solvable nonlinear probe.

Neither statement attributes universal computational power to the scalar feedback alone. The many-body quantum dynamics already supplies the computational obstruction. The feedback results specify how that obstruction survives the complete self-consistent task.

## 1. Model and control promises

Let $c_r,c_r^\dagger$ denote $n$ fermionic modes and $n_r=c_r^\dagger c_r$. Fix two impurity modes $u,v$, and let
$$
A=1-2n_u,\qquad \|A\|=1.
$$
Consider
$$
\begin{aligned}
\dot\rho(t)&=-i[H_b(t,\rho),\rho(t)],\\
H_b(t,\rho)&=D(t)+[b(t)+\lambda m(t)]A,\\
m(t)&=\operatorname{Tr}(A\rho(t)),\\
D(t)&=Q(t)+g(t)n_un_v.
\end{aligned} \tag{1}
$$

Here $Q(t)=\sum_{rs}q_{rs}(t)c_r^\dagger c_s$ is a number-conserving quadratic Hamiltonian. Its Hermitian coefficient matrix, the quartic coefficient $g(t)$, and the scalar source $b(t)$ are explicit rational piecewise-constant lists. The initial state is a specified Fock product state. The output is a classical estimate of $m(T)$ to additive error $\epsilon$, with bounded failure probability.

The parameter $\kappa=\lambda T$ is fixed to $1$ in the main complexity corollaries. A polynomial bound on control strengths, switch counts, time, and bit lengths is part of the input family; these quantities are charged by the [complete-cost theorem](complete-cost.md).

Two useful control variants are:

| Variant | Quartic interaction | Gaussian controls | Duration convention |
|---|---|---|---|
| Switchable interaction | $g(t)\in\{0,\chi\}$ | Bounded-strength pulses suffice | Polynomial $T$, $\lambda=1/T$ |
| Always-on interaction | $g(t)=\chi>0$ throughout | Polynomially large amplitudes are allowed and charged | Polynomial $T$, $\lambda=1/T$ |

In both rows $\chi$ can be fixed independently of the circuit size. Rescaling a polynomial schedule into $T=1$ multiplies **all** its Hamiltonian coefficients, including its quartic strength, by the original duration. Fixed time therefore does not also imply a fixed bounded interaction strength. This distinction matters for the active-probe construction in Section 6.

The input family permits turning off $Q$ and $b$ after a chosen time. In the switchable variant the quartic term can then be turned off as well; in the always-on variant it remains. Both possibilities commute with $A$, which is the only property needed for terminal-query padding.

The feedback preserves total particle number. A vacuum input under a number-conserving Hamiltonian is stationary and cannot encode a nontrivial computation. The hard construction uses **one particle per logical dual rail**, an easy Fock product state.

## 2. Bare number-conserving impurity dynamics can encode a circuit

The following elementary construction fixes the input and readout details needed for the reduction. Universal fermionic gate constructions are established prior work; this derivation specializes the routing and observable to the present two-mode impurity. [Bravyi–Kitaev 2002](https://arxiv.org/abs/quant-ph/0003137v2)

### Dual-rail gates

Encode a logical qubit in a pair of modes $(a_j,b_j)$ by
$$
|0\rangle_L=|0_{a_j}1_{b_j}\rangle,\qquad
|1\rangle_L=|1_{a_j}0_{b_j}\rangle.
$$
On this one-particle subspace,
$$
X_L=c_{a_j}^\dagger c_{b_j}+c_{b_j}^\dagger c_{a_j},
\qquad Z_L=1-2n_{a_j}.
$$
Hopping and orbital phases therefore implement arbitrary single-qubit rotations. The number-conserving quartic phase
$$
\exp(-i\pi n_{a_j}n_{a_k})
$$
acts as a logical controlled-$Z$.

Only the fixed physical pair $(u,v)$ needs an interaction. Let $W$ be a Gaussian unitary that permutes the selected modes $a_j,a_k$ into $u,v$. Then
$$
W^\dagger e^{-i\pi n_un_v}W
 =e^{-i\pi n_{a_j}n_{a_k}}. \tag{2}
$$
Thus routing to the impurity, waiting under the interaction, and undoing the routing implements the entangler.

Fermionic permutation signs do not require an unpriced correction. A swap of two fermionic modes is itself Gaussian; for example, up to the conventional operator ordering,
$$
S_{rs}
 =e^{i\pi(n_r+n_s)/2}
  e^{-i\pi(c_r^\dagger c_s+c_s^\dagger c_r)/2}
$$
exchanges the single-occupation states and multiplies the double-occupation state by $-1$. Equation (2) is an operator conjugation identity using this actual fermionic unitary and its inverse, so its signs cancel exactly. Adjacent mode swaps can route along a chain with polynomial overhead.

At the end, route the chosen output rail to mode $u$. Its occupation equals the logical output-bit probability. Routing both rails of the output qubit to $u,v$ will additionally be useful for Section 6. The initial encoded all-zero state is the specified one-particle-per-pair Fock state, prepared with $O(n)$ elementary occupation flips in a qubit representation.

### Finite compilation and interaction strength

For a polynomial-size quantum circuit, the preceding gates give a polynomial-size pulse schedule. Single-qubit gates, controlled phases, and swaps require angles such as $\pi/2$; they are replaced by rational angles or rational pulse durations to polynomially many bits. If the circuit has $L$ elementary pulses, approximation error $O(\zeta/L)$ per pulse makes the full bare propagator differ by at most $\zeta$ in operator norm. This requires $O(\log(L/\zeta))$ additional fractional bits, with polynomial classical compilation.

With a switchable quartic interaction, turn it off during Gaussian pulses and on during controlled-phase waits. Constant pulse strengths, polynomial pulse count, and polynomial total time suffice. Amplifying the original circuit's success gap and choosing a fixed small $\zeta$ gives a robust constant gap in the terminal local occupation.

For an **always-on** interaction $V=\chi n_un_v$, implement an intended Gaussian pulse $e^{-iG_j}$ over a short rational interval $\tau_j$, using $G_j/\tau_j+V$. Duhamel's bound gives
$$
\left\|e^{-i(G_j/\tau_j+V)\tau_j}-e^{-iG_j}\right\|
 \leq \|V\|\tau_j.
$$
For $G$ Gaussian pulses, the total error is at most
$$
\|V\|\sum_{j=1}^{G}\tau_j.
$$
Choose $\sum_j\tau_j\leq\zeta/(2\|V\|)$, and use the other half of $\zeta$ for rational gate compilation. For equal durations this requires Gaussian amplitudes $O(G\|V\|/\zeta)$, up to the bounded norms of the intended gate generators. These are polynomial and explicitly charged. Controlled-phase waits under $V$ take time approximately $\pi/\chi$ each.

This proves bare local-density hardness with a fixed two-mode interacting impurity, a number-conserving quadratic bath, a Fock product input, and explicit finite controls. It also gives the stronger always-on version under its stated large-control promise. No difficult thermal state preparation or two-time correlation measurement is required.

For comparison, Jiang and collaborators prove driven impurity universality in a different encoding: their Theorem 7.10 and Eqs. (7.10)–(7.11) identify an easy encoded input and physical local $Z$ readout. The direct dual-rail construction above avoids relying on a vacuum input for a number-conserving model. [Jiang et al., arXiv:2610.02167v2, Sec. 7.3](https://arxiv.org/html/2610.02167v2#S7.SS3)

## 3. Causal cancellation of the actual feedback

Let a target bare trajectory obey
$$
\dot\sigma(t)=-i[D(t)+u(t)A,\sigma(t)].
$$
The function $u$ is supplied, piecewise Lipschitz, and has within-piece Lipschitz bound $L_u$. The complexity consequence uses $u=0$. The more general inequality below is an analytic extension, not an assumption of free evaluation of an arbitrary real function.

Assume a solver can return the terminal mean for every allowed input to (1). We construct an explicit source $b$ one interval at a time. Align a mesh with all supplied discontinuities and make every interval at most $h$ long. At its left endpoint $t_j$, obtain a report $\widehat m_j$ of the mean under the already fixed source prefix, clipped to $[-1,1]$. Define
$$
b(t)=u(t_j)-\lambda\widehat m_j,
\qquad t_j\leq t<t_{j+1}. \tag{3}
$$

Every query starts from the original supplied Fock state and receives its whole explicit source prefix. It is not given an intermediate quantum state. Future changes in the source have no effect on the earlier trajectory; the value assigned at the endpoint itself is irrelevant to the time-ordered propagator. Consequently, all queried left-endpoint means refer to the same final assembled nonlinear trajectory.

Because the measured operator and feedback operator coincide,
$$
\frac{d}{dt}m(t)
 =-i\,\operatorname{Tr}([A,D(t)]\rho(t))
$$
almost everywhere. The source and Hartree terms commute with $A$. Choose an explicitly computable certified bound
$$
B_A\geq\sup_t\|[D(t),A]\|.
$$
For example, twice the largest Pauli coefficient sum of a supplied $D$ pulse suffices; computing an exact many-body norm is unnecessary. The actual mean is globally $B_A$-Lipschitz. On the event that every report has error at most $\delta_{\rm red}$, the residual drive is therefore bounded by
$$
|b(t)+\lambda m(t)-u(t)|
 \leq L_u h+\lambda(B_Ah+\delta_{\rm red})+s. \tag{4}
$$
Here $s$ is an optional bound on source-coefficient rounding. One can set $s=0$: if $u(t_j)$, $\lambda$, and the finite reported mean are rational, (3) is computed as an exact rational product and sum with polynomial bit length.

Ordinary unitary Duhamel comparison between the actual nonlinear trajectory, viewed through its actual prescribed drive, and the target gives
$$
\boxed{
\|\rho_b(T)-\sigma(T)\|_1
\leq
2T\big[L_u h+\lambda B_Ah+
             \lambda\delta_{\rm red}+s\big].
} \tag{5}
$$

There is **no factor $e^{2\lambda T}$** in this reduction. At each step the source cancels the mean of the actual trajectory queried so far. It is not an independently guessed mean whose error is propagated by nonlinear stability.

For example, at $\kappa=1$, $u=0$, and a desired bare-observable accuracy $0<\varepsilon_{\rm red}<1$, take
$$
\delta_{\rm red}\leq\varepsilon_{\rm red}/16,\qquad
h\leq\frac{\varepsilon_{\rm red}}{16B_A},
\qquad
s\leq\frac{\varepsilon_{\rm red}}{16T}.
$$
When $B_A=0$ the step-size condition is unnecessary. Equation (5) is then at most $3\varepsilon_{\rm red}/8$; a final scalar query of accuracy $\varepsilon_{\rm red}/8$ leaves total error below $\varepsilon_{\rm red}$. These constants deliberately leave room for finite rounding. With exact rational sources the bound is smaller.

The mesh has
$$
N\leq K+O(TB_A/\varepsilon_{\rm red})
$$
intervals. In particular, for a constant bare decision gap the oracle accuracies can be fixed constants and the number of calls is polynomial in the circuit input.

## 4. Fixed horizon, finite tables, and adaptive confidence

### A terminal query can return an earlier mean

Every oracle call can have the **same $T,\lambda$, and $\kappa=1$**. To ask for $m(t_j)$, use the desired controls and source up to $t_j$, then turn $Q$ and $b$ off. In the switchable case turn the quartic term off too. In the always-on case leave $V=\chi n_un_v$. In either case the remaining Hamiltonian commutes with $A$, so
$$
m(t)=m(t_j)\quad\text{for all }t_j\leq t\leq T.
$$
Thus the ordinary terminal output is exactly the required earlier mean. This construction assumes the stated ability to halt the Gaussian controls; it does not assume a free variable-time readout primitive.

### Classical input construction is charged

After rounding each report to a rational within a fixed fraction of $\delta_{\rm red}$, each source coefficient requires
$$
O\!\left(B_{\rm in}+\log(1/\delta_{\rm red})\right)
$$
bits up to routine numerator/denominator arithmetic. The table of $N$ entries is explicit. It has bounded magnitude $|b|\leq\sup|u|+\lambda+s$, so cancellation does not require exponentially large source amplitudes.

Building all successive oracle inputs by copying the full growing prefix costs at worst
$$
O\!\left(N^2
[B_{\rm in}+\log(1/\delta_{\rm red})]\right)
$$
bit operations beyond the base-Hamiltonian descriptions. Including those descriptions in every call adds $O(NL_{\rm in})$. These are polynomial and do not assume random access to an implicit source function.

Suppose the hypothetical classical solver succeeds with probability at least $2/3$ for each input. Repeat it $O(\log(N/p_{\rm red}))$ times per query and take a median, reducing the conditional failure probability to $p_{\rm red}/O(N)$. This bound holds for each adaptively chosen input conditional on all earlier reports. A union bound makes all reports correct simultaneously with probability at least $1-p_{\rm red}$.

### Complexity consequence

Combining Sections 2–4, a uniform randomized classical polynomial-time estimator for all the stated impurity-feedback inputs at fixed $\kappa=1$ would simulate arbitrary polynomial-size quantum circuits with bounded error. Hence it would imply
$$
\mathrm{BPP}=\mathrm{BQP}.
$$

This implication is an **adaptive bounded-error polynomial-time Turing reduction** to a scalar estimation task. It is not a single-call reduction, and does not prove that every individual hard-source construction is hard to evaluate. Its source table can depend on earlier solver answers. The quantum algorithm in [Complete cost](complete-cost.md) is polynomial on this family, including all those same input resources.

The causal argument does not establish hardness for source-free models, fixed natural drive ensembles, equilibrium states, an immutable bath, or a constrained DMFT hybridization kernel. Section 6 establishes a different, specially controlled source-free corollary.

## 5. A nonlinear probe with an exact response

Place one logical dual rail in the two impurity modes $u,v$, with one particle in that pair, and decouple it from the bath. On that subspace $n_un_v=0$, even if the quartic interaction is always on. Let
$$
H_{\rm probe}=\frac{\lambda}{2}X_L+\lambda z(t)Z_L,
\qquad z(t)=\operatorname{Tr}(Z_L\rho(t)).
$$
Starting from either $Z_L$ eigenstate with eigenvalue $s=\pm1$, the Bloch solution is
$$
x(t)=\tanh^2(\lambda t),\qquad
y(t)=-s\,\operatorname{sech}(\lambda t)\tanh(\lambda t),
\qquad
z(t)=s\,\operatorname{sech}(\lambda t). \tag{6}
$$
Substitution into $\dot{\boldsymbol r}=2\boldsymbol h\times\boldsymbol r$ verifies the solution and its initial condition. Without the feedback term, the same probe gives $z(t)=s\cos(\lambda t)$. At integrated probe action near $1$, the two outputs differ by a fixed constant.

For two physical initial states under the same nonlinear equation,
$$
\|\rho(t)-\sigma(t)\|_1
 \leq e^{2\lambda t}\|\rho(0)-\sigma(0)\|_1. \tag{7}
$$
Indeed, write the difference in an interaction picture generated by either trajectory's actual Hermitian Hamiltonian, use
$$
|\operatorname{Tr}(A(\rho-\sigma))|
\leq\|\rho-\sigma\|_1,\qquad
\|[A,\sigma]\|_1\leq2,
$$
and apply Grönwall's inequality. The bound is independent of the norm of the common base Hamiltonian. In particular, it remains valid with an arbitrarily large common quartic interaction.

## 6. A direct source-free hardness corollary with an active probe

This subsection uses a stronger, explicitly charged control promise: the bare computation can be compressed into a short fixed interval by scaling **all required controls**, including the quartic interaction strength. It is not a fixed-$\chi$, bounded-strength, fixed-time statement.

Set
$$
T=\lambda=1,\qquad b(t)=0,\qquad
t_c=2^{-10},\qquad
\tau_p=1-t_c.
$$
To make the decision problem explicit, fix a polynomial resource cap in the ordinary input length $L_{\rm in}$, large enough for the compiler below. It bounds the numerical Hamiltonian norms, control amplitudes, pulse count, and coefficient bit lengths; $T=\lambda=1$ is fixed. Define the source-free promise problem $\mathsf{FeedbackSign}$ on these finite inputs by
$$
\begin{array}{ll}
\mathrm{YES}:&m(1)\geq1/2,\\
\mathrm{NO}:&m(1)\leq-1/2.
\end{array}
$$
Inputs between these two thresholds are outside the promise. This resource cap excludes exponentially large numerical controls merely described with short binary strings.

Amplify a quantum circuit so that its output bit is wrong with probability at most
$$
a_0=2^{-24}.
$$
Compile its dual-rail impurity implementation, including final routing of both output rails into $u,v$, with total bare operator-norm error at most
$$
\zeta=2^{-16}.
$$
Choose the output convention in which acceptance corresponds to the $Z_L=+1$ state. A fixed final logical $X$, included before the final routing and within the compilation budget, converts the usual acceptance-bit-$1$ convention when needed.

Compress that entire bare computation into $[0,t_c]$. Its pulse count and description length stay polynomial, while its control norms, including the quartic strength, grow polynomially and are charged.

For an always-on interaction, first construct the polynomial-time schedule from Section 2 with the stated fast Gaussian controls and error budget, then rescale the entire schedule. The resulting $\chi$ is constant in time but polynomially dependent on the instance. During the subsequent probe it acts as zero on the ideal one-particle impurity pair. A switchable interaction can instead be turned off during the probe.

During the computation interval, adding the actual source-free Hartree term perturbs the state in trace norm by at most $2t_c$, since $|m|\leq1$. The ideal amplified computation's global output state is within $2\sqrt{a_0}$ of a product of the correct pure output eigenstate and a normalized bath state. Compilation contributes at most $2\zeta$. Thus at the start of the probe the actual state is within
$$
d_0=2t_c+2\sqrt{a_0}+2\zeta
   =\frac{81}{32768}
$$
of that reference product state.

Now append the probe from Section 5 for duration $\tau_p$, with $\lambda=1$. Equations (6)–(7) imply
$$
\left|m(T)-s\,\operatorname{sech}(\tau_p)\right|
\leq e^{2\tau_p}d_0. \tag{8}
$$
The exact expressions give a terminal error bound below $0.0183$ and a sign margin greater than $0.63$. More conservatively, the elementary inequalities
$$
e^{2\tau_p}<7.4,\qquad
\operatorname{sech}(\tau_p)>0.648
$$
already give a sign margin greater than $5/8$. Therefore a single call estimating $m(T)$ to additive error $1/8$ decides the amplified circuit by its sign.

The transformation from the circuit to this finite source-free instance is deterministic and polynomial-time. It maps accepting circuits to the positive branch and rejecting circuits to the negative branch, with the stronger margin just proved. Thus it gives a **direct many-one reduction to $\mathsf{FeedbackSign}$** at $\kappa=1$. Conversely, the complete quantum upper bound at additive accuracy $1/8$ decides every promised input by its sign in polynomial time under the fixed resource cap. The problem is therefore BQP-complete in the standard promise-problem sense under this control contract.

### The final nonlinear stage affects the same measured output

Compare the actual final nonlinear probe with a probe that starts from the **same actual post-computation state**, uses the same base Hamiltonian, and has feedback removed only during the probe. Linear unitary evolution preserves the initial trace-distance error $d_0$, whereas the nonlinear probe has bound (8). Consequently their local means differ in magnitude by at least
$$
\operatorname{sech}(\tau_p)-\cos(\tau_p)
 -(e^{2\tau_p}+1)d_0
 >0.08. \tag{9}
$$
For example, $\cos(\tau_p)<0.542$, together with the conservative bounds above, already proves the final inequality. Using the exact expressions gives approximately $0.0867$.

Thus the measured hard-family output includes an active feedback effect, with a certified constant lower bound on that effect. The construction nevertheless consists of inherited universal quantum computation followed by an analytically solvable nonlinear transducer. It is not evidence that feedback itself creates hardness, that typical material drives encode circuits, or that an unconstrained natural-instance family has a practical quantum advantage.

## 7. Scope of the conditional advantage

The scalar task requires no full state reconstruction, no free state preparation, and no oracle for the unknown mean. Its quantum algorithm is fully charged, and a general efficient classical solver would collapse BQP to BPP under either the general causal theorem or the more specially controlled direct corollary.

This rules out a **universal polynomial-time analytic shortcut** for the admitted growing family under the usual complexity assumption. It does not prove an exponential classical runtime lower bound, an advantage at fixed small Hilbert-space dimension, a fixed-time bounded-norm local-light-cone instance, or a useful hardware crossover. It also does not contradict polynomial classical static-energy or thermal-impurity results, whose inputs and outputs differ from the driven states used here.

Ordinary Gaussian time-dependent Hartree–Fock is outside this hardness construction: the fixed impurity quartic term creates non-Gaussian quantum correlations. The bath remains quadratic; the scalar mean field couples to a genuine quantum impurity system whose internal entanglement is retained.
