
shoppingAmt=3000

#3000>=500
if shoppingAmt>=500:     #outer if
    print("no delivery charges applied")
    #3000>=2000
    if shoppingAmt>=2000:   #inner/nested if
        print("10% additional discount")
    else:
        print("no additional discount")
else:
    print("RS 50 delivery charges applied")
