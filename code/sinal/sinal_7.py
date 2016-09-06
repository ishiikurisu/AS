import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-1,1,100) # redefine por conviniencia
fs=5.0 # taxa de amostragem
k=np.array(sorted(set((t*fs).astype(int)))) # ordenando a lista de coeficientes 
fig=plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,(np.sin(2*np.pi*(k[:,None]/fs))*np.sinc(k[:,None]-fs*t)).T,'--', # funcao individual de whittaker 
        t,(np.sin(2*np.pi*(k[:,None]/fs))*np.sinc(k[:,None]-fs*t)).sum(axis=0),'k-', # funcao de interpolacao de whittaker 
     k/fs,np.sin(2*np.pi*k/fs),'ob')# amostras
ax.set_xlabel('tempo',fontsize=14)
ax.axis((-1.1,1.1,-1.1,1.1))
plt.show()
