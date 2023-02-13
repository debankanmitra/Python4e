from sys import argv


if 3%2==0:
    print('ODD')
else:   
    if 3>2:
        print('GREATER')
    print('EVEN')    

print('BYE')

# ELIF
x=int(argv[1])
if x==1:
    print(x)
elif x==2:
    print(x)
else:
    print(x)    


# while loop
i=1
while i<10:
    print("DEBANKAN",end=' ') # end prints on same line
   # i++ #Python does not have unary increment/decrement operator( ++/--)
    i=i+1

# FOR LOOP
name='DEBANKAN'
for i in name: # i takes each value from name 
     print(i," ",'9')


for i in range(10,100,10):
    print('value:',i)

# reverse loop
for i in range(100,10,-10):
    print('value:',i)


# for - else loop

nums=[10,23,44,65]

for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print('not found')        
