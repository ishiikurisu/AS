# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pylab as mpl

def fsin(x, f):
    return np.sin(x + f)

print '# Somando três senos'
x1 = float(raw_input('Valor inferior: '))
x2 = float(raw_input('Valor superior: '))
f = float(raw_input('Fase: '))

# Math stuff
x = np.linspace(x1, x2, 1001)
ys = []
for i in range(3):
    r = fsin(x*(i+1), f)
    ys.append(r)
y = sum(ys)

# Plotting stuff
for it in ys:
    mpl.plot(x, it)
mpl.xlabel('x', style='italic')
mpl.ylabel('Somas parciais')
mpl.plot(x, y)
mpl.show()
