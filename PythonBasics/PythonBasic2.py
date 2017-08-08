# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:43:06 2017

@author: gauta
"""

def mySquare(x):
    return x * x;

def doSomething(func, param):
    return func(param);

print(mySquare(5));
print(doSomething(mySquare, 10));

print(doSomething(lambda x: x * x * x, 10));