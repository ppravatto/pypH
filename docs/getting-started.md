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

(getting-started)=
# Getting started

The latest unreleased version can instead be downloaded directly from our [GitHub](https://github.com/ppravatto/pypH) page and then installed using `pip`. 

```
git clone https://github.com/ppravatto/pypH.git
cd pypH
pip install .
```

:::{admonition} Note
:class: warning
We always recommend installing new Python packages in a clean Conda environment and avoid installing in the system Python distribution or in the base Conda environment! If you are unfamiliar with Conda, please refer to their [documentation](https://docs.anaconda.com/free/anaconda/install/index.html) for a guide on how to set up environments.
:::

The library can be imported in a Python script via the following syntax:

```python
import pypH
```

Alternatively, individual submodules, classes, and functions can be imported separately:

```python
from pypH.acid import Acid
```

For a more detailed explanation of the available features in each submodule, please refer to their specific page in this [User Guide](user-guide).