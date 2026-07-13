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
[H_{n-m}A^{m-}]=\frac{[H_3O^+]^{i-m}}{\prod_{j=m+1}^{i} k_a^{(j)}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m < i
$$

while all the intermediates having lower protonation states $n-m < n-1$ can be rewritten according to:

$$
[H_{n-m}A^{m-}]=\frac{\prod_{j=i+1}^{m} k_a^{(j)}}{[H_3O^+]^{m-i}}[H_{n-i}A^{i-}] \qquad \text{for} \qquad m > i
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

(buffer-capacity)=
## Buffer capacity
The buffer capacity $\beta$ indicates the capacity of a given acid-base system to resist changes in $\mathrm{pH}$ induced by the addition of a strong base or acid. The buffer capacity is defined as:

$$ \beta := \frac{d C_b}{d \mathrm{pH}} $$

where the quantity $C_b$ represents the quantity of strong base required to increase the $\mathrm{pH}$ of the solution. The buffer capacity definition can also be rewritten as a function of the $[H_3O^+]$ concentration. To do so, one can consider the following series of equalities:

$$ \beta = \frac{d C_b}{d \mathrm{pH}} = \frac{d C_b}{d [H_3O^+]}\frac{[H_3O^+]}{d \mathrm{pH}} = \frac{d C_b}{d [H_3O^+]}\left(\frac{d \mathrm{pH}}{d[H_3O^+]}\right)^{-1}$$

By recalling the definition $\mathrm{pH}:= -\log{[H_3O^+]}$, the last term can be computed according to:

$$ \frac{d \mathrm{pH}}{d[H_3O^+]} = - \frac{d}{d[H_3O^+]} \log{[H_3O^+]} = - \frac{1}{[H_3O^+] \log{10}} $$

That, by simple substitution, returns the following relation:

$$ \beta = -\log{10}[H_3O^+] \frac{d C_b}{d [H_3O^+]} $$

Adopting this form of the buffer capacity, an explicit equation for a generic acid/base sistem can be obtained considering the following charge balance equation:

$$ [OH^-] + \sum_A \sum_{i=1}^{n_A} i [H_{n_A - i}A^{i-}] = [H_3O^+] + C_b $$

Where the index $A$ runs across all the weak acid/base species in the system and the index $i$ along all the possible deprotonation states going from $1$ to $n_A$. Please notice how an increase in the deprotonation state directly corresponds to an higher charge state that, in turn, is taken into account by multiplying their concentration by the index $i$. Please notice how strong acid or bases in the system are not taken into accout since their neutralization produces water the contribution of which is already described by the $[H_3O^+]$ and $[OH^-]$ terms. Please notice how the $C_b$ term represent the amount of strong base hypotetically added to the acid/base system to probe its buffer capacity and can thinked as the concentration of an hypotetical counter-ion (e.g. $Na^+$ in during the addition of the strong base $NaOH$).

From the above equation one can easily obtain the expression:

$$ C_b = \frac{k_w}{[H_3O^+]} + \sum_A \sum_{i=1}^{n_A} i [H_{n_A - i}A^{i-}] - [H_3O^+]$$

the derivative of which, in respect to the $[H_3O^+]$ concentration can be computed according to:

$$ \frac{d C_b}{d [H_3O^+]} = -\frac{k_w}{[H_3O^+]^2} + \sum_A \sum_{i=1}^{n_A} i \frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]}  - 1 $$

Considering the previously derived definition of $\beta$ it is simple to observe how:

$$ \beta = \log{10}\left[\frac{k_w}{[H_3O^+]} - \sum_A \sum_{i=1}^{n_A} i [H_3O^+]\frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]} + [H_3O^+]\right] $$

Where the only missing term to compute is represented by the derivative $[H_{n-i}A^{i-}]$ in respect to $[H_3O^+]$. This can be easily computed recalling that, according to what derived in the previous section, the following equation can be written:

$$
[H_{n-i}A^{i-}] = C_A \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-1}
$$

Following this definition the missing term can easily be computed according to:

$$
\frac{d[H_{n_A - i}A^{i-}]}{d[H_3O^+]} = -C_A \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-2} \sum_{m=0}^{n_A}\frac{(i-m)\beta_{m}[H_3O^+]^{i-m-1}}{\beta_{i}}
$$

By simple substitution one can finally obtain the expression:

$$\beta = \log{10}\left[ \frac{k_w}{[H_3O^+]} + \sum_A C_A \sum_{i=1}^{n_A} i \bigg( \sum_{m=0}^{n_A}\frac{\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} \bigg)^{-2} \sum_{m=0}^{n_A}\frac{(i-m)\beta_{m}[H_3O^+]^{i-m}}{\beta_{i}} + [H_3O^+] \right] $$