class GrandFather:
   def home(self):
       print("1 BHK")

   def money(self):
       print("1 Lakh")


class Father(GrandFather):
   def home(self):         #Method overriding
       print("2 BHK")

   def money(self):          #Method overriding
       print("2 Lakh")


class Son(Father):
   def home(self):           #Method overriding
       print("3 BHK")

   def money(self):           #Method overriding
       print("3 Lakh")


f=Father()
f.home()
f.money()
print("-----")
s=Son()
s.home()
s.money()
