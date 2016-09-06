import numpy as np
import matplotlib.pyplot as plt
f = 1.0  # Hz, sinal de frequencia
fs = 5.0 # Hz, taxa de amostragem (i.e. >= 2*f) 
t = np.linspace(-1,1,100) # redefine this here for convenience
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
sqe = ( x_hat - np.sin(2*np.pi*f*tp))**2


ts = np.arange(-1,1+1/fs,1/fs) # pontos da amostras 
num_coeffs=len(ts) 
sm=0
for k in range(-num_coeffs,num_coeffs): # Ja que a funcao eh real, necessa ambos lados 
   sm+=np.sin(2*np.pi*(k/fs))*np.sinc( k - fs * t)


ax1 = plt.figure().add_subplot(111)
ax1.fill_between(t,sm,np.sin(2*np.pi*f*t),facecolor='red')
ax1.set_ylabel('Amplitude',fontsize=18)
ax2 = ax1.twinx()
sqe = (sm - np.sin(2*np.pi*f*t))**2
ax2.plot(t, sqe,'r')
ax2.axis(xmin=0,ymax = sqe.max())
ax2.set_ylabel('squared error', color='r',fontsize=18)
ax1.set_title('Errors with sinc Interpolant')
plt.show()

