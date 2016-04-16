import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

a=1.0
b=0.2
def func(y,t):
    # Defines the differential equations
    y0, y1 = y
    return [(a*(y0 - y0*y1)), (b*(-y1 + y0*y1))]

def Psfigure(t, prey,predators):
    fig=plt.figure(1)
    plt.subplot(211)
    plt.plot(t, prey, "+", label="rabbits")
    plt.plot(t, predators, "rx", label="Foxes")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population against Time(Year)")
    plt.legend();
    plt.subplot(212)
    plt.plot(prey, predators, "-")
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.title("Predators against Prey");
    fig = plt.gcf()
    fig.set_size_inches(15,15)
    return plt.show()

if __name__ == "__main__":
    
    t0=0
    tn=5
    N=100
    t = np.linspace(t0,tn,N+1)
    
    # System ODE for y0(t=0)=0.1, y1(t=0)=1.0
    y_0= [0.1,1.0]
    Ps = odeint(func, y_0, t)
    prey = Ps[:,0]
    predators = Ps[:,1]
    #its plot
    Psfigure(t, prey, predators)
    
    #Test sensitivity of initial conditions
    y_0= [0.11,1.0]
    Ps1 = odeint(func, y_0, t)
    prey1 = Ps[:,0]
    predators1 = Ps[:,1]
    fig=plt.figure(1)
    plt.subplot(211)
    plt.plot(t, prey, "b+", label="rabbits")
    plt.plot(t, predators, "gx", label="Foxes")
    plt.plot(t, prey1, "r-", label="rabbits_t")
    plt.plot(t, predators1, "m--", label="foxes_t")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population against Time(Year)")
    plt.legend();
    plt.subplot(212)
    plt.plot(prey, predators, "-")
    plt.plot(prey1, predators1, "rx")
    plt.xlabel("Rabbits")
    plt.ylabel("Foxes")
    plt.title("Predators against Prey");
    fig = plt.gcf()
    fig.set_size_inches(15,15)
    plt.show();
    
    
    