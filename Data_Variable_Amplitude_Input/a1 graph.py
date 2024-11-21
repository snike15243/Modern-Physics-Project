import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import tikzplotlib
matplotlib.use('Qt5Agg')
numberarray=['42','62','82','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
plt.xlabel('Time (s)')
#plt.title('Signal produced by the signal generator for different vpp')
plt.ylabel('Voltage (V)')

ax.set_ylim(-12,12)

for i in range(len(numberarray)):
    name='Data_Variable_Amplitude_Input/'+f'{numberarray[i]}'+'a.xls'
    name2='Data_Variable_Amplitude_Input/'+f'{numberarray[i]}'+'b.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df2=pd.read_csv(name2,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    df2=np.array(df2,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{float(numberarray[i])/10} V')
    
    if int(numberarray[i])/10 in [10.2,22.6]:
        fig2=plt.figure()
        ax2=fig2.add_subplot()
        plt.xlabel('Time (s)')
        #plt.title(f'Signal produced by the signal generator with vpp={int(numberarray[i])/10}')
        plt.ylabel('Voltage (V)')
        ax2.set_ylim(-12,12)
        ax2.plot(df[:,0],df[:,1],label='Input voltage')
        ax2.plot(df2[:,0],(df2[:,1]-np.mean(df2[:,1]))*30,label='Output of photo diode')
        
        fig2.legend()
ax.legend()
#plt.show()

tikzplotlib.save('vpp graph.tex')





