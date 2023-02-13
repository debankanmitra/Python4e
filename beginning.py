
print("Hello world")

# division
print(9/2) # print true value , autoamtically converts value to float
print(9//2) # print only the integer part , also known as integer division or floor division

# concatenate 
print('DEBANKAN'+' MITRA')

# supports multiply of a string 
print(10*'DEBANKAN')

# output of the previous operation , we use _ in python
x=1
x+9
#print(_+10) # its working in shell btw

# Fetching a character from a string 
str='DEBANKAN'
print(str[-1])# -1 prints the last character 
print(str[1]) # that means here string is array of characters
print(str[0:2]) #IT PRINTS THE CHARACTER FROM ZERO UPTO 2 AND EXCLUDING 2
print(str[0:]) # it starts from 0 to the end 
print(str[:3]) # it start from first till 3
print(str[0:100]) # it will end upto the last available value but won't give any error

#changing the value of string 
print('MY'+str[2:])

# Length of string 
Surname='MITRA'
print(len(Surname))

#List in Python (LIST IS MUTABLE THAT MEANS WE CAN CHANGE VALUES)
nums=[11,22,33,44,55,66]
print(nums)
print(nums[-1])
print(nums[1:4])
print(nums[1])
#print(nums[0][0]) # IT IS GIVING ERROR BECAUSE STRING IS A LIST OF CHARACTERS BUT NUMBERS ARE NOT

#List of string
names=['raja','gaja','vaja','haja','maja']
print(names[1])
print(names[-1])
print(names[1][0])

mil=[nums,names]
print(mil)
print(mil[1][0][0]) # 3D ARRAY
print(mil+nums)

# ARRAY FUNCTIONS
# appending elements with the list
print(nums[0]+10)
#print(nums+10) #TypeError: can only concatenate list (not "int") to list
nums.append(19) #IN APPEND IT WILL ADD THE VALUE AT THE END
print(nums) # NO ERROR , THIS IS THE ACTUAL WAY 
nums.insert(0,81) # IN INSERT WE CAN INSERT THE VALUE IN ANY POSITION
print(nums)
nums.remove(22) # IN REMOVE WE USE THE ELEMENT ITSELF
print(nums)
print(nums.pop(0)) # IN POPS OUT THE SPECIFIC NUMBER ON THAT INDEX AND PRINT IT BUT REMOVE DOESNOT PRINT THE NUMBER
                   # IF WE DOESN'T SPECIFY INDEX IT WILL POP OUT LAST ELEMENT  
print(nums)

del nums[:2] # IT IS USED TO DELETE MULTIPLE VALUES
print(nums)

nums.extend([1,2,3,4,5]) # IT IS USED TO ADD MULTIPLE VALUES
print(nums)

print(max(nums)) #
print(min(nums)) # PRINT MAX AND MIN VALUE OF A LIST
print(sum(nums)) # PRINT SUM OF ALL THE VALUES

nums.sort() # SORT THE ARRAY ASCENDING ORDER
print(nums)
nums.reverse() # SORT IN DESCENDING ORDER
print(nums)

#TUPLE IN PYTHON (TUPLE IS IMMUTABLE)
# SINCE WE DON'T CHANGE VALUES IN TUPLE ITERATION BECOME FASTER IN TUPLE THAN LIST
#Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple. 

tup=(10,20,30,40)
print(tup[0])
#tup[0]=11 will not work
print(tup[0])

#SET IN PYTHON , IT NEVER FOLLOWS A SPECIFIC SEQUENCE
# Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
# it has a highly optimized method for checking whether a specific element is contained in the set.
# A set contains only unique elements 
# Indexing doesn't supported in set
s={19,3,14,95,78,5,13,88}
print(s)

# Dictionary in Python is an unordered collection of data values, used to store data values like a map, which,
# unlike other data types that hold only a single value as an element, Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimised.
# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

name={1:'Debankan',2:'[1,2,3,4]','naam': 'Geeks',7:''}
print(name['naam'])
print(name.get(11)) # IF THERE IS NO DATA IT WILL RETURN NONE

# Merge 2 list to form a Dictionary 
name=['Dev','Raja','Ram']
age=[22,33,44]
data=dict(zip(name,age))
print(data)
del data['Dev']
print(data)








