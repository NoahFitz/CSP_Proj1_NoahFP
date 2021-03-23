#Author: Noah FitzPatrick
#Date: 3/23/2021
#Takes in orbital data of two planets and calculates the distance between the two
import numpy as np

def ReadOrbitalData():
    orbit_data = np.loadtxt('OrbitData.csv', delimiter =",", skiprows = 1)
    print(orbit_data)

ReadOrbitalData()

