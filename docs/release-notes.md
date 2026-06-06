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