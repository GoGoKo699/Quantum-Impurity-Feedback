# Classical boundary: Gaussian dynamics and bounded impurity action

## Why two actions are needed

The self-consistent feedback action and the interacting impurity action govern different costs:
```math
\kappa=\lambda T,
\qquad
S=\int_0^T\sum_a|v_a(t)|\,dt.
\tag{1}
```
Here the non-Gaussian interaction has a specified expansion
```math
V(t)=\sum_a v_a(t)M_a
\tag{2}
```
into normalized Hermitian even Majorana monomials.

The quantum [complete cost bound](complete-cost.md) retains polynomial dependence on the supplied Hamiltonian normalization, time, and description. It therefore pays polynomially for growing $`S`$, while its feedback-stability factor is exponential in $`\kappa`$.

This page proves a complementary classical upper bound. For Gaussian initial states and quadratic prescribed feedback, a direct Dyson/Wick estimator costs exponentially in $`S`$, with all its other work explicit and polynomial. Combining it with the same certified feedback reconstruction gives
```math
\widetilde O\!\left(
J\,e^{4(S+\kappa)}L_q^2\epsilon^{-2}C_{\rm Wick}
\right),
\tag{3}
```
where $`J`$, $`L_q`$, and the polynomial factor $`C_{\rm Wick}`$ are defined below.

Thus bounded impurity action is already a classical regime, even for a large bath. The exponential dependence in (3) is a feature of one conservative algorithm. It is not a lower bound for all classical methods.

## 1. The input subclass

There are $`n`$ complex fermionic modes with Majoranas
```math
\gamma_1,\ldots,\gamma_{2n},
\qquad
\{\gamma_j,\gamma_k\}=2\delta_{jk}I.
\tag{4}
```
The prescribed-field Hamiltonian is
```math
H_p(t)=Q_p(t)+V(t),
\qquad
Q_p(t)=Q_0(t)+[b(t)+\lambda p(t)]A.
\tag{5}
```
The assumptions for the classical bound are:

- $`Q_0`$ and $`A`$ are quadratic fermionic operators, apart from irrelevant scalar multiples of identity. The supplied $`Q_0,b,V`$ are piecewise constant on an explicit finite pulse list.
- The interaction $`V`$ acts on a fixed number of impurity modes. Its supplied or explicitly computed expansion (2) contains a fixed number of even monomials, each of bounded degree $`d_0`$. A phase in $`\{1,-1,i,-i\}`$ makes every $`M_a`$ Hermitian and unitary, so $`\|M_a\|=1`$, and the coefficients $`v_a`$ are real.
- Identity and quadratic terms may be absorbed into $`Q_0+bA`$. Define
  ```math
  v(t)=\sum_a|v_a(t)|,\qquad S_\tau=\int_0^\tau v(t)\,dt,\qquad S=S_T.
  \tag{6}
  ```
  This is a bound for a declared decomposition; it is not asserted to be an intrinsic optimum over all representations.
- The initial state $`\rho_0`$ is Gaussian and has an explicitly computable two-point matrix
  ```math
  C^{(0)}_{jk}=\mathrm{Tr}(\rho_0\gamma_j\gamma_k).
  \tag{7}
  ```
  The main example is a specified product Fock state, including one fermion per encoded pair. Its two-point matrix is immediate from the occupation string.
- The target $`O`$ and feedback observable $`A`$ are centered single-mode occupations, or fixed quadratic Majorana monomials of norm at most one. Fixed finite linear combinations can be included by charging their coefficient sums and component counts.
- The known proxy $`p`$ is real and piecewise polynomial of degree at most $`q`$, with explicit finite coefficients on $`P`$ panels. The reconstruction algorithm guarantees
  ```math
  \|p\|_\infty\le2L_q,\qquad
  \sum_{\ell=0}^q|\widehat c_\ell|\le2(q+1)+\beta
  \tag{8}
  ```
  on every panel, where $`\beta<1`$.

All pulse boundaries, coefficient lists, probability computations, and one-body matrices are paid classical data. No interacting-state preparation or measurement oracle is used by the classical estimator.

For example, with
```math
n_j=\frac{I+i\gamma_{2j-1}\gamma_{2j}}{2},
```
a density interaction $`\chi(t)n_1n_2`$ has one quartic term of magnitude $`|\chi(t)|/4`$, after its identity and quadratic parts are absorbed into $`Q_p`$. This choice gives
```math
S=\frac14\int_0^T|\chi(t)|\,dt.
\tag{9}
```
The centered density $`1-2n_j`$ is quadratic, so adding its mean field does not increase $`S`$.

## 2. The exact Gaussian subcase

If $`V=0`$, every prescribed trajectory is Gaussian. The same is true of the self-consistent trajectory: at each real time its Hamiltonian is quadratic, so its evolution is a Gaussian unitary.

Let $`R(t)`$ be the real orthogonal matrix satisfying
```math
G(t)^\dagger\gamma_jG(t)=\sum_\ell R_{j\ell}(t)\gamma_\ell.
\tag{10}
```
Its generator is a known $`2n`$-dimensional real antisymmetric matrix $`K(t)`$, and
```math
\dot R(t)=K(t)R(t),\qquad R(0)=I.
\tag{11}
```
The covariance evolves by the corresponding matrix conjugation. Centered local occupations are entries of that covariance. With self-consistent quadratic feedback, this is a closed nonlinear matrix equation on $`O(n^2)`$ real data.

Consequently the Gaussian subclass has a direct classical representation. The spectral feedback procedure can also be executed classically, using deterministic one-body propagation for each nodal response. Neither a large Fock-space dimension nor nonzero scalar feedback establishes an advantage in this subclass. The Gaussian simulation and Wick/Pfaffian primitives used here are standard. [TD]

There are also constant-response cases even when $`V\ne0`$. The maximally mixed state commutes with every Hamiltonian and therefore remains fixed; its centered one-time charge is zero. In a number-conserving model, the vacuum and completely filled sectors are each one dimensional, so their occupations are constant as well. The half-filled product state used by the encoded computation avoids these particular degeneracies. Hardness of a two-time correlation from a different initial state does not by itself establish hardness of the present one-time charge.

## 3. A prescribed interacting response as an expectation over words

Fix a proxy $`p`$ and a target time $`\tau\le T`$. Let $`G_p`$ be the Gaussian propagator of $`Q_p`$. In its interaction picture,
```math
M_a^I(t)=G_p(t)^\dagger M_aG_p(t),\qquad
O^I(\tau)=G_p(\tau)^\dagger OG_p(\tau),
\tag{12}
```
and
```math
U_I(\tau)=\mathcal T\exp\left[-i\int_0^\tau V_I(t)\,dt\right].
\tag{13}
```
Each $`M_a^I(t)`$ is still a product of at most $`d_0`$ transformed Majoranas.

Assume first that $`S_\tau>0`$. Generate a random word as follows:

1. Draw $`k`$ from a Poisson distribution of mean $`S_\tau`$.
2. Draw $`k`$ independent times with density $`v(t)/S_\tau`$ on $`[0,\tau]`$, and sort them into increasing order.
3. At each time $`t_j`$, choose a label $`a_j`$ with probability $`|v_{a_j}(t_j)|/v(t_j)`$.
4. Set
   ```math
   W=(-i)^k
   \left(\prod_{j=1}^k\mathrm{sgn}v_{a_j}(t_j)\right)
   M_{a_k}^I(t_k)\cdots M_{a_1}^I(t_1).
   \tag{14}
   ```

Zero-weight times and labels are never selected. The empty word is $`I`$. Every word is unitary up to its explicitly known phase.

**Lemma 1: Poisson representation.**
```math
U_I(\tau)=e^{S_\tau}\mathbb E W.
\tag{15}
```

To verify the identity, condition on $`k`$. Sorting $`k`$ independent times multiplies their density on the ordered simplex by $`k!`$. This cancels the $`k!`$ in the Poisson probability; the powers of $`S_\tau`$, the factors $`v(t)`$, and the label probabilities then reproduce exactly the $`k`$-th Dyson term. The factor $`e^{-S_\tau}`$ is common to all terms. The series is absolutely convergent in operator norm because its norm sum is bounded by $`e^{S_\tau}`$.

Take two independent words $`W,W'`$. The prescribed response is
```math
\begin{aligned}
F_p(\tau)
&=\mathrm{Tr}\!\left[
\rho_0 U_I(\tau)^\dagger O^I(\tau)U_I(\tau)
\right]\\
&=e^{2S_\tau}\mathbb E Z,
\qquad
Z=\mathrm{Re}\mathrm{Tr}
\!\left[\rho_0 W^\dagger O^I(\tau)W'\right].
\end{aligned}
\tag{16}
```
Since $`\rho_0`$ is a density matrix and the operator in its expectation has norm at most one,
```math
|Z|\le1.
\tag{17}
```
The two words are sampled independently; replacing them by one shared word would not reproduce (16).

If $`S_\tau=0`$, use Gaussian propagation directly. No Poisson distribution with zero denominator needs to be formed.

The expansion is a simple independent-sampling version of established real-time interaction-picture and Keldysh diagrammatic methods. [WOM] The bounds here use the coefficient envelope and norm-one words rather than a favorable average sign, an assumed Markov-chain mixing time, or a model-specific resummation.

## 4. Wick evaluation of one word pair

A word pair with $`N=k+\ell`$ total interaction insertions contains at most
```math
d_0N+2
\tag{18}
```
Majorana factors, including the quadratic observable. Each factor is a real linear combination
```math
\gamma(u)=\sum_j u_j\gamma_j
\tag{19}
```
obtained from a row of the appropriate one-body propagator. For exact real-time propagation, $`\|u\|_2=1`$ and $`\|\gamma(u)\|=1`$.

The ordered product expectation in a Gaussian state is the Pfaffian of the antisymmetric contraction matrix. For ordered factor vectors $`u_1,\ldots,u_{2r}`$, its entries above the diagonal are
```math
\mathsf C_{ij}=u_i^T C^{(0)}u_j,\qquad i<j,
\tag{20}
```
with $`\mathsf C_{ji}=-\mathsf C_{ij}`$ and zero diagonal. Multiplying the Pfaffian by the word and observable phases gives the complex expectation in (16). [TD, Sections III–V]

The matrix has size $`O(d_0N+1)`$, not size $`2^n`$. Its contractions cost polynomial time in $`n`$ and $`N`$, and its Pfaffian has polynomial arithmetic complexity. Initial covariance construction, vector transformations, contractions, and the Pfaffian are all charged.

### Absolute numerical accuracy without a pivot promise

Let the word length be bounded by $`M`$, and let the resulting Pfaffian matrix have dimension $`2r\le d_0M+2`$. Each exact contraction has magnitude at most one. The Pfaffian expansion has
```math
(2r-1)!!
\tag{21}
```
terms, each a product of $`r`$ contractions. If each contraction is approximated to absolute accuracy $`\xi\le1/r`$, a direct product bound gives a Pfaffian perturbation at most
```math
e\,r(2r-1)!!\,\xi.
\tag{22}
```
Therefore a word expectation can be evaluated to absolute accuracy
$`\delta e^{-2S}/c`$ using a number of fractional bits
```math
O\!\left(
r\log(r+1)+S+\log(1/\delta)
\right),
\tag{23}
```
plus the input and contraction-arithmetic bit lengths. This intentionally loose bound suffices for polynomial bit complexity.

Use rational approximations for the contractions and compute their Pfaffian by exact or fraction-free elimination. A nonzero off-diagonal entry can be moved to the first $`2\times2`$ block by a simultaneous row and column permutation. For
```math
\mathsf C=
\begin{pmatrix}
0&a&u^T\\
-a&0&v^T\\
-u&-v&D
\end{pmatrix},
```
the recursion is
```math
\mathrm{Pf}(\mathsf C)
=a\mathrm{Pf}
\left(D+\frac{vu^T-uv^T}{a}\right),
\tag{24}
```
with the permutation sign retained. An all-zero remaining matrix has zero Pfaffian unless its dimension is zero. Fraction-free implementations keep intermediate numerator and denominator lengths polynomial in $`r`$ and the rational input bit length, as can also be bounded by the corresponding Pfaffian minors. A floating-point lower bound on the pivots is unnecessary.

Approximation error in the one-body propagators and initial contractions is included before applying (22). The final numerical real word value may be clipped to $`[-1,1]`$; this cannot increase its discrepancy from the exact $`Z`$.

## 5. Truncation, sampling precision, and nodal cost

The total number $`N`$ of insertions in two independent Poisson words is Poisson with mean $`2S_\tau`$. Since
```math
\mathbb E\,2^N=e^{2S_\tau},
\tag{25}
```
Markov's inequality gives
```math
e^{2S_\tau}\Pr(N>M)
\le e^{4S_\tau}2^{-M}.
\tag{26}
```
For nodal target error $`0<\delta<1`$, choose
```math
M=
\left\lceil
\frac{4S+\log(8/\delta)}{\log2}
\right\rceil.
\tag{27}
```
Return zero whenever $`N>M`$. This introduces bias at most $`\delta/8`$ and makes the work of every accepted trial polynomially bounded.

The truncated distribution can be sampled from a finite table containing probabilities for $`N=0,\ldots,M`$ and the remaining tail. Conditional branch labels, or equivalently two separate word lengths, reproduce independent forward and backward Poisson words. Finite probability tables with total variation error $`\xi_{\rm prob}`$ change the scaled expectation by at most
```math
2e^{2S}\xi_{\rm prob}.
\tag{28}
```
Choosing $`\xi_{\rm prob}\le\delta e^{-2S}/16`$ fits another $`\delta/8`$ budget. The required probability precision has polynomial bit length in $`S`$, $`\log(1/\delta)`$, the table sizes, and the supplied coefficient bit lengths. This sampling has a known independent distribution; there is no mixing-time assumption.

### Finite time samples

Because $`v(t)`$ is piecewise constant, a time sample is generated by selecting a pulse interval with probability proportional to $`v_j\Delta t_j`$, then drawing a uniform time within that interval. For each branch, round the times by a monotone midpoint-grid map within their intervals, sort them, and only then draw the monomial labels using the corresponding constant $`|v_{a,j}|/v_j`$. The midpoint grids keep rounded times strictly inside the selected interval. Ties can occur only among samples with the same label law; assigning independent labels after sorting couples the rounded and exact ordered words without an additional ordering bias.

Let
```math
\Omega\ge\sup_{t\in[0,\tau]}\|K_p(t)\|
\tag{29}
```
be a known bound for the real one-body generator. One may use $`\Omega=B_Q+4\lambda L_q`$, with the explicitly computed $`B_Q`$ from Section 6. A transformed Majorana changes by at most $`\Omega|t-s|`$ in operator norm when its time changes from $`s`$ to $`t`$. This remains true across finitely many supplied or proxy jumps by integration. Telescoping the factors in a truncated word pair shows that moving every insertion time by at most $`\Delta_t`$ changes its unscaled expectation by at most
```math
d_0M\Omega\Delta_t.
\tag{30}
```
Thus, for example,
```math
\Delta_t\le
\frac{\delta e^{-2S}}{8d_0(M+1)(\Omega+1)}
\tag{31}
```
fits a $`\delta/8`$ timing budget. The additions of one avoid zero denominators and are harmless conservative guards. Sampling and sorting these finite times is polynomial work. Their bit lengths include those of the given interval endpoints.

The remaining $`\delta/8`$ numerical budget can be split among the Gaussian propagators, contractions, Pfaffian, and the scale $`e^{2S_\tau}`$. Together with truncation, probability rounding, and time discretization, the mean bias is at most $`\delta/2`$.

### Statistical samples

After these deterministic accuracy allocations, use independent bounded trials and Hoeffding's inequality for the remaining $`\delta/2`$ statistical error. A known upper bound for the magnitude of a scaled trial can be chosen between $`e^{2S_\tau}`$ and $`2e^{2S_\tau}`$. Clipping to that range preserves the bias bound. It suffices to use
```math
N_{\rm samp}
=O\!\left(
e^{4S_\tau}\delta^{-2}\log(1/p_{\rm node})
\right)
\tag{32}
```
trials to obtain total additive error at most $`\delta`$, with failure probability at most $`p_{\rm node}`$.

Approximating an irrational target endpoint is a separate nodal-time allocation in the [reconstruction theorem](spectral-reconstruction.md). All the preceding calculations can use its finite endpoint.

## 6. A paid Gaussian matrix integrator

The preceding bounds require one-body propagators at the sampled times. Their cost is polynomial and can be made logarithmic in inverse numerical accuracy at fixed model parameters. The following direct construction gives a concrete guarantee for the supplied polynomial proxies.

On one panel of length $`h`$, the one-body generator has the form
```math
K_p(t)=K_{0,j}+\lambda p(t)K_A,
\qquad
\|K_{0,j}\|\le B_Q,\quad \|K_A\|\le2.
\tag{33}
```
The source $`b`$ and the quadratic part of the impurity decomposition have already been included in $`K_{0,j}`$. A coefficient sum bound gives a computable $`B_Q`$. In the multiple-field version, replace $`\lambda`$ by the sum of absolute coupling magnitudes.

### Complex bound for the known polynomial

Let $`q\ge1`$, and consider the Bernstein ellipse of parameter
```math
\varrho=1+\frac1q.
\tag{34}
```
On that ellipse, $`|T_\ell(z)|\le\varrho^\ell\le e<3`$ for $`0\le\ell\le q`$. Equation (8) therefore implies the conservative bound
```math
|p(z)|\le9(q+1).
\tag{35}
```
Thus
```math
\|K_p(z)\|\le
\Gamma:=B_Q+18\lambda(q+1).
\tag{36}
```

The ellipse around the normalized interval $`[-1,1]`$ has semimajor axis
```math
a=\frac{\varrho+\varrho^{-1}}2,
\qquad
a-1=\frac{1}{2q^2\varrho}\ge\frac{1}{4q^2}.
\tag{37}
```
It contains a disk of radius $`a-1`$ centered at each endpoint: substituting $`x=1+(a-1)\cos\theta`$, $`y=(a-1)\sin\theta`$ into the ellipse equation gives a value at most one, and the other endpoint follows by symmetry. Convexity then includes the disk of that radius about every intervening real point. After rescaling to the physical panel, every real point therefore has a complex disk of radius at least $`h/(8q^2)`$ contained in the ellipse.

### Taylor substeps and their error

If $`\Gamma=0`$, the one-body propagator is the identity. Otherwise use an analytic radius
```math
r_G=\min\left\{\frac{h}{16q^2},\frac{1}{2\Gamma}\right\}
\tag{38}
```
at each real substep start, and a substep length at most $`r_G/2`$. The local fundamental matrix $`Y(z)`$, with $`Y(0)=I`$, is holomorphic in that disk and obeys
```math
\|Y(z)\|\le e^{\Gamma|z|}<2.
\tag{39}
```
Its Taylor polynomial of degree $`\ell`$ has local operator-norm error at most $`4\,2^{-\ell}`$ at a real substep endpoint.

Across a whole prefix, the number of substeps is at most
```math
N_G\le P(1+32q^2)+4\Gamma T.
\tag{40}
```
Choosing
```math
\ell=O\!\left(
\log\frac{N_G+1}{\nu}
\right)
\tag{41}
```
and allocating rounding error of the same order as the Taylor truncation on each substep gives a full one-body propagator error at most $`\nu`$. Exact real-time factors are orthogonal; a telescoping product bound controls accumulation by the sum of the substep errors, up to a constant factor. No exponential factor in the quadratic evolution time is introduced.

### Arithmetic cost

Write the local generator and propagator as
```math
K(z)=\sum_{r=0}^q K_r z^r,\qquad
Y(z)=\sum_{s\ge0}Y_s z^s.
```
Their coefficients satisfy the explicit recurrence
```math
Y_0=I,\qquad
Y_{s+1}=\frac{1}{s+1}
\sum_{r=0}^{\min(q,s)}K_rY_{s-r}.
\tag{42}
```
Each Taylor coefficient uses $`O(q+1)`$ matrix multiplications of dimension $`2n`$. Changing from the stored Chebyshev polynomial to the local power basis takes polynomially many operations; scaling each substep to a unit interval controls numerical sizes.

One conservative arithmetic count for a whole prefix is
```math
C_G(\nu)=
O\!\left(
N_G\left[
n^3(q+1)(\ell+1)+n^2(q+1)^2
\right]\mathrm{poly}(B_G)
\right),
\tag{43}
```
where $`B_G`$ is polynomial in the input bit lengths, $`q,\ell`$, $`\log(n+1)`$, $`\log(N_G+1)`$, $`\log(1/\nu)`$, and the bit lengths of the panel endpoints and inverse panel lengths. Exact rational coefficient recurrences followed by controlled rounding give one implementation; small panel lengths are charged through those bit lengths.

At most $`M+1`$ distinct propagator times are required for one truncated word pair, including the target time. Computing their prefixes independently costs at most $`(M+1)C_G(\nu)`$. Sorting and sharing propagation can improve this count but is unnecessary for a polynomial bound.

For a concrete trial bound, let $`D_w=d_0M+2`$, enlarge it to an even integer if necessary, and put $`r=D_w/2`$. One sufficiently small contraction tolerance and propagator tolerance are
```math
\xi=\frac{\delta e^{-2S}}
{128e\,r(2r-1)!!},
\qquad
\nu=\frac{\xi}{64}.
```
Approximating each one-body propagator and the initial two-point matrix to operator-norm accuracy $`\nu`$, and allocating another $`\xi/2`$ to each contraction's arithmetic, meets (22) with room for the scalar scale and output rounding. An entrywise initial-matrix tolerance $`\nu/(2n)`$ suffices for its operator-norm target.

With $`R_V`$ interaction labels, a conservative fully paid count for a single truncated trial is
```math
\begin{aligned}
C_{\rm Wick}\le{}&
(M+1)C_G(\nu)\\
&+
O\!\left(
\left[
n^2D_w^2+D_w^3+
M\bigl(K+R_V+\log(M+1)\bigr)
\right]\mathrm{poly}(B_W)
\right).
\end{aligned}
\tag{44}
```
The first two terms in the square brackets cover dense contractions and Pfaffian elimination. The last covers a simple scan of the finite probability tables, label selection, and time sorting; faster table access is unnecessary. The bit length $`B_W`$ is polynomial in the supplied numerical bit lengths, $`B_G`$, $`S`$, $`D_w\log(D_w+1)`$, and $`\log(n/\delta)`$. Here the total input length $`L_{\rm in}`$, covariance construction, and probability-table construction are additionally charged as data work. Equations (27), (40), (41), and (43) show that (44) is polynomial in $`n,P,q,d_0,S,\Gamma T,L_{\rm in},B_{\rm in},\log(1/\delta)`$. It does not contain an unpriced Gaussian-propagator oracle.

## 7. Closing the actual self-consistent task

Use the [certified spectral algorithm](spectral-reconstruction.md) for
```math
\dot\rho=-i[Q_0(t)+b(t)A+V(t)+\lambda m(t)A,\rho],
\qquad
m(t)=\mathrm{Tr}(O\rho(t)).
\tag{45}
```
Its parameters are
```math
\eta=\frac{\epsilon e^{-2\kappa}}{16},\qquad
\delta=\Theta\!\left(\frac{\eta}{L_q}\right),\qquad
J=P(q+1)I,
\tag{46}
```
with
```math
q=O(\kappa+\log(1/\epsilon)),\quad
I=O(\kappa+\log(1/\epsilon)+\log L_q),\quad
P=O(K+T\Lambda+\kappa L_q).
\tag{47}
```
The norm bound $`\Lambda`$ includes the entire supplied base Hamiltonian. It is a paid parameter.

Replace each quantum nodal response procedure by the classical estimator above, and assign $`p_{\rm node}=p/J`$. Apply the word estimator with an error allowance $`\delta/2`$, reserving the other $`\delta/2`$ for approximation of the requested node endpoint and any remaining response-interface rounding. These fixed fractions change (32) only by a constant factor. The field proxy and source remain quadratic at every iteration; the same non-Gaussian action bound $`S`$ applies to every prefix and every measurement history. Hence all conditional guarantees required by the reconstruction theorem hold.

**The prefix distinction is essential.** The interacting state at a later panel start is generally not Gaussian. The classical estimator never replaces it by a Gaussian state. Instead, every word expansion includes the entire prescribed prefix from the original Gaussian $`\rho_0`$, through both Dyson branches. This is exactly the response needed by the collocation map.

Combining the nodal count with (32) gives
```math
\begin{aligned}
C_{\rm classical}
&\le
O\!\left(
J\,e^{4S}\delta^{-2}
\log(J/p)\,C_{\rm Wick}
\right)
+C_{\rm data}\\
&=
\widetilde O\!\left(
J\,e^{4(S+\kappa)}
L_q^2\epsilon^{-2}C_{\rm Wick}
\right)
+C_{\rm data}.
\end{aligned}
\tag{48}
```
The term $`C_{\rm data}`$ includes input reading, construction of the sampling tables, the $`O(Jq)`$ coefficient-processing arithmetic operations, $`O(Pqb)`$ retained coefficient bits, and final scalar rounding. All these costs are polynomial in the stated descriptions and precisions. The initial Fock-state covariance is exact; an approximate specified Gaussian initialization can instead use the initial-state error allocation in the reconstruction theorem.

For $`d`$ fixed quadratic feedback observables, estimate each component and replace $`\lambda`$ by $`\sum_a|\lambda_a|`$. The scalar node count is multiplied by $`d`$, and every covariance, coefficient, and measurement component is charged.

## 8. Consequences for advantage claims

### A rigorous classical regime

Let $`N`$ be an input-size parameter. If the explicit bath and pulse descriptions, norm/time parameters, numerical bit lengths, and $`1/\epsilon`$ are polynomially bounded in $`N`$, and
```math
S+\kappa=O(\log N),
\tag{49}
```
then (48) is a randomized polynomial-time classical algorithm. In particular, fixed $`\kappa`$ and fixed $`S`$, or fixed $`\kappa`$ and $`S=O(\log N)`$, cannot support a uniform conditional superpolynomial quantum advantage for this Gaussian-input subclass.

At fixed interaction strength, fixed elapsed time gives bounded $`S`$. Increasing the bath size alone does not defeat this comparator. This statement does not require a spatial light-cone argument or local bath geometry. Spatial locality, weak coupling, symmetries, or restricted excitation numbers can provide further shortcuts.

### What growing action does and does not show

A universal controlled-impurity family can accumulate polynomially many interaction pulses, so its $`S`$ grows with the encoded computation. Keeping $`\kappa`$ fixed can be achieved either by taking $`\lambda=\kappa/T`$, or by rescaling a supplied schedule to fixed $`T`$ and charging its larger Hamiltonian coefficients. The quantum bound retains these time and normalization costs. The classical bounded-action guarantee then does not settle that entire family.

This does not prove exponential classical cost at larger $`S`$. The factor $`e^{4S}`$ is the variance bound of the independent-word estimator. Better interaction pictures, cancellations, resummation, deterministic integration, inchworm reuse, influence-functionals, tensor networks, and other model-specific algorithms can reduce the cost. Inchworm methods provide concrete examples of much better time scaling in Anderson impurity regimes. [CGRM]

Likewise, the $`\epsilon^{-2}`$ factor in (48) comes from ordinary sampling of this estimator. It is not a lower bound on the precision cost of every classical algorithm. The quantum inverse-linear precision guarantee and a conditional input-size hardness theorem answer different questions and should be stated separately.

The meaningful comparison therefore retains both actions: feedback acquisition has a controlled quantum cost for moderate $`\kappa`$, while interacting response evaluation can be difficult as the non-Gaussian action and explicit control family grow. A useful natural-drive advantage requires a comparison against the best classical methods for that drive family, in addition to the worst-case theorem.

## References

- **[TD]** Barbara M. Terhal and David P. DiVincenzo, “Classical simulation of noninteracting-fermion quantum circuits,” *Physical Review A* **65**, 032325 (2002). Sections III–V give Gaussian transformations, Wick/Pfaffian evaluation, and differently conjugated operator groups. [Paper](https://arxiv.org/pdf/quant-ph/0108010); [DOI](https://doi.org/10.1103/PhysRevA.65.032325).
- **[WOM]** Philipp Werner, Takashi Oka, and Andrew J. Millis, “Diagrammatic Monte Carlo simulation of nonequilibrium systems,” *Physical Review B* **79**, 035320 (2009). Real-time impurity interaction and hybridization expansions use forward/backward Keldysh branches and Wick/determinant weights. [Paper](https://arxiv.org/pdf/0810.2345); [DOI](https://doi.org/10.1103/PhysRevB.79.035320). The independent bounded Poisson estimator and conservative cost proof above are derived explicitly here.
- **[CGRM]** Guy Cohen, Emanuel Gull, David R. Reichman, and Andrew J. Millis, “Taming the dynamical sign problem in real-time evolution of quantum many-body problems,” *Physical Review Letters* **115**, 266802 (2015). [Paper](https://arxiv.org/abs/1510.03534); [DOI](https://doi.org/10.1103/PhysRevLett.115.266802).
