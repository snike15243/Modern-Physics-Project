import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()
xmaxplt=350
xminplt=200
ax=fig.add_subplot()
ax.set_xlim(xminplt,xmaxplt)




freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]

#ax.set_ylim(-12,12)
xmin=280
xmax=320
xmean=[]
for i in range(11):
    name='Data/Good Luck Luka 2/B4/Short/b4.' f'{i*10}'+'.csv'
    df1=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    
    df1=np.array(df1,dtype=float)
    #print(df1)
    ax.plot(df1[:,0]/1000,df1[:,1],label='short'+f' {i*10} um')

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

for i in range(len(freql)):
    if freqs[i]<xmaxplt and freqs[i]>xminplt:
        ax.vlines(freqs[i],-90,-40,colors='red',linestyles='dashed', label=f'fres {round(freqs[i],1)} kHz')


plt.legend()
plt.title('Frequency output for different positions on the short cantilever')
plt.xlabel('Driven frequency (kHz)')
plt.ylabel('Output of the photo diode (dBm)')
fig=plt.figure()
ax1=fig.add_subplot()
xlst=np.arange(0,110,10)
plt.title('1st resonance mode')
ax1.plot(xlst,xmean,'-r')
plt.xlabel('um')
plt.ylabel('average dB')


plt.show()