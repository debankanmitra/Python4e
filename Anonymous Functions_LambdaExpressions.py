# this type of function we are gonna use only once and we don't wanna define any name
# this are anonymous function 
# Lambda functions are used when you need a function for a short period of time. 
# This is commonly used when you want to pass a function as an argument to higher-order 
# functions, that is, functions that take other functions as their arguments

# normal function
from functools import reduce


def square(a):
    return a*a
print(square(5))

# lambda function/ anonymous function
square =lambda a : a*a
print(square(5))

f =lambda a,b : a*b
print(f(5,7))

# where we use lambda funcrions? [filer,map , reduce]
#is_even =lambda e: e%2==0

nums=[1,2,3,4,5,6,7,8]
#evens= list(filter(is_even,nums))
evens= list(filter(lambda e: e%2==0,nums))
print(evens)
doubles=list(map(lambda n : 2*n,evens))
print(doubles)
sum=reduce(lambda a,b : a+b , doubles)
print(sum)

