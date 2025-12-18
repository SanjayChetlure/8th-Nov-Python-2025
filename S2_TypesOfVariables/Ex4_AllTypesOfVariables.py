#4: All Types of variable

num1=10           #global variable

class Demo5:

    num2=20                       #num1 -> class variable

    def __init__(self,a):          # a  ->  local variable
        self.num3=a                #num2-> class variable

    def m1(self,num4):        # num4   -> local variable
        num5=50               # num5   -> local variable
        print(num5)
        print(num4)
        print(self.num2)
        print(self.num3)
        print(num1)

d5=Demo5(7)
d5.m1(8)


