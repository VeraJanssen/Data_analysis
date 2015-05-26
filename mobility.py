# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:12:59 2015

@author: verajanssen
"""

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
mlin = np.empty(1)


 # open IVsd files from IVsd folder
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IV2/'

for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.dat'):
        print file
        IVsdnew = np.loadtxt(source_dir + file)
        IVsd = np.column_stack((IVsd, IVsdnew[:,1]))

bias = IVsdnew[:,0]*1000 #in mV       
for i in range(np.size(IVsd,1)):
    rawIVsd = plt.plot(bias, IVsd[:,i])
plt.show()
        
        

 # open IVg files from IVg folder
IVg = np.loadtxt('C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IVg/megasweep2.dat')
gate = np.linspace(0.5, -0.5, np.size(IVg,1))

for i in range(np.size(IVg, 0)):
    rawIVg = plt.plot(gate[600:680], IVg[i, 600:680])
    #subtract the Vg = 0V (background) curve. Use the middle column. Will give error when the number of measurements is odd (than there is no Vg = 0V) 
    normIVg = plt.plot(gate, IVg[i, :]-IVg[(np.size(IVg, 0)-1)/2])
    mlinnew = np.polyfit(gate[600:680], IVg[i,600:680]-IVg[2, 600:680], 1)
    mlin = np.column_stack([mlin, mlinnew[0]]) 

plt.scatter(np.linspace(-0.5, 0.5, 5),mlin[0,1:6]/np.linspace(-0.5, 0.5, 5))
 # check for loop or seperate files

 # plot both datasets in two figures in same window

 # save the figure with foldername, filenames, githash

 # calculate mobility, Rsq