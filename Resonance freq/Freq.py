import numpy as np
import matplotlib.pyplot as plt

def fE(L,Fc,I):
    return L**3*Fc/(3*I)  #Fc*L**3/(1/12*w*h**3)

def ff(x,L,h,E,rho):
    
    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))

Fccond=0

w=40*10**(-6)
L=100*10**(-6)
h=0.5*10**(-6)
rho=3440

if Fccond==1:
    #h=0.8*10**(-6)
    Fc=0.06
    I=1/12*w*h**3
    E=fE(L,Fc,I)
else:
    E=200*10**9


    
print(f'{E/10**9} [Gpa]')





#g=open('Resonance freq\an coeficient.txt')
dd=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)

print(f'frequency={np.round(ff(dd[:,1],L,h,E,rho)/1000,1)} [kHz]')