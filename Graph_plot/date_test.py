#! /usr/bin/python
# encoding: utf-8

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tick

data = pd.read_json("http://192.168.10.121:3000/monitoring/122?date=20160523")
x = pd.to_datetime(data["updated"]) + pd.offsets.Hour(9)
y = data["temperature"]

fig, ax = plt.subplots()
ax.plot(x, y)

hour = mdates.HourLocator(byhour=xrange(24), interval=6)
ax.xaxis.set_major_locator(hour)
xfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.yaxis.set_major_locator(tick.MultipleLocator(10))

fig.autofmt_xdate()
plt.title("ID:122")
plt.xlabel("Time")
plt.ylabel("Temp")
plt.ylim([0, 40])
plt.grid()

plt.show()