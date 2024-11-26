import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import tikzplotlib
from Tikzplotlib_fixer import tikzplotlib_fix_ncols

LaTeX_plot = False

numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()
ax=fig.add_subplot()
#ax.set_ylim(-12,12)

for i in range(5):
    name='Data/Good Luck Luka 2/B1/Volts/b1.15.'+f'{i+3}'+'v.csv'
    df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    #print(df)
    df=np.array(df,dtype=float)
    ax.plot(df[:,0]/1000,df[:,1],label=f'{i+3} V')
if LaTeX_plot:
    plt.xlabel('Driven frequency (\\si{\\kilo\\hertz})')
    plt.ylabel('Photo diode output (\\si{\\decibel\\meter})')
else:
    plt.xlabel('Driven frequency (kHz)')
    plt.ylabel('Photo diode output (dBm)')
#plt.title('Frequency spectrum for driven voltage')
plt.legend()

#plt.legend()


if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/B1.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()


