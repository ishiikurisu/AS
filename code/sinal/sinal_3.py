import numpy as np
import matplotlib.pyplot as plt


f = 1.0  # Hz, sinal de frequencia
fs = 5.0 # Hz, taxa de amostragem (i.e. >= 2*f) 
t = np.arange(-1,1+1/fs,1/fs) # intervalo de amostragem, simetrico 
x = np.sin(2*np.pi*f*t)

interval=[] # dominio piecewise 
apprx = []  # dominio linear
# construir pontos * uniformemente * dentro de intervalos
tp = np.hstack([ np.linspace(t[i],t[i+1],20,False) for i in range(len(t)-1) ])
# construct arguments for piecewise2
for i in range(len(t)-1):
   interval.append( np.logical_and(t[i] <= tp,tp < t[i+1]))
   apprx.append( (x[i+1]-x[i])/(t[i+1]-t[i])*(tp[interval[-1]]-t[i]) + x[i])
x_hat = np.piecewise(tp,interval,apprx) # aproximacao piecewise linear 

ax1 = plt.figure().add_subplot(111)
ax1.fill_between(tp,x_hat,np.sin(2*np.pi*f*tp),facecolor='red')
ax1.set_xlabel('tempo',fontsize=18)
ax1.set_ylabel('Amplitude',fontsize=18)
ax2 = ax1.twinx()
sqe = ( x_hat - np.sin(2*np.pi*f*tp))**2
ax2.plot(tp, sqe,'r')
ax2.axis(xmin=-1,ymax= sqe.max() )
ax2.set_ylabel('error quadratico', color='r',fontsize=18)
ax1.set_title('Errors com a interpolacao linear Piecewise')
plt.show()

