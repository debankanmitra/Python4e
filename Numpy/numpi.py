import numpy as np

# Linespace is used to create an array with evenly spaced numbers between a start point and a stop point 
print(np.linspace(1,1.5))  # it will create an array of 50 evenly spaced parts between 1 and 2
print(np.linspace(1,8,5,endpoint=True))
print(np.linspace(1,8,5,endpoint=False)) # 8 will not be included

# get dimension
a=np.array([[1,2,3,0,8,6,4,2],[4,7,2,1,4,5,6,9]],dtype='int16')
print('dimension',a.ndim)

# shape of matrix
print('shape',a.shape)

# type 
print('type ',a.dtype) # because we have mentioned the dtype as 'int16'

# itemsize in bytes
print(a.itemsize,'bytes')

# total size
print(a.nbytes) # a.size * a.itemsize

# accessing specific element
print('accessing specific element',a[0][1]) # use a[0,1] instead

# accessing specific row
print('accessing specific column',a[0,:]) # 0th row , all the columns

# accessing specific column
print('accessing specific element',a[:,2]) # all the row , 2nd column

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0,1:5:2])
print(a[0,1:5:1])

print('-----------------------------------------------------------------------------------------------------')
# 3-D ARRAYS
b=np.array([[[2,3,4],[3,4,5]],[[3,4,6],[9,6,1]]])
print(b)
print('shape',b.shape)
print('dimension',b.ndim)

# accessing specific element
print('accessing specific element',b[0,1,2])

# Getting a little more fancy
print(b[:,0,1]) # its working like select all the elements of all row > select 0th row of those element>select 1 column of those row

# replace 
print('element',b[:,0,:])
b[:,0,:]=[[2,2,2],[9,9,9]]
print('array',b)

print('------------------------------------------------------------------------------------------------------------')
#all 0's matrix
print(np.zeros((2,3)))

# all 1's
print(np.ones((2,3),dtype='int16'))

# any other number
print(np.full((2,2),99,dtype='float32')) # np.full((size,size),value)

# full_like
print(np.full_like(a,4)) # it will create a same size array like a , with value 4

# random decimal numbers
print('random',np.random.random_sample(a.shape))
print('random',np.random.rand(2,2)) # 2,2 is the size

# Random integer values
print('random integer',np.random.randint(1,4,size=(3,3))) # starts from 1 with exclusive 4

# identity matrix ( basically going to be a square matrix with 1 diagonally)
print('identity',np.identity(4,dtype='int8')) # size = 4

# repeat an array given times
arr=np.array([1,2,3])
print('repeat',np.repeat(arr,3)) # 111222333

arr=np.array([[1,2,3]])
print('repeat',np.repeat(arr,3,axis=0)) # it will repeat the row at 0th axis

# Q. 1 1 1 1 1   make this matrix with above functions
#    1 0 0 0 1
#    1 0 9 0 1
#    1 0 0 0 1
#    1 1 1 1 1
print('QUESTIONS')
ar1=np.ones((5,5))
ar2=np.zeros((3,3))
ar2[1,1]=9
ar1[1:4,1:4]=ar2
print(ar1)

# make an array direct copy of another array
arr1=np.array([1,2,3])
arr2=arr1 # change the value in arr2 will also change in value of arr1 , for this we can use arr1.copy()
print('arr2 is',arr2)

# addition
print('addition',arr1+2)

# substraction
print('substraction',arr1-2)

# multiplication
print('addition',arr1*2)

# division
print('addition',arr1/2)
arr1+=2
print(arr1)

# exponential
print('exponential',arr1**2)

# take the sin
print('sin',np.sin(a))

# matrix multiplication
print('matmul is',np.matmul(arr1,arr2))

print('--------------------------------------------------------------------------------------------------')
# STATISTICS
stats=np.array([[12,13,14],[11,22,33]])
print('mean',np.mean(stats[1]))
print('median',np.median(stats[1]))
print('minimum',np.min(stats[:,1]))
print('maximum',np.max(stats[:,1]))
print('summation',np.sum(stats[:,1]))

print('--------------------------------------------------------------------------------------------------')
# REORGANIZING ARRAYS 
before=np.array([[12,13,14],[11,22,33]])
print('reshaping',before.reshape(2,3))

# vertically stacking vectors
v1=np.array([[12,13,14],[11,22,33]])
v2=np.array([[14,10,4],[11,22,33]])
print('vertically stacking',np.vstack([v1,v1,v2,v2]))

# horizontally stacking vectors
v1=np.array([[12,13,14],[11,22,33]])
v2=np.array([[14,10,4],[11,22,33]])
print('horizonatally stacking',np.hstack([v1,v1,v2,v2]))

# creating a matrix
m=np.matrix('1 2 3;3 4 5;6 7 8')
print('matrix',m)

# faltten an array
print(m.flatten())



