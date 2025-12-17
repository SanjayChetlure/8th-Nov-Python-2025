#2: Local variable

print("------Local variables in functions-------")

def f1_add():
    num1=10             #local variable
    num2=20             #local variable
    print(num1+num2)

def f2_mult(num3, num4):       #num3, num4  -> local variable
    print(num3*num4)

f1_add()
print("--")
f2_mult(5,7)

print("-----Local variables in method------")

class Demo2:

    def m1_div(self):
        num1=30                #local variable
        num2=5                 #local variable
        print(num1/num2)

    def m2_sub(self, num1,num2):        #num1,num2-> local variables
        print(num1-num2)

d2=Demo2()
d2.m1_div()
d2.m2_sub(7,9)


print("-----Local variables in constructor------")

class Demo3:

    def __init__(self,a):         #a-> local variable
        b=20                      #b  -> local variable
        self.num1=a             #assign local variable info into class variable
        self.num2=b             #classVariable=localVariable

    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1*self.num2)

d3=Demo3(5)
d3.add()
d3.mult()


