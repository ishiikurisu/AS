from __future__ import print_function, division
import numpy as np
import matplotlib.pylab as plt

print('# Numbers')
print('division: 5/2={0}'.format(5/2))
print('type of 3j: {0}'.format(type(3j)))
print()
print('# Strings')
print('Concat: \'JOE\' + \'FRANK\' = {0}'.format('JOE' + 'FRANK'))
print('Don\'t scream: \'SCREAM\'.lower() = {0}'.format('SCREAM'.lower()))
print('\'joe frank\'[-2] = {0}'.format('joe frank'[-2]))
print()
print('# Lists')
a = []
a.append(1)
print('type of list: type([]) = {0}'.format(type([])))
print('\'joe frank\'[2:-2] = {0}'.format('joe frank'[2:-2]))
print('\'joe frank\'[-3:] = {0}'.format('joe frank'[-3:]))
print('Appending: [].append(1) = {0}'.format(a))
print()
print('# Maps')
b = {}
b['nome'] = 'joe'
b['idade'] = 22
print('b:', b)
print('b[nome] = {0}'.format(b['nome']))
# This will raise an error
# print('b[emprego] = {0}'.format(b['emprego']))
del b['nome']
print('b:', b)
print()
print('# Functions')
def multi(a, b):
    return a*b
def multpot(a, b, e=1):
    return (a*b)**e
print('multi(2,3) = {0}'.format(multi(2, 3)))
print('multpot(2,3) = {0}'.format(multpot(2, 3)))
print('multpot(2,3,4) = {0}'.format(multpot(2, 3, 4)))
print()
print('# Imports')
import math
print('math.sin(math.e) = {0}'.format(math.sin(math.e)))
print()
print('# Control flow')
for x in xrange(10):
    print(x, 'inside loop')
print('outside loop')
print()
print('# Numpy')
x = np.linspace(start = 0, stop = 100, num = 1E6, dtype = np.float64)
y = x ** 2
print('sum y = {0}'.format(sum(y)))
print('x = {0}'.format(x))
x = np.random.random(100)
print('random: {0}'.format(x))
fx = np.fft.fft(x)
fxi = np.fft.ifft(fx)
print('x == fx? {0}'.format(fxi == fx))
print()
print('# MATPLOTLIB')
plt.plot(np.sin(np.linspace(0, 2*np.pi, 2000)), color = 'green', label = 'some curve')
plt.legend()
plt.ylim(-2, 2)
plt.show()
