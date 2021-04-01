from OrbitalCalc import Velocity
import matplotlib.pyplot as plt
from pylab import savefig, plot
import numpy as np
def VelPlot():
    fig = plt.figure()
    fig.suptitle('Velocity vs Distance in Degrees from 0 to 90 degrees')
    d = np.linspace(0,180,180)
    V1 = np.array([])
    for i in range(180):
        V1 = np.append(V1, [Velocity(i)[0]])
    V2 = np.array([])                         
    for i in range(180):
        V2 = np.append(V2, [Velocity(i)[1]])
    plot(d, V1, "b.", V2, "r.")
    plt.xlabel("Degrees")
    plt.ylabel("Tangential Velocity in m/s")
    savefig('VelocityPlot')
VelPlot()




