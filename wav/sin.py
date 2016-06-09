#! /usr/bin/python
# encoding: utf-8

import wave
import struct
import numpy as np
from pylab import *

def createSinwave(A, f0, fs, len):
    """振幅A、基本周波数f0、サンプリング周波数fs、長さlen秒の正弦波を作成して返す"""
    data = []
    # [-1.0, 1.0]の少数値が入った波を作成
    for n in arange(len * fs):  # nはサンプルインデックス
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0: s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    plot(data[0:50]); show()
    # バイナリに変換
    #data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    #return data

if __name__ == "__main__":
    freqlist = [262, 294, 330, 349, 392, 440, 494, 523] # ドレミファソラシド
    for f in freqlist:
        data = createSinwave(1.0, f, 8000.0, 1.0)