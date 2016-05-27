# encoding: utf-8

import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("C:\Users\TAKATSUKI\Downloads\se_amb01.wav", "r")
    print "Frame rate: ", wf.getframerate()    # サンプリング周波数
    print "Sample Width: ", wf.getsampwidth()  # サンプリング幅

def plot():
    wf = wave.open("C:\Users\TAKATSUKI\Downloads\se_amb01.wav", "r")
    buf = wf.readframes(wf.getnframes())
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    main()
    plot()