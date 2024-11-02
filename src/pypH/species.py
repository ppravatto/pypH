from __future__ import annotations
from copy import deepcopy
from typing import List, Dict, Optional, Union, Generator

class Species:
    """
    Simple class used in the definition of an auxiliary curve to indentify a generic deprotonated species.
    The class can be directly used to construct `Auxiliary` class object by summation and subtraction with
    other `Species` or `Auxiliary` objects and multiplication by a `float` numerical coefficient.

    Attribues
    ---------
    acid_id: int
        The ID of the acid from which the speces is derived
    name: str
        The name of the acid from which the term should be selected
    index: int
        The deprotonation index of the desired form.
    """

    def __init__(self, acid_id: int, name: str, index: int):
        self.acid_id = acid_id
        self.name: str = name
        self.index: int = index
    
    def to_auxiliary(self) -> Auxiliary:
        """
        Function dedicated to the direct conversion of a `Species` object into a `Auxiliary` one.

        Returns
        -------
        Auxiliary
            The auxiliary object encoding the species with coefficient 1.
        """
        obj = Auxiliary()
        obj.species.append(self)
        obj.coefficients.append(1.)
        return obj
    
    def __add__(self, other: Union[Species, Auxiliary]) -> Auxiliary:
        obj = self.to_auxiliary()
        return obj+other
    
    def __sub__(self, other: Union[Species, Auxiliary]) -> Auxiliary:
        obj = self.to_auxiliary()
        return obj-other

    def __mul__(self, coefficient: float) -> Auxiliary:
        obj = self.to_auxiliary()
        return coefficient*obj
    
    def __rmul__(self, coefficient: float) -> Auxiliary:
        return self.__mul__(coefficient)


global Hydronium
Hydronium = Species(None, "H_3O^+", None)

global Hydroxide
Hydroxide = Species(None, "OH^-", None)


class Auxiliary:
    """
    The Auxiliary class provides a simple object capable of handling the definition of auxiliary
    curves to be represented on the logarithmic diagram. The class provides an `__iter__` method
    yielding ordered couples of species and coefficients. The class supports summations and subtraction
    with other `Auxiliary` and `Species` class objects and multiplication by a float numerical value.

    Attributes
    ----------
    species: List[Species]
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
