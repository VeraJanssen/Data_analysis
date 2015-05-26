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
    rawIVg = plt.plot(gate, IVg[i, :])
    #subtract the Vg = 0V (background) curve. Use the middle column. Will give error when the number of measurements is odd (than there is no Vg = 0V) 
    normIVg = plt.plot(gate, IVg[i, :]-IVg[(np.size(IVg, 0)+1)/2])


 # open IVg files from IVg folder

 # check for loop or seperate files

 # plot both datasets in two figures in same window

 # save the figure with foldername, filenames, githash

 # calculate mobility, Rsq