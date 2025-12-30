print("----2: example of multiple except block----")


num1=10
num2=0

print("program started")
try:
    print(num1/num2)     #10/0 = ZeroDivisionError
except ValueError:
    print("value error exception handled")
except AttributeError:
    print("AttributeError handled ")
except ZeroDivisionError:
    print("Zero Division Error handled ")

print("program ended")