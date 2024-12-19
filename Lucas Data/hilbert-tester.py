import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
from scipy.signal import savgol_filter, find_peaks, hilbert
from numderivative import nthorderjthdegreenumderivative
stop = 3
num = 10000
# Define the function
def actual_displacement(t):
    return -4*np.cos(2*np.pi*t)

wavelength = 2.3

def ir_signal(displacement):
    IR_voltage_in = 1
    Reflectivity = 0.1
    Finesse = 4*Reflectivity/(1-Reflectivity)**2

    return IR_voltage_in * Finesse * (np.sin(displacement*np.pi/wavelength))**2 / (1 + Finesse * (np.sin(displacement*np.pi/wavelength))**2)

actualdisplacement = actual_displacement(np.linspace(0, stop, num))
IR_signal = ir_signal(actualdisplacement)

def g(x):
    return (-0.5*np.cos(np.pi*x)+0.5+(1/3)*np.cos(3*np.pi*x) -0.2 * np.cos(4*np.pi*x))/1.30008

# functionathand = lambda x: g(x)
functionathand = lambda t: ir_signal(actual_displacement(t))
gmax = np.max([functionathand(x) for x in np.linspace(0, stop, num)])

def p(x):
    gval = functionathand(x)/gmax
    gprimeval = (functionathand(x+0.0001) - functionathand(x))/0.0001
    if True: # gprimeval > 0:
        return np.arcsin(2*gval-1)/(2*np.pi)
    else:
        return 0.5 - np.arcsin(2*gval-1)/(2*np.pi)


#gvals = np.array([g(x) for x in np.linspace(0, stop, num)])
pvals = np.array([p(x) for x in np.linspace(0, stop, num)])
def m(x):
    return np.trapz(np.abs(np.gradient(pvals, np.linspace(0, stop, num)))[0:int(x*num/stop)], np.linspace(0, stop, num)[0:int(x*num/stop)])

mvals = np.array([m(x)*wavelength for x in np.linspace(0, stop, num)])
absolute_displacement = [np.trapz(np.abs(np.gradient(actualdisplacement, np.linspace(0, stop, num)))[0:int(x*num/stop)], np.linspace(0, stop, num)[0:int(x*num/stop)]) for x in np.linspace(0, stop, num)]
hilbert_data = np.angle(hilbert(2*IR_signal/gmax - 1))
hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)
absgrad = np.abs(np.gradient(hilbert_data2, np.linspace(0, stop, num)))
# for i, j in enumerate(np.where(absgrad >  50)):
#     absgrad[j] = np.min([absgrad[j-5], absgrad[j+5]])
phase_over_time = [np.trapz(absgrad[0:int(x*num/stop)], np.linspace(0, stop, num)[0:int(x*num/stop)]) for x in np.linspace(0, stop, num)]
absolute_hilbert_displacement = phase_over_time*((wavelength/(2*np.pi))*np.ones(np.shape(phase_over_time)))

fig, ax = plt.subplots(1,1, figsize=(6,6))
ax.plot(np.linspace(0, stop, num), mvals)
ax.plot(np.linspace(0,stop,num), pvals)
#ax.plot(np.linspace(0,stop,num), gvals)
ax.plot(np.linspace(0, stop, num), actualdisplacement)
ax.plot(np.linspace(0, stop, num), IR_signal/np.max(IR_signal))
ax.plot(np.linspace(0, stop, num), absolute_displacement)
ax.plot(np.linspace(0, stop, num), absolute_hilbert_displacement)
plt.show()
