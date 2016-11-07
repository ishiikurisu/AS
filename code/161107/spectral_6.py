from scipy import fftpack
from scipy import signal
import scipy.io.wavfile
from scipy import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('temperature_outdoor_2014.tsv', delimiter="\t",
names=["time", "temperature"])
df.time = (pd.to_datetime(df.time.values, unit="s").
tz_localize('UTC').tz_convert('Europe/Stockholm'))
df = df.set_index("time")
df = df.resample("H")
df = df[df.index < "2014-08-01"]
df = df.fillna(method='ffill')

time = df.index.astype('int64')/1.0e9
temperature = df.temperature.values

window = signal.blackman(len(temperature))

temperature_windowed = temperature * window

data_fft = fftpack.fft(temperature_windowed)
f = fftpack.fftfreq(len(temperature), time[1]-time[0])

mask = f > 0
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0.000001, 0.00004)
ax.axvline(1./86400, color='r', lw=0.5)
ax.axvline(2./86400, color='r', lw=0.5)
ax.axvline(3./86400, color='r', lw=0.5)
#ax.plot(f[mask], np.log(abs(data_fft_window[mask])), lw=2)
ax.plot(f[mask], np.log(abs(data_fft[mask])), lw=2)
ax.set_ylabel("$\log|F|$", fontsize=14)
ax.set_xlabel("frequency (Hz)", fontsize=14)

plt.show()
