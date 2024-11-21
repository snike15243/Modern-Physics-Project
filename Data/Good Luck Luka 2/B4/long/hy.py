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

Lopt=np.linspace(180,200,400)
hopt=np.linspace(0.4,0.6,400)*10**(-6)



