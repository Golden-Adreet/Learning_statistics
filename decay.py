import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random

T_half = 10
lam = np.log(2)/T_half
dt = 1
T= np.arange(0,50,1)
P = lam*dt
Q = 1- P
N = 100000
def decay(N):
    survive = [N,]
    n = N
    for _ in range(len(T)-1):
        prob = random(n)
        sur = np.sum(prob<Q)
        survive.append(sur)
        n = sur
    return survive

mean_decay = np.mean(np.array([decay(N) for _ in range(1000)]), axis = 0)
plt.semilogy()
plt.plot(T,mean_decay,label = 'Value obtained using\nMonte Carlo method')
plt.plot(T,N*np.exp(-lam*T),label = 'Theoretical value')
plt.title(f'Simulation of Nuclear decay with initial N= {N}')
plt.legend()
plt.grid()
plt.xlabel('T')
plt.ylabel('N')
plt.show()