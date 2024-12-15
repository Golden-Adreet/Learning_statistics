import numpy as np
from scipy.integrate import quad,simps
from numpy.random import uniform

f = lambda x: np.sin(x)
a = 0
b = np.pi
N = 10000

xrand = uniform(a,b,N)
result = np.array([((b-a)/N)*np.sum(f(xrand)) for _ in range(100000)])
print(f'The result of integration sin(x) form 0 to pi (Monte Carlo): {np.mean(result)}')

result = quad(f,a,b)[0]
print(f'The result of integration sin(x) form 0 to pi (Quad): {result}')

x = np.linspace(a,b,1000)
result = simps(f(x),x)
print(f'The result of integration sin(x) form 0 to pi (Simpson): {result}')
