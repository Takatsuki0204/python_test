#! /usr/bin/python
# encoding: utf-8

import datetime, sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tick
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'C:\WINDOWS\Fonts\YuGothic.ttf', size=14)

connector = sqlite3.connect("C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db")
data = pd.read_sql("SELECT * FROM environment WHERE datetime BETWEEN '2016-06-06 00:00:00' AND '2016-06-06 23:59:59'", connector)
connector.close()
xdate = pd.to_datetime(data["datetime"])
print xdate
ytemp = data["temp"]
yhumidity = data["humidity"]

fig = plt.figure(figsize=(15, 5))

# ax1:Temp plot settings
ax1 = fig.add_subplot(1, 2, 1)
xfmt = mdates.DateFormatter('%H:%M:%S')
ax1.xaxis.set_major_formatter(xfmt)
ax1.yaxis.set_major_locator(tick.MultipleLocator(10))
ax1.plot(xdate, ytemp)
ax1.set_ylim(0, 40)
ax1.set_title("Temp")
ax1.set_xlabel("Time")
ax1.set_ylabel("Temp")

# ax2:Humidity plot settings
ax2 = fig.add_subplot(1, 2, 2)
xfmt = mdates.DateFormatter('%H:%M:%S')
ax2.xaxis.set_major_formatter(xfmt)
ax2.yaxis.set_major_locator(tick.MultipleLocator(10))
ax2.plot(xdate, yhumidity)
ax2.set_ylim(0, 100)
ax2.set_title("Humidity")
ax2.set_xlabel("Time")
ax2.set_ylabel("Humidity")

fig.autofmt_xdate()
plt.show()