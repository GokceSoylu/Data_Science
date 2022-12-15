#sorted() sıralayan fonksiyon
liste=[(1,'b','x'),(6,'e',0),(2,'c',2),(4,'a',5),(5,'d','w')]
liste_new=sorted(liste, key=lambda x: x[1] ) #sırala ama her elemanın birinci indis eleman göre yaa çok güzel
print(liste_new[:])