counter = 0
for itr in range(0,5,1):
    n=str(input("name "))
    if n.startswith('e') and n.endswith('e'):
        counter+=1
print("ther are",counter,"name starting and ending with e")


#todo startswith ile başlıyor mu bool döndürür
#todo endswith ile bitiyor mu bool döndürür