# Ex2: user defined without parameter constructor

class Demo2:

    #user defined constructor -> without parameter
    #use1: initialize object
    def __init__(self):        #Constriuctor declare
        print("running constructor")

    def m1(self):
        print("running non-static method m1")

d2=Demo2()   #Object Creation -> Constructor call -> initialize object
d2.m1()                    #Copy all members of class into object