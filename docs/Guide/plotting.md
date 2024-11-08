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
# Basic usage
The core of the `pypH` library is represented the `System`class. This class represents a generic system of acid-base equilibrium reactions happening simultaneously within a solution. To define a `System` class object one should provide all the acid-base species and the eventually relevant spectator species. These are in turn represented in software by the `Acid` and `Spectator` classes.

## The simple case of a single acid
Let us start discussing the working of the library by showing how the logarithmic diagram of a single acid species can be plotted. For this example let us consider a $0.05M$ solution of oxalic acid.

The starting point of the operation is to define an `Acid` object that will represent our oxalic acid species in solution. The `Acid` class is a simple object capable of encoding a generic mono or polyprotic acid. An instance of the class can be created providing the $pKa$ of the acid and its total concentration. 

```{code-cell} python
from pypH.acid import Acid

oxalic_acid = Acid([1.25, 4.14], 0.05)

```

Once an instance of the `Acid` class has been defined the concentration of each deprotonation product can be computed at a given $pH$ using the `concentration` function. The user can select the desired deprotonation product using as `index` the number of protons removed from the base acid. As an example the concentration of the $A^{2-}$ species (`index = 2`) at $pH=5.2$ can be computed according to:

```{code-cell} python
print(oxalic_acid.concentration(2, 5.2))
```

Once the acid system has been defined it can be passed to the `System` class to generate the acid-base system representing the desired solution. Please notice how in this case the operation is trivial since the oxalic acid is the only species present in the solution. A `System` object however a more generic object that, as it will be shown further on in this guide, can support multiple `Acid` and `Spectator` objects and represents complex acid-base systems. Once the desired `System` object has been defined the corresponding logarithmic diagram can be easily plotted according to:

```{code-cell} python
from pypH.system import System

plotter = System()
plotter.add(oxalic_acid)

plotter.plot_logarithmic_diagram(show_legend=True)
```

Please notice how the names of the deprotonation speces have automatically been set to $H_2A$, $HA^{-}$ and $A^{2-}$ by the `Acid` class constructor. If desired, these labels can be customized by the user by directly listing the desired name in the class constructor. To do so, a list of strings, given in order from the completely protonated form to the completely deprotonated one, can be given as the `names` variable. LaTeX syntax is accepted. As an example, the previous plot can be customized as follows:

```{code-cell} python
oxalic_acid = Acid([1.25, 4.14], 0.05, names=["$H_2Ox$", "$HOx^-$", "$Ox^{2-}$" ])

plotter = System()
plotter.add(oxalic_acid)

plotter.plot_logarithmic_diagram(show_legend=True)
```

## Using `Spectator` species

Besides acid-base active species the `pypH` library also allows the representation of spectator species and ions. This can be useful for example in the resolution of protonic balances of various systems (e.g. salts or strong acid or bases). This can be done using the the `Spectator` class. An object of the `Spectator` class can be initialized by specifying a name for the species and a concentration value. As an example the case of the dissociation of a $0.01M$ hydrochloric acid solution can be represented on the logarithmic diagram as:


```{code-cell} python
from pypH.spectator import Spectator
from pypH.system import System

chloride = Spectator("$Cl^-$", 0.01)

plotter = System()
plotter.add(chloride)

plotter.plot_logarithmic_diagram(show_legend=True)

```

that, according to the protonic balance $[H_3O^+] = [OH^-] + [Cl^-]$, confirm the expected solution of $pH=2$. Please notice how the `add` method of the `System` class automatically detects the type of term given to it (either `Acid` or `Spectator` object).