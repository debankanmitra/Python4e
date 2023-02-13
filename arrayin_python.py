
from array import array # this package doesn't use multidimensional array for this we can use third party package numpy
import numpy as np
vals = array('i', [1, -2, 3,7,4]) # Typecode: 'i' means signed int for more search for type code array in python

print(vals)
print(vals.buffer_info()) # address size_of_array
vals.reverse()
print(vals[0])


for i in range(len(vals)):
    print(vals[i])

# OR

for i in vals:
    print(i)

# https://youtu.be/6a39OjkCN5I
# vid: 13:00    

# Input from user
#arr=array('i',[])

#n=int(input('size of array'))

#for i in range(n):
#    x=int(input('Enter next value'))
#    arr.append(x)

#print(arr)

a=np.array([['a','b','c','f','g'],[1,3,4,5,6]]) # in numpy typecode is optional
print(a)

array1=np.array([1,2,3,4,5,6,7])
print(array1)
print(array1.dtype)

array2=np.array([1,2,3,4,5.8,6,7],int) # for 1 float value , whole array will be converted to float to avoid these we have to mention int
print(array2)
print(array2.dtype)


