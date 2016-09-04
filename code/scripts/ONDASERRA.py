from pylab import *
from numpy import pi, arange
a = arange (-2*pi, 2*pi, 0.01)
b = 2*sin(a)
for n in range (2,1002,1):
     b = b - 2.*((-1.)**n/n)*sin(n*a)

subplot (231)
plot (a,b, 'b-')
ylabel ('f(x)')
grid (False)
title ('(a)')

x = arange (-2*pi, 2*pi, 0.01)
y = -2*(-1)*sin(x)
for n in range (2,2,1):
     y = y - 2.*((-1.)**n/n)*sin(n*x)

subplot (232)
plot (a,b,'b-')
plot (x, y, 'r-')

title ('n=1 (b)')

x = arange (-2*pi, 2*pi, 0.01)
y = -2*(-1)*sin(x)
for n in range (2,6,1):
     y = y - 2.*((-1.)**n/n)*sin(n*x)

subplot (233)
plot (x, y, 'r-')
plot (a,b, 'b-')
title ('n=5 (c)')


x = arange (-2*pi, 2*pi, 0.01)
y = -2*(-1)*sin(x)
for n in range (2,32,1):
     y = y - 2.*((-1.)**n/n)*sin(n*x)


subplot (234)
plot (a,b, 'b-')
plot (x, y, 'r-')
title ('n=31 (d)')


ylabel ('f(x)')

x = arange (-2*pi, 2*pi, 0.01)
y = -2*(-1)*sin(x)
for n in range (2,62,1):
     y = y - 2.*((-1.)**n/n)*sin(n*x)

subplot (235)
plot (x, y, 'r-')
plot (a,b,'b-')
title ('n=61 (e)')

xlabel ('x')

x = arange (-2*pi, 2*pi, 0.01)
y = -2*(-1)*sin(x)
for n in range (2,1002,1):
     y = y - 2.*((-1.)**n/n)*sin(n*x)

subplot (236)
plot (x, y, 'r-')
plot (a,b, 'b-')
title ('n=1001 (f)')


show ()
