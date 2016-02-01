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

daten1 = np.genfromtxt("02011548.TXT", comments='#', delimiter='\t')
print daten1

