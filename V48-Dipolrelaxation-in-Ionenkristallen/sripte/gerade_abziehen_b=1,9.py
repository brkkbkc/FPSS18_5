import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker


x,y = np.genfromtxt("(T,i(T))_b=1,9.txt", unpack=True)

a=0.016
b=-26.56
def efkt(x_,a_,b_):
	return np.exp(a_*x_)+b_

#for x_neu in x: #laeuft selber alle x werte durch, und weist x_neu[i]=x[i] zu
y_neu = y - efkt(x,a,b)
#x,y sind arrays, viele werte, also x[i], y[i] i von 0 bis 60,
#so aufgeschrieben ist identisch zu
#for i in range(0, 61):
# 	y_neu[i] = y[i] + gerade(x[i],m,b)

for y_neu_untereinander in y_neu:
	print(y_neu_untereinander)#durch nacheinanderausgabe der for schleife sind werte untereinander print(neu) macht so n packet

