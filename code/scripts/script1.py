#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,101)
f=np.ones_like(x)
f[x<0]=-1
y1=(4/np.pi)*(np.sin(x)+np.sin(3*x)/3.0)
y2=y1+(4/np.pi)*(np.sin(5*x)/5+np.sin(7*x)/7.0)
y3=y2+(4/np.pi)*(np.sin(9*x)/9+np.sin(11*x)/11.0)

plt.plot(x,f,'b-',lw=3,label='f(x)')
plt.plot(x,y1,'c--',lw=2,label='dois termos')   #rachurado, espessura da linha lw
plt.plot(x,y2,'r-',lw=2,label='quatro termos')
plt.plot(x,y3,'b:',lw=2,label='seis termos')
plt.legend(loc='best')
plt.xlabel('x',style='italic')
plt.ylabel('Soma parcias',style='italic')
plt.suptitle('Somas parcial para Serie de Fourier de f(x)', size=16, weight='bold')
#plt.savefig('teste.png')
plt.show()
