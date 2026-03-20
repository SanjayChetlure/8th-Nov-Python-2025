# 9: Duplicate Occurrence, Duplicate & Unique words in statement


s = "this is a test this is only a test b is"
allWords = s.split()
dict = {}

# Key    Value
# this  1+1=2
# is    1+1=2+1=3
# a     1+1=2
# test  1+1
# only  1
# b     1



for word in allWords:             #test
   if dict.__contains__(word):    #false
       dict[word]=dict.get(word)+1   #1 + 1 = 2
   else:
       dict[word]=1

       #dict
       # key        Value
       # this       2
       # is         1
       # a          1
       # test       1

print("------Print Occurrence of each word in statement------")
for key in dict:
       print(key, dict.get(key))


print("------Print only duplicate words in statement------")
for k in dict:
   if dict.get(k)>1:
       print(k, dict.get(k))


print("------Print only unique words in statement------")
for k in dict:
   if dict.get(k)==1:
       print(k, dict.get(k))