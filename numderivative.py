import numpy as np
import matplotlib.pyplot as plt

def fifthordernumderivative(x,i,dx):  #x is an array and i is the index of the derivative
    return 1/12*(f(x[i-2])-8*f(x[i-1])+8*f(x[i+1])-f(x[i+2]))/dx

def f(x):
    return np.sin(x)

def fp(x):
    return np.cos(x)


A=np.array([[1,1,1,1,1],
           [-2,-1,0,2,1],
           [4,1,0,1,4],
           [-8,-1,0,1,8],
           [16,1,0,1,16]])
b=np.array([0,1,0,0,0])

x=np.linalg.solve(A,b)

#for i in range(21+1):
#    print(i)
#    print(x*i)

#print(sum(x))
#for i in range(5):
#    print(np.transpose(A[i]))
#
#    print(np.matmul(A[i],np.transpose(x)))

print(x)
print(f'1/12*{x*21}')

xlst=np.linspace(0,20,200)

xplst=fp(xlst)
xptlst=np.array([])
for i in range(200):
    #print(i)
    #is only valid when ui-2 etc exist
    if i<2 or i>197:
        xptlst=np.append(xptlst,fp(xlst[i]))
    else:
        xptlst=np.append(xptlst,fifthordernumderivative(xlst,i,(xlst[1]-xlst[0])))
err=xptlst-xplst
print(f'error={abs(sum(err)/len(xlst))}')
plt.figure()
plt.plot(xlst,xplst,'-g')
plt.plot(xlst,xptlst,'-b')
plt.plot(xlst,err,'-r')
plt.show()

#print(xlst)
#print(xplst)
#print(xptlst)
