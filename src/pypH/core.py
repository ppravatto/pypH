from __future__ import annotations

from typing import List, Optional
from copy import deepcopy

from pypH.species import Species


class Acid:
    """
    The Acid class encodes the behavior of a generic mono or polyprotic acid. The number of acidic protons
    is defined automatically by setting the `pKa` values. The class can be used to compute the concentration
    of each deprotonated species at a given pH by directly calling its `concentration` method. Furthermore
    the class provides a simple interface to the construction of auxiliary curves by providing direct access
    to the deprotonated `Species` generated by the acid. These can be easily obtained using the `[]` square 
    bracket operator and specifying the deprotonation `index`

    Parameters
    ----------
    pka: List[float]
        The list of pka values associated to the various acid dissociations.
    concentration: float
        The molar concentration of the acid.
    names: Optional[List[str]]
        An optional field in which the user can specify names to be assigned to each deprotonation product.
        If no name is given the system will automatically call the species with the scheme `H_iX^{{n-i}-}" where
        `X` is a progressive letter assigned starting form `A`.
    """

    __acid_class_id = 0

    def __init__(
        self, pka: List[float], concentration: float, names: Optional[List[str]] = None
    ) -> None:

        self.__Ca: float = concentration
        self.__pka: List[float] = sorted(pka)
        self.__ka = [10 ** (-pka) for pka in self.__pka]
        self.__id = deepcopy(Acid.__acid_class_id)

        self.__betas = [1]
        for ka in self.__ka:
            self.__betas.append(self.__betas[-1] * ka)

        if names is None:

            letter = chr(ord("A") + self.__id)

            self.__names = []

            for i in range(self.nprotons + 1):

                name = "$"
                name += "H" if self.nprotons - i > 0 else ""
                name += (
                    ("_{" + f"{self.nprotons-i}" + "}") if self.nprotons - i > 1 else ""
                )
                name += f"{letter}"

                if i != 0:
                    name += "^-" if i == 1 else "^{" + f"{i}" + "-}"

                name += "$"
                self.__names.append(name)

        else:

            if len(names) != self.nprotons + 1:
                raise ValueError(
                    "The number of provided names does not match the number of deprotonation products"
                )

            self.__names = names
        
        Acid.__acid_class_id += 1

    def __getitem__(self, index: int) -> Species:
        """
        Returns the species obtained from the acid by `index` subsequent deprotonations.

        Retruns
        -------
        Species
            The `Species` object identifying the deprotonated species

        Raises
        ------
        ValueError
            Exceprion raised when the user specified index is smaller than zero or greate than the number of protons
        """

        if index < 0 or index > self.nprotons:
            raise ValueError("Invalid index")

        return Species(self.__id, self.__names[index], index)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nprotons(self) -> int:
        """
        The number of acidic protons in the molecule

        Returns
        -------
        int
            The number of acidic protons
        """
        return len(self.__pka)

    @property
    def names(self) -> List[str]:
        """
        The names associated to each deprotonation product.

        Returns
        -------
        str
            The list of names.
        """
        return self.__names

    def concentration(self, index: int, pH: float) -> float:
        """
        Compute the concentration of the user defined deprotonation state of the acid at the specified pH.

        Parameters
        ----------
        index: int
            The index of the deprotonation state as the number of lost protons
        pH: float
            The pH value at which the concentration must be computed

        Raises
        ------
        ValueError
            Exceprion raised when the user specified index is smaller than zero or greate than the number of protons

        Returns
        -------
        float
            The concentration of the selected deprotonation state at the given pH.
        """
        hydronium = 10 ** (-pH)

        if index < 0 or index > self.nprotons:
            raise ValueError("Invalid index")

        factor = 0
        for m in range(0, self.nprotons + 1):
            factor += hydronium ** (index - m) * self.__betas[m] / self.__betas[index]

        return self.__Ca / factor

