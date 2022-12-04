#remove append insert pop
#? mini özet remove ve append fonksiyonları parametre olarak string alır
#? pop ve insert fonksiyonları parametre olarak int alır
#todo remove(str) append(str) pop(int) insert(int,str)
list=["necmiye","soylu","sabriye","soylu","the queen","behice","soylu"]
list.remove("soylu") #ilkini siler :))
print(list)
list.append("soylu")#sona ekler
print(list)

list.pop()#indis yazmazasan son elemanı siler
print(list)

list.pop(2)
print(list)

list.insert(1,"soylu")
list.insert(3,"soylu")
print(list)