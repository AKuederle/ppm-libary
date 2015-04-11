# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:54:34 2015

@author: Arne
"""

import matplotlib.pyplot as plt
import numpy as np

def _print_table(row_header, line_header, data):
    """Controll table formatting of output.
    
    Code taken from: http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
    """
    row_format = "{:>15}" * (len(row_header) + 1)
    print(row_format.format("", *row_header))
    for line_head, row in zip(line_header, data):
        print(row_format.format(line_head, *row))
    

def wiw(fig=plt.gcf(),props=["c", "marker"]):
    """ 'What is what' display all lines with respective properties linked to a given figure. """
    for ax in fig.get_axes():
        lines = []
        data = []
        for line in ax.get_lines():
            lines.append(plt.getp(line, "label"))
            data_line = []
            for prop in props:
                data_line.append(plt.getp(line, prop))
            data.append(data_line)
        _print_table(props, lines, data)
        