#ModuleName 2: ArithMaticOperations

#Approach1: import moduleName
# moduleName.fn()    -> call functions
# moduleName.variable  -> global variable call

# obj=moduleName.className()      #object create class from diff module
# obj.methodName()               -> method call
# obj.variableName              -> class variable call


import Calculator

#call Function & global variable
Calculator.add(10,20)         #call fn
Calculator.mult(5,8)
print(Calculator.num)                     #call global variable

print("---------")

#class methods & class variables
d1=Calculator.Demo1()                 #object creation
d1.m1()                               # method call
d1.m2()
print(d1.a)                           # class variable call