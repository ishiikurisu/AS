import numpy as np
import matplotlib.pyplot as plt

def ellapsedTime(n, v, z, h):
    return  2 * np.sqrt(z**2 + (n*h)**2) / v

if __name__ == '__main__':
    v = 1500.
    z = 150.
    h = 2.
    n = np.linspace(-80, 1000, 600)
    print(n)
    t = ellapsedTime(n, v, z, h)
    plt.plot(n, t)
    plt.show()
