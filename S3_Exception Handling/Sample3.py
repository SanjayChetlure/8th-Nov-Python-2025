print("----3.1: example of generic exception----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)     #10/0= ZeroDivisionError
except Exception:
    print("generic exception handled")

print("program ended")



print("----3.2: example of generic exception----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)     #10/0= ZeroDivisionError
except Exception as e:
    print("generic exception handled")
    print(e)

print("program ended")