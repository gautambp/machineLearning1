# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls")
#print("Read the cars.xls - a few lines from head")
#print(df)

scale = StandardScaler()
x = df[['Mileage', 'Cylinder', 'Doors']]
#print(x)
y = df['Price']
#print(y)

# scale the data between -1 & 1
x[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(x[['Mileage', 'Cylinder', 'Doors']].as_matrix())
#print(x)

results = sm.OLS(y, x).fit()
print("Result params (coeff for each feature) - ", results.params)
print("Result t-values (for each feature) - ", results.tvalues)
