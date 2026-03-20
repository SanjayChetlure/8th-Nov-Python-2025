# 10: Occurrence, Duplicate & Unique chars in string
from S1_DataType.Ex6_Dict import value

name = "abcdabb"
dict= {}

# key  value
# a     1
# b     1


for char in name:
   if dict.__contains__(char):
       dict[char]=dict.get(char)+1
   else:
       dict[char]=1


print("------Print Occurrence of each char in string------")
for k in dict:
       print(k, dict.get(k))


print("------Print only duplicate char in string------")
for k in dict:
   if dict.get(k)>1:
       print(k, dict.get(k))


print("------Print only unique char in string------")
for k in dict:
   if dict.get(k)==1:
       print(k, dict.get(k))