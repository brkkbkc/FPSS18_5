import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker

#alten y werte, vor abzug des untergrunds
y = np.genfromtxt("(T,i(T))_b=1,4_neu.txt", unpack=True)
x,s = np.genfromtxt("(T,i(T))_b=1,4.txt", unpack=True)
m_sternchen=40 
y_ne=[0] * 41 
for n in range(0, m_sternchen+1):
	for m in range(n, m_sternchen+1):
			y_ne[n] += (x[m+1]-x[m])*y[m]
#numerisches integrieren (obersumme)

y_neu=[0]*41
for i in range(0,40+1):
	y_neu[i]=np.log(y_ne[i]/y[i])


#print(y_neu)
for y_neu_untereinander in y_neu:
	print(y_neu_untereinander)