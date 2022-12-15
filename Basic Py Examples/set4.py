#intersection fonksiyonu iki künin kesişimi döndürür a.intersection(b) anb
#kesişimi  & operetörü ile de yapabiliriz a&b anb
#union iki kümeyi birleştirir ama tabi her elemandan bir kez olacak şekilde a.union(b) aUb
#birde intersection_update var burada da meetodu çalıştıran set, çalıştıran set ile parametre setin farkı  olur a.intersection_update(b) a=anb
a=set([1,2,3,4])
b=set([3,4,5,'e'])
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a&b)
a.intersection_update(b)
print(a)
b.intersection_update(a)
print(b)