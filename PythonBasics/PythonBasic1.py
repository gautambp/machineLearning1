# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

myNos = np.random.normal(25.0, 5.0, 10);
for i in myNos:
    print(i)
print(myNos);
print(len(myNos));
print(myNos[:3]);
print(myNos[3:]);
print(myNos[-2:]);
print(myNos[:-2]);
# lists use [] brackets and are mutable
x = [9, 8, 7, 6, 5]
x.extend([1, 2, 3, 4]);
x.append(10);
print(x);
x.sort();
print(x);
y = [x, myNos];
print(y);
(age, income) = "35,20000".split(",");
print(age, income);
""" tuple, same as list but immutable """
t1 = (1, 2, 3);
print(t1);
# dictionaries use {} brackets
myMap = {}
myMap["name"] = "some name";
myMap["age"] = 30;
print(myMap);
print(myMap.get("name"), myMap["age"]);
