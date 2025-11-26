#3: Function with Return type
print("------3.1 - Function with Single return type-------")

def getStudentName():
    name="Amol"
    return name

s1=getStudentName()     #amol
print(s1)
print(getStudentName())

print("----")

def add():
    num1=10
    num2=30
    num3=num1+num2
    return num3

num4=add()
print(num4)
print(add())

print("----")

def add(num1, num2):
    num3=num1+num2
    return num3

num4=add(5,6)
print(num4)

num5=add(7,8)
print(num5)

print(add(11,12))



print("------3.2 - Function with multiple return type-------")

def addAndMult(num1,num2):
    add=num1+num2
    mult=num1*num2
    return add,mult

num3, num4=addAndMult(5,6)
print("Addition-",num3)
print("multiplication-",num4)
