import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,1e7,7,dtype=int)
def pi(N,flg = False):
    random_x = np.random.random(N)
    random_y = np.random.random(N)
    r = random_x**2 + random_y**2
    N_inside = np.sum(r<=1)
    approx_pi = 4*N_inside/N
    if flg:
        return N_inside,approx_pi
    else:
        return approx_pi
for N in n:
    res = pi(N,True)
    print(f'Total number of points = {N}\nTotal number of points inside the circle = {res[0]}\nValue of pi = {res[1]}\n','-'*10)
x = np.linspace(1,10000,10000,dtype=int)
plt.plot(x,list(map(pi,x)),label = r'approximated value of $\pi$')
plt.xlabel('Total number of points')
plt.hlines(y = np.pi,xmin=0,xmax=10000,colors='Black',label = r'theoretical value of $\pi$')
plt.ylabel(r'value of $\pi$')
plt.grid()
plt.legend()
plt.ylim(2,4)
plt.title(f'Calculating the value of $\pi$ using Monte Carlo method')
plt.show()