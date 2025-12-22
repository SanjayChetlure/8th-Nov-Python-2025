# ModuleName:  ArithmaticOperation2

#Approach2:
# from moduleName import variableName, functionName, className
# from moduleName import *

# fn()                       -> function call
#  objName=className()      -> object creation


print("2.1 import only specific data")

from Calculator import num,add, Demo1       #import only num(variable), add(fn), Demo1(class)


print(num)                   #variableCall

add(5,6)         #function Call

d1=Demo1()                   #objectCreation
d1.m1()
d1.m2()
