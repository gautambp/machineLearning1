# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

print("Normal distribution centered around 0")
vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

print("50 percentile - ", np.percentile(vals, 50))
print("90 percentile - ", np.percentile(vals, 90))
print("10 percentile - ", np.percentile(vals, 10))

print("Moment (first = mean) - ", np.mean(vals))
print("Moment (second = variance) - ", np.var(vals))
print("Moment (third = skew) - ", sp.skew(vals))
print("Moment (fourth = kurtosis) - ", sp.kurtosis(vals))

