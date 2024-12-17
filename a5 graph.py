import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib


LaTeX_plot = False

fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(-12,12)

for i in range(6):
    name='Data2.0/dc_offset/dc_1_'+f'{i}'+'.xls'
    


    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    avg=np.mean(df[:,1])
    if i==0 or i==3:
        fig1=plt.figure()
        ax1=fig1.add_subplot()
        ax1.set_ylim(-6,6)
        name1='Data2.0/dc_offset/dc_2_'+f'{i}'+'.xls'
        df1=pd.read_csv(name1,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
        df1=np.array(df1,dtype=float)
        ax1.plot(df[:,0],df[:,1]) #label=f'{round(avg,1)} V')
        ax1.plot(df1[:,0],(df1[:,1]-np.mean(df1[:,1]))*300) #label=f'{round(avg,1)} V')
        plt.title(f'{round(avg,1)} V')
    
    ax.plot(df[:,0],df[:,1],label=f'{round(avg,1)} V')
    
if LaTeX_plot:
    matplotlib.use('Qt5Agg')
    import tikzplotlib
    from Tikzplotlib_fixer import tikzplotlib_fix_ncols
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