#IIR filter

from scipy import fftpack
from scipy import signal
import scipy.io.wavfile
from scipy import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

b, a = signal.butter(2, 14/365.0, btype='high')


df = pd.read_csv('temperature_outdoor_2014.tsv', delimiter="\t", names=["time", "temperature"])
df.time = pd.to_datetime(df.time.values, unit="s").tz_localize('UTC').tz_convert('Europe/Stockholm')
df = df.set_index("time")
df = df.resample("1H")
df = df[(df.index < "2014-06-01")]
df = df.fillna(method='ffill')
time = df.index.astype('int')/1e9
temperature = df.temperature.values

temperature_filtered_iir = signal.lfilter(b, a, temperature)
temperature_filtered_filtfilt = signal.filtfilt(b, a, temperature)
f, h = signal.freqz(b)

fig, ax = plt.subplots(1, 1, figsize=(8, 3))
h_ampl = 20 * np.log10(abs(h))
h_phase = np.unwrap(np.angle(h))
ax.plot(f/max(f)/100, h_ampl, 'b')
ax.set_ylabel('frequency response (dB)', color="b")
ax.set_xlabel(r'normalized frequency')
ax = ax.twinx()
ax.plot(f/max(f)/100, h_phase, 'r')
ax.set_ylabel('phase response', color="r")
fig.tight_layout()
plt.show()
