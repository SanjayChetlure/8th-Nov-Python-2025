org = "abcd"
rev=org[::-1]


# if org.__eq__(rev):
if org==rev:        #abcd==dcba
   print("Palindrome")
else:
   print("not a palindrome")