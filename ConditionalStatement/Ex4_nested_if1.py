
PEM=350

# 350>=300
if PEM>=300:      #outer if
    print("Selected in Prelim exam")
    print("preparing for mains exam")
    MEM=501
    #  501>=500
    if MEM>=500:    # inner/nested if
        print("selected in mains exam")
    else:
        print("rejected in mains exam")
else:
    print("rejected in prelim exam")