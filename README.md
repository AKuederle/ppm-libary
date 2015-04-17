# ppm-library

This module has the porpoise of providing a few easy to use functions and classes to quickly manipulate a already processed matplotlib plot without redrawing it.

Its target use cases are the manipulation and the highlighting of certain parts of a plot, while showing it as part of a presentation or while observing the plotted data.

## Installation

This project is not jet a full module and more a work-in-process proof of concept. Therefore no setup script is provided yet. However you can place the *ppm.py* file inside your working directory and use the module by typing ```import ppm```.


## Working example

Imagine you have some multiline plot prepared to show your boss in a meeting. He is impressed by your pretty figure, but to better understand the data he wants see each line by its own or have this very dominant one temporary removed from the plot to better observe the other lines.

Instead of changing your code and redraw your entire figure, you can use some functionality provided by this module to easily accomplish such things.

A expected workflow would look something like this:


1. Plot your pretty plot with all your important data
![Your pretty plot with all your important data](http://akuederle.github.io/ppm-library/readme_figs/simple_line_0.PNG)

2. Call ppm.wiw() to display a table listing some properties of all displayed lines
![example wiw](http://akuederle.github.io/ppm-library/readme_figs/example_wiw_0.PNG)

3. Select a single or multiple lines based on their index (first column) or any other available line property using ppm.gl()
    - Get the line with index 3:
    ``` python
    ppm.gl(3)
    ```
    - Get all lines with dots as marker
    ``` python
    ppm.gl("o", "marker")
    ```

ppm.gl() returns a MulitLine class object. The MultiLine class can handle a list of lines and add certain properties to them.

4. Call a class-function to manipulate the selected lines.

Hide line 3 from the plot:
``` python
ppm.gl(3).hide()
```


