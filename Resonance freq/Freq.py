import numpy as np
import matplotlib.pyplot as plt



def ff(x):
    w=40*10**(-6)
    L=200*10**(-6)
    h=0.8*10**(-6)
    Fc=0.0
    I=1/12*w*h**3
    E=L**3*Fc/(3*I)   #Fc*L**3/(1/12*w*h**3)
    rho=3440
    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))

g=open('an coeficient.txt')
xsol=g.read()

print(xsol)








print(f'frequency={ff(xsol)/1000} [kHz]')