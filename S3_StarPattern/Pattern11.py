#*****
# ****
#  ***
#   **
#    *



space=0
star=5
for i in range(5):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    print()
    space+=1
    star-=1