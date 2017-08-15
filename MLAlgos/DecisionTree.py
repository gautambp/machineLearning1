# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.externals.six import StringIO
from IPython.display import Image

df= pd.read_csv("PastHires.csv")
print("Past hires data - ", df.head())

d = {"Y": 1, "N": 0}
df["Hired"] = df["Hired"].map(d)
df["Interned"] = df["Interned"].map(d)
df["Employed?"] = df["Employed?"].map(d)
df["Top-tier school"] = df["Top-tier school"].map(d)

d = {"BS": 0, "MS": 1, "PhD":2}
df["Level of Education"] = df["Level of Education"].map(d)
print("Past hires mapped data - ", df.head())

# pick all but last Hired column as features
features = list(df.columns[:6])
print("Features from the file - ", features)

y = df["Hired"]
x = df[features]

# create decision tree classifier and train it with the data
cf = tree.DecisionTreeClassifier()
cf = cf.fit(x, y)

#dot_data = StringIO()
# export all data from the tree in dot_data string
#tree.export_graphviz(cf, out_file=dot_data, feature_names=features)

# find prediction for a 10 years experienced candidate
testcase= [10, 1, 4, 0, 0, 0]
print("Prediction of decision tree data : ", cf.predict(testcase))

