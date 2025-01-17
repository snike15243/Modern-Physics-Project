import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')

LaTeX_plot = False

numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
#ax.set_ylim(-12,12)


name='Data/Good Luck Luka 2/B2/b2.500.csv'
df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
#print(df)
df=np.array(df,dtype=float)
if LaTeX_plot:
    matplotlib.use('Qt5Agg')
    import tikzplotlib
    from Tikzplotlib_fixer import tikzplotlib_fix_ncols
    ax.plot(df[:,0]/1000,df[:,1],'-b',label='long (\\qty{200}{\\micro\\meter})')
else:
    ax.plot(df[:,0]/1000,df[:,1],'-b',label='long (200 um)')

freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]

for i in range(len(freql)):
    if freql[i]<500:
        if i==0:
            ax.vlines(freql[i],-90,-40,colors='blue',linestyles='dashed',label=f'theoretical resonance freq for long cantiliver')
        else:
            ax.vlines(freql[i],-90,-40,colors='blue',linestyles='dashed')
    if freqs[i]<500:
        if i==0:
            ax.vlines(freqs[i],-90,-40,colors='red',linestyles='dashed',label=f'theoretical resonance freq for short cantiliver')
        else:
            ax.vlines(freqs[i],-90,-40,colors='red',linestyles='dashed')



name='Data/Good Luck Luka 2/not so usefull data/zero measurment freq.csv'
df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
#print(df)
df=np.array(df,dtype=float)
ax.plot(df[:,0]/1000,df[:,1],'-g',label='zero measurment')




plt.legend()


#ax.set_ylim(-12,12)


name='Data/Good Luck Luka 2/B2/b2.500.short.csv'
df1=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
#print(df1)
df1=np.array(df1,dtype=float)
if LaTeX_plot:
    ax.plot(df1[:,0]/1000,df1[:,1],'-r',label='short (\\qty{100}{\\micro\\meter})')
else:
    ax.plot(df1[:,0]/1000,df1[:,1],'-r',label='short (100 um)')
if LaTeX_plot:
    plt.xlabel('Driven frequency (\\si{\\kilo\\hertz})')
    plt.ylabel('Output of the photo diode (\\si{\\decibel\\meter})')
else:
    plt.xlabel('Driven frequency (kHz)')
    plt.ylabel('Output of the photo diode (dBm)')
#plt.title('Resonance frequencies')
plt.legend()


if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/B2.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()