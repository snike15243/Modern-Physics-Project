import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names=['70','90','110','130','150','170','200','250','300','400','500','600','700','800','900','1000','1100','1200','1300','1400','1500']

#ax.set_ylim(-12,12)
fig=plt.figure()
ax=fig.add_subplot()
oi=1
for i in range(21):
    name='Data_variable_frequency_input/'+f'{names[i]}'+'a.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    print(df)
    df=np.array(df,dtype=float)
    if i>(21/6*oi):
        plt.legend()
        fig=plt.figure()
        ax=fig.add_subplot()
        oi=oi+1
    ax.plot(df[:,0],df[:,1],label=f'{names[i]}')

plt.legend()



plt.show()