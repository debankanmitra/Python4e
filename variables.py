
num=5
print(id(num)) # print the memory location where the num variable was created 
ida=55
idb=ida  # so heres the thing for two different varibales , if one variable pointing the other , two differnt boxes are not created but two variables point the same object so addresses will be also same 
print(id(ida))
print(id(idb))

#You cannot declare a variable or value as constant in Python.
#To indicate to programmers that a variable is a constant, one usually writes it in upper case
print(type(ida))

# Data Types in Python
number_a=6+9j
print(type(number_a))
number_b=30
number_c=float(number_b)
print(number_c)
print(number_b>12)

print(int(True)) # True is 1
print(int(False)) # False is 0

# RANGE AND LIST IN PYTHON
print(range(10))
print(list(range(10)))
print(list(range(1,20,2)))

# Different Data Type 
# none
# Numeric : int , float , complex , bool 
# Sequence : List ,Tuple , Set , Sring , Range 
# Mapping : Dictionary

# OPERATORS IN PYTHON
# assignment
a,b=2,3
print(a+b)
# unary: 
n=7
n=-n
print(n)
# comparison
print(a==b)

# logical operator
print(a<8 and b<2)
print(a<8 or b<2)
x=1
print(not x)

