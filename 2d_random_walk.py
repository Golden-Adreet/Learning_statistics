import numpy as np
from random import choice
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def rand_dir():
    r = choice([(1,0),(0,1),(-1,0),(0,-1)])
    return r
def rand_dir_array(n,flg = False):
    res = []
    f = np.array([0,0])
    for i in range(n):
        a = rand_dir()
        f = f+a
        if not flg:
            res.append(f)
        else:
            res.append(f[0]**2 + f[1]**2)
    return np.array(res)
res = rand_dir_array(1000)
plt.figure(1)
plt.plot(res[:,0],res[:,1])
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot of displacement of a praticle performing random walk in 2D')
config,steps = 1000,1000
walks = np.array([rand_dir_array(steps,True) for i in range(config)])
def test1(x,a,b):
    return a*x**b
def test2(x,a,b):
    return a*x + b
rms = np.sqrt(np.mean(walks,axis = 0))
t = np.arange(1,config+1)
fit = curve_fit(test1,t,rms)[0]
rms_log = np.log(rms)
t_log = np.log(t)
fit_log = curve_fit(test2,t_log,rms_log)[0]
print(f'fitted equation:{round(fit[0],2)}*x^{round(fit[1],2)}')
print(f'fitted equation:{round(fit[0],2)} + x*{round(fit[1],2)}')
print(np.max(abs(t_log*0.5 - fit_log[0]*t_log - fit_log[1])))
plt.figure(2)
plt.subplot(2,1,1)
plt.plot(t[::50],rms[::50],'o',label = 'calculated value')
plt.plot(t,t**0.5,label = 'theoretical value')
plt.plot(t,fit[0]*t**fit[1],'--',label = 'fitted value')
plt.legend()
plt.grid()
plt.xlabel('T')
plt.ylabel(r'$r_{rms}$')
plt.suptitle(f'RMS value of the random walk of {config} particles over {steps} steps in 2D')
plt.subplot(2,1,2)
plt.plot(t,abs(rms-t**0.5),t,abs(t**0.5-fit[0]*t**fit[1]))
plt.legend(['calculated-theoretical','theoretical-fitted'])
plt.grid()
plt.xlabel('T')
plt.ylabel('Absolute error')
plt.subplots_adjust(hspace=0.3)
plt.figure(3)
plt.subplot(2,1,1)
plt.plot(t_log[::50],rms_log[::50],'o',label = 'calculated value')
plt.plot(t_log,t_log*0.5,label = 'theoretical value')
plt.plot(t_log,fit_log[0]*t_log + fit_log[1],'--',label = 'fitted value')
plt.legend()
plt.grid()
plt.xlabel(r'$\log_e(T)$')
plt.ylabel(r'$\log_e(r_{rms})$')
plt.suptitle(f'RMS value of the random walk of {config} particles over {steps} steps in 2D')
plt.subplot(2,1,2)
plt.plot(t_log,abs(rms_log-t_log*0.5),t_log,abs(t_log*0.5-fit_log[0]*t_log-fit_log[1]))
plt.legend(['calculated-theoretical','theoretical-fitted'])
plt.grid()
plt.xlabel(r'$\log_e(T)$')
plt.ylabel('Absolute error')
plt.subplots_adjust(hspace=0.3)
plt.show()