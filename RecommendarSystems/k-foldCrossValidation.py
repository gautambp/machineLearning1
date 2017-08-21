# -*- coding: utf-8 -*-

import numpy as np
from sklearn import datasets, svm, cross_validation

# load iris data
iris = datasets.load_iris()

# this is conventional train/test split.. with 40% data for test
# split iris data into random sets.. reserve 40% data for test and rest for train
x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

# build the SVC model with train dataset
clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)

# measure the model performance with test dataset
print(clf.score(x_test, y_test))


# now we'll try out k-fold (k-random buckets) cross-validation with k = 5
scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(scores.mean())



