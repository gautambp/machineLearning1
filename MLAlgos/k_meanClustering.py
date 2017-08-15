# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

# create fake clustered data for n people in k clusters
def createClusteredData(n, k):
    np.random.seed(10)
    ptsPerCluster = float(n)/k
    x = []
    for i in range(k):
        # random income between 20k and 200k
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        # random age between 20 & 70
        ageCentroid = np.random.uniform(20, 70)
        for j in range(int(ptsPerCluster)):
            # for each pt in cluster, create random income centered around incomeCentroid
            # and random age centered around ageCentroid
            x.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
    return np.array(x)

# create random income/age data for 100 people in 5 clusters
data = createClusteredData(100, 5)

# create kmeans model for 5 clusters
model = KMeans(n_clusters=5)

# train the model with random income/age data
# scale the data to get good results
model = model.fit(scale(data))

print ("Model labels after the training", model.labels_)

plt.scatter(data[:, 0], data[:, 1], c=model.labels_.astype(np.float))
plt.show()
