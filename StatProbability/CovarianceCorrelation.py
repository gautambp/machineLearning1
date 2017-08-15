# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x, y) / stddevx / stddevy

pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmt = np.random.normal(50, 10, 1000)

plt.scatter(pageSpeeds, purchaseAmt)
plt.show()

print("manually computed covariance - ", covariance(pageSpeeds, purchaseAmt))
print("manually computed correlation - ", correlation(pageSpeeds, purchaseAmt))
print("numpy computed covariance - ", np.cov(pageSpeeds, purchaseAmt))
print("numpy computed correlation - ", np.corrcoef(pageSpeeds, purchaseAmt))

purchaseAmt = np.random.normal(50, 10, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmt)
plt.show()

print("manually computed covariance with amt/speed - ", covariance(pageSpeeds, purchaseAmt))
print("manually computed correlation with amt/speed - ", correlation(pageSpeeds, purchaseAmt))
print("numpy computed covariance with amt/speed - ", np.cov(pageSpeeds, purchaseAmt))
print("numpy computed correlation with amt/speed - ", np.corrcoef(pageSpeeds, purchaseAmt))

