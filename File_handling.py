
# READ
f=open('data.txt','r')
#print(f.read()) # we use read to fetch the data
#print(f.readline()) # only read the first line
#print(f.readline(4)) # only read first 4 characters of the first line

# WRITE
f1=open('abc','w') # w means write, if the write file doesn't exist it will create it
#f1.write("WRITING AFTER WATCHING TELUSKO VIDEOS")

# APPEND
f2=open('mao','a')
#f2.write("APPENDING SOME MORE TEXT THE PREVIOUS TEXT WILL NOT LOST")

# WRITING DATA FROM DATA.TXT TO ABC
for data in f:
    f1.write(data)
    print(data)


