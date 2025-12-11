# Ex3: user defined with parameter constructor

class Demo3:

    #user defined with parameter constructor
    #use1: initialize object
    #use2: initialize class variable
    def __init__(self,num):      #num=4  (local variable)
        self.num1=num               # assign local variable data into class variable  classVariable=localVariable

    def squareOfNum(self):
        print(self.num1*self.num1)

    def cubeOfNUm(self):
        print(self.num1*self.num1*self.num1)


d3=Demo3(4)
d3.squareOfNum()
d3.cubeOfNUm()

print("-----")

d4=Demo3(5)
d4.squareOfNum()
d4.cubeOfNUm()

print("-----")

d5=Demo3(6)
d5.squareOfNum()
d5.cubeOfNUm()


