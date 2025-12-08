
# objectName=[]    -> syntax of list object creation
# 1: List is declared using [ ]
# 2: List contains duplicate Items
# 3: order of insertion Maintained in list
# 4: data is stored in index format (index start with 0)


ls=['Rahul',101,65.5,"A+",101]

#display data
print(ls)

#print type of object
print(type(ls))

#get size of list
print(len(ls))

#get data from specific index
print(ls[1])     #101

#replace existing data with new data
ls[0]="RAHUL"       #reinitialization of index 0


print("-------add data in list (append/insert/extend)---------")
#Add single data at last position
ls.append("xyz")
print(ls)

#add new data at specific position -> right shift operation
ls.insert(1,200)
print(ls)

#add multiple at the end of list object
ls.extend([10,40,"abc"])
print(ls)


print("-------remove data from list(pop/pop(index)/remove(element))---------")
# remove last element from list
ls.pop()
print(ls)

# remove element from specific index -> left shift operation
ls.pop(4)
print(ls)

# remove specific element from list
ls.remove("xyz")
print(ls)


print("-----copy list--------")
ls1=ls.copy()
print(ls1)


print("--------print all data using for loop-------")
for i in ls:
    print(i)

print("----")

for i in range(0,7):    # 2<7              0 to 6
    print(ls[i])

# for i in range(0,len(ls)):    # 2<7              0 to 6
#     print(ls[i])

print("----")

for i in range(1,5):    # 2<7              0 to 2
    print(ls[i])


print("--------print list in reverse order-------")
print(ls)
ls.reverse()
print(ls)


