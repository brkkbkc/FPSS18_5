import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
from scipy import constants as con 
import csv
import matplotlib.ticker as plticker
from uncertainties import ufloat

e_0=8.8542*10**(-12)
z=2
Z=79
N=5.910*10**(28)
m_e=9.10938188*10**(-31)
v=0.915*con.c
I=9.225*con.e
E=ufloat(1.756*10**6*con.e, 0.1*10**6*con.e) #energie in joule, alle in m 
v=16270992

x=E/((4*np.pi*con.e**4*z**2*N*Z * np.log(2*m_e*v**2/I))/(m_e*v**2*(4*np.pi*con.epsilon_0)**2))

print(x)

