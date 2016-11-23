from scipy import fftpack
from scipy import signal
import scipy.io.wavfile
from scipy import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

n = 101
f_s = 1.0 /3600
nyq = f_s/2
b = signal.firwin(n, cutoff=nyq/12, nyq=nyq, window="hamming")


df = pd.read_csv('temperature_outdoor_2014.tsv', delimiter="\t", names=["time", "temperature"])
df.time = pd.to_datetime(df.time.values, unit="s").tz_localize('UTC').tz_convert('Europe/Stockholm')
df = df.set_index("time")
df = df.resample("1H")
df = df[(df.index < "2014-06-01")]
df = df.fillna(method='ffill')
time = df.index.astype('int')/1e9
temperature = df.temperature.values

temperature_filtered = signal.lfilter(b, 1, temperature)

temperature_median_filtered = signal.medfilt(temperature, 25)

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(df.index, temperature, label="original", alpha=0.5)
ax.plot(df.index, temperature_filtered, color="green", lw=2, label="FIR")
ax.plot(df.index, temperature_median_filtered, color="red", lw=2, label="median filer")
ax.set_ylabel("temperature", fontsize=14)
ax.legend(loc=0)
fig.tight_layout()

plt.show()

#fig.savefig("ch17-temperature-signal-fir.pdf")



