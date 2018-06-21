import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker

y = np.genfromtxt("(T,i(T))_b=1,9_neu.txt", unpack=True)
x,s = np.genfromtxt("(T,i(T))_b=1,9.txt", unpack=True)

plt.plot(x,y, "rx", label="Messwerte")
plt.xlabel("$t/s$")
plt.ylabel("$U_A/V$")
plt.title("gedaempfte schwingung h), also ausgangsspannung U_A als funktion der zeit")

plt.grid()
#plt.yscale("log")#logarithmische y achse
plt.legend(loc= "best")
plt.tight_layout()#wird so gemacht, dass graph erster und letzter wert genau an bildgrenze sind, und in y achse auch weniger platz lassen bis zum graphen
#plt.show()
plt.savefig("test_1,9.pdf")
