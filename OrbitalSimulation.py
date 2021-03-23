#Author: Noah FitzPatrick
#Date: 3/23/2021
#Takes in orbital data of two planets and calculates the distance between the two
import numpy as np

def ReadOrbitalData(): #Takes in data for the two planets
    orbit_data = np.loadtxt('OrbitData.csv', delimiter =",", skiprows = 1)
    return orbit_data
print(ReadOrbitalData())

def GenerateOrbitalPlot():
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
