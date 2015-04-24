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
        
def gl(line="_all_", identifier="id", fig="_current_"):
    """ Get a one or more lineobjekts based on a certain line-propertie."""
    if identifier == "id":
        props = []
    else:
        props = [identifier]
    lines, data =  wiw(fig=fig, props=props, _return=True)
    if line == "_all_":
        return MultiLine(lines)
    elif identifier == "id":
        if hasattr(line, "__getitem__") is False:
            line = [line]
        return MultiLine(list(map(lines.__getitem__, line)))
    else:
        line_id = [i for i, j in enumerate(data) if j[-1] == line]
        return MultiLine(list(map(lines.__getitem__, line_id)))
        
class MultiLine:
    def __init__(self, lines):
        if hasattr(lines, "__getitem__") is True:
            self.lines = lines
        else:
            self.lines = [lines]
        
    def __getitem__(self, index):
        return MultiLine(self.lines[index])
    
    def setp(self, propertie, value):
        if hasattr(value, "__getitem__") is True:
            for line, val in zip(self.lines, value):
                plt.setp(line, propertie, val)
        else:
            for line in self.lines:
                plt.setp(line, propertie, value)
                
    def getp(self, propertie):
        props = []
        for line in self.lines:
            props.append(plt.getp(line, propertie))
        return props
            
    def hide(self):
        self.setp("visible", False)
    #alias:
    h = hide
    
    def show(self):
        self.setp("visible", True)
    #alias:
    s = show
    
    def focus(self):
        self.focus_off()
        for line in gl().lines:
            if plt.getp(line, "visible") is True:
                line._temp_hide = True
                plt.setp(line, "visible", False)
            else:
                line._temp_hide = False
        for line in self.lines:
            line._temp_hide = False
        self.show()
        
    #alias:
    f = focus 
    
    def focus_off(self):
        for line in gl().lines:
            if hasattr(line, "_temp_hide") and line._temp_hide is True:
                plt.setp(line, "visible", True)
    
    #alias:
    fo = focus_off
    
    def highlight(self):
        for line, width, size, z in zip(self.lines, self.getp("linewidth"), self.getp("markersize"), self.getp("zorder")):
            if not hasattr(line, "_highlight") or line._highlight is False:
                line._non_high_width = width
                line._non_high_size = size
                line._non_high_z = z
                plt.setp(line, "linewidth", 3*width)
                plt.setp(line, "markersize", 1.5*size)
                plt.setp(line, "zorder", 0)
                line._highlight = True
            else:
                pass
            
    #alias:
    hi = highlight
    
    def highlight_off(self, _all=False):
        if _all is True:
            lines = gl().lines
        else:
            lines = self.lines
        for line in lines:
            if hasattr(line, "_highlight") and line._highlight is True:
                plt.setp(line, "linewidth", line._non_high_width)
                plt.setp(line, "markersize", line._non_high_size)
                plt.setp(line, "zorder", line._non_high_z)
                line._highlight = False
                
    #alias:
    ho = highlight_off
        