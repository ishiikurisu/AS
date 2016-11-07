from scipy import fftpack
from scipy import signal
import scipy.io.wavfile
from scipy import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#metodo fillna scipy para eliminar qualquer valor NaN

df = pd.read_csv('temperature_outdoor_2014.tsv', delimiter="\t",
names=["time", "temperature"])
df.time = (pd.to_datetime(df.time.values, unit="s").
tz_localize('UTC').tz_convert('Europe/Stockholm'))
df = df.set_index("time")
df = df.resample("H")
df = df[df.index < "2014-08-01"]
df = df.fillna(method='ffill')

#usar o modulo fftpack e filtro blackman

time = df.index.astype('int64')/1.0e9
temperature = df.temperature.values

window = signal.blackman(len(temperature))


#multiplicando com a janela
temperature_windowed = temperature * window
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(df.index, temperature, label="original")
ax.plot(df.index, temperature_windowed, label="janelado")
ax.set_ylabel("temperatura", fontsize=14)
ax.legend(loc=0)

plt.show()
