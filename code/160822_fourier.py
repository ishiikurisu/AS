#!/usr/bin/python
import numpy as np
import matplotlib.pylab as mpl

print('# Aula de Série de Fourier')
x = np.linspace(-np.pi, np.pi, 100001)
f = np.ones_like(x)
f[x<0] = -1 # para cada valor de x que for menor 0, o
            # item de índice correspondente em f será -1
y1 = (4/np.pi)*(np.sin(x) + np.sin(3*x)/3)
y2 = y1 + (4/np.pi)*(np.sin(5*x)/5 + np.sin(7*x)/7)
y3 = y2 + (4/np.pi)*(np.sin(9*x)/9 + np.sin(11*x)/11)

mpl.plot(x, f, 'c', lw=3, label='obj')
mpl.plot(x, y1, 'b-', lw=2, label='2 termos')
mpl.plot(x, y2, 'r--', label='4 termos')
mpl.plot(x, y3, 'y:', label='6 termos')
mpl.xlabel('x', style='italic')
mpl.ylabel('Somas parciais', style='italic')
mpl.suptitle('Somas parciais da série de Fourier', size=16, weight='bold')
mpl.legend(loc='best')
mpl.savefig('teste.png')
mpl.show()

# Notas:
# - O matplotlib não tem suporte a caracteres Unicode
