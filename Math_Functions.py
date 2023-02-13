import math
import math as debu #this is alias , instead of math we can use debu.functions()
from math import sqrt,pow # if we want to import only specific funtions

x=math.sqrt(23)
print(x)

print(math.floor(x))
print(math.ceil(x))

# pow
print(math.pow(3,3)) # when you we are working on a big software it is better to use
                     # functions because it is more readable
print(3**3)

# after alias
print(debu.sqrt(339))
