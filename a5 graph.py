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
ax.set_ylim(-12,12)

for i in range(6):
    name='Data2.0/dc_offset/dc_1_'+f'{i}'+'.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    avg=np.mean(df[:,1])
    ax.plot(df[:,0],df[:,1],label=f'{round(avg,1)} V')
if LaTeX_plot:
    plt.xlabel('Time (\\si{\\second})')
else:
    plt.xlabel('Time (s)')
if LaTeX_plot:
    plt.ylabel('Voltage (\\si{\\volt})')
else:
    plt.ylabel('Voltage (V)')
#plt.title('Signal generator output for different dc offsets')
plt.legend()

if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save(filepath="LaTeX_plots/A5.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()