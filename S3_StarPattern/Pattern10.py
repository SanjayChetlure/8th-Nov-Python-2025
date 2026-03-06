#     *
#    ***
#   *****
#  *******
# *********
#***********

space=5
star=1
for i in range(6):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    print()
    space-=1
    star+=2
