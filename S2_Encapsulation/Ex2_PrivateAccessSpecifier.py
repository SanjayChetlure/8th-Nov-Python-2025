
#Ex2_PrivateAccessSpecifier.py

class Demo1:

    def __init__(self,num1,num2,num3):
        self.__num1=num1       #access specifier->private
        self.__num2=num2       #access specifier->private
        self.num3=num3         #access specifier->public

    def add(self):                  #access specifier->public
        sum=self.__num1+self.__num2
        print(sum)

    def __squareOfNum(self):        #access specifier->private
        print(self.num3*self.num3)

    def m1(self):                   #access specifier->public
        self.__squareOfNum()

d1=Demo1(10,20,30)
d1.add()                     #acceesing public method - access
d1.__squareOfNum()           #accessing private method - no access
d1.m1()                      #acceesing public method -  access
print(d1.__num1)             #accessing private variable -no access
print(d1.__num2)             #accessing private variable -no access
print(d1.num3)               #acceesing public variable - access