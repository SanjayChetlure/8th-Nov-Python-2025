# 3: elif -> syntax
#
# if condition1:
#     ifBody
# elif condition2:
#     elIfBody
# elif condition3:
#     elIfBody
# elif condition4:
#     elIfBody


marks=30

if marks>=65:
    print("distinction")
    #55>=60 and 62<65
elif marks>=60 and marks<65:                           # 60 - 64.9
    print("1st class")
    #55>=50 and 55<60
elif marks>=50 and marks<60:
    print("2nd class")
    #42>=35 and 42<50
elif marks>=35 and marks<50:
    print("Pass")
    #30<35
elif marks<35:
    print("Fail")





# true and true  -> true
# true and false -> false
# false and true -> false
# false nad false -> false