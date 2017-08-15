# -*- coding: utf-8 -*-

someConst = 1

def foo(i = someConst):
    print(i)

someConst = 2
foo()

def funcWithSideEffects(a, L=[]):
    L.append(a)
    print(L)
    return L

funcWithSideEffects(1)
funcWithSideEffects(2)
funcWithSideEffects(3)

def bar(p1, p2):
    print(p1)
    print(p2)    

bar(p2=1, p1=2)

def moreParamStuff(p1, *arguments, **keywords):
    print(p1);
    for arg in arguments:
        print(arg)
    for key in keywords:
        print(key, keywords[key])
        
moreParamStuff("Fixed named param", "arg1", "arg2", key1="value1", key2="value2")
# unpacking args and keys
myArgs = ["arg1", "arg2"]
mykeys = {}
mykeys["key1"] = "value1"
mykeys["key2"] = "value2"
moreParamStuff("Fixed named param", *myArgs, **mykeys)

def emptyFunc():
    """ This is function documentation
    More func doc
    The end.. """
    pass

print(emptyFunc.__doc__)