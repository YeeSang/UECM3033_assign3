import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

if __name__ == "__main__":
        
    def ode(y,t,a,b):
        y0, y1 = y
        return [a*(y0 - y0*y1),b*(-y1 + y0*y1)]
        
    a = 1.0
    b = 0.2    
    initial_y = [0.1,1.0]
    t = np.linspace(0, 5, 200)
    
    sln = spIn.odeint(ode,initial_y,t,args=(a,b))
  
    plt.plot(t, sln[:, 0], 'b', label='y0(t)')
    plt.plot(t, sln[:, 1], 'g', label='y1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Graph of y(t) against t')
    plt.grid()
    plt.show()
    
    plt.plot(sln[:, 0],sln[:,1], 'r', label='y1 against y0')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.title('Graph of y1 against y0 with initial value y0=0.1 y1=1.0')
    plt.grid()
    plt.show()

    
    initial_y_new = [0.11, 1.0]
    sln = spIn.odeint(ode,initial_y_new,t,args=(a,b))
    
    plt.plot(sln[:, 0],sln[:,1], 'r', label='y1 against new y0')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.title('Graph of y1 against y0 with initial value y0=0.11 y1=1.0')
    plt.grid()
    plt.show()

