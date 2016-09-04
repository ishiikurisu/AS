#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

x=np.linspace(0,4,21)
y=np.exp(-x)
xe=0.08*npr.randn(len(x))
ye=0.1*npr.randn(len(y))

plt.errorbar(x,y,fmt='bo',lw=2,xerr=xe,yerr=ye,ecolor='r',elinewidth=1)
plt.show()
