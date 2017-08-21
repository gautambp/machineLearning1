# -*- coding: utf-8 -*-

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

conf = SparkConf().setMaster('local').setAppName('DecisionTree')
sc = SparkContext(conf = conf)

def binary(YN):
    if (YN == 'Y'):
        return 1
    else:
        return 0
    
def mapEducation(degree):
    if (degree == 'BS'):
        return 1
    elif (degree == 'MS'):
        return 2
    elif (degree == 'PhD'):
        return 3
    else:
        return 0

def createLabeledPoints(fields):
    exp = int(fields[0])
    employed = binary(fields[1])
    prevEmp = binary(fields[2])
    edu = mapEducation(fields[3])
    topTier = binary(fields[4])
    interned = binary(fields[5])
    hired = binary(fields[6])
    return LabeledPoint(hired, array([exp, employed, prevEmp, edu, topTier, interned]))
    
rawData = sc.textFile('PastHires.csv')
# separate header and the data
header = rawData.first()
rawData = rawData.filter(lambda x: x != header)

# convert each line to the list of comma separated fields
csvData = rawData.map(lambda x: x.split(','))

trainData = csvData.map(createLabeledPoints)

testCandidate = [array([10, 1, 3, 1, 0, 0])]
testData = sc.parallelize(testCandidate)

model = DecisionTree.trainClassifier(trainData, numClasses=2, impurity='gini', maxDepth=5, maxBins=32,
                                     categoricalFeaturesInfo={1:2, 3:4, 4:2, 5:2})

predicts = model.predict(testData)
results = predicts.collect()
for result in results:
    print(result)

print(model.toDebugString())
