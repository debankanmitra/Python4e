import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def greet(): # function calling itself is known as recursion
    print('hello')
    greet()

#greet()    

# 5! USING RECURSION

def factorial(a):
    if a==0:
        return 1
    return a * factorial(a-1) # it is working like 5*4*factorail(4-1).....
                            # return 5*4*3*2*1*1

result=factorial(5)
print(result)    