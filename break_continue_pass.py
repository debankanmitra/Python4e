# break , continue known earlier 
# pass , continue does not exit the block of statement or break the program

for i in range(1,100):
    if i%5==0:
        pass # pass means if there is no  code ignre it , because we cant leave the space vacant 
    else:    # we actually use pass when we dont know what to write inside the block of statement for the time being
        print(i)

print('Done')    