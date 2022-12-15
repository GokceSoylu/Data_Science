#extend birleştirme
list=[1,'a',2,'b']
list2=[3,'c',4,'d']

list.extend(list2)
list.extend([5,'e'])
print(list)

list.extend(list)
print(list)

#index verilen elemanın kacıncı indexte olduğunu bulur. parametre olarak hem int hem string alabilir. hatırlarsın fonksiyonlarda zaten parametre tipi yazmıyorduk ne verse kabul
print("b nin indexi = ",list.index('b'))
print("4 ün indexi = ",list.index(4))

#reverse ters çeviren fonk :)
list.reverse()
print(list)
list.reverse()
print("tersin tersi düzdür :))")
print(list)

#sort fonksiyonu ancak sıralayabilmesi için listenin içinin aynı veri tiplerinden oluşması gerekir
list_int=[1,3,6,2,5,7,4]
list_char=['d','a','b','e','c','f']

list_int.sort()
list_char.sort()
print(list_int)
print(list_char)

print()
print(list,list2,list_int,list_char,sep=(' <> '))