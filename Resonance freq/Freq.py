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
    Fc=0.48
    I=1/12*w*h**3
    E=fE(L,Fc,I)
else:
    E=231*10**9


    
print(f'{E/10**9} [Gpa]')





#g=open('Resonance freq\an coeficient.txt')
dd=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)
freqs=ff(dd[:,1]*np.pi,L,h,E,rho)
freql=ff(dd[:,1]*np.pi,L*2,h,E,rho)
print(f'short cantilever (red) frequency={np.round(freqs/1000,1)} [kHz]')
print(f'long cantilever (blue) frequency={np.round(freql/1000,1)} [kHz]')

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)

ax1.set_xlim(0,450)
ax1.vlines(freqs[0:2]/1000,0,10,colors='red',linestyles='dashed')
ax1.vlines(freql[0:2]/1000,0,10,colors='blue',linestyles='dashed')

plt.show()