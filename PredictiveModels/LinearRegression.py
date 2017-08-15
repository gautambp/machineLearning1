# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmts = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

slope, intercept, r_value, p_value, std_err = st.linregress(pageSpeeds, purchaseAmts)

print("Fitness of points to the line - ", r_value ** 2)

def predict(x):
    return slope * x + intercept

predictedPurchaseAmts = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmts)
plt.plot(pageSpeeds, predictedPurchaseAmts, c="r")
plt.show()

