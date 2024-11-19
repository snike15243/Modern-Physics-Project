import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

numberarray=['15','20','25','102','122','142','162','182','198','226']
xminplt=0   #zooming in on peak
xmaxplt=500
fig=plt.figure()
ax=fig.add_subplot()
ax.set_xlim(xminplt,xmaxplt)
plt.title('Frequency output for different positions on the long cantilever')
plt.xlabel('Driven frequency (kHz)')
plt.ylabel('Output of the photo diode (dBm)')

xmin=250  # isolating peak
xmax=280
xmean=[]
for i in range(11):
    name='Data/Good Luck Luka 2/B4/long/b4.'+f'{i*20}'+'.csv'
    df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    #print(df)
    df=np.array(df,dtype=float)
    ax.plot(df[:,0]/1000,df[:,1],label='long'+f' {i*20} um')
    x=0
    j=0
    yusefull=[]
    while x<=xmax:
        x=df[j,0]/1000
        #print(x)
        if x>xmin and x<xmax:
            yusefull.append(df[j,1])
            
        j=j+1
    xmean.append(np.mean(np.array(yusefull,dtype=float)))





freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]

for i in range(len(freql)):
    if freql[i]<xmaxplt and freql[i]>xminplt:
        ax.vlines(freql[i],-90,-40,colors='blue',linestyles='dashed',label=f'fres {round(freql[i],1)} kHz')

plt.legend()

fig=plt.figure()
ax1=fig.add_subplot()
xlst=np.arange(0,220,20)
ax1.plot(xlst,xmean,'-r')
plt.title('3th resonance mode')
plt.xlabel('um')
plt.ylabel('average dB')







#ax.set_ylim(-12,12)

plt.legend()



plt.show()