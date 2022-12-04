# diffarance method a.diffarnde(b) a/b a fark b döner
#symmetric_differnce a.symeetric_difference(b) a/b U b/b döner 
#hatta set(küme)de fark işlemlerini direjt - ilede yapaliriz

a=set([1,2,3,4])
b=set([2,3,4,5])
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))