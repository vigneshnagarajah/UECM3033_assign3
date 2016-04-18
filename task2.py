import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def g(y,t):
    a=1.0
    b=0.2    
    d0=a*(y[0]-(y[0]*y[1]))
    d1=b*(-y[1]+(y[0]*y[1]))
    return [d0,d1]
    

#First integrate from 0 to 5
y_ic=np.array([0.1,1.0])
t=np.linspace(0,5,1000) #time range
sol=odeint(g,y_ic,t)
prey=sol[:,0]
pred=sol[:,1]


# plot results for vs. Time plot
plt.figure('Population vs. Time Plot')
plt.plot(t, prey, label='prey', color="blue", linestyle="-")
plt.plot(t, pred, label='predator', color="red", linestyle="-")
plt.grid()
plt.title('Population vs. Time Plot')
plt.ylabel('population')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
plt.show()

plt.figure('Predator vs Prey')
plt.plot(prey,pred)
plt.title('Predator-Prey')
plt.ylabel('predator')
plt.xlabel('prey')
plt.show()

#to observe sensitivity
#another case when y0=0.11
y_ic=np.array([0.11,1.0])
t=np.linspace(0,5,1000) 
sol=odeint(g,y_ic,t)
prey=sol[:,0]
pred=sol[:,1]


# plot results for vs. Time plot
plt.figure('Population vs. Time Plot')
plt.plot(t, prey, label='prey', color="blue", linestyle="-")
plt.plot(t, pred, label='predator', color="red", linestyle="-")
plt.grid()
plt.title('Population vs. Time Plot')
plt.ylabel('population')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
plt.show()

plt.figure('Predator vs Prey')
plt.plot(prey,pred)
plt.title('Predator-Prey')
plt.ylabel('predator')
plt.xlabel('prey')
plt.show()