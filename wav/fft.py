#! /usr/bin/python
# encoding: utf-8
import wave
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

N = 16
t = np.arange(N)
x = sp.sin(2 * sp.pi / N * t)
X = sp.fft(x)

print x
plt.plot(np.abs(x), "bo-")
plt.plot(np.real(x), "go-")
plt.plot(np.imag(x), "ro-")
plt.show()