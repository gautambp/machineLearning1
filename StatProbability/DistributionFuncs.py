# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps 

print("Random values (-10 to 10) with uniform probability")
values = np.random.uniform(low=-10, high=10, size=100000)
plt.hist(values, 50)
plt.show()

print("Range of values (-3 to 3) with normal distribution")
x = np.arange(-3, 3, 0.001)
plt.plot(x, sps.norm.pdf(x))
plt.show()

print("Exponential distribution (0 to 10)")
x = np.arange(0, 10, 0.001)
plt.plot(x, sps.expon.pdf(x))
plt.show()

print("Binomial probability distrubution (range 10 and centered at 50%)")
n, p = 10, 0.5
x = np.arange(0, n, 0.001)
plt.plot(x, sps.binom.pmf(x, n, p))
plt.show()

print("Poisson probability distribution (median - 500, variance - 100)")
mu = 500
x = np.arange(mu-100, mu+100, 0.5)
plt.plot(x, sps.poisson.pmf(x, mu))
plt.show()
