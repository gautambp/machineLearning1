# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmt = np.random.normal(50.0, 30.0, 100) / pageSpeeds

print("Entire dataset")
plt.scatter(pageSpeeds, purchaseAmt)
plt.show()

# allocate 80% for training and 20% for testing
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmt[:80]
testY = purchaseAmt[80:]

print("Train dataset")
plt.scatter(trainX, trainY)
plt.show()

print("Test dataset")
plt.scatter(testX, testY)
plt.show()

x = np.array(trainX)
y = np.array(trainY)
model = np.polyfit(x, y, 6)
predictor = np.poly1d(model)

print("Train dataset with the model")
xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, predictor(xp), c="r")
plt.show()

print("Performance of the model against train data - ", r2_score(y, predictor(x)))

print("Test dataset with the model")
x = np.array(testX)
y = np.array(testY)
xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, predictor(xp), c="r")
plt.show()

print("Performance of the model against test data - ", r2_score(y, predictor(x)))

