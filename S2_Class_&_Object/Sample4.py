# 4: method with return  type

class Demo4:

    def add(self,num1, num2):
        add = num1 + num2
        return add

d4=Demo4()
addValue=d4.add(5,6)
print(addValue)

print("-----")

print(d4.add(7,8))
