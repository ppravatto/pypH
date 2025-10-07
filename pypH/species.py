from __future__ import annotations

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import List, Union, Generator


class Species(ABC):
    """
    Abstract base class from which all the core-specific speces will be derived by inheritance.

    Attribues
    ---------
    name: str
        The name of the species.
    """

    def __init__(self, name: str):
        super().__init__()
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def to_auxiliary(self) -> Auxiliary:
        """
        Function dedicated to the direct conversion of a `Species` object into an `Auxiliary` one.

        Returns
        -------
        Auxiliary
            The auxiliary object encoding the species with coefficient 1.
        """
        obj = Auxiliary()
        obj.species.append(self)
        obj.coefficients.append(1.0)
        return obj

    def __add__(self, other: Union[Species, Auxiliary]) -> Auxiliary:
        obj = self.to_auxiliary()
        return obj + other

    def __sub__(self, other: Union[Species, Auxiliary]) -> Auxiliary:
        obj = self.to_auxiliary()
        return obj - other

    def __mul__(self, coefficient: float) -> Auxiliary:
        obj = self.to_auxiliary()
        return coefficient * obj

    def __rmul__(self, coefficient: float) -> Auxiliary:
        return self.__mul__(coefficient)

    def __str__(self) -> str:
        return f"$[{self.__name.strip('$')}]$"

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Auxiliary:
    """
    The Auxiliary class provides a simple object capable of handling the definition of auxiliary
    curves to be represented on the logarithmic diagram. The class provides an `__iter__` method
    yielding ordered couples of species and coefficients. The class supports summations and subtraction
    with other `Auxiliary` and `AcidSpecies` class objects and multiplication by a float numerical value.

    Attributes
    ----------
    species: List[AcidSpecies]
        A list of the species involved in the curve definition
    coefficients: List[float]
        A list of the coefficients associated to the species list.
    """

    def __init__(self):
        self.species: List[Species] = []
        self.coefficients: List[float] = []

    def __iter__(self) -> Generator[Species, float]:
        for species, coefficient in zip(self.species, self.coefficients):
            yield species, coefficient
        
    def __str__(self) -> str:
        string = "$"
        for i, (species, coefficient) in enumerate(self):
            
            if i==0:
                string += f"{coefficient}"
            else:
                string += f"{coefficient}" if coefficient<0 else f"+{coefficient}"
            
            string += f"*{str(species).strip('$')}"
        
        return string + "$"

    def __add__(self, other: Union[Species, Auxiliary]) -> Auxiliary:

        obj: Auxiliary = deepcopy(self)

        if isinstance(other, Species):
            obj.species.append(other)
            obj.coefficients.append(1.0)
            return obj

        elif isinstance(other, Auxiliary):
            for species, coefficient in other:
                obj.species.append(species)
                obj.coefficients.append(coefficient)
            return obj

        else:
            raise TypeError(
                f"Cannot perform summation between Auxiliary object and {type(other)} object"
            )

    def __sub__(self, other: Union[Species, Auxiliary]) -> Auxiliary:

        obj: Auxiliary = deepcopy(self)

        if isinstance(other, Species):
            obj.species.append(other)
            obj.coefficients.append(-1.0)
            return obj

        elif isinstance(other, Auxiliary):
            for species, coefficient in other:
                obj.species.append(species)
                obj.coefficients.append(-coefficient)
            return obj

        else:
            raise TypeError(
                f"Cannot perform summation between Auxiliary object and {type(other)} object"
            )

    def __mul__(self, number: float) -> Auxiliary:

        obj: Auxiliary = deepcopy(self)

        obj.coefficients = []
        for coefficient in self.coefficients:
            obj.coefficients.append(coefficient * float(number))

        return obj

    def __rmul__(self, number: float) -> Auxiliary:
        return self.__mul__(number)
