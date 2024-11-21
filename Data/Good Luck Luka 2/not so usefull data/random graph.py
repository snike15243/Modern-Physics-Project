import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
#ax.set_ylim(-12,12)


name='Data/Good Luck Luka 2/not so usefull data/zero measurment freq.csv'
df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
#print(df)
df=np.array(df,dtype=float)
ax.plot(df[:,0]/1000,df[:,1],'-b',label='zero measurment')







plt.show()