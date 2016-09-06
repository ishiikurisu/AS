import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111) # criando eixo manualmente 
k=0
fs=2 # fazer esse grafico facil para ler
t = np.linspace(-1,1,100) # redefine por conviniencia
ax.plot (t,np.sinc( k - fs * t), 
         t,np.sinc( k+1 - fs * t),'--',k/fs,1,'o',(k)/fs,0,'o',
         t,np.sinc( k-1 - fs * t),'--',k/fs,1,'o',(-k)/fs,0,'o'
)
ax.hlines(0,-1,1)
ax.vlines(0,-.2,1)
ax.annotate('valor da amostra vai aqui',
            xy=(0,1),
            xytext=(-1+.1,1.1),
            arrowprops={'facecolor':'red','shrink':0.05},
            )
ax.annotate('nenhuma interferencia aqui',
            xy=(0,0),
            xytext=(-1+.1,0.5),
            arrowprops={'facecolor':'green','shrink':0.05},
            )
plt.show()
