import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
from scipy import constants as con 
import csv
import matplotlib.ticker as plticker
from uncertainties import ufloat

theta, Z_out=np.genfromtxt("zaehlrate-und-zugehoeriger-winkel.txt", unpack=True)
Z_out = Z_out/60
theta=theta*2*np.pi/360

Z_Quelle=285/1 #pro sekunde
F=20*10**(-6)
A_Folie=np.pi*1/4*10**(-4) #1cm durchmesser
A_Detektor=np.pi*1/4*10**(-4)
pi=np.pi
d=2*10**(-6)
N_Folie= 1.18*10**(22) #N_Folie (in anzahl pro m^2) = N(teilchenanzahl pro m^3 *d), eigentlich 23 im exponenten

#y=((Z_out*8*pi**2 * 0.039**2 * 0.017**2)/(Z_Quelle*F*A_Folie*np.cos(theta/2)))*((8*pi**2*0.041**2*0.04**2)/(F*A_Detektor))*1/(N_Folie*d)
#print(y)

#eigentlich
y=((Z_out*4*pi*(0.0039+0.0017)**2)/(Z_Quelle*A_Folie))*((4*pi*(0.0039+0.0017+0.0041)**2)/(F))*((1)/(N_Folie))
#print(y)

#jetzt normale funktion plotten
x=np.linspace(1,20,1000)
#x=x*2*np.pi/360
e_0=8.8542*10**(-12)
z=2
Z=79
E_a=5486
y_2=(1/(4*pi*e_0)**2)*((z*Z*con.e)/(4*5486*10**6))**2 * (1/( np.sin(((x-2.7)*2*pi/360)*pi/360)**4) ) 
#bei python ist entspricht np.sin(x*2*np.pi/360) sin(x) im taschenrechner
print(y_2)

#plt.plot(theta,y)
plt.plot(x,y_2)
plt.ylim(0, 4*10**(-21))
plt.show()
