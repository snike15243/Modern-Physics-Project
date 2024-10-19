import numpy as np
import matplotlib.pyplot as plt

def fifthordernumderivative(x,i,dx):  #x is an array and i is the index of the derivative
    return 1/12*(f(x[i-2])-8*f(x[i-1])+8*f(x[i+1])-f(x[i+2]))/dx

def f(x):
    return np.sin(x)

def fp(x):
    return np.cos(x)

xlst=np.linspace(0,20,200)

xplst=fp(xlst)
xptlst=np.array([])
for i in range(200):
    print(i)
    #is only valid when ui-2 etc exist
    if i<2 or i>197:
        xptlst=np.append(xptlst,fp(xlst[i]))
    else:
        xptlst=np.append(xptlst,fifthordernumderivative(xlst,i,1/10))
err=xptlst-xplst
print(sum(err)/200)
plt.figure()
plt.plot(xlst,xplst,'-g')
plt.plot(xlst,xptlst,'-b')
plt.plot(xlst,err,'-r')
plt.show()

#print(xlst)
#print(xplst)
#print(xptlst)
