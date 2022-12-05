import numpy as np
# Map
#Filter
#Reduce 
#—> yukarıda üç fonk lambda ile kullanılır ve vektörel işlem yapmayı sağlar

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
ab=[]
for itr in range(0,len(a)):
    ab.append(a[itr]*b[itr])            #burada ab ye indis gösterilmez append sırıyle ekler zaten
print(ab[:])

#numpy ssayesinde * ile vektorel çarpabliriz
aa=np.array([1,2,3,4,5,6])
bb=np.arry([1,2,3,4,5,6])
aabb=aa*bb
print(aabb[:])