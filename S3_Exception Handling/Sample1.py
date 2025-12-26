# num1=10
# num2=0
#
# print("program started")
# num3=num1/num2        #10/0
# print(num3)
#
# print("hi ")
# print("Hello")
# print("program ended")


print("---1.1 basic example of EH ----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)          #10/0      #risky code
except ZeroDivisionError as e:          #expected exception name
    print("Zero Division Error handled")

print("hi ")
print("Hello")
print("program ended")


print("------1.2 basic example of EH (Alternate solution)-----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)          #10/0      #risky code
except ZeroDivisionError:          #expected exception name
    print(num1/1)            #alterte code

print("hi ")
print("Hello")
print("program ended")


print("------1.3 basic example of EH (Alternate solution & msg)-----")

num1=10
num2=0

print("program started")
try:
    print(num1/num2)          #10/0      #risky code
except ZeroDivisionError:          #expected exception name
    print("Zero Division Error handled ")
    print(num1/1)            #alterte code

print("hi ")
print("Hello")
print("program ended")