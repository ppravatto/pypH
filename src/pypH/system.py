from __future__ import annotations

from typing import List, Optional, Dict, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np

from pypH.acid import Acid, AcidSpecies
from pypH.spectator import Spectator, SpectatorSpecies
from pypH.species import Auxiliary


class System:
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

    def __validate_auxiliary(self, auxiliary: Auxiliary) -> None:
        """
        Validates an user provided auxiliay expression.

        Raises
        ------
        TypeError
            Exception raised if the auxiliary expression is not an `Auxiliary` type object.
        RuntimeError
            Exception raised if the deprotonation index of the Species is not compatible with the
            selected acid or if the acid ID does not match one of the acid in the system.
        """
        if type(auxiliary) != Auxiliary:
            raise TypeError(
                "Auxiliary curve definitions must be provided as instances of the `Auxiliary` class"
            )

        for species in auxiliary.species:

            if species.name == "H_3O^+" or species.name == "OH^-":
                continue

            if type(species) == AcidSpecies:

                for acid in self.__acids:
                    if acid.id == species.acid_id:

                        if species.index < 0 or species.index > acid.nprotons:
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

    def __evaluate_auxiliary(self, auxiliary: Auxiliary, pH: float) -> float:
        """
        Evaluates the auxiliary espression at the given pH.

        Arguments
        ---------
        auxiliary: Auxiliary
            The auxiliary expression to be evaluated
        pH: float
            The pH at which the expression must be evaluated

        Returns
        -------
        float
            The value of the auxiliary expression at the given pH
        """

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
                i = [spectator.id for spectator in self.__spectators].index(
                    species.spectator_id
                )
                value += coefficient * self.__spectators[i].concentration
            else:
                RuntimeError("Unexpected behavior: unknown species has been found")

        return value

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

    def add_auxiliary(
        self,
        auxiliary: Auxiliary,
        name: Optional[str] = None,
        color: Optional[str] = None,
    ):
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
        TypeError
            Exception raised if the auxiliary expression is not an `Auxiliary` type object.
        RuntimeError
            Exception raised if the deprotonation index of the Species is not compatible with the
            selected acid or if the acid ID does not match one of the acid in the system.
        """

        if name is None:
            name = f"aux. {len(self.__auxiliaries)+1}"

        if name in self.__auxiliaries:
            raise ValueError("The selected auxiliary curve name is already in use")

        self.__validate_auxiliary(auxiliary)
        self.__auxiliaries[name] = [auxiliary, color]

    def plot_logarithmic_diagram(
        self,
        pH_range: List[float] = [0, 14],
        pH_delta: float = 0.001,
        concentration_range: List[float] = [1e-14, 1],
        show_legend: bool = False,
        legend_location: Union[int, str] = "lower right",
        figsize: Tuple[float] = [10, 9],
        save_path: Optional[str] = None,
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
        save_path: Optional[str]
            The path of the file where to save the logarithmic diagram image. If set to None (default)
            will only display the result to the user without saving the plot.
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
            plt.semilogy(
                pH_range,
                [spectator.concentration, spectator.concentration],
                label=spectator.name,
            )

        if self.__auxiliaries != {}:
            for name, [auxiliary, color] in self.__auxiliaries.items():
                conc = []
                for pH in pH_scale:
                    value = self.__evaluate_auxiliary(auxiliary, pH)
                    conc.append(value)

                if color is not None:
                    plt.semilogy(
                        pH_scale, conc, label=name, linestyle="--", color=color
                    )
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

        if save_path is not None:
            plt.savefig(save_path, dpi=600)

        plt.show()

    def solve(
        self,
        first: Auxiliary,
        second: Auxiliary,
        pH_range: Tuple[float, float] = (0.0, 14.0),
        eabs: float = 1e-6,
    ) -> float:
        """
        Numerically comutes the pH at which the equality `first == second` is satisfied. The function
        uses the dicotomic method in the range `pH_range` to solve the proble iteratively until the
        absolute variation between the terms is smaller then `eabs`.

        Arguments
        ---------
        first: Auxiliary
            The expression for the left side of the equation
        second: Auxiliary
            The expression for the right side of the equation
        pH_range: Tuple[float, float]
            The pH range in which the solution must be searched. (default: (0., 14.))
        eabs: float
            The maximum absolute error between iteration points to stop the dicotomic search. (default: 1e-6)
        
        Raises
        ------
        TypeError
            Exception raised if the auxiliary expression is not an `Auxiliary` type object.
        RuntimeError
            Exception raised if the deprotonation index of the Species is not compatible with the
            selected acid or if the acid ID does not match one of the acid in the system.
        
        Returns
        -------
        float
            The pH value at which the equality is satisfied.
        """

        self.__validate_auxiliary(first)
        self.__validate_auxiliary(second)

        left, right = min(pH_range), max(pH_range)

        lvalue = self.__evaluate_auxiliary(first - second, left)
        rvalue = self.__evaluate_auxiliary(first - second, right)

        while True:
            middle = 0.5 * (left + right)

            if right - left < eabs:
                return middle

            mvalue = self.__evaluate_auxiliary(first - second, middle)

            if mvalue == 0.0:
                return middle
            elif lvalue * mvalue < 0:
                right = middle
                rvalue = mvalue
            elif rvalue * mvalue < 0:
                left = middle
                lvalue = mvalue
            else:
                raise RuntimeError("No change in sign found in dicotomic range.")