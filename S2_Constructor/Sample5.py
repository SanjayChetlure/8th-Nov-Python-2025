class Demo5:

    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2


    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)

    def sub(self):
        print(self.num1 - self.num2)


obj1=Demo5(4,5)
obj1.add()
obj1.mult()
obj1.div()
obj1.sub()

print("-----")
obj2=Demo5(10,8)
obj2.add()
obj2.mult()
obj2.div()
obj2.sub()