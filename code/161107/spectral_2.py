from scipy import fftpack
from scipy import signal
import scipy.io.wavfile
from scipy import io
import numpy as np
import pandas as pd
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
f_t = 2 * np.sin(2 * 2 * np.pi * t) + 3 * np.sin(22 * 2 * np.pi * t) + 2* np.random.randn(*np.shape(t))

#F = fftpack.fft(f_t)
#F = np.fft.fft(f_t)
F = np.fft.fftpack.fft(f_t)

#Dw =2*np.pi/T
#f = np.arange(0, Dw*(N),Dw)
#f = fftpack.fftfreq(N, 1.0/f_s)
f = np.fft.fftfreq(N, 1.0/f_s)
mask = np.where(f >= 0)


fig, axes = plt.subplots(3, 1, figsize=(8, 6))
axes[0].plot(f[mask], np.log(abs(F[mask])), label="real")
axes[0].plot(B, 0, 'r*', markersize=10)
axes[0].set_ylabel("$\log(|F|)$", fontsize=14)
axes[1].plot(f[mask], abs(F[mask])/N, label="real")
axes[1].set_xlim(0, 5)
axes[1].set_ylabel("$|F|$", fontsize=14)
axes[2].plot(f[mask], abs(F[mask])/N, label="real")
axes[2].set_xlim(20, 24)
axes[2].set_xlabel("frequencia (Hz)", fontsize=14)
axes[2].set_ylabel("$|F|$", fontsize=14)


plt.show()


