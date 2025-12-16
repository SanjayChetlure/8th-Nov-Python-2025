class Demo:

   def add(self,a=0,b=0,c=0,d=0):
       print(a+b+c+d)

d=Demo()
d.add()                        #method without parameter
d.add(5,6)               #method with 2 parameter
d.add(5,6,7)          #method with 3 parameter
d.add(5,6,7,8)     #method with 4 parameter
print("------------")



class Demo1:

    def studentName(self,name="abc"):
        print("student Name: ",name)


d1=Demo1()
d1.studentName()
d1.studentName("xyz")







