
print("----5: Alternative way of using of using generic exception----")

num1=10
num2=2

print("program started")
try:
    print(num1/num2)     #10/0= ZeroDivisionError
except:
    print("generic exception handled")

print("program ended")

# except Exception as e:
#     print("generic exception handled")
#     print(e)
# except Exception:
#     print("generic exception handled")


