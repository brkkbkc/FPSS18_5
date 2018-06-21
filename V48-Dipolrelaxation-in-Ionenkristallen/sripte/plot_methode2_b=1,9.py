import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker

y = np.genfromtxt("(T,i(T))_b=1,9_methode2.txt", unpack=True)
x,s = np.genfromtxt("(T,i(T))_b=1,9_xybisT*.txt", unpack=True)

plt.plot(1/x,y, "rx", label="Messwerte")
#plt.xlabel()
#plt.ylabel()
#plt.title()

plt.grid()
#plt.yscale("log")#logarithmische y achse
plt.legend(loc= "best")
plt.tight_layout()#wird so gemacht, dass graph erster und letzter wert genau an bildgrenze sind, und in y achse auch weniger platz lassen bis zum graphen
#plt.show()
plt.savefig("methode2_b=1,9")
