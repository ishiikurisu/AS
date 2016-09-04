from pylab import *
from numpy import pi, arange

x = arange (-1*pi, 1*pi,0.01)
y = 4./pi *sin(pi*x)
for n in range (3,1003,2):
    y = y + 4./pi * 1/n * sin(n*pi*x)
    
subplot (231)
plot (x,y)
ylabel ('f(x)')
title ('(a)')
x = arange (-1*pi, 1*pi, 0.01)
a = 4./pi * sin(pi*x)
for n in range (3,3,2):
    a = a + 4./pi * 1/n * sin(n*pi*x)

subplot (232)
plot (x, y, 'b-')
plot (x,a, 'r-')
title ('n=1 (b)')

x = arange (-1*pi, 1*pi, 0.01)
b = 4./pi * sin(pi*x)
for n in range (3,7,2):
    b = b + 4./pi * 1/n * sin(n*pi*x)

subplot (233)
plot (x, y, 'b-')
plot (x,b, 'r-')
title ('n=5 (c)')

x = arange (-1*pi, 1*pi, 0.01)
c = 4./pi * sin(pi*x)
for n in range (3,33,2):
    c = c + 4./pi * 1/n * sin(n*pi*x)

subplot (234)
plot (x, y, 'b-')
plot (x,c, 'r-')
title ('n=31 (d)')


ylabel ('f(x)')

x = arange (-1*pi, 1*pi, 0.01)
d = 4./pi * sin(pi*x)
for n in range (3,63,2):
    d = d + 4./pi * 1/n * sin(n*pi*x)

subplot (235)
plot (x, y, 'b-')
plot (x,d, 'r-')
title ('n=61 (e)')

xlabel ('x')

x = arange (-1*pi, 1*pi, 0.01)
e = 4./pi * sin(pi*x)
for n in range (3,1003,2):
    e = e + 4./pi * 1/n * sin(n*pi*x)

subplot (236)
plot (x, y, 'b-')
plot (x,e, 'r-')
title ('n=1001 (f)')


show ()
