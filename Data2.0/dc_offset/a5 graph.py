import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(6):
    name='Data2.0/dc_offset/dc_1_'+f'{i}'+'.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{i}')

plt.legend()
plt.show()