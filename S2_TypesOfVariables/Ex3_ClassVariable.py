#3: class variable

class Demo4:

    num1=20                       #num1 -> class variable

    def __init__(self,a):
        self.num2=a                #num2-> class variable

    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1*self.num2)

d4=Demo4(6)
d4.add()
d4.mult()
print(d4.num1)
print(d4.num2)

