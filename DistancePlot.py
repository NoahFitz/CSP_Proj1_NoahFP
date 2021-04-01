from OrbitalCalc import Difference
import matplotlib.pyplot as plt
from pylab import savefig, plot
import numpy as np
def DistPlot():
    fig = plt.figure()
    fig.suptitle('Earth-Mars Distance over 20 days (Starting 3/31/2021)')
    t = np.linspace(0,10,10)
    D = np.array([])
    for i in range(10):
        T = i*86400
        D = np.append(D, [Difference(T)*10**-10])
    plot(t, D, "k.")
    plt.xlabel("Time in Days")
    plt.ylabel("Disance in 10^10 Meters")
    savefig('DistancePlot')
DistPlot()




