#variable override with super()

class Parent:
    name="amol"


class Child(Parent):
    name = "AMOL"

    def studentName(self):
        print("Sub class Student Name: ",self.name)
        print("Super class Student Name: ",super().name)


childClassObj=Child()
childClassObj.studentName()
