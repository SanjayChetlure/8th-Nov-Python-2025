#ex3: static & non-static method in same class

class Demo3:

    def m1(self):
        print("running non-static method m1")

    def squareOfNum(self, num):
        print("square of num",num,"is",num*num)

    @staticmethod
    def m2():
        print("running static method m2")

    @staticmethod
    def mult(num1, num2):
        print("multiplication of numbers",num1,"&",num2,"is",num1*num2)


#call non-static method
d3=Demo3()
d3.m1()
d3.squareOfNum(6)

print("----")
#call static methods
Demo3.m2()
Demo3.mult(4,5)


