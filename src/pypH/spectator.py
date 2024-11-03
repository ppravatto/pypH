from __future__ import annotations
from copy import deepcopy

from pypH.species import Species


class Spectator:
    """
    The `Spectator` class encodes a generic spectator species with no acid-base properties.

    Parameters
    ----------
    name: str
        The name of the spectator species. (Accepts LaTeX)
    concentration: float
        The molar concentration of the species.
    """

    __spectator_class_id = 0

    def __init__(self, name: str, concentration: float):
        self.__id = deepcopy(Spectator.__spectator_class_id)
        self.__name = name
        self.__concentration = float(concentration)
        Spectator.__spectator_class_id += 1
    
    def __call__(self) -> SpectatorSpecies:
        return SpectatorSpecies(self.__id, self.__name)

    @property
    def id(self) -> int:
        """
        The univocal ID that can be used to identiy the `Spectator` species.

        Reutrns
        -------
        int
            The ID of the spectator species
        """
        return self.__id

    @property
    def name(self) -> str:
        """
        The name of the spectator species.

        Returns
        -------
        str
            The string containing the name of the spectator species.
        """
        return self.__name

    @property
    def concentration(self) -> float:
        """
        The concentration of the spectator species.

        Returns
        -------
        str
            The float indicating the concentration of the spectator species in mol/L.
        """
        return self.__concentration


class SpectatorSpecies(Species):
    """
    Simple class used in the definition of an auxiliary curve to indentify a generic spectator species.
    The class can be directly used to construct `Auxiliary` class object by summation and subtraction with
    other `Species` or `Auxiliary` objects and multiplication by a `float` numerical coefficient.

    Attribues
    ---------
    spectator_id: int
        The ID of the acid from which the speces is derived
    name: str
        The name of the selected species
    index: int
        The deprotonation index of the desired form.
    """

    def __init__(self, spectator_id: int, name: str):
        super().__init__(name)
        self.__spectator_id = spectator_id

    @property
    def spectator_id(self) -> int:
        return self.__spectator_id

    def __repr__(self):
        return f"SpectatorSpecies[id: {self.__spectator_id}, name: {self.name}]"
