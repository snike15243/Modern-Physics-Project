import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import tikzplotlib
from Tikzplotlib_fixer import tikzplotlib_fix_ncols

LaTeX_plot = False


fig=plt.figure()
ax=fig.add_subplot()
#ax.set_ylim(-12,12)

for i in range(5):
    name='Data/Good Luck Luka 2/B1/freq/b1.'+f'{15+i*5}'+'.3v.csv'
    df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    print(df)
    df=np.array(df,dtype=float)
    if LaTeX_plot:
        ax.plot(df[:,0]/1000,df[:,1],label=f'\\qty{{{15+i*5}}}{{\\kilo\\hertz}}')
    else:
        ax.plot(df[:,0]/1000,df[:,1],label=f'{15+i*5} kHz')
if LaTeX_plot:
    plt.xlabel('Driven frequency (\\si{\\kilo\\hertz})')
    plt.ylabel('Output of the photo diode (\\si{\\decibel\\meter})')
else:
    plt.xlabel('Driven frequency (kHz)')
    plt.ylabel('Output of the photo diode (dBm)')
#plt.title('Frequency spectrum for driven frequency')
plt.legend()


if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/B1_2_freq.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()