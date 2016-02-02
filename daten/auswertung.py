# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as rnd
import scipy as sp
import matplotlib as mt
import scipy.integrate as inte
#mt.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import *
import sys
import time as ti

daten = np.array(np.genfromtxt("02011548.TXT", comments='#', delimiter='\t'))
#daten1 = np.array(np.genfromtxt("02011347.TXT", comments='#', delimiter='\t'))

daten[:,1] /= 1e6
daten[:,2] /= 1e5
daten[:,3] /= 100.0
daten[:,4] /= 100.0
daten[:,0] -= daten[0,0]

laengengrad = daten[:,2]*(4e4/360.0)
breitengrad = laengengrad*np.sin(np.pi/2.0-(np.pi/180.0)*daten[:,1])

fig = figure()
plt.plot(daten[:,1],daten[:,2], 'r-')
fig.show()

fig = figure()
plt.plot(breitengrad,laengengrad)
#plt.plot(diff)
plt.show()

