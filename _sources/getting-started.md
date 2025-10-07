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

The last stable release of the `pypH` library can be installed directly from `pip` using the command:

```
pip install pyph-toolkit
```

If the last unreleased version is required, it can instead be downloaded directly from our [GitHub](https://github.com/ppravatto/pypH) page and then installed using `pip`. 

```
git clone https://github.com/ppravatto/pypH.git
cd pypH
pip install .
```

the library can also be installed in editable mode for local development purposes using the `pip install -e .` command.

:::{admonition} Note
:class: warning
We always recommend installing new Python packages in a clean Conda environment and avoid installing in the system Python distribution or in the base Conda environment! If you are unfamiliar with Conda, please refer to their [documentation](https://docs.anaconda.com/free/anaconda/install/index.html) for a guide on how to set up environments.
:::

Once installed, the library can be imported in a Python script via the following syntax:

```python
import pypH
```

Alternatively, individual submodules, classes, and functions can be imported separately:

```python
from pypH.acid import Acid
```

For a more detailed explanation of the available features in each submodule, please refer to their specific page in this [User Guide](user-guide).