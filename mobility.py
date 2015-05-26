# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:35:41 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


 # ask for inputs:
    #working folder
    #device size
    #....



 # open IVsd files from IVsd folder

IVg = np.loadtxt('D:/verajanssen/megasweep2.dat')
gate = np.linspace(0.5, -0.5, np.size(IVg,1))

for i in range(np.size(IVg, 0)):
    plt.plot(gate, IVg[i, :])
plt.show()



 # open IVg files from IVg folder

 # check for loop or seperate files

 # plot both datasets in two figures in same window

 # save the figure with foldername, filenames, githash

 # calculate mobility, Rsq