# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:35:41 2015

@author: verajanssen
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import fnmatch
import os

 # ask for inputs:
    #working folder
    #device size
    #....
IVsd = np.empty(297)


 # open IVsd files from IVsd folder
#IVsd = np.loadtxt('C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IV2/Vgn1100mV.dat')
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IV2/'
#file_list = glob('C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IV2/')


for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.dat'):
        print file
        IVsdnew = np.loadtxt(source_dir + file)
        IVsd = np.column_stack((IVsd, IVsdnew[:,1]))
        
for i in range(np.size(IVsd,1)):
    rawIVsd = plt.plot(IVsd)
        
        

 # open IVg files from IVg folder
IVg = np.loadtxt('C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IVg/megasweep2.dat')
gate = np.linspace(0.5, -0.5, np.size(IVg,1))

for i in range(np.size(IVg, 0)):
    rawIVg = plt.plot(gate, IVg[i, :])
    #subtract the Vg = 0V (background) curve. Use the middle column. Will give error when the number of measurements is odd (than there is no Vg = 0V) 
    normIVg = plt.plot(gate, IVg[i, :]-IVg[(np.size(IVg, 0)+1)/2])
    

 # check for loop or seperate files

 # plot both datasets in two figures in same window

 # save the figure with foldername, filenames, githash

 # calculate mobility, Rsq