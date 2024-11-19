import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
ax.set_xlim(200,350)




freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]

for i in range(len(freql)):
    if freqs[i]<350 and freqs[i]>200:
        ax.vlines(freqs[i],-90,-40,colors='red',linestyles='dashed')







plt.legend()


#ax.set_ylim(-12,12)
xmin=290
xmax=310
xmean=[]
for i in range(11):
    name='Data/Good Luck Luka 2/B4/Short/b4.' f'{i*10}'+'.csv'
    df1=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    
    df1=np.array(df1,dtype=float)
    #print(df1)
    ax.plot(df1[:,0]/1000,df1[:,1],label='short'+f' {i*10}')

    x=0
    j=0
    yusefull=[]
    while x<=xmax:
        x=df1[j,0]/1000
        #print(x)
        if x>xmin and x<xmax:
            yusefull.append(df1[j,1])
            
        j=j+1
    xmean.append(np.mean(np.array(yusefull,dtype=float)))



plt.legend()
fig=plt.figure()
ax1=fig.add_subplot()
xlst=np.arange(0,110,10)
ax1.plot(xlst,xmean,'-r')


plt.show()