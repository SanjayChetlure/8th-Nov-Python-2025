#1: global variable

num1=10     #global variable

def f1():
    print(num1)

f1()
print("----")

class Demo1:

    def m1(self):
        print(num1)

d1=Demo1()
d1.m1()


