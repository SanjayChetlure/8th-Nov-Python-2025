num = 153
sum = 0          #
orgNum=num           #153


while num>0:      #153>0   15>0  1>0  0>0
   rem=num%10    #1%10 = 1
   sum=sum + rem*rem*rem   # 152 + 1= 153
   num =num//10            #1//10 =0


print(sum)
if orgNum == sum:    #153==153
   print("Given num is armstrong")
else:
   print("Given num is not armstrong")