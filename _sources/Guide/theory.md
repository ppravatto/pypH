(Guide-Theory)=

# Theory
When an acid of generic formula $H_nA$, with $n\geq1$, is dissolved in an aquous solution, a series of dissociations equilibrium are immediately estabished according to the sequence of reactions:

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

Each of the written reactions is an equilibrium characterized by a acidic dissociation constant $k_a^{(i)}$ defined according to:

$$
k_a^{(i)}=\frac{[H_{n-i}A^{i-}][H_3O^+]}{[H_{n-i+1}A^{(i-1)-}]}
$$

where $1\leq i\leq n$ represents the index of the dissociation reaction numbered in order and starting from $1$.

Given an initial concentration $C_a$ of the acid substance, the following mass balance can be written:

$$
C_a = [H_nA]+[H_{n-1}A^-]+[H_{n-2}A^{2-}] + ... + [HA^{(n-1)-}] + [A^{n-}]
$$

or, in more compact form, according to the summation:

$$
C_a = \sum_{j=0}^{n} [H_{n-j}A^{j-}]
$$

Using this relation one can easily express the concentration $[H_{n-j}A^{j-}]$ of each dissociation product as a function of the total acid concentration $C_a$ and the solution $pH$.

To show how this can be done we can start by adopting a simple observation: each dissociation constant $k_a^{(i)}$ can be used to write the concentration of two subsequent dissociation product one as a function of the other. 

As an example the concentraion of the deprotonation product $H_{n-i}A^{i-}$ can be use to express the concentration of its precursor $H_{n-i+1}A^{(i-1)-}$ according to:

$$
[H_{n-i+1}A^{(i-1)-}]=\frac{[H_3O^+]}{k_a^{(i)}}[H_{n-i}A^{i-}]
$$

while, at the same time, it can also be used to express the concentration of its deprotonation product $H_{k-1}A^{(n-k+1)-}$ of the following one according to:

$$
[H_{n-i-1}A^{(i+1)-}]=\frac{k_a^{(i+1)}}{[H_3O^+]}[H_{n-i}A^{i-}]
$$

These relations can be chained allowing to express the concentration of each species in the dissociation sequence as a function of any other.

Using this observation one can rewrite the acid mass balance as a function of the concentration of a generic intermediate $[H_{n-i}A^{i-}]$. To do so, a two step process can be employed. All the intermediates having higher protonation states $n-m>n-i$ can be rewritten according to:

$$
[H_{n-m}A^{m-}]=\frac{[H_3O^+]^{i-m}}{\prod_{j=m+1}^{i} k_a^{(i)}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m < i
$$

while all the intermediates having lower protonation states $n-m < n-1$ can be rewritten according to:

$$
[H_{n-m}A^{m-}]=\frac{\prod_{j=i+1}^{m} k_a^{(i)}}{[H_3O^+]^{m-i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m > i
$$

By introducting the cumulative dissociation contants:

$$
\beta_j := \prod_{i=1}^{j} k_a^{(i)}
$$

The previous relations can be rewritten as:

$$
[H_{n-m}A^{m-}]=\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m < i
$$

$$
[H_{n-m}A^{m-}]=\frac{\beta_m}{\beta_{i}[H_3O^+]^{m-i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m > i
$$

where, for the special case of $m=0$, $\beta_0 := 1$. By observing that, when moving from $m<i$ to the case of $i>m$, the change in sign of the exponent $i-m$ automatically takes care of bringing the $[H_3O^+]$ term to the denominator one can easily see how the two relations can be rewritten in a single expression that takes care of all the possible scenarios:

$$
[H_{n-m}A^{m-}]=\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}[H_{n-i}A^{i-}] 
$$


By substituting this relation in the acid mass balance the following result can be obtained:

$$
C_a = [H_{n-i}A^{i-}]\sum_{m=0}^{n}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}}
$$

From which:

$$
[H_{n-i}A^{i-}] = C_a \bigg( \sum_{m=0}^{n}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-1}
$$
