import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib


LaTeX_plot = False

names=['70','90','110','130','150','170','200','250','300','400','500','600','700','800','900','1000','1100','1200','1300','1400','1500']

#ax.set_ylim(-12,12)
figs = []
axs = []
ax1=[]
figs.append(plt.figure())
axs.append(figs[-1].add_subplot())
oi=1
for i in range(21):
    name='Data_variable_frequency_input/'+f'{names[i]}'+'a.xls'
    df=pd.read_csv(name,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    #print(df)
    name2='Data_variable_frequency_input/'+f'{names[i]}'+'b.xls'
    df2=pd.read_csv(name2,sep='\t',skiprows=range(9),index_col=False,header=None,usecols=[1,2])
    df=np.array(df,dtype=float)
    df2=np.array(df2,dtype=float)

    if i==0 or i==6:
        fig1=plt.figure()
        ax1.append(fig1.add_subplot())
        ax1[-1].set_ylim(-1.6,0.7)
        ax1[-1].plot(df[:,0],df[:,1])
        ax1[-1].plot(df2[:,0],(df2[:,1]-np.mean(df2[:,1]))*2.5)
        plt.title(f'{names[i]} Hz')

    if i>(21/6*oi):
        axs[-1].legend()
        if LaTeX_plot:
            matplotlib.use('Qt5Agg')
            import tikzplotlib
            from Tikzplotlib_fixer import tikzplotlib_fix_ncols
            axs[-1].set_xlabel('Time (\\si{\\second})')
            axs[-1].set_ylabel('Voltage (\\si{\\volt})')
        else:
            axs[-1].set_xlabel('Time (s)')
            axs[-1].set_ylabel('Voltage (V)')
        #plt.title('Signal produced by the signal generator')
        
        figs.append(plt.figure())
        axs.append(figs[-1].add_subplot())
        oi=oi+1
    if LaTeX_plot:
        axs[-1].plot(df[:,0],df[:,1],label=f'\\qty{{{names[i]}}}{{\\hertz}}')
    else:
        axs[-1].plot(df[:,0],df[:,1],label=f'{names[i]} Hz')
    #fig2=plt.figure()
    #ax2=fig2.add_subplot()
    #ax2.plot(df[:,0],df[:,1],label=f'{names[i]}')
    #ax2.plot(df2[:,0],df2[:,1],label=f'{names[i]} b')
    axs[-1].legend()

if LaTeX_plot:
    axs[-1].set_xlabel('Time (\\si{\\second})')
    axs[-1].set_ylabel('Voltage (\\si{\\volt})')
else:
    axs[-1].set_xlabel('Time (s)')
    axs[-1].set_ylabel('Voltage (V)')
#plt.title('Signal produced by the signal generator')
axs[-1].legend()


if LaTeX_plot:
    for i in range(len(figs)):
        tikzplotlib_fix_ncols(axs[i].legend())
        tikzplotlib.save(figure=figs[i], filepath=f"LaTeX_plots/A11_{i}.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()