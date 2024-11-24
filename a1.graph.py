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

for i in range(5):
    name='Data2.0/A1/A1_1_'+f'{i+1}'+'V.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{i+1}')

plt.legend()

if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/A1_1.tex")

fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(5):
    name='Data2.0/A1/A1_2_'+f'{i+1}'+'V.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    if i in [3,4]:
       ax.plot(df[:,0],(df[:,1]-np.mean(df[:,1]))*1000,label=f'{i+1}')


plt.legend()

if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/A1_2.tex")

fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)
for i in range(5):
    name='Data2.0/A1/A1_3_'+f'{i+1}'+'V.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    ax.plot(df[:,0],df[:,1],label=f'{i+1}')

plt.legend()

if LaTeX_plot:
    tikzplotlib_fix_ncols(plt.legend())
    tikzplotlib.save("LaTeX_plots/A1_3.tex")

if not LaTeX_plot:
    plt.show()
