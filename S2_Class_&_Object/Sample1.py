
class Demo1:            #class declaration
    #class body

    #members of class
    #1-method  (non-static/static)
    #2-variables
    #-Constructor

    #non-static/instance method-> without parameter
    def m1(self):       #method declaration
        #method body
        print("method m1 running")

    def m2(self):
        print("method m2 running")

    # non-static/instance method-> with parameter
    def squareOfNum(self,num):
        print(num*num)

    def addOfNum(self,num1,num2):
        print(num1+num2)



#call/run non-static/instance method from class
#1: Create object/instance of class   ->  objectName=className()
#2: method call using syntax -> objectName.methodName()

s1=Demo1()
s1.m1()
s1.m2()
s1.squareOfNum(8)
s1.addOfNum(2,4)

print("---")

s2=Demo1()
s2.squareOfNum(9)
s2.addOfNum(5,6)



#para 1- s1 > objectName  -> to identify/refer object
#para 2- Demo1()> className() -> constructor -> create object & store all data(variables & method) from class into object
# className()






