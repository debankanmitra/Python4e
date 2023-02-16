# Types of Arguments in Python
from lib2to3.pygram import pattern_symbols


def person(name,age): # formal arguments 
    print(name)
    print(age)


person('dev',20)  # actual arguments: these has itself 4 types: position,keyword,default,variable length
#person(20,'dev')  # this will create a problem because of postition mismatched
person(age=20,name='dev') # we can do this, we are using keywords here

def person(name,age=18): # here we using default
    print(name)
    print(age)

person('dev') 

# variable length
def sum(a,*b):
    c=a
    for i in b: # here other values of b forms a tuple
        c+=i

    print(c)
sum(12,11,1,3,56)    # first value will go to a and others to b


# KEYWORD ARGUMENTS **kwargs arguments but with their keywords
def person_details(name,**data): # ** helps tp take variable length arguments with their keywords
    print('name: ',name)
    for i,j in data.items():
        print(i,j)
person_details('dev',place='WB',mob=9222,age=82)

# Pass list to a function in python
def even_odd(a):
    even,odd=0,0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1 

    print('odd:',odd,'even:',even)
even_odd([11,22,33,44,55,66])               
         



