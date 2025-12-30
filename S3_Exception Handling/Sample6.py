
print("----6: example of finally block-----")


num1=10
num2=0

print("program started")
try:
    print(num1/num2)     #10/0= ZeroDivisionError
except ValueError:
    print("ZeroDivisionError exception handled")
finally:
    print("running finally block")

print("program ended")