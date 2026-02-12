# Apr1:
# num1 = 2456
#
# s1=str(num1)                          # str(num) converts the number to a string.
# s1_Rev=s1[::-1]                      # [::-1] reverses the string.
# num1_rev= int(s1_Rev)                # int(s1_Rev) converts it back to an integer.
# # rev = int(str(num)[::-1])
# print(num1_rev)




# Apr2:
orgNum = 123
rev = 0      #321
while orgNum>0:    #0>0
   rem=orgNum%10       #1%10=1            #get last digit
   rev=rev*10+rem      #320 + 1=321                   #Append last digit to rev num
   orgNum =orgNum//10     #1//10=0            #remove last digit
print(rev)
