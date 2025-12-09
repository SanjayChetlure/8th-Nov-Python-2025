#ex2: static method

class Demo2:

    @staticmethod
    def m3():                       #static method-> without
        print("running static method m3")

    @staticmethod
    def m4():  # static method        #static method-> without
        print("running static method m4")

    @staticmethod
    def add(num1, num2):
        print(num1+num2)


#static method call
# className.methodName()


Demo2.m3()
Demo2.m4()
Demo2.add(7,8)


