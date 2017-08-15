# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

# create fake clustered data for n people in k clusters
def createClusteredData(n, k):
    ptsPerCluster = float(n)/k
    x = []
    y = []
    for i in range(k):
        # random income between 20k and 200k
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        # random age between 20 & 70
        ageCentroid = np.random.uniform(20, 70)
        for j in range(int(ptsPerCluster)):
            # for each pt in cluster, create random income centered around incomeCentroid
            # and random age centered around ageCentroid
            x.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)
            
    return np.array(x), np.array(y)

(x, y) = createClusteredData(100, 5)

plt.scatter(x[:,0], x[:,1], c=y.astype(np.float))
plt.show()

c = 1.0
svm = svm.SVC(kernel='linear', C=c).fit(x, y)

def plotPredictions(clf):
    ageRange = np.arange(0, 80, 0.5)
    incomeRange = np.arange(0, 250000, 10)
    xx, yy = np.meshgrid(incomeRange, ageRange)
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(x[:,0], x[:,1], c=y.astype(np.float))
    plt.show()

plotPredictions(svm)
