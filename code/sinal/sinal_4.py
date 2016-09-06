import numpy as np
import matplotlib.pyplot as plt


fs = 5.0 # Hz, taxa de amostragem (i.e. >= 2*f) 
t = np.linspace(-1,1,100) # redefine this here for convenience
ts = np.arange(-1,1+1/fs,1/fs) # pontos da amostras 
num_coeffs=len(ts) 
sm=0
for k in range(-num_coeffs,num_coeffs): # Ja que a funcao eh real, necessa ambos lados 
   sm+=np.sin(2*np.pi*(k/fs))*np.sinc( k - fs * t)
#close('all')
plt.plot( t,sm,'--',t,np.sin(2*np.pi*t),ts, np.sin(2*np.pi*ts),'o')
plt.title('taxa de amostragem=%3.2f Hz' % fs )
plt.show()
