# Certified spectral reconstruction of a scalar quantum mean field

## Result and scope

A scalar self-consistent field can be acquired with only logarithmically many polynomial coefficients per short time panel. The coefficient acquisition remains stable when every response is estimated with error. The proof uses complex-time analyticity of the exact local solution and a real-norm contraction for all computed iterates.

The result below is dimension independent as an analytic statement. It does not provide the response evaluations for free. Each evaluation starts from the supplied initial state and simulates the complete prescribed-field prefix. The [complete cost analysis](complete-cost.md) compiles and prices those evaluations, their inverses, numerical arithmetic, and scalar output.

### Input and notation

Let $`\mathcal H`$ be a finite-dimensional Hilbert space. Write $`\|X\|`$ for operator norm and $`\|X\|_1`$ for trace norm. Distances between density matrices below use the full trace norm, without a factor of $`1/2`$.

The input specifies:

**Time partition.** A time $`T>0`$ and $`K`$ nonempty pulse intervals with supplied boundaries

```math
0=\tau_0<\tau_1<\cdots<\tau_K=T.
```


**Hamiltonian pulses.** A Hermitian Hamiltonian $`B(t)=B_j`$ on each interval, with a certified bound

```math
\max_j\|B_j\|\le \Lambda.
```

A finite Pauli coefficient sum bound may be used for $`\Lambda`$. A supplied scalar source multiplying a fixed observable can be absorbed into $`B`$.

**Observables and state.** Fixed Hermitian operators $`A,O`$ with $`\|A\|,\|O\|\le1`$, a real coupling $`\lambda\ge0`$, and an initial density matrix $`\rho_0`$ with an explicit preparation procedure.

The target equation is
```math
\begin{aligned}
&\dot\rho(t)=-i[B(t)+\lambda m(t)A,\rho(t)],
\qquad
m(t)=\mathrm{Tr}(O\rho(t)),
\end{aligned}
\tag{1}
```
and the feedback action is
```math
\begin{aligned}
&\kappa=\lambda T.
\end{aligned}
\tag{2}
```

The principal output is a classical approximation to $`m(T)`$. The algorithm also produces a piecewise polynomial approximation to the whole mean curve. An additional bounded observable can be read out from the reconstructed prescribed-field evolution at the separately charged cost of one further response evaluation.

The pulse description consists of finite data. Those encoded coefficients and boundaries define the mathematical input. Errors in a different underlying physical model are separate from numerical errors in solving that input.

## The reconstruction theorem

Let $`0<\epsilon<1`$ and $`0\lt p<1`$. Choose a local error parameter
```math
\begin{aligned}
&\eta=\frac{\epsilon e^{-2\kappa}}{16}.
\end{aligned}
\tag{3}
```
It is harmless to replace $`\eta`$ by a computable dyadic lower approximation between $`\eta/2`$ and $`\eta`$.

Let $`I_q`$ denote interpolation of degree $`q`$ at the $`q+1`$ Chebyshev–Lobatto nodes on a panel. Let $`L_q`$ be any certified upper bound for its Lebesgue constant. A convenient analytic choice is
```math
\begin{aligned}
&L_q=2+\frac{2}{\pi}\log(q+1).
\end{aligned}
\tag{4}
```
An upward rational approximation to this bound can be used in every implementation formula. Alternatively, $`3+\lceil\log_2(q+1)\rceil`$ is an entirely integer, slightly more conservative choice. The relevant property is $`\|I_q f\|_\infty\le L_q\|f\|_\infty`$, with $`L_q=O(\log(q+1))`$. [ATAP]

Set
```math
\begin{aligned}
&q=\max\!\left\{1,\left\lceil\log_2\frac{128}{\eta}\right\rceil\right\},
\qquad
I=\left\lceil\log_2\frac{16L_q}{\eta}\right\rceil,
\end{aligned}
\tag{5}
```
and use nodal and coefficient-map error budgets
```math
\begin{aligned}
&\delta\le\frac{\eta}{64L_q},
\qquad
\beta\le\frac{\eta}{64}.
\end{aligned}
\tag{6}
```
Partition every supplied pulse interval into panels of length at most
```math
\begin{aligned}
&h_{\max}
=\min\left\{
\frac{1}{64(\Lambda+2\lambda)},
\frac{1}{4\lambda L_q}
\right\}.
\end{aligned}
\tag{7}
```
The second constraint is omitted when $`\lambda=0`$; the constant equation $`\Lambda=\lambda=0`$ is handled below.

For a finite subdivision, choose a rational $`\underline h`$ with
$`h_{\max}/2\le\underline h\le h_{\max}`$, and split each supplied pulse of length $`\Delta_j`$ into $`\lceil\Delta_j/\underline h\rceil`$ equal rational panels. Computable upper parameter bounds suffice to construct such a conservative width. This fixes the panel count before any response estimates are acquired.

On each panel, perform $`I`$ noisy collocation iterations as specified in the next section. Each iteration estimates $`q+1`$ prescribed-field means. Assume that each reported nodal value has conditional error at most $`\delta`$, with conditional failure probability at most $`p/J`$, where
```math
\begin{aligned}
&J=P(q+1)I
\end{aligned}
\tag{8}
```
and $`P`$ is the predetermined panel count. The coefficient computation must produce a real polynomial of degree $`q`$ whose sup-norm discrepancy from the exact interpolant of the clipped reports is at most $`\beta`$.

Let the ideal prepared initial state be $`\rho_{\rm prep}`$, with
```math
\begin{aligned}
&\|\rho_{\rm prep}-\rho_0\|_1\le\zeta.
\end{aligned}
\tag{9}
```
The statement permits $`\zeta=0`$, as for a specified product Fock state.

**Theorem.** With probability at least $`1-p`$, the algorithm constructs an explicit real piecewise polynomial $`p(t)`$ and its prescribed-field trajectory
```math
\begin{aligned}
&\dot{\widetilde\rho}(t)
=-i[B(t)+\lambda p(t)A,\widetilde\rho(t)],
\qquad
\widetilde\rho(0)=\rho_{\rm prep},
\end{aligned}
\tag{10}
```
such that, for $`0\le t\le T`$,
```math
\begin{aligned}
&\|\widetilde\rho(t)-\rho(t)\|_1
\le e^{2\lambda t}\zeta+\eta(e^{2\lambda t}-1),
\end{aligned}
\tag{11}
```
and, with either one-sided value at a panel boundary,
```math
\begin{aligned}
&|p(t)-m(t)|\le e^{2\lambda t}(\zeta+\eta).
\end{aligned}
\tag{12}
```

In particular, if $`\zeta\le\eta`$, returning the final polynomial endpoint with rounding error at most $`\epsilon/4`$ gives additive error less than $`\epsilon`$. The constants above leave substantial slack: the reconstruction and initial-state contributions to (12) total at most $`\epsilon/8`$.

The panel count can be bounded explicitly by
```math
\begin{aligned}
&P\le K+128T\Lambda+256\kappa+8\kappa L_q.
\end{aligned}
\tag{13}
```
Indeed $`P\le K+T/\underline h\le K+2T/h_{\max}`$, and the maximum defining $`h_{\max}^{-1}`$ is at most $`64(\Lambda+2\lambda)+4\lambda L_q`$.
Consequently,
```math
\begin{aligned}
q&=O(\kappa+\log(1/\epsilon)),\\
I&=O(\kappa+\log(1/\epsilon)+\log L_q),\\
P&=O(K+T\Lambda+\kappa L_q).
\end{aligned}
\tag{14}
```
There are $`J`$ scalar response evaluations and $`O(Pq)`$ retained real coefficients. The response precision is
```math
\begin{aligned}
&\delta=\Theta\!\left(\frac{\epsilon e^{-2\kappa}}{L_q}\right).
\end{aligned}
\tag{15}
```

All bounds are uniform in the Hilbert-space dimension and in the physical state reached at a panel boundary. They do not imply that the required response evaluations are classically efficient.

## Algorithm: the state at a panel boundary is a paid prefix

Suppose panels $`0,\ldots,k-1`$ already have stored polynomials $`p_0,\ldots,p_{k-1}`$. Define $`\sigma_k`$ to be the exact state obtained from $`\rho_{\rm prep}`$ by their prescribed-field evolution up to the start of panel $`k`$. This is a mathematical definition of a known circuit input, not a free copy of an unknown intermediate state.

For any real continuous function $`v`$ on the current panel of length $`h_k`$, let
```math
\begin{aligned}
&F_{\sigma_k}(v)(s)
=\mathrm{Tr}\!\left[
O\,U_v(s)\sigma_k U_v(s)^\dagger
\right],
\quad
0\le s\le h_k,
\end{aligned}
\tag{16}
```
where $`U_v`$ is the ordinary unitary propagator of $`B_j+\lambda v(s)A`$ on that panel.

Start the current polynomial at $`v_0=0`$. For $`r=0,\ldots,I-1`$:

1. Estimate $`F_{\sigma_k}(v_r)`$ at the $`q+1`$ Chebyshev–Lobatto nodes. Every evaluation prepares the original state and replays the complete stored prefix, followed by the current partial panel under $`v_r`$.
2. Clip each reported scalar to $`[-1,1]`$.
3. Compute and store real polynomial coefficients for the interpolant of those reports, with coefficient-map error at most $`\beta`$. The resulting finite coefficient list defines $`v_{r+1}`$.

Set $`p_k=v_I`$. The next panel's state $`\sigma_{k+1}`$ is defined using this final stored polynomial, not the polynomial used in the preceding nodal evaluations.

No state is transferred between response evaluations. All measurement histories and polynomial coefficients are classical. The argument below is conditional on the preceding history, so it applies to this adaptive construction.

## Proof, part 1: physical existence and dimension-independent analyticity

On each pulse interval the vector field in (1) is locally Lipschitz on finite-dimensional matrix space and preserves Hermiticity. Along a solution starting from a density matrix, the Hamiltonian is therefore Hermitian. Treating that time-dependent Hamiltonian as given shows that the solution is unitary conjugation of its initial state. Thus positivity, trace one, and $`\|\rho(t)\|_1=1`$ are preserved, and no finite-time blowup occurs on a bounded interval. Concatenating the pulse solutions gives the unique continuous physical solution. Hamiltonian values at isolated pulse boundaries do not change the propagator.

For the quantitative complex-time bound, start at any physical state $`\sigma`$ at the left end of a panel and continue the current constant $`B_j`$ as a constant across a complex neighborhood. Define
```math
\begin{aligned}
&\mathcal V(R)=-i[B_j+\lambda\mathrm{Tr}(OR)A,R].
\end{aligned}
\tag{17}
```
This is a holomorphic polynomial in the entries of $`R`$. The use of a complex matrix $`R`$, rather than a wavefunction and its conjugate, is useful here.

On the trace-norm ball $`\|R-\sigma\|_1\le1`$, one has $`\|R\|_1\le2`$. The inequalities
```math
\begin{aligned}
&|\mathrm{Tr}(OR)|\le\|R\|_1,
\qquad
\|[X,Y]\|_1\le2\|X\|\|Y\|_1
\end{aligned}
\tag{18}
```
give
```math
\begin{aligned}
&\|\mathcal V(R)\|_1\le4\Lambda+8\lambda,
\end{aligned}
\tag{19}
```
and, for two matrices in the ball,
```math
\begin{aligned}
&\|\mathcal V(R)-\mathcal V(S)\|_1
\le(2\Lambda+8\lambda)\|R-S\|_1.
\end{aligned}
\tag{20}
```

Take
```math
\begin{aligned}
&r_*=\frac{1}{16(\Lambda+2\lambda)}.
\end{aligned}
\tag{21}
```
On the Banach space of matrix functions holomorphic in $`|z|\lt r_*`$, continuous on its closure, and within unit sup trace distance of $`\sigma`$, the complex Picard map
```math
\begin{aligned}
&\mathcal P(R)(z)
=\sigma+\int_0^z \mathcal V(R(w))\,dw
\end{aligned}
\tag{22}
```
maps the ball into itself. Indeed its displacement is at most
```math
r_*(4\Lambda+8\lambda)=\frac14.
```
It is a contraction with factor at most
```math
r_*(2\Lambda+8\lambda)\le\frac14.
```
The integrand is holomorphic and the integral may be taken along the straight segment. The fixed point is holomorphic, satisfies $`\|R(z)\|_1\le2`$, and agrees with the physical solution for real $`z`$ by uniqueness. Its mean
```math
\begin{aligned}
&m_\sigma(z)=\mathrm{Tr}(OR(z))
\end{aligned}
\tag{23}
```
is therefore holomorphic and bounded by $`2`$ on that disk.

Equation (7) implies $`h_k\le r_*/4`$. For the interval $`[0,h_k]`$, the Bernstein ellipse with parameter $`2`$ has farthest point from $`0`$ at distance $`9h_k/8\lt r_*`$. The analytic Chebyshev interpolation estimate with bound $`2`$ consequently gives [ATAP, Theorem 8.2]
```math
\begin{aligned}
&\|m_\sigma-I_qm_\sigma\|_\infty
\le8\,2^{-q}.
\end{aligned}
\tag{24}
```

This analytic continuation is that of the current pulse equation. It need not coincide with the preceding or following pulse equation outside the panel. Only the mean on the panel is interpolated.

## Proof, part 2: contraction uses only real-time unitarity

For two prescribed real functions $`v,w`$, Duhamel's identity and unitary invariance of trace norm imply
```math
\begin{aligned}
&\|\rho_{\sigma,v}(s)-\rho_{\sigma,w}(s)\|_1
\le2\lambda\int_0^s|v(u)-w(u)|\,du.
\end{aligned}
\tag{25}
```
It follows that
```math
\begin{aligned}
&\|F_\sigma(v)-F_\sigma(w)\|_\infty
\le2\lambda h_k\|v-w\|_\infty.
\end{aligned}
\tag{26}
```
This bound holds for arbitrary real continuous $`v,w`$. No complex-time bound, analyticity promise, or physical-state interpretation is required of the proxies.

The finite-dimensional map
```math
\begin{aligned}
&\mathcal C_\sigma(v)=I_qF_\sigma(v)
\end{aligned}
\tag{27}
```
on the space of real polynomials of degree at most $`q`$ has contraction factor
```math
\begin{aligned}
&\theta_k=2\lambda h_kL_q\le\frac12.
\end{aligned}
\tag{28}
```
Hence it has a unique fixed polynomial $`v_\sigma^*`$. Since all real-time responses lie in $`[-1,1]`$,
```math
\begin{aligned}
&\|v_\sigma^*\|_\infty\le L_q.
\end{aligned}
\tag{29}
```

The exact nonlinear mean obeys $`m_\sigma=F_\sigma(m_\sigma)`$. Although $`m_\sigma`$ need not be a polynomial, the Lipschitz bound (26) also compares it with $`v_\sigma^*`$. Thus
```math
\begin{aligned}
\|v_\sigma^*-m_\sigma\|_\infty
&\le\theta_k\|v_\sigma^*-m_\sigma\|_\infty
  +\|I_qm_\sigma-m_\sigma\|_\infty,\\
\|v_\sigma^*-m_\sigma\|_\infty
&\le16\,2^{-q}.
\end{aligned}
\tag{30}
```

Only the exact local mean entered the analytic approximation estimate. The contraction controls every noisy iterate in a real norm.

## Proof, part 3: measurement and coefficient errors

Clipping a reported value to $`[-1,1]`$ cannot increase its error relative to the exact physical response. If all nodal errors in a round are at most $`\delta`$, and the stored polynomial differs from their ideal interpolant by at most $`\beta`$, then
```math
\begin{aligned}
&\|v_{r+1}-\mathcal C_\sigma(v_r)\|_\infty
\le L_q\delta+\beta.
\end{aligned}
\tag{31}
```
Starting from $`v_0=0`$, equations (28)–(29) give
```math
\begin{aligned}
&\|v_I-v_\sigma^*\|_\infty
\le\theta_k^I L_q+
\frac{L_q\delta+\beta}{1-\theta_k}.
\end{aligned}
\tag{32}
```
The choices (5)–(6) imply
```math
16\,2^{-q}\le\frac{\eta}{8},\qquad
\theta_k^I L_q\le\frac{\eta}{16},\qquad
\frac{L_q\delta+\beta}{1-\theta_k}\le\frac{\eta}{16}.
```
Therefore
```math
\begin{aligned}
&\|p_k-m_{\sigma_k}\|_\infty\le\frac{\eta}{4}\le\eta.
\end{aligned}
\tag{33}
```
We retain the simpler bound $`\eta`$ in the global statement.

Every stored iterate has a separate a priori real bound. It is within $`\beta`$ of the interpolant of values in $`[-1,1]`$, so
```math
\begin{aligned}
&\|v_r\|_\infty\le L_q+\beta\le2L_q
\end{aligned}
\tag{34}
```
for $`r\ge1`$, and $`v_0=0`$. This bound is independent of earlier measurement errors once clipping and the coefficient accuracy requirement are enforced.

## Proof, part 4: global error from local physical prefixes

Let $`\Phi_s`$ denote exact nonlinear evolution on the current pulse. For density matrices $`\rho,\sigma`$, use the Hamiltonian of one solution as the unitary reference. The remaining field difference is bounded by $`\lambda\|\Phi_s(\rho)-\Phi_s(\sigma)\|_1`$, so Grönwall's inequality gives
```math
\begin{aligned}
&\|\Phi_s(\rho)-\Phi_s(\sigma)\|_1
\le e^{2\lambda s}\|\rho-\sigma\|_1.
\end{aligned}
\tag{35}
```
There is no factor involving the norm of $`B_j`$ in this real-time stability estimate.

On a panel, compare its prescribed-field trajectory from $`\sigma_k`$ with exact nonlinear evolution from the same $`\sigma_k`$. Equation (25), with one prescribed field replaced by the already existing exact mean $`m_{\sigma_k}`$, gives
```math
\begin{aligned}
&\|\rho_{\sigma_k,p_k}(s)-\Phi_s(\sigma_k)\|_1
\le2\lambda s\eta.
\end{aligned}
\tag{36}
```
This comparison does not assume an oracle for that exact mean.

Write $`t_k`$ for the panel start and
```math
D_k=\|\sigma_k-\rho(t_k)\|_1.
```
At the panel endpoint,
```math
\begin{aligned}
&D_{k+1}\le e^{2\lambda h_k}D_k+2\lambda h_k\eta.
\end{aligned}
\tag{37}
```
Since $`2\lambda h_k\le e^{2\lambda h_k}-1`$, iteration telescopes to
```math
\begin{aligned}
&D_k\le e^{2\lambda t_k}\zeta+
\eta(e^{2\lambda t_k}-1).
\end{aligned}
\tag{38}
```
The same argument with a partial last panel proves (11).

For the mean table itself, compare $`p_k(t_k+s)`$ first with $`m_{\sigma_k}(s)`$, and then compare the two exact nonlinear trajectories:
```math
\begin{aligned}
&|p_k(t_k+s)-m(t_k+s)|
\le\eta+e^{2\lambda s}D_k
\le e^{2\lambda(t_k+s)}(\eta+\zeta).
\end{aligned}
\tag{39}
```
This proves (12).

All local inequalities hold for every physical $`\sigma_k`$, including the state determined by any preceding successful measurement history. The panel and iteration counts are fixed before those measurements. A conditional union bound over the $`J`$ nodal calls therefore makes all the estimates hold simultaneously with probability at least $`1-p`$. Independence between different adaptive calls is unnecessary.

## Finite precision and the response-evaluation interface

### Stored coefficients define the computed field

On a panel use the normalized coordinate $`x=2s/h_k-1`$. At nodes $`x_j=\cos(j\pi/q)`$, let $`y_j\in[-1,1]`$ be the clipped finite reports. The exact Chebyshev coefficients of their interpolant are
```math
\begin{aligned}
&c_\ell=\frac{2w_\ell}{q}
\sum_{j=0}^{q}w_jy_j
\cos\frac{\pi\ell j}{q},
\qquad
w_0=w_q=\frac12,\quad w_j=1\ \ (0\lt j\lt q).
\end{aligned}
\tag{40}
```
They satisfy $`|c_\ell|\le2`$ and
```math
\begin{aligned}
&\sum_{\ell=0}^{q}|c_\ell|\le2(q+1).
\end{aligned}
\tag{41}
```
Compute finite real coefficients $`\widehat c_\ell`$ with
```math
\begin{aligned}
&\sum_{\ell=0}^{q}|\widehat c_\ell-c_\ell|\le\beta.
\end{aligned}
\tag{42}
```
Because $`|T_\ell(x)|\le1`$ on $`[-1,1]`$, (42) implies the required coefficient-map error. A direct cosine transform takes $`O(q^2)`$ arithmetic operations. It can meet (42) with a number of fractional bits polynomial in $`\log(q+1)+\log(1/\beta)`$; input reports and panel boundaries retain their own bit lengths.

The exact computed field is
```math
\begin{aligned}
&\widehat p(x)=\sum_{\ell=0}^{q}\widehat c_\ell T_\ell(x).
\end{aligned}
\tag{43}
```
Its coefficient-rounding error is counted once, as $`\beta`$ in (31). Numerical simulation or reversible evaluation of this already stored polynomial is a different operation; its error belongs to the nodal response budget $`\delta`$.

### What a nodal guarantee includes

A nodal response procedure must bound its total discrepancy from the exact expectation for the stored real polynomial and the ideal complete prefix. That total includes:

- Statistical or amplitude-estimation error.
- Bias from implementing the supplied initial preparation and complete prefix.
- Prescribed-Hamiltonian simulation and gate-synthesis error.
- Numerical evaluation of the already stored polynomial.
- Approximation of the requested Chebyshev node time.

These contributions can be assigned fixed fractions of $`\delta`$. A guarantee only on the measurement's sampling error is insufficient.

For node times, the exact prescribed response satisfies
```math
\begin{aligned}
&\left|\frac{d}{ds}F_\sigma(v)(s)\right|
\le2(\Lambda+\lambda\|v\|_\infty)
\le2(\Lambda+2\lambda L_q).
\end{aligned}
\tag{44}
```
An absolute time error at most a prescribed fraction of
$`\delta/[2(\Lambda+2\lambda L_q)]`$ therefore fits its bias budget. Endpoints may be represented exactly by the supplied rational boundaries, and interior approximations can be clamped to their panel. Exact irrational node access is unnecessary.

Positive pulse lengths can be subdivided into equal rational subpanels, with their number chosen using upward bounds for the quantities in (7). Their smallest length affects numerical bit lengths and timing precision; it does not create an uncharged exact-time oracle.

The reference state $`\rho_{\rm prep}`$ in (9) is fixed. Its discrepancy from the requested $`\rho_0`$ is amplified globally as in (11). Any additional error incurred while implementing a fresh copy of that reference preparation is instead part of the corresponding nodal bias. This keeps the two roles separate.

### Accounting consequence

Let $`C_{\rm response}(\delta,p/J)`$ be a fully implemented cost for one such scalar expectation, including its complete prefix. The reconstruction uses at most
```math
\begin{aligned}
&J\,C_{\rm response}(\delta,p/J)
\end{aligned}
\tag{45}
```
of that cost, plus input reading, $`O(Jq)`$ coefficient-processing arithmetic operations, coefficient storage, circuit construction, and final rounding. The retained mean table uses $`O(Pqb)`$ classical bits when coefficients have $`b`$-bit precision.

If the compiled response primitive has inverse-linear precision cost, then (14)–(15) preserve an inverse-linear power of $`1/\epsilon`$, with logarithmic factors at fixed model parameters. The implementation and its other parameter dependence are established in the [complete cost analysis](complete-cost.md). Equation (45) alone is an interface statement rather than a free-oracle complexity claim.

## Edge cases and extensions

**Zero elapsed time.** For $`T=0`$, the target is $`\mathrm{Tr}(O\rho_0)`$. Estimate it directly using the supplied initial preparation, charging that operation. No time table is needed.

**Constant equation.** If $`\Lambda=\lambda=0`$, the state is constant. One initial expectation estimate suffices; it is not supplied for free.

**No feedback.** If $`\lambda=0`$, the reconstruction theorem remains valid with contraction factor zero. For a terminal-only target the more economical method is one ordinary prescribed-dynamics response evaluation.

**Negative scalar coupling.** A real negative coupling can be written with $`|\lambda|`$ and $`A`$ replaced by $`-A`$. All action and error bounds then use $`|\lambda|T`$.

**Discontinuities.** Every supplied jump must be a panel boundary. The state and exact mean are continuous there; the polynomial table may have a small jump, and either one-sided table value satisfies (12).

**Several fields.** For
```math
\begin{aligned}
&H(t)=B(t)+\sum_{a=1}^{d}\lambda_a m_a(t)A_a,
\qquad
m_a(t)=\mathrm{Tr}(O_a\rho(t)),
\end{aligned}
\tag{46}
```
with bounded Hermitian $`A_a,O_a`$, replace $`\lambda`$ everywhere by
$`\lambda_{\rm tot}=\sum_a|\lambda_a|`$, and use the maximum norm on the mean vector. Equations (19), (20), (26), and (35) have the same bounds with this replacement. Interpolate and clip componentwise. The node count becomes $`dP(q+1)I`$, and the stored table has $`O(dPq)`$ coefficients. Preparation and measurement costs for every $`O_a`$, and Hamiltonian evaluation costs for every $`A_a`$, must be charged. The constants do not hide an unbounded number of fields.

**More general time dependence.** Piecewise polynomial or analytic supplied $`B(t)`$ can be treated with an appropriate complex-neighborhood norm bound and its computation charged. A real-axis norm bound by itself is not a substitute for that extra analytic hypothesis. The theorem proved here requires only piecewise constant $`B`$.

## Interpretation

The approximation dimension concerns time dependence of a few observables. It does not assert that the many-body state has a small classical representation, or that the nodal responses can be evaluated classically from their short descriptions.

The stability factor $`e^{2\kappa}`$ is explicit. Thus the theorem's efficient quantum window includes $`\kappa=O(\log N)`$ when all other charged resources and $`1/\epsilon`$ are polynomial in an input-size parameter $`N`$. It makes no uniform polynomial claim for arbitrarily large $`\kappa`$.

Analytic Chebyshev approximation, Duhamel bounds, and contraction with inexact evaluations are standard ingredients. The result here is their joint application to an acquired self-consistent quantum field with a consistent physical prefix, finite coefficients, and one final classical scalar. The [classical boundary](classical-boundary.md) identifies regimes in which the same response and reconstruction task is already classically tractable.

## References

- **[ATAP]** Lloyd N. Trefethen, *Approximation Theory and Approximation Practice*, SIAM, 2013. Theorem 8.2 gives analytic Chebyshev interpolation error; Theorem 15.2 gives the Chebyshev–Lobatto Lebesgue-constant bound. [Author's sample](https://people.maths.ox.ac.uk/trefethen/trefethen_sample.pdf); [2013 text](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf).
