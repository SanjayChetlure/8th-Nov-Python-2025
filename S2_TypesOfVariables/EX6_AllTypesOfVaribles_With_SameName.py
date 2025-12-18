# EX6: All Types Of Variables With Same Name

a,b=10,20           #global variable


class Sample1:

    a,b=30,40            #class variable

    def add(self):
        a,b=50,60        #local variable
        print(a+b)               #addition of local variables
        print(self.a+self.b)     #addition of class variables
        print(globals()['a'] + globals()['b'])   #addition of global variable


S1=Sample1()
S1.add()
