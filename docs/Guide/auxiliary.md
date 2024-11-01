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

(Guide-Auxiliary)=
# Auxiliary function

The `Plotter` class also supports the definition of auxiliary curves. These are for example useful when visualizing the protonic balance of a solution.

Let us consider as an example the problem of computing the $pH$ of a $0.01M$ diammonium phosphate $(NH_4)_2HPO_4$ solution. To do so, let us start by defining the system of acids according to:

```{code-cell} python
from pypH.base import *

phosphoric_acid = Acid([2.14, 7.20, 12.37], 0.01, names=["$H_3PO_4$", "$H_2PO_4^-$", "$HPO_4^{2-}$", "$PO_4^{3-}$"])
ammonium = Acid([9.24], 0.02, names=["$NH_4^+$", "$NH_3$"])
```

That, represented on the logarithmic diagram, appears as follows:

```{code-cell} python
plotter = Plotter()

plotter.add("ammonium", ammonium)
plotter.add("phosphoric acid", phosphoric_acid)

plotter.plot(show_legend=True)
```

To solve the problem and compute the $pH$ of the solution, one should consider the protonic balance that, for the system in question is represented by:

$$
    [H_3O^+] + [H_2PO_4^-] + 2[H_3PO_4] = [PO_4^{3-}] + [NH_3] + [OH^-]
$$

To compose the two sides of the protonic balance and represent them on the logarithmic diagram we should use a list of instances of the `Term` class. A `Term` object is a simple container holding the name of the acid system of the species, its deprotonation index and the relative coefficient. As such the right and left sides of the protonic balance can be constructed according to:

```{code-cell} python
right_side = [
    Hydronium(1.),
    Term("phosphoric acid", 1, 1.),
    Term("phosphoric acid", 0, 2.)
    ]

left_side = [
    Term("phosphoric acid", 3, 1.),
    Term("ammonium", 1, 1.),
    Hydroxide(1.)
    ]
```

Where the `Hydronium` and `Hydroxide` object are pre-defined intances of the `Term` class to represent the solvent derived ions.

The auxiliary curves can be added to the plot using the `add_auxiliary` function according to:

```{code-cell} python
plotter.add_auxiliary(right_side)
plotter.add_auxiliary(left_side)

plotter.plot(show_legend=True)
```