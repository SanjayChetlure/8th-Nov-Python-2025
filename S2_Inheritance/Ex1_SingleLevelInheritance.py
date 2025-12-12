# Example1: Single level Inheritance

#super/parent/base class
class Father:
    def car(self):
        print("Car: Tata")

    def money(self):
        print("Money: 1L")

    def home(self):
        print("home: 2BHK")

#sub/child class
class Son:
    def mobile(self):
        print("Mobile: Samsung")

    # def car(self):
    #     print("Car: Tata")
    #
    # def money(self):
    #     print("Money: 1L")
    #
    # def home(self):
    #     print("home: 2BHK")



s=Son()
s.mobile()
s.car()
s.money()
s.home()

