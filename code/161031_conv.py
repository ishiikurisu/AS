import numpy as np
import matplotlib.pyplot as mpl

def f(t):
   a = np.array([0, 1, 2, 3, 0, 0, 0])
   return a[t]

def d(t):
    return 1 if np.abs(t) < 0.1 else 0

if __name__ == '__main__':
    # math
    T = np.linspace(0, 6, 7)
    X = np.linspace(-2, 5, 7)
    F = f(T)
    D = d(X)
    DF = np.convolve(F, D)

    # plotting
    mpl.plot(DF)
    mpl.show()
    
