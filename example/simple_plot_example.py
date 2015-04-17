# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:37:50 2015

@author: Arne
"""
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
x=np.arange(0,10,1)
plt.plot(x,x,"o")        
plt.plot(x,2*x,"o")
plt.plot(x,3*x,"o")
plt.plot(x,4*x,"-")