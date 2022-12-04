file=open("student","r")
arg=file.read()#tamammını okur
print(arg)
file.close

file=open("student","r")
arg=file.read(8)#ilk n elemanı okur
print(arg)
