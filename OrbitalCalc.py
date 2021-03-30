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

def Velocity(d):
    G = 6.67430*(10**-11)#N*m^2/kg^2
    M = 1.989*(10**30)#kg
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]*10**10
    a2 = ReadOrbitalData()[1][1]*10**10
    deg = d
    theta = (np.pi*deg)/18
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    vtheta1 = np.sqrt(G*M*a1*(1-e2**2))/r1
    r2 = (a2*(1-e2**2))/(1+e2*np.cos(theta))
    vtheta2 = np.sqrt(G*M*a2*(1-e2**2))/r2
    return vtheta1, vtheta2

def Radius(d):
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]*10**10
    a2 = ReadOrbitalData()[1][1]*10**10
    deg = d                     
    theta = (np.pi*deg)/180
    r1 = (a1*(1-e1**2))/(1+e1*np.cos(theta))
    r2 = (a2*(1-e2**2))/(1+e2*np.cos(theta))
    return r1, r2

def DeltaT(d):
    v1 = Velocity(d)[0]/(Radius(d)[0])
    Dt1 = (np.pi/1800)/v1
    v2 = Velocity(d)[1]/(Radius(d)[1])
    Dt2 = (np.pi/1800)/v2
    return Dt1, Dt2

def TimeElapsed(D):
    d=0
    t1=0
    t2=0
    D=D
    while d<D:
        v = Velocity(d)[0]/(Radius(d)[0])
        d = d + 1
        t1 = t1 + d/v*(np.pi/180)
    d=0
    while d<D:
        v = Velocity(d)[1]/(Radius(d)[1])
        d = d + 1
        t2 = t2 + d/v*(np.pi/180)
    return t1, t2

def Distance(T):
    t=0
    d1=0
    d2=0
    while t<T:
        d1 = d1 + 0.1
        t = t + DeltaT(d1)[0]
    t=0
    while t<T:
        d2 = d2 + 0.1
        t = t + DeltaT(d2)[1]
    return d1, d2

def XandY(T):
    e1 = ReadOrbitalData()[0][0]
    e2 = ReadOrbitalData()[1][0]
    a1 = ReadOrbitalData()[0][1]*10**10
    a2 = ReadOrbitalData()[1][1]*10**10
    d1 = Distance(T)[0]
    x1 = Radius(d1)[0]*np.cos(d1)
    y1 = Radius(d2)[0]*np.sin(d2)
    d2 = Distance(T)[1]
    x2 = Radius(d2)[1]*np.cos(d2)
    y2 = Radius(d2)[1]*np.sin(d2)
    return x1, x2, y1, y2

def Difference(T):
    x1 = XandY(T)[0]
    x2 = XandY(T)[1]
    y1 = XandY(T)[2]
    y2 = XandY(T)[3]
    dif = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dif


#Test statements:
#t = 3*86400
#print(Distance(t)[0], Distance(t)[1])
#print(TimeElapsed(2))
#print(Velocity(1)[0], Velocity(1)[1])
#print(XandY(3)[0]*10**-10, XandY(3)[1]*10**-10, XandY(3)[2]*10**-10, XandY(3)[3]*10**-10)
#print(Difference(3))

