# -*- coding: utf-8 -*-

from pyspark.mllib.clustering import KMeans
from numpy import array, random
from math import sqrt
from pyspark import SparkConf, SparkContext
from sklearn.preprocessing import scale

conf = SparkConf().setMaster('local').setAppName('KMeansClustering')
sc = SparkContext(conf = conf)

# create clustered data for n people in k buckets
def createClusteredData(n, k):
    random.seet(10)
    ptsPerCluster = float(n)/k
    x = []
    for i in range(k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(ptsPerCluster):
            x.append([random.normal(incomeCentroid, 10000), random.normal(ageCentroid, 2.0)])
    return array(x)

# k = 5 bucket.. n = 100 people
k = 5
data = sc.parallelize(scale(createClusteredData(100, k)))
clusters = KMeans.train(data, k, maxIterations=10, runs=10, initializationMode='random')

resultRDD = data.map(lambda pt : clusters.predict(pt)).cache()
print(resultRDD.countByValue())
