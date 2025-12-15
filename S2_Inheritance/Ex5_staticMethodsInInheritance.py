class Test1:

    @staticmethod
    def m1():
        print("static method m1 from super class Test1")


class Test2(Test1):

    @staticmethod
    def m2():
        print("static method m2 from sub class Test2")

Test2.m1()
Test2.m2()