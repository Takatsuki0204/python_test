#! /usr/bin/python
# encoding: utf-8

import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("C:\Users\TAKATSUKI\Documents\GitHub\python_test\FFT\se_amb01.wav", "r")
    buf = wf.readframes(wf.getnframes())
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    main()