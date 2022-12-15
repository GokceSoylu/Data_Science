list=["ali_","ata_"]
set=set(list)
print(set)
set.add("bak")
print(set)

set.add("ali")
set.add("ali") #ayni argümanı eklemeye çelıştığımızdda hata almayız sadece eklemez :))
print(set)

set.remove("ali")
# set.remove("ali") remove fonksiyonu vrilen parametreyi bulamazsa hata fırlatır
set.discard("ali")#discard fonksiyonu silinecek elemanı set in içerisinde bulamazsa hata vaermez
print(set)