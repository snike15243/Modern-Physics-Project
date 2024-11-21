import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def ff(x,L,h,E):
    rho=3440
    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))



anlst=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)[:,1]*np.pi

short=np.array([50.7,296])*1000
long=np.array([14.4,86.3,241,459])*1000
an=anlst[0:4]
print(an)
val, cov=curve_fit(ff,an,long,p0=[200*10**(-6),0.5*10**(-6),200*10**9])
print(val)
def ffshort(x,E):
    rho=3440
    L=100*10**(-6)
    h=val[1]
    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))

val2,cov2=curve_fit(ffshort,an[0:2],short,p0=[val[2]])
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(anlst[0:4],long)
ax.plot(anlst[0:2],short)
print(val2)
plt.show()



