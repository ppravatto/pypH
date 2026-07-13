(changelog)=
# Release notes

## Version `0.1.0`
First official release of the `pypH` package on PyPI. The main features of the release are:

- Definition of `Acid` class as general object to represent pH-active chemical system
- Definition of `Spectator` class as general object to represent pH-inactive chemical system
- Definition of `Species` abstract class and derivatives as a general representation of a species derived from a given system
- Definition of a `System` class handling in-solution chemistry and capable of plotting acid-base logarithmic diagrams and titration curves (still work in progress)

### Version `0.1.1`
Update to the `0.1.0` release implementing the following minor changes:

- When plotting logarithmic diagrams the `y` axis now shows the `C_i` label instead of `log(C_i)`. This is more correct since the scale is shown in logarithmic mode and not plotted as logarithmic units.
- Added `total_concentration` property to the `Acid` class to give the user easy access to the total conentration.
- Introduction of the `plot_distribution_diagram` function to plot distribution diagrams.

### Version `0.1.2`
Update to the `0.1.1` release implementing the following minor changes:

- Introduction of the `concentration_derivative_oxonium` in the `Acid` class returning the derivative of the concentration of a given deprotonation product as a function of the oxonium $H_3O^+$ concentration.
- Introduction of the `plot_buffer_capacity_diagram` function to represent the buffer capacity of an acid/base system.