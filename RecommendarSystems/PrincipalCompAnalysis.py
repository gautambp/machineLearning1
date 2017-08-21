# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as py
from itertools import cycle

iris = load_iris()
numSamples, numFeatures = iris.data.shape
# it has 4 features..  means 4 dimensions
print(numSamples)
print(numFeatures)
print(iris.target_names)

X = iris.data
# n_components = 2 .. go down to 2 dimension
# whiten indicates normalizing
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)

print(pca.components_)
