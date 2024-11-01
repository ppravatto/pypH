---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(Guide-Basic)=
# Basic plotting

The starting point in plotting a logarithmic diagram is to define the acid-base system. This can be done through the `Acid` class that is capable of encoding a generic polyprotic acid. An instance of the class can be created providing the $pKa$ of the acid and its total concentration. 

```{code-cell} python
from pypH.base import *

oxalic_acid = Acid([1.25, 4.14], 0.05)
```

Additionally, labels can be added directly in the class constructor to help in identifying each deprotonation product. To do so, a list of strings, given in order from the completely protonated form to the completely deprotonated one, can be given as the `names` variable. Latex syntax is accepted.

```{code-cell} python
oxalic_acid = Acid([1.25, 4.14], 0.05, names=["$H_2Ox$", "$HOx^-$", "$Ox^{2-}$" ])
```

Once an instance of the `Acid` class has been defined the concentration of each deprotonation product can be computed at a given $pH$ using the `concentration` function. The user can select the desired deprotonation product using as `index` the number of protons removed from the base acid. As an example the concentration of the $Ox^{2-}$ (`index = 2`) at $pH=5.2$ can be computed according to:

```{code-cell} python
print(oxalic_acid.concentration(2, 5.2))
```

Once the acid system has been defined it can be passed to the `Plotter` class to generate the corresponding logarithmic diagram:

```{code-cell} python
plotter = Plotter()
plotter.add("oxalic acid", oxalic_acid)

plotter.plot(show_legend=True)
```