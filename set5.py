#isdisjoint iki kümenin kesimi boş mu diye sorar boşsa true döner
#issupset çalıştıran parametrenin alt kümesi mi a.issupset(b)  a<b a alt küme b mi
#issuperseet çalıştıren paremetreyi kapsar mı a.issuperset(b) a>b a kapsar b mi
tuple=1,2,3,'a','b','c'
list=[1,2,'a']
set0=set([10,11,12])
set1=set(tuple)
set2=set(list)
if(set0.isdisjoint(set1)):
    print("set0 ve set1 in ortak elemanı yoktur")
if(set2.issubset(set1)):
    print("set2 set1 in alt kümesidir")
if(set1.issuperset(set2)):
    print("set1 set2 yi kapsar")

#not set lere tuple gönderebiliriz. peki tuple değiştirilemiyordu set ise değiştirilebiliyor nasıl olacak?
#zaten tuple değiştirmiyoruz. tuple ı kopyalayıp seti oluşturuyoruz. seti değiştiriyoruz tuple etkilenmiyor