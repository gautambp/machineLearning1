# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as skm

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmts = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

x = np.array(pageSpeeds)
y = np.array(purchaseAmts)
result = np.polyfit(x, y, deg=4)
print("Polyfit result : ", result)

predictor = np.poly1d(result)

xp = np.linspace(0, 7, 1000)
plt.scatter(pageSpeeds, purchaseAmts)
plt.plot(xp, predictor(xp), c="r")
plt.show()

# compute r-square error - sum of (y - yp) square

print("R-Squared error : ", skm.r2_score(y, predictor(x)))
