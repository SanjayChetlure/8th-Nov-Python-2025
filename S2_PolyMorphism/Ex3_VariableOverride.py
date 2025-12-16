
#variable override

class parent:
   name="amol"

class child(parent):
   name="AMOL"       #variable override / reinitialization


childClassObj=child()
print(childClassObj.name)