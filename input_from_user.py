import sys


x=int(input('Enter first number')) # by default input converts the input into string format , so we are chaning it to int
y=float(input('Enter second number'))
z=x+y
print(z)

a=input('enter a character')[0]
print(a)

# evaluate 
result=eval(input("enter expression")) # it will evaluate an expression passed on input
print(result)

# input from arguments from command line 
inputa=int(sys.argv[1]) # it will give you string but u have to convert it to int
inputb=int(sys.argv[1])
print(inputa+inputb)
