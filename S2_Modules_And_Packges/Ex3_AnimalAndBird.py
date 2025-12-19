
# Approach1:  import moduleName
#             moduleName.fn()


print("----- function calling - Approach1------")
import Animal,Bird

Animal.fly()
Animal.colour()
print("----")
Bird.fly()
Bird.colour()


print("----- function calling - Approach2------")

from Animal import *
from Bird import *

fly()
colour()

