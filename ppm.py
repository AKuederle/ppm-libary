# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:54:34 2015

@author: Arne
"""

import matplotlib.pyplot as plt
import numpy as np


def _print_table(row_header, data):
    """Controll table formatting of output.
    
    Code taken from: http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
    """
    line_numbers = np.arange(len(data))
    row_format = "{}" + "{:>15}" * (len(row_header))
    print(row_format.format("", *row_header))
    for line_number, line in zip(line_numbers, data):
        print(row_format.format(line_number, *line))
    

def wiw(fig="_current_", props=["c", "marker"], _return=False):
    """ Display all lines with respective properties linked to a given figure. """
    if fig == "_current_":
        fig = plt.gcf()
    if "label" not in props and "visible" not in props: 
        props[:0] = ["label", "visible"]
    data = []
    lines = []
    for ax in fig.get_axes():
        ax_lines = ax.get_lines()
        lines.extend(ax_lines)
        for line in ax_lines:
            data_line = []
            for prop in props:
                data_line.append(plt.getp(line, prop))
            data.append(data_line)
    if _return is True:
        return lines, data
    else:
        _print_table(props, data)