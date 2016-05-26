import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("http://stat.biopapyrus.net/data/tseed.csv", dtype = np.float, delimiter = ",")

x = np.array([1, 2, 3, 4, 5])
y = data.mean()
e = np.sqrt(data.var())

plt.bar(x, y, align = "center", yerr = e, ecolor = "black")
plt.xticks(x, data.columns)
plt.show()