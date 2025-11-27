
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





