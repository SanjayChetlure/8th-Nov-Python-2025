#Ex3: method overriding with super()

#super class
class A:
    def m1(self):
        print("method m1 from super class")

class B(A):
    def m1(self):           #method override
        super().m1()                          #call existing method body
        print("method m1 from sub class")     #add additional code into sub class method


subClassObj=B()
subClassObj.m1()