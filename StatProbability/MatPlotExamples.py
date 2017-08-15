# -*- coding: utf-8 -*-

import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt
import random

print("Simple line graph")
x = np.arange(-3, 3, 0.001)
plt.plot(x, sp.norm.pdf(x))
plt.show()

print("Multiple plots in one graph")
plt.plot(x, sp.norm.pdf(x))
plt.plot(x, sp.norm.pdf(x, 1, 0.5))
plt.show()

print("Save the graph to a file")
#plt.plot(x, sp.norm.pdf(x))
#plt.plot(x, sp.norm.pdf(x, 1, 0.5))
#plt.savefig('sample.png', format='png')

print("Graph with adjusted plot axis and grid displayed with line colors, legends")
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1])
# ticks from -5 to 5
axes.set_xticks([x-5 for x in range(11)])
# ticks from 0.1 to 1.0
axes.set_yticks([x/10 for x in range(11)])
axes.grid()
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
# b- (blue color & - indicates solid line)
plt.plot(x, sp.norm.pdf(x), 'b-')
# r: (red color & : indicates dotted line)
plt.plot(x, sp.norm.pdf(x, 1, 0.5), 'r:')
plt.legend(['legend 1', 'legend 2'], loc=4)
plt.show()

print("XKCD plot")
plt.xkcd()
data = np.ones(100)
data[70:] -= np.arange(30)
plt.annotate("Plot annotation", xy=(70,1))
plt.plot(data)
plt.show()

print("Simple pie charts")
# reset the plot to defaults.. needed since we changed it to xkcd earlier
plt.rcdefaults()

values = [10, 20, 30, 40]
colors = ['r', 'g', 'b', 'c']
labels = ['US', 'Russia', 'Canada', 'India']
explode = [0, 0, 0, 0.2]
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title('Student Locations')
plt.show()

print("Simple bar charts")
plt.rcdefaults()
plt.bar(range(0, 4), values, color=colors)
plt.show()


print("Scatter Plot")
x = np.random.randn(500)
y = np.random.randn(500)
plt.scatter(x, y)
plt.show()

print("Box & Whisker Plot")
uniformSkewed = np.random.rand(100) * 100 - 40
high_outlier = np.random.rand(10) * 50 + 100
low_outlier = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed, high_outlier, low_outlier))
plt.boxplot(data)
plt.show()
