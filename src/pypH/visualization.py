from __future__ import annotations

from typing import List, Optional, Dict

import matplotlib.pyplot as plt
import numpy as np

from pypH.core import Acid
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
        self.__auxiliaries: Dict[str, Auxiliary] = {}

    def add(self, acid: Acid) -> None:
        """
        Funtion used to add an acid species to the list of acids.

        Parameters
        ----------
        acid: Acid
            The acid class enconding the properties and concentration of the acid.

        Raises
        ------
        TypeError
            Exception raised if the `acid` argument is not of `Acid` type.
        """

        if type(acid) != Acid:
            raise TypeError("Acid class object expected as argument")

        self.__acids.append(acid)

    def add_auxiliary(self, auxiliary: Auxiliary, name: Optional[str] = None):
        """
        Function used to add an auxiliary curve to the plot.

        Parameters
        ----------
        auxiliary: Auxiliary
            The `pypH.species.Auxiliary` object defining the curve to be plotted
        name: Optional[str]
            The name of the auxiliary curve. If set to `None` the name will be set to `aux. <N>` with
            `<N>` a progressive number starting from 1.
        
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
            
            for acid in self.__acids:
                if acid.id == species.acid_id:

                    if species.index<0 or species.index>acid.nprotons:
                        raise RuntimeError("Invalid deprotonation index found")
                    break
            else:
                raise RuntimeError("Invalid acid ID found")

        self.__auxiliaries[name] = auxiliary


    def plot(
        self,
        pH_range: List[float] = [0, 14],
        pH_delta: float = 0.001,
        concentration_range: List[float] = [1e-14, 1],
        show_legend: bool = False,
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
        """

        pH_scale = np.arange(pH_range[0], pH_range[1], pH_delta)

        plt.rc("font", **{"size": 16})
        fig = plt.figure(figsize=(10, 9))

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

        if self.__auxiliaries != {}:
            for name, auxiliary in self.__auxiliaries.items():
                conc = []
                for pH in pH_scale:
                    value = 0.0
                    for species, coefficient in zip(auxiliary.species, auxiliary.coefficients):

                        if species.name == "H_3O^+":
                            value += coefficient * 10 ** (-pH)

                        elif species.name == "OH^-":
                            value += coefficient * 10 ** (-14 + pH)

                        else:
                            i = [acid.id for acid in self.__acids].index(species.acid_id)
                            value += coefficient * self.__acids[i].concentration(species.index, pH)

                    conc.append(value)

                plt.semilogy(pH_scale, conc, label=name, linestyle="--")

        plt.ylim(concentration_range)
        plt.xlim(pH_range)

        plt.xlabel(r"$pH$", size=18)
        plt.ylabel(r"$\log(C_i)$", size=18)

        plt.grid(which="major", c="#DDDDDD")
        plt.grid(which="minor", c="#EEEEEE")

        if show_legend:
            plt.legend(loc=4)

        plt.tight_layout()
        plt.show()
