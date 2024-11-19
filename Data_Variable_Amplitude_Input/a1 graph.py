import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
numberarray=['42','62','82','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(len(numberarray)):
    name='Data_Variable_Amplitude_Input/'+f'{numberarray[i]}'+'a.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{numberarray[i]}')

plt.legend()
plt.show()





