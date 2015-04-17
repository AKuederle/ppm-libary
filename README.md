# ppm-library

This module has the porpoise of providing a few easy to use functions and classes to quickly manipulate a already processed matplotlib plot without redrawing it.

Its target use cases are the manipulation and the highlighting of certain parts of a plot, while showing it as part of a presentation or while observing the plotted data.

## Installation

This project is not jet a full module and more a work-in-process proof of concept. Therefore no setup script is provided yet. However you can place the *ppm.py* file inside your working directory and use the module by typing ```import ppm```.


## Working example

Imagine you have some multiline plot prepared to show your boss in a meeting. He is impressed by your pretty figure, but to better understand the data he wants see each line by its own or have this very dominant one temporary removed from the plot to better observe the other lines.

Instead of changing your code and redraw your entire figure, you can use some functionality provided by this module to easily accomplish such things.

A expected workflow would look something like this:

![Your pretty plot with all your important data](akuederle.github.io/ppm-library/readme_figs/simple_line_0.PNG)
