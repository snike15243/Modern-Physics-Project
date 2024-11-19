import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(5):
    name='Data2.0/A1/A1_1_'+f'{i+1}'+'V.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{i+1}')

plt.legend()


fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(5):
    name='Data2.0/A1/A1_3_'+f'{i+1}'+'V.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{i+1}')

plt.legend()


plt.show()
