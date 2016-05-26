#! /usr/bin/python
# encoding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_json("http://192.168.10.121:3000/monitoring/122?date=20160523")

xdate = pd.Series(pd.to_datetime(data["updated"]).dt.tz_localize("UTC").dt.tz_convert("Asia/Tokyo"))
ytemp = data["temperature"]
yhumidity = data["humidity"]

fig = plt.figure(figsize=(15, 5))

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(xdate, ytemp)
ax1.set_ylim(0, 40)
ax1.set_title("Temp")
ax1.set_xlabel("Time")
ax1.set_ylabel("Temp")

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(xdate, yhumidity)
ax2.set_ylim(0, 100)
ax2.set_title("Humidity")
ax2.set_xlabel("Time")
ax2.set_ylabel("Humidity")

fig.autofmt_xdate()
plt.show()