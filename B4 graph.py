import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import matplotlib


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
        y=ai[0]*cosh(x[z]*an/200)+ai[1]*sinh(an/200*x[z])+ai[2]*np.cos(an/200*x[z])+ai[3]*np.sin(an/200*x[z])
        if y>0:
            yy.append(y)
        else:
            yy.append(abs(y))
    return np.array(yy)




numberarray=['15','20','25','102','122','142','162','182','198','226']
xminplt=[10,75,220]  #zooming in on peak
xmaxplt=[25,110,285]
fig=plt.figure()
fig1=plt.figure()
if LaTeX_plot:
    matplotlib.use('Qt5Agg')
    import tikzplotlib
    from Tikzplotlib_fixer import tikzplotlib_fix_ncols
    fig1.supxlabel('Distance [\\si{\\micro\\meter}]', y=-0.05)
else:
    fig1.supxlabel('Distance [um]')
ax1=fig1.subplots(1,11)
fig2=plt.figure()
if LaTeX_plot:
    fig2.supxlabel('Distance [\\si{\\micro\\meter}]', y=-0.05)
else:
    fig1.supxlabel('Distance [um]')
ax2=fig2.subplots(1,11)
fig3=plt.figure()
if LaTeX_plot:
    fig1.supxlabel('Distance [\\si{\\micro\\meter}]', y=-0.05)
else:
    fig3.supxlabel('Distance [um]')
ax3=fig3.subplots(1,11)


ax=fig.add_subplot()
ax.set_xlim(0,500)

resmode=2
xmin=xminplt[resmode]  # isolating peak
xmax=xmaxplt[resmode]
xmean=[]
xstd=[]
for i in range(11):
    
    name='Data/Good Luck Luka 2/B4/long/b4.'+f'{i*20}'+'.csv'
    df=pd.read_csv(name,sep=',',skiprows=range(2),index_col=False,header=None,usecols=[0,2])
    #print(df)
    df=np.array(df,dtype=float)
    ax.plot(df[:,0]/1000,df[:,1],label=f' {i*20} um')
    x=0
    j=0
    yusefull=[]
    yllst=[]
    xllst=[]
    ylllst=[]
    xlllst=[]
    yllllst=[]
    xllllst=[]
    while j<=600:
        x=df[j,0]/1000
        #print(x)
        if x>xmin and x<xmax:
            yusefull.append(df[j,1])
            
        if x>xminplt[0] and x<xmaxplt[0]:
            xllst.append(x)
            yllst.append(df[j,1])
        if x>xminplt[1] and x<xmaxplt[1]:
            xlllst.append(x)
            ylllst.append(df[j,1])
        if x>xminplt[2] and x<xmaxplt[2]:
            xllllst.append(x)
            yllllst.append(df[j,1])
        

        
        j=j+1
    #print(yllst)
    ax1[i].plot(xllst,yllst)
    ax1[i].set_ylim(-90,-40)
    ax1[i].set_xlabel(f'{i*20}')
    ax1[i].xaxis.set_tick_params(labelbottom=False)
    if i!=0:
        ax1[i].yaxis.set_tick_params(labelleft=False)
    else:
        if LaTeX_plot:
            ax1[i].set_ylabel('Power [\\si{\\decibel\\meter}]')
        else:
            ax1[i].set_ylabel('Power [dBm]')
    ax2[i].plot(xlllst,ylllst)
    ax2[i].set_xlabel(f'{i*20}')
    ax2[i].set_ylim(-90,-40)
    ax2[i].xaxis.set_tick_params(labelbottom=False)
    if i!=0:
        ax2[i].yaxis.set_tick_params(labelleft=False)
    else:
        if LaTeX_plot:
            ax2[i].set_ylabel('Power [\\si{\\decibel\\meter}]')
        else:
            ax2[i].set_ylabel('Power [dBm]')
    ax3[i].plot(xllllst,yllllst)
    ax3[i].set_xlabel(f'{i*20}')
    ax3[i].set_ylim(-90,-40)
    
    ax3[i].xaxis.set_tick_params(labelbottom=False)
    if i!=0:
        ax3[i].yaxis.set_tick_params(labelleft=False)
    else:
        if LaTeX_plot:
            ax3[i].set_ylabel('Power [\\si{\\decibel\\meter}]')
        else:
            ax3[i].set_ylabel('Power [dBm]')
    xmean.append(np.mean(np.array(yusefull,dtype=float)))
    xstd.append(np.std(np.array(yusefull,dtype=float)))















freq=pd.read_csv('Resonance freq/freq.txt',sep=',',index_col=False,header=None,usecols=[1,2])
#print(freq)
freq=np.array(freq,dtype=float)
freql=freq[:,0]
freqs=freq[:,1]
for i in range(len(freql)):
    if freql[i]<500 and freql[i]>0:
        ax.vlines(freql[i],-90,-40,colors='blue',linestyles='dashed')

an=np.loadtxt(r'Resonance freq\an coeficient.txt',dtype=float)[:,1]*np.pi

ai=solve_ai(an[resmode])
#print(ai)
xxlst=np.linspace(0,200,200)
yyylst=modeshape(xxlst,ai,an[resmode])
yylst=yyylst*(-min(xmean)+max(xmean))/max(yyylst)+min(xmean)
#plt.figure()

#-75 -70
#1.5 -2



ax.legend()
if LaTeX_plot:
    ax.set_xlabel('Driven frequency [\\si{\\kilo\\hertz}]')
    ax.set_ylabel('Power [\\si{\\decibel\\meter}]')
    tikzplotlib_fix_ncols(ax.legend())
    tikzplotlib.save(f"LaTeX_plots/B4_1b_{resmode}.tex", figure=fig1, extra_tikzpicture_parameters = ['trim axis group left', 'trim axis group right'], extra_groupstyle_parameters={'horizontal sep=0.18cm}, unit vector ratio=0.07, {': '0.18cm'} )
    tikzplotlib.save(f"LaTeX_plots/B4_2b_{resmode}.tex", figure=fig2, extra_tikzpicture_parameters = ['trim axis group left', 'trim axis group right'], extra_groupstyle_parameters={'horizontal sep=0.18cm}, unit vector ratio=0.07, {': '0.18cm'} )
    tikzplotlib.save(f"LaTeX_plots/B4_3b_{resmode}.tex", figure=fig3, extra_tikzpicture_parameters = ['trim axis group left', 'trim axis group right'], extra_groupstyle_parameters={'horizontal sep=0.18cm}, unit vector ratio=0.07, {': '0.18cm'} )
    tikzplotlib.save(f"LaTeX_plots/B4_0b_{resmode}.tex", figure=fig, extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    ax.set_xlabel('Driven frequency (kHz)')
    ax.set_ylabel('Output of the photo diode (dBm)')
    plt.show()




fig=plt.figure()
ax1=fig.add_subplot()
xlst=np.arange(0,220,20)
eb=ax1.errorbar(xlst,xmean, yerr=xstd, color='red', capsize=5)
eb[-1][0].set_linestyle((0,(5,10)))
ax1.plot(xxlst,yylst,linestyle=':')
if resmode == 0:
    plt.title('1st resonance mode')
elif resmode == 1:
    plt.title('2nd resonance mode')
elif resmode == 2:
    plt.title('3rd resonance mode')
else:
    plt.title(f'{resmode+1}th resonance mode')
if LaTeX_plot:
    plt.xlabel('\\si{\\micro\\meter}')
    plt.ylabel('Power (averaged over frequency) [\\si{\\decibel}]')
    tikzplotlib_fix_ncols(ax1.legend())
    tikzplotlib.save(f"LaTeX_plots/B4_4b_{resmode}.tex", figure=fig, extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.xlabel('um')
    plt.ylabel('average dB')
    plt.show()






#ax.set_ylim(-12,12)

#plt.legend()



#plt.show()