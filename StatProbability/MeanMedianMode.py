# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("Normal income distribution centered around 27000 with 15000 variance");
incomes = np.random.normal(27000, 15000, 10000)

print ("mean income - ", np.mean(incomes))
print ("median income - ", np.median(incomes))

plt.hist(incomes, 50)
plt.show()

print("Adding a billionaire to the income distribution")
incomes = np.append(incomes, [10000000000])

print ("mean income - ", np.mean(incomes))
print ("median income - ", np.median(incomes))

print("For Mode - generate age data for 500 ppl betn 10 & 90")
ages = np.random.randint(10, high=90, size=500)
print(ages)

plt.hist(ages, 8)
plt.show()

print("mode of ages - (most common item, count for it) ", stats.mode(ages))

