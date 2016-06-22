# encoding: utf-8

import wave
import numpy as np
import matplotlib.pyplot as plt


def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print "チャンネル数:", wf.getnchannels()
    print "サンプリング幅:", wf.getsampwidth()
    print "サンプリング周波数:", wf.getframerate()
    print "フレーム数:", wf.getnframes()
    print "パラメータ:", wf.getparams()
    print "長さ(秒):", float(wf.getnframes()) / wf.getframerate()


def plot(wf):
    # wf = wave.open("C:\Users\TAKATSUKI\Downloads\se_amb01.wav", "r")
    buf = wf.readframes(wf.getnframes())
    print len(buf)
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    # plt.plot(data[0:500])
    plt.show()


def main():
    wf = wave.open("C:/Python27/test/se_amb01.wav", "r")
    printWaveInfo(wf)
    plot(wf)

if __name__ == "__main__":
    main()
