import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker
from uncertainties import ufloat

x,y=np.genfromtxt("Differentiator_1804.txt", unpack=True)
i=0
for i in range(len(x)):
   xi=x[0:i]
   yi=y[0:i]
   print(xi)
   print(np.corrcoef(xi,yi))  #erstellet arrays x,y= . . x,y= . ., . .
   #x,y = . ., . ., . .  usw, alle subarrays aufsteigend
 
print(np.corrcoef(x,y))

#Ab x=13 isr korrelation kleiner also 0,9 (0,896), deshalb alle werte bis dahin
