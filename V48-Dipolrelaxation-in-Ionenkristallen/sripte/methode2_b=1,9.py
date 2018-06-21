import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker
#benutz jetz alten x,y werte, ohne abgezogene gerade!!

y = np.genfromtxt("(T,i(T))_b=1,9_neu.txt", unpack=True)#nur neuen y werte gepeichert
x,s = np.genfromtxt("(T,i(T))_b=1,9.txt", unpack=True)#alten x werte holen, muss aber auch alten y werte generieren (s), da zwei spalten
m_sternchen=34 #T_35 ist T*, also T wo i(T) minimum hat
y_ne=[0] * 35 #leeres array (wie aus np.genfromtxt) mit 35 plaetzen
for n in range(0, m_sternchen+1):
	for m in range(n, m_sternchen+1):
			y_ne[n] += (x[m+1]-x[m])*y[m]
#numerisches integrieren (obersumme)

#y_neu=np.log(y_ne/y)#geht nicht, weil y_ne 35 lang, y 64 lang
y_neu=[0]*35
for i in range(0,34+1):
	y_neu[i]=np.log(y_ne[i]/y[i])
#y werte logarithmisch oder normal bei achse logarythmisch ist exakt selber graph, aber bei werte logarithmisch, hat man die werte selbst geandert-> log achse ist das richtige 


#print(y_neu)
for y_neu_untereinander in y_neu:
	print(y_neu_untereinander)

for y_ne_untereinander in y_ne:
	print(y_ne_untereinander)