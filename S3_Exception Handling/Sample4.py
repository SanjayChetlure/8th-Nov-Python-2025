
print("----4: correct way of using of using generic exception----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)     #10/0= ZeroDivisionError
except ValueError:
    print("value error exception handled")
except ZeroDivisionError:
    print("Zero division exception handled")
except Exception as e:
    print("generic exception handled")
    print(e)

print("program ended")