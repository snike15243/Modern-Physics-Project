import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.odr as odr
from scipy.optimize import curve_fit


#def ff(x,E):
#    L=200*10**(-6)
#    h=0.5*10**(-6)
#    rho=3440
#    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))



anlst=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)[:,1]*np.pi

short=np.array([50.7,296])*1000
long=np.array([14.4,86.3,241,459])*1000
an=anlst[0:4]
#print(an)
#val,cov=curve_fit(ff,an,long,p0=[200*10**9])
#print(cov)
#print(val)
#print(np.sqrt(np.diag(cov)))

#def ffshort(x,E):
#    rho=3440
#    L=100*10**(-6)
#    h=val[1]
#    return (x**2*h)/(4*np.pi*L**2)*np.sqrt(E/(3*rho))
#
#val2,cov2=curve_fit(ffshort,an[0:2],short,p0=[val[2]])
#fig=plt.figure()
#ax=fig.add_subplot()
#longlst=ff(anlst[0:4],val[0],val[1],val[2])
#shortlst=ffshort(anlst[0:2],val2[0])
#ax.plot(long,'.b')
#ax.plot(longlst,'-b')
#ax.plot(short,'.r')
#ax.plot(shortlst,'-r')
#print(val2)
#plt.show()


def fff(x,E):
    h=0.5*10**(-6)
    rho=3440
    #E=186*10**(9)
    return (x**2*h)/(4*np.pi)*np.sqrt(E/(3*rho))


Ls=100*10**(-6)
shortl=short*Ls**2

stdshort=np.array([10,13])*Ls**2*1000



Ll=200*10**(-6)
longl=long*Ll**2

stdlong=np.array([2,4,2,10])*Ll**2*1000




print(longl,shortl)

freql=np.append(longl,shortl)
anl=np.array([an[0],an[0],an[1],an[1]])    #np.append(an,anlst[0:2])
anl=np.append(anl,an[2:4])
freql=np.array([shortl[0],longl[0],shortl[1],longl[1]])
freql=np.append(freql,longl[2:4])
sy=np.array([stdshort[0],stdlong[0],stdshort[1],stdlong[1]])
sy=np.append(sy,stdlong[2:4])
print(anl)
print(freql)

val,cov=curve_fit(fff,anl,freql,p0=[200*10**(9)])
print(cov)
print(val)
print(f'Fit paramaters={val}+-{np.sqrt(np.diag(cov))}')
print('----------')
xlst=np.linspace(anl[0],11,1000)
#print(xlst)
ylst=fff(xlst,val[0])
fig=plt.figure()
ax=fig.add_subplot()
plt.xlabel('an')
plt.ylabel('fres/L**2')
ax.plot(xlst,ylst,':b')
ax.plot(anl,freql,'.r')



def f(B,x):
    h=0.5*10**(-6)
    rho=3440
    #E=186*10**(9)
    return (x**2*h)/(4*np.pi)*np.sqrt(B[0]/(3*rho))

#sx=[0.1]*6

fit=odr.Model(f)
mydata=odr.RealData(anl,freql,sy=sy)
myodr=odr.ODR(mydata,fit,beta0=[151*10**(9)])
myoutput=myodr.run()
myoutput.pprint()

yllst=f(myoutput.beta,xlst)
ax.plot(xlst,yllst,':g')

plt.show()






