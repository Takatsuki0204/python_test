#! /usr/bin/env python
# encoding: utf-8

import numpy.random as nprand
import matplotlib.pyplot as plt

R = nprand.randn(10000) # 標準正規分布で乱数を1万個生成
plt.hist(R, bins=100)   # 100本のヒストグラムを作成
plt.show()              # 表示