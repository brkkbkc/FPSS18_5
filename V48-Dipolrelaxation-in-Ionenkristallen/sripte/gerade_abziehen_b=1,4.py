import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker


x,y = np.genfromtxt("(T,i(T))_b=1,4.txt", unpack=True)

a=0.0156
b=-23.41
def efkt(x_,a_,b_):
	return np.exp(a_*x_)+b_

#for x_neu in x: #laeuft selber alle x werte durch, und weist x_neu[i]=x[i] zu
y_neu = y - efkt(x,a,b)

for y_neu_untereinander in y_neu:
	print(y_neu_untereinander)