#! /usr/bin/python
# encoding: utf-8

import datetime, sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json("http://192.168.10.121:3000/monitoring/122?date=20160523")
#connector = sqlite3.connect("C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db")
#data = pd.read_sql("select * from test", con=connector)

print data.head(10)    # 先頭10行を表示
print data.tail(20)    # 後尾20行を表示
print data["light"]    # 単独カラムのみ表示
print data[["temperature", "humidity"]]    # 複数カラムの表示
print data["temperature"].sum()    # 温度カラムの合計を表示(mean:平均, median:中央値)
print data.describe()  # 平均、分散など
print data["temperature"].mean()   # 温度の平均
print data.ix[10:100, ["light", "temperature"]]     # ix:列名と列番号が使える。10行目から100行目までの照度、温度を表示
print data.query("light == 193 & humidity == 50")    # 条件文(&：and, |:or)
print data.query("index in [10, 20]")    # 特定の行の表示
print data[["temperature", "humidity"]].sum(axis=0)    # axis=1:横方向に計算
print data.sort("humidity", ascending=False)   # 降順でソート
# data.to_csv("log.csv")    # csv形式で保存