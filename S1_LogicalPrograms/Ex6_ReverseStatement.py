inp = "my name is abc"
output="abc is name my"

print(inp)
l1=inp.split()     #[my(0)  name(1)  is(2)  abc(3)]
l1.reverse()      # [abc(0)   is(1)   name(2)  my(3)]    l1=l1[::-1]
# print(l1)


out=' '.join(l1)        #abc is name my
print(out)
