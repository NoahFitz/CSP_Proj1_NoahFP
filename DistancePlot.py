from OrbitalCalc import Difference
import matplotlib.pyplot as plt
from pylab import savefig, plot
import numpy as np
def DistPlot():
    t = np.linspace(0,10,10)
    D = np.array([])
    for i in range(10):#range(900)
        T = i*86400
        D = np.append(D, [Difference(T)*10**-10])
    plot(t, D, "k.")
    savefig('DistancePlot')
DistPlot()




