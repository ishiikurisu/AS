import numpy as np
import matplotlib.pyplot as mpl

x = [3, 4, 6, 1, 0, 8, 2, 3]
y = [1, 0, 3, 4, 5, 9, 2.8, 1]
n = [-2, -1, 0, 1, 2, 3, 4, 5]
m = [-4, -3, -2, -1, 0, 1, 2, 3]

if __name__ == '__main__':    
    t = range(1, len(x)+1, 1)
    result = np.convolve(x, y)
    new_t = []
    step = len(x) / (0.0+len(result))
    i = 1.0 - step
    while len(new_t) is not len(result):
        new_t.append(i)
        i += step
    mpl.plot(t, x, 'y')
    mpl.plot(t, y, 'b')
    mpl.plot(new_t, result, 'g')
    mpl.show()

    # Exercise: x(n)*y(m)
