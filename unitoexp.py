import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform

N = 100000
initial_distro = uniform(0,1,N)
lam =5
exp_distro = -(1/lam)*np.log(1 - initial_distro)
plt.subplot(2,1,1)
plt.hist(initial_distro,bins=50,edgecolor = 'black',density=True)
plt.grid()
plt.title(f'Uniform distribution with N = {N}')
plt.suptitle('Transformation of uniform distribution to exponential distribution')
plt.xlabel('u')
plt.ylabel(r'$P_{uniform}(u)$')
plt.subplot(2,1,2)
freq,bins,_=plt.hist(exp_distro,bins=50,edgecolor = 'black',density=True,label='uniform to exponential\ntransforation')
bin_mids = (bins[:-1] + bins[1:])/2
theory_plot = lam*np.exp(-lam*bin_mids)
plt.plot(bin_mids,theory_plot,'o-',label = 'Theoretical curve, '+r'$\lambda ='+str(lam)+'$')
plt.xlim(0,1)
plt.title('Exponential distribution')
plt.subplots_adjust(hspace=0.6)
plt.xlabel('x')
plt.ylabel(r'$P_{exp}(x)$')
plt.grid()
plt.legend()
plt.show()