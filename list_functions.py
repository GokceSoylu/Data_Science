list=[] #aşşağıda direkt kullanacağım için tanımlamam gerekti
counter_a=0
n=int(input("how many argumants are there in the list "))
for itr in range (0,n,1):
    list.append(str(input("name ")))
    control=list[itr]
    if control[0]=='a':
        counter_a+=1
print(counter_a,"kelime a ile basliyor")

#todo appaned fonsiyonu listenin sonuna eleman eklemek için kullanılır