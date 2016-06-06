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
data = pd.read_sql("SELECT * FROM environment WHERE datetime < '2016-06-06'", connector)
connector.close()
print data
x = pd.to_datetime(data["datetime"]) # + pd.offsets.Hour(9)
y = data["temp"]

fig, ax = plt.subplots()
ax.plot(x, y)

hour = mdates.HourLocator(byhour=xrange(30), interval=5)
ax.xaxis.set_major_locator(hour)
xfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.yaxis.set_major_locator(tick.MultipleLocator(10))

fig.autofmt_xdate()
plt.title(u"2016-06-02:技術部", fontproperties=fp)
plt.xlabel("Time")
plt.ylabel("Temp")
plt.ylim([0, 40])
plt.grid()

plt.show()