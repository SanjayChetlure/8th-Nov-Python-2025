# Example3: Hirarchical Inheritance

#super class
class Father:
    def car(self):
        print("Car: Tata")

    def money(self):
        print("Money: 1L")

    def home(self):
        print("home: 2BHK")


#sub class 1
class Son1(Father):
    def mobile(self):
        print("Mobile- Samsung")

    # def car(self):
    #     print("Car: Tata")
    #
    # def money(self):
    #     print("Money: 1L")
    #
    # def home(self):
    #     print("home: 2BHK")

#sub class 2
class Son2(Father):
    def laptop(self):
        print("Laptop-HP")

    # def car(self):
    #     print("Car: Tata")
    #
    # def money(self):
    #     print("Money: 1L")
    #
    # def home(self):
    #     print("home: 2BHK")


print("-----Features of Son1------")
S1=Son1()
S1.mobile()
S1.car()
S1.money()
S1.home()

print("-----Features of Son2------")
S2=Son2()
S2.laptop()
S2.car()
S2.money()
S2.home()


