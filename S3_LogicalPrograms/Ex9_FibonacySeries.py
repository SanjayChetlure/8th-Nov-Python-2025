# 8: Fibonacci series
num1 = 0  #1  1  2
num2 = 1  #1  2  3


for i in range(10):
   print(num1, end=" ")    #   0 1 1 2
   num3 = num1 + num2   #3
   num1 = num2    #1
   num2 = num3   #3


#0 1 1 2