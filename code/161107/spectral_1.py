#from scipy import fftpack
#from scipy import signal
#import scipy.io.wavfile
#from scipy import io
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# faixa de 30 hz, taxa de amostragem de 0.01 hz, periodo 100 hz

B = 30.0
f_s = 2 * B
delta_f = 0.01
N = int(f_s / delta_f)
T = N / f_s

t = np.linspace(0, T, N)
#funcao definida para o ruido
f_t = 2 * np.sin(2 * np.pi * t) + 3 * np.sin(22 * 2 * np.pi * t) + 2* np.random.randn(*np.shape(t))

fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
axes[0].plot(t, f_t)
axes[0].set_xlabel("tempo (s)")
axes[0].set_ylabel("sinal")
axes[1].plot(t, f_t)
axes[1].set_xlim(0, 5)
axes[1].set_xlabel("tempo (s)")

plt.show()
