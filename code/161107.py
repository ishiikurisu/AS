# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

def ex1():
    # Defining function on time domain
    dt = 0.01
    fs = 20 * 2 * np.pi
    t = np.arange(-np.pi, np.pi, dt)
    f = np.cos(fs*t)
    
    # Defining function on frequency domain
    f_hat = np.fft.fft(f)
    w = np.fft.fftfreq(len(t), dt)
    
    # Plotting stuff
    mpl.plot(w, f_hat)
    mpl.show()

def ex2():
    delta = np.zeros(630)
    delta[400] = 200
    fs = 100
    t = np.linspace(-np.pi, np.pi, 630)
    f = np.cos(fs*t)
    f3 = f + delta
    # w = XXX
    F3 = np.fft.fftshift(np.fft.fft(f3))
    
    mpl.plot(t, F3)
    mpl.show()
    
if __name__ == '__main__':
    ex1()
    ex2()