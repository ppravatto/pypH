from __future__ import annotations

from typing import List, Optional, Dict, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np

from pypH.acid import Acid, AcidSpecies
from pypH.spectator import Spectator, SpectatorSpecies
from pypH.species import Auxiliary

class Plotter:
    """
    A simple class dedicated to the plot and manipulation of logarithmic diagrams. The class
    allows the user to define a system of acid and plot the concentration of the various deprotonation
    products as a function of the pH. The class also allows the user to define auxiliary curves to
    solve specific problems (e.g. solution based on protonic balance)
    """

    def __init__(self) -> None:
        self.__acids: List[Acid] = []
        self.__spectators: List[Spectator] = []
        self.__auxiliaries: Dict[str, List[Auxiliary, str]] = {}   

    def add(self, element: Union[Acid, Spectator]) -> None:
        """
        Funtion used to add an acid species to the list of acids.

        Parameters
        ----------
        element: Union[Acid, Spectator
            The `Acid` or `Spectator` class enconding the properties and concentration of the species.

        Raises
        ------
        TypeError
            Exception raised if the `element` argument is not of `Acid` nor `Spectator` type.
        """
        if type(element) == Acid:
            self.__acids.append(element)
        elif type(element) == Spectator:
            self.__spectators.append(element)
        else:
            raise TypeError("The functions requires `Acid` or `Spectator` objects-")
        

    def add_auxiliary(self, auxiliary: Auxiliary, name: Optional[str] = None, color: Optional[str] = None):
        """
        Function used to add an auxiliary curve to the plot.

        Parameters
        ----------
        auxiliary: Auxiliary
            The `pypH.species.Auxiliary` object defining the curve to be plotted
        name: Optional[str]
            The name of the auxiliary curve. If set to `None` the name will be set to `aux. <N>` with
            `<N>` a progressive number starting from 1.
        color: Optional[str]
            The color to be used in tracing the auxiliary curve. If set to `None` (default) will leave
            the choice to matplotlib color sequence.
        
        Raises
        ------
        RuntimeError
            Exception raised if the deprotonation index of the Species is not compatible with the 
            selected acid or if the acid ID does not match one of the acid in the system.
        """

        if name is None:
            name = f"aux. {len(self.__auxiliaries)+1}"

        if name in self.__auxiliaries:
            raise ValueError("The selected auxiliary curve name is already in use")
        
        if type(auxiliary) != Auxiliary:
            raise TypeError("Auxiliary curve definitions must be provided as instances of the Auxiliary class")

        for species in auxiliary.species:

            if species.name == "H_3O^+" or species.name == "OH^-":
                continue
            
            if type(species) == AcidSpecies:
                
                for acid in self.__acids:
                    if acid.id == species.acid_id:

                        if species.index<0 or species.index>acid.nprotons:
                            raise RuntimeError("Invalid deprotonation index found")
                        break
                else:
                    raise RuntimeError("Invalid acid ID found")
            
            elif type(species) == SpectatorSpecies:

                for spectator in self.__spectators:
                    if spectator.id == species.spectator_id:
                        break
                else:
                    raise RuntimeError("Invalid acid ID found")

        self.__auxiliaries[name] = [auxiliary, color]

    def plot(
        self,
        pH_range: List[float] = [0, 14],
        pH_delta: float = 0.001,
        concentration_range: List[float] = [1e-14, 1],
        show_legend: bool = False,
        legend_location: Union[int, str] = 'lower right',
        figsize: Tuple[float] = [10, 9],
    ) -> None:
        """
        Funtion to plot the logarithmic diagram of the defined acid-base system.

        Parameters
        ----------
        pH_range: List[float]
            The minimum and maximum value of pH to be plotted, (defaut: [0, 14])
        pH_delta: float
            The pH steps used in plotting the diagram (defaut: 0.001)
        concentration_range: List[float]
            The range of concentrations to be plotted on the Y axis (default: [1e-14, 1])
        show_legend: bool
            If set to True will show the legend with the name of the traces (default: False)
        legend_location: Union[int, str]
            The location of the legend as expressed bu matplotlib. (default: lower right)
        figsize: Tuple[float]
            The tuple of float values setting the size of the figure.
        """

        pH_scale = np.arange(pH_range[0], pH_range[1], pH_delta)

        plt.rc("font", **{"size": 16})
        fig = plt.figure(figsize=figsize)

        hydronium = [10 ** (-pH) for pH in pH_scale]
        hydroxide = [10 ** (-14 + pH) for pH in pH_scale]

        plt.semilogy(pH_scale, hydronium, label=r"$H_3O^+$")
        plt.semilogy(pH_scale, hydroxide, label=r"$OH^-$")

        for acid in self.__acids:
            for i in range(acid.nprotons + 1):
                conc = [acid.concentration(i, pH) for pH in pH_scale]
                plt.semilogy(
                    pH_scale, conc, label=None if acid.names is None else acid.names[i]
                )
        
        for spectator in self.__spectators:
            plt.semilogy(pH_range, [spectator.concentration, spectator.concentration], label=spectator.name)

        if self.__auxiliaries != {}:
            for name, [auxiliary, color] in self.__auxiliaries.items():
                conc = []
                for pH in pH_scale:
                    value = 0.0
                    for species, coefficient in zip(auxiliary.species, auxiliary.coefficients):

                        if species.name == "H_3O^+":
                            value += coefficient * 10 ** (-pH)

                        elif species.name == "OH^-":
                            value += coefficient * 10 ** (-14 + pH)

                        elif type(species) == AcidSpecies:
                            i = [acid.id for acid in self.__acids].index(species.acid_id)
                            value += coefficient * self.__acids[i].concentration(species.index, pH)
                        
                        elif type(species) == SpectatorSpecies:
                            i = [spectator.id for spectator in self.__spectators].index(species.spectator_id)
                            value += coefficient * self.__spectators[i].concentration
                        else:
                            RuntimeError("Unexpected behavior: unknown species has been found")

                    conc.append(value)

                if color is not None:
                    plt.semilogy(pH_scale, conc, label=name, linestyle="--", color=color)
                else:
                    plt.semilogy(pH_scale, conc, label=name, linestyle="--")

        plt.ylim(concentration_range)
        plt.xlim(pH_range)

        plt.xlabel(r"$pH$", size=18)
        plt.ylabel(r"$\log(C_i)$", size=18)

        plt.grid(which="major", c="#DDDDDD")
        plt.grid(which="minor", c="#EEEEEE")

        if show_legend:
            plt.legend(loc=legend_location, fontsize=14)

        plt.tight_layout()
        plt.show()
