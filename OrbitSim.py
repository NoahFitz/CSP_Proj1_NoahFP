#from OrbitalSimulation import Difference
import numpy as np
from pylab import savefig, plot
import matplotlib.pyplot as plt
from matplotlib import patches

def ReadOrbitalData(): #Takes in data for the two planets
    orbit_data = np.loadtxt('OrbitData.csv', delimiter =",", skiprows = 1)
    return orbit_data

def GenerateOrbitalPlot(): #Plots an image of the two planets' orbits
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    width1 = 2 * a1 * np.sqrt(1-e1)
    height1 = 2 * a1
    orbit1 = patches.Ellipse((a1*e1,0), width1, height1, angle=0, linewidth=2, fill=False)
    width2 = 2 * a2 * np.sqrt(1-e2)
    height2 = 2 * a2
    orbit2 = patches.Ellipse((a2*e2,0), width2, height2, angle=0, linewidth=2, fill=False)
    ax = plt.gca()
    ax.add_patch(orbit1)
    ax.add_patch(orbit2)
    plt.axis("scaled")
    savefig("EllipseTest2.png")

GenerateOrbitalPlot()
