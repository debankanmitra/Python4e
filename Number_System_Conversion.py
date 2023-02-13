print(bin(25))
print(0b11001)
print(oct(25))
print(hex(25))

# SWAPPING TWO VALUES WITHOUT USING TEMP VARIABLE
a=6
b=3
a=a+b
b=a-b # 9-3
a=a-b # 9-6
print(a)
print(b)
a,b=b,a # two values of a,b go to the stack and then it reverse, it uses concept of rotation 
