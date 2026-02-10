
#Ex3: Example of Encapsulation

class Demo2:

    def __init__(self,num1,num2,num3):
        self.__num1=num1
        self.__num2=num2
        self.__num3=num3

    def add(self):
        print(self.__num1+self.__num2+self.__num3)

    def mult(self):
        print(self.__num2 * self.__num3)

    def squareOfNum(self):
        print(self.__num3*self.__num3)


d2=Demo2(10,20,30)
d2.add()
d2.mult()
d2.squareOfNum()

