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


plt.plot(daten[:,1],daten[:,2], 'r-')

#plt.plot(diff)
plt.show()

