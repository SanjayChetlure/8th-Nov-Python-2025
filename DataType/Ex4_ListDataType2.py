print("-----Sorting operation------")
s1=[40,10,50,30,20]

print("--before sort---")
print(s1)
s1.sort()  #[10, 20, 30, 40, 50]

print("--after sort->Ascending order---")
print(s1)


print("--soft data >Descending order---")
s1.reverse()      #[50, 40, 30, 20, 10]
print(s1)

print("---occurrence of specific element----")
s2=[40,10,50,30,20,30,40,"abc","xyz","abc"]
print(s2.count("abc"))

print(len(s2))

print("-----remove/clear all elements from list----")
s2.clear()
print(len(s2))

print("-----delete list----")
del s2







