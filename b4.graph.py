import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import tikzplotlib
from Tikzplotlib_fixer import tikzplotlib_fix_ncols

LaTeX_plot = False

def cosh(x):
    return (np.e**x+np.e**(-x))/2

def sinh(x):
    return (np.e**x-np.e**(-x))/2

def solve_ai(an):
    A=np.array([[1,0,1,0],[0,1,0,1],[cosh(an),sinh(an),-np.cos(an),-np.sin(an)],[sinh(an),cosh(an),np.sin(an),-np.sin(an)]])
    A1=np.array([1])
    A=np.array([[0,1,0],[1,0,1],[sinh(an),-np.cos(an),-np.sin(an)]])
    b=[-A1[0],0,-cosh(an)*A1[0]]
    x=np.linalg.solve(A,b)
    #print(x)
    x=np.append(A1,x)
    #print(x)
    return x




def modeshape(x,ai,an):  #x in um
    yy=[]
    for z in range(len(x)):
        y=ai[0]*cosh(x[z]*an/100)+ai[1]*sinh(an/100*x[z])+ai[2]*np.cos(an/100*x[z])+ai[3]*np.sin(an/100*x[z])
        if y>0:
            yy.append(y)
        else:
            yy.append(abs(y))
    return np.array(yy)



numberarray=['15','20','25','102','122','142','162','182','198','226']
fig=plt.figure()

fig1=plt.figure()
ax1=fig1.subplots(1,11)
fig2=plt.figure()
ax2=fig2.subplots(1,11)
xminplt=[35,280]  #zooming in on peak
xmaxplt=[80,340]
ax=fig.add_subplot()
ax.set_xlim(0,500)




freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
#print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]

#ax.set_ylim(-12,12)
resmode=1
xmin=xminplt[resmode]  # isolating peak
xmax=xmaxplt[resmode]
xmean=[]
for i in range(11):
    name='Data/Good Luck Luka 2/B4/Short/b4.' f'{i*10}'+'.csv'
    df1=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    
    df1=np.array(df1,dtype=float)
    #print(df1)
    if LaTeX_plot:
        ax.plot(df1[:,0]/1000,df1[:,1],label=f' \\qty{{{i*10}}}{{\\micro\\meter}}')
    else:
        ax.plot(df1[:,0]/1000,df1[:,1],label=f' {i*10} um')

    x=0
    j=0
    yusefull=[]
    yllst=[]
    xllst=[]
    ylllst=[]
    xlllst=[]
    while j<601:
        x=df1[j,0]/1000
        #print(x)
        if x>xmin and x<xmax:
            yusefull.append(df1[j,1])
        
        if x>xminplt[0] and x<xmaxplt[0]:
            xllst.append(x)
            yllst.append(df1[j,1])
        if x>xminplt[1] and x<xmaxplt[1]:
            xlllst.append(x)
            ylllst.append(df1[j,1])
            
        j=j+1
    ax1[i].plot(xllst,yllst)
    ax1[i].set_ylim(-90,-40)
    ax1[i].set_xlabel(f'{i*10}')
    ax1[i].xaxis.set_tick_params(labelbottom=False)
    ax1[i].yaxis.set_tick_params(labelleft=False)
    ax2[i].plot(xlllst,ylllst)
    ax2[i].set_ylim(-90,-40)
    ax2[i].set_xlabel(f'{i*10}')
    ax2[i].xaxis.set_tick_params(labelbottom=False)
    ax2[i].yaxis.set_tick_params(labelleft=False)
    xmean.append(np.mean(np.array(yusefull,dtype=float)))

for i in range(len(freql)):
    if freqs[i]<500 and freqs[i]>0:
        ax.vlines(freqs[i],-90,-40,colors='red',linestyles='dashed')


an=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)[:,1]*np.pi

ai=solve_ai(an[resmode])
#print(ai)
xxlst=np.linspace(0,100,100)
yyylst=modeshape(xxlst,ai,an[resmode])
yylst=yyylst*(-min(xmean)+max(xmean))/max(yyylst)+min(xmean)


ax.legend()
#plt.title('Frequency output for different positions on the short cantilever')


if LaTeX_plot:
    ax.set_xlabel('Driven frequency (\\si{\\kilo\\hertz})')
    ax.set_ylabel('Output of the photo diode (\\si{\\decibel\\meter})')
    tikzplotlib_fix_ncols(ax.legend())
    tikzplotlib.save("LaTeX_plots/B4_1.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'], figure=fig)
    tikzplotlib.save("LaTeX_plots/B4_2.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'], figure=fig1, axis_width='10', axis_height='10')
    tikzplotlib.save("LaTeX_plots/B4_3.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'], figure=fig2, axis_width='10', axis_height='10')

else:
    ax.set_xlabel('Driven frequency (kHz)')
    ax.set_ylabel('Output of the photo diode (dBm)')
    plt.show()

fig=plt.figure()
ax1=fig.add_subplot()
xlst=np.arange(0,110,10)
plt.title('2nd resonance mode')
ax1.plot(xlst,xmean,'-r')
ax1.plot(xxlst,yylst,linestyle='-')
if LaTeX_plot:
    plt.xlabel('\\si{\\micro\\meter}')
    plt.ylabel('average \\si{\\decibel}')
else:
    plt.xlabel('um')
    plt.ylabel('average dB')

if LaTeX_plot:
    tikzplotlib.save("LaTeX_plots/B4_4.tex", extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'], figure=fig)
else:
    plt.show()