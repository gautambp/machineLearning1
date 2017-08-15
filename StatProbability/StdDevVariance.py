# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

print("incomes centered around 100 with variance of 20")
incomes = np.random.normal(100, 20, 10000)

plt.hist(incomes, 50)
plt.show()

print("Std Dev - ", incomes.std())
print("Variance - ", incomes.var())
