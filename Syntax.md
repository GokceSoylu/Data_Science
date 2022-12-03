## Python genel bakış

### Ön bilgi
Tebrik ederim başarılar dilerim:))
Hocam öncelikle c/c++/java yazdıktan sonra python a geçişi biraz zor olabilir. genel özelliklerinden bahsedelim
komutların sonuna ; konulmaz
print fonksiyı-onu için kütüphaneye ihtiyaç yoktur
yorum satırı için # kullanılır
/ işareti ile bölme yaptığımızda float bölme yapar. int bölme yapmak için // işaretini kullanmalıyız
### Veri tipleri
integer, float, String gibi veri tipleri burada da var, ancak değişkenler tanımlanırken değiken tipi başına yazlımaz :))
````python
    a=10
    b=10.2
    c="leyla"
    d=[1,2,3,4]#liste
    e=[1,2,3,4,"kbu"]#liste bu c deki listeye stack yapısına benziyor
    f=(1,2,3,4,"kbu")#tuple --> touple ve list çok benziyor farkındayım kısaca touple değiştirilemez lisr değiştirilebilir.
    g={"Monday":1,"Thursday":2}#dictionary C'deki enum'a benziyor:))
    h=True
````
birde bunların hangi tipte olduklarını anlamammızı saglayan type() fonksiyonunu var.
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
class 'int'
class 'float'
class 'str'
class 'list'
class 'list'
class 'tuple'
class 'dict'
class 'bool'
> integer ve float
bunlaral alakalı çokta farklı bir şey bir aritmatik kısmında python / işaretir float bölme yapar, tam bölme için // işaretinin 
kullanırız. Float bölme dediğimiz c yada java daki gibi rakam rakam yazdırmak değildir. virgülden sonrai kısmı yuvarlar :))
````python
    a=10
    b=4
    c=a/b
    d=a//b
    e=d/2
    print(c)
    print(d)
    print(e)
````
output
2.5
2
1.0
> String
elma+elma evet python'da iki elma yapar :)). String birleştirmeyi direkt + ile yaapbiliriz. hatta * kullanarak bir stringi multiple 
yapabiliriz. peki ya / ve - işaretleri? Abartma o kadar değil :))
````python
    b="hasan"
    c="pasa"
    d=a+b
    e="besik"
    f="tas"
    h=e+f
    h*=3
    print(d,h)
````
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