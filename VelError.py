#Author: Noah FitzPatrick
#Date: 3/27/2021
#Displays error in velocity data

import numpy as np
from pylab import savefig, plot
import matplotlib.pyplot as plt
from matplotlib import patches
def ReadOrbitalData(): #Takes in data for the two planets
    orbit_data = np.loadtxt('OrbitData.csv', delimiter =",", skiprows = 1)
    return orbit_data
print(ReadOrbitalData())

def VelocityEr(): #Plots an image of the two planets' orbits
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    deg = np.linspace(0,9000,9000)
    theta = (np.pi*deg)/18000
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    vtheta1 = (np.sqrt(G*M*a1*(1-e1**2)))/r1
    thetaB = (np.pi*(deg+0.5))/18000                      
    r1B = (a1*(1-e1**2))/(1+e1*np.cos(thetaB))     
    vtheta1B = (np.sqrt(G*M*a1*(1-e1**2)))/r1B
    E = (abs(vtheta1B - vtheta1)/vtheta1B)*100
    plot(deg, E)
    savefig('ErrorTest4')
VelocityEr()
def Velocity(d):
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    deg = d
    theta = (np.pi*deg)/180
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    vtheta1 = (np.sqrt(G*M*a1*(1-e1**2)))/r1
    return vtheta1
"""
print(Velocity(0))
print(Velocity(0.5))
print(Velocity(1))
print(Velocity(1.5))
print(abs(Velocity(20.1)-Velocity(20)))
"""
