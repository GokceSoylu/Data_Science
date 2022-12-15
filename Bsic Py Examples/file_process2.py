file=open("student","r")
for line in file:
    print(line)
file.close

file=open("student","r")
lines=[]
lines=[line_ for line_ in file] # tuhaf değişk ancak boylede atam şekli var
print(lines[:])
file.close