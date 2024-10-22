import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1+1/2*(np.e**x+np.e**(-x))*np.cos(x)

def fp(x):
    return 1/2*(np.e**x-np.e**(-x))*np.cos(x)-1/2*(np.e**x+np.e**(-x))*np.sin(x)

def plotting(xn):
    ax.set_ylim(-300,450)
    plot1=ax.plot(xn,0,'.r')
    plt.pause(0.01)
    return plot1
xmax=50
iter=10000
xlst=np.linspace(0,xmax,iter)
ylst=f(xlst)

xnlst=np.array([2,6,8,12,16,17,20,25,28,30,33,35,38,40,42,45,49],float)
fig=plt.figure()
ax=fig.add_subplot()
ax.hlines(0,0,xmax,colors='black')
plot2=ax.plot(xlst,ylst,'-b')


xsol=np.array([],float)
for j in range(len(xnlst)):
    xn=xnlst[j]
    plot1=plotting(xnlst[j])
    #print(f'x={xnlst[j]}')
    for i in range(10):


        xn=-f(xn)/fp(xn)+xn
        #print(f'x={xn}')
        plot1=plotting(xn)
    if xn>=25:
        None
    else:
        xsol=np.append(xsol,xn)

ax.clear()
ax.set_ylim(-300,450)
ax.plot(xlst,ylst,'-b')
ax.hlines(0,0,xmax,colors='black')
ax.plot(xsol,[0]*(len(xsol)),'.r')
#ax.set_ylim(-300,450)
#for i in range(iter):
#    if np.abs(ylst[i])<=10**(-1):
#        xsol.append(xlst[i])
#        ax.plot(xlst[i],0,'.r')
print(f'solutions to f={xsol}')
delta=np.array([],float)
for i in range(len(xsol)-1):
    delta=np.append(delta,(xsol[i+1]-xsol[i]))
print(f'difference between i+1 and i={delta}')
print(f(xsol))
f=open('an coeficient.txt','w')
for i in range(len(xsol)):
    f.writelines(f'{i+1}\t'+str(xsol[i]))
    f.write('\n')

plt.show()




    
    
    









