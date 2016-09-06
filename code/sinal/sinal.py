import numpy as np
import matplotlib.pyplot as plt


fig,ax = plt.subplots()

f = 1.0  # Hz, sinal de frequencia
fs = 5.0 # Hz, taxa de amostragem (i.e. >= 2*f) 
t = np.arange(-1,1+1/fs,1/fs) # intervalo de amostragem, simetrico 
x = np.sin(2*np.pi*f*t)
ax.plot(t,x,'o-')
ax.set_xlabel('tempo',fontsize=18)
ax.set_ylabel('amplitude',fontsize=18)
plt.show()
