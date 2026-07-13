(Guide-Theory)=

# Theory
When an acid of generic formula $H_nA$, with $n\geq1$, is dissolved in an aqueous solution, a series of dissociation equilibria is immediately established according to the following sequence of reactions:

$$
\ce{H_nA + H_2O <=> H_{n-1}A^- + H_3O^+}
$$

$$
\ce{H_{n-1}A^- + H_2O <=> H_{n-2}A^{2-} + H_3O^+}
$$

$$ ... $$

$$
\ce{HA^{(n-1)-} + H_2O <=> A^{n-} + H_3O^+}
$$

Each of the above reactions is an equilibrium characterized by an acid dissociation constant $k_a^{(i)}$, defined as:

$$
k_a^{(i)}=\frac{[H_{n-i}A^{i-}][H_3O^+]}{[H_{n-i+1}A^{(i-1)-}]}
$$

where $1\leq i\leq n$ denotes the index of the dissociation reaction, numbered sequentially starting from $1$.

Given an initial acid concentration $C_a$, the following mass balance can be written:

$$
C_a = [H_nA]+[H_{n-1}A^-]+[H_{n-2}A^{2-}] + ... + [HA^{(n-1)-}] + [A^{n-}]
$$

or, in a more compact form,

$$
C_a = \sum_{j=0}^{n} [H_{n-j}A^{j-}]
$$

Using this relation, the concentration $[H_{n-j}A^{j-}]$ of each dissociation product can be expressed as a function of the total acid concentration $C_a$ and the solution pH.

To show how this can be done, let us start with a simple observation: each dissociation constant $k_a^{(i)}$ can be used to express the concentration of either of two consecutive dissociation products as a function of the other.

For example, the concentration of the deprotonated species $H_{n-i}A^{i-}$ can be used to express the concentration of its precursor $H_{n-i+1}A^{(i-1)-}$ according to:

$$
[H_{n-i+1}A^{(i-1)-}]=\frac{[H_3O^+]}{k_a^{(i)}}[H_{n-i}A^{i-}]
$$

Likewise, it can also be used to express the concentration of the following deprotonation product according to:

$$
[H_{n-i-1}A^{(i+1)-}]=\frac{k_a^{(i+1)}}{[H_3O^+]}[H_{n-i}A^{i-}]
$$

These relations can be chained together, allowing the concentration of each species in the dissociation sequence to be expressed as a function of any other species.

Using this observation, the acid mass balance can be rewritten as a function of the concentration of a generic intermediate species $[H_{n-i}A^{i-}]$. To do so, a two-step process can be employed. All species with higher protonation states ($n-m>n-i$) can be rewritten according to:

$$
[H_{n-m}A^{m-}]=\frac{[H_3O^+]^{i-m}}{\prod_{j=m+1}^{i} k_a^{(j)}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m < i
$$

while all species with lower protonation states ($n-m < n-1$) can be rewritten according to:

$$
[H_{n-m}A^{m-}]=\frac{\prod_{j=i+1}^{m} k_a^{(j)}}{[H_3O^+]^{m-i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m > i
$$

By introducing the cumulative dissociation constants:

$$
\beta_j := \prod_{i=1}^{j} k_a^{(i)}
$$

the previous relations can be rewritten as:

$$
[H_{n-m}A^{m-}]=\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m < i
$$

$$
[H_{n-m}A^{m-}]=\frac{\beta_m}{\beta_{i}[H_3O^+]^{m-i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m > i
$$

where, for the special case $m=0$, $\beta_0 := 1$. By observing that, when moving from the case $m<i$ to the case $m>i$, the change in the sign of the exponent $i-m$ automatically moves the $[H_3O^+]$ term to the denominator, it is easy to see that the two expressions can be combined into a single equation valid for all possible cases:

$$
[H_{n-m}A^{m-}]=\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}[H_{n-i}A^{i-}]
$$

Substituting this relation into the acid mass balance yields:

$$
C_a = [H_{n-i}A^{i-}]\sum_{m=0}^{n}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}
$$

from which:

$$
[H_{n-i}A^{i-}] = C_a \bigg( \sum_{m=0}^{n}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-1}
$$

(buffer-capacity)=
## Buffer capacity

The buffer capacity $\beta$ indicates the ability of an acid-base system to resist changes in $\mathrm{pH}$ induced by the addition of a strong acid or base. The buffer capacity is defined as:

$$ \beta := \frac{d C_b}{d \mathrm{pH}} $$

where the quantity $C_b$ represents the amount of strong base required to increase the $\mathrm{pH}$ of the solution. The definition of the buffer capacity can also be rewritten as a function of the $[H_3O^+]$ concentration. To do so, one can consider the following sequence of equalities:

$$ \beta = \frac{d C_b}{d \mathrm{pH}} = \frac{d C_b}{d [H_3O^+]}\frac{[H_3O^+]}{d \mathrm{pH}} = \frac{d C_b}{d [H_3O^+]}\left(\frac{d \mathrm{pH}}{d[H_3O^+]}\right)^{-1}$$

Recalling the definition $\mathrm{pH}:= -\log{[H_3O^+]}$, the last term can be computed as:

$$ \frac{d \mathrm{pH}}{d[H_3O^+]} = - \frac{d}{d[H_3O^+]} \log{[H_3O^+]} = - \frac{1}{[H_3O^+] \log{10}} $$

Substituting this expression into the previous equation yields:

$$ \beta = -\log{10}[H_3O^+] \frac{d C_b}{d [H_3O^+]} $$

Using this form of the buffer capacity, an explicit expression for a generic acid-base system can be obtained by considering the following charge balance equation:

$$ [OH^-] + \sum_A \sum_{i=1}^{n_A} i [H_{n_A - i}A^{i-}] = [H_3O^+] + C_b $$

where the index $A$ runs over all weak acid-base species in the system, while the index $i$ runs over all possible deprotonation states, from $1$ to $n_A$. Note that an increase in the deprotonation state directly corresponds to a higher charge state, which is taken into account by multiplying the concentration of each species by the index $i$. Strong acids and bases are not explicitly included in the balance because their neutralization produces water, whose contribution is already represented by the $[H_3O^+]$ and $[OH^-]$ terms. Finally, the term $C_b$ represents the amount of strong base hypothetically added to the acid-base system to evaluate its buffer capacity and can be interpreted as the concentration of a hypothetical counter-ion (e.g. $Na^+$ during the addition of the strong base $NaOH$).

From the above equation one can easily obtain:

$$ C_b = \frac{k_w}{[H_3O^+]} + \sum_A \sum_{i=1}^{n_A} i [H_{n_A - i}A^{i-}] - [H_3O^+]$$

whose derivative with respect to the $[H_3O^+]$ concentration can be computed as:

$$ \frac{d C_b}{d [H_3O^+]} = -\frac{k_w}{[H_3O^+]^2} + \sum_A \sum_{i=1}^{n_A} i \frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]}  - 1 $$

Considering the previously derived definition of $\beta$, it follows that:

$$ \beta = \log{10}\left[\frac{k_w}{[H_3O^+]} - \sum_A \sum_{i=1}^{n_A} i [H_3O^+]\frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]} + [H_3O^+]\right] $$

The only remaining term to evaluate is the derivative of $[H_{n-i}A^{i-}]$ with respect to $[H_3O^+]$. Recalling the expression derived in the previous section,

$$
[H_{n-i}A^{i-}] = C_A \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-1}
$$

its derivative can be computed as:

$$
\frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]} = -C_A \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-2} \sum_{m=0}^{n_A}\frac{(i-m)\beta_{m}[H_3O^+]^{i-m-1}}{\beta_{i}}
$$

Substituting this result into the previous equation finally yields:

$$\beta = \log{10}\left[ \frac{k_w}{[H_3O^+]} + \sum_A C_A \sum_{i=1}^{n_A} i \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-2} \sum_{m=0}^{n_A}\frac{(i-m)\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} + [H_3O^+] \right] $$