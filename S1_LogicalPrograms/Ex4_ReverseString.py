# 4: Reverse String
#  Apr1:
org = "xyz"
rev=org[::-1]
print(rev)


# Apr2:
orgString = "abcd"
revString=""       #dcba

for singleCharinString in orgString:
  revString = singleCharinString + revString       #d+cba = dcba

print(revString)