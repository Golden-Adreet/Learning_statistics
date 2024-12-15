import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt
initial_distro = uniform(0,1,6000)
def CLT(initial,sample_size):
    normal_sample = [np.mean(np.random.choice(initial,size=sample_size,replace=False)) for _ in range(10000)]
    return np.array(normal_sample)
var_i = np.var(initial_distro)
sample_size = [1,3,10,30,100,1000]
final_distro = [CLT(initial_distro,i) for i in sample_size]
fig = plt.figure(figsize=(12,10))
for i in range(6):
    ax = fig.add_subplot(3,2,i+1)
    ax.hist(final_distro[i],bins='auto',color = 'white',edgecolor = 'black',density=True)
    ax.set_title(f'sample size = {sample_size[i]}\n'+r'$\sigma_{T}^2 = '+str(round(var_i/sample_size[i],5))+',\sigma_{C}^2 ='+str(round(np.var(final_distro[i]),5))+'$')
    ax.grid()
plt.subplots_adjust(hspace=1)
plt.show()
