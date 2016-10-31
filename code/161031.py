import numpy as np
import matplotlib.pyplot as mpl

def f(t):
    return np.cos(t) + np.cos(3.0*t)

if __name__ == '__main__':
    T = np.linspace(0, 5*(np.pi/3), 6)
    F = f(T)
    f_hat = lambda t: np.fft.fft(f(t))
    F_hat = f_hat(T) # F_hat = np.fft.fft(F)
    # mpl.plot(T, F)
    T_hat = np.arange(-2, 6*np.pi/3 - 2 , np.pi/3)
    mpl.plot(T_hat, F_hat)
    mpl.show()
