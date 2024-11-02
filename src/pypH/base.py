import matplotlib.pyplot as plt
import numpy as np

from typing import List, Dict, Optional


class Acid:
    """
    The Acid class encodes the behavior of a generic mono or polyprotic acid. The number of acidic protons
    is defined automatically by setting the pKa values.

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

    __acid_id = 0

    def __init__(
        self, pka: List[float], concentration: float, names: Optional[List[str]] = None
    ) -> None:
        
        self.__Ca: float = concentration
        self.__pka: List[float] = sorted(pka)
        self.__ka = [10 ** (-pka) for pka in self.__pka]

        self.__betas = [1]
        for ka in self.__ka:
            self.__betas.append(self.__betas[-1] * ka)

        if names is None:

            letter = chr(ord('A') + Acid.__acid_id)

            self.__names = []

            for i in range(self.nprotons+1):
                
                name = "$"
                name += "H" if self.nprotons - i > 0 else ""
                name += ("_{" + f"{self.nprotons-i}" + "}") if self.nprotons - i > 1 else ""
                name += f"{letter}"
                
                if i!=0:
                    name += "^-" if i==1 else "^{" + f"{i}" + "-}"
                
                name += "$"
                self.__names.append(name)
        
        else:

            if len(names) != self.nprotons + 1:
                raise ValueError(
                    "The number of provided names does not match the number of deprotonation products"
                )
            
            self.__names = names  

        Acid.__acid_id += 1       


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


class Term:
    """
    Simple class used to define a term to be used in the definition of an auxiliary curve.

    Attribues
    ---------
    name: str
        The name of the acid from which the term should be selected
    index: int
        The deprotonation index of the desired form.
    coefficient: float
        The coefficient to be applied to the term.
    """

    def __init__(self, name: str, index: int, coefficient: float = 1.0):
        self.name: str = name
        self.index: int = index
        self.coefficient: float = coefficient


class Hydronium(Term):
    """
    Simple class to define a hydronium ion term in an auxiliary curve definition.
    The name of the species is automatically set to "H_3O^+"

    Attribues
    ---------
    coefficient: float
        The coefficient to be applied to the term.
    """

    def __init__(self, coefficient: float = 1):
        super().__init__("H_3O^+", None, coefficient)


class Hydroxide(Term):
    """
    Simple class to define a hydroxide ion term in an auxiliary curve definition.
    The name of the species is automatically set to "OH^-"

    Attribues
    ---------
    coefficient: float
        The coefficient to be applied to the term.
    """

    def __init__(self, coefficient: float = 1):
        super().__init__("OH^-", None, coefficient)


class Plotter:
    """
    A simple class dedicated to the plot and manipulation of logarithmic diagrams. The class
    allows the user to define a system of acid and plot the concentration of the various deprotonation
    products as a function of the pH. The class also allows the user to define auxiliary curves to
    solve specific problems (e.g. solution based on protonic balance)
    """

    def __init__(self) -> None:
        self.__acids: Dict[str, Acid] = {}
        self.__auxiliary: Dict[str, List[Term]] = {}

    def add(self, name: str, acid: Acid) -> None:
        """
        Funtion used to add an acid species to the list of acids.

        Parameters
        ----------
        name: str
            The name used to indentify the acid.
        acid: Acid
            The acid class enconding the properties and concentration of the acid.

        Raises
        ------
        TypeError
            Exception raised if the `acid` object is not of `Acid` type.
        KeyError
            Exception raised if the name used to identify the acid is already in use.
        """

        if type(acid) != Acid:
            raise TypeError("Acid class object expected as argument")

        if name in self.__acids:
            raise ValueError("The name is aleady in use")

        self.__acids[name] = acid

    def add_auxiliary(self, terms: List[Term], name: Optional[str] = None):
        """
        Function used to add an auxiliary curve to the plot.

        Parameters
        ----------
        terms: List[Term]
            The list of terms that compose the auxiliary curve

        name: Optional[str]
            The name of the auxiliary curve. If set to None the curve will be called "aux. N" with
            N a progressive number.
        """

        if name is None:
            name = f"aux. {len(self.__auxiliary)+1}"

        if name in self.__auxiliary:
            raise ValueError("Auxiliary name already in use")

        for term in terms:

            if term.name == "H_3O^+" or term.name == "OH^-":
                continue

            if term.name not in self.__acids.keys():
                raise ValueError("Acid name invalid")

            if term.index < 0 or term.index > self.__acids[term.name].nprotons:
                raise ValueError("Deprotonation index is invalid")

        self.__auxiliary[name] = terms

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

        for name, acid in self.__acids.items():
            for i in range(acid.nprotons + 1):
                conc = [acid.concentration(i, pH) for pH in pH_scale]
                plt.semilogy(
                    pH_scale, conc, label=None if acid.names is None else acid.names[i]
                )

        if self.__auxiliary != {}:
            for name, terms in self.__auxiliary.items():
                conc = []
                for pH in pH_scale:
                    value = 0.0
                    for term in terms:

                        if term.name == "H_3O^+":
                            value += term.coefficient * 10 ** (-pH)

                        elif term.name == "OH^-":
                            value += term.coefficient * 10 ** (-14 + pH)

                        else:
                            value += term.coefficient * self.__acids[
                                term.name
                            ].concentration(term.index, pH)

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


