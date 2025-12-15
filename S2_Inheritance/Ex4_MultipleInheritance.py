#4: Example of multiple inheritance

#super class 1
class A:
    def m1(self):
        print("method m1 from super class A")

#super class 2
class B:
    def m2(self):
        print("method m2 from super class B")

#sub class
class C(A,B):
    def m3(self):
        print("method m3 from sub class C")


subClassObj=C()
subClassObj.m1()
subClassObj.m2()
subClassObj.m3()

