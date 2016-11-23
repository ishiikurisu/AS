#signal FIR filter
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

plt.plot(b)
plt.show()




