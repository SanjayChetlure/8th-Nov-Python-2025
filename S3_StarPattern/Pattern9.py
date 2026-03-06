#  *
# **
#***

space=2
star=1
for i in range(3):         #3<=3
    for j in range(space):  #1<=0
        print(" ",end="")
    for j in range(star):   #1<=3
        print("*",end="")
    print()
    space-=1      #0
    star+=1       #3


#  *
# **
#***