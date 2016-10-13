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
f_t = 2 * np.sin(2 * np.pi * t) + 3 * np.sin(22 * 2 * np.pi * t) + 2* np.random.randn(*np.shape(t))

F = fftpack.fft(f_t)

f = fftpack.fftfreq(N, 1.0/f_s)

mask = np.where(f >= 0)

F_filtered = F * (abs(f) < 2)
f_t_filtered = fftpack.ifft(F_filtered)

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, f_t, label='original')
ax.plot(t, f_t_filtered.real, color="red", lw=3, label='filtrado')
ax.set_xlim(0, 10)
ax.set_xlabel("tempo (s)")
ax.set_ylabel("sinal")
ax.legend()


plt.show()


