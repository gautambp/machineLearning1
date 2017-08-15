# -*- coding: utf-8 -*-

from collections import deque

#how to use list as stack
myStack = [1, 2, 3]
myStack.append(4)
print(myStack)
print(myStack.pop())
print(myStack)

#how to do queuing..
myqueue = deque([1, 2, 3])
print(myqueue)
myqueue.append(4)
print(myqueue)
# pop from right/last
print(myqueue.pop())
# pop from left/first
print(myqueue.popleft())
print(myqueue)

# how to use range
myRange = range(10)
print(myRange)

#how to use list and map
myMap = map(lambda x: x ** 2, range(10))
sqrs = list(myMap)
print(sqrs)
# same result different ways
sqrs = [x ** 2 for x in range(10)]
print(sqrs)

myTuples = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]
print(myTuples)

# exclude negatives from the list
aList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print([x for x in aList if x >= 0])
