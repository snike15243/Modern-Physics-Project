import numpy as np
import matplotlib.pyplot as plt
import random
def fE(L,Fc,I):
    return L**3*Fc/(3*I)  #Fc*L**3/(1/12*w*h**3)


# noinspection PyShadowingNames,PyPep8Naming
def ff(x,L,h,E,rho):
    
    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))

def normal(x,mean,std):
    return 1/(std*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*std**2))

def ex(x,a,b):
    return b*np.exp(-a*x)

def noismij(A,sigmagaus,n,xlst):
    n=random.randint(n-6,n+9)
    Alst=[]
    xmlst=[]
    sigmalst=[]
    nn=0

    for i in range(n):
        m=random.randint(-1,1)
        if m!=0:
            An=random.uniform(A*0.88,A*1.12)
            Alst.append(An*m)
            if i<8:
                xm=random.uniform(sigmagaus,100-sigmagaus)
                xmlst.append(xm)
            else:
                xm=random.uniform(sigmagaus*2,450-sigmagaus*2)
                xmlst.append(xm)
            sigma=random.uniform(sigmagaus*0.6,sigmagaus*2)
            sigmalst.append(sigma)
            nn=nn+1
    noiselst=[]
    for i in range(len(xlst)):
        noise=0
        for j in range(nn):
            if abs(xlst[i]-xmlst[j])<sigmalst[j]*4: 
                noise=noise+Alst[j]*normal(xlst[i],xmlst[j],sigmalst[j])
        noiselst.append(noise)


    return noiselst

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
    E=170*10**9


    
print(f'{E/10**9} [Gpa]')





#g=open('Resonance freq\an coeficient.txt')
dd=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)
freqs=ff(dd[:,1]*np.pi,109*10**(-6),h,E,rho)
freql=ff(dd[:,1]*np.pi,205*10**(-6),h,E,rho)

f=open(r'Resonance freq\freq.txt','w')
for i in range(len(freql)):
    f.writelines(f'{i+1},'+f'{freql[i]/1000},'+f'{freqs[i]/1000},')
    f.write('\n')

print(f'short cantilever (red) frequency={np.round(freqs/1000,1)} [kHz]')
print(f'long cantilever (blue) frequency={np.round(freql/1000,1)} [kHz]')

res=10

xlst=np.linspace(0,450,450*res)
noise=np.random.normal(0,0.012,res*450)
noisem=noismij(1,10,35,xlst)
ylsts=ex(xlst,0.01,0.4)+noise+noisem
noise=np.random.normal(0,0.012,res*450)
noisem=noismij(1,10,35,xlst)
ylstl=ex(xlst,0.01,0.4)+noise+noisem
sigma=6


for i in range(res*450):
    f=xlst[i]
    #print(f)
    for j in range(3):
        resfreq=freql[j]/1000
        
        if abs(resfreq-f)<=sigma*3:
            if j==0:
                ylstl[i]=ylstl[i]+random.uniform(3,5)*normal(f,resfreq,sigma)
            else:
                ylstl[i]=ylstl[i]+random.uniform(3,5)*normal(f,resfreq,sigma)
            #print(f-resfreq)
            #print(resfreq)
            #print(5*normal((f-freql[j]/1000),freql[j]/1000,sigma))
            #plt.pause(0.1)
            #print('poep')
            #print(norm(f-freql[j],freql[j],sigma))
        resfreq=freqs[j]/1000
        if j<2:
            if abs(resfreq-f)<=sigma*3:
                if j==0:
                    ylsts[i]=ylsts[i]+2*normal(f,resfreq,sigma/2)
                else:
                    ylsts[i]=ylsts[i]+5*normal(f,resfreq,sigma)







fig=plt.figure()
ax1=fig.add_subplot(1,2,1)

ax1.set_xlim(0,450)
ax1.plot(xlst,ylstl,'blue',linewidth=0.5)
ax1.plot(xlst,ylsts,'red',linewidth=0.5)
ax1.vlines(freqs[0:2]/1000,0,1.2,colors='red',linestyles='dashed',label='short')
ax1.vlines(freql[0:3]/1000,0,1.2,colors='blue',linestyles='dashed',label='long')
plt.legend()
plt.show()