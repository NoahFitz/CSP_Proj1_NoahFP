#Author: Noah FitzPatrick
#Date: 3/23/2021
#Takes in orbital data of two planets and calculates the distance between the two
import numpy as np
from pylab import savefig, plot
import matplotlib.pyplot as plt
from matplotlib import patches
def ReadOrbitalData(): #Takes in data for the two planets
    orbit_data = np.loadtxt('OrbitData.csv', delimiter =",", skiprows = 1)
    return orbit_data
print(ReadOrbitalData())

def GenerateOrbitalPlot(): #Plots an image of the two planets' orbits
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    #y1 = np.sqrt((1-e1)*(a1**2 - x**2))
    width1 = 2 * a1 * np.sqrt(1-e1)
    height1 = 2 * a1
    orbit1 = patches.Ellipse((e1*a1,0), width1, height1, angle=0, linewidth=2, fill=False)
    plot(orbit1)
    savefig('OrbitSim3.png')
#GenerateOrbitalPlot()

#def Velocity(d): #Plots an image of the two planets' orbits
 #   G = 6.67430*(10**-11)#N*m^2/kg^2
  #  M = 1.989*(10**30)#kg
 #  # e1 = ReadOrbitalData()[0][0]
  #  e2 = ReadOrbitalData()[1][0]
#   # a1 = ReadOrbitalData()[0][1]
#    a2 = ReadOrbitalData()[1][1]
#    deg = np.linspace(0,9000,9000)
#    theta = (np.pi*deg)/18000
#    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
#    vtheta1 = (np.sqrt(G*M*a1*(1-e1**2)))/r1
#    thetaB = (np.pi*(deg+0.5))/18000                      
#    r1B = (a1*(1-e1**2))/(1+e1*np.cos(thetaB))     
#    vtheta1B = (np.sqrt(G*M*a1*(1-e1**2)))/r1B
#TimeElapsed()


def Velocity(d):#Velocity is ridonculous
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    deg = d
    theta = (np.pi*deg)/18
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    vtheta1 = np.sqrt(G*M*a1*(1-e1**2))/r1
    r2 = (a2*(1-e2**2))/(1+e2*np.cos(theta))
    vtheta2 = np.sqrt(G*M*a2*(1-e2**2))/r2
    return vtheta1, vtheta2

def Radius(d):
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    deg = d                     
    theta = (np.pi*deg)/180
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    r2 = (a2*(1-e2**2))/(1+e2*np.cos(theta))
    return r1, r2

def Distance(T):
    t=0
    d=0
    T=T
    while t<T:
        v = Velocity(d)[0]/(Radius(d)[0])
        D1 = d + t*v
        t = t + 1
        
    t=0
    d=0
    while t<T:
        v = Velocity(d)[1]/(Radius(d)[1])
        D2 = d + t*v
        t = t + 1
    return D1, D2

def XandY(T):#Error with x1
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]
    a2 = ReadOrbitalData()[1][1]
    d1 = Distance(T)[0]
    x1 = Radius(d1)[0]*np.cos(d1)
    y1 = np.sqrt((1-e1)*(a1**2-x1**2))
    d2 = Distance(T)[1]
    x2 = Radius(d2)[1]*np.cos(d2)
    y2 = np.sqrt((1-e2)*(a2**2-x2**2))
    return x1, y1, y2, y3

def Difference(T):
    x1 = XandY(T)[0]
    x2 = XandY(T)[1]
    y1 = XandY(T)[2]
    y2 = XandY(T)[3]
    dif = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dif




print(Distance(3))
print(Velocity(1))
print(XandY(3)[0], XandY(3)[1])


