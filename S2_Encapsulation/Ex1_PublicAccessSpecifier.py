#Ex1_PublicAccessSpecifier

class Demo1:

    def __init__(self,num1,num2,num3):
        self.num1=num1       #access specifier->public
        self.num2=num2
        self.num3=num3

    def add(self):          #access specifier->public
        sum=self.num1+self.num2
        print(sum)

    def squareOfNum(self):
        print(self.num3*self.num3)


d1=Demo1(10,20,30)
d1.add()
d1.squareOfNum()
print(d1.num1)
print(d1.num2)
print(d1.num3)