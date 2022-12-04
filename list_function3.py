list=[0,1,2,3,4,5,6,7,8,9,10]
while True:
    indis=int(input("which number do yoou want to delete "))
    if not (indis%2==0):
        list.pop(indis)
        print("if bloğu",indis)
    else:
        list.pop()
        print("else bloğu",indis)
    print(list[indis])
    key=int(input("to exit please enter 0"))
    if key==0:
        break
print(list[:])

#todo pop fonsiyonu eğer indis belirtirsen indisteki sayıyı siler belirtmessen listenin sonundakini siler