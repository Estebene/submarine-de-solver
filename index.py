import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def calculateTime(distance):
    time_interval = 0.001
    # initial condition
    v0 = 0

    # time points
    t = np.arange(0, 1.5, time_interval)

    # solve ODE
    v = odeint(model,v0,t)[:,0]

    total_distance = 0
    t_count = 0
    while total_distance < distance:
        total_distance += v[t_count] * time_interval
        t_count += 1
    total_time = t_count * time_interval
    
   # plot results
    plt.plot(t,v)

    # show integrated area
    t_section = t[:t_count]
    v_section = v[:t_count]
    plt.fill_between(t_section, v_section, alpha=0.2)
    

    plt.xlabel('time (s)')
    plt.ylabel('v(t)')
    plt.show()   
    return total_time


# function that returns dy/dt
def model(v,t):
    p = 997
    g = 9.81
    v_f = 0.000164
    m = 0.09
    d = np.array([1.17, 1.15])
    a = np.array([0.00525, 0.00045])
    drag_area_total = np.sum(d*a)

    dvdt = (p*g*v_f)/m - (drag_area_total*p*(v**2))/(2*m) - g
    return dvdt

for i in np.arange(0.25, 0.50, 0.05):
    total_time = calculateTime(i)
    print(f"{i:.2f}cm: {total_time:.2f} seconds")