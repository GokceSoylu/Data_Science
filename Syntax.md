## Python genel bakış

### Ön bilgi
Tebrik ederim başarılar dilerim:))
Hocam öncelikle c/c++/java yazdıktan sonra python a geçişi biraz zor olabilir. genel özelliklerinden bahsedelim
komutların sonuna ; konulmaz
print fonksiyı-onu için kütüphaneye ihtiyaç yoktur
yorum satırı için # kullanılır
### Veri tipleri
integer, float, String gibi veri tipleri burada da var, ancak değişkenler tanımlanırken değiken tipi başına yazlımaz :))
````python
    a=10
    b=10.2
    c="leyla"
    d=[1,2,3,4]
    e=[1,2,3,4,"kbu"]
    f=(1,2,3,4,"kbu")
    g={"Monday":1,"Thursday":2}
    h=True
````
birde bunların hangi tipte olduklarını anlamammızı saglayan type() fonksiyonunu kullanırız.
````python
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
    print(type(h))
````
output


### Yazdırma
print() fonksiyonu kullanılır. String yazdırmak için "içine" istenilen string yazılır.
````python
    print("hello World!)
````
%d %f gibi referanslara ihtiyaç yoktur. Bunun yanık sıra println deki gibi, ifadeler türler arasına + koymayada gerek yok. virgül yeterli
````python   
    print("mehmet")
    print(25)
    print("mehmet",25,"yasinda")
````
> sep fonksiyonu 
normalde print() virgül ile ayırdığımız ifadeler arasına boşluk koyarak yazdırır. set fonksiyonu kullanarak biz bunu değiştirebiliriz.
````python
    print("hasan","yalova'da","yasiyor")
    print("hasan","yalova'da","yasiyor",sep="*")
````
output
hasan yalova'da yasiyor
hasan*yalova'da*yasiyor
işte separete(boşluk)yerine bunu kullan demiş oluyoruz.
>.format fonsiyonu
bir nevi %d %f refaranslarına andırıyor.
````python
    print("{}+{} = {}".format(12,17,12+17))