import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig=plt.figure()
ax=fig.add_subplot()
#ax.set_ylim(-12,12)

for i in range(5):
    name='Data/Good Luck Luka 2/B1/freq/b1.'+f'{15+i*5}'+'.3v.csv'
    df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    print(df)
    df=np.array(df,dtype=float)
    ax.plot(df[:,0]/1000,df[:,1],label=f'{15+i*5} kHz')
plt.xlabel('Driven frequency (kHz)')
plt.ylabel('Output of the photo diode (dBm)')
#plt.title('Frequency spectrum for driven frequency')
plt.legend()



plt.show()