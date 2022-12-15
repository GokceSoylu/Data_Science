#neler yapıyorduk file open r w a r+ w+
# read() write() 
file =open("student","w")
n=int(input("how many student are there "))
for i in range(0,n,1):
    file.write(input("number "))
    file.write(input("name "))
    file.write("\n")
file.close