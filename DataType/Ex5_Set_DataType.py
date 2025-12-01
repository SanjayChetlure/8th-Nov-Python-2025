#create set object
st={"mahesh",101,'A',56.1,101,101}

print(st)         #{56.1, 'mahesh', 101, 'A'}

#size of set
print(len(st))           #4

print("--------All data---------")
#add single element
st.add(5)          #{5, 101, 'mahesh', 'A', 56.1}
print(st)

#add multiple elements
st.update(["abc","xyz"])         #{'abc', 5, 101, 'mahesh', 'A', 'xyz', 56.1}
print(st)

print("-----Remove data------")
#remove          -> it throws error if element doesn't exist
st.remove("xyz")
print(st)               #{'mahesh', 5, 101, 'A', 'abc', 56.1}

#discard           -> no error even if element doesn't exist
st.discard("abc")
print(st)               #   {5, 101, 'mahesh', 'A', 56.1}

#pop            -> random element gets removed
st.pop()
print(st)

print("--------")
for i in st:
    print(i)

print("----Copying set----")
st1=st.copy()
print(st1)          #{56.1, 'A', 101, 'mahesh'}


print("--------------sorting operation-----------------")
st2={50,30,10,40,60,50}
print(st2)
st2=sorted(st2)
print(st2)        #[10, 30, 40, 50, 60]

print("----clear set----")
st3={"mahesh",101,'A',56.1,101,101}
st3.clear()
print(len(st3))

print("----delete set----")
del st3
# print(st3)



print("-------convert set to list---------")
st4={50,30,10,40,60,50}
print(st4)
ls=list(st4)
print(ls)



