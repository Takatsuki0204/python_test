#! /usr/bin/python
# encoding: utf-8

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json("http://192.168.10.121:3000/monitoring/122?date=20160523")

# print(data.head(10))    # 先頭10行を表示
# print(data.tail(20))    # 後尾20行を表示
# print(data["light"])    # 単独カラムのみ表示
# print(data[["temperature", "humidity"]])    # 複数カラムの表示
# print(data["temperature"].sum())    # 温度カラムの合計を表示(mean:平均, median:中央値)
# print(data.describe())  # 平均、分散など
# rint(data["temperature"].mean())   # 温度の平均
# print(data.ix[10:100, ["light", "temperature"]])     # ix:列名と列番号が使える。10行目から100行目までの照度、温度を表示
# print(data.query("light == 193 & humidity == 50"))    # 条件文(&：and, |:or)
# print(data.query("index in [10, 20]"))    # 特定の行の表示
# print(data.sort("humidity", ascending = False))   # 降順でソート
# print(data[["temperature", "humidity"]].sum(axis=0))    # axis=1:横方向に計算
# data.to_csv("log.csv")    # csv形式で保存

x = pd.to_datetime(data["updated"]) # + pd.offsets.Hour(9)
print(x)
# x = pd.Series(pd.to_datetime(data["updated"]).dt.tz_localize("UTC").dt.tz_convert("Asia/Tokyo"))
# print(x)
y = data["temperature"]
plt.plot(x, y)

plt.xlabel("Time")
plt.ylabel("Temp")

# plt.xlim([0, 24])
plt.ylim([0, 40])

plt.show()