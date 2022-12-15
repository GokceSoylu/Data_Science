a={"east":0,"west":1,"north":3,"south":4}
print(a["east"])
print(a["north"])
a["west"]=10
print(a["west"])             
#hocam burada anahtarlarımız string ifadelerimiz, tuttuğu değerler ise yanına yazdığımız değerler oluyor.
#c ve java daki enum'a ile karıştırmayalım. bu sabit değil bir defa :))
#adı üztünd bu bir sözlük bunun karşılığı bu şeklinde belirtiyoruz okadar :))

#bunda isteğimiz tipleri kullanmakta özgürüz mezu bir anahtar ve değer şeklinde olması. değer istersek liste olur istersek tek bir int fark etmez
#özgürüz derken açıklamaya her şey olur ama key varaible olamaz sabit olmalı. bu yüzden tuple olabilri
dic={"REG":"regresyon modeli ", "LOJ":"lojistic regresyon", "CART":"classification and Reg"}
print(dic["LOJ"])

dic2={102:["cpe",100],101:["cpe",30],100:["cpe",30,2]}
print(dic2[100])
print(dic2[102])
#yani listenin farkı tuple ve liste gibi indisle çağirmek yerine[key_word] ilre çağiriyoruz

#listede tuple da olduğğu gibi nurada da matris yapısı uygun
dic_eng={"cp":{102:["cpe",100],101:["cpe",30],100:["cpe",30,2]},
        "mach" :{102:["mach",100],101:["mach",30],100:["mach",30,2]},
        "elec":{102:["elec",100],101:["elec",30],100:["elec",30,2]}}

print(dic_eng["mach"][102])
 
#sonrada değiştirilebilr ekelenebilir
dic_eng["hmn"]=102

